# MVP-1 geliştirme günlüğü

Bu günlük sunumda anlatılabilecek karar ve doğrulama izidir. Kod/çıktı yerine geçmez. Değişiklikler henüz yerel çalışma ağacındadır; uzak depoya yayımlandığı iddia edilmez.

## 22 Ekim 2026

- Kullanıcı isterleri dört kategori, başlığa göre arama, tek eserden aynı kategoriye gerekçeli öneri, hesapla kaydetme ve gerçek görsel olarak sınırlandı. Bahar kullanıcı akışı ve arayüzü üstlendi; backend/API tarafı ayrı yürütüldü.
- Aion CLI (DeepSeek) önce dar bir görevle GET /api/contents/{id}/recommendations ve odaklı testini ekledi. İlk kapsamın token harcamasını kullanıcı izleyebilsin diye görev küçük tutuldu.
- Kullanıcı onayından sonra ikinci görevde GET /api/me/saved, dört kategori filtresi, kalite raporu ve testler eklendi. Kod farkı lead tarafından incelendi; ajan 8 backend testinin geçtiğini bildirdi.

## 26 Ekim 2026

- Kullanıcı MVP-1 işlerine devam yetkisi verdi; Bahar'ın arayüz ve kullanıcı akışına dokunulmaması ayrıca teyit edildi.
- Aion CLI, kaynak/atıf alanları için Alembic 0002 migration ve doğrulanmış manifesti güvenli, tekrarlanabilir güncelleyen backend aracı ekledi. 13 test geçti. Lead migration'ı yerel PostgreSQL'de çalıştırıp 0002 (head) olduğunu gördü.
- Lead, Open Library resmî Search/Covers kaynaklarında 15 kitabın eser/kapak eşleşmelerini aradı; kapakları görsel olarak gözden geçirip eser özelinde kısa açıklamalarla katalog manifesti hazırladı. Yerel dry-run, apply ve ikinci dry-run (sıfır değişiklik) uygulandı. API 15/15 kitap için görsel ve atıf döndürdü; kalite raporunda film/dizi/oyun için 45 eksik kayıt kaldı.
- Aion CLI, TMDB ve RAWG için yalnız aday çıkaran, veritabanına yazmayan araç ve mock testler hazırladı. Lead resmî RAWG belgesiyle kodu karşılaştırırken yanlış API hostunu ve HTTP görsel kabulünü buldu; takip göreviyle düzeltildi. Yerel backend test çalıştırması: 19 passed, 1 üçüncü taraf TestClient uyarısı. Canlı sağlayıcı çağrısı henüz yapılmadı; anahtarlar gerekli.
- Manuel öneri gözlemi: Dune, Arrival, Dark için başlangıç eşleşmeleri makul; Stardew Valley için mevcut oyun kataloğu cozy/yaşam simülasyonu komşularından yoksun. Bu gözlem otomatik kalite ölçümü değildir.

## Açık kalanlar

- Film, dizi ve oyun eserlerinin doğrulanmış görsel, özgün açıklama ve kaynak/atıf verisi. TMDB ve RAWG geliştirici anahtarları kullanıcı tarafından yerel ortamda sağlanmalı; depoya konmamalı.
- Bahar'ın hazırladığı arayüzün yeni API sözleşmesine bağlanması ve zorunlu sağlayıcı atıflarının tasarıma yerleştirilmesi Bahar'ın alanıdır.
- Oyun kataloğunun kullanıcı örneklerine göre zenginleştirilmesi, öneri kalitesinin yeniden değerlendirilmesi, dört kategori uçtan uca kabul kontrolü ve sunucuya taşıma hazırlığı.
