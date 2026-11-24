import React from 'react';
import {afterEach, beforeEach, expect, test, vi} from 'vitest';
import {cleanup, render, screen, within, waitFor} from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import {App} from './main';

const items=Array.from({length:6},(_,i)=>({id:i+1,title:`Eser ${i+1}`,category:i%2?'film':'kitap',description:'Örnek açıklama',genres:['bilimkurgu'],themes:['gizem'],moods:['karanlık'],creators:['Örnek kişi'],year:2000,image_url:null}));
let requests:{url:string;method:string;body:any}[];
let account:any;
let feedback:Record<number,string>;
const result={content:items[5],score:4,reason:'Gizem eşleşmesi.'};
beforeEach(()=>{
  requests=[];feedback={};account={id:1,email:'demo@example.com',preferences:{},favorites:[6],feedback};
  vi.stubGlobal('fetch',vi.fn(async(input:string,options:any={})=>{
    const url=String(input),method=options.method||'GET',body=options.body?JSON.parse(options.body):null;
    requests.push({url,method,body});
    let data:any;
    if(url==='/api/me')data={...account,feedback};
    else if(url==='/api/contents')data=items;
    else if(url==='/api/me/saved')data=[items[5]];
    else if(url==='/api/me/history')data=[{id:9,created_at:'2026-11-24T10:00:00Z',sources:[{id:1,title:'Eser 1'},{id:2,title:'Eser 2'}],count:1}];
    else if(url==='/api/me/history/9')data={created_at:'2026-11-24T10:00:00Z',sources:items.slice(0,2),request:{answers:{mode:'discover'}},results:{film:[result]},missing_count:0,legacy:false};
    else if(url==='/api/recommend')data={film:[result]};
    else if(url==='/api/me/preferences'){account={...account,preferences:body};data={preferences:body};}
    else if(url.includes('/api/me/contents/')){const parts=url.split('/');const id=Number(parts[parts.length-2]);if(method==='DELETE')delete feedback[id];else feedback[id]=parts[parts.length-1];data={ok:true};}
    else return new Response(JSON.stringify({detail:'Bulunamadı'}),{status:404});
    return new Response(JSON.stringify(data),{status:200,headers:{'Content-Type':'application/json'}});
  }));
});
afterEach(()=>{cleanup();vi.unstubAllGlobals()});
async function choose(){const user=userEvent.setup();render(<App/>);await user.click(screen.getByRole('button',{name:'Eser seç →'}));await screen.findByRole('button',{name:/Eser 1.*Seç/});return user;}

test('selects up to five sources across category filters and sends preferences and mode',async()=>{
  const user=await choose();
  await user.click(screen.getByRole('button',{name:/Eser 1.*Seç/}));
  const filters=screen.getByRole('group',{name:'Eser kategorisi'});
  await user.click(within(filters).getByRole('button',{name:'Film'}));
  await user.click(screen.getByRole('button',{name:/Eser 2.*Seç/}));
  expect(screen.getByText('Seçilen eserler (2/5)')).toBeTruthy();
  await user.click(within(filters).getByRole('button',{name:'Tümü'}));
  for(const n of [3,4,5,6])await user.click(screen.getByRole('button',{name:new RegExp(`Eser ${n}.*Seç`)}));
  expect(screen.getByText('Seçilen eserler (5/5)')).toBeTruthy();
  expect(screen.getByText(/En fazla 5 eser/)).toBeTruthy();
  await user.click(screen.getByRole('checkbox',{name:'bilimkurgu'}));
  await user.click(screen.getByRole('checkbox',{name:'karanlık'}));
  await user.click(screen.getByRole('radio',{name:/Şaşırt/}));
  await user.click(screen.getByRole('button',{name:'Önerileri göster'}));
  await waitFor(()=>expect(requests.some(r=>r.url==='/api/recommend')).toBe(true));
  const request=requests.find(r=>r.url==='/api/recommend')!;
  expect(request.body.source_ids).toEqual([1,2,3,4,5]);
  expect(request.body.answers).toMatchObject({features:['bilimkurgu'],moods:['karanlık'],mode:'surprise'});
  await user.click(screen.getByRole('button',{name:'← Eser seçimine dön'}));
  expect(screen.getByText('Seçilen eserler (5/5)')).toBeTruthy();
});

test('saved detail returns to saved items even after recommendations exist',async()=>{
  const user=await choose();await user.click(screen.getByRole('button',{name:/Eser 1.*Seç/}));
  await user.click(screen.getByRole('button',{name:'Önerileri göster'}));
  await screen.findByRole('button',{name:'Detay'});
  await user.click(screen.getByRole('button',{name:'Kaydedilenler'}));
  await user.click(await screen.findByRole('button',{name:'Detay'}));
  await user.click(screen.getByRole('button',{name:'← Kaydedilenlere dön'}));
  expect(screen.getByRole('heading',{name:'Kaydedilenler'})).toBeTruthy();
});

test('history names sources and opens stored results without making a new recommendation',async()=>{
  const user=userEvent.setup();render(<App/>);
  await user.click(await screen.findByRole('button',{name:'Profilim'}));
  expect(await screen.findByText('Eser 1 · Eser 2')).toBeTruthy();
  await user.click(screen.getByRole('button',{name:'Sonuçları aç'}));
  expect(await screen.findByText(/tarihindeki kayıtlı sonuçlar/)).toBeTruthy();
  expect(screen.getByText('Gizem eşleşmesi.')).toBeTruthy();
  expect(requests.filter(r=>r.url==='/api/recommend')).toHaveLength(0);
  await user.click(screen.getByRole('button',{name:'← Profilime dön'}));
  expect(screen.getByRole('heading',{name:'Profilim'})).toBeTruthy();
});

test('dislike removes a card and undo restores it',async()=>{
  const user=await choose();await user.click(screen.getByRole('button',{name:/Eser 1.*Seç/}));
  await user.click(screen.getByRole('button',{name:'Önerileri göster'}));
  await user.click(await screen.findByRole('button',{name:'Beğenme'}));
  await waitFor(()=>expect(screen.queryByRole('heading',{name:'Eser 6'})).toBeNull());
  await user.click(screen.getByRole('button',{name:'Geri al'}));
  expect(await screen.findByRole('heading',{name:'Eser 6'})).toBeTruthy();
});

test('profile saves persistent preferences independently of per-request choices',async()=>{
  const user=userEvent.setup();render(<App/>);
  await user.click(await screen.findByRole('button',{name:'Profilim'}));
  await user.click(screen.getByRole('checkbox',{name:'gizem'}));
  await user.click(screen.getByRole('button',{name:'Tercihleri kaydet'}));
  expect(await screen.findByText('Tercihlerin kaydedildi.')).toBeTruthy();
  expect(requests.find(r=>r.url==='/api/me/preferences')?.body.features).toEqual(['gizem']);
});
