// Week 1 follows Tell, Show, Do, Review cycles inside WIPPEA (2026-09-26 Week 1 structure review).
// Sources: scripts/dl2/author-content.py (week 1) and scripts/dl2/build-pages.py; regenerate before running.
const {test,expect}=require('@playwright/test');const fs=require('fs');
const read=p=>fs.readFileSync(p,'utf8');
const w1=JSON.parse(read('scripts/dl2/curriculum.json')).weeks[0];
const w6=JSON.parse(read('scripts/dl2/curriculum.json')).weeks[5];
const dir='courses/digital-literacy-2/weeks/week-01';
const plan=read(`${dir}/lesson-plan.html`),worksheet=read(`${dir}/worksheet.html`);
const text=html=>html.replace(/<[^>]+>/g,' ').replace(/&amp;/g,'&').replace(/&#x27;/g,"'").replace(/&quot;/g,'"').replace(/\s+/g,' ');
const slide=title=>{const s=w1.slides.find(s=>s.title===title);if(!s)throw new Error(`no slide "${title}"`);return s;};

test('Week 1 agenda teaches each skill group as its own Tell, Show, Do, Review cycle',()=>{
 expect(w1.agenda.reduce((n,a)=>n+a[0],0)).toBe(120);
 const cycles=w1.agenda.filter(([,phase])=>/^Cycle [A-E]\b/.test(phase));
 expect(cycles).toHaveLength(5);
 for(const [,phase,action] of cycles)for(const step of ['Tell','Show','Do','Review'])expect(action,`${phase} names its ${step} step`).toContain(step+':');
 const all=w1.agenda.map(a=>a[2]).join(' ');
 expect(all).not.toMatch(/switch driver and coach roles halfway/i);
 expect(all).toMatch(/every learner/i);
});

test('Week 1 teaches live; the video is home viewing, and every unit is on the run sheet',()=>{
 const all=w1.agenda.map(a=>a[2]).join(' ');
 for(const [,phase,action] of w1.agenda.filter(([,p])=>/^Cycle/.test(p)))expect(action,`${phase} plays no video`).not.toMatch(/chapter \d|Play the explainer|Play chapter/);
 expect(w1.agenda.at(-1)[2]).toMatch(/video/i);
 // Units are the single source: five, each with the Tell, Show, Do, Review parts, in the agenda order.
 const units=w1.runsheet.filter(x=>x.kind==='unit');
 expect(units.map(u=>u.letter)).toEqual(['A','B','C','D','E']);
 expect(w1.runsheet.reduce((n,x)=>n+x.minutes,0)).toBe(120);
 const run=text(read(`${dir}/run-sheet.html`));
 for(const u of units){
  for(const key of ['problem','do'])expect(u[key].length).toBeGreaterThan(20);
  for(const key of ['tell','show','review'])expect(u[key].length).toBeGreaterThan(0);
  expect(u.show.length,`unit ${u.letter} shows real clicks`).toBeGreaterThanOrEqual(3);
  for(const step of u.show)expect(run).toContain(step);
  expect(u.do).toMatch(/every learner/);
  const row=w1.agenda.find(([,p])=>p.startsWith(`Cycle ${u.letter}`));
  expect(row[0]).toBe(u.minutes);
  for(const s of u.slides)expect(w1.slides.map(x=>x.title)).toContain(s);
 }
 // The post-test items that belong to week 1 are each the target of a unit.
 const tested=units.flatMap(u=>u.tested);
 for(const item of ['post 1','post 2','post 3','post 4','post 8'])expect(tested).toContain(item);
 expect(run).toMatch(/Pose the problem/);
});

test('Week 1 pre-test step records each score instead of printing full reports',()=>{
 const pre=w1.agenda.find(([,phase])=>phase==='Pre-test')[2];
 expect(pre).toMatch(/record each score/i);expect(pre).toMatch(/page 1/i);
});

test('Week 1 lesson plan states measurable ABCD outcomes, including the two that were missing',()=>{
 expect(w1.outcomes).toHaveLength(5);
 const plain=text(plan);
 for(const o of w1.outcomes)expect(plain).toContain(o);
 expect(w1.outcomes.join(' ')).toMatch(/AutoCorrect/);expect(w1.outcomes.join(' ')).toMatch(/help request/i);
 expect(w1.objectives).toHaveLength(5);
});

test('Week 1 worksheet tasks give learners everything they need to finish them',()=>{
 // Tasks follow the units: 2 zoom, 3 sound, 4 print preview, 5 cables, 6 paper calendar, 7 views and sharing, 8 undo and help.
 const [,,,print,cables,calendar,,help]=w1.lab;
 for(const job of ['external screen','wired network','flash drive'])expect(cables).toContain(job);
 expect(calendar).toMatch(/paper/i);expect(calendar).toMatch(/simulated/i);
 expect(print).toMatch(/page 1 of this worksheet/i);expect(print).toMatch(/Ctrl and P/);
 expect(help).toMatch(/\bteh\b/);expect(help).toMatch(/Ctrl and Z/);
 expect(w1.lab).toHaveLength(8);
});

test('Week 1 slides say how printers, screens and connectors really behave',()=>{
 expect(slide('Printer choices').body).toMatch(/last printer you used/i);
 expect(slide('Printer choices').body).toMatch(/color/i);
 expect(slide('Sound and screen checks').body).toMatch(/buttons on the monitor/i);
 expect(slide('Match a connection to its job').cards.find(c=>/flash drive/.test(c[0]))[1]).toMatch(/power/i);
 expect(slide('Automation still needs a check').body).not.toMatch(/repeat a reminder/);
 expect(slide('Make text comfortable').body).toMatch(/each site/i);
 expect(slide('Print one page before twenty').body).toMatch(/when printing is allowed/i);
});

test('Week 1 knowledge checks offer believable wrong answers',()=>{
 const options=w1.slides.filter(s=>s.kind==='check').flatMap(s=>s.options);
 for(const silly of ['Buy a new monitor','Erase the browser history','Publish your account password'])expect(options).not.toContain(silly);
});

test('Week 1 lab quick card gives Windows 10 steps, with Windows 11 notes, on the lesson plan and the worksheet',()=>{
 expect(w1.lab_os).toBe('Windows 10');
 expect(w1.lab_paths.length).toBeGreaterThanOrEqual(8);
 for(const row of w1.lab_paths)expect(row).toHaveLength(2);
 for(const page of [plan,worksheet]){const plain=text(page);
  expect(plain).toMatch(/Lab quick card: Windows 10/);expect(plain).toMatch(/Windows 11/);
  for(const [task,steps] of w1.lab_paths){expect(plain).toContain(task);expect(plain).toContain(steps);}}
});

test('Week 1 prep list is specific to week 1',()=>{
 const plain=text(plan);
 expect(plain).not.toMatch(/For week 6/);expect(plain).not.toMatch(/spreadsheet app/);
 for(const item of ['headset','HDMI','Start fresh on this computer'])expect(plain).toContain(item);
 expect(text(read('courses/digital-literacy-2/weeks/week-06/lesson-plan.html'))).toMatch(/plain-text editor/);
 expect(w6.prep===undefined||typeof w6.prep==='string').toBe(true);
});
