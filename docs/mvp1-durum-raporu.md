# Güncel durum raporu

Güncelleme: 24 Kasım 2026.

- Katalog: dört kategoride toplam 500 eser; temsili SVG görseller.
- Kullanıcı farklı kategorilerden 1–5 kaynak seçer. Filtre değişince seçimler korunur; altıncı seçim açıklanarak engellenir.
- Tema, tür ve atmosfer tercihleri ile Benzer / Keşfet / Şaşırt modları API'ye iletilir.
- Hesaba özel kalıcı tercihler, kaydedilen/beğenilen eserler ve son 20 istekteki seçimler öneri hafızasına katılır. Beğenilmeyen eserler çıkarılır.
- Profilde geçmişin kaynak adları ve sonuç sayısı görünür. Sonuçları aç, yeni öneri isteği yapmadan eski sırayı gösterir; yeni kayıtlarda skor/gerekçe saklanır. Eski ID kayıtlarında olmayan gerekçe uydurulmaz. Katalogdan kaldırılmış sonuçlar sayıyla bildirilir.
- Detay ekranının geri düğmesi, açıldığı Kaydedilenler / Öneriler / Seçim ekranına döner. Geçmiş sonuçları profile döner.
- `0005` migration'ı eser sahibi ve bilgi kaynağı alanlarını ekler. `python seed.py` kaynakla doğrulanmış 9 eserin yıl/eser sahibi bilgisini doldurur. Kalan **491 eserin bu alanları eksiktir**; arayüz doğrulanmadığını açıkça gösterir. 500 eserin metadata zenginleştirmesi tamamlanmış değildir.

## Doğrulama

`frontend`: `npm ci`, `npm test`, `npm run build`.
`backend`: `python -m pytest -q`.

Arayüz testleri Vitest + jsdom + Testing Library ile gerçek React bileşenini kullanır; çoklu seçim, beş sınırı, kategori filtresinde koruma, tür/atmosfer ve mod payload'ı, kaydedilenlere geri dönüş, geçmiş açma, dislike/geri al ve profil kaydetmeyi kapsar. Ağ yanıtları taklit edilir; bu testler tarayıcı görsel kontrolünün yerine geçmez.

Backend testleri SQLite üzerinde çalışır. PostgreSQL ve gerçek tarayıcı görsel kontrolü ayrıca yapılmalıdır.
