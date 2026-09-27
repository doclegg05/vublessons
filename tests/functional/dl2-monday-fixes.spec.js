// Browser regressions from the 2026-09-26 DL2 full review (fixes before the 2026-09-28 cohort).
const {test,expect}=require('@playwright/test');const fs=require('fs');
const bank=JSON.parse(fs.readFileSync('courses/digital-literacy-2/assets/questions.json','utf8'));
const base='/courses/digital-literacy-2';
const deck=n=>`${base}/weeks/week-0${n}/presentation.html`;

// WCAG relative-luminance contrast between two computed CSS colours.
const contrast=(a,b)=>{const lum=c=>{const [r,g,bl]=c.match(/[\d.]+/g).slice(0,3).map(Number).map(v=>{v/=255;return v<=0.03928?v/12.92:((v+0.055)/1.055)**2.4;});return 0.2126*r+0.7152*g+0.0722*bl;};
 const [x,y]=[lum(a),lum(b)].sort((m,n)=>n-m);return (x+0.05)/(y+0.05);};

async function gradePreTest(page,name){
 await page.goto(base+'/assessments/pre-test.html');await expect(page.locator('fieldset')).toHaveCount(28);
 if(name)await page.getByLabel('Learner name or code').fill(name);
 await page.getByRole('button',{name:'Review all questions',exact:true}).click();
 for(const q of bank.pre)await page.locator(`input[name="${q.id}"][value="${q.answer}"]`).check();
 await page.getByRole('button',{name:'Grade my assessment'}).click();await expect(page.locator('#results')).toBeVisible();
}

test.describe('shared lab computers',()=>{
 test('Start fresh clears the previous learner\'s lessons and results after confirmation',async({page})=>{
  await page.goto(deck(3)+'#slide-8');await expect(page.locator('#slide-8')).toBeVisible();
  await gradePreTest(page,'Alice Example');
  await page.goto(base+'/index.html');await expect(page.locator('.continue-course')).toHaveText('Continue week 3');
  const reset=page.getByRole('button',{name:'Start fresh on this computer'});
  page.once('dialog',d=>d.dismiss());await reset.click();
  await expect(page.locator('.continue-course')).toHaveText('Continue week 3');
  page.once('dialog',d=>d.accept());await reset.click();
  await expect(page.locator('.continue-course')).toHaveText('Begin week 1');
  await expect(page.locator('[data-course-count]')).toHaveText('0 of 6 lessons viewed to the end');
  await page.goto(base+'/assessments/pre-test.html');await expect(page.locator('#answer-count')).toHaveText('0 of 28 answered');
  await expect(page.locator('#results')).toBeHidden();await expect(page.getByLabel('Learner name or code')).toHaveValue('');
 });

 test('Clear my assessment asks first and keeps results when the learner cancels',async({page})=>{
  await gradePreTest(page);
  page.once('dialog',d=>d.dismiss());await page.getByRole('button',{name:'Clear my assessment'}).click();
  await expect(page.locator('#results')).toBeVisible();
  page.once('dialog',d=>d.accept());await page.getByRole('button',{name:'Clear my assessment'}).click();
  await expect(page.locator('#results')).toBeHidden();await expect(page.locator('input:checked')).toHaveCount(0);
 });

 test('A worksheet with typed answers warns before the page is left',async({page})=>{
  await page.goto(`${base}/weeks/week-01/worksheet.html`);
  const leaving=()=>page.evaluate(()=>{const ev=new Event('beforeunload',{cancelable:true});window.dispatchEvent(ev);return ev.defaultPrevented;});
  expect(await leaving()).toBe(false);
  await page.locator('#answer-0').fill('Zoomed to 125% and checked the page');expect(await leaving()).toBe(true);
  await page.locator('#answer-0').fill('');expect(await leaving()).toBe(false);
 });
});

test('Graded results show the learner name typed without opening a disclosure, and the date graded',async({page})=>{
 await gradePreTest(page,'Learner 07');
 await expect(page.locator('.report-learner')).toContainText('Learner 07');
 const today=await page.evaluate(()=>new Date().toLocaleDateString('en-US',{year:'numeric',month:'long',day:'numeric'}));
 await expect(page.locator('.report-date')).toContainText(today);
 await page.reload();await expect(page.locator('.report-date')).toContainText(today);
});

test('Pressing Enter after typing a name moves on to the first question instead of grading',async({page})=>{
 await page.goto(base+'/assessments/pre-test.html');await expect(page.locator('fieldset')).toHaveCount(28);
 await page.getByLabel('Learner name or code').fill('Learner 07');await page.keyboard.press('Enter');
 await expect(page.locator('#assessment-error')).toHaveText('');await expect(page.locator('fieldset:visible')).toBeFocused();
});

test('Pressing Enter in the name field keeps the review-all view',async({page})=>{
 await page.goto(base+'/assessments/pre-test.html');await expect(page.locator('fieldset')).toHaveCount(28);
 await page.getByRole('button',{name:'Review all questions',exact:true}).click();await expect(page.locator('fieldset:visible')).toHaveCount(28);
 await page.getByLabel('Learner name or code').fill('Learner 07');await page.keyboard.press('Enter');
 await expect(page.locator('fieldset:visible')).toHaveCount(28);
});

test.describe('presenting a deck',()=>{
 test.use({viewport:{width:1366,height:768}});

 test('Arrow keys still change slides after clicking a button inside a slide',async({page})=>{
  await page.goto(deck(1)+'#slide-16');await page.locator('#slide-16 .check-options button').first().click();
  await page.keyboard.press('ArrowRight');await expect(page.locator('#slide-17')).toBeVisible();
 });

 test('Page Up and Page Down inside the practice calendar do not change slides',async({page})=>{
  await page.goto(deck(1)+'#slide-14');await page.locator('#slide-14 .calendar-surface').focus();
  for(const key of ['PageDown','PageUp']){await page.keyboard.press(key);await expect(page.locator('#slide-counter')).toHaveText('Slide 14 of 23');}
 });

 test('Previous and Next stay on screen on a tall slide',async({page})=>{
  await page.goto(deck(1));await page.locator('[data-slide="6"]').click();await expect(page.locator('#slide-7')).toBeVisible();
  const box=await page.locator('#next').boundingBox();expect(box.y+box.height).toBeLessThanOrEqual(768);expect(box.y).toBeGreaterThanOrEqual(0);
 });

 test('Opening a deck without a slide address does not jump down the page',async({page})=>{
  await page.goto(deck(3));await page.waitForTimeout(900);
  expect(await page.evaluate(()=>scrollY)).toBe(0);
 });
});

test.describe('contrast on the projector',()=>{
 test.use({viewport:{width:1366,height:768}});
 test.beforeEach(async({page})=>page.emulateMedia({reducedMotion:'reduce'}));

 test('Flip-card text stays readable while the pointer is over it',async({page})=>{
  await page.goto(deck(1)+'#slide-12');const card=page.locator('#slide-12 .flip').first();await card.hover();
  const [fg,bg]=await card.locator('.flip-front').evaluate(el=>[getComputedStyle(el).color,getComputedStyle(el).backgroundColor]);
  expect(contrast(fg,bg)).toBeGreaterThanOrEqual(4.5);
 });

 test('A selected phishing clue stays readable',async({page})=>{
  await page.goto(deck(5)+'#slide-8');const clue=page.locator('#slide-8 .message-preview button').first();await clue.click();await page.mouse.move(0,0);
  await expect(clue).toHaveAttribute('aria-pressed','true');
  const [fg,bg]=await clue.evaluate(el=>[getComputedStyle(el).color,getComputedStyle(el).backgroundColor]);
  expect(contrast(fg,bg)).toBeGreaterThanOrEqual(4.5);
 });

 test('The button on every completion slide stands out from the slide',async({page})=>{
  for(const n of [1,2,3,4,5,6]){await page.goto(deck(n));const last=page.locator('.slide').last();const id=await last.getAttribute('id');
   await page.goto(deck(n)+'#'+id);const cta=last.locator('.button');
   const [fg,bg,slide]=await cta.evaluate(el=>[getComputedStyle(el).color,getComputedStyle(el).backgroundColor,getComputedStyle(el.closest('.slide')).backgroundColor]);
   expect(contrast(bg,slide),`week ${n} button against slide`).toBeGreaterThanOrEqual(3);expect(contrast(fg,bg),`week ${n} button text`).toBeGreaterThanOrEqual(4.5);}
 });

 test('Keyboard focus rings are visible on dark backgrounds',async({page})=>{
  // Outline colour against the nearest opaque background behind the focused control.
  const ring=async locator=>{await page.keyboard.press('Tab');await locator.focus();
   return locator.evaluate(el=>{let bg='rgb(255, 255, 255)';
    for(let n=el.parentElement;n;n=n.parentElement){const c=getComputedStyle(n).backgroundColor;if(!/rgba\(.*,\s*0\)$|transparent/.test(c)){bg=c;break;}}
    return [getComputedStyle(el).outlineColor,bg];});};
  await page.goto(deck(1));const [tabRing,tabBg]=await ring(page.locator('.slide-link').nth(3));
  expect(contrast(tabRing,tabBg),'chapter tab').toBeGreaterThanOrEqual(3);
  await page.goto(base+'/index.html');
  // The hero button reads "Continue week 1" here, because this test already opened week 1.
  for(const [name,target] of [['pre-test',page.getByRole('link',{name:'Take the pre-test',exact:true})],['post-test',page.getByRole('link',{name:'Take the post-test',exact:true})],['continue',page.locator('.continue-course')]]){
   const [r,bg]=await ring(target);expect(contrast(r,bg),name).toBeGreaterThanOrEqual(3);}
 });
});

test('Assessment topic labels fit their tabs on a tablet-width screen',async({page})=>{
 await page.setViewportSize({width:768,height:1024});await page.goto(base+'/assessments/pre-test.html');
 const tabs=page.locator('[data-topic-index]');await expect(tabs).toHaveCount(7);
 for(let i=0;i<7;i++)expect(await tabs.nth(i).evaluate(el=>el.scrollWidth<=el.clientWidth+1),`topic ${i+1}`).toBe(true);
});
