// Week 2 (AI-assisted search): the deck, the worksheet and the demo must agree with each other.
// Source: scripts/dl2/mission-control/week2.py, visuals.py and build.py; regenerate before running.
const {test,expect}=require('@playwright/test');const fs=require('fs');
const read=p=>fs.readFileSync(p,'utf8');
const dir='courses/digital-literacy-2/weeks/week-02/';
const slides=read(dir+'presentation.html').split('<section class="slide').slice(1);
const sheet=read(dir+'worksheet.html');
const heading=slide=>slide.match(/<h1[^>]*>(.*?)<\/h1>/)[1];
const appLabel=slide=>slide.match(/<span class="app">(.*?)<\/span>/)[1];

test.describe('Week 2 Mission A demo teaches the AI-search steps',()=>{
 const demo=slides.find(s=>s.includes('data-mission-demo'));
 const active=[...demo.matchAll(/<div class="visual-row visual-active"><span>(.*?)<\/span><b>(.*?)<\/b>/g)].map(m=>({label:m[1],value:m[2]}));
 test('step 1 highlights a full-sentence question, not keywords',()=>{
  expect(active[0].value).toMatch(/\?$/);
  expect(active[0].value.split(/\s+/).length).toBeGreaterThanOrEqual(8);
 });
 test('steps 2 and 3 put an AI answer beside a library page that disagrees with it',()=>{
  expect(active[1].label).toMatch(/AI answer/i);
  expect(active[2].label).toMatch(/page/i);
  expect(active[1].value).not.toBe(active[2].value);
 });
 test('the review question repeats the same two facts the demo showed',()=>{
  const review=heading(slides.slice(slides.indexOf(demo)).find(s=>s.includes('mission-check')));
  for(const {value} of active.slice(1))expect(review.toLowerCase()).toContain(value.toLowerCase().replace(/^open /,''));
 });
});

test('Rounds whose material is printed on the worksheet say Worksheet on the slide',()=>{
 const rounds=[...sheet.matchAll(/<div class="round" id="m2[A-D]-r\d"><h3>Round (\d) · (.*?)<\/h3>(.*?)<label/gs)];
 expect(rounds.length).toBe(10);
 const mislabelled=rounds.filter(([,,,body])=>/<table|<blockquote/.test(body))
  .map(([,n,title])=>slides.find(s=>heading(s)===`Round ${n}: ${title}`))
  .filter(slide=>!appLabel(slide).startsWith('Worksheet'))
  .map(slide=>`${heading(slide)} is labelled ${appLabel(slide)}`);
 expect(mislabelled).toEqual([]);
});

test('Each mission answer box sits under its own tasks, before the extra rounds',()=>{
 for(const mission of ['2A','2B','2C','2D']){
  const box=sheet.indexOf(`id="evidence-${mission}"`),firstRound=sheet.indexOf(`id="m${mission}-r2"`);
  expect(box,`Mission ${mission} answer box`).toBeGreaterThan(-1);
  expect(box,`Mission ${mission}: answer box comes after Round 2`).toBeLessThan(firstRound);
 }
});
