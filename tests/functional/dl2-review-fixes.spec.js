// Mission Control extension: legacy simulation checks now exercise the retained practice library.
// Browser regressions from the 2026-09-24 DL2 curriculum review.
const {test,expect}=require('@playwright/test');
const base='/courses/digital-literacy-2';

// Decks start keyboard focus inside the current slide (the deck's own bypass), so the skip link
// is reached by tabbing backwards there; on document pages it is the first Tab stop.
// Narrowed 2026-09-28 (Mission Control, Task 11): the generated-deck case uses week 2, since week 1's deck was replaced.
for(const path of ['/assessments/pre-test.html','/weeks/week-02/practice.html']){
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

// Retired 2026-09-28 (Mission Control, Task 11): 'DL2 assessment topic buttons expose their visible text and answered
// count to assistive tech'. The replaced 28-question pre-test's topic tabs are gone; the new test has no topic tabs.

// Retired 2026-09-26 with the week 6 redesign: 'DL2 week 6 manual edit still passes the v2 search check'.
// Learners no longer rename a record; the three practice pages are checked in
// tests/functional/dl2-week6-agent.spec.js. The top-level resources array stays for dl2-video-chapters.
test('DL2 week 6 starter keeps its data in a top-level resources array',async({page})=>{
 await page.goto(base+'/activities/resource-finder.html');
 expect(await page.evaluate(()=>resources[0].name)).toBe('Community library');
});
