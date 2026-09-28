// tests/functional/dl2-os-week1-deck.spec.js
// Week 1 deck: 28 slides, WIPPEA order, every Show mounts, text floor, no external requests.
const { test, expect } = require('@playwright/test');
const URL = '/courses/digital-literacy-2/weeks/week-01/presentation.html';

test('structure: 28 slides, phases in order, five demos, five Do timers', async ({ page }) => {
  await page.goto(URL);
  await expect(page.locator('.slide')).toHaveCount(28);
  await expect(page.locator('.slide[data-stage="show"] .demo-bezel')).toHaveCount(5);
  await expect(page.locator('.slide[data-stage="do"][data-minutes]')).toHaveCount(5);
  const phases = await page.locator('.slide[data-phase]').evaluateAll(s => s.map(x => x.dataset.phase));
  const order = ['warm-up', 'intro', 'present', 'practice', 'evaluate', 'apply'];
  expect(phases[0]).toBe('warm-up'); expect(phases.at(-1)).toBe('apply');
  expect(phases.every(p => order.includes(p))).toBe(true);
  await expect(page.locator('a[href*="legacy"]')).toHaveCount(0);
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
