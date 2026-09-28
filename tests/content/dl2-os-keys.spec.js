// Keys and paper tests come from the same item bank as the online test (assessment alignment rule).
const { test, expect } = require('@playwright/test');
const Items = require('../../courses/digital-literacy-2/os/items.js');
const A = '/courses/digital-literacy-2/assessments/';

for (const form of ['pre', 'post']) {
  test(`${form} key lists all 20 answers with reasons`, async ({ page }) => {
    await page.goto(`${A}${form}-test-answer-key.html`);
    await expect(page.locator('.letterhead')).toContainText('Veterans Upward Bound');
    const rows = page.locator('tbody tr');
    await expect(rows).toHaveCount(20);
    for (const i of [0, 9, 19]) await expect(rows.nth(i)).toContainText(Items[form][i].answer + ' · ');
  });
  test(`${form} printable has 20 questions with four bubbles each`, async ({ page }) => {
    await page.goto(`${A}${form}-test-printable.html`);
    await expect(page.locator('.pq')).toHaveCount(20);
    await expect(page.locator('.pq').first().locator('.bubble')).toHaveCount(4);
    await expect(page.locator('.pq').nth(19)).toContainText(Items[form][19].stem.slice(0, 30));
  });
}

test('syllabus states 20 questions', async ({ page }) => {
  await page.goto('/courses/digital-literacy-2/syllabus.html');
  await expect(page.locator('main')).toContainText('Each has 20 questions across the seven IC3 domains');
  await expect(page.locator('main')).not.toContainText('28 questions');
});
