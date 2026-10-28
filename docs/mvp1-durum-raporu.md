# MVP-1 durum raporu

**Tarih:** 26 Ekim 2026; akış güncellemesi 28 Ekim 2026

**İncelenen sürüm:** `main` (backend çalışması ile Bahar'ın `feat/flow-first-frontend` dalının birleşimi)

**Amaç:** Çalışan kodu, yerel veriyi ve üzerinde anlaşılmış MVP-1 kapsamını birbirinden ayırarak teslim durumunu göstermek.

## Üzerinde anlaşılan MVP-1

Ziyaretçi **kitap, film, dizi veya oyun** kategorisinde eser adını arar, **bir eser** seçer ve **aynı kategoriden** gerekçeli öneriler görür. Eser kartında gerçek kapak/afiş, türler ve esere özel kısa açıklama bulunur. Arama ve öneri hesapsızdır; eser kaydetmek ve kaydedilenleri görmek için hesap gerekir. Tür/özellik araması, kategoriler arası öneri, çoklu başlangıç eseri, müzik ve sosyal profil bu teslimin kapsamı dışındadır.

**Durum anahtarı:** “Çalışıyor” otomatik test veya yerel API kontrolüyle doğrulandı. “Kısmi” kod mevcut fakat kullanıcı akışı, veri veya tarayıcı testi eksik. “Çalışmıyor” hedeflenen MVP-1 davranışı mevcut birleşik sürümde sağlanmıyor.

## Özellik durumu

| İster / akış | Durum | Bugünkü gerçek davranış ve kanıt |
| --- | --- | --- |
| Dört kategorili katalog | **Çalışıyor** | PostgreSQL'de kitap, film, dizi ve oyundan 15'er eser var; `GET /api/contents` bu 60 eseri listeliyor. Arayüz artık yalnız bu dört kategoriyi gösteriyor. Eski 15 müzik kaydı veritabanında duruyor, MVP listesinden ve arayüzden gizli. |
| Eser adına göre arama | **Çalışıyor** | Backend `q` ile başlık araması sunuyor; arayüz yüklenen katalogda başlığa göre filtreliyor. Tür adına göre arama henüz yok; bu MVP-2 konusu. |
| Tek eserden aynı kategoride öneri | **Kısmi** | Arayüz artık tek eser seçtiriyor ve `GET /api/contents/{id}/recommendations` ucunu çağırıyor. Kaynak eseri dışarıda bırakıp aynı kategoriden en çok 8 gerekçeli sonuç veren API yerel istekte doğrulandı. Tarayıcıda seçim ve geri dönüş akışının manuel kabul testi henüz yapılmadı. |
| Gerçek görsel, tür, kısa açıklama | **Kısmi** | Yerel veritabanındaki 15 kitabın doğrulanmış kapağı, kaynak/atıf alanı ve esere özel kısa açıklaması var. Film, dizi ve oyundan **45 kayıt** hâlâ görselsiz ve kalıp açıklamalı; arayüz bunlarda kategori simgesi gösteriyor. Türler kartta görünüyor. Görsel kredisi/kaynak bağlantısı API'de var, arayüzde gösterilmiyor. |
| Giriş/kayıt ve kaydetme | **Kısmi** | Backend oturum, CSRF, favori ekleme/çıkarma ve kullanıcılar arası ayrımı test ediyor. Arayüz giriş gerektiren kaydetme ve girişten sonra aynı esere dönme koduna sahip. Birleşik arayüzde gerçek tarayıcıdan baştan sona test henüz yapılmadı. |
| Kaydedilenler ekranı | **Kısmi** | Backend `GET /api/me/saved` ile kullanıcının tam eser kartlarını döndürüyor; kalıcılık ve hesap ayrımı testli. Arayüz bu ucu çağırmıyor, ilk katalog listesini favori ID'leriyle filtreliyor. Mevcut 60 MVP kaydında görülebilir; katalog 100'ü aşınca eksik kart riski var. |
| Boş/yüklenme/hata durumları | **Kısmi** | Arayüzde katalog yüklenmesi, boş arama ve bazı API hata ekranları var. Telefon, klavye ve ağ kesintisiyle uçtan uca kabul kontrolü yapılmadı. |

**Bugün hedeflendiği gibi çalışmayanlar:** 45 film/dizi/oyun kartında istenen gerçek görsel ve özgün açıklama yok; görsel kaynak/atıf bilgisi kullanıcıya gösterilmiyor. Tek eser önerisi ve kaydetme için API/kod kontrolleri var, ancak tarayıcı kabul testi henüz yok.

## Doğrulama ve yerel veri

- `backend` içinde `python -m pytest -q`: **20 test geçti**, Starlette TestClient için 1 üçüncü taraf kullanım uyarısı çıktı; test hatası yok.
- `frontend` içinde `npm run build`: TypeScript kontrolü ve Vite üretim derlemesi **geçti**. Vite geliştirme sunucusu yerelde açıldı. Bu kontroller tek başına tarayıcı akışının tamamını kanıtlamaz.
- Yerel PostgreSQL: Docker veritabanı sağlıklı, Alembic sürümü **0002 (head)**, toplam **75 kayıt** (beş kategoride 15'er). Bunun 60'ı dört MVP kategorisinde listeleniyor.
- Yerel API kontrolü: kitap listesi `200` ve 15/15 görselli; müzik filtresi `422`; tek kitap için aynı kategori önerisi `200` ve 8 sonuç verdi.
- 28 Ekim kontrolü: Dune başlık araması HTTP `200` ile tek kayıt; seçilen Dune için öneri ucu HTTP `200` ile 8 kitap döndürdü. Frontend derlemesi ve 20 backend testi yeniden geçti. Tarayıcı otomasyonu URL güvenliği denetiminde durduğu için bu kontrol gerçek kullanıcı tıklamasının yerini tutmaz.
- `python -m app.catalog` kalite raporu: **45 sorunlu MVP kaydı** (film 15, dizi 15, oyun 15; kitap 0). Bu sayı bu bilgisayardaki güncellenmiş veritabanına aittir.

## Açık işler ve öncelik

1. **P0 — Tarayıcı kabulünü tamamla:** Dört kategori, tek eser seçimi ve aynı kategori önerisi kodda bağlıdır. Misafir olarak arama → seçim → öneri → detay → geri dönüş akışı gerçek tarayıcıda kontrol edilmeli; çoklu kaynak, müzik ve kategoriler arası akış sonraki sürüme kalır.
2. **P0 — Katalog verisini tamamla:** 45 film/dizi/oyun kaydı için doğru görsel, kullanım/atıf bilgisi ve esere özel açıklama insan kontrolünden geçirilsin. Aday arama ve güvenli JSON güncelleme araçları hazır; TMDB/RAWG adaylarını canlı sorgulamak için yerel geliştirici anahtarları gerekiyor. Anahtarlar repoya eklenmemeli.
3. **P1 — Kaydetme akışını tarayıcıda doğrula:** Misafir kaydet → giriş/kayıt → aynı eser; sayfa yenileme, çıkış/giriş, kaydı kaldırma ve iki hesap ayrımı. Kaydedilenler ekranı `/api/me/saved` ucunu kullansın.
4. **P1 — Öneri kalitesini iyileştir:** Stardew Valley için sıcak/2D yaşam simülasyonu benzerleri zayıf; souls-like başlangıç eseri ve uygun komşular katalogda yok. Eser/etiket ekleme sonrası insan değerlendirmesi tekrarlanmalı.
5. **P1 — Yayın öncesi kontrol:** Görsel kaynak koşulları ve atıf arayüzde tamamlanmalı; telefon, klavye, boş sonuç ve ağ hatası akışları denenmeli. Sunucuya dağıtım henüz yapılmadı.

## Çalıştırma ve yeni kurulum notu

Bu bilgisayarda `.env`, Python sanal ortamı, npm paketleri ve PostgreSQL hazır. İlk kurulumda Docker veritabanını başlatıp Alembic migration'ı ve `backend/seed.py` dosyasını çalıştırmak gerekir. **Seed tek başına doğrulanmış kitap kapaklarını yüklemez:** `backend/data/catalog-books.json` ayrıca `python -m app.catalog_update data/catalog-books.json --apply` ile uygulanmalıdır. Var olan veritabanında seed'i tekrar çalıştırmak veri güncellemesi yerine geçmez. Arayüzde `vite` bulunamazsa `frontend` klasöründe `npm ci --include=dev` gerekir. Ayrıntılı başlatma komutları kök [README](../README.md) içindedir; README'nin eski “yalnız yer tutucu görseller” açıklaması bu yerel verinin güncel durumunu yansıtmıyor.

## Ekip sınırı ve sunum kanıtı

Backend ve katalog araçları ajan desteğiyle geliştirildi; Bahar'ın frontend dalı incelenip birleştirildi. Bu rapor **arayüzde doğrulanmış davranışı** API'de yalnızca mevcut olan özellikten ayırır. Sunumda teknoloji seçimi, API sözleşmesi, test çıktısı, katalog kaynak kararı, tespit edilen uyumsuzluklar ve bunların düzeltme sırası birlikte gösterilebilir.
