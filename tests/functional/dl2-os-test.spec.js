// DL2 pre/post test flow: name, 20 questions, review with skip flags, grading, results copy, offline outbox.
const { test, expect } = require('@playwright/test');
const Items = require('../../courses/digital-literacy-2/os/items.js');
const URL = '/courses/digital-literacy-2/assessments/pre-test.html';

async function start(page, name = 'James Doe') {
  await page.goto(URL);
  await page.evaluate(() => { try { localStorage.clear(); } catch (e) {} });
  await page.reload();
  await page.getByLabel('Your full name').fill(name);
  await page.getByRole('button', { name: 'Start the pre-test' }).click();
}
async function answerAll(page, pick = i => Items.pre[i].answer, skip = []) {
  for (let i = 0; i < 20; i++) {
    await expect(page.locator('.q-count')).toHaveText(`Question ${i + 1} of 20`);
    if (!skip.includes(i)) await page.locator(`.opt[data-letter="${pick(i)}"]`).click();
    await page.getByRole('button', { name: i === 19 ? 'Review answers' : 'Next' }).click();
  }
}

test('name is required and the letterhead header shows', async ({ page }) => {
  await page.goto(URL);
  await expect(page.locator('.test-top')).toContainText('Digital Literacy Level 2 · Pre-Test');
  await page.getByRole('button', { name: 'Start the pre-test' }).click();
  await expect(page.locator('.field-error')).toContainText('Please type your name');
});

test('selection shows in words; Back is disabled on question 1', async ({ page }) => {
  await start(page);
  await page.locator('.opt[data-letter="B"]').click();
  await expect(page.locator('.opt[data-letter="B"] .pick')).toHaveText('✓ Selected');
  await expect(page.locator('.opt[data-letter="B"]')).toHaveAttribute('aria-checked', 'true');
  await expect(page.getByRole('button', { name: 'Back' })).toBeDisabled();
});

test('full run: skip one, review, submit, grade, send copy', async ({ page }) => {
  const posts = [];
  await page.route('**/', async route => {
    if (route.request().method() === 'POST') { posts.push(route.request().postData()); return route.fulfill({ status: 200, body: 'ok' }); }
    return route.continue();
  });
  await start(page);
  await answerAll(page, i => (i === 0 ? (Items.pre[0].answer === 'A' ? 'B' : 'A') : Items.pre[i].answer), [4]);
  await expect(page.locator('.review-row.skipped')).toHaveCount(1);
  await expect(page.locator('.review-row.skipped')).toContainText('Not answered');
  await page.getByRole('button', { name: 'Submit my test' }).click();
  await page.getByRole('button', { name: 'Yes, submit' }).click();
  await expect(page.locator('.result-score')).toContainText('18 of 20');
  await expect(page.locator('.copy-status')).toContainText('A copy was sent to Britt');
  expect(posts).toHaveLength(1);
  const body = new URLSearchParams(posts[0]);
  expect(body.get('form-name')).toBe('dl2-pretest');
  expect(body.get('student')).toBe('James Doe');
  expect(body.get('score')).toBe('18/20');
  expect(body.get('record-id')).toMatch(/^DL2-PRE-\d{8}-\d{4}-JD$/);
  expect(body.get('answers').split(',')).toHaveLength(20);
});

test('offline: result is queued and sent on the next visit', async ({ page }) => {
  let fail = true; const posts = [];
  await page.route('**/', async route => {
    if (route.request().method() !== 'POST') return route.continue();
    if (fail) return route.abort();
    posts.push(route.request().postData()); return route.fulfill({ status: 200, body: 'ok' });
  });
  await start(page, 'Ann Lee');
  await answerAll(page);
  await page.getByRole('button', { name: 'Submit my test' }).click();
  await page.getByRole('button', { name: 'Yes, submit' }).click();
  await expect(page.locator('.copy-status')).toContainText('Saved on this computer. Tell Britt.');
  expect(await page.evaluate(() => JSON.parse(localStorage.getItem('dl2os:outbox')).length)).toBe(1);
  fail = false;
  await page.goto(URL);
  await expect.poll(() => posts.length).toBe(1);
  expect(await page.evaluate(() => JSON.parse(localStorage.getItem('dl2os:outbox') || '[]').length)).toBe(0);
});

test('a reload keeps answers in progress', async ({ page }) => {
  await start(page);
  await page.locator('.opt[data-letter="C"]').click();
  await page.reload();
  await expect(page.locator('.q-count')).toHaveText('Question 1 of 20');
  await expect(page.locator('.opt[data-letter="C"]')).toHaveClass(/sel/);
});

test('the page registers its Netlify form and loads no external resources', async ({ page }) => {
  const external = [];
  page.on('request', r => { if (!r.url().startsWith('http://localhost:3939')) external.push(r.url()); });
  await page.goto(URL);
  await expect(page.locator('form[name="dl2-pretest"][data-netlify="true"]')).toHaveCount(1);
  expect(external).toEqual([]);
});
