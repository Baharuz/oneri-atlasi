from sqlalchemy import select
from .models import Content, Tag, ContentTag
from .catalog_expansion import DATA as EXPANSION
from .catalog_metadata import editorial_metadata
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

DESCRIPTIONS = {
    ("kitap", "Dune"): "Paul Atreides, ailesinin Arrakis'e taşınmasıyla baharat ticaretinin ve çöl halkının belirlediği bir güç mücadelesinin içine düşer.",
    ("kitap", "Yüzüklerin Efendisi"): "Frodo ve yol arkadaşları, Orta Dünya'yı tehdit eden Tek Yüzük'ü yok etmek için tehlikeli ve uzun bir yolculuğa çıkar.",
    ("kitap", "1984"): "Winston Smith, her düşüncenin gözetlendiği Okyanusya'da geçmişin nasıl değiştirildiğini fark ederek baskıcı düzene karşı küçük bir alan arar.",
    ("kitap", "Suç ve Ceza"): "Raskolnikov'un işlediği cinayetin ardından duyduğu suçluluk, onu hem kendi kuramlarıyla hem de çevresindeki insanlarla yüzleşmeye zorlar.",
    ("kitap", "Küçük Prens"): "Küçük Prens farklı gezegenlerde karşılaştığı yetişkinler aracılığıyla dostluk, sevgi ve bakmanın ötesinde görmeyi öğrenir.",
    ("kitap", "Sherlock Holmes: Kızıl Dosya"): "Dr. Watson, Sherlock Holmes ile tanışır ve birlikte izleri Londra'dan uzak bir geçmişe uzanan esrarengiz bir cinayeti araştırırlar.",
    ("kitap", "Vakıf"): "Hari Seldon, imparatorluğun çöküşünü öngörerek bilgiyi koruyacak bir Vakıf kurar; sonraki kuşaklar değişen güç dengelerinde ayakta kalmaya çalışır.",
    ("kitap", "Açlık Oyunları"): "Katniss Everdeen, kız kardeşinin yerine seçilince Panem'in televizyonda yayımlanan ölümcül yarışmasında hayatta kalmak zorunda kalır.",
    ("kitap", "Otostopçunun Galaksi Rehberi"): "Dünya'nın yıkılmasından hemen önce kurtarılan Arthur Dent, galaksiyi dolaşırken evrenin tuhaf kurallarıyla ve absürt yol arkadaşlarıyla tanışır.",
    ("kitap", "Harry Potter ve Felsefe Taşı"): "Harry Potter on birinci yaş gününde büyücü olduğunu öğrenir; Hogwarts'taki ilk yılında yeni dostluklar kurarken ailesinin geçmişine yaklaşır.",
    ("kitap", "Jane Eyre"): "Yetim büyüyen Jane Eyre, kendi ayakları üzerinde durmaya çalışırken Thornfield Malikânesi'ndeki duygusal ve ahlaki sınavlarla karşılaşır.",
    ("kitap", "Drakula"): "Jonathan Harker'ın Transilvanya'daki ziyareti, Kont Drakula'nın İngiltere'ye uzanan tehdidini ortaya çıkarır ve bir grup insanı onu durdurmak için birleştirir.",
    ("kitap", "Simyacı"): "Santiago, gördüğü rüyanın izinden Mısır'a doğru giderken karşılaştığı insanların yardımıyla aradığı hazinenin anlamını sorgular.",
    ("kitap", "Neuromancer"): "Eski hacker Case, yeniden siber uzaya bağlanma umuduyla tehlikeli bir işe girer ve şirketlerin, yapay zekâların yönettiği bir entrikaya çekilir.",
    ("kitap", "Sefiller"): "Jean Valjean geçmişinden kaçıp yeni bir yaşam kurmaya çalışırken Javert'in takibi, yoksulluk ve adaletsizlikle dolu bir toplumda kaderini belirler.",
    ("film", "Arrival"): "Birden fazla ülkeye inen uzay gemilerinin ardından dilbilimci Louise Banks, ziyaretçilerin dilini çözerek niyetlerini anlamaya çalışır.",
    ("film", "Interstellar"): "Yaşanmaz hâle gelen Dünya'da Cooper, insanlığa yeni bir yuva arayan uzay görevine katılır; zamanın etkisi ailesinden uzaklığını derinleştirir.",
    ("film", "The Dark Knight"): "Batman, Gotham'da suç örgütlerini durdurmaya çalışırken Joker'in yarattığı kaos, kahramanlık ve adalet anlayışını sınar.",
    ("film", "Inception"): "Dom Cobb, rüyalara girerek bilgi çalan ekibiyle bu kez bir düşünceyi hedefin zihnine yerleştirmeye çalışır.",
    ("film", "Spirited Away"): "Chihiro, ailesiyle birlikte ruhların dünyasına girer ve onları kurtarmak için gizemli bir hamamda çalışmayı öğrenir.",
    ("film", "The Grand Budapest Hotel"): "Otel görevlisi Gustave ile genç yardımcısı Zero, değerli bir tablo ve tartışmalı bir miras yüzünden peşlerine düşenlerden kaçar.",
    ("film", "Parasite"): "Kim ailesi, varlıklı Park ailesinin evinde iş buldukça iki hanenin yaşamları iç içe geçer ve sınıf farkının yarattığı gerilim büyür.",
    ("film", "The Matrix"): "Yazılımcı Neo, yaşadığı dünyanın bir simülasyon olabileceğini öğrenir ve makinelerin kurduğu düzene karşı mücadeleye katılır.",
    ("film", "Amélie"): "Paris'te yalnız yaşayan Amélie, çevresindekilerin hayatına küçük müdahalelerle neşe katarken kendi mutluluğuyla yüzleşir.",
    ("film", "Blade Runner 2049"): "Replikant avcısı K, geçmişe ilişkin sarsıcı bir iz bulur; araştırması onu kayıp Rick Deckard'a ve kendi kimliğiyle ilgili sorulara götürür.",
    ("film", "The Lord of the Rings: The Fellowship of the Ring"): "Frodo, Tek Yüzük'ü yok etmek için Shire'dan ayrılır; farklı halklardan kurulan yol arkadaşlığı karanlık güçlere karşı ilk adımı atar.",
    ("film", "Knives Out"): "Ünlü bir polisiye yazarının ölümünden sonra dedektif Benoit Blanc, aile üyelerinin çelişkili ifadelerini ve miras çekişmesini inceler.",
    ("film", "Mad Max: Fury Road"): "Furiosa'nın kaçışına katılan Max, çölün acımasız yöneticisinden kurtulmaya çalışan bir grupla uzun bir kovalamacaya girer.",
    ("film", "Her"): "Yalnız bir yazar olan Theodore, yapay zekâ işletim sistemi Samantha ile yakınlaşır ve ilişkinin anlamını yeniden düşünür.",
    ("film", "The Truman Show"): "Truman Burbank, günlük yaşamındaki tuhaflıkları fark ettikçe bütün hayatının bir televizyon programı olarak kurgulandığını keşfeder.",
    ("dizi", "Dark"): "Almanya'daki küçük bir kasabada çocukların kaybolması, birbirine bağlı aileleri geçmişe ve geleceğe uzanan karmaşık bir gizeme sürükler.",
    ("dizi", "The Expanse"): "Dünya, Mars ve Kuşak arasındaki gerilim, kayıp bir kadını arayan dedektif ile bir uzay gemisi mürettebatının yollarını kesiştirir.",
    ("dizi", "Breaking Bad"): "Kimya öğretmeni Walter White, hastalık teşhisinden sonra uyuşturucu üretimine başlar ve aldığı kararlar ailesiyle çevresini giderek tehlikeye atar.",
    ("dizi", "The Good Place"): "Ölümden sonraki iyi yere geldiğini sanan Eleanor, oraya yanlışlıkla alındığını fark ederek daha iyi biri olmayı öğrenmeye çalışır.",
    ("dizi", "Stranger Things"): "Will'in kaybolmasıyla başlayan arayış, arkadaşlarını gizli deneylere, doğaüstü güçlere ve Hawkins'in karanlık yüzüne götürür.",
    ("dizi", "Severance"): "Lumon çalışanları iş ve özel yaşam anılarını ayıran bir işleme girer; Mark, ofisteki düzenin ardındaki gerçeği araştırır.",
    ("dizi", "The Crown"): "II. Elizabeth'in tahta çıkışıyla birlikte kraliyet görevi, aile ilişkileri ve Britanya siyasetindeki değişimler uzun yıllara yayılan bir hikâyeye dönüşür.",
    ("dizi", "Sherlock"): "Sherlock Holmes ve Dr. Watson, modern Londra'da sıra dışı suçları çözerken keskin gözlem ile karmaşık kişisel ilişkiler arasında ilerler.",
    ("dizi", "Arcane"): "Piltover ile Zaun arasındaki eşitsizlik büyürken Vi ve Jinx'in kopan bağı, bilimsel keşifler ve siyasal çatışmalarla sınanır.",
    ("dizi", "Avatar: The Last Airbender"): "Genç Avatar Aang, dostlarıyla dört ulusu dolaşarak elementleri öğrenir ve Ateş Ulusu'nun başlattığı savaşı sona erdirmeye çalışır.",
    ("dizi", "Black Mirror"): "Birbirinden bağımsız öyküler, günlük yaşamı değiştiren teknolojilerin mahremiyet, güç ve insan ilişkileri üzerindeki sonuçlarını ele alır.",
    ("dizi", "Ted Lasso"): "Amerikalı futbol antrenörü Ted Lasso, İngiltere'de bir futbol takımının başına geçer ve iyimser yaklaşımıyla hem oyuncuları hem kendisini değiştirir.",
    ("dizi", "The Last of Us"): "Salgın sonrası Amerika'da Joel, Ellie'yi ülkenin öbür ucuna götürmekle görevlendirilir; zorlu yolculuk aralarında güçlü bir bağ kurar.",
    ("dizi", "Only Murders in the Building"): "Aynı apartmanda yaşayan üç suç meraklısı, komşularının ölümünü araştırırken buldukları ipuçlarını bir podcast'e dönüştürür.",
    ("dizi", "Foundation"): "Hari Seldon'un imparatorluğun çöküşüne ilişkin öngörüsü, farklı gezegenlerde ve kuşaklarda bilgiyi koruma mücadelesini başlatır.",
    ("oyun", "Disco Elysium"): "Hafızasını yitirmiş bir dedektif, Revachol'da bir cinayeti soruştururken kendi geçmişini ve kentin siyasi çatışmalarını da çözmeye çalışır.",
    ("oyun", "Outer Wilds"): "Oyuncu, zaman döngüsüne sıkışmış küçük bir güneş sistemini keşfederek kayıp bir uygarlığın geride bıraktığı işaretleri birleştirir.",
    ("oyun", "Civilization VI"): "Oyuncu, antik çağdan modern döneme uzanan bir uygarlık kurar; diplomasi, araştırma ve savaş kararlarıyla tarihsel yönünü belirler.",
    ("oyun", "The Witcher 3"): "Canavar avcısı Geralt, kayıp Ciri'yi ararken savaşın yıprattığı bölgelerde insanların ve yaratıkların iç içe geçtiği seçimler yapar.",
    ("oyun", "Stardew Valley"): "Oyuncu, miras kalan çiftliği onarır; ürün yetiştirir, kasaba sakinleriyle tanışır ve Pelican Town'da kendi günlük ritmini kurar.",
    ("oyun", "Hollow Knight"): "Küçük bir şövalye, terk edilmiş Hallownest krallığının derinliklerine inerek kayıp tarihini ve yayılan enfeksiyonun kaynağını keşfeder.",
    ("oyun", "Mass Effect"): "Komutan Shepard, galaksiyi tehdit eden kadim bir tehlikeyi araştırırken farklı türlerden bir ekip kurar ve zor seçimlerle karşılaşır.",
    ("oyun", "Portal 2"): "Chell, Aperture laboratuvarlarında portal silahıyla fizik bulmacalarını çözerek yapay zekâ GLaDOS'un kurduğu engelleri aşmaya çalışır.",
    ("oyun", "The Last of Us Part I"): "Joel ve Ellie, salgın sonrası Amerika'yı geçerken kaynak kıtlığı, tehlikeli gruplar ve aralarında gelişen bağla yüzleşir.",
    ("oyun", "Hades"): "Yeraltı dünyasından kaçmaya çalışan Zagreus, her denemede farklı tanrıların desteğini alır ve ailesine ilişkin sırları açığa çıkarır.",
    ("oyun", "Journey"): "Oyuncu, uzak bir dağın zirvesine ulaşmak için çölde ilerler; yolda karşılaştığı isimsiz yolcularla sözsüz bir bağ kurabilir.",
    ("oyun", "Detroit: Become Human"): "Üç androidin kesişen hikâyesi, teknolojik bir toplumda özgür irade ve insan sayılmanın ne anlama geldiğini seçimlerle sorgular.",
    ("oyun", "Baldur's Gate 3"): "Zihnine parazit yerleştirilen bir maceracı, Faerûn'da yoldaşlar toplayarak tedavi arar ve büyük bir tehdidin izini sürer.",
    ("oyun", "Return of the Obra Dinn"): "Sigorta müfettişi, yıllar sonra ortaya çıkan Obra Dinn gemisindeki mürettebatın akıbetini geçmişin donmuş anlarını inceleyerek çözer.",
    ("oyun", "Celeste"): "Madeline, Celeste Dağı'na tırmanırken zorlu platform bölümlerini aşar ve kaygılarıyla başa çıkmanın yolunu arar.",
}

def seed(db):
    existing = {(item.source, item.source_id): item for item in db.scalars(select(Content)).all()}
    for category, block in DATA.items():
        lines = block.splitlines() + EXPANSION.get(category, "").splitlines()
        for number, line in enumerate(lines, 1):
            source_id = f"{category}-{number}"
            parts = line.split("|", 4)
            title, genres, themes, moods = parts[:4]
            if ("local", source_id) in existing:
                item = existing[("local", source_id)]
                if (category, title) in DESCRIPTIONS and _is_pattern_description(item):
                    item.description = DESCRIPTIONS[(category, title)]
                    item.language = "tr"
                continue
            values = [genres.split(","), themes.split(","), moods.split(",")]
            description = parts[4] if len(parts) == 5 else DESCRIPTIONS[(category, title)]
            db.add(Content(category=category, title=title, description=description, genres=values[0], themes=values[1], moods=values[2], language="tr", source="local", source_id=source_id))
    db.flush()
    items = db.scalars(select(Content)).all()
    for item in items:
        if item.source == "local" and item.category in DATA:
            item.pace, item.audience = editorial_metadata(item.category, item.genres, item.themes, item.moods)
            item.image_url = f"/art/{item.source_id}.svg"
            item.image_source_url = f"https://github.com/Baharuz/oneri-atlasi/blob/main/frontend/public/art/{item.source_id}.svg"
            item.image_credit = "Öneri Atlası özgün temsili görseli · Resmî kapak/afiş değil · Proje içi kullanım"
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
