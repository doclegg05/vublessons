// Mission Control deck engine: builds before slides, phase strip, notes, timer, no auto-advance.
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

test('Do-slide timer counts down after T and says TIME\'S UP in words', async ({ page }) => {
  await page.clock.install();
  await open(page);
  await page.keyboard.press('End');
  await expect(page.locator('.strip .t')).toHaveText('T-01:00');
  await page.keyboard.press('t');
  await page.clock.runFor(2000);
  await expect(page.locator('.strip .t')).toHaveText('T-00:58');
  await page.clock.runFor(60000);
  await expect(page.locator('.strip .t')).toHaveText("TIME'S UP");
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
