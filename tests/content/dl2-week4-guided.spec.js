// Week 4 guided build (2026-10-19). Same definition of done as Week 3: a beginner can go slide by slide and finish every
// task; anything critical left out is a failure. Source: scripts/dl2/mission-control/week4.py and guided.py.
const {test,expect}=require('@playwright/test');const fs=require('fs');
const read=p=>fs.readFileSync(p,'utf8');
const dir='courses/digital-literacy-2/weeks/week-04';
const text=html=>html.replace(/<[^>]+>/g,' ').replace(/&amp;/g,'&').replace(/&#x27;/g,"'").replace(/&quot;/g,'"').replace(/&lt;/g,'<').replace(/&gt;/g,'>').replace(/\s+/g,' ').trim();
const deck=()=>read(`${dir}/presentation.html`);
const slides=()=>[...deck().matchAll(/<section class="slide([^"]*)"[^>]*>([\s\S]*?)<\/section>/g)].map(m=>({cls:m[1],html:m[2],shown:m[2].replace(/<aside class="notes">[\s\S]*?<\/aside>/,'')}));
const steps=()=>slides().filter(s=>/\bg-step\b/.test(s.cls));
const title=s=>text(/<h1[^>]*>([\s\S]*?)<\/h1>/.exec(s.html)[1]);
const GMAIL='Gmail (in Microsoft Edge)';
const learnerText=()=>text(slides().map(s=>s.shown).join(' '))+' '+text(read(`${dir}/worksheet.html`));

test('Week 4 shows its five goals up front, each with its program, and they match the five Week 4 post-test items',()=>{
 const goals=slides().find(s=>/Tonight.s goals/.test(title(s)));
 expect(goals,'a goals slide').toBeTruthy();
 const rows=[...goals.shown.matchAll(/<li>([\s\S]*?)<\/li>/g)].map(m=>text(m[1]));
 expect(rows).toHaveLength(5);
 ['Part 1 · Gmail','Part 1 · Gmail','Part 2 · Gmail','Part 3 · Word','Part 4 · Edge'].forEach((label,i)=>expect(rows[i]).toContain(label));
 const items=read('courses/digital-literacy-2/os/items.js');
 const map=/var W = \{([^}]*)\}/.exec(items)[1];
 const week4=[...map.matchAll(/(\d+): 4\b/g)].map(m=>Number(m[1]));
 expect(week4).toEqual([13,14,15,16,17]);
 const plan=text(read(`${dir}/lesson-plan.html`));
 for(const n of week4)expect(plan).toContain(`post-test item ${n}`);
});

test('Each part opens with a slide naming its program, and every slide says which program you are in',()=>{
 const opens=slides().filter(s=>/\bg-orient\b/.test(s.cls)).map(title);
 expect(opens).toEqual([`Now working in: ${GMAIL}`,`Still working in: ${GMAIL}`,'Now working in: Microsoft Word','Now working in: Microsoft Edge']);
 for(const s of slides().filter(s=>/\bg-(step|map|orient|tell|watch|check)\b/.test(s.cls)))
  expect(text(/<div class="hud">([\s\S]*?)<\/div>/.exec(s.html)[1]),title(s)).toMatch(/Working in: (Gmail \(in Microsoft Edge\)|Microsoft (Word|Edge)|File Explorer)/);
});

test('Every step slide gives one or two actions and what you should see',()=>{
 const all=steps();expect(all.length).toBeGreaterThanOrEqual(30);
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
 // The wrap-up shows the instructor check first and the tidy-up step after it, in the deck and on the worksheet alike.
 expect(wsSteps).toEqual(steps().map(title));
 const t=text(ws);
 expect(t).toContain('Week 4 · Worksheet');
 for(const [i,app] of ['GMAIL (IN MICROSOFT EDGE)','GMAIL (IN MICROSOFT EDGE)','MICROSOFT WORD','MICROSOFT EDGE'].entries())expect(t).toContain(`PART ${i+1} OF 4 · ${app}`);
 expect(t).toContain('BEFORE WE START');expect(t).not.toMatch(/practice library exercise/i);
 expect(ws).toContain('href="/courses/digital-literacy-2/activities/free-trial-offer.html" target="_blank" rel="noopener"');
 // The four facts are written on the worksheet, in a box that survives printing.
 expect(ws).toMatch(/<textarea class="worksheet-input" id="predict-[^"]+" rows="4"><\/textarea><span class="print-answer"><\/span>/);
});

test('Only tonight’s skills are taught: no cut topics on slides or worksheet, and no break',()=>{
 for(const cut of [/Join a meeting/i,/raise[- ]hand/i,/webinar/i,/Reply all/i,/community page/i,/choose a channel/i,/Take an 8-minute break/i])
  expect(learnerText()).not.toMatch(cut);
 expect(text(read(`${dir}/lesson-plan.html`))).not.toMatch(/Protected break/i);
});

test('Nothing can be sent: every address ends in example.com and no step tells learners to click Send',()=>{
 const everything=learnerText()+' '+text(read(`${dir}/answer-key.html`))+' '+text(read(`${dir}/lesson-plan.html`));
 const addresses=[...everything.matchAll(/[\w.+-]+@[\w.-]+\.\w+/g)].map(m=>m[0]);
 expect(addresses.length).toBeGreaterThan(0);
 for(const a of addresses)expect(a,a).toMatch(/@example\.com$/);
 for(const s of steps())for(const [,li] of s.shown.matchAll(/<li>([\s\S]*?)<\/li>/g))
  if(/\bSend\b/.test(text(li)))expect(text(li),title(s)).toMatch(/\bDo not click\b/i);
 expect(text(read(`${dir}/worksheet.html`))).toMatch(/never click Send/i);
 expect(deck()).toContain('Do not click');
});

test('The practice offer page is safe and states the same four facts as the slides and worksheet',()=>{
 const page=read('courses/digital-literacy-2/activities/free-trial-offer.html');
 const t=text(page);
 for(const fact of ['Free for 7 days','$12 each month','Your first charge is on day 8.','every month until you cancel','Account › Billing › Cancel plan'])expect(t).toContain(fact);
 expect(page).toContain('<meta name="robots" content="noindex">');
 expect(page).toContain('/shared/text-size.js');
 expect(page).not.toMatch(/<form|fetch\(|XMLHttpRequest|https?:\/\//);
 const shown=text(slides().map(s=>s.shown).join(' '));
 for(const fact of ['Free for 7 days','$12 each month','Your first charge is on day 8','Account › Billing › Cancel plan'])expect(shown).toContain(fact);
 expect(fs.existsSync('courses/digital-literacy-2/activities/free-trial-offer.html')).toBe(true);
});

test('Video clips stay on the taught sentences: they begin and end on caption cues and skip every cut topic',()=>{
 const sec=x=>x.split(':').reduce((t,v)=>t*60+Number(v),0);
 const cues=read('courses/digital-literacy-2/media/week-04.vtt').split(/\n\s*\n/).map(b=>{const m=/([\d:.]+) --> ([\d:.]+)/.exec(b);return m&&{a:sec(m[1]),b:sec(m[2]),t:b.split('\n').slice(1).join(' ')};}).filter(Boolean);
 const clips=[...deck().matchAll(/<source src="[^"]*#t=([\d.]+),([\d.]+)"/g)].map(m=>[Number(m[1]),Number(m[2])]);
 expect(clips).toHaveLength(5);
 for(const [start,end] of clips){
  expect(cues.some(c=>Math.abs(c.a-start)<=.35),`clip ${start} starts on a cue`).toBe(true);
  expect(cues.some(c=>Math.abs(c.b-end)<=.35),`clip ${end} ends on a cue`).toBe(true);
  const spoken=cues.filter(c=>c.b>start+.2&&c.a<end-.2).map(c=>c.t).join(' ');
  expect(spoken,`${start}-${end}`).not.toMatch(/meeting|webinar|community|Reply all|speaker and microphone|captions are available/i);
 }
});

test('Each part ends with check questions that have three choices and a valid answer',()=>{
 const checks=slides().filter(s=>/\bg-check\b/.test(s.cls));
 expect(checks).toHaveLength(5);
 for(const s of checks){
  const answer=Number(/data-answer="(\d)"/.exec(s.shown)[1]);
  const choices=[...s.shown.matchAll(/data-choice="\d"/g)];
  expect(choices,title(s)).toHaveLength(3);expect(answer).toBeLessThan(3);
 }
 expect(steps().map(title)).toContain('Delete your practice draft');
});

test('The 120-minute plan adds up and names every part',()=>{
 const plan=read(`${dir}/lesson-plan.html`);
 const rows=[...plan.matchAll(/<tr><td>(\d+)–(\d+) \((\d+) min\)<\/td><td>[^<]*<\/td><td>([^<]*)<\/td><\/tr>/g)];
 expect(rows.reduce((t,r)=>t+Number(r[3]),0)).toBe(120);
 expect(Number(rows.at(-1)[2])).toBe(120);
 for(const p of ['Part 1 · Gmail (in Microsoft Edge)','Part 2 · Gmail (in Microsoft Edge)','Part 3 · Microsoft Word','Part 4 · Microsoft Edge'])expect(rows.map(r=>r[4]).join('|')).toContain(p);
 expect(rows.length).toBeGreaterThanOrEqual(6);
 expect(plan).toContain('<meta name="robots" content="noindex">');
});

test('Learner pages link only learner pages',()=>{
 for(const page of ['presentation','worksheet']){
  const hrefs=[...read(`${dir}/${page}.html`).matchAll(/href="([^"]*)"/g)].map(m=>m[1]);
  expect(hrefs.filter(h=>/answer-key|lesson-plan|instructor/.test(h)),page).toEqual([]);
 }
});
