// Week 1 follows Tell, Show, Do, Review cycles inside WIPPEA (2026-09-26 Week 1 structure review).
// Sources: scripts/dl2/author-content.py (week 1) and scripts/dl2/build-pages.py; regenerate before running.
const {test,expect}=require('@playwright/test');const fs=require('fs');
const read=p=>fs.readFileSync(p,'utf8');
const w1=JSON.parse(read('scripts/dl2/curriculum.json')).weeks[0];
const w6=JSON.parse(read('scripts/dl2/curriculum.json')).weeks[5];
const dir='courses/digital-literacy-2/weeks/week-01';
const plan=read(`${dir}/lesson-plan.html`);
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

test('Week 1 plays each video chapter inside its cycle and names the pause points',()=>{
 const all=w1.agenda.map(a=>a[2]).join(' ');
 for(let ch=1;ch<=10;ch++)expect(all,`chapter ${ch} is scheduled`).toMatch(new RegExp(`\\bchapters? (?:\\d+(?:[–-]| and ))?${ch}\\b|\\bchapters? ${ch}(?:[–-]| and )\\d+`));
 for(const t of ['1:24','2:02','5:36','6:28'])expect(all,`pause at ${t}`).toContain(t);
 expect(all).not.toMatch(/Play the explainer/);
});

test('Week 1 pre-test step records each score instead of printing full reports',()=>{
 const pre=w1.agenda.find(([,phase])=>phase==='Pre-test')[2];
 expect(pre).toMatch(/record each score/i);expect(pre).toMatch(/page 1/i);
});

test('Week 1 Mission Control plan covers five observable tasks and all 120 minutes',()=>{
 const plain=text(plan);
 for(const task of ['Change Display Scale','Select a headset output','Adjust flyer margins','Create a fictional recurring calendar event','Undo an automatic change'])expect(plain).toContain(task);
 for(const range of ['slides 1–2','slides 3–4','slides 5–8','slides 9–12','slides 13–16','slides 17–20','slides 21–25','slides 26–27'])expect(plain).toContain(range);
 expect(plain).toContain('100–120 (20 min)');
 expect(plain).toContain('20-question pre-test');
 expect(plain).toContain('paper simulation');
 expect(plain).not.toContain('out of 28');
});

test('Week 1 worksheet tasks give learners everything they need to finish them',()=>{
 const [,,,t4,t5,,t7,t8]=w1.lab;
 for(const job of ['external screen','wired network','flash drive'])expect(t4).toContain(job);
 expect(t5).toMatch(/paper/i);expect(t5).toMatch(/simulated/i);
 expect(t7).toMatch(/page 1 of this worksheet/i);expect(t7).toMatch(/Ctrl and P/);
 expect(t8).toMatch(/\bteh\b/);expect(t8).toMatch(/Ctrl and Z/);
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

// Narrowed 2026-09-28 (Mission Control, Task 11): the lesson plan only. The generated worksheet's quick card was
// replaced by the letterhead missions 1A–1E, which give Windows 11 steps per mission (dl2-os-week1-print.spec.js).
test('Week 1 lab quick card gives Windows 11 steps on the lesson plan',()=>{
 expect(w1.lab_paths.length).toBeGreaterThanOrEqual(8);
 for(const row of w1.lab_paths)expect(row).toHaveLength(2);
 const plain=text(plan);
 expect(plain).toMatch(/Windows 11/);
 for(const [task,steps] of w1.lab_paths){expect(plain).toContain(task);expect(plain).toContain(steps);}
});

test('Week 1 prep list is specific to week 1',()=>{
 const plain=text(plan);
 expect(plain).not.toMatch(/For week 6/);expect(plain).not.toMatch(/spreadsheet app/);
 for(const item of ['headset','supplied flyer','Start fresh on this computer'])expect(plain).toContain(item);
 expect(text(read('courses/digital-literacy-2/weeks/week-06/lesson-plan.html'))).toMatch(/plain-text editor/);
 expect(w6.prep===undefined||typeof w6.prep==='string').toBe(true);
});
