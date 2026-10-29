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
Sefiller|klasik|adalet,karakter gelişimi|duygusal,destansı
Fahrenheit 451|distopya|özgürlük,güç,teknoloji|karanlık,gerilimli|Kitapların yasaklandığı bir toplumda itfaiyeci Montag, görevini ve çevresindeki düzeni sorgulamaya başlar.
Cesur Yeni Dünya|distopya|özgürlük,kimlik,güç|karanlık,sakin|İnsanların önceden belirlenmiş rollere göre yetiştirildiği bir dünyada bireysellik ve mutluluğun bedeli tartışılır.
Hobbit|fantastik|keşif,dostluk,ayrıntılı evren|destansı,neşeli|Bilbo Baggins, bir grup cüceyle çıktığı yolculukta evinden çok uzaklara gider ve beklenmedik bir cesaret gösterir.
Frankenstein|korku|kimlik,adalet,teknoloji|karanlık,duygusal|Victor Frankenstein'ın yarattığı canlı, kendisini reddeden dünyada ait olacağı bir yer arar.
Zaman Makinesi|bilimkurgu|keşif,teknoloji,sınıf|karanlık,gizemli|Bir zaman yolcusu uzak geleceğe giderek insanlığın birbirinden ayrılmış iki topluluğa dönüştüğünü görür.
Ben Robot|bilimkurgu|teknoloji,kimlik,adalet|sakin,gizemli|Robotların insanlarla yaşadığı bir gelecekte farklı öyküler, zekâ ve sorumluluk sınırlarını inceler.
Körlük|distopya|hayatta kalma,güç,adalet|karanlık,gerilimli|Açıklanamayan bir körlük salgını, bir kentin düzenini ve insanların birbirine davranışını değiştirir.
Hayvan Çiftliği|klasik|güç,özgürlük,adalet|karanlık|Çiftlikteki hayvanların eşitlik umuduyla başlattığı isyan, yeni bir iktidar mücadelesine dönüşür.
Gurur ve Önyargı|romantik|romantizm,karakter gelişimi,aile|neşeli,duygusal|Elizabeth Bennet ile Bay Darcy'nin ilk izlenimleri, aile beklentileri ve sınıf farkları karşısında değişir.
Yerdeniz Büyücüsü|fantastik|kimlik,kişisel yolculuk,ayrıntılı evren|büyülü,karanlık|Genç büyücü Ged, yaptığı bir hatanın açığa çıkardığı gölgeyle yüzleşmek için adalar arasında yolculuk eder.""",
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
The Truman Show|dram|özgürlük,gerçeklik|umutlu,duygusal
Ex Machina|bilimkurgu|teknoloji,kimlik,güç|sakin,gerilimli|Genç bir yazılımcı, yalıtılmış bir evde geliştirilen yapay zekânın insan gibi düşünüp düşünmediğini sınayan bir deneye katılır.
Eternal Sunshine of the Spotless Mind|romantik|romantizm,kimlik,gerçeklik|duygusal,sakin|Bir çift, ayrılıklarının ardından birbirlerine ait anıları sildirmeye karar verir; geçmiş ve bağları yeniden sorgulanır.
The Prestige|gerilim|gizem,strateji,güç|karanlık,gerilimli|İki sihirbazın sahnede üstün gelme yarışı, giderek hayatlarını etkileyen bir takıntıya dönüşür.
Children of Men|distopya|hayatta kalma,özgürlük,aile|karanlık,gerilimli|İnsanlığın çocuk sahibi olamadığı bir gelecekte bir adam, umut taşıyan genç bir kadını güvenli yere ulaştırmaya çalışır.
Everything Everywhere All at Once|bilimkurgu|aile,kimlik,gerçeklik|neşeli,duygusal|Evelyn, farklı olasılıklardaki hayatlarıyla karşılaşırken ailesiyle ilişkisini yeniden değerlendirir.
The Martian|bilimkurgu|hayatta kalma,teknoloji,keşif|umutlu,neşeli|Mars'ta yalnız kalan bir astronot, bilimsel çözümler geliştirerek Dünya'ya dönmenin yolunu arar.
The Social Network|dram|teknoloji,güç,kimlik|gerilimli,karanlık|Mark Zuckerberg'in bir sosyal ağ kurması, ortaklık ve sahiplik üzerine anlaşmazlıklara yol açar.
Inside Out|animasyon|aile,kimlik,karakter gelişimi|neşeli,duygusal|Riley'nin duyguları, ailesiyle yeni bir şehre taşınmasının ardından değişen yaşamına uyum sağlamaya çalışır.
Princess Mononoke|animasyon|doğa,güç,adalet|destansı,karanlık|Ashitaka, orman ruhlarıyla insanlar arasındaki çatışmanın ortasında denge kurmaya çalışır.
The Shawshank Redemption|dram|özgürlük,dostluk,adalet|umutlu,duygusal|Haksız yere hapsedildiğini söyleyen Andy Dufresne, yıllar boyunca umudunu ve dostluklarını korur.""",
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
Foundation|bilimkurgu|siyasi entrika,strateji,ayrıntılı evren|destansı
Mr. Robot|gerilim|teknoloji,kimlik,güç|karanlık,gerilimli|Siber güvenlik uzmanı Elliot, bir hacker grubunun planlarına katılırken kendi algısını da sorgular.
Better Call Saul|dram|adalet,kimlik,karakter gelişimi|karanlık,duygusal|Avukat Jimmy McGill'in seçimleri, onu zamanla bambaşka bir mesleki kimliğe sürükler.
The Mandalorian|bilimkurgu|aile,hayatta kalma,ayrıntılı evren|destansı,umutlu|Yalnız çalışan bir ödül avcısı, korumaya karar verdiği çocukla galaksiyi dolaşır.
The Witcher|fantastik|ayrıntılı evren,kimlik,aile|karanlık,destansı|Canavar avcısı Geralt'ın yolu, büyücüler ve krallıklar arasındaki çekişmelerde Ciri ile kesişir.
Chernobyl|dram|güç,adalet,hayatta kalma|karanlık,gerilimli|Nükleer felaketten sonra bilim insanları ve görevliler, tehlikeyi anlamaya ve sonuçları sınırlamaya çalışır.
Fleabag|komedi|aile,kimlik,karakter gelişimi|neşeli,duygusal|Londra'da yaşayan bir kadın, kayıp ve aile sorunlarıyla başa çıkarken izleyiciyle doğrudan konuşur.
The Bear|dram|aile,dostluk,kişisel yolculuk|gerilimli,duygusal|Şef Carmy, ailesinden kalan lokantayı ayakta tutmaya çalışırken mutfak ekibiyle yeni bir düzen kurar.
Westworld|bilimkurgu|teknoloji,kimlik,gerçeklik|karanlık,gerilimli|Yapay varlıkların yaşadığı bir eğlence parkında bilinç ve kontrol arasındaki sınırlar bulanıklaşır.
Andor|bilimkurgu|özgürlük,güç,adalet|karanlık,gerilimli|Cassian Andor, İmparatorluk'a karşı büyüyen direnişin parçası hâline gelir.
The OA|bilimkurgu|gizem,kimlik,gerçeklik|sakin,gizemli|Yıllar sonra geri dönen Prairie, kaybolduğu döneme ilişkin sıra dışı bir hikâye anlatır.""",
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
Celeste|platform|kişisel yolculuk,karakter gelişimi|umutlu,duygusal
Animal Crossing: New Horizons|simülasyon|dostluk,kişisel yolculuk|sakin,neşeli|Oyuncu, ıssız bir adayı komşularıyla birlikte geliştirir; toplama, tasarlama ve günlük yaşam etkinliklerine katılır.
My Time at Portia|simülasyon|dostluk,kişisel yolculuk|sakin,neşeli|Portia kasabasında bir atölyeyi devralan oyuncu, yeni yapılar üretir ve kasaba halkıyla ilişkiler kurar.
Spiritfarer|simülasyon|dostluk,aile,kişisel yolculuk|sakin,duygusal|Stella, yolcularını son vedalarına hazırlarken gemisini geliştirir ve onların hikâyelerini dinler.
A Short Hike|macera|keşif,dostluk,kişisel yolculuk|sakin,neşeli|Claire, bir parkta yürüyüş yapıp yeni tanışıklıklar kurarak dağın zirvesine ulaşmaya çalışır.
Unpacking|bulmaca|kişisel yolculuk,kimlik|sakin,duygusal|Oyuncu, farklı evlere taşınan bir kişinin eşyalarını yerleştirerek hayatındaki değişimleri takip eder.
Slime Rancher|simülasyon|keşif,kişisel yolculuk|neşeli,sakin|Beatrix, uzak bir gezegende çiftlik kurar, renkli canlıları toplar ve çevreyi keşfeder.
Terraria|macera|keşif,hayatta kalma,dostluk|neşeli,gerilimli|Oyuncu, iki boyutlu bir dünyada kaynak toplar, yapılar kurar ve düşmanlarla mücadele eder.
Ori and the Blind Forest|platform|aile,keşif,hayatta kalma|büyülü,duygusal|Ori, yaşadığı ormanı kurtarmak için tehlikeli bölgeleri aşar ve geçmişini keşfeder.
Subnautica|macera|keşif,hayatta kalma,gizem|sakin,gerilimli|Okyanuslarla kaplı yabancı bir gezegene düşen oyuncu, hayatta kalmak için su altı dünyasını araştırır.
Firewatch|macera|gizem,kişisel yolculuk,iletişim|sakin,gerilimli|Bir ormanda yangın gözcüsü olan Henry, telsiz görüşmeleri ve tuhaf olaylar arasında geçmişiyle yüzleşir."""
}

def seed(db):
    existing = {(item.source, item.source_id) for item in db.scalars(select(Content)).all()}
    for category, block in DATA.items():
        for number, line in enumerate(block.splitlines(), 1):
            source_id = f"{category}-{number}"
            if ("local", source_id) in existing:
                continue
            parts = line.split("|", 4)
            title, genres, themes, moods = parts[:4]
            values = [genres.split(","), themes.split(","), moods.split(",")]
            description = parts[4] if len(parts) == 5 else f"{title}: {', '.join(values[1])} temalarını {', '.join(values[2])} bir atmosferle buluşturan bir {category}."
            db.add(Content(category=category, title=title, description=description, genres=values[0], themes=values[1], moods=values[2], language="tr" if len(parts) == 5 else "en", source="local", source_id=source_id))
    db.flush()
    items = db.scalars(select(Content)).all()
    lookup = {(tag.kind, tag.name): tag.id for tag in db.scalars(select(Tag)).all()}
    needed = {(kind, name) for item in items for kind, group in (("genre", item.genres), ("theme", item.themes), ("mood", item.moods)) for name in group}
    for kind, name in needed - lookup.keys():
        db.add(Tag(kind=kind, name=name))
    db.flush()
    lookup = {(tag.kind, tag.name): tag.id for tag in db.scalars(select(Tag)).all()}
    linked = set(db.execute(select(ContentTag.content_id, ContentTag.tag_id)).all())
    for item in items:
        for kind, group in (("genre", item.genres), ("theme", item.themes), ("mood", item.moods)):
            for name in group:
                pair = (item.id, lookup[(kind, name)])
                if pair not in linked:
                    db.add(ContentTag(content_id=pair[0], tag_id=pair[1]))
                    linked.add(pair)
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
