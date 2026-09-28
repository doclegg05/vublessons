const { test, expect } = require('@playwright/test');
const { AxeBuilder } = require('@axe-core/playwright');
const base='/courses/digital-literacy-2';
for(let week=2;week<=6;week++) {
 const route=`${base}/weeks/week-0${week}`;
 test(`Week ${week}: matched missions, guided states, checks and resources`,async({page})=>{
  const errors=[];page.on('pageerror',e=>errors.push(e.message));
  await page.goto(route+'/presentation.html#1');
  await expect(page.locator('.slide')).toHaveCount(23);
  for(const stage of ['tell','show','do','review'])await expect(page.locator(`.slide[data-stage=${stage}]`)).toHaveCount(4);
  await expect(page.locator('.slide').filter({hasText:'Take an 8-minute break.'})).toHaveCount(1);
  await page.getByRole('button',{name:'Notes (N)'}).click();await expect(page.locator('.notes-panel')).toBeVisible();
  await page.keyboard.press('n');await expect(page.locator('.notes-panel')).toBeHidden();
  for(const index of [4,8,13,17]) {
   await page.evaluate(i=>DL2Deck.go(i,'forward'),index);
   const demo=page.locator('.slide.is-active [data-mission-demo]');
   await expect(demo.locator('.demo-count')).toHaveText('Step 1 of 3');
   await demo.getByRole('button',{name:'Next step'}).click();await expect(demo.locator('.demo-count')).toHaveText('Step 2 of 3');
   await page.keyboard.press('ArrowRight');await expect(demo.locator('.demo-count')).toHaveText('Step 3 of 3');
   await demo.getByRole('button',{name:'Replay'}).click();await expect(demo.locator('.demo-count')).toHaveText('Step 1 of 3');
  }
  for(const index of [6,10,15,19]) {
   await page.evaluate(i=>DL2Deck.go(i,'forward'),index);
   const check=page.locator('.slide.is-active .mission-check'),correct=Number(await check.getAttribute('data-answer'));
   await check.locator('[data-choice]').nth((correct+1)%3).click();await expect(check.locator('[role=status]')).toContainText('Reconsider.');
   await check.locator('[data-choice]').nth(correct).focus();await page.keyboard.press('Space');await expect(check.locator('[role=status]')).toContainText('Correct.');
   await check.getByRole('button',{name:'Try again'}).click();await expect(check.locator('[aria-pressed=true]')).toHaveCount(0);
  }
  await page.locator('[data-mission-jump]').selectOption('12');await expect(page.locator('.slide.is-active')).toHaveAttribute('id','slide-13');
  await page.reload();await expect(page.locator('.strip .count')).toHaveText('13 / 23');
  for(const file of ['worksheet','answer-key','lesson-plan','run-sheet','instructor-notes']) {
   await page.goto(route+'/'+file+'.html');await expect(page.locator('main h1').first()).toContainText(`Week ${week}`);
  }
  expect(errors).toEqual([]);
 });
}
for(const width of [1366,1920])test(`All new slides fit projector ${width}, default and enlarged, including answers and demo states`,async({page})=>{
 test.setTimeout(120000);await page.setViewportSize({width,height:width===1366?768:1080});await page.emulateMedia({reducedMotion:'reduce'});const bad=[];
 for(let week=2;week<=6;week++)for(const size of ['','xxl']){
  await page.goto(`${base}/weeks/week-0${week}/presentation.html#1`);await page.evaluate(s=>document.documentElement.dataset.textSize=s,size);
  for(let i=0;i<23;i++){
   await page.evaluate(i=>DL2Deck.go(i,'forward'),i);
   for(let step=0;step<3;step++){
    const measure=await page.evaluate(()=>{const s=document.querySelector('.slide.is-active'),panel=s.querySelector('.panel'),bounds=panel.getBoundingClientRect();return [...panel.querySelectorAll('h1,p,li,button,a,[data-visual]')].filter(e=>e.offsetWidth&&!e.closest('[hidden]')).filter(e=>{const r=e.getBoundingClientRect();return r.bottom>bounds.bottom-5||r.right>bounds.right-5||r.left<bounds.left}).map(e=>e.textContent.slice(0,65));});
    if(measure.length)bad.push({week,size,slide:i+1,step,measure});
    const demo=page.locator('.slide.is-active [data-demo-next]');if(await demo.count()){if(await demo.isEnabled())await demo.click();else break;}
    else if(step===0&&await page.locator('.slide.is-active [data-choice]').count())await page.locator('.slide.is-active [data-choice]').first().click();else break;
   }
  }
 }
 expect(bad).toEqual([]);
});
test('Mobile and enlarged paper pages retain controls, typed print evidence and no horizontal overflow',async({page})=>{
 await page.setViewportSize({width:390,height:844});
 for(let n=2;n<=6;n++)for(const file of ['presentation','worksheet','answer-key']){
  await page.goto(`${base}/weeks/week-0${n}/${file}.html#1`);await page.evaluate(()=>document.documentElement.dataset.textSize='xxl');
  expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),`${n} ${file}`).toBe(true);
 }
 await page.goto(`${base}/weeks/week-03/worksheet.html`);await page.locator('textarea').first().fill('I checked the PDF from its folder.');await page.reload();await expect(page.locator('textarea').first()).toHaveValue('I checked the PDF from its folder.');await page.emulateMedia({media:'print'});await expect(page.locator('.print-answer').first()).toHaveText('I checked the PDF from its folder.');await expect(page.locator('textarea').first()).toBeHidden();
});
test('Week positions are isolated and the practice library never overwrites lesson progress',async({page})=>{
 await page.goto(`${base}/weeks/week-02/presentation.html#9`);await page.waitForFunction(()=>window.VubProgress);await page.goto(`${base}/weeks/week-03/presentation.html#5`);await page.waitForFunction(()=>window.VubProgress);
 const before=await page.evaluate(()=>localStorage.getItem('vub:progress:v1'));
 await page.goto(`${base}/weeks/week-02/practice.html#slide-20`);
 expect(await page.evaluate(()=>localStorage.getItem('vub:progress:v1'))).toBe(before);
 await page.goto(`${base}/weeks/week-02/presentation.html`);await expect(page.locator('.strip .count')).toHaveText('9 / 23');
 await page.goto(`${base}/weeks/week-03/presentation.html`);await expect(page.locator('.strip .count')).toHaveText('5 / 23');
});
test('Mission lesson and worksheet pass automated accessibility checks',async({page})=>{
 for(const path of ['/weeks/week-03/presentation.html#5','/weeks/week-06/worksheet.html']){
  await page.goto(base+path);const scan=await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21aa']).analyze();expect(scan.violations).toEqual([]);
 }
});
test('Start fresh clears mission position and worksheet evidence but preserves pending submissions',async({page})=>{
 await page.goto(base+'/weeks/week-03/worksheet.html');await page.locator('textarea').first().fill('Synthetic saved evidence');
 await page.goto(base+'/weeks/week-03/presentation.html#10');await page.waitForFunction(()=>window.VubProgress);
 await page.evaluate(()=>localStorage.setItem('dl2os:outbox','[{"record-id":"synthetic-pending"}]'));
 await page.goto(base+'/index.html');page.once('dialog',d=>d.accept());await page.getByRole('button',{name:'Start fresh on this computer'}).click();
 expect(await page.evaluate(()=>Object.keys(sessionStorage).filter(k=>k.startsWith('dl2-mission-paper:')||k.startsWith('dl2os:slide:')))).toEqual([]);
 expect(await page.evaluate(()=>JSON.parse(localStorage.getItem('dl2os:outbox'))[0]['record-id'])).toBe('synthetic-pending');
});
