import os
os.environ["DATABASE_URL"] = "sqlite+pysqlite:///:memory:"
os.environ["FRONTEND_ORIGIN"] = "http://localhost:5173"
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from app.db import Base, get_db
from app.catalog import DESCRIPTIONS, seed
from app.main import app
from app.models import Content
from app.recommend import recommend

engine = create_engine("sqlite+pysqlite:///:memory:", connect_args={"check_same_thread": False}, poolclass=StaticPool)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
with Session() as db: seed(db)
def override_db():
    with Session() as db: yield db
app.dependency_overrides[get_db] = override_db

def client(): return TestClient(app, headers={"Origin":"http://localhost:5173"})
def csrf_headers(c): return {"X-CSRF-Token":c.cookies.get("csrf","")}

def test_catalog_and_cross_category():
    c=client()
    source=next(x for x in c.get('/api/contents').json() if x['title']=='Dune')
    result=c.post('/api/recommend',json={'source_ids':[source['id']],'answers':{'categories':['film','oyun']}}).json()
    assert result['film'] and result['oyun']
    assert all(x['content']['id']!=source['id'] for rows in result.values() for x in rows)
    assert all(x['reason'] for rows in result.values() for x in rows)

def test_feature_changes_ranking():
    with Session() as db:
        contents=db.query(Content).all()
        source=next(x for x in contents if x.title=='Küçük Prens')
        friendship=recommend(contents,[source],{'features':['dostluk'],'categories':['oyun']})['oyun']
        exploration=recommend(contents,[source],{'features':['keşif'],'categories':['oyun']})['oyun']
        assert [x['content'].id for x in friendship[:4]] != [x['content'].id for x in exploration[:4]]

def test_seed_expands_existing_catalog_idempotently():
    from app.models import ContentTag
    isolated_engine = create_engine("sqlite+pysqlite:///:memory:")
    Base.metadata.create_all(isolated_engine)
    with sessionmaker(bind=isolated_engine)() as db:
        original = Content(category="kitap", title="Dune", description="Elle düzenlenmiş açıklama", genres=["bilimkurgu"], themes=["siyasi entrika"], moods=["destansı"], source="local", source_id="kitap-1")
        pattern = Content(category="kitap", title="Yüzüklerin Efendisi", description="Yüzüklerin Efendisi: dostluk temalarını destansı bir atmosferle buluşturan bir kitap.", genres=["fantastik"], themes=["dostluk"], moods=["destansı"], source="local", source_id="kitap-2")
        db.add_all([original, pattern])
        db.commit()
        original_id = original.id
        seed(db)
        assert db.query(Content).count() == 300
        assert db.get(Content, original_id).description == "Elle düzenlenmiş açıklama"
        assert db.query(Content).filter_by(source_id="kitap-2").one().description == DESCRIPTIONS[("kitap", "Yüzüklerin Efendisi")]
        assert db.query(ContentTag).count() > 0
        new_book = db.query(Content).filter_by(source="local", source_id="kitap-16").one()
        assert new_book.title == "Fahrenheit 451"
        assert "temalarını" not in new_book.description
        links = db.query(ContentTag).count()
        seed(db)
        assert db.query(Content).count() == 300
        assert db.query(ContentTag).count() == links

def test_user_isolation_persistence_and_ephemeral_answers():
    a,b=client(),client()
    assert a.post('/api/auth/register',json={'email':'a@example.com','password':'password123'}).status_code==200
    assert b.post('/api/auth/register',json={'email':'b@example.com','password':'password123'}).status_code==200
    source=next(x for x in a.get('/api/contents').json() if x['title']=='Dune')
    assert a.put(f"/api/me/contents/{source['id']}/favorite",headers=csrf_headers(a)).status_code==200
    assert a.put('/api/me/preferences',json={'features':['siyasi entrika'],'categories':['film'],'source_ids':[source['id']]},headers=csrf_headers(a)).status_code==200
    assert a.post('/api/recommend',json={'source_ids':[source['id']],'answers':{'features':['ayrıntılı evren'],'categories':['film']}},headers=csrf_headers(a)).status_code==200
    assert a.get('/api/me').json()['preferences']['features']==['siyasi entrika']
    assert a.get('/api/me').json()['preferences']['source_ids']==[source['id']]
    assert b.get('/api/me').json()['favorites']==[]
    assert b.get('/api/me/history').json()==[]
    assert a.post('/api/auth/logout',headers=csrf_headers(a)).status_code==200
    assert a.post('/api/auth/login',json={'email':'a@example.com','password':'password123'}).status_code==200
    assert source['id'] in a.get('/api/me').json()['favorites']
    assert a.get('/api/me/history').json()
    assert a.put(f"/api/me/contents/{source['id']}/like",headers=csrf_headers(a)).status_code==200
    assert a.put(f"/api/me/contents/{source['id']}/dislike",headers=csrf_headers(a)).status_code==200
    assert a.get('/api/me').json()['feedback'][str(source['id'])]=='dislike'
    assert a.put(f"/api/me/contents/{source['id']}/favorite").status_code==403

def test_single_source_recommendations():
    c=client()
    items=c.get('/api/contents').json()
    for category in ('kitap','oyun'):
        source=next(x for x in items if x['category']==category and x['themes'])
        r=c.get(f"/api/contents/{source['id']}/recommendations")
        assert r.status_code==200
        data=r.json()
        assert data['source']['id']==source['id']
        assert data['results'] and all(x['content']['category']==category and x['content']['id']!=source['id'] for x in data['results'])
        assert all(x['reason'] and x['score']>0 for x in data['results'])
    assert c.get('/api/contents/999999/recommendations').status_code==404

def test_guest_search_and_single_source_recommendation():
    c=client()
    found=c.get('/api/contents',params={'q':'disco'}).json()
    assert found and all('disco' in x['title'].lower() for x in found)
    source=found[0]
    data=c.get(f"/api/contents/{source['id']}/recommendations").json()
    assert data['source']['id']==source['id']
    assert data['results']
    assert all(x['content']['category']==source['category'] and x['content']['id']!=source['id'] for x in data['results'])

def test_saved_persistence_and_isolation():
    a,b=client(),client()
    assert a.post('/api/auth/register',json={'email':'s1@example.com','password':'password123'}).status_code==200
    assert b.post('/api/auth/register',json={'email':'s2@example.com','password':'password123'}).status_code==200
    first=a.get('/api/contents').json()[0]
    assert a.get('/api/me/saved').json()==[]
    assert a.put(f"/api/me/contents/{first['id']}/favorite",headers=csrf_headers(a)).status_code==200
    saved=a.get('/api/me/saved').json()
    assert [x['id'] for x in saved]==[first['id']]
    assert saved[0]['title']==first['title'] and saved[0]['themes']==first['themes']
    assert b.get('/api/me/saved').json()==[]
    assert a.post('/api/auth/logout',headers=csrf_headers(a)).status_code==200
    assert a.get('/api/me/saved').status_code==401
    assert a.post('/api/auth/login',json={'email':'s1@example.com','password':'password123'}).status_code==200
    assert [x['id'] for x in a.get('/api/me/saved').json()]==[first['id']]
    assert a.delete(f"/api/me/contents/{first['id']}/favorite",headers=csrf_headers(a)).status_code==200
    assert a.get('/api/me/saved').json()==[]

def test_catalog_filtering_four_categories():
    c=client()
    items=c.get('/api/contents').json()
    assert len(items)==300 and {x['category'] for x in items}=={'kitap','film','dizi','oyun'}
    for category in ('kitap','film','dizi','oyun'):
        rows=c.get('/api/contents',params={'category':category}).json()
        assert len(rows)==(125 if category in ('kitap','film') else 25) and all(x['category']==category for x in rows)
    assert c.get('/api/contents',params={'category':'gecersiz'}).status_code==422
    assert c.get('/api/contents',params={'q':'siyasi entrika'}).json()==[]

def test_quality_report_flags_missing():
    from app.catalog import quality_issues
    blank=Content(category='kitap',title='Boş Açıklamalı Deneme',description='   ',genres=[],themes=[],moods=[],source='local',source_id='test-blank')
    pattern=Content(category='kitap',title='Kalıp Deneme',description='Kalıp Deneme: dostluk temalarını sakin bir atmosferle buluşturan bir kitap.',genres=[],themes=[],moods=[],source='local',source_id='test-pattern')
    with Session() as db:
        db.add_all([blank,pattern]); db.commit()
        try:
            issues=quality_issues(db)
            blank_issues=[x for x in issues if x['id']==blank.id]
            assert blank_issues and set(blank_issues[0]['issues'])>={'description','image_url','image_credit','image_source_url'}
            assert 'pattern_description' in next(x for x in issues if x['id']==pattern.id)['issues']
        finally:
            db.delete(blank); db.delete(pattern); db.commit()
    assert issues
    assert {x['category'] for x in issues}<={'kitap','film','dizi','oyun'}
    assert any('image_url' in x['issues'] for x in issues)
    assert any('description' in x['issues'] for x in issues)
    assert any('image_credit' in x['issues'] for x in issues)
    assert any('image_source_url' in x['issues'] for x in issues)
    assert all(x['id'] and x['title'] for x in issues)
