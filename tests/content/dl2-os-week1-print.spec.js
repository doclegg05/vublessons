// Week 1 printouts: five letterhead missions with Point A/B and "You should see" on every step.
const { test, expect } = require('@playwright/test');
const { PDFDocument } = require('../../courses/digital-literacy-2/os/vendor/pdf-lib.min.js');
const W = '/courses/digital-literacy-2/weeks/week-01/';

// Prints a page the way Chromium's print dialog would (Letter, backgrounds on, and the page's own @page size, which
// the dialog honors: the run sheet is landscape) and counts the sheets.
async function printedPages(page, url) {
  await page.goto(url);
  await page.evaluate(() => document.fonts.ready);
  const doc = await PDFDocument.load(await page.pdf({ format: 'Letter', printBackground: true, preferCSSPageSize: true }));
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
  await expect(page.locator('table tbody tr')).toHaveCount(9); // pre-test, video, intro, five missions, close; no break row
});

// I2 (final review): Mission E spilled onto a sixth, nearly empty sheet with its Take it home line.
test('the worksheet prints as exactly 5 pages, one per mission', async ({ page }) => {
  expect(await printedPages(page, W + 'worksheet.html')).toBe(5);
});

// Final review I3/I5/C1: the run sheet's Before class list covers stale tests, the deck's slide 1 and a Forms check,
// and still prints on one landscape sheet.
test('the run sheet prints on exactly 1 page, with the Before class checks', async ({ page }) => {
  expect(await printedPages(page, W + 'run-sheet.html')).toBe(1);
  const list = page.locator('.checklist');
  await expect(list).toContainText('Open the Pre-test on each PC. If it says “Continuing the pre-test for…”, click Start over.');
  await expect(list).toContainText('Open presentation.html#1 (starts at slide 1) and press F.');
  await expect(list).toContainText('Send one test submission and confirm it arrives in Netlify Forms.');
});

// Final review minor: with the print dialog's "Background graphics" off (Edge's default), the navy DO badge, step
// numbers and Take it home bar printed white-on-white. Those mission parts keep their fills on paper.
test('mission fills print even with background graphics off', async ({ page }) => {
  await page.goto(W + 'worksheet.html');
  await page.emulateMedia({ media: 'print' });
  const sel = ['.letterhead .lh-bar', '.badges span.do', '.mission-ab .a', '.mission-ab .b', '.mission-steps > li .n',
    '.stuck', '.check', '.home', '.home .ln'];
  const modes = await page.locator('article.mission').first().evaluate((m, list) => Object.fromEntries(list.map(s => {
    const el = m.querySelector(s) || document.querySelector('#m1E ' + s);
    const cs = getComputedStyle(el);
    return [s, cs.printColorAdjust || cs.webkitPrintColorAdjust];
  })), sel);
  for (const s of sel) expect(modes[s], s).toBe('exact');
});
