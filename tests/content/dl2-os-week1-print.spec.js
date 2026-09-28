// Week 1 printouts: five letterhead missions with Point A/B and "You should see" on every step.
const { test, expect } = require('@playwright/test');
const { PDFDocument } = require('../../courses/digital-literacy-2/os/vendor/pdf-lib.min.js');
const W = '/courses/digital-literacy-2/weeks/week-01/';

// Prints a page the way Chromium's print dialog would (Letter, backgrounds on) and counts the sheets.
async function printedPages(page, url) {
  await page.goto(url);
  await page.evaluate(() => document.fonts.ready);
  const doc = await PDFDocument.load(await page.pdf({ format: 'Letter', printBackground: true }));
  return doc.getPageCount();
}

test('five missions, each complete', async ({ page }) => {
  await page.goto(W + 'worksheet.html');
  const m = page.locator('article.mission');
  await expect(m).toHaveCount(5);
  for (let i = 0; i < 5; i++) {
    const one = m.nth(i);
    await expect(one.locator('.letterhead')).toContainText('A TRIO program funded by the U.S. Department of Education');
    await expect(one.locator('.mission-ab .a')).toContainText('POINT A');
    await expect(one.locator('.mission-ab .b')).toContainText('POINT B');
    const steps = one.locator('ol.mission-steps > li');
    expect(await steps.count()).toBeGreaterThanOrEqual(5);
    expect(await one.locator('ol.mission-steps > li .see').count()).toBe(await steps.count());
  }
});

test('each mission prints on its own page(s), letter size', async ({ page }) => {
  await page.goto(W + 'worksheet.html');
  await page.emulateMedia({ media: 'print' });
  const breaks = await page.locator('article.mission').evaluateAll(a => a.slice(1).map(x => getComputedStyle(x).breakBefore));
  expect(breaks.every(b => b === 'page')).toBe(true);
});

test('run sheet and key exist with the letterhead', async ({ page }) => {
  for (const f of ['run-sheet.html', 'answer-key.html']) {
    await page.goto(W + f);
    await expect(page.locator('.letterhead')).toContainText('New River Community and Technical College');
  }
  await page.goto(W + 'run-sheet.html');
  await expect(page.locator('table tbody tr')).toHaveCount(9);
});

// I2 (final review): Mission E spilled onto a sixth, nearly empty sheet with its Take it home line.
test('the worksheet prints as exactly 5 pages, one per mission', async ({ page }) => {
  expect(await printedPages(page, W + 'worksheet.html')).toBe(5);
});
