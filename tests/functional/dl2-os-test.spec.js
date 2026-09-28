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

// I4 (final review): with the PDF unavailable, the HTML report shows the name and record ID as text only.
// Every element in the report must be one the report itself writes, with no event-handler attributes.
test('fallback report: a crafted name adds no markup of its own', async ({ page }) => {
  await page.addInitScript(() => {
    Object.defineProperty(window, 'DL2Pdf', { value: { build: () => Promise.reject(new Error('forced')) }, writable: false });
  });
  await page.route('**/', r => (r.request().method() === 'POST' ? r.fulfill({ status: 200, body: 'ok' }) : r.continue()));
  const name = '<x onmouseover=window.__pwn=1 y';
  await start(page, name);
  await answerAll(page);
  await page.getByRole('button', { name: 'Submit my test' }).click();
  await page.getByRole('button', { name: 'Yes, submit' }).click();
  const report = page.locator('.html-report');
  await expect(report).toBeVisible();
  await expect(report).toContainText(name);
  await expect(report).toContainText(/Record DL2-PRE-\d{8}-\d{4}-XY/);
  const odd = await report.evaluate(el => {
    const ok = ['DIV', 'HEADER', 'IMG', 'DL', 'DT', 'DD', 'H2', 'P', 'TABLE', 'THEAD', 'TBODY', 'TR', 'TH', 'TD'];
    return [...el.querySelectorAll('*')]
      .filter(n => !ok.includes(n.tagName) || [...n.attributes].some(a => /^on/i.test(a.name)))
      .map(n => n.outerHTML.slice(0, 80));
  });
  expect(odd).toEqual([]);
});

test('fallback report escapes the record ID itself', async ({ page }) => {
  await page.addInitScript(() => {
    Object.defineProperty(window, 'DL2Pdf', { value: { build: () => Promise.reject(new Error('forced')) }, writable: false });
    // Force a record ID with markup in it, whatever initials() returns.
    let grade;
    Object.defineProperty(window, 'DL2Grade', {
      configurable: true,
      get: () => grade,
      set: v => { grade = Object.assign({}, v, { recordId: () => 'DL2-PRE-<i>ID</i>' }); }
    });
  });
  await page.route('**/', r => (r.request().method() === 'POST' ? r.fulfill({ status: 200, body: 'ok' }) : r.continue()));
  await start(page, 'Lee Park');
  await answerAll(page);
  await page.getByRole('button', { name: 'Submit my test' }).click();
  await page.getByRole('button', { name: 'Yes, submit' }).click();
  const report = page.locator('.html-report');
  await expect(report).toContainText('Record DL2-PRE-<i>ID</i> · Lee Park');
  await expect(report.locator('i')).toHaveCount(0);
});

// I5 (final review): a lab PC can open on someone else's unsubmitted test. When a saved test in progress
// has a name, the question and review screens say whose it is and offer Start over (keyboard, words, escaped).
async function leaveTest(page, saved) {
  await page.goto(URL);
  await page.evaluate(s => { localStorage.clear(); localStorage.setItem('dl2os:test:pre', JSON.stringify(s)); }, saved);
  await page.reload();
}
const inProgress = (phase, name) => ({ phase, name, started: new Date().toISOString(), at: 3, answers: Array.from({ length: 20 }, (_, i) => (i < 3 ? 'A' : null)) });

test('a saved test in progress says whose it is, and Start over returns to the name screen', async ({ page }) => {
  await leaveTest(page, inProgress('q', '<b>Pat</b> Smith'));
  await expect(page.locator('.q-count')).toHaveText('Question 4 of 20');
  const note = page.locator('.resume-note');
  await expect(note).toHaveText('Continuing the pre-test for <b>Pat</b> Smith. Not you? Start over');
  await expect(note.locator('b')).toHaveCount(0);
  await page.keyboard.press('Shift+Tab'); // from the focused answer back to Start over
  await expect(note.getByRole('button', { name: 'Start over' })).toBeFocused();
  await page.keyboard.press('Enter');
  await expect(page.getByLabel('Your full name')).toHaveValue('');
  await expect(page.getByLabel('Your full name')).toBeFocused();
  await expect(page.locator('.resume-note')).toHaveCount(0);
  expect(await page.evaluate(() => localStorage.getItem('dl2os:test:pre'))).toBeNull();
  await page.reload();
  await expect(page.getByRole('button', { name: 'Start the pre-test' })).toBeVisible();
});

test('the review screen also says whose test it is', async ({ page }) => {
  await leaveTest(page, inProgress('review', 'Ann Lee'));
  await expect(page.getByRole('heading', { name: 'Check your answers' })).toBeVisible();
  await expect(page.locator('.resume-note')).toContainText('Continuing the pre-test for Ann Lee. Not you?');
  await page.locator('.resume-note').getByRole('button', { name: 'Start over' }).click();
  await expect(page.getByRole('button', { name: 'Start the pre-test' })).toBeVisible();
});

test('a test started in this visit shows no Not-you note', async ({ page }) => {
  await start(page);
  await expect(page.locator('.q-count')).toHaveText('Question 1 of 20');
  await expect(page.locator('.resume-note')).toHaveCount(0);
});

// Final review minor (ledger T5): an arrow key pressed to scroll must not silently change the answer.
// Arrow keys only act inside the answer options; A–D still work anywhere outside a text field.
test('arrow keys change the answer only when focus is on the options', async ({ page }) => {
  await start(page);
  await page.locator('.opt[data-letter="A"]').click();
  await page.getByRole('button', { name: 'Next' }).focus();
  await page.keyboard.press('ArrowDown');
  await expect(page.locator('.opt[data-letter="A"]')).toHaveAttribute('aria-checked', 'true');
  await expect(page.locator('.opt[data-letter="B"]')).toHaveAttribute('aria-checked', 'false');
  await expect(page.locator('.q-count')).toHaveText('Question 1 of 20');
  await page.getByRole('button', { name: 'Next' }).focus();
  await page.keyboard.press('c');
  await expect(page.locator('.opt[data-letter="C"]')).toHaveAttribute('aria-checked', 'true');
});
