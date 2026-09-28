// tests/functional/dl2-os-week1-deck.spec.js
// Week 1 deck: 27 slides (no break), WIPPEA order, every Show mounts, text floor, no external requests.
const { test, expect } = require('@playwright/test');
const URL = '/courses/digital-literacy-2/weeks/week-01/presentation.html';

test('structure: 27 slides, phases in order, five demos, five Do slides, no timer', async ({ page }) => {
  await page.goto(URL);
  await expect(page.locator('.slide')).toHaveCount(27);
  await expect(page.locator('.slide[data-stage="show"] .demo-bezel')).toHaveCount(5);
  await expect(page.locator('.slide[data-stage="do"]')).toHaveCount(5);
  await expect(page.locator('.timer, [data-minutes], .strip [role="timer"]')).toHaveCount(0);
  const phases = await page.locator('.slide[data-phase]').evaluateAll(s => s.map(x => x.dataset.phase));
  const order = ['warm-up', 'intro', 'present', 'practice', 'evaluate', 'apply'];
  expect(phases[0]).toBe('warm-up'); expect(phases.at(-1)).toBe('apply');
  expect(phases.every(p => order.includes(p))).toBe(true);
  await expect(page.locator('a[href*="legacy"]')).toHaveCount(0);
});

// Britt teaches without a class break, so no slide or speaker note schedules one.
test('no break slide or break cue', async ({ page }) => {
  await page.goto(URL);
  const text = await page.locator('.slide').evaluateAll(s => s.map(x => x.textContent).join(' '));
  expect(text).not.toMatch(/\bbreak\b|intermission/i);
});

// Every unit slide names the app (and file, when there is one) learners work in.
test('every unit slide names its app', async ({ page }) => {
  await page.goto(URL);
  const want = { A: 'Windows Settings', B: 'Windows Quick Settings', C: 'Microsoft Word', D: 'Microsoft Outlook', E: 'Microsoft Word' };
  const got = await page.locator('.slide[data-unit]').evaluateAll(s =>
    s.map(x => ({ unit: x.dataset.unit, app: (x.querySelector('.hud .app') || {}).textContent || '' })));
  expect(got.length).toBe(21);
  for (const g of got) expect(g.app, `unit ${g.unit}`).toContain(want[g.unit]);
  const c = got.filter(g => g.unit === 'C');
  expect(c.every(g => g.app.includes('Community Supper Flyer.docx'))).toBe(true);
});

test('every slide fits 1920×1080 and body text is at least 32px', async ({ page }) => {
  await page.setViewportSize({ width: 1920, height: 1080 });
  await page.emulateMedia({ reducedMotion: 'reduce' });
  await page.goto(URL + '#1');
  const n = await page.locator('.slide').count();
  const problems = [];
  for (let i = 0; i < n; i++) {
    await page.evaluate(k => DL2Deck.go(k, 'back'), i); // back = all build parts shown
    const r = await page.evaluate(() => {
      const s = document.querySelector('.slide.is-active');
      const texts = [...s.querySelectorAll('p, li, .demo-cap, .ab div, .sab div, .dsteps div')].filter(e => e.offsetParent && !e.closest('.screen'));
      const small = texts.filter(e => parseFloat(getComputedStyle(e).fontSize) < 31.5).map(e => e.textContent.trim().slice(0, 40));
      const deck = document.querySelector('.deck').getBoundingClientRect();
      const over = [...s.querySelectorAll('*')].filter(e => !e.closest('.screen') && e.getBoundingClientRect().bottom > deck.bottom + 1).map(e => e.className);
      return { small, over };
    });
    if (r.small.length || r.over.length) problems.push({ slide: i + 1, ...r });
  }
  expect(problems).toEqual([]);
});

test('no external requests', async ({ page }) => {
  const ext = [];
  page.on('request', r => { if (!r.url().startsWith('http://localhost:3939')) ext.push(r.url()); });
  await page.goto(URL);
  await page.waitForLoadState('networkidle');
  expect(ext).toEqual([]);
});

test('legacy deck still opens', async ({ page }) => {
  const r = await page.goto('/courses/digital-literacy-2/weeks/week-01/presentation-legacy.html');
  expect(r.status()).toBe(200);
});

// Polish pass: the deck must fit at every step of the A−/A+ control, and the control's status
// label ("Default text") is for screen readers only; the phase strip shows just A− and A+.
test('every slide fits at every text size, and the text-size status is visually hidden', async ({ page }) => {
  test.setTimeout(120_000);
  await page.setViewportSize({ width: 1920, height: 1080 });
  await page.emulateMedia({ reducedMotion: 'reduce' });
  await page.goto(URL + '#1');
  await page.evaluate(() => document.fonts.ready);

  const status = await page.evaluate(() => {
    const s = document.querySelector('.strip .vub-textsize .status');
    if (!s) return null;
    return { width: s.getBoundingClientRect().width, computed: parseFloat(getComputedStyle(s).width) };
  });
  expect(status, 'text-size.js adds a status label to the strip').not.toBeNull();
  expect.soft(status.width, "status label rendered width").toBeLessThanOrEqual(1);
  expect.soft(status.computed, "status label computed width").toBeLessThanOrEqual(1);

  const n = await page.locator('.slide').count();
  const problems = [];
  for (const size of ['sm', '', 'lg', 'xl', 'xxl']) {
    await page.evaluate(sz => {
      if (sz) document.documentElement.dataset.textSize = sz;
      else document.documentElement.removeAttribute('data-text-size');
    }, size);
    for (let i = 0; i < n; i++) {
      await page.evaluate(k => DL2Deck.go(k, 'back'), i); // back = all build parts shown
      const r = await page.evaluate(() => {
        const s = document.querySelector('.slide.is-active');
        const deck = document.querySelector('.deck').getBoundingClientRect();
        const strip = document.querySelector('.strip').getBoundingClientRect();
        const panel = s.querySelector('.panel');
        const box = panel.getBoundingClientRect();
        // The panel's clip-path hides anything past its edge, so content must also end inside the
        // panel (and above the phase strip on the full-bleed gorge slides).
        const limit = Math.min(box.bottom, strip.top);
        const live = [...s.querySelectorAll('*')].filter(e => !e.closest('.screen, .notes, [aria-hidden="true"]'));
        const inPanel = [...panel.querySelectorAll('*')].filter(e => !e.closest('.screen, [aria-hidden="true"]'));
        const name = e => e.tagName.toLowerCase() + (e.className && typeof e.className === 'string' ? '.' + e.className.trim().replace(/\s+/g, '.') : '');
        const pastDeck = live.filter(e => e.getBoundingClientRect().bottom > deck.bottom + 1).map(name);
        const pastPanel = inPanel.filter(e => { const b = e.getBoundingClientRect(); return b.height > 0 && b.bottom > limit + 1; }).map(name);
        return { pastDeck, pastPanel };
      });
      if (r.pastDeck.length || r.pastPanel.length) problems.push({ size: size || 'default', slide: i + 1, ...r });
    }
  }
  expect(problems).toEqual([]);
});
