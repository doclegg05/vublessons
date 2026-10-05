// Week 2: opening the practice library must not take the lesson off the projector or lose its place.
// Source: scripts/dl2/mission-control/build.py (practice_tab flag in week2.py); rebuild the site before running.
const {test,expect}=require('@playwright/test');
const route='/courses/digital-literacy-2/weeks/week-02';
const count=page=>page.locator('.strip .count');
const openSlide7=async page=>{
 await page.goto(route+'/presentation.html#1');
 await page.evaluate(()=>DL2Deck.go(6,'forward'));
 await expect(count(page)).toHaveText('7 / 36');
};

test('the practice button says it opens a new tab',async({page})=>{
 await openSlide7(page);
 await expect(page.locator('.slide.is-active').getByRole('link',{name:/Open interactive practice/})).toHaveAccessibleName(/new tab/);
});

test('the practice library opens in a second tab and the lesson stays on its slide',async({page,context})=>{
 await openSlide7(page);
 const opened=context.waitForEvent('page',{timeout:5000});
 await page.locator('.slide.is-active').getByRole('link',{name:/Open interactive practice/}).click();
 const practice=await opened;
 await practice.waitForLoadState();
 await expect(practice).toHaveURL(/practice(\.html)?#slide-6$/);
 await expect(count(page)).toHaveText('7 / 36');
});

test('Return to Mission Control comes back to the slide the lesson was on',async({page})=>{
 await openSlide7(page);
 await page.goto(route+'/practice.html#slide-6');
 await page.getByRole('link',{name:'Return to Mission Control'}).click();
 await expect(count(page)).toHaveText('7 / 36');
});
