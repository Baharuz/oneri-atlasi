import json

import httpx
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.catalog_candidates import collect_candidates, load_targets
from app.db import Base
from app.models import Content

MOVIES = {"results": [
    {"id": 550, "title": "Dövüş Kulübü", "release_date": "1999-10-15", "poster_path": "/pB8BM7pdSp6B6Ih7QZ4DrQ3PmJK.jpg"},
    {"id": 680, "title": "Ucuz Roman", "release_date": "1994-09-10", "poster_path": None},
    {"id": 13, "title": "Forrest Gump", "release_date": "1994-06-23", "poster_path": "/arw2vcBveWOVZr6pxd9XTd1TdQa.jpg"},
    {"id": 14, "title": "Dördüncü", "release_date": "2001-01-01", "poster_path": "/dorduncu.jpg"},
]}

TV = {"results": [
    {"id": 1396, "name": "Breaking Bad", "first_air_date": "2008-01-20", "poster_path": "/ggFHVNu6YYI5L9pCfOacjizRGt.jpg"},
    {"id": 1399, "name": "Game of Thrones", "first_air_date": "2011-04-17", "poster_path": None},
]}

GAMES = {"results": [
    {"id": 3498, "name": "Grand Theft Auto V", "released": "2013-09-17", "slug": "grand-theft-auto-v", "background_image": "https://media.rawg.io/media/games/456/456f3c0a3b1b2f6f5c5e5e5e.jpg"},
    {"id": 3328, "name": "Kısa Ad", "released": None, "slug": "kisa-ad", "background_image": "http://media.rawg.io/media/games/http-only.jpg"},
    {"id": 4200, "name": "Portal 2", "released": "2011-04-18", "slug": "portal-2", "background_image": "https://media.rawg.io/media/games/2/portal.jpg"},
    {"id": 4300, "name": "Fazla", "released": "2020-01-01", "slug": "fazla", "background_image": "https://media.rawg.io/media/games/fazla.jpg"},
]}

def _client(payload, status=200, capture=None, error=None):
    def handler(request):
        if error is not None: raise error
        if capture is not None: capture.append(request)
        return httpx.Response(status, json=payload)
    return httpx.Client(transport=httpx.MockTransport(handler), timeout=5.0)

@pytest.fixture()
def db():
    engine = create_engine("sqlite+pysqlite:///:memory:", connect_args={"check_same_thread": False}, poolclass=StaticPool)
    Base.metadata.create_all(engine)
    with sessionmaker(bind=engine)() as session:
        for index, (category, title) in enumerate((("film", "Dövüş Kulübü"), ("dizi", "Breaking Bad"), ("oyun", "GTA V"), ("kitap", "Bir Kitap"))):
            session.add(Content(category=category, title=title, description="Elle yazılmış açıklama.", genres=[], themes=[], moods=[], source="local", source_id=f"{category}-{index+1}"))
        session.commit()
        yield session
        session.rollback()

def test_film_candidates_parse(db):
    capture = []
    payload = collect_candidates(db, category="film", tmdb_token="test-token", client=_client(MOVIES, capture=capture), delay=0)
    assert len(payload["results"]) == 1 and not payload["errors"]
    candidates = payload["results"][0]["candidates"]
    assert len(candidates) == 3
    first = candidates[0]
    assert first == {"provider": "tmdb", "provider_id": "550", "title": "Dövüş Kulübü", "year": 1999,
                     "image_url": "https://image.tmdb.org/t/p/w500/pB8BM7pdSp6B6Ih7QZ4DrQ3PmJK.jpg",
                     "page_url": "https://www.themoviedb.org/movie/550"}
    assert candidates[1]["image_url"] is None and candidates[1]["page_url"] == "https://www.themoviedb.org/movie/680"
    assert capture[0].url.path == "/3/search/movie" and capture[0].headers["authorization"] == "Bearer test-token"
    assert "test-token" not in json.dumps(payload)
    assert not db.dirty and not db.new

def test_dizi_candidates_parse(db):
    capture = []
    payload = collect_candidates(db, category="dizi", tmdb_token="test-token", client=_client(TV, capture=capture), delay=0)
    candidates = payload["results"][0]["candidates"]
    assert capture[0].url.path == "/3/search/tv"
    assert candidates[0]["title"] == "Breaking Bad" and candidates[0]["year"] == 2008
    assert candidates[0]["page_url"] == "https://www.themoviedb.org/tv/1396"
    assert candidates[1]["image_url"] is None

def test_oyun_candidates_parse(db):
    capture = []
    payload = collect_candidates(db, category="oyun", rawg_key="rawg-secret", client=_client(GAMES, capture=capture), delay=0)
    candidates = payload["results"][0]["candidates"]
    assert len(candidates) == 3
    assert capture[0].url.host == "api.rawg.io" and capture[0].url.path == "/api/games"
    assert capture[0].url.params["page_size"] == "3"
    assert capture[0].url.params["key"] == "rawg-secret"
    assert candidates[0] == {"provider": "rawg", "provider_id": "3498", "title": "Grand Theft Auto V", "year": 2013,
                             "image_url": "https://media.rawg.io/media/games/456/456f3c0a3b1b2f6f5c5e5e5e.jpg",
                             "page_url": "https://rawg.io/games/grand-theft-auto-v"}
    assert candidates[1]["year"] is None and candidates[1]["image_url"] is None  # http:// görsel reddedilir
    assert "http-only" not in json.dumps(payload)
    assert "rawg-secret" not in json.dumps(payload) and "rawg.io/api" not in json.dumps(payload)

def test_missing_keys_make_no_requests(db):
    def handler(request):
        raise AssertionError("anahtar yokken istek atılmamalı")
    client = httpx.Client(transport=httpx.MockTransport(handler), timeout=5.0)
    payload = collect_candidates(db, client=client, delay=0)
    assert payload["results"] == []
    errors = json.dumps(payload["errors"], ensure_ascii=False)
    assert "TMDB_READ_TOKEN tanımlı değil" in errors and "RAWG_API_KEY tanımlı değil" in errors
    assert len(payload["errors"]) == 2

def test_provider_errors_are_sanitized(db):
    status_error = collect_candidates(db, category="film", tmdb_token="gizli-token", client=_client({"detail": "auth"}, status=500), delay=0)
    entry = status_error["errors"][0]
    assert entry["provider"] == "tmdb" and "HTTP 500" in entry["error"]
    dumped = json.dumps(status_error, ensure_ascii=False)
    assert "gizli-token" not in dumped and "api.themoviedb.org" not in dumped

    timeout_payload = collect_candidates(db, category="oyun", rawg_key="gizli-key", client=_client(None, error=httpx.ConnectTimeout("zaman aşımı")), delay=0)
    timeout_entry = timeout_payload["errors"][0]
    assert timeout_entry["provider"] == "rawg" and "zaman aşımı" in timeout_entry["error"]
    dumped = json.dumps(timeout_payload, ensure_ascii=False)
    assert "gizli-key" not in dumped and "rawg.io" not in dumped and "zaman aşımı" not in dumped.replace(timeout_entry["error"], "")

def test_filters_and_request_counts(db):
    capture = []
    assert [c.category for c in load_targets(db)] == ["film", "dizi", "oyun"]
    assert [c.source_id for c in load_targets(db, category="oyun")] == ["oyun-3"]
    assert [c.source_id for c in load_targets(db, source_id="dizi-2")] == ["dizi-2"]
    with pytest.raises(ValueError):
        load_targets(db, category="kitap")
    payload = collect_candidates(db, category="oyun", rawg_key="k", client=_client(GAMES, capture=capture), delay=0)
    assert len(capture) == 1 and len(payload["results"][0]["candidates"]) == 3
