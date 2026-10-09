// Video pause cards and topic dividers (Britt, 2026-10-08): every card must point at real lesson material,
// every spoken pause prompt gets a card with about 10 seconds of silence, and the transcript carries the card text.
// Sources: video/digital-literacy-2/week-NN/cards.json, narration/beats.json; scripts/dl2/build-media.py.
const {test,expect}=require('@playwright/test');const fs=require('fs');
const read=p=>fs.readFileSync(p,'utf8');
const weeks=[1,2,3,4,5,6].map(n=>String(n).padStart(2,'0')).filter(w=>fs.existsSync(`video/digital-literacy-2/week-${w}/cards.json`));

test('At least one week has video cards',()=>expect(weeks.length).toBeGreaterThan(0));

for(const w of weeks){
 const cards=JSON.parse(read(`video/digital-literacy-2/week-${w}/cards.json`)).chapters;
 const beats=JSON.parse(read(`video/digital-literacy-2/week-${w}/narration/beats.json`));
 const sheet=read(`courses/digital-literacy-2/weeks/week-${w}/worksheet.html`);
 const deck=read(`courses/digital-literacy-2/weeks/week-${w}/presentation.html`);
 const transcript=read(`courses/digital-literacy-2/weeks/week-${w}/video-transcript.html`);
 const tasksIn=mission=>{const section=sheet.match(new RegExp(`<section class="mission" id="m${mission}">.*?<ol>(.*?)</ol>`,'s'));return section?(section[1].match(/<li>/g)||[]).length:0;};

 test(`Week ${w}: every pause card names worksheet tasks or rounds that exist`,()=>{
  for(const [id,card] of Object.entries(cards))if(card.pause){
   const m=card.pause.where.match(/^Mission (\d[A-E]), (?:tasks? (\d+)(?:(?: to | and )(\d+))?|Round (\d+))$/);
   expect(m,`${id}: "${card.pause.where}"`).not.toBeNull();
   const [,mission,first,last,round]=m;
   if(round)expect(sheet,`${id}: Round ${round} of Mission ${mission}`).toContain(`id="m${mission}-r${round}"`);
   else expect(tasksIn(mission),`${id}: Mission ${mission} has task ${last||first}`).toBeGreaterThanOrEqual(Number(last||first));
   expect(card.pause.try.length).toBeGreaterThan(0);
  }
 });

 test(`Week ${w}: every divider names a mission title the deck uses`,()=>{
  for(const [id,card] of Object.entries(cards))if(card.divider&&card.divider.mission){
   const letter=card.divider.mission.slice(1);
   expect(deck,`${id}: Mission ${card.divider.mission}`).toContain(`>${letter} · ${card.divider.title}</option>`);
  }
 });

 test(`Week ${w}: every spoken pause prompt ends its chapter and holds about 10 seconds behind a card`,()=>{
  for(const b of beats){
   const spoken=/Pause the video/.test(b.text);
   expect(Boolean(cards[b.id]?.pause),`${b.id}: pause card matches the narration`).toBe(spoken);
   if(spoken){expect(b.text.trim()).toMatch(/Pause the video now\.$/);expect(b.visualHold).toBeGreaterThanOrEqual(10);}
   if(cards[b.id]?.divider)expect(b.leadIn).toBeGreaterThanOrEqual(3);
  }
 });

 test(`Week ${w}: the transcript carries each pause card's steps`,()=>{
  const text=transcript.replace(/<[^>]+>/g,' ').replace(/&#x27;/g,"'").replace(/&amp;/g,'&').replace(/\s+/g,' ');
  for(const card of Object.values(cards))if(card.pause)expect(text).toContain(`Worksheet: ${card.pause.where}.`);
 });
}
