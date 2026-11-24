# Öneri Atlası

Kitap, film, dizi ve oyun arasında ortak tema ve atmosferlere göre öneri veren Türkçe öğrenci projesi. React + Vite + TypeScript arayüzü, FastAPI + SQLAlchemy API'si, PostgreSQL ve Alembic kullanır. API anahtarı gerekmez.

## Windows / PowerShell kurulumu

Önkoşullar: Python 3.11+, Node.js 20+, Docker Desktop (Linux container etkin).

```powershell
cd C:\YOL\oneri-atlasi
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
cd C:\YOL\oneri-atlasi\frontend
npm install
npm run dev
```

Tarayıcıda `http://localhost:5173` adresini açın. Vite `/api` isteklerini `localhost:8000` adresine iletir. Test için backend klasöründe `pytest -q`, arayüz derlemesi için frontend klasöründe `npm run build` çalıştırın.

## Ortam değişkenleri

`.env.example` örneği yerel geliştirme içindir. `DATABASE_URL` PostgreSQL bağlantısını, `SESSION_SECRET` imzalı oturum çerezini, `FRONTEND_ORIGIN` izin verilen tarayıcı kaynağını belirler. Üretimde uzun ve rastgele `SESSION_SECRET`, HTTPS ile `COOKIE_SECURE=true` ve dağıtım topolojinize uygun `COOKIE_SAMESITE` kullanın. Çerezli yazma istekleri CSRF tokeni ve Origin doğrulaması gerektirir. `.env` Git'e alınmaz.

## Özellikler

- **Profilim** ekranında tema ve atmosfer tercihleri düzenlenip kalıcı kaydedilebilir. Hesaplı öneriler bu tercihlerden, kaydedilen/beğenilen eserlerin tema ve atmosferlerinden ve son 20 öneri isteğinin kaynak/tercihlerinden yararlanır. Hesap bilgisi sunucudaki oturumdan alınır; misafirler ve diğer hesaplar bu hafızayı kullanmaz. Anlık tercihler profilin üzerine yazılmaz.
- Hesapla giriş yapan kullanıcı kartlardaki **Beğen / Beğenme** düğmeleriyle geri bildirim verebilir. Beğenme, eseri mevcut önerilerden ve sonraki öneri isteklerinden çıkarır; son çıkarma işlemi **Geri al** ile geri çevrilebilir. Beğen düğmesine tekrar basmak beğeniyi kaldırır. Kaydedilenler listesi bu işlemle silinmez.
- Öneri modu seçilebilir: **Benzer** (varsayılan), **Keşfet** veya **Şaşırt**. Keşfet ve Şaşırt, eşleşen eserler arasında çeşitliliğe giderek daha fazla ağırlık verir; rastgele veya tamamen ilgisiz eser seçmez. Sonuç ekranı kullanılan modu gösterir.
- Eser seçildikten sonra “Bu eserde neyi sevdin?” alanında isteğe bağlı tema ve atmosfer tercihleri seçilebilir. Tercihler yalnızca o öneri isteğinde kullanılır; kaynak eser değişince temizlenir.
- Hesapsız: başlığa göre arama, kaynak eseri ve hedef kategoriyi seçme, seçilen kategorilerde gerekçeli öneriler. Seçim ekranı 500 eseri 24'erli gruplar hâlinde gösterir; arama tüm kataloğu kapsar.
- Hesaplı: kayıt, giriş, çıkış, favori ekleme/çıkarma, kaydedilen eserler ve öneri geçmişi.
- Kaydetme işlemi kullanıcının hesabına yazılır; geçici ekran seçimi profil kaydını değiştirmez.
- API her kullanıcının özel kaydını oturumdaki kullanıcı kimliğiyle sınırlar. Şifreler Argon2 ile hashlenir.
- Katalogda her kategoriden 125, toplam 500 eser vardır. Açıklamalar eser özelinde Türkçe hazırlanmıştır. Görseller resmî kapak/afiş değildir; eser adlarından ve etiketlerinden `app.catalog_art` ile üretilen özgün, temsili SVG'lerdir. Önce `backend` dizininde `python -m app.catalog_art`, ardından `python seed.py` çalıştırın. Seed, elle düzenlenmiş açıklamaları ve kullanıcı kayıtlarını korur; yerel katalog görsellerini proje görsellerine geçirir.
- Kaydedilenler ekranı doğrudan `GET /api/me/saved` sonucunu gösterir. Görseli olan eserlerde kart ve detay ekranı kaynak atfını bağlantısıyla birlikte gösterir.

## Katalog denetimi

Şema geçişleri `0003` ile kullanılmayan kategoriyi temizler; son sürüm `0004_editorial_metadata` tempo ve hedef kitle etiketlerini ekler. Katalog tamamlanma hedefi kategori başına 125, toplam 500 eserdir. Hedefin karşılanıp karşılanmadığını, mükerrer başlıkları ve boş görsel/atıf/açıklama alanlarını denetlemek için `backend` dizininde:

```powershell
python -m app.catalog_audit
python -m app.catalog_audit --check-urls
```

İkinci komut yerel SVG dosyalarını ve dış kaynak bağlantılarının HTTP yanıtını denetler; proje içi GitHub kaynak bağlantıları yerel dosya/yol eşleşmesiyle doğrulanır. Görseller yalnızca bu proje için üretilmiştir; resmî eser görseli olarak sunulmamalıdır. Denetim kategori başına 125 kayıt bekler.

## Öneri algoritması

Kaynak içeriklerin tema etiketleri 2, atmosfer etiketleri 1, aynı kategorideki türleri 3 ve kategoriler arası ortak türleri 2,5 ağırlık alır. Profilde kayıtlı tema/atmosferler 1,5/1; anlık testte işaretlenen özellik/atmosferler 5/3 ağırlık alır. Adayın eşleşen etiket ağırlıkları toplanır. Beğenilmeyen ve seçilen kaynak içerikler çıkarılır. “Keşfet” ve “Şaşırt” seçenekleri yalnızca en az bir gerçek eşleşmesi olan adaylarda tekrar eden etiketlere çeşitlilik cezası uygular. Her kategorinin sonuçları ayrı sıralanır ve gerçek eşleşen en güçlü iki etiket gerekçede gösterilir. Sayısal skor arayüzde olasılık veya doğruluk yüzdesi olarak gösterilmez.

## Sağlayıcılar ve sınırlar

`CatalogProvider` arayüzü ileride katalog verisi getiren adaptörler içindir. TMDB ve RAWG için salt okunur aday toplama aracı bulunur; bunların kullanımı ilgili API anahtarlarını gerektirir. Öneri sıralamasını dış API'ler değil, uygulamanın kendi algoritması yapar. Görsel yüklenemezse yerel kategori simgesi gösterilir. Bazı dar tercih birleşimlerinde uygun sonuç bulunmayabilir; arayüz bunu belirtir. PostgreSQL kurulumu için Docker Desktop çalışır durumda olmalıdır.

### Hesap hafızasının ağırlığı
Kaydedilen ve beğenilen eserler tekilleştirilir; tema/atmosfer katkıları eser sayısına bölünerek toplam 1,25/0,75 ile sınırlanır. Son 20 isteğin kaynak eser ve açık tercihlerinin katkısı ortalama 0,5/0,25 olur. Beğenilmeyen eserler olumlu hafızaya katılmaz ve sonuçlardan çıkarılır. Sadece gösterilen sonuçlar hafızaya olumlu sinyal olarak eklenmez. Kaydı veya beğeniyi kaldırmak ilgili sinyali sonraki isteklerden çıkarır; bağımsız geçmiş istekleri ve diğer olumlu sinyaller geçerliliğini korur.
