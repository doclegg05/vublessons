// Week 3 guided build (2026-10-12). Britt's definition of done: a beginner can go slide by slide and finish
// every task; anything critical left out is a failure. Source: scripts/dl2/mission-control/week3.py and guided.py.
const {test,expect}=require('@playwright/test');const fs=require('fs');
const read=p=>fs.readFileSync(p,'utf8');
const dir='courses/digital-literacy-2/weeks/week-03';
const text=html=>html.replace(/<[^>]+>/g,' ').replace(/&amp;/g,'&').replace(/&#x27;/g,"'").replace(/&quot;/g,'"').replace(/&lt;/g,'<').replace(/&gt;/g,'>').replace(/\s+/g,' ').trim();
const deck=()=>read(`${dir}/presentation.html`);
const slides=()=>[...deck().matchAll(/<section class="slide([^"]*)"[^>]*>([\s\S]*?)<\/section>/g)].map(m=>({cls:m[1],html:m[2],shown:m[2].replace(/<aside class="notes">[\s\S]*?<\/aside>/,'')}));
const steps=()=>slides().filter(s=>/\bg-step\b/.test(s.cls));
const title=s=>text(/<h1[^>]*>([\s\S]*?)<\/h1>/.exec(s.html)[1]);
const programs=['Microsoft Word','Microsoft Excel','Microsoft PowerPoint'];

test('Week 3 shows its four goals up front, each with its program, and they match the four Week 3 post-test items',()=>{
 const goals=slides().find(s=>title(s)==='Tonight’s goals'||title(s)==="Tonight's goals");
 expect(goals,'a goals slide').toBeTruthy();
 const rows=[...goals.shown.matchAll(/<li>([\s\S]*?)<\/li>/g)].map(m=>text(m[1]));
 expect(rows).toHaveLength(4);
 ['Word','Word','Excel','PowerPoint'].forEach((app,i)=>expect(rows[i]).toContain(`Part ${i+1} · ${app}`));
 const items=read('courses/digital-literacy-2/os/items.js');
 const map=/var W = \{([^}]*)\}/.exec(items)[1];
 const week3=[...map.matchAll(/(\d+): 3\b/g)].map(m=>Number(m[1]));
 expect(week3).toEqual([9,10,11,12]);
 const plan=text(read(`${dir}/lesson-plan.html`));
 for(const n of week3)expect(plan).toContain(`post-test item ${n}`);
});

test('Each part opens with a slide naming its program, and every slide says which program you are in',()=>{
 const opens=slides().filter(s=>/\bg-orient\b/.test(s.cls)).map(title);
 expect(opens).toEqual(['Now working in: Microsoft Word','Still working in: Microsoft Word','Now working in: Microsoft Excel','Now working in: Microsoft PowerPoint']);
 for(const s of slides().filter(s=>/\bg-(step|map|orient|tell|watch|check)\b/.test(s.cls)))
  expect(text(/<div class="hud">([\s\S]*?)<\/div>/.exec(s.html)[1]),title(s)).toMatch(/Working in: (Microsoft (Word|Excel|PowerPoint|Edge)|File Explorer)/);
});

test('Every step slide gives one or two actions and what you should see',()=>{
 const all=steps();expect(all.length).toBeGreaterThanOrEqual(40);
 for(const s of all){
  const actions=[...s.shown.matchAll(/<ol class="g-actions">([\s\S]*?)<\/ol>/g)];
  expect(actions,title(s)).toHaveLength(1);
  const items=[...actions[0][1].matchAll(/<li>/g)];
  expect(items.length,title(s)).toBeGreaterThanOrEqual(1);expect(items.length,title(s)).toBeLessThanOrEqual(2);
  expect(text(s.shown),title(s)).toMatch(/You should see: \S/);
  expect(s.shown,title(s)).toMatch(/data-visual/);
 }
});

test('The worksheet repeats every step in the same order, each with You should see and a check box',()=>{
 const ws=read(`${dir}/worksheet.html`);
 const wsSteps=[...ws.matchAll(/<li><span class="n">\d+<\/span><div class="d"><b class="act">([\s\S]*?)\.<\/b>[\s\S]*?<span class="see">[\s\S]*?<\/span><\/div><label class="box"><input type="checkbox">/g)].map(m=>text(m[1]));
 expect(wsSteps).toEqual(steps().map(title));
 const t=text(ws);
 expect(t).toContain('Week 3 · Worksheet');
 for(const [i,app] of ['MICROSOFT WORD','MICROSOFT WORD','MICROSOFT EXCEL','MICROSOFT POWERPOINT'].entries())expect(t).toContain(`PART ${i+1} OF 4 · ${app}`);
 expect(t).toContain('BEFORE WE START');expect(t).not.toMatch(/practice library exercise/i);
 // The photo downloads from this site, so Edge honours the download attribute.
 expect(ws).toContain('href="/courses/digital-literacy-2/assets/practice-photo.jpg" download="practice-photo.jpg"');
 expect(fs.existsSync('courses/digital-literacy-2/assets/practice-photo.jpg')).toBe(true);
 // The prediction is written before the change, and survives printing.
 expect(ws).toMatch(/<textarea class="worksheet-input" id="predict-[^"]+"[^>]*><\/textarea><span class="print-answer"><\/span>/);
});

test('Only tonight’s skills are taught: no cut topics on slides or worksheet, and no break',()=>{
 const learnerText=text(slides().map(s=>s.shown).join(' '))+' '+text(read(`${dir}/worksheet.html`));
 for(const cut of [/Track Changes/i,/Ctrl\+K|Ctrl and K/i,/\bchart\b/i,/\btrim\b/i,/\bsplit\b/i,/alt text/i,/Ctrl\+C|Ctrl and C/i,/Ctrl\+V|Ctrl and V/i,/Take an 8-minute break/i])
  expect(learnerText).not.toMatch(cut);
 expect(text(read(`${dir}/lesson-plan.html`))).not.toMatch(/Protected break/i);
});

test('The 120-minute plan adds up and names every part',()=>{
 const plan=read(`${dir}/lesson-plan.html`);
 const rows=[...plan.matchAll(/<tr><td>(\d+)–(\d+) \((\d+) min\)<\/td><td>[^<]*<\/td><td>([^<]*)<\/td><\/tr>/g)];
 expect(rows.reduce((t,r)=>t+Number(r[3]),0)).toBe(120);
 expect(Number(rows.at(-1)[2])).toBe(120);
 for(const p of ['Part 1 · Microsoft Word','Part 2 · Microsoft Word','Part 3 · Microsoft Excel','Part 4 · Microsoft PowerPoint'])expect(rows.map(r=>r[4]).join('|')).toContain(p);
 expect(rows.length).toBeGreaterThanOrEqual(6);
 expect(plan).toContain('<meta name="robots" content="noindex">');
});

test('Learner pages link only learner pages',()=>{
 for(const page of ['presentation','worksheet']){
  const hrefs=[...read(`${dir}/${page}.html`).matchAll(/href="([^"]*)"/g)].map(m=>m[1]);
  expect(hrefs.filter(h=>/answer-key|lesson-plan|instructor/.test(h)),page).toEqual([]);
 }
});
