// Week 5 guided build (2026-10-23). Same definition of done as Weeks 3 and 4: a learner can go slide by slide and finish every
// task; anything critical left out is a failure. Source: scripts/dl2/mission-control/week5.py and guided.py.
const {test,expect}=require('@playwright/test');const fs=require('fs');
const read=p=>fs.readFileSync(p,'utf8');
const dir='courses/digital-literacy-2/weeks/week-05';
const act='courses/digital-literacy-2/activities';
const text=html=>html.replace(/<[^>]+>/g,' ').replace(/&amp;/g,'&').replace(/&#x27;/g,"'").replace(/&quot;/g,'"').replace(/&lt;/g,'<').replace(/&gt;/g,'>').replace(/\s+/g,' ').trim();
const deck=()=>read(`${dir}/presentation.html`);
const slides=()=>[...deck().matchAll(/<section class="slide([^"]*)"[^>]*>([\s\S]*?)<\/section>/g)].map(m=>({cls:m[1],html:m[2],shown:m[2].replace(/<aside class="notes">[\s\S]*?<\/aside>/,'')}));
const steps=()=>slides().filter(s=>/\bg-step\b/.test(s.cls));
const title=s=>text(/<h1[^>]*>([\s\S]*?)<\/h1>/.exec(s.html)[1]);
const learnerText=()=>text(slides().map(s=>s.shown).join(' '))+' '+text(read(`${dir}/worksheet.html`));
const PASSPHRASE='kettle orbit meadow quilt';
const MAIL5='/courses/digital-literacy-2/activities/practice-mail.html?inbox=week-5#inbox=week-5';
const SIGNUP='/courses/digital-literacy-2/activities/practice-signup.html';

test('Week 5 shows its three goals up front, each with its program, and they match the three Week 5 post-test items',()=>{
 const goals=slides().find(s=>/Tonight.s goals/.test(title(s)));
 expect(goals,'a goals slide').toBeTruthy();
 const rows=[...goals.shown.matchAll(/<li>([\s\S]*?)<\/li>/g)].map(m=>text(m[1]));
 expect(rows).toHaveLength(3);
 ['Part 1 · Excel','Part 2 · Edge','Part 3 · Practice Mail'].forEach((label,i)=>expect(rows[i]).toContain(label));
 const items=read('courses/digital-literacy-2/os/items.js');
 const map=/var W = \{([^}]*)\}/.exec(items)[1];
 const week5=[...map.matchAll(/(\d+): 5\b/g)].map(m=>Number(m[1]));
 expect(week5).toEqual([18,19,20]);
 const plan=text(read(`${dir}/lesson-plan.html`));
 for(const n of week5)expect(plan).toContain(`post-test item ${n}`);
});

test('Each part opens with a slide naming its program, and every slide says which program you are in',()=>{
 const opens=slides().filter(s=>/\bg-orient\b/.test(s.cls)).map(title);
 expect(opens).toEqual(['Now working in: Microsoft Excel','Now working in: Microsoft Edge','Now working in: Practice Mail']);
 for(const s of slides().filter(s=>/\bg-(step|map|orient|tell|watch|check)\b/.test(s.cls)))
  expect(text(/<div class="hud">([\s\S]*?)<\/div>/.exec(s.html)[1]),title(s)).toMatch(/Working in: (Practice Mail|Microsoft (Excel|Edge)|File Explorer)/);
});

test('Every step slide gives one or two actions and what you should see',()=>{
 const all=steps();expect(all.length).toBeGreaterThanOrEqual(45);
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
 expect(t).toContain('Week 5 · Worksheet');
 for(const [i,app] of ['MICROSOFT EXCEL','MICROSOFT EDGE','PRACTICE MAIL'].entries())expect(t).toContain(`PART ${i+1} OF 3 · ${app}`);
 expect(t).toContain('BEFORE WE START');expect(t).not.toMatch(/practice library exercise/i);
 expect(ws).toContain(`href="${SIGNUP}" target="_blank" rel="noopener"`);
 expect(ws).toContain(`href="${MAIL5}" target="_blank" rel="noopener"`);
 // The safer route is written on the worksheet, in a box that survives printing.
 expect(ws).toMatch(/<textarea class="worksheet-input" id="predict-[^"]+" rows="3"><\/textarea><span class="print-answer"><\/span>/);
 // The letter you already have is printed on the worksheet, with the trusted number.
 expect(t).toContain('A letter you already have');expect(t).toContain('304-555-0188');
 // The practice passphrase is on the worksheet and says it is for practice only.
 expect(t).toContain(PASSPHRASE);expect(t).toMatch(/For this practice page only\. Never use it for a real account/);
});

test('Only tonight’s skills are taught: no cut topics on slides or worksheet, no break, no skills challenge, no post-test slide',()=>{
 for(const cut of [/camera/i,/microphone/i,/encrypt/i,/read-only/i,/\bUSB\b/,/catfish/i,/harmful post/i,/skills challenge/i,/five-task/i,/capstone/i,/Take an 8-minute break/i,/Navigation Pane/i])
  expect(learnerText()).not.toMatch(cut);
 const lessonPlan=text(read(`${dir}/lesson-plan.html`));
 expect(lessonPlan).not.toMatch(/Protected break|Individual post-test/i);
 expect(deck()).not.toMatch(/assessments\/post-test/);
 for(const s of slides())expect(title(s),'no post-test slide').not.toMatch(/post-test|Show your progress/i);
 // The test scenarios are not copied into the lesson.
 for(const scenario of [/red and green dots/i,/on time.{1,10}late/i,/Social Security/i,/unlock it now/i,/Tiger7/])expect(learnerText()).not.toMatch(scenario);
});

test('Meaning without color: the sheet, the words and the chart question are all in the lesson',()=>{
 const t=learnerText();
 for(const word of ['Fill Color','Complete','Not yet','labels','patterns','Excel Workbook'])expect(t+deck()).toContain(word);
 const chart=slides().filter(s=>/\bg-check\b/.test(s.cls)).map(s=>text(s.shown)).find(x=>/chart/i.test(x));
 expect(chart,'a check question about a chart').toBeTruthy();
 expect(steps().map(title)).toEqual(expect.arrayContaining(['Choose green','Choose red','Add the words','Read the sheet without color','Save the file']));
});

test('Practice sign-up page: example.com only, a short password is refused, no network and nothing is stored',()=>{
 const page=read(`${act}/practice-signup.html`);
 expect(page).toContain('<meta name="robots" content="noindex">');
 expect(page).toContain('/shared/text-size.js');
 expect(page).not.toMatch(/<form|fetch\(|XMLHttpRequest|navigator\.sendBeacon|WebSocket|localStorage|sessionStorage|document\.cookie|https?:\/\/|location\.(search|hash)/);
 expect(page).toMatch(/@example\\\.com/);
 expect(page).toContain('[hidden]{display:none!important}');
 expect(page).toContain('482913');
 const everything=learnerText()+' '+text(page);
 for(const a of [...everything.matchAll(/[\w.+-]+@[\w.-]+\.\w+/g)].map(m=>m[0]))expect(a,a).toMatch(/@example\.com$/);
});

test('Practice sign-up works end to end in the browser and keeps nothing',async({page})=>{
 const requests=[];page.on('request',r=>{if(!/^(data|blob):/.test(r.url()))requests.push(new URL(r.url()).pathname);});
 await page.goto(SIGNUP);
 await page.locator('#email').fill('learner@example.com');await page.locator('#pw').fill('Maple9');
 await page.getByRole('button',{name:'Create account'}).click();
 await expect(page.locator('#msg-account')).toContainText('too short');
 await expect(page.locator('#s-step')).toBeHidden();
 await page.locator('#pw').fill(PASSPHRASE);await page.getByRole('button',{name:'Create account'}).click();
 await expect(page.locator('#keep')).toContainText('this one site only');
 await expect(page.locator('#pw')).toHaveValue('');
 await page.getByRole('button',{name:'Text me a code'}).click();
 await expect(page.locator('.phone')).toContainText('482913');
 await page.locator('#code').fill('111111');await page.getByRole('button',{name:'Verify'}).click();
 await expect(page.locator('#msg-code')).toContainText('does not match');
 await page.locator('#code').fill('482913');await page.getByRole('button',{name:'Verify'}).click();
 await expect(page.locator('#s-done')).toContainText('Two-step verification is on');
 expect(await page.evaluate(()=>[localStorage.length,sessionStorage.length,document.cookie,location.href.includes('Maple')||location.href.includes('kettle')])).toEqual([0,0,'',false]);
 expect(requests.filter(p=>!/^(\/courses\/digital-literacy-2\/activities\/practice-signup(\.html)?|\/shared\/text-size\.js|\/favicon\.ico)$/.test(p))).toEqual([]);
 await page.goto(SIGNUP);await page.locator('#email').fill('someone@gmail.com');await page.getByRole('button',{name:'Create account'}).click();
 await expect(page.locator('#msg-account')).toContainText('@example.com');
});

test('Practice Mail has a Week 5 inbox behind a URL parameter and still behaves as before without it',async({page})=>{
 const html=read(`${act}/practice-mail.html`);
 expect(html).not.toMatch(/<form|fetch\(|XMLHttpRequest|navigator\.sendBeacon|WebSocket|https?:\/\//);
 const requests=[];page.on('request',r=>{if(!/^(data|blob):/.test(r.url()))requests.push(new URL(r.url()).pathname);});
 await page.goto('/courses/digital-literacy-2/activities/practice-mail.html');
 await expect(page.locator('.list li')).toHaveCount(3);await expect(page.locator('.list')).toContainText('Your Week 4 worksheet');
 await page.goto('/courses/digital-literacy-2/activities/practice-mail?inbox=week-5');
 await expect(page.locator('.list li')).toHaveCount(1);
 await page.goto('/courses/digital-literacy-2/activities/practice-mail#inbox=week-5');
 await expect(page.locator('.list li')).toHaveCount(1);
 await page.goto(MAIL5);
 await expect(page.locator('.list li')).toHaveCount(1);
 await page.locator('.list button').click();
 const link=page.locator('.bad-link');
 await expect(link).toHaveText('maplevalleyhealth.org/confirm');
 expect(await link.getAttribute('href')).toContain('maple-valley-confirm.example.net/login');
 await link.hover();await expect(page.locator('.where')).toContainText('maple-valley-confirm.example.net/login');
 const before=page.url();await link.click();
 expect(page.url()).toBe(before);await expect(page.locator('#status')).toContainText('did not open');
 await expect(page.locator('.msg')).toContainText('304-555-0199');
 await expect(page.locator('.msg')).toContainText('act now');
 await page.getByRole('button',{name:'Report this message'}).click();
 await expect(page.getByRole('button',{name:'Reported'})).toBeDisabled();await expect(page.locator('#status')).toContainText('Reported in practice');
 expect(requests.filter(p=>!/^(\/courses\/digital-literacy-2\/activities\/practice-mail(\.html)?|\/shared\/text-size\.js|\/favicon\.ico)$/.test(p))).toEqual([]);
});

test('The Week 5 message has pressure words, a lookalike link and a number that differs from the letter',()=>{
 const html=read(`${act}/practice-mail.html`);
 for(const s of ['stops today','act now','within 1 hour','maplevalleyhealth.org/confirm','maple-valley-confirm.example.net/login','304-555-0199'])expect(html).toContain(s);
 const t=learnerText();
 for(const s of ['stops today','act now','within 1 hour','maple-valley-confirm.example.net/login','304-555-0199','304-555-0188','bottom left'])expect(t,s).toContain(s);
 const everything=t+' '+text(html);
 for(const a of [...everything.matchAll(/[\w.+-]+@[\w.-]+\.\w+/g)].map(m=>m[0]))expect(a,a).toMatch(/@example\.com$/);
 const checks=slides().filter(s=>/\bg-check\b/.test(s.cls)).map(s=>text(s.shown)).join(' ');
 expect(checks).toMatch(/email/i);expect(checks).toMatch(/caller/i);
});

test('Learner pages use plain words: no jargon, and the new words are defined',()=>{
 for(const [name,body] of [['slides',text(slides().map(s=>s.shown).join(' '))],['worksheet',text(read(`${dir}/worksheet.html`))]])
  for(const jargon of [/\bMFA\b/,/multifactor/i,/\bphishing\b/i,/\bspoof/i,/credentials?/i,/\bribbon\b/i,/\brecipients?\b/i])
   expect(body,`${name}: ${jargon}`).not.toMatch(jargon);
 const ws=text(read(`${dir}/worksheet.html`));
 for(const term of ['Cell','Fill Color','Passphrase','Two-step verification','Pressure words','Link','Trusted route','Report'])expect(ws,term).toContain(term+' ');
});

test('The Week 5 practice library keeps its slide numbers',()=>{
 const lib=read(`${dir}/practice.html`);
 expect(lib).toContain('id="slide-8"');
});

test('Nothing labels the learners: no skill-level wording on any Week 5 page',()=>{
 for(const f of ['presentation','worksheet','answer-key','lesson-plan','run-sheet','instructor-notes'])
  expect(text(read(`${dir}/${f}.html`)),f).not.toMatch(/\b(beginners?|non-?technical|not technical|novices?|first-time users?|low-skill|struggling)\b/i);
 for(const f of ['practice-mail','practice-signup'])
  expect(text(read(`${act}/${f}.html`)),f).not.toMatch(/\b(beginners?|non-?technical|novices?)\b/i);
});

test('The worksheet ends in a My result page with a box for every piece of finished work, and never the passphrase',()=>{
 const ws=read(`${dir}/worksheet.html`);
 expect(ws).toContain('id="result"');
 const fields=[...ws.matchAll(/<label class="g-write-label" for="result-(\d+)">([\s\S]*?)<\/label><textarea class="worksheet-input" id="result-\1"/g)].map(m=>text(m[2]));
 expect(fields).toHaveLength(7);
 for(const f of ['words I added','rule for a password','Two-step verification','pressure words','link','trusted route','One habit'])expect(fields.join('|').toLowerCase()).toContain(f.toLowerCase());
 expect(ws.indexOf('id="result"')).toBeGreaterThan(ws.indexOf('id="wrap"'));
 const result=text(ws.slice(ws.indexOf('id="result"')));
 expect(result).toMatch(/Do not write your passphrase here/);
 expect(result.replace(/Do not write your passphrase here/,'')).not.toContain(PASSPHRASE);
 expect(text(ws)).toContain('Words we use tonight');
 expect(steps().map(title)).toContain('Fill in your result page');
});

test('Video clips stay on the taught sentences: they begin and end on caption cues and skip every cut topic',()=>{
 const sec=x=>x.split(':').reduce((t,v)=>t*60+Number(v),0);
 const cues=read('courses/digital-literacy-2/media/week-05.vtt').split(/\n\s*\n/).map(b=>{const m=/([\d:.]+) --> ([\d:.]+)/.exec(b);return m&&{a:sec(m[1]),b:sec(m[2]),t:b.split('\n').slice(1).join(' ')};}).filter(Boolean);
 const clips=[...deck().matchAll(/<source src="[^"]*#t=([\d.]+),([\d.]+)"/g)].map(m=>[Number(m[1]),Number(m[2])]);
 expect(clips).toHaveLength(3);
 for(const [start,end] of clips){
  expect(cues.some(c=>Math.abs(c.a-start)<=.35),`clip ${start} starts on a cue`).toBe(true);
  expect(cues.some(c=>Math.abs(c.b-end)<=.35),`clip ${end} ends on a cue`).toBe(true);
  const spoken=cues.filter(c=>c.b>start+.2&&c.a<end-.2).map(c=>c.t).join(' ');
  expect(spoken,`${start}-${end}`).not.toMatch(/Pause and|read-only|encryption|USB|camera|permission|catfishing|post-test/i);
 }
 // The passwords part has no clip: the video does not cover passwords.
 const part2=slides().filter(s=>/Part 2 · /.test(text(/<span class="g-kicker">([\s\S]*?)<\/span>/.exec(s.html)?.[1]||'')));
 expect(part2.filter(s=>/\bg-watch\b/.test(s.cls))).toEqual([]);
});

test('Each part ends with check questions that have three choices and a valid answer',()=>{
 const checks=slides().filter(s=>/\bg-check\b/.test(s.cls));
 expect(checks).toHaveLength(5);
 for(const s of checks){
  const answer=Number(/data-answer="(\d)"/.exec(s.shown)[1]);
  const choices=[...s.shown.matchAll(/data-choice="\d"/g)];
  expect(choices,title(s)).toHaveLength(3);expect(answer).toBeLessThan(3);
 }
});

test('The 120-minute plan adds up and names every part',()=>{
 const plan=read(`${dir}/lesson-plan.html`);
 const rows=[...plan.matchAll(/<tr><td>(\d+)–(\d+) \((\d+) min\)<\/td><td>[^<]*<\/td><td>([^<]*)<\/td><\/tr>/g)];
 expect(rows.reduce((t,r)=>t+Number(r[3]),0)).toBe(120);
 expect(Number(rows.at(-1)[2])).toBe(120);
 for(const p of ['Part 1 · Microsoft Excel','Part 2 · Microsoft Edge','Part 3 · Practice Mail'])expect(rows.map(r=>r[4]).join('|')).toContain(p);
 expect(rows.length).toBeGreaterThanOrEqual(6);
 expect(plan).toContain('<meta name="robots" content="noindex">');
});

test('Learner pages link only learner pages',()=>{
 for(const page of ['presentation','worksheet']){
  const hrefs=[...read(`${dir}/${page}.html`).matchAll(/href="([^"]*)"/g)].map(m=>m[1]);
  expect(hrefs.filter(h=>/answer-key|lesson-plan|instructor/.test(h)),page).toEqual([]);
 }
});
