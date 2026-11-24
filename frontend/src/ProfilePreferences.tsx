import { useState, type FormEvent } from 'react';

export type Profile = {features?:string[]; moods?:string[]; mode?:string; categories?:string[]; source_ids?:number[]};
export function ProfilePreferences({preferences, themes, atmospheres, onSave}: {
  preferences:Profile; themes:string[]; atmospheres:string[]; onSave:(profile:Profile)=>Promise<void>;
}) {
  const [features,setFeatures]=useState(preferences.features||[]);
  const [moods,setMoods]=useState(preferences.moods||[]);
  const [busy,setBusy]=useState(false),[error,setError]=useState(''),[saved,setSaved]=useState(false);
  async function submit(event:FormEvent){
    event.preventDefault();setBusy(true);setError('');setSaved(false);
    try{await onSave({...preferences,features,moods});setSaved(true)}
    catch(error){setError(error instanceof Error?error.message:'Tercihler kaydedilemedi.')}
    finally{setBusy(false)}
  }
  return <form className="profile-preferences" onSubmit={submit}>
    <h2>Kalıcı tercihlerim</h2>
    <p>Bu seçimler hesabında saklanır ve sonraki girişlerinde önerilere katılır. Tek bir öneri için seçtiğin tercihler bu kaydı değiştirmez.</p>
    {([{label:'Sevdiğin temalar',options:themes,value:features,set:setFeatures,limit:20},
       {label:'Sevdiğin atmosferler',options:atmospheres,value:moods,set:setMoods,limit:10}]).map(group=><fieldset key={group.label} disabled={busy}>
      <legend>{group.label} ({group.value.length}/{group.limit})</legend>
      <div className="preference-options">{[...new Set([...group.options,...group.value])].sort((a,b)=>a.localeCompare(b,'tr')).map(tag=><label className="preference-option" key={tag}>
        <input type="checkbox" checked={group.value.includes(tag)} disabled={!group.value.includes(tag)&&group.value.length>=group.limit}
          onChange={()=>{group.set(current=>current.includes(tag)?current.filter(value=>value!==tag):[...current,tag]);setSaved(false)}}/><span>{tag}</span>
      </label>)}</div>
    </fieldset>)}
    <div className="actions"><button className="primary" disabled={busy}>{busy?'Kaydediliyor…':'Tercihleri kaydet'}</button>
    <button type="button" className="secondary" disabled={busy} onClick={()=>{setFeatures([]);setMoods([]);setSaved(false)}}>Seçimleri temizle</button></div>
    <p>Temizleme işlemini kalıcı yapmak için Tercihleri kaydet düğmesine bas.</p>
    {error&&<p role="alert">{error}</p>}{saved&&<p role="status">Tercihlerin kaydedildi.</p>}
  </form>;
}
