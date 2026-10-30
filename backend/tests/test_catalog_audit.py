import httpx
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.catalog_audit import _url_error, audit
from app.catalog import seed
from app.db import Base
from app.models import Content


def test_audit_rejects_short_catalog_and_duplicate_titles():
    engine = create_engine("sqlite+pysqlite:///:memory:")
    Base.metadata.create_all(engine)
    with sessionmaker(bind=engine)() as db:
        for source_id, title in (("1", "Dune"), ("2", " dune ")):
            db.add(Content(category="kitap", title=title, source="local", source_id=source_id,
                           description="Özgün açıklama", genres=[], themes=[], moods=[]))
        db.commit()
        report = audit(db)
        assert report["total"] == 2 and not report["ok"]
        assert any("Mükerrer eser" in error for error in report["errors"])
        assert any("beklenen 125" in error for error in report["errors"])
        assert any("image_url" in error for error in report["errors"])


def test_url_audit_rejects_broken_or_non_image_response():
    def handle(request):
        if request.url.path == "/broken":
            return httpx.Response(404)
        return httpx.Response(200, headers={"content-type": "text/html"})
    with httpx.Client(transport=httpx.MockTransport(handle)) as client:
        assert _url_error(client, "http://example.test/image", True) == "HTTPS URL gerekli"
        assert _url_error(client, "https://example.test/broken", True) == "HTTP 404"
        assert _url_error(client, "https://example.test/page", True) == "yanıt görsel değil"
        assert _url_error(client, "https://example.test/page", False) is None
        assert _url_error(client, "/art/kitap-1.svg", True) is None
        assert _url_error(client, "/art/olmayan.svg", True) == "yerel görsel dosyası yok"


def test_full_seed_has_500_valid_records_and_art():
    engine = create_engine("sqlite+pysqlite:///:memory:")
    Base.metadata.create_all(engine)
    with sessionmaker(bind=engine)() as db:
        seed(db)
        report = audit(db)
        assert report == {
            "ok": True, "total": 500,
            "categories": {"kitap": 125, "film": 125, "dizi": 125, "oyun": 125},
            "errors": [],
        }
        item = db.query(Content).filter_by(source_id="oyun-125").one()
        item.image_source_url = "https://example.invalid/yanlis"
        assert any("kaynak bağlantısı uyuşmuyor" in error for error in audit(db)["errors"])
