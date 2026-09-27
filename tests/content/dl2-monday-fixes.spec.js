// Content-level regressions from the 2026-09-26 DL2 full review (fixes before the 2026-09-28 cohort).
// Generated pages come from scripts/dl2/build-pages.py and learning.py; regenerate before running.
const {test,expect}=require('@playwright/test');const fs=require('fs');
const read=p=>fs.readFileSync(p,'utf8');
const course='courses/digital-literacy-2';
const weeks=[1,2,3,4,5,6].map(n=>`weeks/week-0${n}`);
const learnerPages=['index.html','syllabus.html','sources.html','activities/resource-finder.html','activities/resource-finder-agent.html','activities/resource-finder-agent-fixed.html',
 'assessments/pre-test.html','assessments/post-test.html','assessments/pre-test-printable.html','assessments/post-test-printable.html',
 ...weeks.flatMap(w=>[`${w}/presentation.html`,`${w}/worksheet.html`,`${w}/video-transcript.html`])];
const instructorPages=['instructor-guide.html','assessments/pre-test-answer-key.html','assessments/post-test-answer-key.html',
 ...weeks.flatMap(w=>[`${w}/lesson-plan.html`,`${w}/answer-key.html`])];
const hrefs=html=>[...html.matchAll(/href="([^"]*)"/g)].map(m=>m[1]);

test('DL2 learner pages do not link answer keys, lesson plans or the instructor guide',()=>{
 for(const p of learnerPages){const bad=hrefs(read(`${course}/${p}`)).filter(h=>/answer-key|lesson-plan|instructor-guide/.test(h));
  expect(bad,`${p} links instructor material`).toEqual([]);}
});

test('DL2 instructor pages are kept out of search results',()=>{
 for(const p of instructorPages)expect(read(`${course}/${p}`),p).toContain('<meta name="robots" content="noindex">');
 for(const p of learnerPages.filter(p=>!p.startsWith('activities/')))expect(read(`${course}/${p}`),p).not.toContain('noindex');
});

test('DL2 instructor pages still reach each other',()=>{
 const guide=hrefs(read(`${course}/instructor-guide.html`));
 for(const k of ['pre','post'])expect(guide).toContain(`/courses/digital-literacy-2/assessments/${k}-test-answer-key.html`);
 for(const w of weeks){expect(guide).toContain(`/courses/digital-literacy-2/${w}/lesson-plan.html`);
  expect(hrefs(read(`${course}/${w}/lesson-plan.html`))).toContain(`/courses/digital-literacy-2/${w}/answer-key.html`);}
});

test('DL2 appears in the instructor area',()=>{
 expect(hrefs(read('instructors/index.html'))).toContain('/courses/digital-literacy-2/instructor-guide.html');
});

test('DL2 pre-test shows the learner name field without an extra click and promises no missing score field',()=>{
 const pre=read(`${course}/assessments/pre-test.html`);
 expect(pre).toMatch(/<details class="learner-details" open>/);
 expect(pre).not.toMatch(/saved score/i);
});
