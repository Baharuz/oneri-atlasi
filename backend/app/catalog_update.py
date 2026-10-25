"""İnsan doğrulamalı manifest ile katalog kayıtlarını güvenli, idempotent güncelleyen CLI.

Kullanım:
    python -m app.catalog_update manifest.json          # dry-run önizleme
    python -m app.catalog_update manifest.json --apply  # tek transaction yazma

Manifest biçimi:
    {"items": [{"source": "...", "source_id": "...", "category": "kitap",
                "image_url": "https://...", "description": "...",
                "image_source_url": "https://...", "image_credit": "..."}]}

Yalnızca image_url, description, image_credit, image_source_url alanları güncellenir;
ID, source/source_id, favoriler ve etiketler korunur.
"""
import argparse
import json
from urllib.parse import urlparse

from sqlalchemy import select

from .models import Content

MVP_CATEGORIES = ("kitap", "film", "dizi", "oyun")
REQUIRED_FIELDS = ("source", "source_id", "category", "image_url", "description", "image_credit", "image_source_url")
UPDATE_FIELDS = ("image_url", "description", "image_credit", "image_source_url")

class ManifestError(ValueError):
    def __init__(self, errors):
        self.errors = list(errors)
        super().__init__("; ".join(self.errors))

def load_manifest(path):
    with open(path, encoding="utf-8") as handle:
        data = json.load(handle)
    items = data.get("items") if isinstance(data, dict) else data
    if not isinstance(items, list) or not items:
        raise ManifestError(["Manifest boş veya 'items' listesi değil."])
    return items

def _is_https(value):
    if not isinstance(value, str) or not value.strip(): return False
    parsed = urlparse(value.strip())
    return parsed.scheme == "https" and bool(parsed.netloc)

def _looks_generated(title, description):
    text = description or ""
    if " bir atmosferle buluşturan " in text: return True
    return text.startswith(f"{title}: ") and " temalarını " in text

def find_record(db, item):
    return db.scalar(select(Content).where(Content.source == item.get("source"), Content.source_id == item.get("source_id")))

def validate_manifest(db, items):
    errors, seen = [], {}
    for index, item in enumerate(items):
        order = index + 1
        if not isinstance(item, dict):
            errors.append(f"#{order}: kayıt bir nesne değil.")
            continue
        label = f"{item.get('source')}/{item.get('source_id')}"
        empty = [name for name in REQUIRED_FIELDS if not isinstance(item.get(name), str) or not item[name].strip()]
        if empty: errors.append(f"{label}: zorunlu alanlar eksik veya boş: {', '.join(empty)}")
        if item.get("category") not in MVP_CATEGORIES: errors.append(f"{label}: geçersiz kategori: {item.get('category')!r} (izinli: {', '.join(MVP_CATEGORIES)}).")
        if item.get("image_url") and not _is_https(item["image_url"]): errors.append(f"{label}: image_url HTTPS bir URL olmalı.")
        if item.get("image_source_url") and not _is_https(item["image_source_url"]): errors.append(f"{label}: image_source_url HTTPS bir URL olmalı.")
        if item.get("image_credit") is not None and not isinstance(item["image_credit"], str): errors.append(f"{label}: image_credit metin olmalı.")
        if "description" in item and isinstance(item["description"], str) and not item["description"].strip(): errors.append(f"{label}: açıklama boş olamaz.")
        key = (item.get("source"), item.get("source_id"))
        if key in seen: errors.append(f"{label}: tekrarlı anahtar (satır {seen[key]} ve {order}).")
        else: seen[key] = order
        record = find_record(db, item)
        if record is None:
            errors.append(f"{label}: katalogda eşleşen kayıt yok (source+source_id).")
            continue
        if record.category != item.get("category"): errors.append(f"{label}: kategori uyuşmuyor (katalog: {record.category}).")
        if _looks_generated(record.title, item.get("description")): errors.append(f"{label}: açıklama kalıp/otomatik metne benziyor.")
    return errors

def build_plan(db, items):
    plan = []
    for item in items:
        record = find_record(db, item)
        changes = {}
        for field in UPDATE_FIELDS:
            if field in item:
                new = item[field].strip() if isinstance(item[field], str) else item[field]
                if getattr(record, field) != new: changes[field] = {"from": getattr(record, field), "to": new}
        if changes: plan.append({"id": record.id, "source": record.source, "source_id": record.source_id, "title": record.title, "changes": changes})
    return plan

def _set_fields(record, item):
    for field in UPDATE_FIELDS:
        if field in item:
            value = item[field]
            setattr(record, field, value.strip() if isinstance(value, str) else value)

def apply_manifest(db, items, write=True):
    """Doğrular; write=False ise yalnız plan döner. Hata halinde hiçbir değişiklik kalmaz."""
    errors = validate_manifest(db, items)
    if errors:
        db.rollback()
        raise ManifestError(errors)
    records = [(find_record(db, item), item) for item in items]
    plan = build_plan(db, items)
    if not write or not plan:
        db.rollback()
        return plan
    try:
        for record, item in records:
            _set_fields(record, item)
        db.commit()
    except Exception:
        db.rollback()
        raise
    return plan

def main(argv=None):
    parser = argparse.ArgumentParser(description="Doğrulanmış katalog manifestini uygular (varsayılan dry-run).")
    parser.add_argument("manifest", help="JSON manifest dosyası")
    parser.add_argument("--apply", action="store_true", help="Değişiklikleri tek transaction içinde yazar.")
    args = parser.parse_args(argv)
    from .db import SessionLocal
    try:
        items = load_manifest(args.manifest)
        with SessionLocal() as db:
            plan = apply_manifest(db, items, write=args.apply)
    except ManifestError as error:
        print(json.dumps({"ok": False, "errors": error.errors}, ensure_ascii=False, indent=2))
        return 1
    except Exception as error:
        print(json.dumps({"ok": False, "error": str(error)}, ensure_ascii=False))
        return 1
    print(json.dumps({"ok": True, "mode": "apply" if args.apply else "dry-run", "changes": plan}, ensure_ascii=False, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
