// Weeks rebuilt with the Week 2 method (2026-10-08): rounds, no break, no capstone, practice pages per mission.
// Week-specific facts live in dl2-weekN-consistency.spec.js. Source: scripts/dl2/mission-control/weekN.py and build.py.
// DL2_ROOT points the checks at another copy of the repository (for example an export of an older commit).
const {test,expect}=require('@playwright/test');const fs=require('fs');const path=require('path');
const root=process.env.DL2_ROOT||'.';
const read=p=>fs.readFileSync(path.join(root,p),'utf8');
const heading=slide=>slide.match(/<h1[^>]*>(.*?)<\/h1>/)[1];
const appLabel=slide=>slide.match(/<span class="app">(.*?)<\/span>/)[1];
const plain=html=>html.replace(/<[^>]+>/g,' ').replace(/&amp;/g,'&').replace(/&#x27;/g,"'").replace(/\s+/g,' ');
// Extra rounds and practice pages each rebuilt week is expected to have.
const weeks={3:{rounds:11,pages:['practice-3d.html']},4:{rounds:10,pages:['practice-4c.html','practice-4d.html']},5:{rounds:6,pages:['practice-5b.html','practice-5c.html']},6:{rounds:12,pages:['practice-6a.html','practice-6b.html']}};

for(const [n,expected] of Object.entries(weeks)){
 const dir=`courses/digital-literacy-2/weeks/week-0${n}/`;
 const slides=()=>read(dir+'presentation.html').split('<section class="slide').slice(1);
 const sheet=()=>read(dir+'worksheet.html');

 test(`Week ${n}: no break and no capstone`,()=>{
  expect(slides().filter(s=>/break/i.test(heading(s)))).toEqual([]);
  expect(slides().filter(s=>/capstone/i.test(s))).toEqual([]);
  expect(plain(read(dir+'lesson-plan.html'))).not.toMatch(/Protect the 8-minute break/);
 });

 test(`Week ${n}: the worksheet links practice pages, never numbered practice-library exercises`,()=>{
  // build.py rewrites "slide N" to "practice library exercise N"; rebuilt weeks link one practice page per mission.
  expect(plain(sheet())).not.toMatch(/practice library exercise/);
 });

 test(`Week ${n}: each Show picture highlights the step the slide names`,()=>{
  const states=[...slides().join('').matchAll(/<div class="mission-state" data-state="(\d)"[^>]*>.*?<strong>(.*?)<\/strong><div data-visual>(.*?)<\/div><div class="artifact-path"/gs)];
  expect(states.length).toBe(12);
  for(const [,step,title,visual] of states){
   const active=visual.match(/<div class="visual-row visual-active"><span>(.*?)<\/span>/);
   if(active)expect(active[1],`step ${step} of ${title}`).toBe(title);
   else expect(visual,`${title} photo step has a caption`).toMatch(/visual-caption">[^<]+</);
  }
 });

 test(`Week ${n}: rounds whose material is printed on the worksheet say Worksheet on the slide`,()=>{
  const rounds=[...sheet().matchAll(new RegExp(`<div class="round" id="m${n}[A-D]-r\\d"><h3>Round (\\d) · (.*?)</h3>(.*?)<label`,'gs'))];
  expect(rounds.length).toBe(expected.rounds);
  const mislabelled=rounds.filter(([,,,body])=>/<table|<blockquote/.test(body))
   .map(([,r,title])=>slides().find(s=>heading(s)===`Round ${r}: ${title}`))
   .filter(slide=>!appLabel(slide).startsWith('Worksheet'))
   .map(slide=>`${heading(slide)} is labelled ${appLabel(slide)}`);
  expect(mislabelled).toEqual([]);
 });

 test(`Week ${n}: each mission answer box sits under its own tasks, before the extra rounds`,()=>{
  for(const mission of ['A','B','C','D'].map(l=>n+l)){
   const box=sheet().indexOf(`id="evidence-${mission}"`),firstRound=sheet().indexOf(`id="m${mission}-r2"`);
   expect(box,`Mission ${mission} answer box`).toBeGreaterThan(-1);
   if(firstRound>-1)expect(box,`Mission ${mission}: answer box comes after Round 2`).toBeLessThan(firstRound); // Mission 5D, the skills challenge, has no rounds
  }
 });

 test(`Week ${n}: practice pages exist and every link to them opens a new tab`,()=>{
  const pages=fs.readdirSync(path.join(root,dir)).filter(f=>/^practice-\d[a-d]\.html$/.test(f)).sort();
  expect(pages).toEqual(expected.pages);
  for(const page of pages){
   expect(slides().join(''),`a slide links ${page}`).toContain(`href="${page}" target="_blank"`);
   expect(sheet(),`the worksheet links ${page}`).toContain(`href="${page}" target="_blank"`);
  }
 });
}
