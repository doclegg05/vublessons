// Week 3 (resource pack): the deck, the worksheet, the practice page and the video must agree with each other.
// Source: scripts/dl2/mission-control/week3.py, visuals.py and build.py; regenerate before running.
// DL2_ROOT points the checks at another copy of the repository (for example an export of an older commit).
const {test,expect}=require('@playwright/test');const fs=require('fs');const path=require('path');
const root=process.env.DL2_ROOT||'.';
const read=p=>fs.readFileSync(path.join(root,p),'utf8');
const dir='courses/digital-literacy-2/weeks/week-03/';
const slides=read(dir+'presentation.html').split('<section class="slide').slice(1);
const sheet=read(dir+'worksheet.html');
const heading=slide=>slide.match(/<h1[^>]*>(.*?)<\/h1>/)[1];
const appLabel=slide=>slide.match(/<span class="app">(.*?)<\/span>/)[1];
const plain=html=>html.replace(/<[^>]+>/g,' ').replace(/&amp;/g,'&').replace(/&#x27;/g,"'").replace(/\s+/g,' ');

test('Supplies are listed in the CSV order everywhere: paper, folders, pens',()=>{
 const csv=read('courses/digital-literacy-2/assets/supplies.csv').split('\n').slice(1,4).map(r=>r.split(',')[0]);
 expect(csv).toEqual(['Paper','Folders','Pens']);
 const deck=plain(slides.join(' ')).toLowerCase();
 expect(deck).toContain('paper $12 + folders $8 + pens $5');
 expect(deck).not.toMatch(/pens \$8|pens \+ folders/);
});

test('The lesson has no break and no capstone',()=>{
 expect(slides.filter(s=>/break/i.test(heading(s)))).toEqual([]);
 expect(slides.filter(s=>/capstone/i.test(s))).toEqual([]);
 expect(plain(read(dir+'lesson-plan.html'))).not.toMatch(/Protect the 8-minute break/);
});

test('Worksheet text names PowerPoint slides in words, never as practice-library exercises',()=>{
 // build.py rewrites "slide N" to "practice library exercise N"; Week 3 links practice pages instead.
 expect(plain(sheet)).not.toMatch(/practice library exercise/);
});

test('Each Show picture highlights the step the slide names',()=>{
 const states=[...slides.join('').matchAll(/<div class="mission-state" data-state="(\d)"[^>]*>.*?<strong>(.*?)<\/strong><div data-visual>(.*?)<\/div><div class="artifact-path"/gs)];
 expect(states.length).toBe(12);
 for(const [,step,title,visual] of states){
  const active=visual.match(/<div class="visual-row visual-active"><span>(.*?)<\/span>/);
  if(active)expect(active[1],`step ${step} of ${title}`).toBe(title);
  else expect(visual,`${title} photo step has a caption`).toMatch(/visual-caption">[^<]+</);
 }
});

test('Rounds whose material is printed on the worksheet say Worksheet on the slide',()=>{
 const rounds=[...sheet.matchAll(/<div class="round" id="m3[A-D]-r\d"><h3>Round (\d) · (.*?)<\/h3>(.*?)<label/gs)];
 expect(rounds.length).toBe(11);
 const mislabelled=rounds.filter(([,,,body])=>/<table|<blockquote/.test(body))
  .map(([,n,title])=>slides.find(s=>heading(s)===`Round ${n}: ${title}`))
  .filter(slide=>!appLabel(slide).startsWith('Worksheet'))
  .map(slide=>`${heading(slide)} is labelled ${appLabel(slide)}`);
 expect(mislabelled).toEqual([]);
});

test('Each mission answer box sits under its own tasks, before the extra rounds',()=>{
 for(const mission of ['3A','3B','3C','3D']){
  const box=sheet.indexOf(`id="evidence-${mission}"`),firstRound=sheet.indexOf(`id="m${mission}-r2"`);
  expect(box,`Mission ${mission} answer box`).toBeGreaterThan(-1);
  expect(box,`Mission ${mission}: answer box comes after Round 2`).toBeLessThan(firstRound);
 }
});

test('Clip editing has its own practice page, linked from its round on the slide and the worksheet',()=>{
 const pages=fs.readdirSync(path.join(root,dir)).filter(f=>/^practice-\d[a-d]\.html$/.test(f));
 expect(pages).toEqual(['practice-3d.html']);
 const round=slides.find(s=>heading(s)==='Round 4: Trim and split a clip');
 expect(round).toContain('href="practice-3d.html" target="_blank"');
 expect(sheet.match(/id="m3D-r4".*?<\/h3><p class="app-line">(.*?)<\/p>/s)[1]).toContain('href="practice-3d.html"');
 expect(read(dir+'practice-3d.html')).toContain('data-trim-lab');
});
