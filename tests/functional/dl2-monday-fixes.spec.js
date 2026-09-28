// Browser regressions from the 2026-09-26 DL2 full review (fixes before the 2026-09-28 cohort).
const {test,expect}=require('@playwright/test');
const base='/courses/digital-literacy-2';
const deck=n=>`${base}/weeks/week-0${n}/presentation.html`;

// WCAG relative-luminance contrast between two computed CSS colours.
const contrast=(a,b)=>{const lum=c=>{const [r,g,bl]=c.match(/[\d.]+/g).slice(0,3).map(Number).map(v=>{v/=255;return v<=0.03928?v/12.92:((v+0.055)/1.055)**2.4;});return 0.2126*r+0.7152*g+0.0722*bl;};
 const [x,y]=[lum(a),lum(b)].sort((m,n)=>n-m);return (x+0.05)/(y+0.05);};

// Retired 2026-09-28 (Mission Control, Task 11) with the replaced 28-question pre-test, old Week 1 deck and old
// Week 1 worksheet (their new versions are covered by the dl2-os-* specs):
//  - 'Clear my assessment asks first and keeps results when the learner cancels' (old results panel)
//  - 'A worksheet with typed answers warns before the page is left' (old worksheet #answer-0; the new missions are paper)
//  - 'Graded results show the learner name typed without opening a disclosure, and the date graded' (old results report)
//  - 'Pressing Enter after typing a name moves on to the first question instead of grading' (old name field)
//  - 'Pressing Enter in the name field keeps the review-all view' (old review-all view)
//  - 'Arrow keys still change slides after clicking a button inside a slide' (old week 1 slide 21)
//  - 'Page Up and Page Down inside the practice calendar do not change slides' (old week 1 slide 15)
//  - 'Previous and Next stay on screen on a tall slide' (old week 1 slide 7)
//  - 'Flip-card text stays readable while the pointer is over it' (old week 1 slide 10)
//  - 'Assessment topic labels fit their tabs on a tablet-width screen' (old topic tabs)

test.describe('shared lab computers',()=>{
 // Narrowed 2026-09-28 (Mission Control, Task 11): the old pre-test grading is gone. The new pre-test keeps answers in
 // progress (not results) on the computer, so Start fresh must clear those, but keep any unsent copy meant for Britt.
 test('Start fresh clears the previous learner\'s lessons and test answers after confirmation',async({page})=>{
  await page.goto(deck(3)+'#slide-8');await expect(page.locator('#slide-8')).toBeVisible();
  await page.goto(base+'/assessments/pre-test.html');
  await page.getByLabel('Your full name').fill('Alice Example');await page.getByRole('button',{name:'Start the pre-test'}).click();
  await page.locator('.opt[data-letter="A"]').click();
  await page.evaluate(()=>localStorage.setItem('dl2os:outbox',JSON.stringify([{'record-id':'DL2-PRE-20260928-1700-AE'}])));
  await page.goto(base+'/index.html');await expect(page.locator('.continue-course')).toHaveText('Continue week 3');
  const reset=page.getByRole('button',{name:'Start fresh on this computer'});
  page.once('dialog',d=>d.dismiss());await reset.click();
  await expect(page.locator('.continue-course')).toHaveText('Continue week 3');
  page.once('dialog',d=>d.accept());await reset.click();
  await expect(page.locator('.continue-course')).toHaveText('Begin week 1');
  await expect(page.locator('[data-course-count]')).toHaveText('0 of 6 lessons viewed to the end');
  expect(await page.evaluate(()=>JSON.parse(localStorage.getItem('dl2os:outbox')).length),'unsent copy kept').toBe(1);
  await page.route('**/',r=>r.request().method()==='POST'?r.fulfill({status:200,body:'ok'}):r.continue());
  await page.goto(base+'/assessments/pre-test.html');
  await expect(page.getByLabel('Your full name')).toHaveValue('');await expect(page.locator('.q-count')).toHaveCount(0);
 });
});

test.describe('presenting a deck',()=>{
 test.use({viewport:{width:1366,height:768}});

 test('Opening a deck without a slide address does not jump down the page',async({page})=>{
  await page.goto(deck(3));await page.waitForTimeout(900);
  expect(await page.evaluate(()=>scrollY)).toBe(0);
 });
});

test.describe('contrast on the projector',()=>{
 test.use({viewport:{width:1366,height:768}});
 test.beforeEach(async({page})=>page.emulateMedia({reducedMotion:'reduce'}));

 test('A selected phishing clue stays readable',async({page})=>{
  await page.goto(deck(5)+'#slide-1');const clue=page.locator('#slide-1 .message-preview button').first();await clue.click();await page.mouse.move(0,0);
  await expect(clue).toHaveAttribute('aria-pressed','true');
  const [fg,bg]=await clue.evaluate(el=>[getComputedStyle(el).color,getComputedStyle(el).backgroundColor]);
  expect(contrast(fg,bg)).toBeGreaterThanOrEqual(4.5);
 });

 // Narrowed 2026-09-28 (Mission Control, Task 11): weeks 2–6; week 1's replaced deck ends on a finale with no .button call to action.
 test('The button on every completion slide stands out from the slide',async({page})=>{
  for(const n of [2,3,4,5,6]){await page.goto(deck(n));const last=page.locator('.slide').last();const id=await last.getAttribute('id');
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
  // Narrowed 2026-09-28 (Mission Control, Task 11): the chapter tab is checked on week 2, since week 1's replaced
  // deck has no .slide-link chapter tabs.
  await page.goto(deck(2));const [tabRing,tabBg]=await ring(page.locator('.slide-link').nth(3));
  expect(contrast(tabRing,tabBg),'chapter tab').toBeGreaterThanOrEqual(3);
  await page.goto(base+'/index.html');
  // The hero button reads "Continue week 2" here, because this test already opened week 2.
  for(const [name,target] of [['pre-test',page.getByRole('link',{name:'Take the pre-test',exact:true})],['post-test',page.getByRole('link',{name:'Take the post-test',exact:true})],['continue',page.locator('.continue-course')]]){
   const [r,bg]=await ring(target);expect(contrast(r,bg),name).toBeGreaterThanOrEqual(3);}
 });
});
