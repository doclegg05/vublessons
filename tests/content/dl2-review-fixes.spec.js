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

test('DL2 teaching text is visible on every slide, not only inside a collapsed note',()=>{
 for(const w of curriculum.weeks){const html=deck(w.n);
  w.slides.forEach((s,i)=>{const visible=withoutDetails(section(html,i+2));expect(visible,`week ${w.n} slide ${i+2} "${s.title}"`).toContain(esc(s.body));});}
});

test('DL2 week 6 v2 acceptance check searches for the resource the learner renamed',()=>{
 const w6=curriculum.weeks[5];const html=deck(6);
 expect(w6.lab[3]).toContain('Community Skills Desk');
 const slide10=section(html,10);
 expect(slide10).not.toContain('Check library still matches');
 expect(slide10).toMatch(/skills[^<]*Community Skills Desk/i);
});

test('DL2 week 6 worksheet teaches the build mechanics the answer key grades',()=>{
 const ws=worksheet(6);
 expect(ws).toContain('download="resource-finder-v1.html"');
 expect(ws).toMatch(/Notepad/);
 expect(ws).toMatch(/TextEdit/);
 expect(ws).toMatch(/All files/i);
 expect(ws).toMatch(/Save As/i);
 expect(ws).toMatch(/paste/i);
 expect(ws).toMatch(/\.html/);
});

test('DL2 week 5 skills challenge gives every task its inputs, a response box and a rating',()=>{
 const w5=curriculum.weeks[4];
 expect(w5.challenge.item).toBe(6);
 expect(w5.challenge.tasks).toHaveLength(7);
 for(const t of w5.challenge.tasks){expect(t).toHaveLength(3);for(const part of t)expect(typeof part==='string'&&part.length>10,JSON.stringify(t)).toBe(true);}
 const ws=worksheet(5);
 for(const [task,materials] of w5.challenge.tasks){expect(ws).toContain(esc(task));expect(ws).toContain(esc(materials));}
 expect(ws.match(/id="challenge-answer-\d"/g)).toHaveLength(7);
 for(let i=0;i<7;i++){const radios=ws.match(new RegExp(`name="challenge-rating-${i}"`,'g'));expect(radios,`task ${i+1} rating radios`).toHaveLength(3);}
 for(const label of ['Independent','With prompt','Needs practice'])expect(ws).toContain(label);
 const key=answerKey(5);
 for(const [task,,evidence] of w5.challenge.tasks){expect(key).toContain(esc(task));expect(key).toContain(esc(evidence));}
});
