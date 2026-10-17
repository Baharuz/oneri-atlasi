import os
from datetime import timedelta
from fastapi import FastAPI, Depends, HTTPException, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr, Field, field_validator
from sqlalchemy import select, delete
from sqlalchemy.orm import Session
from pwdlib import PasswordHash
from itsdangerous import URLSafeTimedSerializer, BadSignature, SignatureExpired
from .db import get_db
from .models import User, Content, Interaction, RecommendationRun
from .recommend import recommend

app = FastAPI(title="Öneri Atlası API")
origin = os.getenv("FRONTEND_ORIGIN", "http://localhost:5173")
app.add_middleware(CORSMiddleware, allow_origins=[origin], allow_credentials=True, allow_methods=["GET", "POST", "PUT", "DELETE"], allow_headers=["Content-Type", "X-CSRF-Token"])
hasher = PasswordHash.recommended()
serializer = URLSafeTimedSerializer(os.getenv("SESSION_SECRET", "dev-only-change-me"))
COOKIE_SECURE = os.getenv("COOKIE_SECURE", "false").lower() == "true"
COOKIE_SAMESITE = os.getenv("COOKIE_SAMESITE", "lax")
CATEGORIES = {"kitap", "film", "dizi", "oyun", "müzik"}

class AuthInput(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)

class Answers(BaseModel):
    features: list[str] = Field(default_factory=list, max_length=20)
    moods: list[str] = Field(default_factory=list, max_length=10)
    mode: str = "close"
    categories: list[str] = Field(default_factory=lambda: list(CATEGORIES))
    @field_validator("mode")
    @classmethod
    def mode_valid(cls, value):
        if value not in {"close", "discover", "surprise"}: raise ValueError("Geçersiz tercih")
        return value
    @field_validator("categories")
    @classmethod
    def categories_valid(cls, value):
        if not value or not set(value) <= CATEGORIES: raise ValueError("Geçersiz kategori")
        return list(dict.fromkeys(value))

class RecommendInput(BaseModel):
    source_ids: list[int] = Field(min_length=1, max_length=5)
    answers: Answers = Field(default_factory=Answers)

class ProfileInput(Answers):
    source_ids: list[int] = Field(default_factory=list, max_length=5)

class FeedbackInput(BaseModel):
    kind: str

def current_user(request: Request, db: Session = Depends(get_db)):
    token = request.cookies.get("session")
    if not token: raise HTTPException(401, "Giriş yapmalısınız")
    try: user_id = serializer.loads(token, max_age=60 * 60 * 24 * 7)
    except (BadSignature, SignatureExpired): raise HTTPException(401, "Oturum geçersiz")
    user = db.get(User, user_id)
    if not user: raise HTTPException(401, "Kullanıcı bulunamadı")
    return user

def optional_user(request: Request, db: Session):
    try: return current_user(request, db)
    except HTTPException: return None

def csrf(request: Request):
    if request.method in {"POST", "PUT", "DELETE"} and request.cookies.get("session"):
        cookie = request.cookies.get("csrf")
        header = request.headers.get("X-CSRF-Token")
        if not cookie or not header or cookie != header: raise HTTPException(403, "CSRF doğrulaması başarısız")
        if request.headers.get("origin") != origin: raise HTTPException(403, "Kaynak doğrulaması başarısız")

def set_cookies(response: Response, user_id: int):
    import secrets
    response.set_cookie("session", serializer.dumps(user_id), httponly=True, secure=COOKIE_SECURE, samesite=COOKIE_SAMESITE, max_age=604800)
    response.set_cookie("csrf", secrets.token_urlsafe(32), httponly=False, secure=COOKIE_SECURE, samesite=COOKIE_SAMESITE, max_age=604800)

def content_dict(item):
    return {field: getattr(item, field) for field in ("id", "category", "title", "description", "genres", "themes", "moods", "language", "year", "image_url", "source", "source_id")}

@app.get("/api/health")
def health(): return {"ok": True}

@app.post("/api/auth/register")
def register(data: AuthInput, response: Response, db: Session = Depends(get_db)):
    email = data.email.lower()
    if db.scalar(select(User).where(User.email == email)): raise HTTPException(409, "Bu e-posta zaten kayıtlı")
    user = User(email=email, password_hash=hasher.hash(data.password), preferences={})
    db.add(user); db.commit(); db.refresh(user); set_cookies(response, user.id)
    return {"id": user.id, "email": user.email, "preferences": user.preferences}

@app.post("/api/auth/login")
def login(data: AuthInput, response: Response, db: Session = Depends(get_db)):
    user = db.scalar(select(User).where(User.email == data.email.lower()))
    if not user or not hasher.verify(data.password, user.password_hash): raise HTTPException(401, "E-posta veya şifre hatalı")
    set_cookies(response, user.id)
    return {"id": user.id, "email": user.email, "preferences": user.preferences}

@app.post("/api/auth/logout", dependencies=[Depends(csrf)])
def logout(response: Response):
    response.delete_cookie("session"); response.delete_cookie("csrf")
    return {"ok": True}

@app.get("/api/me")
def me(user: User = Depends(current_user), db: Session = Depends(get_db)):
    interactions = db.scalars(select(Interaction).where(Interaction.user_id == user.id)).all()
    return {"id": user.id, "email": user.email, "preferences": user.preferences, "favorites": [x.content_id for x in interactions if x.kind == "favorite"], "feedback": {x.content_id: x.kind for x in interactions if x.kind in {"like", "dislike"}}}

@app.put("/api/me/preferences", dependencies=[Depends(csrf)])
def save_preferences(data: ProfileInput, user: User = Depends(current_user), db: Session = Depends(get_db)):
    if len(set(data.source_ids)) != len(data.source_ids): raise HTTPException(422, "Tekrarlı kaynak")
    if data.source_ids:
        found = db.scalars(select(Content.id).where(Content.id.in_(data.source_ids))).all()
        if len(found) != len(data.source_ids): raise HTTPException(422, "İçerik bulunamadı")
    user.preferences = data.model_dump()
    for content_id in data.source_ids:
        existing = db.scalar(select(Interaction).where(Interaction.user_id == user.id, Interaction.content_id == content_id, Interaction.kind == "favorite"))
        if not existing: db.add(Interaction(user_id=user.id, content_id=content_id, kind="favorite"))
    db.commit()
    return {"preferences": user.preferences}

@app.get("/api/contents")
def contents(q: str = "", category: str | None = None, db: Session = Depends(get_db)):
    stmt = select(Content)
    if category:
        if category not in CATEGORIES: raise HTTPException(422, "Geçersiz kategori")
        stmt = stmt.where(Content.category == category)
    if q: stmt = stmt.where(Content.title.ilike(f"%{q[:80]}%"))
    return [content_dict(x) for x in db.scalars(stmt.order_by(Content.title).limit(100)).all()]

@app.get("/api/contents/{content_id}")
def content_detail(content_id: int, db: Session = Depends(get_db)):
    item = db.get(Content, content_id)
    if not item: raise HTTPException(404, "İçerik bulunamadı")
    return content_dict(item)

@app.post("/api/recommend", dependencies=[Depends(csrf)])
def recommendations(data: RecommendInput, request: Request, db: Session = Depends(get_db)):
    if len(set(data.source_ids)) != len(data.source_ids): raise HTTPException(422, "Tekrarlı kaynak")
    sources = db.scalars(select(Content).where(Content.id.in_(data.source_ids))).all()
    if len(sources) != len(data.source_ids): raise HTTPException(422, "İçerik bulunamadı")
    all_contents = db.scalars(select(Content)).all()
    allowed = set().union(*(set(x.themes + x.moods + x.genres) for x in sources))
    if not set(data.answers.features) <= allowed: raise HTTPException(422, "Seçilen özellik kaynak içeriklerde yok")
    user = optional_user(request, db)
    feedback = {}
    if user:
        feedback = {x.content_id: x.kind for x in db.scalars(select(Interaction).where(Interaction.user_id == user.id, Interaction.kind.in_(["like", "dislike"]))).all()}
    result = recommend(all_contents, sources, data.answers.model_dump(), user.preferences if user else None, feedback)
    output = {category: [{"content": content_dict(x["content"]), "score": x["score"], "reason": x["reason"]} for x in rows] for category, rows in result.items()}
    if user:
        db.add(RecommendationRun(user_id=user.id, request_data=data.model_dump(), results={k: [x["content"]["id"] for x in v] for k, v in output.items()})); db.commit()
    return output

@app.put("/api/me/contents/{content_id}/{kind}", dependencies=[Depends(csrf)])
def interaction(content_id: int, kind: str, user: User = Depends(current_user), db: Session = Depends(get_db)):
    if kind not in {"favorite", "like", "dislike"}: raise HTTPException(422, "Geçersiz işlem")
    if not db.get(Content, content_id): raise HTTPException(404, "İçerik bulunamadı")
    if kind in {"like", "dislike"}:
        db.execute(delete(Interaction).where(Interaction.user_id == user.id, Interaction.content_id == content_id, Interaction.kind.in_(["like", "dislike"])))
    existing = db.scalar(select(Interaction).where(Interaction.user_id == user.id, Interaction.content_id == content_id, Interaction.kind == kind))
    if not existing: db.add(Interaction(user_id=user.id, content_id=content_id, kind=kind))
    db.commit(); return {"ok": True}

@app.delete("/api/me/contents/{content_id}/{kind}", dependencies=[Depends(csrf)])
def remove_interaction(content_id: int, kind: str, user: User = Depends(current_user), db: Session = Depends(get_db)):
    if kind not in {"favorite", "like", "dislike"}: raise HTTPException(422, "Geçersiz işlem")
    db.execute(delete(Interaction).where(Interaction.user_id == user.id, Interaction.content_id == content_id, Interaction.kind == kind)); db.commit()
    return {"ok": True}

@app.get("/api/me/history")
def history(user: User = Depends(current_user), db: Session = Depends(get_db)):
    runs = db.scalars(select(RecommendationRun).where(RecommendationRun.user_id == user.id).order_by(RecommendationRun.created_at.desc()).limit(20)).all()
    return [{"id": x.id, "created_at": x.created_at, "request": x.request_data, "results": x.results} for x in runs]
