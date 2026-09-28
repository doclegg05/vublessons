// Submitting the pre-test downloads a letterhead PDF whose metadata carries the record ID.
const { test, expect } = require('@playwright/test');
const fs = require('fs');
const { PDFDocument } = require('../../courses/digital-literacy-2/os/vendor/pdf-lib.min.js');
const Items = require('../../courses/digital-literacy-2/os/items.js');

test('pre-test PDF: 2 pages, record-id title, named file', async ({ page }) => {
  await page.route('**/', r => r.request().method() === 'POST' ? r.fulfill({ status: 200, body: 'ok' }) : r.continue());
  await page.goto('/courses/digital-literacy-2/assessments/pre-test.html');
  await page.evaluate(() => { try { localStorage.clear(); } catch (e) {} });
  await page.reload();
  await page.getByLabel('Your full name').fill('James Doe');
  await page.getByRole('button', { name: 'Start the pre-test' }).click();
  for (let i = 0; i < 20; i++) {
    await page.locator(`.opt[data-letter="${Items.pre[i].answer}"]`).click();
    await page.getByRole('button', { name: i === 19 ? 'Review answers' : 'Next' }).click();
  }
  await page.getByRole('button', { name: 'Submit my test' }).click();
  const [download] = await Promise.all([page.waitForEvent('download'), page.getByRole('button', { name: 'Yes, submit' }).click()]);
  expect(download.suggestedFilename()).toMatch(/^DL2-PreTest-Doe-\d{8}-\d{4}\.pdf$/);
  const bytes = fs.readFileSync(await download.path());
  expect(bytes.subarray(0, 4).toString()).toBe('%PDF');
  const doc = await PDFDocument.load(bytes);
  expect(doc.getPageCount()).toBe(2);
  expect(doc.getTitle()).toMatch(/^DL2-PRE-\d{8}-\d{4}-JD$/);
  expect(doc.getAuthor()).toBe('West Virginia Veterans Upward Bound');
  await expect(page.locator('.pdf-status')).toContainText('saved in Downloads');
});
