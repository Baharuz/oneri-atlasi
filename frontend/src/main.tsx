import React, { useEffect, useRef, useState } from 'react';
import { createRoot } from 'react-dom/client';
import './style.css';
import { ProfilePreferences, type Profile } from './ProfilePreferences';
import { RecommendationMode, modes, type Mode } from './RecommendationMode';

type Category = 'kitap'|'film'|'dizi'|'oyun';
type Content = {id:number; category:Category; title:string; description:string; genres:string[]; themes:string[]; moods:string[]; pace:string|null; audience:string|null; source:string; year:number|null; creators:string[]; metadata_source_url:string|null; image_url:string|null; image_credit:string|null; image_source_url:string|null};
type Result = {content:Content; reason:string; score:number|null};
type RecommendationGroups = Partial<Record<Category,Result[]>>;
type User = {id:number; email:string; preferences:Profile; favorites:number[]; feedback:Record<number,string>};
const cats:Category[]=['kitap','film','dizi','oyun'];
const names:Record<Category,string>={kitap:'Kitap',film:'Film',dizi:'Dizi',oyun:'Oyun'};
const icons:Record<Category,string>={kitap:'📚',film:'🎬',dizi:'📺',oyun:'🎮'};
const creatorLabels:Record<Category,string>={kitap:'Yazar',film:'Yönetmen',dizi:'Yaratıcı',oyun:'Geliştirici'};
const PAGE_SIZE=24;
function cookie(name:string){return document.cookie.split('; ').find(x=>x.startsWith(name+'='))?.split('=')[1]||''}
async function api<T>(path:string, method='GET', data?:unknown):Promise<T>{
  const response=await fetch('/api'+path,{method,credentials:'include',headers:{'Content-Type':'application/json',...(cookie('csrf')?{'X-CSRF-Token':decodeURIComponent(cookie('csrf'))}:{})},body:data===undefined?undefined:JSON.stringify(data)});
  if(!response.ok){const error=await response.json().catch(()=>({detail:'İstek başarısız'}));throw new Error(typeof error.detail==='string'?error.detail:'Lütfen bilgileri kontrol edin')}
  return response.json();
}
export function App(){
  const [page,setPage]=useState<'home'|'auth'|'choose'|'results'|'profile'|'detail'|'saved'>('home');
  const [user,setUser]=useState<User|null>(null),[items,setItems]=useState<Content[]>([]),[selectedItems,setSelectedItems]=useState<Content[]>([]);
  const [category,setCategory]=useState<Category|null>(null),[catalogBusy,setCatalogBusy]=useState(true),[catalogError,setCatalogError]=useState(false),[returnPage,setReturnPage]=useState<'detail'|'saved'|'results'|null>(null),[pendingSaveId,setPendingSaveId]=useState<number|null>(null);
  const [query,setQuery]=useState(''),[authMode,setAuthMode]=useState<'login'|'register'>('login'),[email,setEmail]=useState(''),[password,setPassword]=useState('');
  const [sourceItems,setSourceItems]=useState<Content[]>([]),[recs,setRecs]=useState<Result[]>([]),[recBusy,setRecBusy]=useState(false),[recError,setRecError]=useState('');
  const [targetCategory,setTargetCategory]=useState<Category|null>(null),[recommendationGroups,setRecommendationGroups]=useState<RecommendationGroups>({});
  const [detail,setDetail]=useState<Content|null>(null),[history,setHistory]=useState<{id:number;created_at:string;sources:{id:number;title:string}[];count:number}[]>([]);
  const [busy,setBusy]=useState(false),[error,setError]=useState(''),[notice,setNotice]=useState('');
  const [savedItems,setSavedItems]=useState<Content[]>([]),[savedBusy,setSavedBusy]=useState(false),[savedError,setSavedError]=useState('');
  const [displayLimit,setDisplayLimit]=useState(PAGE_SIZE);
  const [detailReturn,setDetailReturn]=useState<'saved'|'results'|'choose'>('choose');
  const [resultsReturn,setResultsReturn]=useState<'choose'|'profile'>('choose');
  const [historyBusy,setHistoryBusy]=useState<number|null>(null);
  const [resultCategories,setResultCategories]=useState<Category[]>(cats);
  const [historicalAt,setHistoricalAt]=useState<string|null>(null);
  const source=sourceItems[0]||null;
  function openDetail(item:Content){setDetailReturn(page==='saved'?'saved':page==='results'?'results':'choose');setDetail(item);setPageSafe('detail')}
  function toggleSource(item:Content){
    if(selectedItems.some(value=>value.id===item.id)){setSelectedItems(current=>current.filter(value=>value.id!==item.id));return;}
    if(selectedItems.length>=5){setNotice('En fazla 5 eser seçebilirsin. Yeni eser eklemek için bir seçimi kaldır.');return;}
    setSelectedItems(current=>[...current,item]);setNotice('');
  }

  const [feedbackBusy,setFeedbackBusy]=useState<number|null>(null);
  const feedbackLock=useRef(false);
  const [dismissed,setDismissed]=useState<{item:Content;previous:string|undefined}|null>(null);
  const visibleRecommendations=(rows:Result[])=>rows.filter(row=>user?.feedback[row.content.id]!=='dislike');
  async function giveFeedback(item:Content,kind:'like'|'dislike',undo=false){
    if(!user){setDetail(item);setPendingSaveId(null);setReturnPage(page==='results'?'results':'detail');setPageSafe('auth');return;}
    if(feedbackLock.current)return;
    feedbackLock.current=true;setFeedbackBusy(item.id);setError('');
    const previous=user.feedback[item.id];
    const target=undo?dismissed?.previous:(previous===kind?undefined:kind);
    try{
      await api(`/me/contents/${item.id}/${target||previous}`,target?'PUT':'DELETE');
      setUser(current=>{if(!current||current.id!==user.id)return current;const feedback={...current.feedback};if(target)feedback[item.id]=target;else delete feedback[item.id];return {...current,feedback};});
      if(undo)setDismissed(null);
      else if(target==='dislike')setDismissed({item,previous});
    }catch(e){showError(e)}finally{feedbackLock.current=false;setFeedbackBusy(null);}
  }

  const [mode,setMode]=useState<Mode>('close'),[resultMode,setResultMode]=useState<Mode>('close');
  const [features,setFeatures]=useState<string[]>([]),[moods,setMoods]=useState<string[]>([]);
  const availableThemes=[...new Set(selectedItems.flatMap(item=>item.themes))];
  const availableGenres=[...new Set(selectedItems.flatMap(item=>item.genres))];
  const availableMoods=[...new Set(selectedItems.flatMap(item=>item.moods))];
  const selectionKey=selectedItems.map(item=>item.id).sort((a,b)=>a-b).join(',');
  useEffect(()=>{
    setFeatures(current=>current.filter(tag=>selectedItems.some(item=>item.themes.includes(tag)||item.genres.includes(tag))));
    setMoods(current=>current.filter(tag=>selectedItems.some(item=>item.moods.includes(tag))));
  },[selectionKey]);
  function togglePreference(kind:'features'|'moods',tag:string){
    const current=kind==='features'?features:moods;
    if(!current.includes(tag)&&current.length>=(kind==='features'?20:10)){setNotice('Bu tercih grubunda seçim sınırına ulaştın.');return;}
    (kind==='features'?setFeatures:setMoods)(previous=>previous.includes(tag)?previous.filter(value=>value!==tag):[...previous,tag]);
  }

  useEffect(()=>{api<User>('/me').then(setUser).catch(()=>{});api<Content[]>('/contents').then(setItems).catch(()=>setCatalogError(true)).finally(()=>setCatalogBusy(false))},[]);
  const setPageSafe=(p:typeof page)=>{setError('');setNotice('');setPage(p)};
  const visible=items.filter(x=>(!category||x.category===category)&&x.title.toLocaleLowerCase('tr').includes(query.trim().toLocaleLowerCase('tr')));
  const shown=visible.slice(0,displayLimit);
  const updateQuery=(value:string)=>{setQuery(value);setDisplayLimit(PAGE_SIZE)};
  const enterCategory=(c:Category|null)=>{setCategory(c);setSelectedItems([]);setQuery('');setDisplayLimit(PAGE_SIZE);setPageSafe('choose')};
  const filterCategory=(c:Category|null)=>{setCategory(c);setDisplayLimit(PAGE_SIZE)};
  async function loadSaved(){setSavedBusy(true);setSavedError('');try{setSavedItems(await api<Content[]>('/me/saved'))}catch(e){setSavedError(e instanceof Error?e.message:'Kaydedilenler alınamadı')}finally{setSavedBusy(false)}}
  const openSaved=()=>{setPendingSaveId(null);if(!user){setReturnPage('saved');setPageSafe('auth')}else{setPageSafe('saved');void loadSaved()}};
  const reloadCatalog=async()=>{setCatalogBusy(true);setCatalogError(false);try{setItems(await api<Content[]>('/contents'));try{setUser(await api<User>('/me'))}catch{setUser(null)}}catch{setCatalogError(true)}finally{setCatalogBusy(false)}};
  const showError=(e:unknown)=>setError(e instanceof Error?e.message:'Bir hata oluştu');
  async function authenticate(e:React.FormEvent){e.preventDefault();setBusy(true);setError('');try{await api('/auth/'+authMode,'POST',{email,password});let me=await api<User>('/me');let saveError='';if(pendingSaveId!==null){try{await api(`/me/contents/${pendingSaveId}/favorite`,'PUT');me=await api<User>('/me')}catch(e){saveError=e instanceof Error?e.message:'Eser kaydedilemedi'}}setUser(me);setPageSafe(returnPage||'choose');if(returnPage==='saved')await loadSaved();if(saveError)setError(saveError);else if(pendingSaveId!==null)setNotice('Eser kaydedildi. Kaydedilenler bölümünde bulabilirsin.');setPendingSaveId(null);setReturnPage(null)}catch(e){showError(e)}finally{setBusy(false)}}
  async function logout(){try{await api('/auth/logout','POST');setUser(null);setDismissed(null);setSavedItems([]);setSelectedItems([]);setSourceItems([]);setRecs([]);setRecommendationGroups({});setPageSafe('home')}catch(e){showError(e)}}
  async function recommend(sources=selectedItems){
    if(!sources.length)return;
    setDismissed(null);setSourceItems(sources);setResultMode(mode);setRecBusy(true);setRecError('');setHistoricalAt(null);setResultsReturn('choose');setPageSafe('results');
    const categories=targetCategory?[targetCategory]:cats;setResultCategories(categories);
    try{
      const groups=await api<RecommendationGroups>('/recommend','POST',{source_ids:sources.map(item=>item.id),answers:{categories,mode,features,moods}});
      setRecommendationGroups(groups);setRecs(cats.flatMap(c=>groups[c]||[]));
    }catch(e){setRecommendationGroups({});setRecs([]);setRecError(e instanceof Error?e.message:'Öneriler alınamadı')}
    finally{setRecBusy(false)}
  }
  async function openHistory(id:number){
    setHistoryBusy(id);setError('');
    try{
      const run=await api<{created_at:string;sources:Content[];request:{answers:{mode?:Mode}};results:RecommendationGroups;missing_count:number;legacy:boolean}>('/me/history/'+id);
      setSourceItems(run.sources);setRecommendationGroups(run.results);setRecs(cats.flatMap(c=>run.results[c]||[]));setResultCategories(cats.filter(c=>c in run.results));
      setResultMode(run.request.answers.mode||'close');setHistoricalAt(run.created_at);setResultsReturn('profile');setRecError('');setDismissed(null);setPageSafe('results');
      if(run.missing_count)setNotice(`${run.missing_count} eser artık katalogda bulunmadığı için gösterilemiyor.`);
    }catch(e){showError(e)}finally{setHistoryBusy(null)}
  }
  async function interact(id:number,kind:'favorite'|'like'|'dislike'){if(!user)return;try{const existing=kind==='favorite'?user.favorites.includes(id):user.feedback[id]===kind;await api(`/me/contents/${id}/${kind}`,existing?'DELETE':'PUT');setUser(await api<User>('/me'));if(page==='saved'&&kind==='favorite')await loadSaved();setError('')}catch(e){showError(e)}}
  async function saveProfile(preferences:Profile){
    const result=await api<{preferences:Profile}>('/me/preferences','PUT',preferences);
    setUser(current=>current?{...current,preferences:result.preferences}:current);
  }
  async function openProfile(){try{setUser(await api<User>('/me'));setHistory(await api('/me/history'));setPageSafe('profile')}catch(e){showError(e)}}
  const art=(item:Content)=>item.image_url?<img className="artimage" src={item.image_url} alt={item.title+' eser görseli'} loading="lazy" onError={e=>{e.currentTarget.hidden=true;e.currentTarget.parentElement?.classList.add('image-missing')}}/>:null;
  const imageCredit=(item:Content)=>item.image_url&&item.image_credit?<p className="imagecredit">Görsel: {item.image_source_url?.startsWith('https://')?<a href={item.image_source_url} target="_blank" rel="noopener noreferrer">{item.image_credit}</a>:item.image_credit}</p>:null;
  const saveButton=(item:Content)=>{const saved=user?.favorites.includes(item.id);return <button className="secondary compact" onClick={()=>{if(!user){setDetailReturn(page==='saved'?'saved':page==='results'?'results':'choose');setDetail(item);setPendingSaveId(item.id);setReturnPage('detail');setPageSafe('auth');return}void interact(item.id,'favorite')}}>{saved?'Kaydı kaldır':'Kaydet'}</button>};
  const feedbackButtons=(item:Content)=><div className="feedback-controls" role="group" aria-label={item.title+' için geri bildirim'}>{(['like','dislike'] as const).map(kind=><button key={kind} className={'secondary compact feedback-button '+(user?.feedback[item.id]===kind?'feedback-active':'')} aria-pressed={user?.feedback[item.id]===kind} disabled={feedbackBusy!==null} onClick={()=>void giveFeedback(item,kind)}>{feedbackBusy===item.id?'İşleniyor…':kind==='like'?'Beğen':'Beğenme'}</button>)}{!user&&<small>Geri bildirimi kaydetmek için giriş yapmalısın.</small>}</div>;
  const cards=(list:Content[],reasons?:Record<number,string>)=>list.map(item=><article className="card" key={item.id}><div className={'art '+item.category}>{art(item)}<span className="artfallback" aria-hidden="true">{icons[item.category]}</span></div><div className="cardbody">{imageCredit(item)}<small>{names[item.category]}{item.year?' · '+item.year:''}</small><h3>{item.title}</h3><p className="genres">{item.genres.join(', ')||'Tür belirtilmemiş'}</p><p>{item.description}</p><p className="genres">{creatorLabels[item.category]}: {item.creators?.join(', ')||'Bilgi henüz doğrulanmadı'}</p>{reasons?.[item.id]&&<p className="reason"><strong>Neden önerildi?</strong> {reasons[item.id]}</p>}<div className="actions"><button className="secondary compact" onClick={()=>openDetail(item)}>Detay</button>{saveButton(item)}</div>{feedbackButtons(item)}</div></article>);
  return <><a className="skiplink" href="#main">İçeriğe geç</a><header className="top"><button className="brand" onClick={()=>setPageSafe('home')}>✦ Öneri Atlası</button><nav aria-label="Ana gezinme"><button onClick={()=>enterCategory(null)}>Öneri al</button><button onClick={openSaved}>Kaydedilenler</button>{user?<><button onClick={openProfile}>Profilim</button><button onClick={logout}>Çıkış</button></>:<button onClick={()=>setPageSafe('auth')}>Giriş / Kayıt</button>}</nav></header><main id="main">{error&&<div role="alert" className="alert">{error} <button onClick={()=>setError('')}>Kapat</button></div>}{notice&&<div role="status" className="notice">{notice}</div>}
  {page==='home'&&<section className="hero"><div className="eyebrow">KİTAP · FİLM · DİZİ · OYUN</div><h1>Sevdiğin eserden<br/><em>yeni hikâyeler keşfet.</em></h1><p>Bir eser seç, hangi kategorilerden öneri istediğini belirle. Ortak tema ve atmosferleri keşfet.</p><button className="primary" onClick={()=>enterCategory(null)}>Eser seç →</button><h2>Bir kategoriyle başla</h2><div className="homecategories">{cats.map(c=><button key={c} onClick={()=>enterCategory(c)}><span aria-hidden="true">{icons[c]}</span><strong>{names[c]}</strong><span> Eser ara →</span></button>)}</div></section>}
  {page==='auth'&&<section className="panel narrow"><button className="textbutton" onClick={()=>{setPendingSaveId(null);setPageSafe(returnPage||'home')}}>← Geri</button><div className="eyebrow">HESABIN</div><h1>{authMode==='login'?'Giriş yap':'Kayıt ol'}</h1>{returnPage&&<p>{returnPage==='results'?'Geri bildirim vermek için giriş yap. Ardından önerilere dönüp seçimini yapabilirsin.':'Kaydettiğin eserlere hesabından erişebilirsin. Girişten sonra kaldığın yere döneceksin.'}</p>}<form onSubmit={authenticate}><label>E-posta<input type="email" required value={email} onChange={e=>setEmail(e.target.value)}/></label><label>Şifre<input type="password" minLength={8} required value={password} onChange={e=>setPassword(e.target.value)}/></label><button className="primary" disabled={busy}>{busy?'Bekleyin…':authMode==='login'?'Giriş yap':'Kayıt ol'}</button></form><button className="textbutton" onClick={()=>setAuthMode(authMode==='login'?'register':'login')}>{authMode==='login'?'Hesabın yok mu? Kayıt ol':'Zaten hesabın var mı? Giriş yap'}</button></section>}
  {page==='choose'&&<section><button className="textbutton" onClick={()=>setPageSafe('home')}>← Ana sayfa</button><div className="eyebrow">1 / 2 · ESER SEÇ</div><h1>Sevdiğin eserleri seç</h1><p>Sevdiğin eseri ara, ardından öneri görmek istediğin kategoriyi seç.</p><div className="chooser"><div><label className="searchlabel">Eser adına göre ara<input type="search" placeholder="Örneğin: Dune" value={query} onChange={e=>updateQuery(e.target.value)}/></label><div className="categoryfilters" role="group" aria-label="Eser kategorisi"><button className={!category?'active':''} aria-pressed={!category} onClick={()=>filterCategory(null)}>Tümü</button>{cats.map(c=><button key={c} className={category===c?'active':''} aria-pressed={category===c} onClick={()=>filterCategory(c)}>{names[c]}</button>)}</div>{catalogBusy?<div role="status" className="empty">Eserler yükleniyor…</div>:catalogError?<div role="alert" className="empty">Eserler alınamadı. <button className="secondary" onClick={reloadCatalog}>Yeniden dene</button></div>:visible.length?<><p className="resultcount" role="status">{visible.length} eser bulundu · {shown.length} eser gösteriliyor</p><div className="grid">{shown.map(item=><button key={item.id} className={'pick '+(selectedItems.some(value=>value.id===item.id)?'picked':'')} aria-pressed={selectedItems.some(value=>value.id===item.id)} onClick={()=>toggleSource(item)}><span aria-hidden="true">{icons[item.category]}</span><strong>{item.title}</strong><small>{names[item.category]} · {item.genres.join(', ')}</small><span className="pickaction">{selectedItems.some(value=>value.id===item.id)?'Seçili':'Seç'}</span></button>)}</div>{shown.length<visible.length&&<button className="secondary loadmore" onClick={()=>setDisplayLimit(limit=>limit+PAGE_SIZE)}>Daha fazla göster ({visible.length-shown.length} kaldı)</button>}</>:<div className="empty">Bu kategoride {query?'“'+query+'” adına uygun':'gösterilecek'} eser bulunamadı. <button className="secondary" onClick={()=>{updateQuery('');setCategory(null)}}>Aramayı temizle ve tümünü göster</button></div>}</div><aside className="selectionpanel"><h2>Seçilen eserler ({selectedItems.length}/5)</h2>{selectedItems.length?<ul>{selectedItems.map(item=><li key={item.id}>{item.title} · {names[item.category]} <button aria-label={item.title+' seçimini kaldır'} onClick={()=>toggleSource(item)}>×</button></li>)}</ul>:<p>Henüz eser seçmedin.</p>}{selectedItems.length>0&&<div className="preferences"><h3>Bu eserde neyi sevdin?</h3><p id="preference-help">İstersen birden fazla tema ve atmosfer seç. Seçtiklerin önerilerde daha fazla ağırlık alır; boş bırakırsan eserin genel benzerliği kullanılır.</p>{([['features','Temalar',availableThemes,features],['features','Türler',availableGenres,features],['moods','Atmosfer',availableMoods,moods]] as const).map(([kind,label,tags,chosen])=><fieldset key={label} aria-describedby="preference-help"><legend>{label}</legend>{tags.length?<div className="preference-options">{[...new Set(tags)].map(tag=><label className="preference-option" key={tag}><input type="checkbox" checked={chosen.includes(tag)} onChange={()=>togglePreference(kind,tag)}/><span>{tag}</span></label>)}</div>:<p>Seçilen eserler için {label.toLocaleLowerCase('tr')} etiketi bulunmuyor.</p>}</fieldset>)}{(features.length>0||moods.length>0)&&<button className="textbutton" onClick={()=>(setFeatures([]),setMoods([]))}>Tercihleri temizle</button>}</div>}<div className="targetchoice" role="group" aria-label="Öneri hedef kategorisi"><strong>Öneri kategorisi</strong><div className="categoryfilters"><button aria-pressed={targetCategory===null} className={targetCategory===null?'active':''} onClick={()=>setTargetCategory(null)}>Tümü</button>{cats.map(c=><button key={c} aria-pressed={targetCategory===c} className={targetCategory===c?'active':''} onClick={()=>setTargetCategory(c)}>{names[c]}</button>)}</div></div><RecommendationMode value={mode} onChange={setMode} disabled={recBusy}/><button className="primary" disabled={!selectedItems.length||recBusy} onClick={()=>recommend()}>{recBusy?'Öneriler hazırlanıyor…':'Önerileri göster'}</button><p>1–5 eser seçebilirsin. Farklı kategorilerdeki seçimlerin korunur.</p>{user&&<p>Önerilerde hesabındaki tercihler ve geçmiş seçimlerin de kullanılır.</p>}</aside></div></section>}
  {page==='results'&&<section><button className="textbutton" onClick={()=>setPageSafe(resultsReturn)}>{resultsReturn==='profile'?'← Profilime dön':'← Eser seçimine dön'}</button><div className="eyebrow">2 / 2 · ÖNERİLER</div><h1>Kategorilere göre öneriler</h1>{recBusy?<div role="status" className="empty">Öneriler hazırlanıyor…</div>:recError?<div role="alert" className="empty">{recError} <button className="secondary" onClick={()=>recommend(sourceItems)}>Yeniden dene</button> <button className="secondary" onClick={()=>setPageSafe('choose')}>Başka bir eser seç</button></div>:<>{source&&<div className="sourcebox"><strong>Kaynak eserler:</strong> {sourceItems.map(item=>item.title).join(' · ')} <button className="secondary compact" onClick={()=>setPageSafe('choose')}>Değiştir</button></div>}{historicalAt&&<p role="status">{new Date(historicalAt).toLocaleString('tr-TR')} tarihindeki kayıtlı sonuçlar. Güncel öneri hesabı yapılmadı.</p>}<p><strong>Öneri modu: {modes.find(option=>option.value===resultMode)?.label}</strong> · Ortak tema ve atmosferlere göre seçtiğin hedef kategorilerde öneriler.</p>{dismissed&&user&&<div className="notice" role="status">{dismissed.item.title} önerilerden çıkarıldı. <button className="textbutton" disabled={feedbackBusy!==null} onClick={()=>void giveFeedback(dismissed.item,'dislike',true)}>Geri al</button></div>}<div className="resultsections">{resultCategories.map(c=><section className="resultsection" key={c} aria-label={names[c]+' önerileri'}><h2>{icons[c]} {names[c]} önerileri</h2>{visibleRecommendations(recommendationGroups[c]||[]).length?<div className="resultgrid">{cards(visibleRecommendations(recommendationGroups[c]||[]).map(x=>x.content),Object.fromEntries((recommendationGroups[c]||[]).map(x=>[x.content.id,x.reason])))}</div>:<div className="empty">Bu kategoride eşleşen öneri bulunamadı.</div>}</section>)}</div></>}</section>}
  {page==='detail'&&detail&&<section className="panel"><button className="textbutton" onClick={()=>setPageSafe(detailReturn)}>← {detailReturn==='saved'?'Kaydedilenlere':detailReturn==='results'?'Önerilere':'Eser seçimine'} dön</button><div className="detailview"><div className={'detailart art '+detail.category}>{art(detail)}<span className="artfallback" aria-hidden="true">{icons[detail.category]}</span></div><div><div className="eyebrow">{names[detail.category]}{detail.year?' · '+detail.year:''}</div><h1>{detail.title}</h1><p className="genres">{detail.genres.join(', ')}</p><p>{detail.description}</p><p><strong>İlk yayın / çıkış yılı:</strong> {detail.year||'Bilgi henüz doğrulanmadı'}</p><p><strong>{creatorLabels[detail.category]}:</strong> {detail.creators?.join(', ')||'Bilgi henüz doğrulanmadı'}</p>{detail.metadata_source_url?.startsWith('https://')&&<a href={detail.metadata_source_url} target="_blank" rel="noopener noreferrer">Eser bilgilerinin kaynağı</a>}{imageCredit(detail)}{recs.find(x=>x.content.id===detail.id)?.reason&&<div className="sourcebox"><strong>Neden önerildi?</strong><p>{recs.find(x=>x.content.id===detail.id)?.reason}</p></div>}<div className="actions">{saveButton(detail)}</div></div></div></section>}
  {page==='saved'&&user&&<section><button className="textbutton" onClick={()=>setPageSafe(source?'results':'home')}>← Geri</button><div className="eyebrow">HESABIM</div><h1>Kaydedilenler</h1>{savedBusy?<div role="status" className="empty">Kaydedilen eserler yükleniyor…</div>:savedError?<div role="alert" className="empty">{savedError} <button className="secondary" onClick={()=>void loadSaved()}>Yeniden dene</button></div>:savedItems.length?<div className="resultgrid">{cards(savedItems)}</div>:<div className="empty">Henüz eser kaydetmedin. <button className="secondary" onClick={()=>enterCategory(null)}>Öneri al</button></div>}</section>}
  {page==='profile'&&user&&<section><div className="eyebrow">HESABIM</div><h1>Profilim</h1><p>{user.email}</p><div className="panel"><ProfilePreferences key={user.id} preferences={user.preferences||{}} themes={[...new Set(items.flatMap(item=>item.themes))]} atmospheres={[...new Set(items.flatMap(item=>item.moods))]} onSave={saveProfile}/></div><div className="columns"><div className="panel"><h2>Öneri hafızan</h2><p>Kalıcı tercihlerin, kaydettiğin ve beğendiğin eserler ile son 20 öneri isteğinde seçtiğin eser ve tercihler sıralamaya katılır. Beğenmediklerin elenir. Sadece sonuçlarda gösterilmiş bir eser beğenilmiş sayılmaz.</p><button className="secondary" onClick={openSaved}>Kaydedilenleri gör</button></div><div className="panel"><h2>Öneri geçmişi</h2>{history.length?history.map(x=><p key={x.id}>{new Date(x.created_at).toLocaleString('tr-TR')} · {x.count} öneri<br/><strong>{x.sources.map(item=>item.title).join(' · ')||'Kaynak eser bulunamadı'}</strong><br/><button className="secondary compact" disabled={historyBusy!==null} onClick={()=>void openHistory(x.id)}>{historyBusy===x.id?'Açılıyor…':'Sonuçları aç'}</button></p>):<p>Henüz öneri geçmişi yok.</p>}</div></div></section>}
  </main><footer>Öneri Atlası · Elle hazırlanmış örnek katalog · İçerik benzerliğine dayalı öneriler</footer></>
}
const root=document.getElementById('root');
if(root)createRoot(root).render(<App/>);

