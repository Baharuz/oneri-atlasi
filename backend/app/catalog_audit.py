"""Katalog bütünlüğü ve görsel URL denetimi.

DATABASE_URL ayarlı iken: python -m app.catalog_audit
Bağlantı denetimi için: python -m app.catalog_audit --check-urls
"""
import argparse
from collections import Counter
import json
import unicodedata
from pathlib import Path
import xml.etree.ElementTree as ET

import httpx
from sqlalchemy import select

from .catalog import REPORT_CATEGORIES, quality_issues
from .models import Content

EXPECTED_PER_CATEGORY = 125


def _key(title):
    return unicodedata.normalize("NFKC", title).casefold().strip()


def _url_error(client, url, image):
    if image and isinstance(url, str) and url.startswith("/art/"):
        public = Path(__file__).resolve().parents[2] / "frontend" / "public"
        path = (public / url.lstrip("/")).resolve()
        if not path.is_relative_to(public.resolve()) or path.suffix != ".svg":
            return "geçersiz yerel görsel yolu"
        if not path.is_file():
            return "yerel görsel dosyası yok"
        try:
            ET.parse(path)
        except ET.ParseError:
            return "SVG geçersiz"
        return None
    if not isinstance(url, str) or not url.startswith("https://"):
        return "HTTPS URL gerekli"
    try:
        response = client.get(url, follow_redirects=True)
        if response.status_code >= 400:
            return f"HTTP {response.status_code}"
        if image and not response.headers.get("content-type", "").lower().startswith("image/"):
            return "yanıt görsel değil"
    except httpx.HTTPError as error:
        return type(error).__name__
    return None


def audit(db, check_urls=False, client=None):
    items = list(db.scalars(select(Content).order_by(Content.category, Content.title, Content.id)))
    counts = Counter(item.category for item in items)
    errors = []
    for category in REPORT_CATEGORIES:
        if counts[category] != EXPECTED_PER_CATEGORY:
            errors.append(f"{category}: {counts[category]} eser; beklenen {EXPECTED_PER_CATEGORY}")
    extra = set(counts) - set(REPORT_CATEGORIES)
    if extra:
        errors.append(f"Beklenmeyen kategoriler: {', '.join(sorted(extra))}")
    seen = {}
    for item in items:
        key = (item.category, _key(item.title))
        if key in seen:
            errors.append(f"Mükerrer eser: {item.category} / {item.title} (#{seen[key]}, #{item.id})")
        seen[key] = item.id
    issues = quality_issues(db)
    for issue in issues:
        errors.append(f"#{issue['id']} {issue['title']}: {', '.join(issue['issues'])}")
    if check_urls:
        owned = client is None
        if owned:
            client = httpx.Client(timeout=12, headers={"User-Agent": "OneriAtlasiCatalogAudit/1.0"})
        try:
            for item in items:
                for field, image in (("image_url", True), ("image_source_url", False)):
                    url = getattr(item, field)
                    if not url:
                        continue
                    problem = _url_error(client, url, image)
                    if problem:
                        errors.append(f"#{item.id} {field}: {problem}")
        finally:
            if owned:
                client.close()
    return {"ok": not errors, "total": len(items), "categories": dict(counts), "errors": errors}


def main(argv=None):
    parser = argparse.ArgumentParser(description="500 eserlik katalog bütünlüğünü denetle.")
    parser.add_argument("--check-urls", action="store_true", help="Görsel ve kaynak bağlantılarını HTTP ile kontrol et")
    args = parser.parse_args(argv)
    from .db import SessionLocal
    with SessionLocal() as db:
        report = audit(db, check_urls=args.check_urls)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
