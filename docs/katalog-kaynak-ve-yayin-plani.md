# Katalog görsel kaynağı ve yayın notu

**Güncelleme:** 30 Ekim 2026

Katalog 125 kitap, 125 film, 125 dizi ve 125 oyun içerir. Görseller eserlerin resmî kapakları veya afişleri değildir. Her eser için başlık, kategori ve etiketlerden üretilen özgün temsili SVG kullanılır. Üçüncü taraf görseli, API anahtarı veya haricî görsel barındırıcısı gerekmez.

`backend/app/catalog_art.py` üretim kaynağıdır. 500 çıktı `frontend/public/art/` dizininde sürümlenir. `image_url` yerel SVG yolunu, `image_source_url` depodaki dosya bağlantısını, `image_credit` proje atfını ve proje içi kullanım bilgisini taşır. Arayüz atfı ve tıklanabilir kaynak bağlantısını kartta ve detayda gösterir.

`python -m app.catalog_audit --check-urls` her katalog satırında bu alanları, dosya varlığını, SVG yapısını ve eser başlığını doğrular. Bu kontrol dış kaynak lisansı veya gelecekteki dağıtım koşulları hakkında hüküm vermez. Proje dışı kullanım için görsel hakları ve eser adlarının kullanım bağlamı ayrıca gözden geçirilmelidir.

Eski Open Library/TMDB/RAWG pilotu ve `0002` geçişi tarihsel geliştirme aşamasıydı. Güncel katalog seed'i `0003` şemasında çalışır; eski sağlayıcı görselleri seed tarafından kullanılmaz.
