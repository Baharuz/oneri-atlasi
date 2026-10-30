> **Arşiv notu (30 Ekim 2026):** Bu belge ilk tasarım incelemesinin tarihsel kaydıdır. 500 eserlik güncel katalog, özgün temsili görseller ve 0003 geçişi için [durum raporuna](mvp1-durum-raporu.md) bakın. Aşağıdaki eski eksikler güncel teslim durumu değildir.

# Gemini incelemesi — Ürün gereksinimleri ve mimari taslağı

**Durum:** İnceleme taslağı (v0.5, 22 Ekim 2026; hesaplı kaydetmenin veritabanında tutulması kararlaştırıldı)
**Amaç:** İki kişinin ajan destekli geliştireceği, yerelde çalışıp daha sonra sunucuya taşınabilecek bir öneri ürünü için gereksinim ve mimari önerisini bağımsız incelemeye sunmak. Bu belge karar taslağıdır; Gemini'nin eleştirisi istenmektedir.
**Not:** Depodaki ad "Öneri Atlası"; ürünün nihai adı ayrıca kararlaştırılacak.

## 1. Ürün fikri

Kullanıcı sevdiği bir eserden hareketle yeni kitap, oyun, dizi veya film keşfeder. Tam üründe dört kategorinin her biri hem başlangıç hem sonuç kategorisi olabilir: film → kitap, oyun → dizi, kitap → oyun ve aynı kategori içindeki öneriler dahil. Kullanıcı ileride eserin özellikle sevdiği yönleri (ör. uzay teması, kasvetli atmosfer, oyun mekaniği) de belirtebilir.

Ürünün değeri yalnızca „benzer eser” listesi vermek değil; önerinin neden yapıldığını anlaşılır biçimde göstermektir. Sıralama kalitesi, katalogdaki eser ve etiket verisinin doğruluğuna bağlıdır.

## 2. İlk sürümün sınırı

İlk sürümde kullanıcı **bir eser seçer ve aynı kategoriden** öneriler alır. Dört kategorinin tamamı kullanılabilir; kategori değiştiren öneriler sonraki aşamaya bırakılır. İlk sürüm için kesinleşen işlevler:

| ID | Kullanıcı isteği | Kabul ölçütü |
| --- | --- | --- |
| G-01 | Kitap, oyun, dizi ve film katalogları | Kullanıcı dört kategorinin her birindeki eserleri ayrı görebilir. |
| G-02 | Eser arama | İlk MVP'de kullanıcı eser adına göre arayabilir ve sonuç yoksa açık bir mesaj görür. Tür araması ve arama çubuğunun gelişmiş arayüzü MVP-2 kapsamındadır. |
| G-03 | Eserden aynı türe öneri | Bir eser seçildiğinde sonuçlar onun kategorisinden gelir; seçilen eser kendisine önerilmez. Her sonuç için kısa bir gerekçe gösterilir. |
| G-04 | Gerçek eser görseli | Yayınlanan her kaydın o esere ait gerçek afişi/kapağı/görseli ve doğrulanmış bir görsel kaynağı bulunur. Eksik görselli kayıt yayına alınmaz. Görseller için kaynak koşulları uygulanır. |
| G-05 | Eser kartı | Kartta başlık, kategori, tür(ler), görsel ve eserin ne olduğuna dair kısa, anlaşılır açıklama yer alır. |
| G-06 | Kaydetme | Ziyaretçi önerilere giriş yapmadan bakabilir. Kaydetme için giriş gerekir; giriş yapan kullanıcı eseri kaydedebilir, kaydedilenlerde tekrar bulabilir ve kayıttan çıkarabilir. Kayıtlar kullanıcı hesabına bağlı olarak PostgreSQL'de saklanır; sayfa yenilenince ve uygulama yeniden açılınca korunur. |
| G-07 | Düzenli arayüz | Ana akış eser bulma → seçme → önerileri inceleme → kaydetme adımlarını kolay anlaşılır biçimde sunar; masaüstü ve telefonda kullanılabilir. Yüklenirken durum bildirilir; boş sonuç ve ağ/API hatasında anlaşılır mesaj ile yeniden deneme yolu bulunur. |

**İlk sürüm dışında:** farklı kategoriler arasında öneri, eser içindeki sevilen nitelikleri ayrıntılı seçme, eser seçmeden yalnızca ruh hâli/tür ile öneri alma, tür araması, gelişmiş arama çubuğu, herkese açık "gurme" profilleri ve sosyal özellikler. Tür araması ile gelişmiş arama deneyimi MVP-2'de ele alınır. Bunlar ürün vizyonundadır; ilk sürüm tamamlanmadan uygulama görevi yapılmaz.

### Örnek kullanıcı akışı

1. Kullanıcı „Oyun”u seçer.
2. „Stardew Valley”i arayıp başlangıç eseri olarak seçer.
3. Aynı kategoriden önerilen oyunları; görsel, tür, kısa açıklama ve öneri gerekçesiyle görür.
4. İlgisini çekeni kaydetmek için giriş yapar; "Kaydedilenler" bölümünde yeniden bulur.

Boş arama sonucu, öneri bulunamaması, yüklenme ve API hatası da tasarlanacak ekran durumlarıdır.

## 3. Mevcut depoyla karşılaştırma

Depoda React + Vite + TypeScript arayüzü, FastAPI + SQLAlchemy API'si, PostgreSQL ve Alembic bulunuyor. Katalogda dört kategori ve kategori başına 15 eser var. Başlığa göre arama, kategoriye göre öneri ve hesaplı favori kaydı için temel kod mevcut.

Başlıca açıklar:

- Eser kartları gerçek görsel yerine kategori simgesi kullanıyor; `image_url` alanı bulunmasına rağmen başlangıç kayıtlarında doldurulmuyor.
- Türler veride mevcut ama kartta belirgin gösterilmiyor. Kısa açıklamalar eser özelinde yazılmak yerine etiketlerden şablonla üretiliyor.
- Arayüz hesap, profil, test, çoklu eser ve farklı kategori seçeneklerini aynı akışta gösteriyor; ilk sürüm için sadeleştirilmeli.
- Küçük katalogda bazı eserler için güçlü eşleşme çıkmayabilir. Öneri niteliği gerçek örneklerle değerlendirilip katalog/etiketler düzenlenmeli.
- Docker Compose şu anda yalnızca PostgreSQL'i çalıştırıyor; üretim dağıtımı henüz hazırlanmış değil.

## 4. Teknik yaklaşım ve veri

İlk sürüm için mevcut tek repo ve tek FastAPI uygulaması korunur. Arayüz React ile, kalıcı veri PostgreSQL ile devam eder. Ayrı mikroservis, mesaj kuyruğu veya çalışma anında yapay zekâ çağrısı ilk sürümün gereksinimi değildir.

Önerilen istek akışı: tarayıcı eserleri API'den arar → kullanıcı tek başlangıç eseri seçer → API aynı kategorideki adayları etiketlerine göre sıralar → görsel, tür, özet ve kısa gerekçeli sonuçları döner. Kaydetme için kullanıcı giriş yapar. Mevcut API'de `/api/contents` araması, `/api/recommend` önerisi ve hesaplı favori kaydı vardır; ilk sürüm sözleşmesi tasarım onayından sonra kesinleştirilecektir.

**Saklama kararı:** Uygulama internete açık olmasa bile geliştirme bilgisayarında FastAPI sunucusu ve kalıcı PostgreSQL veritabanı çalışır. Giriş yapan kullanıcının kaydedilen eserleri yerel PostgreSQL'de tutulur; mevcut API bu yolu zaten kullanır. Tarayıcı yalnızca oturum ve henüz kaydedilmemiş geçici ekran seçimlerini tutabilir. `localStorage` ile kalıcı favori saklama tercih edilmedi: giriş yapan kullanıcının kayıtlarını tek tarayıcıya bağlar ve ileride sunucuya geçişte veri aktarımı gerektirir. Sunucuya taşınırken veritabanı verileri ayrıca aktarılmalı veya yeni katalogla yeniden oluşturulmalıdır.

Bu mimariyi seçme gerekçesi: mevcut çalışan kodu koruması, iki kişi için geliştirme ve hata ayıklamayı kolaylaştırması, yerel geliştirme ile daha sonra sunucuya dağıtım arasında aynı veri modelini kullanabilmesidir. Sınırı: katalog büyüdüğünde veri edinme, etiket kalitesi ve arama performansı ölçülüp gerekirse ayrı iyileştirmeler gerekecektir. Şimdiden dağıtık servis tasarlamak için kanıt yoktur.

Her eser kaydında en az kategori, başlık, türler, kısa açıklama, tema/atmosfer etiketleri, görsel adresi, görsel/veri kaynağı ve kaynaktaki benzersiz kimlik tutulmalıdır. Görsel ve açıklamalar yayın öncesi kontrol edilir. Film/dizi için TMDB, oyun için RAWG, kitap için Open Library değerlendirilebilir; seçilen kaynakların atıf, bağlantı, kullanım ve erişim koşulları uygulama için ayrıca doğrulanır. Katalog verisini kontrollü biçimde önceden yüklemek, öneri anında dış servis cevabına bağımlılığı azaltır. Görseller sağlayıcı URL'lerinden sunulursa bunların erişilebilirliği ve kaynak koşulları yine izlenmelidir; ön yükleme tek başına bütün ağ hatalarını ortadan kaldırmaz.

Öneri sıralaması ilk aşamada mevcut açıklanabilir etiket eşleştirmesinden geliştirilebilir. Tür, tema, atmosfer ve oyuna özgü mekanik/görsel tarz kavramları birbirine karıştırılmamalıdır. Sonuç sırası birkaç gerçek kullanım örneğiyle insan tarafından değerlendirilir; sayısal puan „uyum yüzdesi” olarak gösterilmez.

## 5. Yerelden sunucuya hazırlık

Yerel geliştirme sürecek; kod yapılandırması sunucuya taşınmayı engellememeli. Veritabanı şeması Alembic geçişleriyle yönetilir. API anahtarları, oturum sırrı ve veritabanı parolaları kaynak koduna yazılmaz. Yayına hazırlıkta üretim yapılandırması, uygulama paketleme, HTTPS, görsel kaynaklarının erişilebilirliği, sağlık kontrolü, hata kaydı ve veritabanı yedeği ayrıca tamamlanır. İlk sürümün bitmesi ile internete açılması ayrı kabul kapılarıdır.

## 6. İki kişilik iş bölümü

**İlk MVP aşamasında Bahar — kullanıcı akışı ve arayüz sahipliği**

- İlk sürüm ekran haritasını ve düşük ayrıntılı ekran taslaklarını hazırlamak: ana sayfa/kategori, arama-seçim, öneriler, eser detayı ve kaydedilenler.
- Kartlarda gerçek görsel, tür, kısa açıklama ve kaydetme eylemini görünür ve tutarlı tasarlamak.
- Telefon ve masaüstü düzenlerini, yüklenme/boş sonuç/hata durumlarını tasarlamak.
- Üzerinde anlaşılmış API sözleşmesine göre ön yüzü uygulamak ve kullanılabilirlik kontrolü yapmak.

**İlk MVP aşamasında Haktan ve Codex — API, katalog ve öneri tarafı sahipliği**

- Arayüzle birlikte API istek/yanıt sözleşmesini netleştirmek.
- Eser kayıtlarını, görsel kaynaklarını, türleri ve kısa açıklamaları doğrulamak; katalog ekleme sürecini hazırlamak.
- Aynı kategori önerisi ve kaydetme davranışını gerekli ölçüde düzenlemek.
- Kritik API davranışlarını test etmek; yerel kurulum ve sunucuya geçiş hazırlığını belgelendirmek.

İki taraf da gereksinimleri ve tamamlanan değişiklikleri gözden geçirir. Ajanlar sınırlı, ölçülebilir görevlerde kullanılır; ürettikleri kod insanlar tarafından incelenir. DeepSeek API bütçesi korunur: görevler dar dosya kapsamı ve açık kabul ölçütleriyle verilir, gereksiz yeniden tarama yapılmaz. Yeni ajan görevleri Haktan ile konuşulmadan açılmaz.

**MVP sonrasında rol değişimi:** İlk iş bölümü kalıcı değildir. Haktan arayüz, küçük özellikler, kullanılabilirlik ve hata düzeltme işlerinde daha fazla uygulama sorumluluğu alabilir. Bahar ise ilgisi ve hazırlığına göre kategori geçişleri, öneri/veri kalitesi, API entegrasyonu veya dağıtım hazırlığı gibi daha zor bir işi sahiplenebilir. Hangi işin kime verileceği MVP sonucu ve Bahar'la yapılacak görüşmeden sonra kararlaştırılır. Devirde mevcut API sözleşmesi, örnekler ve testler birlikte incelenir; iki kişi de diğerinin değişikliğini gözden geçirir. Bu rotasyon, ikisinin de bütün ürünü sunumda açıklayabilmesine hizmet eder.

## 7. Henüz karara bağlanmayan konular

1. **Başlangıç katalog büyüklüğü:** Mevcut 15 eser/kategori hangi örnek önerilerde yetersiz kalıyor? Yayın hedefi kalite kontrolünden sonra belirlenecek.
2. **Görsel/veri kaynakları:** Her kategori için hangi sağlayıcı ve hangi atıf gösterimi kullanılacak?
3. **Tasarım yönü:** Beğenilen/beğenilmeyen örnek siteler ve görsel ton Bahar'la birlikte kararlaştırılacak.
4. **İş dağılımı:** Bahar'ın teknik deneyimine göre ön yüz ve içerik işlerinin son sınırı birlikte kesinleştirilecek.

## 8. Geliştirme ve doğrulama sırası

1. Haktan ve Bahar açık kararları yanıtlayıp bu gereksinimleri birlikte onaylar.
2. Bahar kullanıcı akışını ve ekran taslaklarını hazırlar; ikisi birlikte kullanılabilirlik açısından gözden geçirir.
3. Ön yüz ve API için örnek istek/yanıtlar yazılarak arayüz sözleşmesi kararlaştırılır.
4. İşler küçük, bağımsız görevler olarak açılır. Her ajan görevinin dosya kapsamı, kabul ölçütü ve beklenen doğrulaması önceden yazılır.
5. Kod değişiklikleri ikinci kişi tarafından incelenir. İlgili otomatik testler, kod biçimi/tür kontrolleri ve ön yüz derlemesi çalıştırılır; gerçek eser örnekleriyle öneri kalitesi ayrıca kontrol edilir. Test kapsamı değişikliğin riskine göre seçilir.
6. Yerel ilk sürüm kabul edildikten sonra ayrı bir dağıtım kontrolüyle sunucu hazırlığı yapılır.

Bu sıra ders sunumunda da gösterilebilir: hangi kararın kim tarafından verildiği, ajanın ne ürettiği, insanların neyi düzelttiği ve test sonucunda ne değiştiği kaydedilir.

## 9. Teknoloji kararları: sunumda savunulacak taslak

Bu tablo kesinleşmiş üstünlük iddiası değil, mevcut depo ve ürün hedefi için karar gerekçesidir. Gereksinimler değişirse kararlar da yeniden değerlendirilir.

| Karar | Düşünülen alternatif | Bu projedeki gerekçe | Bedel / yeniden değerlendirme koşulu |
| --- | --- | --- | --- |
| Tek repo ve tek API uygulaması | SOA / mikroservisler | İlk sürümün öneri, katalog ve kaydetme akışları küçük bir ekip tarafından birlikte geliştiriliyor; bağımsız servis dağıtımı ihtiyacı henüz yok. | Modüller net tutulmalı. Ayrı ölçekleme veya ekip ihtiyacı somutlaşırsa servis ayrımı tekrar düşünülür. |
| Mevcut React + Vite ön yüzünü sürdürmek | Vue ile yeniden yazmak | Çalışan arayüz ve kurulum zaten var; ürün isterleri yeniden yazımı gerektirmiyor. Vite geliştirme sunucusu ve üretim derlemesini sağlar. | Mevcut arayüz sadeleştirilmeli; framework değiştirmenin maliyeti bugün faydasından yüksek. |
| Mevcut FastAPI API'sini sürdürmek | Node/Express ile yeni API | Öneri kodu Python'da hazır; istek doğrulama ve API şeması için FastAPI'nin olanakları var. | Ön yüz ve API farklı dillerde; iki kişinin bu sınıra hâkim olması ve sözleşmeyi yazması gerekir. |
| PostgreSQL'i sürdürmek | SQLite | SQLite küçük ve tek sunuculu bir uygulamada da çalışabilir. Bu depoda PostgreSQL şeması ve Alembic geçişleri zaten var; kullanıcı kayıtları ile ileride sunucuya dağıtım için istemci-sunucu veritabanını baştan kullanmak yeniden geçişi önler. | Yerelde Docker ve veritabanı işletimi maliyeti var. Çok küçük, tek sunuculu ve az yazmalı bir ürün hedeflenseydi SQLite daha sade olabilirdi. |
| Açıklanabilir etiket eşleştirmesi | Her istekte LLM veya harici öneri API'si | Mevcut algoritma maliyeti öngörülebilir ve gerekçe üretebiliyor; ilk sürümün kalitesi katalog/etiket verisiyle ölçülebilir. | Etiketlerin insan kontrolü gerekir; iyi sonuç üretmediği örneklerle gösterilirse yöntem geliştirilmeli. |
| Kontrollü yerel katalog | Her kullanıcı isteğinde canlı katalog sağlayıcısı | Doğrulanmış verilerle tutarlı sonuç ve tekrarlanabilir test sağlar. | İçerik güncellemesi ve görsel bağlantılarının kontrolü ekip sorumluluğudur. |

Örnek jüri yanıtı — **"Neden PostgreSQL, neden SQLite değil?"**: "SQLite'ı yanlış veya yetersiz bulduğumuz için değil. Küçük bir prototipte uygun olurdu. Mevcut depoda PostgreSQL ve geçişler hazır; hesaplı kaydetme ve ileride sunucuya taşıma hedefi için aynı veritabanıyla devam etmek daha az yeniden iş yaratıyor. Bunun yerel kurulum maliyetini kabul ediyoruz." SQLite'ın küçük web uygulamalarında kullanılabildiği ve istemci-sunucu veritabanlarının yüksek eşzamanlı yazma için daha uygun olduğu [resmî SQLite açıklamasında](https://www.sqlite.org/whentouse.html) belirtilir. PostgreSQL'in eşzamanlı veri erişimi yaklaşımı [belgelenmiştir](https://www.postgresql.org/docs/16/mvcc-intro.html).

## 10. Profesyonel geliştirmeyi sunumda nasıl kanıtlarız?

| Gösterilecek kanıt | Ne açıklanacak? |
| --- | --- |
| Bu gereksinim belgesi ve açık kararlar | Kimin hangi ihtiyacını çözdüğümüz, ilk sürüm sınırı ve kabul ölçütleri. |
| Bahar'ın kullanıcı akışı ve ekran taslakları | Arayüzün koddan önce hangi kararlarla sadeleştirildiği ve hata/boş durumların düşünüldüğü. |
| Teknoloji kararları tablosu ve API sözleşmesi | Alternatiflerin değerlendirildiği, ön yüz ile API sınırının tanımlandığı. |
| Küçük görevler, ajan istemleri ve insan incelemesi | Ajanın ne yaptığı, insanların neyi doğruladığı veya düzelttiği; görev ve değişiklik geçmişi. |
| Otomatik kontroller ve gerçek eser senaryoları | API testleri, ön yüz derlemesi, öneri kalitesinin örneklerle kontrolü ve bulunan hataların çözümü. |
| Çalışan yerel demo ve yayın hazırlık listesi | Dört kategoriden eser seçme, aynı türde öneri, gerçek görsel, arama ve kaydetme; sunucuya geçişte kalan işler. |

Sunumu ancak gerçek uygulama ve doğrulama sonuçları ortaya çıktıktan sonra tamamlamak gerekir. Henüz yapılmamış test veya dağıtım, yapılmış gibi anlatılmaz. Her iki geliştirici de hem kendi bölümünü hem bütün kullanıcı akışını açıklayabilmelidir.

## 11. Gemini'ye elle gönderilecek inceleme isteği

> Ekteki ürün gereksinimleri ve mimari taslağını bağımsız bir incelemeci gibi değerlendir. Kod yazma veya dosya değiştirme. İlk sürümün iki kişiyle uygulanabilirliğini; önerilen React/FastAPI/PostgreSQL yapısının ve Bölüm 9'daki karşılaştırmaların savunulabilirliğini; belirsiz veya çelişen gereksinimleri; veri/görsel kaynağı risklerini; eksik kabul ölçütlerini ve Bahar ile Haktan arasındaki iş sınırını değerlendir. Öncelik sırasına göre en fazla 5 somut düzeltme ve hocanın sorabileceği 3 zor soru öner. Her düzeltmenin ilgili bölümünü belirt, varsayımlarını açıkça işaretle. Kısa ve Türkçe yanıt ver.

## Kaynaklar

- Mevcut depo: `README.md`, `frontend/src/main.tsx`, `backend/app/main.py`, `backend/app/models.py`, `backend/app/catalog.py`, `backend/app/recommend.py`.
- TMDB kullanım ve atıf: https://developer.themoviedb.org/docs/faq
- RAWG API koşulları: https://rawg.io/tos_api
- Open Library kapak API'si: https://openlibrary.org/dev/docs/api/covers
- SQLite uygun kullanım senaryoları: https://www.sqlite.org/whentouse.html
- PostgreSQL eşzamanlılık: https://www.postgresql.org/docs/16/mvcc-intro.html
- FastAPI özellikleri: https://fastapi.tiangolo.com/features/
- Vite geliştirme yaklaşımı: https://vite.dev/guide/why
