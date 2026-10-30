# MVP-1 durum raporu

**Güncelleme:** 30 Ekim 2026

## Kapsam

Katalog kitap, film, dizi ve oyun kategorilerinden 125'er, toplam 500 gerçek eserden oluşur. Eser seçimi, aynı kategoride gerekçeli öneriler, hesapla kaydetme ve kaydedilenler ekranı uygulamadadır. Müzik kategorisi `0003` geçişiyle kaldırıldı. `0004`, tempo ve geniş hedef kitle etiketlerini ekler; bunlar resmî yaş sınıflandırması değildir.

## Veri ve görseller

`python seed.py` mevcut kaynak kimlikleriyle upsert yapar; kullanıcıları ve etkileşimleri silmez. Katalogdaki açıklamalar esere özel Türkçe metinlerdir. Her eser için `/art/` altında özgün, temsili SVG bulunur. Bunlar resmî kapak veya afiş değildir. Kart ve detay ekranı kaynak bağlantısını ve görsel kredisini gösterir. Kaynak/kullanım açıklaması [görsel notunda](../frontend/public/art/README.md) yer alır.

## Doğrulama

- Yerel SQLite üzerinde seed sonrasında 500 kayıt ve kategori başına 125 kayıt doğrulandı.
- `python -m app.catalog_audit --check-urls` 500 kaydın açıklamasını, görselini, kredi ve kaynak alanlarını, SVG dosyasını ve başlık eşleşmesini kontrol etti; hata sayısı sıfırdı.
- Backend testleri 27/27 geçti; frontend üretim derlemesi geçti.
- Gerçek tarayıcıda dört kategoride arama, seçim, öneri ve detay; misafir kaydetme, kayıt, yenileme, kaydedilenlerden kaldırma ve tekrar giriş; mobil görünüm, klavye, boş sonuç ve ağ hatası durumları denendi.

Bu rapor yerel geliştirme ortamına ilişkindir. Dağıtım ve bağımsız kullanıcı kabul testi ayrı kararlardır.
