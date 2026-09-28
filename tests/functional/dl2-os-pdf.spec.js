// Submitting the pre-test downloads a letterhead PDF whose metadata carries the record ID.
const { test, expect } = require('@playwright/test');
const fs = require('fs');
const { PDFDocument } = require('../../courses/digital-literacy-2/os/vendor/pdf-lib.min.js');
const Items = require('../../courses/digital-literacy-2/os/items.js');

// Takes the pre-test as `name` (pick(i) is the letter chosen for item i; skipped items get no answer),
// submits it, and returns the downloaded PDF.
async function submitPre(page, pick = i => Items.pre[i].answer, skip = [], name = 'James Doe') {
  await page.route('**/', r => r.request().method() === 'POST' ? r.fulfill({ status: 200, body: 'ok' }) : r.continue());
  await page.goto('/courses/digital-literacy-2/assessments/pre-test.html');
  await page.evaluate(() => { try { localStorage.clear(); } catch (e) {} });
  await page.reload();
  await page.getByLabel('Your full name').fill(name);
  await page.getByRole('button', { name: 'Start the pre-test' }).click();
  for (let i = 0; i < 20; i++) {
    if (!skip.includes(i)) await page.locator(`.opt[data-letter="${pick(i)}"]`).click();
    await page.getByRole('button', { name: i === 19 ? 'Review answers' : 'Next' }).click();
  }
  await page.getByRole('button', { name: 'Submit my test' }).click();
  const [download] = await Promise.all([page.waitForEvent('download'), page.getByRole('button', { name: 'Yes, submit' }).click()]);
  const bytes = fs.readFileSync(await download.path());
  expect(bytes.subarray(0, 4).toString()).toBe('%PDF');
  return { download, doc: await PDFDocument.load(bytes) };
}

test('pre-test PDF: 2 pages, record-id title, named file', async ({ page }) => {
  const { download, doc } = await submitPre(page);
  expect(download.suggestedFilename()).toMatch(/^DL2-PreTest-Doe-\d{8}-\d{4}\.pdf$/);
  expect(doc.getPageCount()).toBe(2);
  expect(doc.getTitle()).toMatch(/^DL2-PRE-\d{8}-\d{4}-JD$/);
  expect(doc.getAuthor()).toBe('West Virginia Veterans Upward Bound');
  await expect(page.locator('.pdf-status')).toContainText('saved in Downloads');
});

test('mixed result PDF (item 1 wrong, item 5 skipped): 2 pages, record-id title', async ({ page }) => {
  const wrong = Items.pre[0].answer === 'A' ? 'B' : 'A';
  const { doc } = await submitPre(page, i => (i === 0 ? wrong : Items.pre[i].answer), [4]);
  await expect(page.locator('.result-score')).toContainText('18 of 20');
  expect(doc.getPageCount()).toBe(2);
  expect(doc.getTitle()).toMatch(/^DL2-PRE-\d{8}-\d{4}-JD$/);
  await expect(page.locator('.pdf-status')).toContainText('saved in Downloads');
});

test('without the self-hosted fonts, the PDF falls back to standard fonts and still builds', async ({ page }) => {
  await page.route('**/os/fonts/*.woff', r => r.abort());
  const { doc } = await submitPre(page, undefined, [], 'José Núñez−Smith');
  expect(doc.getPageCount()).toBe(2);
  expect(doc.getTitle()).toMatch(/^DL2-PRE-\d{8}-\d{4}-JN$/);
  await expect(page.locator('.pdf-status')).toContainText('saved in Downloads');
});
