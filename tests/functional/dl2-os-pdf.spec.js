// Submitting the pre-test downloads a letterhead PDF whose metadata carries the record ID.
const { test, expect } = require('@playwright/test');
const fs = require('fs');
const { PDFDocument, PDFArray, StandardFonts, decodePDFRawStream } = require('../../courses/digital-literacy-2/os/vendor/pdf-lib.min.js');
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
  expect(download.suggestedFilename()).toMatch(/^DL2-PreTest-Doe-\d{8}-\d{4}-[0-9a-f]{8}\.pdf$/);
  expect(doc.getPageCount()).toBe(2);
  expect(doc.getTitle()).toMatch(/^DL2-PRE-\d{8}-\d{4}-JD-[0-9a-f]{8}$/);
  expect(doc.getAuthor()).toBe('West Virginia Veterans Upward Bound');
  await expect(page.locator('.pdf-status')).toContainText('download has started');
});

test('mixed result PDF (item 1 wrong, item 5 skipped): 2 pages, record-id title', async ({ page }) => {
  const wrong = Items.pre[0].answer === 'A' ? 'B' : 'A';
  const { doc } = await submitPre(page, i => (i === 0 ? wrong : Items.pre[i].answer), [4]);
  await expect(page.locator('.result-score')).toContainText('18 of 20');
  expect(doc.getPageCount()).toBe(2);
  expect(doc.getTitle()).toMatch(/^DL2-PRE-\d{8}-\d{4}-JD-[0-9a-f]{8}$/);
  await expect(page.locator('.pdf-status')).toContainText('download has started');
});

test('without the self-hosted fonts, the PDF falls back to standard fonts and still builds', async ({ page }) => {
  await page.route('**/os/fonts/*.woff', r => r.abort());
  const { doc } = await submitPre(page, undefined, [], 'José Núñez−Smith');
  expect(doc.getPageCount()).toBe(2);
  expect(doc.getTitle()).toMatch(/^DL2-PRE-\d{8}-\d{4}-JN-[0-9a-f]{8}$/);
  await expect(page.locator('.pdf-status')).toContainText('download has started');
});

// Every text run drawn on a page, as { size, text }. Only readable for the StandardFonts (WinAnsi) fallback,
// so tests that use it block the self-hosted fonts.
async function drawnText(doc, pageIndex) {
  const c = doc.getPage(pageIndex).node.Contents();
  const streams = c instanceof PDFArray ? c.asArray().map(r => doc.context.lookup(r)) : [c];
  const src = streams.map(st => Buffer.from(decodePDFRawStream(st).decode()).toString('latin1')).join('\n');
  const WIN = { 0x85: '…', 0x91: '‘', 0x92: '’', 0x93: '“', 0x94: '”', 0x95: '•', 0x96: '–', 0x97: '—' };
  return [...src.matchAll(/\/\S+ ([\d.]+) Tf[\s\S]*?<([0-9A-Fa-f]*)> Tj/g)].map(m => ({
    size: Number(m[1]),
    text: Buffer.from(m[2], 'hex').toString('latin1').replace(/[\x80-\x9f]/g, ch => WIN[ch.charCodeAt(0)] || ch)
  }));
}
const studentName = runs => runs[runs.findIndex(r => r.text === 'STUDENT') + 1];
const STUDENT_BOX = 190 - 18; // box width less 9pt padding each side

// Final review minors: a long name shrank nothing and ran into STARTED / SUBMITTED; letters outside Latin-1
// were dropped ("Nguyễn" became "Nguyn") in the PDF and its file name.
test('a very long, accented name fits the Student box (shrunk to 7pt, then cut with …) and the file name is ASCII', async ({ page }) => {
  await page.route('**/os/fonts/*.woff', r => r.abort());
  const name = 'Nguyễn Thị Bartholomew-Alexander Montgomery-Wellington Fitzgerald-Nguyễn';
  const { download, doc } = await submitPre(page, undefined, [], name);
  expect(download.suggestedFilename()).toMatch(/^DL2-PreTest-Fitzgerald-Nguyen-\d{8}-\d{4}-[0-9a-f]{8}\.pdf$/);
  const helv = await (await PDFDocument.create()).embedFont(StandardFonts.Helvetica);
  const drawn = studentName(await drawnText(doc, 0));
  expect(drawn.text.startsWith('Nguyen Thi Bartholomew')).toBe(true);
  expect(drawn.text.endsWith('…')).toBe(true);
  expect(drawn.size).toBe(7);
  expect(helv.widthOfTextAtSize(drawn.text, drawn.size)).toBeLessThanOrEqual(STUDENT_BOX);
  // Page 2's running header (name · record) stays inside the right margin too.
  const head = (await drawnText(doc, 1)).find(r => r.text.includes(' · Record DL2-PRE-'));
  expect(head.text.startsWith('Nguyen Thi ')).toBe(true);
  expect(helv.widthOfTextAtSize(head.text, head.size)).toBeLessThanOrEqual(612 - 44 - (44 + 50));
});

test('a longish name shrinks to fit the Student box without being cut', async ({ page }) => {
  await page.route('**/os/fonts/*.woff', r => r.abort());
  const name = 'Bartholomew Alexander Montgomery-Wellington';
  await submitPre(page, undefined, [], name).then(async ({ doc }) => {
    const helv = await (await PDFDocument.create()).embedFont(StandardFonts.Helvetica);
    const drawn = studentName(await drawnText(doc, 0));
    expect(drawn.text).toBe(name);
    expect(drawn.size).toBeGreaterThanOrEqual(7);
    expect(drawn.size).toBeLessThan(10.5);
    expect(helv.widthOfTextAtSize(drawn.text, drawn.size)).toBeLessThanOrEqual(STUDENT_BOX);
  });
});

test('a short name keeps the full 10.5pt size', async ({ page }) => {
  await page.route('**/os/fonts/*.woff', r => r.abort());
  const { doc } = await submitPre(page, undefined, [], 'Ann Lee');
  expect(studentName(await drawnText(doc, 0))).toEqual({ size: 10.5, text: 'Ann Lee' });
});
