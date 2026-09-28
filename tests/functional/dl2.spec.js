const {test,expect}=require('@playwright/test');
const AxeBuilder=require('@axe-core/playwright').default;
const fs=require('fs');
const base='/courses/digital-literacy-2';
// Narrowed 2026-09-28 (Mission Control, Task 11): weeks 2–6. Week 1's replaced deck is covered by
// tests/functional/dl2-os-week1-deck.spec.js and dl2-os-deck.spec.js.
for(let week=2;week<=6;week++)test(`DL2 week ${week}: all slides, navigation, resources and reload`,async({page})=>{
 const errors=[];page.on('pageerror',e=>errors.push(e.message));await page.goto(`${base}/weeks/week-${String(week).padStart(2,'0')}/presentation.html`);
 const slides=page.locator('.slide'),nav=page.locator('[data-slide]');const count=await slides.count();expect(count).toBeGreaterThan(18);
 for(let i=0;i<count;i++){await nav.nth(i).click();await expect(slides.nth(i)).toBeVisible();await expect(page.locator('#slide-counter')).toHaveText(`Slide ${i+1} of ${count}`);}
 await expect(page.locator('#next')).toBeDisabled();await page.reload();await expect(slides.last()).toBeVisible();await page.locator('#restart').click();await expect(slides.first()).toBeVisible();await expect(page.locator('#previous')).toBeDisabled();
 await slides.first().locator('h2').focus();await page.keyboard.press('ArrowRight');await expect(slides.nth(1)).toBeVisible();await page.keyboard.press('End');await expect(slides.last()).toBeVisible();await page.keyboard.press('Home');await expect(slides.first()).toBeVisible();
 for(const a of await page.locator('.resources a').all()){expect((await page.request.get(await a.getAttribute('href'))).ok()).toBeTruthy();}expect(errors).toEqual([]);
});
test('DL2 interactions use keyboard, score checks, and preserve input keys',async({page})=>{
 await page.goto(`${base}/weeks/week-02/presentation.html`);await page.getByRole('button',{name:/Compare two results/}).click();const flip=page.locator('.slide:not([hidden]) .flip').first();await flip.focus();await page.keyboard.press('Space');await expect(flip).toHaveAttribute('aria-expanded','true');await page.keyboard.press('Enter');await expect(flip).toHaveAttribute('aria-expanded','false');
 await page.getByRole('button',{name:/Choose who can change/}).click();await page.getByLabel('Alex needs').selectOption('commenter');await expect(page.locator('#permission-result')).toContainText('You decide');
 await page.getByRole('button',{name:/Practice form: request/}).click();await page.getByLabel('Help topic').selectOption('Finding a file');await page.getByLabel('Practice contact method').selectOption('Ask at the desk');await page.getByRole('button',{name:'Review practice request'}).click();await expect(page.locator('#form-result')).toContainText('No request was sent');
 await page.getByRole('button',{name:/Knowledge check: read-only/}).click();await page.getByRole('button',{name:'The content is encrypted',exact:true}).click();await expect(page.locator('.slide:not([hidden]) .feedback')).toContainText('Try again');await page.getByRole('button',{name:'Editing is restricted',exact:true}).click();await expect(page.locator('.slide:not([hidden]) .feedback')).toContainText('Correct');
});
// Retired 2026-09-28 (Mission Control, Task 11), all targeting the replaced 28-question assessments (and, for the
// last, the replaced week 1 deck's #next/#slide-counter):
//  - 'DL2 pre: validation, perfect score, refresh, download and clear' and the matching post case
//  - 'DL2 incorrect score and domain totals are calculated from choices'
//  - 'DL2 works with blocked storage and reduced motion'
// The new test and deck are covered by the dl2-os-* specs (blocked storage: dl2-os-storage.spec.js).
test('DL2 mobile menu, text enlargement and starter edge cases',async({page})=>{
 await page.setViewportSize({width:390,height:844});await page.goto(`${base}/weeks/week-06/presentation.html`);await page.getByRole('button',{name:'Show lesson navigation'}).click();await expect(page.locator('.sidebar')).toBeVisible();await page.getByRole('button',{name:/Start with a working reference/}).click();await expect(page.locator('.sidebar')).toBeHidden();expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBeTruthy();
 await page.goto(`${base}/activities/resource-finder.html`);await page.getByLabel('Search fictional').fill('LIBRARY');await expect(page.locator('#status')).toHaveText('1 fictional resource found.');await page.getByLabel('Category').selectOption('Community');await expect(page.locator('#status')).toContainText('No matching');await page.getByRole('button',{name:'Reset filters'}).click();await expect(page.locator('#status')).toHaveText('3 fictional resources found.');await page.getByLabel('Search fictional').fill('<script>');await expect(page.locator('#status')).toContainText('No matching');
});
for(const path of ['/index.html','/syllabus.html','/weeks/week-01/presentation.html','/weeks/week-02/worksheet.html','/assessments/pre-test.html','/activities/resource-finder.html','/activities/resource-finder-agent.html','/activities/resource-finder-agent-fixed.html','/weeks/week-06/worksheet.html'])test(`DL2 accessibility ${path}`,async({page})=>{await page.goto(base+path);await page.emulateMedia({reducedMotion:'reduce'});await page.evaluate(()=>document.fonts.ready);const results=await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21aa']).analyze();expect(results.violations.map(v=>({id:v.id,nodes:v.nodes.map(n=>n.target)}))).toEqual([]);});
// Narrowed 2026-09-28 (Mission Control, Task 11): weeks 2–6. The Mission Control week 1 deck has no video slide;
// the week 1 video is still checked on its transcript page (dl2-video-chapters.spec.js).
for(let week=2;week<=6;week++)test(`DL2 week ${week}: video plays, seeks, and loads captions`,async({page})=>{
 await page.goto(`${base}/weeks/week-${String(week).padStart(2,'0')}/presentation.html`);
 await page.locator('[data-slide]').filter({hasText:/Watch:/}).click();
 const video=page.locator('video');await video.evaluate(v=>{v.muted=true;v.load();});
 await expect.poll(()=>video.evaluate(v=>v.readyState)).toBeGreaterThanOrEqual(2);
 const media=JSON.parse(fs.readFileSync('courses/digital-literacy-2/media/manifest.json','utf8'));
 expect(await video.evaluate(v=>v.duration)).toBeCloseTo(media.videos[week-1].durationSeconds,1);
 await video.evaluate(v=>v.play());await expect.poll(()=>video.evaluate(v=>v.currentTime)).toBeGreaterThan(.2);
 await video.evaluate(v=>{v.pause();v.textTracks[0].mode='showing';v.currentTime=v.duration-3;});
 await expect.poll(()=>video.evaluate(v=>v.textTracks[0].cues?.length||0)).toBeGreaterThan(15);
 await expect.poll(()=>video.evaluate(v=>v.seeking)).toBe(false);expect(await video.evaluate(v=>v.error)).toBe(null);
 await page.locator('#next').click();expect(await video.evaluate(v=>v.paused)).toBe(true);
});
// Narrowed 2026-09-28 (Mission Control, Task 11): weeks 2–6, enlarging the text on the first of them (week 2) exactly
// as it was enlarged on week 1 before, so every remaining week is still checked at the enlarged size.
test('DL2 enlarged text remains readable and every mobile lesson fits',async({page})=>{
 await page.setViewportSize({width:390,height:844});
 for(let week=2;week<=6;week++){
  await page.goto(`${base}/weeks/week-${String(week).padStart(2,'0')}/presentation.html`);
  if(week===2)for(let n=0;n<3;n++)await page.getByRole('button',{name:'Increase text size'}).click();
  const slides=page.locator('.slide');
  for(let i=0;i<await slides.count();i++){
   if(i>0)await page.locator('#next').click();
   expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1)).toBe(true);
  }
  const font=await page.locator('.slide:not([hidden]) p').first().evaluate(e=>parseFloat(getComputedStyle(e).fontSize));expect(font).toBeGreaterThanOrEqual(44);
 }
});
// Retired 2026-09-28 (Mission Control, Task 11): 'DL2 assessment fetch failure gives a recovery message'. The new
// pre-test bundles its items in os/items.js, so there is no questions.json fetch to fail.
test('DL2 worksheet typed answers appear in print',async({page})=>{
 await page.goto(`${base}/weeks/week-03/worksheet.html`);await page.locator('.worksheet-input').first().fill('Practice answer for the classroom.');await page.emulateMedia({media:'print'});await expect(page.locator('.print-answer').first()).toHaveText('Practice answer for the classroom.');await expect(page.locator('.worksheet-input').first()).toBeHidden();
});
test('DL2 knowledge-check choices keep the classroom type floor at every text size',async({page})=>{
 await page.goto(`${base}/weeks/week-03/presentation.html`);await page.locator('[data-slide]').filter({hasText:/Knowledge check/}).first().click();const choice=page.locator('.slide:not([hidden]) .check-options button').first();
 for(const size of ['sm','','lg','xl','xxl']){await page.evaluate(s=>{s?document.documentElement.setAttribute('data-text-size',s):document.documentElement.removeAttribute('data-text-size')},size);expect(await choice.evaluate(e=>parseFloat(getComputedStyle(e).fontSize))).toBeGreaterThanOrEqual(size==='xxl'?44:32);}
 await page.emulateMedia({media:'print'});expect(await choice.evaluate(e=>parseFloat(getComputedStyle(e).fontSize))).toBeGreaterThanOrEqual(32);
});
