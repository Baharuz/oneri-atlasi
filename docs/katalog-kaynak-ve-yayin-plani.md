# MVP-1 katalog kaynak ve yayın planı

**Durum:** Kaynak seçimi taslağı, 26 Ekim 2026. Sağlayıcı hesabı/anahtarı veya eser eşleştirmesi henüz tamamlanmadı. Bahar'ın arayüz dosyalarına dokunulmaz.

## Yayın ölçütü

MVP'de görünen dört kategorideki her eserde doğru esere/edisyona ait gerçek görsel, esere özgü kısa Türkçe açıklama, en az bir tür etiketi, görselin sağlayıcı kaydı ve sağlayıcının istediği atıf bulunmalı. Boş görsel veya seed'in kalıp açıklaması olan kayıt yayına hazır sayılmaz. Uydurma URL, başka eser/edisyon kapağı ve salt HTTP adresi kabul edilmez. Sağlayıcının API sonucu ve görseli insan gözden geçirir. Dış API çağrısı öneri sırasında yapılmaz; doğrulanmış kayıtlar önceden PostgreSQL'e işlenir.

## Olası kaynaklar ve koşullar

| Kategori | Kaynak | Uygulama kararı / kontrol |
| --- | --- | --- |
| Kitap | Open Library Search/Works + Covers | Eser ve belirli baskı kapağı eşleştirilecek. Kapaklar için doğrudan covers.openlibrary.org URL'si kullanılacak; toplu tarama yapılmayacak. Kapak bulunmamasını kontrol etmek için ?default=false kullanılabilir. Eser bağlantısı/teşekkür kredilerde verilecek. |
| Film/dizi | TMDB API ve image CDN | API anahtarı gerekir. Eserin film mi dizi mi olduğu, yılı ve poster yolu doğrulanacak. Görsel URL'si resmî yapılandırmadan kurulur. Ticari olmayan kullanımda TMDB atfı, onaylı logo ve resmî bildirim About/Credits alanında gerekir. Ticari kullanım için ayrı lisans görüşmesi gerekir. |
| Oyun | RAWG API | API anahtarı gerekir. Eser ve oyun görseli doğrulanır. RAWG verisinin/görselinin kullanıldığı sayfadan etkin RAWG bağlantısı ve atıf gerekir. Güncel plan ve kullanım sınırları hesap açarken yeniden kontrol edilir. |

**Resmî belgeler:** https://openlibrary.org/dev/docs/api/covers ; https://openlibrary.org/dev/docs/api/search ; https://developer.themoviedb.org/docs/image-basics ; https://developer.themoviedb.org/docs/faq ; https://rawg.io/apidocs ; https://rawg.io/tos_api

Sağlayıcıların kendi API belgesi görsel üzerindeki bütün üçüncü taraf haklarını garanti etmez. Özellikle ticari yayın kararı verilirse koşullar yeniden değerlendirilecek. API anahtarları depoya veya manifest dosyasına yazılmayacak. Mevcut uygulama yerelde eğitim amaçlıdır; internet yayını ayrıca gözden geçirilir.

## Veri işleme sırası

1. Katalog güncelleme aracı mevcut eseri kalıcı source + source_id ile eşleştirir; Content ID'si ve kullanıcı kaydı korunur. Manifest doğrulaması ve dry-run gerçek veriye yazmadan önce yapılır.
2. Her kategoriden 2-3 eserlik pilot seçilir. Doğru eser/baskı, çalışır HTTPS görsel, açıklama ve sağlayıcı URL'si insan tarafından doğrulanır. Araçla güncellenir; API yanıtı ve kalite raporu kontrol edilir.
3. Aynı iş 15 eser/kategoriye genişletilir. Eşleşmeyen, görseli bulunmayan veya kullanım koşulu belirsiz kayıt doğrulanıncaya kadar yayına alınmaz; gerekiyorsa görünür katalog küçültülür, fakat her dört kategoride anlamlı öneri havuzu korunur.
4. Bahar'ın kart ve detay tasarımı, API'nin görsel ve kredi alanlarını kullanır. Sağlayıcının zorunlu link/logo/bildirimi arayüz kabul kontrolünde doğrulanır. Bu tasarım işini Bahar üstlenir; backend görevi arayüze müdahale etmez.
5. Yerel PostgreSQL üzerinde migration, katalog güncellemesi, arama/öneri/kaydetme ve boş/hatalı görsel durumları uçtan uca denetlenir. Sonra sunucuya geçişte DB yedeği ve ortam değişkenleri ayrı ele alınır.

## Bekleyen kararlar

- Haktan'ın TMDB ve RAWG geliştirici anahtarlarına erişimi var mı? Yoksa hesaplar ve kullanım koşulları doğrulandıktan sonra oluşturulmalı.
- Eser adlarının Türkçe/İngilizce karşılığı ve kitap baskısı hangisi? Eşleştirme kayıt bazında doğrulanmalı.
- Öneri kalitesi için 15 eser/kategori yeterli mi? Gerçek kullanıcı senaryolarıyla bakılmalı.

## Kitap pilotu için aday eşleşmeler (henüz yayına alınmadı)

26 Ekim 2026'da Open Library Search API başlık + yazar sorgularında Dune / Frank Herbert için OL893414W ve cover ID 11481354; Neuromancer / William Gibson için OL27258W ve cover ID 283860; Dracula / Bram Stoker için OL85892W ve cover ID 12216503 döndü. Bunlar yalnızca adaydır. Her kapak URL'si ?default=false ile gerçekten bulunuyor mu, doğru eseri ve uygun baskıyı gösteriyor mu diye görsel kontrol yapılmadan manifestte kullanılmaz. 1984 ve Küçük Prens aramaları benzer ad/uyarlama sonuçları verdiği için ilk pilotta seçilmedi.

Üç adayın Open Library cover ID URL'si 26 Ekim 2026'da ?default=false ile 200/image/jpeg döndü; küçük kapak önizlemeleri insan tarafından görsel olarak incelendi ve Dune, Neuromancer, Dracula başlık/yazar eşleşmeleri görüldü. Bunlar Türkçe baskı kapakları olmak zorunda değildir; ürünün baskı tercihi ayrıca kararlaştırılır. Doğrudan adresler sırasıyla https://covers.openlibrary.org/b/id/11481354-M.jpg, https://covers.openlibrary.org/b/id/283860-M.jpg, https://covers.openlibrary.org/b/id/12216503-M.jpg şeklindedir.

## Yerel pilot sonucu (26 Ekim 2026)

Alembic 0002 migration yerel PostgreSQL'e uygulandı. 15 kitabın Open Library kapakları doğrudan görsel önizlemeyle doğrulandı; eser özelinde Türkçe açıklamalar ve kaynak/atıf bilgileri backend/data/catalog-books.json dosyasına işlendi. dry-run sonrası apply yapıldı; ikinci dry-run değişiklik döndürmedi. TestClient ile kitap kataloğu 200, 15 kayıt, 15 dolu image_url ve image_credit verdi. Salt okunur kalite raporunda 45 kayıt kaldı: 15 film, 15 dizi, 15 oyun. Bu durum yerel geliştirme veritabanı içindir; dosyayı alan başka geliştirici migration ve manifest apply işlemlerini kendi veritabanında çalıştırmalıdır. Kapaklar çeşitli dil/baskılardan seçilmiştir; Türkçe baskı görseli gerekip gerekmediği ürün kararıdır.
