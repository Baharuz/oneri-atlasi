# Öneri Atlası

Kitap, film, dizi ve oyun arasında ortak tema ve atmosferlere göre öneri veren Türkçe öğrenci projesi. React + Vite + TypeScript arayüzü, FastAPI + SQLAlchemy API'si, PostgreSQL ve Alembic kullanır. API anahtarı gerekmez.

## Windows / PowerShell kurulumu

Önkoşullar: Python 3.11+, Node.js 20+, Docker Desktop (Linux container etkin).

```powershell
cd C:\YOL\turkce-oneri
Copy-Item .env.example .env
docker compose up -d db
cd backend
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Get-Content ..\.env | ForEach-Object { if ($_ -match '^([^#=]+)=(.*)$') { [Environment]::SetEnvironmentVariable($matches[1],$matches[2],'Process') } }
alembic upgrade head
python seed.py
uvicorn app.main:app --reload --port 8000
```

Başka bir PowerShell penceresinde:

```powershell
cd C:\YOL\turkce-oneri\frontend
npm install
npm run dev
```

Tarayıcıda `http://localhost:5173` adresini açın. Vite `/api` isteklerini `localhost:8000` adresine iletir. Test için backend klasöründe `pytest -q`, arayüz derlemesi için frontend klasöründe `npm run build` çalıştırın.

## Ortam değişkenleri

`.env.example` örneği yerel geliştirme içindir. `DATABASE_URL` PostgreSQL bağlantısını, `SESSION_SECRET` imzalı oturum çerezini, `FRONTEND_ORIGIN` izin verilen tarayıcı kaynağını belirler. Üretimde uzun ve rastgele `SESSION_SECRET`, HTTPS ile `COOKIE_SECURE=true` ve dağıtım topolojinize uygun `COOKIE_SAMESITE` kullanın. Çerezli yazma istekleri CSRF tokeni ve Origin doğrulaması gerektirir. `.env` Git'e alınmaz.

## Özellikler

- Hesapsız: 1–5 içerik seçimi, dört adımlı atlanabilir tercih testi, kategori bazında gerekçeli sonuçlar.
- Hesaplı: kayıt, giriş, çıkış, kalıcı tercihler, favoriler, değiştirilebilir beğeni/beğenmeme, öneri geçmişi ve “Bugüne özel öneri al”.
- Anlık test cevapları profili değiştirmez; yalnızca açık kaydetme düğmesi bunu yapar.
- API her kullanıcının özel kaydını oturumdaki kullanıcı kimliğiyle sınırlar. Şifreler Argon2 ile hashlenir.
- Başlangıç kataloğunda kategori başına 25, toplam 100 eser vardır. Yeni eklenen 40 eserin kısa açıklamaları ve etiketleri proje için elle hazırlanmıştır; görselleri ve kaynak atıfları henüz eklenmemiştir. Var olan bir veritabanını genişletmek için `backend` dizininde `python seed.py` komutunu yeniden çalıştırın; mevcut eser kayıtları korunur.

## Öneri algoritması

Kaynak içeriklerin tema etiketleri 2, atmosfer etiketleri 1,5, aynı kategorideki türleri 1 ağırlık alır. Profilde kayıtlı tema/atmosferler 1,5/1; anlık testte işaretlenen özellik/atmosferler 5/3 ağırlık alır. Adayın eşleşen etiket ağırlıkları toplanır. Beğenilmeyen ve seçilen kaynak içerikler çıkarılır. “Keşfet” ve “Şaşırt” seçenekleri yalnızca en az bir gerçek eşleşmesi olan adaylarda tekrar eden etiketlere çeşitlilik cezası uygular. Her kategorinin sonuçları ayrı sıralanır ve gerçek eşleşen en güçlü iki etiket gerekçede gösterilir. Sayısal skor arayüzde olasılık veya doğruluk yüzdesi olarak gösterilmez.

## Sağlayıcılar ve sınırlar

`CatalogProvider` arayüzü ileride katalog verisi getiren adaptörler içindir. TMDB, Open Library ve IGDB canlı bağlantıları **ertelendi**. Öneri sıralamasını bu API'ler değil, uygulamanın kendi algoritması yapar. Şimdilik kapak görselleri yerine yerel kategori yer tutucuları kullanılır. Katalog küçük ve elle hazırlanmış olduğundan bazı dar tercih birleşimlerinde uygun sonuç bulunmayabilir; arayüz bunu belirtir. Geliştirme ortamında Docker Desktop çalışır durumda olmalıdır.
