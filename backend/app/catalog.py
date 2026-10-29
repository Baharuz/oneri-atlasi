from sqlalchemy import select
from .models import Content, Tag, ContentTag
import json

# Etiketler ve kısa açıklamalar bu öğrenci projesi için elle hazırlanmıştır.
# biçim: ad | tür | tema | atmosfer
DATA = {
"kitap": """Dune|bilimkurgu|siyasi entrika,ayrıntılı evren|destansı,karanlık
Yüzüklerin Efendisi|fantastik|dostluk,keşif,ayrıntılı evren|destansı
1984|distopya|özgürlük,güç|karanlık,gerilimli
Suç ve Ceza|klasik|vicdan,karakter gelişimi|karanlık,duygusal
Küçük Prens|masal|dostluk,keşif|sakin,duygusal
Sherlock Holmes: Kızıl Dosya|polisiye|gizem,strateji|gerilimli
Vakıf|bilimkurgu|siyasi entrika,strateji,ayrıntılı evren|destansı
Açlık Oyunları|distopya|hayatta kalma,güç|gerilimli,karanlık
Otostopçunun Galaksi Rehberi|bilimkurgu|keşif,mizah|neşeli
Harry Potter ve Felsefe Taşı|fantastik|dostluk,gizem,ayrıntılı evren|büyülü
Jane Eyre|romantik|romantizm,karakter gelişimi|duygusal
Drakula|korku|gizem,hayatta kalma|karanlık,gerilimli
Simyacı|macera|keşif,kişisel yolculuk|sakin,umutlu
Neuromancer|bilimkurgu|teknoloji,güç|karanlık,gerilimli
Sefiller|klasik|adalet,karakter gelişimi|duygusal,destansı""",
"film": """Arrival|bilimkurgu|iletişim,gizem|sakin,duygusal
Interstellar|bilimkurgu|keşif,aile|destansı,duygusal
The Dark Knight|aksiyon|adalet,güç,strateji|karanlık,gerilimli
Inception|bilimkurgu|gizem,gerçeklik|gerilimli
Spirited Away|animasyon|keşif,karakter gelişimi|büyülü,duygusal
The Grand Budapest Hotel|komedi|dostluk,mizah|neşeli
Parasite|gerilim|sınıf,güç|karanlık,gerilimli
The Matrix|bilimkurgu|özgürlük,gerçeklik,teknoloji|karanlık
Amélie|romantik|romantizm,kişisel yolculuk|neşeli,umutlu
Blade Runner 2049|bilimkurgu|kimlik,teknoloji|karanlık,sakin
The Lord of the Rings: The Fellowship of the Ring|fantastik|dostluk,keşif,ayrıntılı evren|destansı
Knives Out|polisiye|gizem,strateji|neşeli,gerilimli
Mad Max: Fury Road|aksiyon|hayatta kalma,özgürlük|gerilimli,destansı
Her|romantik|romantizm,teknoloji,kimlik|sakin,duygusal
The Truman Show|dram|özgürlük,gerçeklik|umutlu,duygusal""",
"dizi": """Dark|bilimkurgu|gizem,aile,gerçeklik|karanlık,gerilimli
The Expanse|bilimkurgu|siyasi entrika,ayrıntılı evren|destansı,gerilimli
Breaking Bad|dram|güç,karakter gelişimi|karanlık,gerilimli
The Good Place|komedi|vicdan,mizah|neşeli,umutlu
Stranger Things|bilimkurgu|dostluk,gizem|gerilimli,büyülü
Severance|bilimkurgu|kimlik,özgürlük,gizem|sakin,gerilimli
The Crown|dram|siyasi entrika,aile|duygusal
Sherlock|polisiye|gizem,strateji|gerilimli
Arcane|animasyon|sınıf,güç,karakter gelişimi|karanlık,destansı
Avatar: The Last Airbender|fantastik|dostluk,keşif,karakter gelişimi|destansı,umutlu
Black Mirror|bilimkurgu|teknoloji,gerçeklik|karanlık
Ted Lasso|komedi|dostluk,kişisel yolculuk|neşeli,umutlu
The Last of Us|dram|hayatta kalma,aile|karanlık,duygusal
Only Murders in the Building|polisiye|gizem,mizah|neşeli
Foundation|bilimkurgu|siyasi entrika,strateji,ayrıntılı evren|destansı""",
"oyun": """Disco Elysium|rol yapma|siyasi entrika,kimlik,gizem|karanlık,duygusal
Outer Wilds|macera|keşif,gizem|sakin,duygusal
Civilization VI|strateji|strateji,güç,keşif|destansı
The Witcher 3|rol yapma|ayrıntılı evren,karakter gelişimi|destansı,karanlık
Stardew Valley|simülasyon|dostluk,kişisel yolculuk|sakin,neşeli
Hollow Knight|macera|keşif,gizem|karanlık
Mass Effect|rol yapma|siyasi entrika,ayrıntılı evren,dostluk|destansı
Portal 2|bulmaca|strateji,mizah|neşeli
The Last of Us Part I|macera|hayatta kalma,aile|karanlık,duygusal
Hades|aksiyon|aile,karakter gelişimi|destansı,neşeli
Journey|macera|keşif,kişisel yolculuk|sakin,duygusal
Detroit: Become Human|macera|özgürlük,teknoloji,kimlik|gerilimli,duygusal
Baldur's Gate 3|rol yapma|ayrıntılı evren,dostluk,strateji|destansı
Return of the Obra Dinn|bulmaca|gizem,strateji|gerilimli
Celeste|platform|kişisel yolculuk,karakter gelişimi|umutlu,duygusal"""
}

def seed(db):
    if not db.scalar(select(Content.id).limit(1)):
        tags = set()
        for category, block in DATA.items():
            for number, line in enumerate(block.splitlines(), 1):
                title, genres, themes, moods = line.split("|")
                values = [genres.split(","), themes.split(","), moods.split(",")]
                for kind, group in zip(("genre", "theme", "mood"), values):
                    tags.update((kind, value) for value in group)
                db.add(Content(category=category, title=title, description=f"{title}: {', '.join(values[1])} temalarını {', '.join(values[2])} bir atmosferle buluşturan bir {category}.", genres=values[0], themes=values[1], moods=values[2], language="en", source="local", source_id=f"{category}-{number}"))
        for kind, name in tags:
            db.add(Tag(kind=kind, name=name))
        db.commit()
    if not db.scalar(select(ContentTag.content_id).limit(1)):
        lookup = {(t.kind,t.name):t.id for t in db.scalars(select(Tag)).all()}
        for item in db.scalars(select(Content)).all():
            for kind, group in (("genre",item.genres),("theme",item.themes),("mood",item.moods)):
                for name in group:
                    tag_id = lookup.get((kind,name))
                    if tag_id: db.add(ContentTag(content_id=item.id,tag_id=tag_id))
        db.commit()

REPORT_CATEGORIES = ("kitap", "film", "dizi", "oyun")

def _is_pattern_description(item):
    text = item.description or ""
    return text.startswith(f"{item.title}: ") and " temalarını " in text and " bir atmosferle buluşturan bir " in text

def quality_issues(db):
    """Salt okunur rapor: boş görsel/açıklama/kaynak-atıf ve kalıp açıklamalı kayıtlar. Eksik bulmak normal sonuçtur."""
    items = db.scalars(select(Content).where(Content.category.in_(REPORT_CATEGORIES)).order_by(Content.category, Content.title, Content.id)).all()
    issues = []
    for item in items:
        missing = []
        if not (item.image_url or "").strip(): missing.append("image_url")
        if not (item.description or "").strip(): missing.append("description")
        if not (item.image_credit or "").strip(): missing.append("image_credit")
        if not (item.image_source_url or "").strip(): missing.append("image_source_url")
        if _is_pattern_description(item): missing.append("pattern_description")
        if missing: issues.append({"id": item.id, "category": item.category, "title": item.title, "issues": missing})
    return issues

def main():
    from .db import SessionLocal
    try:
        with SessionLocal() as db:
            issues = quality_issues(db)
    except Exception as error:
        print(json.dumps({"error": str(error), "hint": "Veritabanına erişilemedi; DATABASE_URL değerini kontrol edin."}, ensure_ascii=False))
        return 1
    print(json.dumps({"total": len(issues), "items": issues}, ensure_ascii=False, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
