// Week 2: each mission's simulation has its own page, reached from the slide and from the worksheet.
// A learner who follows a practice link should land on one activity, not inside the older 23-slide lesson.
// Source: scripts/dl2/mission-control/build.py (practice_pages flag in week2.py); rebuild the site before running.
const {test,expect}=require('@playwright/test');
const { AxeBuilder } = require('@axe-core/playwright');
const route='/courses/digital-literacy-2/weeks/week-02';
const count=page=>page.locator('.strip .count');
const openTurn=async(page,mission)=>{
 await page.goto(route+'/presentation.html#1');
 await page.evaluate(title=>DL2Deck.go([...document.querySelectorAll('.slide')].findIndex(s=>s.querySelector('h1').textContent===title),'forward'),'Your turn: Mission '+mission);
 await expect(page.locator('.slide.is-active h1')).toHaveText('Your turn: Mission '+mission);
};
const activities={
 '2B':{file:'practice-2b',title:'Practice form: request computer help'},
 '2C':{file:'practice-2c',title:'Recover the right thing'},
 '2D':{file:'practice-2d',title:'Choose who can change the file'},
};

for(const [mission,{file,title}] of Object.entries(activities)){
 test(`Mission ${mission}: the slide button opens that mission's practice page in a second tab`,async({page,context})=>{
  await openTurn(page,mission);const before=await count(page).innerText();
  const opened=context.waitForEvent('page',{timeout:5000});
  await page.locator('.slide.is-active').getByRole('link',{name:`Open Mission ${mission} practice (opens a new tab)`}).click({timeout:5000});
  const practice=await opened;await practice.waitForLoadState();
  await expect(practice).toHaveURL(new RegExp(file+'(\\.html)?$'));
  await expect(count(page)).toHaveText(before);
 });
 test(`Mission ${mission}: the practice page shows one activity and no deck controls`,async({page})=>{
  const errors=[];page.on('pageerror',e=>errors.push(e.message));
  const response=await page.goto(`${route}/${file}.html`);expect(response.status()).toBe(200);
  await expect(page.getByRole('heading',{level:1})).toHaveText(`Week 2 · Mission ${mission} practice`);
  await expect(page.locator('section.slide')).toHaveCount(1);
  await expect(page.getByRole('heading',{level:2,name:title})).toBeVisible();
  for(const control of [page.locator('#lesson-sidebar'),page.locator('#slide-counter'),page.locator('#previous'),page.locator('#next'),page.locator('#restart'),page.locator('#lesson-progress'),page.locator('.bottom-nav')])await expect(control).toBeHidden();
  await expect(page.locator('.slide-link')).toHaveCount(0);
  expect(errors).toEqual([]);
 });
}

test('Mission 2B practice: the form still validates and confirms on its own page',async({page})=>{
 await page.goto(route+'/practice-2b.html');
 await page.getByLabel('Help topic').selectOption('Finding a file');
 await page.getByLabel('Practice contact method').selectOption('Ask at the desk');
 await page.getByRole('button',{name:'Review practice request'}).click();
 await expect(page.locator('#form-result')).toContainText('No request was sent');
});
test('Mission 2C practice: choosing a recovery route still switches the preview',async({page})=>{
 await page.goto(route+'/practice-2c.html');
 await page.getByRole('button',{name:'Wrong content'}).click();
 await expect(page.getByRole('button',{name:'Wrong content'})).toHaveAttribute('aria-pressed','true');
 await expect(page.locator('.scene-state:not([hidden]) .authored-title')).toHaveText('Version history');
});
test('Mission 2D practice: choosing an access role still reports what it allows',async({page})=>{
 await page.goto(route+'/practice-2d.html');
 await page.locator('#permission').selectOption('commenter');
 await expect(page.locator('#permission-result')).toContainText('Commenter');
});

test('Mission 2A is done in the real browser, so its slide offers no practice page',async({page})=>{
 await openTurn(page,'2A');
 await expect(page.locator('.slide.is-active').getByRole('link',{name:/practice/i})).toHaveCount(0);
 await expect(page.locator('.slide.is-active').getByRole('link',{name:'Open step-by-step worksheet'})).toBeVisible();
});

test('The worksheet sends each mission to its own practice page and keeps each task under one mission',async({page})=>{
 await page.goto(route+'/worksheet.html');
 for(const [mission,{file}] of Object.entries(activities)){
  const links=page.locator(`#m${mission} a[href*="${file}"]`);
  expect(await links.count(),`Mission ${mission} links to ${file}`).toBeGreaterThan(0);
  await expect(links.first()).toHaveAttribute('target','_blank');
  await expect(links.first()).toHaveAccessibleName(/new tab/);
 }
 await expect(page.locator('#m2A a[href*="practice"]')).toHaveCount(0);
 await expect(page.locator('main')).not.toContainText('practice library exercise');
 await expect(page.locator('#m2C')).toContainText('Compressed (zipped) folder');
 await expect(page.locator('#m2D')).not.toContainText('Compressed (zipped) folder');
});

test('A practice page passes the automated accessibility checks',async({page})=>{
 await page.goto(route+'/practice-2b.html');
 const scan=await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21aa']).analyze();
 expect(scan.violations).toEqual([]);
});

test('Return to Mission Control in the full practice library comes back to the slide the lesson was on',async({page})=>{
 await openTurn(page,'2B');const before=await count(page).innerText();
 await page.goto(route+'/practice.html#slide-6');
 await page.getByRole('link',{name:'Return to Mission Control'}).click();
 await expect(count(page)).toHaveText(before);
});
