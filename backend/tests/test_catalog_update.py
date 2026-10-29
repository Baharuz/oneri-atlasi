import pytest
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.catalog_update import ManifestError, apply_manifest
from app.db import Base
from app.main import content_dict
from app.models import Content, ContentTag, Interaction, Tag, User

SEED = (("kitap", "Bir Kitap"), ("film", "Bir Film"), ("oyun", "Bir Oyun"))

def _item(kind, number, **overrides):
    item = {"source": "local", "source_id": f"{kind}-{number}", "category": kind,
            "image_url": "https://images.example.com/kapak.jpg",
            "description": f"{kind} için elle yazılmış özgün bir tanıtım metni.",
            "image_source_url": "https://kaynak.example.com/eser",
            "image_credit": "Örnek Atıf"}
    item.update(overrides)
    return item

@pytest.fixture()
def session():
    engine = create_engine("sqlite+pysqlite:///:memory:", connect_args={"check_same_thread": False}, poolclass=StaticPool)
    Base.metadata.create_all(engine)
    with sessionmaker(bind=engine)() as db:
        for index, (category, title) in enumerate(SEED):
            db.add(Content(category=category, title=title, description=f"{title}: dostluk temalarını sıcak bir atmosferle buluşturan bir {category}.", genres=[], themes=["dostluk"], moods=["sıcak"], source="local", source_id=f"{category}-{index+1}"))
        db.commit()
        yield db
        db.rollback()

def test_apply_updates_and_preserves_relations(session):
    record = session.scalar(select(Content).where(Content.source_id == "kitap-1"))
    identity = (record.id, record.source, record.source_id)
    user = User(email="manifest@example.com", password_hash="x")
    tag = Tag(kind="theme", name="dostluk")
    session.add_all([user, tag])
    session.commit()
    session.add_all([Interaction(user_id=user.id, content_id=record.id, kind="favorite"), ContentTag(content_id=record.id, tag_id=tag.id)])
    session.commit()

    plan = apply_manifest(session, [_item("kitap", 1), _item("film", 2)])

    assert len(plan) == 2 and "image_url" in plan[0]["changes"]
    session.expire_all()
    updated = session.scalar(select(Content).where(Content.source_id == "kitap-1"))
    assert (updated.id, updated.source, updated.source_id) == identity
    assert updated.image_url == "https://images.example.com/kapak.jpg"
    assert "atmosferle buluşturan" not in updated.description
    assert session.scalar(select(Interaction).where(Interaction.content_id == identity[0], Interaction.kind == "favorite")) is not None
    assert session.scalar(select(ContentTag).where(ContentTag.content_id == identity[0])) is not None
    payload = content_dict(updated)
    assert payload["image_source_url"] == "https://kaynak.example.com/eser"
    assert payload["image_credit"] == "Örnek Atıf"
    assert payload["description"] == "kitap için elle yazılmış özgün bir tanıtım metni."

def test_second_apply_is_idempotent(session):
    items = [_item("kitap", 1), _item("film", 2)]
    assert apply_manifest(session, items)
    snapshot = [(r.source_id, r.image_url, r.description, r.image_credit) for r in session.scalars(select(Content).order_by(Content.id))]
    assert apply_manifest(session, items) == []
    session.expire_all()
    assert snapshot == [(r.source_id, r.image_url, r.description, r.image_credit) for r in session.scalars(select(Content).order_by(Content.id))]

def test_dry_run_previews_without_writing(session):
    plan = apply_manifest(session, [_item("kitap", 1)], write=False)
    assert plan and plan[0]["changes"]["image_url"]["to"] == "https://images.example.com/kapak.jpg"
    session.expire_all()
    assert session.scalar(select(Content).where(Content.source_id == "kitap-1")).image_url is None

def test_validation_errors_block_all_writes(session):
    items = [_item("kitap", 1),
             _item("film", 2, image_url="http://example.com/a.jpg"),
             _item("kitap", 9),
             _item("kitap", 1),
             _item("oyun", 3, category="gecersiz"),
             _item("oyun", 3, description="Bir Oyun: dostluk temalarını sıcak bir atmosferle buluşturan bir oyun.")]
    with pytest.raises(ManifestError) as error:
        apply_manifest(session, items)
    assert len(error.value.errors) >= 5
    session.expire_all()
    assert all(r.image_url is None for r in session.scalars(select(Content)))
    assert all("atmosferle buluşturan" in r.description for r in session.scalars(select(Content)))

def test_write_failure_rolls_back_everything(session, monkeypatch):
    from app import catalog_update
    calls, real = {"count": 0}, catalog_update._set_fields
    def boom(record, item):
        calls["count"] += 1
        if calls["count"] == 2: raise RuntimeError("yazma hatası")
        real(record, item)
    monkeypatch.setattr(catalog_update, "_set_fields", boom)
    with pytest.raises(RuntimeError):
        catalog_update.apply_manifest(session, [_item("kitap", 1), _item("film", 2)])
    session.expire_all()
    assert all(r.image_url is None and r.image_credit is None for r in session.scalars(select(Content)))

def test_missing_or_blank_credit_blocks_entire_manifest(session):
    items = [_item("kitap", 1, image_credit="   "),
             _item("film", 2),
             _item("oyun", 3, image_credit=None)]
    with pytest.raises(ManifestError) as error:
        apply_manifest(session, items)
    assert any("image_credit" in message for message in error.value.errors)
    session.expire_all()
    assert all(r.image_url is None and r.image_credit is None and "atmosferle buluşturan" in r.description for r in session.scalars(select(Content)))
