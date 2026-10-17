import os
os.environ["DATABASE_URL"] = "sqlite+pysqlite:///:memory:"
os.environ["FRONTEND_ORIGIN"] = "http://localhost:5173"
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from app.db import Base, get_db
from app.catalog import seed
from app.main import app
from app.models import Content
from app.recommend import recommend

engine = create_engine("sqlite+pysqlite:///:memory:", connect_args={"check_same_thread": False}, poolclass=StaticPool)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
with Session() as db: seed(db)
def override_db():
    with Session() as db: yield db
app.dependency_overrides[get_db] = override_db

def client(): return TestClient(app, headers={"Origin":"http://localhost:5173"})
def csrf_headers(c): return {"X-CSRF-Token":c.cookies.get("csrf","")}

def test_catalog_and_cross_category():
    c=client()
    source=next(x for x in c.get('/api/contents').json() if x['title']=='Dune')
    result=c.post('/api/recommend',json={'source_ids':[source['id']],'answers':{'categories':['film','oyun']}}).json()
    assert result['film'] and result['oyun']
    assert all(x['content']['id']!=source['id'] for rows in result.values() for x in rows)
    assert all(x['reason'] for rows in result.values() for x in rows)

def test_feature_changes_ranking():
    with Session() as db:
        contents=db.query(Content).all()
        source=next(x for x in contents if x.title=='Küçük Prens')
        friendship=recommend(contents,[source],{'features':['dostluk'],'categories':['oyun']})['oyun']
        exploration=recommend(contents,[source],{'features':['keşif'],'categories':['oyun']})['oyun']
        assert friendship[0]['content'].id != exploration[0]['content'].id

def test_user_isolation_persistence_and_ephemeral_answers():
    a,b=client(),client()
    assert a.post('/api/auth/register',json={'email':'a@example.com','password':'password123'}).status_code==200
    assert b.post('/api/auth/register',json={'email':'b@example.com','password':'password123'}).status_code==200
    source=next(x for x in a.get('/api/contents').json() if x['title']=='Dune')
    assert a.put(f"/api/me/contents/{source['id']}/favorite",headers=csrf_headers(a)).status_code==200
    assert a.put('/api/me/preferences',json={'features':['siyasi entrika'],'categories':['film'],'source_ids':[source['id']]},headers=csrf_headers(a)).status_code==200
    assert a.post('/api/recommend',json={'source_ids':[source['id']],'answers':{'features':['ayrıntılı evren'],'categories':['film']}},headers=csrf_headers(a)).status_code==200
    assert a.get('/api/me').json()['preferences']['features']==['siyasi entrika']
    assert a.get('/api/me').json()['preferences']['source_ids']==[source['id']]
    assert b.get('/api/me').json()['favorites']==[]
    assert b.get('/api/me/history').json()==[]
    assert a.post('/api/auth/logout',headers=csrf_headers(a)).status_code==200
    assert a.post('/api/auth/login',json={'email':'a@example.com','password':'password123'}).status_code==200
    assert source['id'] in a.get('/api/me').json()['favorites']
    assert a.get('/api/me/history').json()
    assert a.put(f"/api/me/contents/{source['id']}/like",headers=csrf_headers(a)).status_code==200
    assert a.put(f"/api/me/contents/{source['id']}/dislike",headers=csrf_headers(a)).status_code==200
    assert a.get('/api/me').json()['feedback'][str(source['id'])]=='dislike'
    assert a.put(f"/api/me/contents/{source['id']}/favorite").status_code==403
