// Week 6 guided build (2026-10-23). Same definition of done as Weeks 3 and 4: the whole class goes slide by slide in Microsoft Edge and
// finishes every step together; nobody works alone until the post-test. Then a course review of weeks 1 to 5 and the post-test.
// Source: scripts/dl2/mission-control/week6.py, ui_week6.py and guided.py. Week 6 has no post-test item of its own.
const {test,expect}=require('@playwright/test');const fs=require('fs');
const read=p=>fs.readFileSync(p,'utf8');
const dir='courses/digital-literacy-2/weeks/week-06';
const text=html=>html.replace(/<[^>]+>/g,' ').replace(/&amp;/g,'&').replace(/&#x27;/g,"'").replace(/&quot;/g,'"').replace(/&lt;/g,'<').replace(/&gt;/g,'>').replace(/\s+/g,' ').trim();
const deck=()=>read(`${dir}/presentation.html`);
const slides=()=>[...deck().matchAll(/<section class="slide([^"]*)"[^>]*>([\s\S]*?)<\/section>/g)].map(m=>({cls:m[1],html:m[2],shown:m[2].replace(/<aside class="notes">[\s\S]*?<\/aside>/,'')}));
const steps=()=>slides().filter(s=>/\bg-step\b/.test(s.cls));
const title=s=>text(/<h1[^>]*>([\s\S]*?)<\/h1>/.exec(s.html)[1]);
const hud=s=>text(/<div class="hud">([\s\S]*?)<\/div>/.exec(s.html)[1]);
const learnerText=()=>text(slides().map(s=>s.shown).join(' '))+' '+text(read(`${dir}/worksheet.html`));
const items=require('../../courses/digital-literacy-2/os/items.js');
const PROGRAMS=/Working in: (Microsoft (Edge|Word|Excel|PowerPoint)|File Explorer|Practice Mail|Windows Settings|Outlook Calendar)/;
const reviewSlides=()=>{const all=slides();const a=all.findIndex(s=>title(s)==='Week 1: make the computer fit you.');const b=all.findIndex(s=>/Now working in/.test(title(s))&&all.indexOf(s)>a);return all.slice(a,b);};
const reviewChecks=()=>reviewSlides().filter(s=>/\bg-check\b/.test(s.cls));
const words=t=>t.toLowerCase().replace(/[^a-z0-9$ ]+/g,' ').split(/\s+/).filter(Boolean);
const grams=(t,n=4)=>{const w=words(t),out=new Set();for(let i=0;i+n<=w.length;i++)out.add(w.slice(i,i+n).join(' '));return out;};

test('Week 6 shows four goals up front, each in Edge, and none claims a post-test item',()=>{
 const goals=slides().find(s=>/Tonight.s goals/.test(title(s)));
 expect(goals,'a goals slide').toBeTruthy();
 const rows=[...goals.shown.matchAll(/<li>([\s\S]*?)<\/li>/g)].map(m=>text(m[1]));
 expect(rows).toHaveLength(4);
 ['Part 1 · Edge','Part 2 · Edge','Part 3 · Edge','Part 4 · Edge'].forEach((label,i)=>expect(rows[i]).toContain(label));
 const plan=text(read(`${dir}/lesson-plan.html`));
 expect(plan.match(/practice only, not on the post-test/g)).toHaveLength(4);
 expect(plan).not.toMatch(/post-test item \d/);
 expect(text(read(`${dir}/answer-key.html`))).toContain('practice only, not on the post-test');
});

test('Each part opens by naming Microsoft Edge, and every slide says which program you are in',()=>{
 const opens=slides().filter(s=>/\bg-orient\b/.test(s.cls)).map(title);
 expect(opens).toEqual(['Now working in: Microsoft Edge','Still working in: Microsoft Edge','Still working in: Microsoft Edge','Still working in: Microsoft Edge','Now working in: Microsoft Edge']);
 for(const s of slides().filter(s=>/\bg-(step|map|orient|tell|watch|check)\b/.test(s.cls)))expect(hud(s),title(s)).toMatch(PROGRAMS);
 // Everything in the four parts and the post-test happens in Edge.
 const all=slides(),first=all.findIndex(s=>/g-orient/.test(s.cls)),last=all.findIndex(s=>title(s)==='Show your instructor.');
 for(const s of all.slice(first,last))expect(hud(s),title(s)).toMatch(/Working in: Microsoft Edge/);
});

test('Every step slide gives one or two actions and what you should see',()=>{
 const all=steps();expect(all.length).toBeGreaterThanOrEqual(60);
 for(const s of all){
  const actions=[...s.shown.matchAll(/<ol class="g-actions">([\s\S]*?)<\/ol>/g)];
  expect(actions,title(s)).toHaveLength(1);
  const n=[...actions[0][1].matchAll(/<li>/g)].length;
  expect(n,title(s)).toBeGreaterThanOrEqual(1);expect(n,title(s)).toBeLessThanOrEqual(2);
  expect(text(s.shown),title(s)).toMatch(/You should see: \S/);
  expect(s.shown,title(s)).toMatch(/data-visual/);
 }
});

test('The worksheet repeats every step in the same order, each with You should see and a check box',()=>{
 const ws=read(`${dir}/worksheet.html`);
 const wsSteps=[...ws.matchAll(/<li><span class="n">\d+<\/span><div class="d"><b class="act">([\s\S]*?)\.<\/b>[\s\S]*?<span class="see">[\s\S]*?<\/span><\/div><label class="box"><input type="checkbox">/g)].map(m=>text(m[1]));
 expect(wsSteps).toEqual(steps().map(title));
 const t=text(ws);
 expect(t).toContain('Week 6 · Worksheet');
 for(const i of [1,2,3,4])expect(t).toContain(`PART ${i} OF 4 · MICROSOFT EDGE`);
 expect(t).toContain('BEFORE WE START');expect(t).toContain('COURSE REVIEW · WEEKS 1 TO 5');expect(t).toContain('POST-TEST · MICROSOFT EDGE');
 for(const f of ['resource-finder.html','resource-finder-agent.html','resource-finder-agent-fixed.html'])
  expect(ws).toContain(`href="/courses/digital-literacy-2/activities/${f}" target="_blank" rel="noopener"`);
 for(const label of ['Open version 1','Open version 2','Open version 3'])expect(ws).toContain(`>${label}</a>`);
 // Predictions and the bug report are typed in boxes that survive printing; the request box shows the lines to type as well.
 expect(ws.match(/<textarea class="worksheet-input" id="predict-[^"]+"[^>]*><\/textarea><span class="print-answer"><\/span>/g).length).toBeGreaterThanOrEqual(9);
 expect(ws).toMatch(/id="predict-type-the-request" rows="5"/);expect(ws).toMatch(/class="g-type-card">Please change only this file\./);
 for(const id of ['t1','t3','t4'])for(let i=0;i<4;i++)expect(ws,`${id}-${i}`).toContain(`id="${id}-${i}"`);
 expect(ws.match(/<th scope="row">(library|learning|zzz|LIBRARY)<\/th>/g)).toHaveLength(12);
});

test('Only tonight’s skills are taught: no cut topics on slides or worksheet, no break, no capstone',()=>{
 for(const cut of [/\bSaaS\b/,/software as a service/i,/\bHTML\b/,/\bCSS\b/,/JavaScript/i,/Notepad|TextEdit|text editor/i,/API key/i,/secret key/i,/\brubric\b/i,/where (the )?data lives/i,/editable/i,/Take an 8-minute break/i,/capstone/i,/\bwebsite or a web app\b/i])
  expect(learnerText()).not.toMatch(cut);
 const plan=text(read(`${dir}/lesson-plan.html`));
 expect(plan).not.toMatch(/Protected break/i);
 for(const f of ['presentation','worksheet','answer-key','lesson-plan','run-sheet','instructor-notes'])expect(text(read(`${dir}/${f}.html`)),f).not.toMatch(/8-point|extension rubric/i);
});

test('Nothing needs an AI account, and the practice pages stay safe',()=>{
 expect(text(read(`${dir}/worksheet.html`))).toMatch(/No AI account is needed/);
 for(const f of ['resource-finder','resource-finder-agent','resource-finder-agent-fixed']){
  const page=read(`courses/digital-literacy-2/activities/${f}.html`);
  expect(page,f).not.toMatch(/<form|fetch\(|XMLHttpRequest|navigator\.sendBeacon|WebSocket|localStorage|sessionStorage|document\.cookie|https?:\/\//);
  expect(page,f).toContain('/shared/text-size.js');
 }
});

test('The slides show the real lines the three pages differ in',()=>{
 const flat=t=>t.replace(/\s+/g,'');
 const shown=flat(text(slides().map(s=>s.shown).join(' ')));
 const lines=f=>read(`courses/digital-literacy-2/activities/${f}.html`).split('\n').map(l=>l.trim());
 const [v1,v2,v3]=['resource-finder','resource-finder-agent','resource-finder-agent-fixed'].map(lines);
 const has=(l,l2)=>l2.some(x=>x.includes(l));
 // The change you asked for, the change nobody asked for, and the repair.
 const asked=["(r.name+' '+r.description).toLowerCase().includes(query)","(r.name+' '+r.category+' '+r.description).toLowerCase().includes(query)"];
 const unasked=['const query=search.value.trim().toLowerCase();','const query=search.value.trim();'];
 const repair=['const query=search.value.trim();','const query=search.value.trim().toLowerCase();'];
 expect(has(asked[0],v1)&&has(asked[1],v2)&&!has(asked[1],v1)).toBe(true);
 expect(has(unasked[0],v1)&&has(unasked[1],v2)&&!has(unasked[1],v1)).toBe(true);
 expect(has(repair[0],v2)&&has(repair[1],v3)&&!has(repair[1],v2)).toBe(true);
 for(const l of [...asked,...unasked,...repair])expect(shown,l).toContain(flat(l));
});

test('Practice results on the slides match the three pages: library 1, learning 0/2/2, zzz none, LIBRARY 1/none/1',()=>{
 const all=steps();
 const find=t=>all.find(s=>title(s)===t);
 const see=s=>text(/<p class="g-see">([\s\S]*?)<\/p>/.exec(s.shown)[1]);
 const label=s=>/aria-label="([^"]*)"/.exec(s.shown.match(/<div class="ui [^"]*"[^>]*>/)[0])[1];
 // Part 1 appears first, then Part 3 (version 2), then Part 4 (version 3): the nth step with the same title.
 const nth=(t,n)=>all.filter(s=>title(s)===t)[n];
 const NONE='No matching resources. Try a different word or reset the filters.';
 expect(see(nth('Search for library',0))).toContain('Community library');
 expect(see(nth('Search for learning',0))).toContain(NONE);
 expect(see(nth('Search for zzz',0))).toContain(NONE);
 expect(see(nth('Search for LIBRARY',0))).toContain('Community library');
 expect(see(nth('Search for learning',1))).toMatch(/Community library.*Practice Workbook Workshop/);
 expect(see(nth('Search for LIBRARY',1))).toContain(NONE);
 expect(see(nth('Search for LIBRARY',2))).toContain('Community library');
 expect(see(nth('Search for learning',2))).toMatch(/Community library.*Practice Workbook Workshop/);
 // The drawings work out their results from the same rules, so they say the same thing.
 expect(label(nth('Search for LIBRARY',1))).toContain(NONE);
 expect(label(nth('Search for LIBRARY',2))).toContain('1 fictional resource found.');
 expect(find('Open version 2')).toBeTruthy();
});

test('The course review has a recap slide per week and 20 questions, one for each post-test item, in item order',()=>{
 const rs=reviewSlides();
 const recaps=rs.filter(s=>/\bg-tell\b/.test(s.cls)).map(title);
 expect(recaps).toHaveLength(5);
 recaps.forEach((t,i)=>expect(t).toMatch(new RegExp(`^Week ${i+1}: `)));
 const checks=reviewChecks();expect(checks).toHaveLength(20);
 const ans=read(`${dir}/answer-key.html`);
 const key=[...ans.matchAll(/<li value="(\d+)"><b>Week (\d) , post-test item (\d+) \(([^)]*)\)/g)];
 const keyText=text(ans);
 for(let n=1;n<=20;n++){
  const it=items.post[n-1];
  expect(keyText,`item ${n}`).toContain(`Week ${it.week}, post-test item ${n} (${it.skill})`);
 }
 void key;
 for(const s of checks){
  const answer=Number(/data-answer="(\d)"/.exec(s.shown)[1]);
  expect([...s.shown.matchAll(/data-choice="\d"/g)],title(s)).toHaveLength(3);expect(answer).toBeLessThan(3);
  expect(hud(s),title(s)).toMatch(PROGRAMS);
 }
 // The right answers do not all sit in one place.
 const spots=checks.map(s=>Number(/data-answer="(\d)"/.exec(s.shown)[1]));
 for(const k of [0,1,2])expect(spots.filter(x=>x===k).length,`answer ${k}`).toBeGreaterThanOrEqual(5);
 // Review slides are grouped by week, in order: recap, then that week's questions.
 const order=rs.map(s=>/\bg-tell\b/.test(s.cls)?'R':'q').join('');
 expect(order).toBe('Rqqqq'+'Rqqqq'+'Rqqqq'+'Rqqqqq'+'Rqqq');
 const t=text(read(`${dir}/worksheet.html`));
 expect(t).toContain('Course review');expect(t.match(/My answer:/g).length).toBeGreaterThanOrEqual(24);
});

test('Every review question is a new scenario: no four-word run in common with any pre-test or post-test stem or option',()=>{
 const bank=[...items.pre,...items.post].flatMap(it=>[it.stem,...it.options]);
 const bankGrams=new Set(bank.flatMap(t=>[...grams(t)]));
 const ws=read(`${dir}/worksheet.html`);
 const qs=[...ws.matchAll(/<div class="g-rq"><p><b>(\d+)\.<\/b> <span class="g-rapp">[^<]*<\/span> ([\s\S]*?)<\/p><p>([\s\S]*?)<\/p>/g)];
 expect(qs).toHaveLength(20);
 for(const [,n,stem,opts] of qs){
  const t=text(stem)+' '+text(opts).replace(/\b[A-C]\. /g,' ');
  const shared=[...grams(t)].filter(g=>bankGrams.has(g));
  expect(shared,`question ${n}`).toEqual([]);
 }
});

test('Every review question names its program, and the answer guide explains each answer',()=>{
 const ans=text(read(`${dir}/answer-key.html`));
 expect(ans).toContain('Course review answers');
 const ws=text(read(`${dir}/worksheet.html`));
 expect(ws.match(/(Windows Settings|Microsoft Word|Outlook Calendar|Microsoft Edge|Microsoft Excel|Microsoft PowerPoint|Practice Mail)\. /g).length).toBeGreaterThanOrEqual(20);
});

test('The post-test is the last segment: opened together, then everyone answers alone, then take it home and mission complete',()=>{
 const all=slides().map(title);
 const iReview=all.indexOf('Week 5: protect your work, show your skills.');
 const iOpen=all.findIndex((t,i)=>i>iReview&&/^Now working in: Microsoft Edge$/.test(t));
 expect(iOpen).toBeGreaterThan(iReview+3);
 expect(all.slice(iOpen)).toEqual(['Now working in: Microsoft Edge','Go to the course home','Open the post-test','Click the name box','Type your name','Start the post-test','Now you answer on your own.','When you finish.','Take it home.','Mission complete.']);
 const t=text(slides().map(s=>s.shown).join(' '));
 for(const phrase of ['No help with answers','raise your hand','Submit my test','Submit to instructor','Download graded PDF'])expect(t).toContain(phrase);
 // The words on the slides are the words the post-test pages use. The clip titled with the video's own chapter name (happy path) is Britt's wording.
 const home=read('courses/digital-literacy-2/index.html'),testJs=read('courses/digital-literacy-2/os/test.js');
 expect(home).toContain('href="/courses/digital-literacy-2/assessments/post-test.html">Take the post-test</a>');
 for(const w of ['Your full name','Review answers','Submit my test','Submit to instructor','Download graded PDF','Start the ','Post-Test'])expect(testJs,w).toContain(w);
 expect(read('courses/digital-literacy-2/assessments/post-test.html')).toContain('os/test.js');
 expect(text(read(`${dir}/worksheet.html`))).toMatch(/Answer every question on your own\./);
});

test('Nothing labels the learners: no skill-level wording on any Week 6 page',()=>{
 for(const f of ['presentation','worksheet','answer-key','lesson-plan','run-sheet','instructor-notes'])
  expect(text(read(`${dir}/${f}.html`)),f).not.toMatch(/\b(beginners?|non-?technical|not technical|novices?|first-time users?|low-skill|struggling)\b/i);
});

test('Learner pages use plain words',()=>{
 for(const [name,body] of [['slides',text(slides().map(s=>s.shown).join(' '))],['worksheet',text(read(`${dir}/worksheet.html`))]])
  for(const jargon of [/\bregressions?\b/i,/acceptance checks?/i,/\bdiff\b/i,/\bprompt engineering\b/i,/\bMFA\b/,/\bASAP\b/,/\bribbon\b/i])
   expect(body,`${name}: ${jargon}`).not.toMatch(jargon);
 const ws=text(read(`${dir}/worksheet.html`));
 for(const term of ['Tab','Address bar','Check','AI agent','Request','Version','Bug','Bug report','Retest','Focus ring'])expect(ws,term).toContain(term+' ');
});

test('The worksheet ends in My result with a box for each piece of finished work',()=>{
 const ws=read(`${dir}/worksheet.html`);
 expect(ws).toContain('id="result"');
 const fields=[...ws.matchAll(/<label class="g-write-label" for="result-(\d+)">([\s\S]*?)<\/label><textarea class="worksheet-input" id="result-\1"/g)].map(m=>text(m[2]));
 expect(fields).toHaveLength(4);
 for(const f of ['My test table','My bug report','My retest','One habit'])expect(fields.join('|')).toContain(f);
 expect(ws.indexOf('id="result"')).toBeGreaterThan(ws.indexOf('id="wrap"'));
 expect(ws.indexOf('id="review"')).toBeGreaterThan(ws.indexOf('id="result"'));
 expect(ws.indexOf('id="posttest"')).toBeGreaterThan(ws.indexOf('id="review"'));
 expect(text(ws)).toContain('Words we use tonight');
 expect(steps().map(title)).toContain('Fill in your result page');
});

test('Video clips stay on the taught sentences: they begin and end on caption cues and skip the cut lessons',()=>{
 const sec=x=>x.split(':').reduce((t,v)=>t*60+Number(v),0);
 const cues=read('courses/digital-literacy-2/media/week-06.vtt').split(/\n\s*\n/).map(b=>{const m=/([\d:.]+) --> ([\d:.]+)/.exec(b);return m&&{a:sec(m[1]),b:sec(m[2]),t:b.split('\n').slice(1).join(' ')};}).filter(Boolean);
 const clips=[...deck().matchAll(/<source src="[^"]*#t=([\d.]+),([\d.]+)"/g)].map(m=>[Number(m[1]),Number(m[2])]);
 expect(clips).toHaveLength(4);
 clips.forEach(([start,end],i)=>{
  expect(cues.some(c=>Math.abs(c.a-start)<=.35),`clip ${start} starts on a cue`).toBe(true);
  expect(cues.some(c=>Math.abs(c.b-end)<=.35),`clip ${end} ends on a cue`).toBe(true);
  const spoken=cues.filter(c=>c.b>start+.2&&c.a<end-.2).map(c=>c.t).join(' ');
  // Never past a "Pause and..." prompt, and none of the cut lessons. Clip 2 (Britt's range, 3:01 to 3:47) keeps the video's example sentence that says one local HTML page, and its one-line reminder not to put passwords in a prompt.
  expect(spoken,`${start}-${end}`).not.toMatch(/Pause and|software as a service|web app|CSS|JavaScript|Browser storage|plain-text editor|Hosting is a separate/i);
  if(i!==1)expect(spoken,`${start}-${end}`).not.toMatch(/API keys?|passwords|HTML/i);
 });
 expect(clips[0][0]).toBeLessThan(clips[1][0]);
});

test('Each part ends with check questions that have three choices and a valid answer',()=>{
 const partChecks=slides().filter(s=>/\bg-check\b/.test(s.cls)&&!/Course review|Review · Week/.test(text(s.shown)));
 expect(partChecks).toHaveLength(4);
 for(const s of partChecks){
  const answer=Number(/data-answer="(\d)"/.exec(s.shown)[1]);
  expect([...s.shown.matchAll(/data-choice="\d"/g)],title(s)).toHaveLength(3);expect(answer).toBeLessThan(3);
 }
});

test('Part 4 ends with one short why slide before its check, and says a sign-in picture is not security',()=>{
 const all=slides().map(title);
 const i=all.indexOf('A practice page is not a real service.');
 expect(i).toBeGreaterThan(0);
 expect(all[i+1]).toBe('The repaired page finds LIBRARY. What else do you test?');
 const s=slides()[i];expect(text(s.shown)).toMatch(/sign-ins?, private data or payments/);expect(text(s.shown)).toMatch(/not security/);
 expect(text(s.shown).length).toBeLessThan(600);
});

test('The 120-minute plan adds up, and the post-test is the last 20 minutes',()=>{
 const plan=read(`${dir}/lesson-plan.html`);
 const rows=[...plan.matchAll(/<tr><td>(\d+)–(\d+) \((\d+) min\)<\/td><td>[^<]*<\/td><td>([^<]*)<\/td><\/tr>/g)];
 expect(rows.reduce((t,r)=>t+Number(r[3]),0)).toBe(120);
 expect(Number(rows.at(-1)[2])).toBe(120);
 const names=rows.map(r=>r[4]);
 for(const p of ['Part 1 · Microsoft Edge','Part 2 · Microsoft Edge','Part 3 · Microsoft Edge','Part 4 · Microsoft Edge','Wrap-up','Course review','Post-test'])expect(names.join('|')).toContain(p);
 expect(rows.at(-1)[4]).toMatch(/^Post-test/);expect(Number(rows.at(-1)[3])).toBe(20);
 expect(Number(rows.find(r=>/^Wrap-up/.test(r[4]))[3])).toBe(12);
 expect(Number(rows.find(r=>/^Course review/.test(r[4]))[3])).toBe(20);
 expect(plan).toContain('<meta name="robots" content="noindex">');
});

test('The jump menu has a stop for the course review and the post-test',()=>{
 const labels=[...deck().matchAll(/<option value="\d+">([^<]*)<\/option>/g)].map(m=>m[1]);
 expect(labels.slice(-3)).toEqual(['Wrap-up','Course review','Post-test']);
 expect(labels).toHaveLength(9);
});

test('Learner pages link only learner pages',()=>{
 for(const page of ['presentation','worksheet']){
  const hrefs=[...read(`${dir}/${page}.html`).matchAll(/href="([^"]*)"/g)].map(m=>m[1]);
  expect(hrefs.filter(h=>/answer-key|lesson-plan|instructor/.test(h)),page).toEqual([]);
 }
});
