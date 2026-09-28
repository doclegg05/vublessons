// Weeks 2–6 follow the week 1 model: Tell, Show, Do, Review cycles inside WIPPEA (2026-09-26 reviews).
// Sources: scripts/dl2/author-content.py and scripts/dl2/build-pages.py; regenerate before running.
const {test,expect}=require('@playwright/test');const fs=require('fs');
const read=p=>fs.readFileSync(p,'utf8');
const weeks=JSON.parse(read('scripts/dl2/curriculum.json')).weeks;
const text=html=>html.replace(/<[^>]+>/g,' ').replace(/&amp;/g,'&').replace(/&#x27;/g,"'").replace(/&quot;/g,'"').replace(/\s+/g,' ');
// Video pause points: the end of each practice prompt, from the narration word timings.
const pauses={2:['1:17','3:29','5:02','6:35'],3:['1:58','6:28'],4:['1:29','2:54','4:22','6:35'],5:['1:23','2:43','3:36','4:55','6:13'],6:['2:52','6:37']};
// Throwaway knowledge-check options named in the 2026-09-26 content review.
// 2026-09-28 (Mission Control, Task 11): the post-test now has 20 questions. The week 5 plan was corrected by hand;
// scripts/dl2/curriculum.json still says "28-question" (the generator was off limits for that task). Remove this
// mapping once the source says 20 and the plan is regenerated.
const asPublished=o=>o.replace('the 28-question post-test','the 20-question post-test');
const silly=['Count the page’s colors','Delete their document','This is bad.','I dislike everything.','Only the button color','Whether the site has animations','Share your password instead','Skip testing','Add real personal records immediately'];

for(const n of [2,3,4,5,6]){
 const w=weeks[n-1],dir=`courses/digital-literacy-2/weeks/week-0${n}`;
 const plan=()=>text(read(`${dir}/lesson-plan.html`)),worksheet=()=>text(read(`${dir}/worksheet.html`));
 const actions=()=>w.agenda.map(a=>a[2]).join(' ');

 test(`Week ${n} agenda teaches in Tell, Show, Do, Review cycles`,()=>{
  expect(w.agenda.reduce((t,a)=>t+a[0],0)).toBe(120);
  const cycles=w.agenda.filter(([,phase])=>/^Cycle [A-F]\b/.test(phase));
  expect(cycles.length).toBeGreaterThanOrEqual(3);
  for(const [,phase,action] of cycles)for(const step of ['Tell','Show','Do','Review'])expect(action,`${phase} names its ${step} step`).toContain(step+':');
  expect(actions()).toMatch(/every learner/i);
  expect(actions()).not.toMatch(/switch driver and coach roles halfway/i);
  // 2026-09-28: Britt teaches without a class break (was: one 10-minute break).
  expect(w.agenda.some(([,phase])=>/break/i.test(phase))).toBe(false);
 });

 test(`Week ${n} plays every video chapter inside the plan and names the pause points`,()=>{
  const all=actions();
  for(let ch=1;ch<=10;ch++)expect(all,`chapter ${ch} is scheduled`).toMatch(new RegExp(`\\bchapters? (?:\\d+(?:[–-]| and ))?${ch}\\b|\\bchapters? ${ch}(?:[–-]| and )\\d+`));
  for(const t of pauses[n])expect(all,`pause at ${t}`).toContain(t);
  expect(all).not.toMatch(/Play the explainer|Play the (cloud-file|sharing|safety|app) explainer/);
 });

 test(`Week ${n} lesson plan states measurable outcomes for every goal`,()=>{
  expect(w.outcomes.length).toBe(w.objectives.length);
  expect(w.outcomes.length).toBeGreaterThanOrEqual(3);
  const p=plan();for(const o of w.outcomes){expect(o).toMatch(/^[A-Z][^:]{1,40}: /);expect(p).toContain(asPublished(o));}
 });

 test(`Week ${n} has a week-specific prep list and a Windows 11 quick card`,()=>{
  expect(typeof w.prep).toBe('string');expect(w.prep).toMatch(/Start fresh on this computer/);
  expect(w.lab_paths.length).toBeGreaterThanOrEqual(6);
  for(const row of w.lab_paths)expect(row).toHaveLength(2);
  for(const page of [plan(),worksheet()]){expect(page).toMatch(/Lab quick card: Windows 11/);for(const [task,steps] of w.lab_paths){expect(page).toContain(task);expect(page).toContain(steps);}}
 });

 test(`Week ${n} knowledge checks offer believable wrong answers`,()=>{
  const options=w.slides.filter(s=>s.kind==='check').flatMap(s=>s.options);
  for(const o of silly)expect(options).not.toContain(o);
  expect(w.lab).toHaveLength(8);expect(w.answers).toHaveLength(8);
 });
}
