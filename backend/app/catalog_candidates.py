"""Salt-okunur katalog aday aracı: TMDB (film/dizi) ve RAWG (oyun) aramaları.

Yalnızca insan incelemesi için ADAY listesi üretir; veritabanına yazmaz,
otomatik eşleştirme veya manifest uygulama yapmaz.

Kullanım:
    python -m app.catalog_candidates                       # tüm film/dizi/oyunlar
    python -m app.catalog_candidates --category film
    python -m app.catalog_candidates --source-id tmdb-550

Ortam değişkenleri: TMDB_READ_TOKEN (Bearer token), RAWG_API_KEY.
Anahtarlar çıktıya ve hata mesajlarına yazılmaz.
"""
import argparse
import json
import time

import httpx
from sqlalchemy import select

from .models import Content

CANDIDATE_CATEGORIES = ("film", "dizi", "oyun")
MAX_CANDIDATES = 3
TMDB_BASE = "https://api.themoviedb.org/3"
TMDB_IMAGE_BASE = "https://image.tmdb.org/t/p/w500"
TMDB_PAGE_BASE = "https://www.themoviedb.org"
RAWG_SEARCH_URL = "https://api.rawg.io/api/games"
REQUEST_TIMEOUT = 10.0
REQUEST_DELAY = 0.25

class ProviderError(Exception):
    """Sağlayıcı hatası; mesajı URL veya anahtar içermez."""

def load_targets(db, category=None, source_id=None):
    stmt = select(Content).where(Content.category.in_(CANDIDATE_CATEGORIES))
    if category:
        if category not in CANDIDATE_CATEGORIES: raise ValueError(f"Geçersiz kategori: {category!r} (izinli: {', '.join(CANDIDATE_CATEGORIES)}).")
        stmt = stmt.where(Content.category == category)
    if source_id: stmt = stmt.where(Content.source_id == source_id)
    return list(db.scalars(stmt.order_by(Content.id)).all())

def _year(value):
    if isinstance(value, str) and len(value) >= 4 and value[:4].isdigit(): return int(value[:4])
    return None

def _https_or_none(value):
    return value if isinstance(value, str) and value.startswith("https://") else None

def tmdb_candidates(client, content, token):
    kind = "movie" if content.category == "film" else "tv"
    response = client.get(f"{TMDB_BASE}/search/{kind}", params={"query": content.title[:100], "language": "tr-TR"}, headers={"Authorization": f"Bearer {token}", "accept": "application/json"})
    response.raise_for_status()
    rows = response.json().get("results") or []
    candidates = []
    for row in rows[:MAX_CANDIDATES]:
        poster = row.get("poster_path")
        candidates.append({
            "provider": "tmdb",
            "provider_id": str(row.get("id")),
            "title": row.get("title") or row.get("name"),
            "year": _year(row.get("release_date") or row.get("first_air_date")),
            "image_url": f"{TMDB_IMAGE_BASE}{poster}" if isinstance(poster, str) and poster.startswith("/") else None,
            "page_url": f"{TMDB_PAGE_BASE}/{kind}/{row.get('id')}" if row.get("id") is not None else None,
        })
    return candidates

def rawg_candidates(client, content, api_key):
    response = client.get(RAWG_SEARCH_URL, params={"key": api_key, "search": content.title[:100], "page_size": MAX_CANDIDATES})
    response.raise_for_status()
    rows = response.json().get("results") or []
    candidates = []
    for row in rows[:MAX_CANDIDATES]:
        slug = row.get("slug")
        candidates.append({
            "provider": "rawg",
            "provider_id": str(row.get("id")),
            "title": row.get("name"),
            "year": _year(row.get("released")),
            "image_url": _https_or_none(row.get("background_image")),
            "page_url": f"https://rawg.io/games/{slug}" if slug else None,
        })
    return candidates

def _provider_error(provider, content, error):
    entry = {"provider": provider, "content_id": content.id, "title": content.title}
    if isinstance(error, httpx.TimeoutException): entry["error"] = "istek zaman aşımına uğradı"
    elif isinstance(error, httpx.HTTPStatusError):
        code = error.response.status_code
        entry["error"] = f"HTTP {code} ({'kimlik doğrulama hatası' if code in (401, 403) else 'sağlayıcı hatası'})"
    elif isinstance(error, httpx.RequestError): entry["error"] = f"ağ hatası ({type(error).__name__})"
    elif isinstance(error, (ValueError, KeyError, TypeError)): entry["error"] = "beklenmeyen sağlayıcı yanıtı"
    else: entry["error"] = "sağlayıcı isteği başarısız"
    return entry

def _missing_key(provider, content, env_name):
    return {"provider": provider, "content_id": content.id, "title": content.title, "error": f"{env_name} tanımlı değil"}

def collect_candidates(db, category=None, source_id=None, tmdb_token=None, rawg_key=None, client=None, delay=REQUEST_DELAY, sleep=time.sleep):
    targets = load_targets(db, category, source_id)
    results, errors, reported = [], [], set()
    owned = client is None
    if owned: client = httpx.Client(timeout=REQUEST_TIMEOUT)
    try:
        for index, content in enumerate(targets):
            if content.category in ("film", "dizi"):
                if not tmdb_token:
                    if "tmdb" not in reported: errors.append(_missing_key("tmdb", content, "TMDB_READ_TOKEN")); reported.add("tmdb")
                    continue
                try:
                    candidates = tmdb_candidates(client, content, tmdb_token)
                except Exception as error:
                    errors.append(_provider_error("tmdb", content, error))
                    candidates = None
            else:
                if not rawg_key:
                    if "rawg" not in reported: errors.append(_missing_key("rawg", content, "RAWG_API_KEY")); reported.add("rawg")
                    continue
                try:
                    candidates = rawg_candidates(client, content, rawg_key)
                except Exception as error:
                    errors.append(_provider_error("rawg", content, error))
                    candidates = None
            if candidates is not None:
                results.append({"content": {"id": content.id, "category": content.category, "title": content.title, "source_id": content.source_id}, "candidates": candidates})
            if delay and index < len(targets) - 1: sleep(delay)
    finally:
        if owned: client.close()
    return {"results": results, "errors": errors}

def main(argv=None):
    parser = argparse.ArgumentParser(description="TMDB/RAWG için salt-okunur katalog aday listesi (DB yazımı yok).")
    parser.add_argument("--category", choices=CANDIDATE_CATEGORIES)
    parser.add_argument("--source-id")
    parser.add_argument("--indent", action="store_true", help="JSON çıktısını girintili yazdır")
    args = parser.parse_args(argv)
    import os
    from .db import SessionLocal
    try:
        with SessionLocal() as db:
            payload = collect_candidates(db, category=args.category, source_id=args.source_id,
                                         tmdb_token=os.environ.get("TMDB_READ_TOKEN"),
                                         rawg_key=os.environ.get("RAWG_API_KEY"))
    except ValueError as error:
        print(json.dumps({"ok": False, "error": str(error)}, ensure_ascii=False))
        return 2
    except Exception:
        print(json.dumps({"ok": False, "error": "Veritabanına erişilemedi; DATABASE_URL değerini kontrol edin."}, ensure_ascii=False))
        return 1
    if not payload["results"] and not payload["errors"]:
        payload["errors"].append({"error": "filtreye uyan kayıt bulunamadı"})
    payload["ok"] = not payload["errors"]
    print(json.dumps(payload, ensure_ascii=False, indent=2 if args.indent else None))
    return 0 if not payload["errors"] else 1

if __name__ == "__main__":
    raise SystemExit(main())
