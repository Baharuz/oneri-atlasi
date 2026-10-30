# MVP-1 API sözleşmesi

**Güncelleme:** 30 Ekim 2026

Katalog dört kategoriden (`kitap`, `film`, `dizi`, `oyun`) 125'er eser içerir. Arama ve aynı kategori önerisi misafire açıktır. Kaydetme ve kaydedilenler oturum gerektirir.

| İşlem | API | Yanıt |
| --- | --- | --- |
| Katalog/başlık arama | `GET /api/contents?category=oyun&q=Stardew` | `Content[]`, en çok 500 eser |
| Eser detayı | `GET /api/contents/{id}` | `Content` veya 404 |
| Öneriler | `GET /api/contents/{id}/recommendations` | `{source, results}`; aynı kategoride en çok 8 sonuç |
| Kayıt/giriş/çıkış | `POST /api/auth/register`, `/login`, `/logout` | Oturum/CSRF çerezleri |
| Oturum | `GET /api/me` | Kullanıcı ve `favorites` ID listesi; misafire 401 |
| Kaydet/kaldır | `PUT` / `DELETE /api/me/contents/{id}/favorite` | `{ok: true}`; oturum ve CSRF gerekir |
| Kaydedilenler | `GET /api/me/saved` | Tam `Content[]`; katalog sayfalamasından bağımsız |

`Content`: `id`, `category`, `title`, `description`, `genres`, `themes`, `moods`, `pace`, `audience`, `language`, `year`, `image_url`, `image_credit`, `image_source_url`, `source`, `source_id`. `image_url` yerel özgün temsili SVG dosyasına, `image_source_url` kaynak dosyasına işaret eder. Görseller resmî kapak/afiş değildir.

Tarayıcı istekleri `credentials: include` kullanır; yazma istekleri `X-CSRF-Token` gönderir. Geçersiz giriş 401, mevcut e-postayla kayıt 409, eksik CSRF/izin verilmeyen Origin 403, bulunmayan eser 404, geçersiz istek 422 döner. Arayüz yüklenme, boş sonuç ve ağ hatası durumlarını gösterir.

Şema geçiş zinciri `0001` → `0002` (görsel kredi/kaynak alanları) → `0003` (kullanılmayan kategori temizliği) → `0004` (tempo/hedef kitle) biçimindedir. Seed mevcut kullanıcı ve kayıt verisini koruyarak kataloğu günceller.
