"""Source-backed catalog enrichment. Dry-run by default; no guessed metadata."""
import argparse
import json
from pathlib import Path
from sqlalchemy import select
from .models import Content

DEFAULT_MANIFEST = Path(__file__).resolve().parents[1] / "data" / "catalog-details.json"

def apply_details(db, manifest=DEFAULT_MANIFEST, overwrite=False):
    payload = json.loads(Path(manifest).read_text(encoding="utf-8"))
    lookup = {(item.category, item.title): item for item in db.scalars(select(Content)).all()}
    records = []
    seen = set()
    for row in payload["items"]:
        key = (row["category"], row["title"])
        if key in seen or key not in lookup: raise ValueError("Tekrarlı veya katalogda bulunmayan eser: " + repr(key))
        seen.add(key)
        if type(row["year"]) is not int or not 1 <= row["year"] <= 2100: raise ValueError("Geçersiz yıl")
        if not row["creators"] or not all(isinstance(name, str) and name.strip() for name in row["creators"]): raise ValueError("Geçersiz eser sahibi")
        if not row["metadata_source_url"].startswith("https://"): raise ValueError("HTTPS kaynak gerekli")
        records.append((lookup[key], row))
    for item, row in records:
        # Preserve manual edits unless an explicit import asks to overwrite.
        if overwrite or (item.year is None and not item.creators):
            item.year = row["year"]
            item.creators = row["creators"]
            item.metadata_source_url = row["metadata_source_url"]
    db.flush()

def coverage(db):
    rows = db.scalars(select(Content)).all()
    return {"total": len(rows), "with_year": sum(item.year is not None for item in rows),
            "with_creators": sum(bool(item.creators) for item in rows),
            "missing": [{"category": item.category, "title": item.title} for item in rows if item.year is None or not item.creators]}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", nargs="?", default=str(DEFAULT_MANIFEST))
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()
    from .db import SessionLocal
    with SessionLocal() as db:
        apply_details(db, args.manifest, args.overwrite)
        print(json.dumps(coverage(db), ensure_ascii=False, indent=2))
        if args.apply: db.commit()
        else: db.rollback()

if __name__ == "__main__": main()
