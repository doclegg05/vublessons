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

test('focus moves to the review h1 and the result h1 on those transitions', async ({ page }) => {
  await start(page);
  await answerAll(page);
  const reviewIsActive = await page.evaluate(() => {
    var h1 = document.querySelector('main h1');
    return !!h1 && document.activeElement === h1 && h1.textContent === 'Check your answers';
  });
  expect(reviewIsActive).toBe(true);
  await page.getByRole('button', { name: 'Submit my test' }).click();
  await page.getByRole('button', { name: 'Yes, submit' }).click();
  const resultIsActive = await page.evaluate(() => {
    var h1 = document.querySelector('main h1');
    return !!h1 && document.activeElement === h1 && h1.textContent.indexOf('Thank you') === 0;
  });
  expect(resultIsActive).toBe(true);
});

test('Go back in the confirm dialog returns focus to Submit my test', async ({ page }) => {
  await start(page);
  await answerAll(page);
  await page.getByRole('button', { name: 'Submit my test' }).click();
  await page.getByRole('button', { name: 'Go back' }).click();
  await expect(page.getByRole('button', { name: 'Submit my test' })).toBeFocused();
});

test('outbox: a failed item is preserved without duplication after a partial flush', async ({ page }) => {
  const mk = (id, letter) => ({
    'form-name': 'dl2-pretest', 'bot-field': '', 'record-id': id, student: letter + ' Tester',
    form: 'pre v1', started: new Date().toISOString(), submitted: new Date().toISOString(),
    score: '18/20', domains: 'x:18/20', answers: Array(20).fill(letter).join(',')
  });
  const aa = mk('DL2-PRE-20260928-1650-AA', 'A');
  const bb = mk('DL2-PRE-20260928-1650-BB', 'B');
  await page.goto(URL);
  await page.evaluate(([aa, bb]) => {
    try { localStorage.clear(); localStorage.setItem('dl2os:outbox', JSON.stringify([aa, bb])); } catch (e) {}
  }, [aa, bb]);
  const posts = [];
  await page.route('**/', async route => {
    if (route.request().method() !== 'POST') return route.continue();
    const body = new URLSearchParams(route.request().postData());
    if (body.get('record-id') === aa['record-id']) { posts.push(body.get('record-id')); return route.fulfill({ status: 200, body: 'ok' }); }
    return route.abort();
  });
  await page.reload();
  await expect.poll(async () => {
    const list = await page.evaluate(() => JSON.parse(localStorage.getItem('dl2os:outbox') || '[]'));
    return list.length === 1 && list[0]['record-id'].endsWith('-BB');
  }).toBe(true);
  expect(posts).toContain(aa['record-id']);
});

// This is the discriminating race test: it fails against a batched flush (read the
// outbox once, send everything, write the survivors back once at the end) because that
// final write clobbers whatever another code path enqueued while the flush was in
// flight. It passes only when each dequeue re-reads storage immediately before writing.
test('outbox: an item enqueued while a flush is in flight is not clobbered by that flush\'s write', async ({ page }) => {
  const mk = (id, letter) => ({
    'form-name': 'dl2-pretest', 'bot-field': '', 'record-id': id, student: letter + ' Tester',
    form: 'pre v1', started: new Date().toISOString(), submitted: new Date().toISOString(),
    score: '18/20', domains: 'x:18/20', answers: Array(20).fill(letter).join(',')
  });
  const aa = mk('DL2-PRE-20260928-1700-AA', 'A');
  const cc = mk('DL2-PRE-20260928-1700-CC', 'C');
  await page.goto(URL);
  await page.evaluate((aa) => {
    try { localStorage.clear(); localStorage.setItem('dl2os:outbox', JSON.stringify([aa])); } catch (e) {}
  }, aa);
  await page.route('**/', async route => {
    if (route.request().method() !== 'POST') return route.continue();
    const body = new URLSearchParams(route.request().postData());
    if (body.get('record-id') === aa['record-id']) {
      await new Promise(r => setTimeout(r, 800));
      return route.fulfill({ status: 200, body: 'ok' });
    }
    return route.abort();
  });
  const aaPosted = page.waitForRequest(req => {
    if (req.method() !== 'POST') return false;
    return new URLSearchParams(req.postData() || '').get('record-id') === aa['record-id'];
  });
  await Promise.all([aaPosted, page.reload()]);
  // AA's POST is now in flight (the route above is 800ms into fulfilling it). Simulate a
  // brand-new submission enqueuing CC through another code path while that flush is
  // still pending, exactly as a real second tab or a fresh submit would.
  await page.evaluate((cc) => {
    var list = JSON.parse(localStorage.getItem('dl2os:outbox') || '[]');
    list.push(cc);
    localStorage.setItem('dl2os:outbox', JSON.stringify(list));
  }, cc);
  await expect.poll(async () => {
    return page.evaluate(() => JSON.parse(localStorage.getItem('dl2os:outbox') || '[]'));
  }, { timeout: 5000 }).toEqual([cc]);
});

test('print: only the HTML report shows, app chrome and score are hidden', async ({ page }) => {
  await page.addInitScript(() => {
    Object.defineProperty(window, 'DL2Pdf', {
      value: { build: () => Promise.reject(new Error('forced')) },
      writable: false
    });
  });
  await start(page, 'Faye Cole');
  await answerAll(page);
  await page.getByRole('button', { name: 'Submit my test' }).click();
  await page.getByRole('button', { name: 'Yes, submit' }).click();
  await expect(page.locator('.html-report')).toBeVisible();
  await page.emulateMedia({ media: 'print' });
  await expect(page.locator('.html-report')).toBeVisible();
  await expect(page.locator('.result-score')).toBeHidden();
  await expect(page.locator('.test-top')).toBeHidden();
  await expect(page.locator('.copy-status')).toBeHidden();
});

test('ArrowDown twice on question 1 selects option B (radiogroup keyboard pattern)', async ({ page }) => {
  await start(page);
  await page.keyboard.press('ArrowDown');
  await page.keyboard.press('ArrowDown');
  await expect(page.locator('.opt[data-letter="B"]')).toHaveAttribute('aria-checked', 'true');
});
