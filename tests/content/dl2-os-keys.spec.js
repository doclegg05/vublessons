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

test('pre-test key letterhead org name renders on one line', async ({ page }) => {
  // Letter page (8.5in) minus 0.5in @page margins on each side = 7.5in usable width, matching
  // real print output (the default 1280px test viewport is wider and hides the wrap).
  await page.setViewportSize({ width: 720, height: 1000 });
  await page.goto(`${A}pre-test-answer-key.html`);
  const metrics = await page.locator('.lh-name').evaluate((el) => {
    const cs = getComputedStyle(el);
    return { height: el.getBoundingClientRect().height, lineHeight: parseFloat(cs.lineHeight), fontSize: parseFloat(cs.fontSize) };
  });
  const lineHeight = Number.isFinite(metrics.lineHeight) ? metrics.lineHeight : metrics.fontSize;
  expect(metrics.height).toBeLessThan(lineHeight * 1.6);
});

for (const form of ['pre', 'post']) {
  test(`${form} answer key is excluded from search indexing`, async ({ page }) => {
    await page.goto(`${A}${form}-test-answer-key.html`);
    await expect(page.locator('meta[name="robots"][content="noindex"]')).toHaveCount(1);
  });
}

test('syllabus states 20 questions', async ({ page }) => {
  await page.goto('/courses/digital-literacy-2/syllabus.html');
  await expect(page.locator('main')).toContainText('Each has 20 questions across the seven IC3 domains');
  await expect(page.locator('main')).not.toContainText('28 questions');
});
