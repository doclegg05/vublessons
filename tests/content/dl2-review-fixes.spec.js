// Content-level regressions from the 2026-09-24 DL2 curriculum review.
// Each test names the generator change that makes it pass; see scripts/dl2/.
const {test,expect}=require('@playwright/test');const fs=require('fs');
const read=p=>fs.readFileSync(p,'utf8');
const curriculum=JSON.parse(read('scripts/dl2/curriculum.json'));
const course='courses/digital-literacy-2';
const deck=n=>read(`${course}/weeks/week-0${n}/presentation.html`);
const worksheet=n=>read(`${course}/weeks/week-0${n}/worksheet.html`);
const answerKey=n=>read(`${course}/weeks/week-0${n}/answer-key.html`);
// Python html.escape(quote=True) escaping, so curriculum text can be matched in rendered HTML.
const esc=s=>s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#x27;');
// Deck slide k is w.slides[k-2]: slide 1 is the objectives slide the generator prepends.
function section(html,slideNumber){const m=html.match(new RegExp(`<section[^>]*id="slide-${slideNumber}"[^>]*>([\\s\\S]*?)</section>`));if(!m)throw new Error(`slide-${slideNumber} not found`);return m[1];}
const withoutDetails=html=>html.replace(/<details[\s\S]*?<\/details>/g,'');

// Narrowed 2026-09-28 (Mission Control, Task 11): weeks 2–6 only. Week 1's generated deck was replaced by the
// 27-slide Mission Control deck, which is not built from curriculum.json (tests/functional/dl2-os-week1-deck.spec.js).
test('DL2 teaching text is visible on every slide, not only inside a collapsed note',()=>{
 for(const w of curriculum.weeks.filter(w=>w.n!==1)){const html=deck(w.n);
  w.slides.forEach((s,i)=>{const visible=withoutDetails(section(html,i+2));expect(visible,`week ${w.n} slide ${i+2} "${s.title}"`).toContain(esc(s.body));});}
});

// Retired 2026-09-26 with the week 6 redesign: 'DL2 week 6 v2 acceptance check searches for the resource
// the learner renamed'. The rename is gone; slide 10 is now the agent's diff (tests/content/dl2-week6-agent.spec.js).

test('DL2 week 6 worksheet teaches the hand-repair mechanics for version 2',()=>{
 const ws=worksheet(6);
 expect(ws).toContain('download="resource-finder-v1.html"');
 expect(ws).toContain('download="resource-finder-v2.html"');
 expect(ws).toMatch(/Notepad/);
 expect(ws).toMatch(/TextEdit/);
 expect(ws).toMatch(/All files/i);
 expect(ws).toMatch(/Save As/i);
 expect(ws).toMatch(/toLowerCase/);
 expect(ws).toMatch(/\.html/);
 expect(ws).not.toMatch(/Make Plain Text/);
});

test('DL2 week 5 skills challenge gives every task its inputs, a response box and a rating',()=>{
 const w5=curriculum.weeks[4];
 expect(w5.challenge.item).toBe(6);
 expect(w5.challenge.tasks).toHaveLength(5);
 for(const t of w5.challenge.tasks){expect(t).toHaveLength(3);for(const part of t)expect(typeof part==='string'&&part.length>10,JSON.stringify(t)).toBe(true);}
 const ws=worksheet(5);
 for(const [task,materials] of w5.challenge.tasks){expect(ws).toContain(esc(task));expect(ws).toContain(esc(materials));}
 expect(ws.match(/id="challenge-answer-\d"/g)).toHaveLength(5);
 for(let i=0;i<5;i++){const radios=ws.match(new RegExp(`name="challenge-rating-${i}"`,'g'));expect(radios,`task ${i+1} rating radios`).toHaveLength(3);}
 for(const label of ['Independent','With prompt','Needs practice'])expect(ws).toContain(label);
 const key=answerKey(5);
 for(const [task,,evidence] of w5.challenge.tasks){expect(key).toContain(esc(task));expect(key).toContain(esc(evidence));}
});
