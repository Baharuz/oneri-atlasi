# MVP-1 API sözleşmesi ve backend incelemesi

**Durum:** Kodla karşılaştırılmış sözleşme taslağı, 22 Ekim 2026. Aşağıdaki uçlar backend'de mevcut. Bahar'ın ekran akışıyla birlikte gözden geçirilip kesinleştirilecek.

## Kapsam

İlk sürümde ziyaretçi dört kategoriden (kitap, film, dizi, oyun) birini seçer, **eser adına** göre arar, tek bir eser seçer ve aynı kategoriden öneriler görür. Eser kartında gerçek kapak/afiş, başlık, türler, kısa eser açıklaması ve öneriyse gerekçe görünür. Giriş yapmadan arama ve öneri açıktır; kaydetme ve kaydedilenleri görme hesap gerektirir. Kategori değiştiren öneri, türle arama ve eser niteliği seçimi sonraki sürümlerdedir.

## Uçlar ve ekran bağlantısı

| Akış | API | Durum | Not |
| --- | --- | --- | --- |
| Katalog/başlık arama | `GET /api/contents?category=oyun&q=Stardew` | Mevcut | Yanıt `Content[]`, başlığa göre kısmi arama; en çok 500 kayıt. Varsayılan listede yalnızca dört MVP kategorisi. |
| Eser ayrıntısı | `GET /api/contents/{id}` | Mevcut | Yanıt `Content`; olmayan ID için 404. |
| Tek eserden aynı kategoriye öneri | `GET /api/contents/{id}/recommendations` | Mevcut | Yanıt `{source: Content, results: Recommendation[]}`. Tek kaynak ve aynı kategori sunucu tarafından garanti edilir; giriş/CSRF gerekmez. |
| Kaydol/giriş/çıkış | `POST /api/auth/register`, `/login`, `/logout` | Mevcut | E-posta + şifre; başarılı giriş oturum ve CSRF çerezi kurar. Çıkış CSRF doğrular. |
| Oturum/kayıtlı ID'ler | `GET /api/me` | Mevcut | 401 ise ziyaretçi. `favorites: number[]` kaydedilmiş eser ID'leri. |
| Kaydet/kayıttan çıkar | `PUT` / `DELETE /api/me/contents/{id}/favorite` | Mevcut | Giriş ve CSRF gerekir. Başarılı yanıt `{ok: true}`; ardından `/api/me` ile durumu tazele. |
| Kaydedilen eser kartları | `GET /api/me/saved` | Mevcut | Yanıt başlık ve ID'ye göre sıralı `Content[]`. Giriş gerekir. `/api/contents` için 500 kayıt sınırına takılmadan kartlar yüklenir. |

`Content` alanları mevcut yanıtla aynı kalır: `id`, `category`, `title`, `description`, `genres`, `themes`, `moods`, `language`, `year`, `image_url`, `image_credit`, `image_source_url`, `source`, `source_id`. `category` değerleri MVP ekranında `kitap | film | dizi | oyun`. Kitap kategorisinde 15 kayıt yerel pilotta doğrulanmış görsel ve eser özelindeki açıklamayla güncellendi; film, dizi ve oyundaki 45 kayıt hâlâ bu verileri bekliyor. Ön yüz boş resmi bir kategori simgesiyle kalıcı olarak gizlememeli; kayıt yayına alınmadan veri düzeltilmelidir.

Öneri ucu için örnek yanıt şekli (temsili içerik, gerçek sıralama veya görsel URL'si taahhüdü değildir):

```json
{
  "source": {
    "id": 12, "category": "oyun", "title": "Stardew Valley",
    "description": "Eser özelinde kısa açıklama", "genres": ["simülasyon"],
    "themes": ["dostluk"], "moods": ["sakin"], "language": "en",
    "year": 2016, "image_url": "https://ornek-kaynak/gercek-gorsel.jpg",
    "image_credit": "Görsel sağlayıcı", "image_source_url": "https://ornek-kaynak/eser",
    "source": "local", "source_id": "oyun-1"
  },
  "results": [
    {"content": {"id": 13, "category": "oyun", "title": "Örnek Oyun", "description": "Eser açıklaması", "genres": ["simülasyon"], "themes": ["dostluk"], "moods": ["sakin"], "language": "en", "year": null, "image_url": "https://ornek-kaynak/gercek-gorsel-2.jpg", "image_credit": "Görsel sağlayıcı", "image_source_url": "https://ornek-kaynak/eser-2", "source": "local", "source_id": "oyun-2"}, "reason": "dostluk ve sakin tercihlerinle örtüştüğü için önerildi.", "score": 3.5}
  ]
}
```

`score` sıralama sinyalidir, olasılık veya yüzde değildir; kullanıcıya gösterilmesi gerekmez. Eşleşme yoksa `results: []` döner. Sonuçlar aynı kategoridedir, kaynak eserin kendisini içermez ve mevcut algoritmanın üst sınırı sekizdir.

## Oturum ve hata davranışı

- Tarayıcı istekleri `credentials: 'include'` ile gönderir. Giriş sonrası yazma isteklerinde `csrf` çerezinin değeri `X-CSRF-Token` başlığına eklenir; sunucu ayrıca izin verilen `Origin` değerini doğrular. Bahar'ın mevcut `api()` yardımcı işlevi bunu yapıyor.
- Giriş yapılmamışken `GET /api/me`, kaydetme ve kaydedilenler 401 döner. Ön yüzde kaydetme tıklaması giriş ekranına götürür; başarılı girişten sonra kullanıcı ilgili esere dönebilmelidir.
- Bulunmayan eser 404; geçersiz kategori ve istek 422; yanlış giriş 401; mevcut e-postayla kayıt 409; geçersiz CSRF/kaynak 403. Yüklenme, boş arama/öneri ve ağ hatası için ayrı ekran durumları gerekir.
- Kaydetme PostgreSQL'deki kullanıcı-eser etkileşimine yazılır. Sayfa yenilenince ve çıkış/giriş sonrası aynı hesabın kayıtları geri gelir. Yerel geliştirme ortamında PostgreSQL de yerel olarak çalışır; tarayıcı `localStorage` favori kaynağı değildir.

## Kod incelemesinden çıkan işler

1. **Öneri sözleşmesi:** Mevcut `POST /api/recommend` bir ila beş kaynak ve istenen herhangi bir hedef kategoriye izin veriyor. Yeni GET ucu mevcut sıralama işlevini yeniden kullanarak tek kaynak/aynı kategori kuralını açıkça uyguluyor; eski uç ileri sürüm için korundu. İlgili odaklı test eklendi.
2. **Kaydedilenleri yükleme:** `/api/me` yalnızca favori ID'lerini döndürüyor. `/api/me/saved` kullanıcının tam eser kartlarını döndürür; katalogdaki 500 kayıt sınırından etkilenmez. Mevcut ön yüz hâlâ katalog listesindeki favori ID'lerini eşliyor; ekran bu uca bağlanmalı.
3. **Katalog kalitesi:** Başlangıç verisi dört kategoride 25'er, toplam 100 kayıt. Seed eksik kayıtları ekler ve mevcut kayıtların açıklama/görsel alanlarını değiştirmez. İlk 60 kaydın açıklaması kalıp metinle oluşturuldu; yeni 40 kaydın esere özel kısa açıklaması vardır. Seed görsel doldurmaz. `backend` dizininden `python -m app.catalog` komutu boş görselleri ve kalıp açıklamaları JSON olarak raporlar; veri değiştirmez. Yayınlanacak her kayıt için doğru görsel ve kaynak atfı ayrıca doğrulanmalıdır.
4. **Doğrulama:** Backend testlerinde misafir başlık arama/aynı kategori öneri, dört kategori filtrelemesi, iki kullanıcı arasında kaydetme ayrımı, çıkış/giriş sonrası kalıcılık, kayıttan çıkarma ve veri kalitesi raporu kapsanıyor. Ajan çalıştırmasında 8 test geçti. PostgreSQL üzerinde yerel uçtan uca kontrol ayrıca yapılmalı; otomatik testler şu anda bellek içi SQLite kullanıyor.

## Uygulama sırası ve ekip sınırı

1. Haktan/Codex: bu sözleşmeyi Bahar'ın ekran akışıyla karşılaştırıp onaylanan değişiklikleri kaydeder.
2. Backend ajanının ilk dar görevi öneri GET ucunu; onaylanan ikinci görevi kaydedilenler GET ucunu, dört kategori filtresini, kalite raporunu ve davranış testlerini ekledi. Ön yüze ve katalog verisine dokunmadı.
3. Haktan/Codex: görsel ve açıklama kaynağını kararlaştırır; küçük bir eser kümesinde doğrulanmış veri akışını kurar, sonra tüm yayın kataloğuna uygular.
4. Bahar: ekranları kararlaştırılan yanıt şekline bağlar; arama, öneri, giriş ve kaydetme durumlarını tasarlar.

Sunum kanıtı olarak bu sözleşmenin sürümü, ajan görev metni, incelenen diff, test çıktısı ve katalog veri kaynağı kararı saklanır.
