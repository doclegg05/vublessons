const {test,expect}=require('@playwright/test');
const base='/courses/digital-literacy-2';
// Retired 2026-09-28 (Mission Control, Task 11), both targeting the replaced 28-question assessments:
// 'DL2 focused assessment retains answers, position and truthful topic progress' (fieldsets, #question-position,
// topic tabs) and 'DL2 learning app remains accessible on mobile with enlarged text and a selected answer' (the old
// post-test's course rail). The new 20-question tests are covered by tests/functional/dl2-os-test.spec.js and
// tests/functional/dl2-os-a11y.spec.js.
test('DL2 course continue reflects the saved lesson rather than invented completion',async({page})=>{
 await page.goto(base+'/weeks/week-02/presentation.html');await page.locator('[data-deck-next]').click();await page.goto(base+'/index.html');await expect(page.locator('.continue-course')).toHaveText('Continue week 2');await expect(page.locator('[data-continue-caption]')).toContainText('slide 2');await expect(page.locator('[data-course-count]')).toHaveText('0 of 6 lessons viewed to the end');await page.locator('.continue-course').click();await expect(page.locator('.strip .count')).toContainText('2 /');
});
