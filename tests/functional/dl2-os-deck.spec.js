// Mission Control deck engine: builds before slides, phase strip, notes, no timer, no auto-advance.
const { test, expect } = require('@playwright/test');
const BASE = 'http://localhost:3939/courses/digital-literacy-2/os/';
const page3 = `<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><base href="${BASE}">
<link rel="stylesheet" href="fonts.css"><link rel="stylesheet" href="deck.css"></head><body class="dl2-os"><main class="deck">
<section class="slide" data-phase="warm-up" data-scene="gorge"><div class="panel center"><h1>One</h1></div><aside class="notes"><p>Say hello.</p></aside></section>
<section class="slide" data-phase="present" data-stage="tell"><div class="panel full"><div class="hud">WK-01</div><h1>Two</h1><ol class="steps"><li class="build">First</li><li class="build">Second</li></ol></div></section>
<section class="slide" data-phase="practice" data-stage="do" data-minutes="1"><div class="panel full"><h1>Three</h1></div></section>
</main><script src="deck.js"></script></body></html>`;

async function open(page) {
  await page.goto('http://localhost:3939/courses/digital-literacy-2/os/fonts.css'); // same origin for storage
  await page.setContent(page3, { waitUntil: 'load' });
}
const active = page => page.locator('.slide.is-active h1');

test('Next reveals build parts before moving on, and Back reverses', async ({ page }) => {
  await open(page);
  await expect(active(page)).toHaveText('One');
  await page.keyboard.press('ArrowRight');
  await expect(active(page)).toHaveText('Two');
  await expect(page.locator('.slide.is-active .build.on')).toHaveCount(0);
  await page.keyboard.press('PageDown');
  await expect(page.locator('.slide.is-active .build.on')).toHaveCount(1);
  await page.keyboard.press('Space');
  await expect(page.locator('.slide.is-active .build.on')).toHaveCount(2);
  await expect(page.locator('.slide.is-active .build.now')).toHaveText('Second');
  await page.keyboard.press('ArrowRight');
  await expect(active(page)).toHaveText('Three');
  await page.keyboard.press('ArrowLeft');
  await expect(active(page)).toHaveText('Two');
  await expect(page.locator('.slide.is-active .build.on')).toHaveCount(2);
  await page.keyboard.press('Home');
  await expect(active(page)).toHaveText('One');
  await page.keyboard.press('End');
  await expect(active(page)).toHaveText('Three');
});

test('phase strip, counter, stage tag and scene follow the slide', async ({ page }) => {
  await open(page);
  await expect(page.locator('.strip .seg.now')).toHaveText('Warm-up');
  await expect(page.locator('.strip .count')).toHaveText('1 / 3');
  await expect(page.locator('body')).toHaveAttribute('data-scene', 'gorge');
  await page.keyboard.press('ArrowRight');
  await expect(page.locator('.strip .seg.now')).toHaveText('Present');
  await expect(page.locator('.strip .seg.now')).toHaveAttribute('aria-current', 'step');
  await expect(page.locator('.strip .seg.done')).toHaveCount(2);
  await expect(page.locator('.slide.is-active .hud .tag')).toHaveText('TELL');
  await expect(page.locator('body')).toHaveAttribute('data-scene', 'deck');
});

test('N shows notes; typed number + Enter jumps; nothing auto-advances', async ({ page }) => {
  await open(page);
  await page.keyboard.press('n');
  await expect(page.locator('.notes-panel')).toBeVisible();
  await expect(page.locator('.notes-panel')).toContainText('Say hello.');
  await page.keyboard.press('n');
  await expect(page.locator('.notes-panel')).toBeHidden();
  await page.waitForTimeout(2500);
  await expect(active(page)).toHaveText('One');
  await page.keyboard.press('3');
  await page.keyboard.press('Enter');
  await expect(active(page)).toHaveText('Three');
});

// Britt paces by the room, not a clock: no countdown in the strip, and T does nothing.
test('no countdown timer anywhere, even after T on a Do slide', async ({ page }) => {
  await page.clock.install();
  await open(page);
  await page.keyboard.press('End');
  await page.keyboard.press('t');
  await page.clock.runFor(2000);
  await expect(page.locator('.strip [role="timer"], .strip .t, .timer')).toHaveCount(0);
  await expect(page.locator('.strip')).not.toContainText(/T-|TIME/);
  await expect(active(page)).toHaveText('Three');
});

test('a registered stepper consumes Next before the slide changes', async ({ page }) => {
  await open(page);
  await page.evaluate(() => {
    const s = document.querySelectorAll('.slide')[2]; let n = 0;
    window.DL2Deck.registerStepper(s, { next: () => (n < 2 ? (++n, true) : false), back: () => (n > 0 ? (--n, true) : false), reset: () => { n = 0; } });
    window.__steps = () => n;
  });
  await page.keyboard.press('End');
  await page.keyboard.press('ArrowRight');
  await page.keyboard.press('ArrowRight');
  expect(await page.evaluate(() => window.__steps())).toBe(2);
  await expect(active(page)).toHaveText('Three');
});

test('text-size host exists so no floating button is added', async ({ page }) => {
  await open(page);
  await expect(page.locator('.strip .vub-appbar .vub-textsize [data-vub-textsize-plus]')).toHaveCount(1);
});

// I3 (final review): the resume position lives in sessionStorage, so a fresh browser opens the real
// Week 1 deck at slide 1 even after a rehearsal left an old slide number in localStorage, while the
// same tab (a reload, or reopening the deck without #N) keeps its place.
test('a fresh open starts at slide 1; the same tab keeps its place', async ({ page, context }) => {
  const DECK = '/courses/digital-literacy-2/weeks/week-01/presentation.html';
  await page.goto(DECK);
  // A rehearsal on this machine left slide 20 behind under the old localStorage key.
  await page.evaluate(() => { localStorage.setItem('dl2os:slide:' + location.pathname, '19'); });
  const deck = await context.newPage(); // a fresh browser tab
  await deck.goto(DECK);
  await expect(deck.locator('.strip .count')).toHaveText('1 / 27');
  await deck.keyboard.press('5');
  await deck.keyboard.press('Enter');
  await expect(deck.locator('.strip .count')).toHaveText('5 / 27');
  await deck.goto(DECK); // no #N: same tab, so it resumes
  await expect(deck.locator('.strip .count')).toHaveText('5 / 27');
  const fresh = await context.newPage(); // another new tab starts a new session
  await fresh.goto(DECK);
  await expect(fresh.locator('.strip .count')).toHaveText('1 / 27');
});

// Final review minor: the old decks recorded each slide through shared/progress.js (VubProgress.saveSlide
// ('dl2', week, slide, total)), which the course home reads for courses.json's statusKey dl2:w1. The Mission
// Control deck records Week 1 the same way.
test('opening the Week 1 deck shows on the course home, and the last slide marks it viewed', async ({ page }) => {
  const DECK = '/courses/digital-literacy-2/weeks/week-01/presentation.html', HOME = '/courses/digital-literacy-2/index.html';
  await page.goto(HOME);
  await page.evaluate(() => localStorage.clear());
  await page.reload();
  await expect(page.locator('[data-week-status="1"]')).toHaveText('Ready to begin');
  await page.goto(DECK);
  await expect(page.locator('.strip .count')).toHaveText('1 / 27');
  await expect.poll(() => page.evaluate(() => {
    const p = JSON.parse(localStorage.getItem('vub:progress:v1') || '{}');
    return p.dl2 && p.dl2['1'] && [p.dl2['1'].slide, p.dl2['1'].total];
  })).toEqual([0, 27]);
  await page.goto(HOME);
  await expect(page.locator('[data-week-status="1"]')).toHaveText('Resume at slide 1');
  await expect(page.locator('.continue-course')).toHaveText('Continue week 1');
  await page.goto(DECK);
  await page.keyboard.press('End');
  await expect(page.locator('.strip .count')).toHaveText('27 / 27');
  await page.goto(HOME);
  await expect(page.locator('[data-week-status="1"]')).toHaveText('Lesson viewed to the end');
  await expect(page.locator('[data-course-count]')).toHaveText('1 of 6 lessons viewed to the end');
});
