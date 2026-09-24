// Browser regressions from the 2026-09-24 DL2 curriculum review.
const {test,expect}=require('@playwright/test');
const base='/courses/digital-literacy-2';

// Decks start keyboard focus inside the current slide (the deck's own bypass), so the skip link
// is reached by tabbing backwards there; on document pages it is the first Tab stop.
for(const path of ['/assessments/pre-test.html','/weeks/week-01/presentation.html']){
 test(`DL2 skip link is keyboard-reachable, visible when focused, and jumps to main content on ${path}`,async({page})=>{
  await page.goto(base+path);
  const skip=page.locator('a.skip');
  await page.keyboard.press('Tab');
  for(let i=0;i<80&&!(await skip.evaluate(el=>document.activeElement===el));i++)await page.keyboard.press('Shift+Tab');
  await expect(skip).toBeFocused();
  const box=await skip.boundingBox();
  expect(box,'skip link has a box').not.toBeNull();
  expect(box.y).toBeGreaterThanOrEqual(0);
  await page.keyboard.press('Enter');
  expect(await page.evaluate(()=>location.hash)).toBe('#main');
 });
}

test('DL2 assessment topic buttons expose their visible text and answered count to assistive tech',async({page})=>{
 await page.goto(base+'/assessments/pre-test.html');
 const buttons=page.locator('[data-topic-index]');
 await expect(buttons).toHaveCount(7);
 for(let i=0;i<7;i++){const b=buttons.nth(i);const visible=(await b.innerText()).replace(/\s+/g,' ').trim();
  const name=await b.evaluate(el=>el.getAttribute('aria-label')||el.textContent);
  const normalized=name.replace(/\s+/g,' ').trim();
  for(const word of visible.split(' '))expect(normalized,`button ${i+1} accessible name "${normalized}" must contain visible "${word}"`).toContain(word);
  await expect(b).toHaveAccessibleName(/0 \/ 4 answered/);}
 await page.locator('fieldset:visible input').first().check();
 await expect(buttons.nth(0)).toHaveAccessibleName(/1 \/ 4 answered/);
 await expect(buttons.nth(3)).toHaveAccessibleName(/Creating/);
});

test('DL2 week 6 manual edit still passes the v2 search check',async({page})=>{
 await page.goto(base+'/activities/resource-finder.html');
 // The worksheet edit: rename the first fictional record, then run the v2 check from slide 10.
 await page.evaluate(()=>{resources[0].name='Community Skills Desk';});
 await page.locator('#search').fill('skills');
 await expect(page.locator('#results')).toContainText('Community Skills Desk');
 await page.locator('#search').fill('library');
 await expect(page.locator('#results')).not.toContainText('Community Skills Desk');
});
