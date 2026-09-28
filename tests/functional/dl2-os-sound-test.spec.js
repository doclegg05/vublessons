// Mission 1B headset sound test: a letterhead page whose one big button plays a three-note chime with Web Audio.
const { test, expect } = require('@playwright/test');
const URL = '/courses/digital-literacy-2/weeks/week-01/files/sound-test.html';

test.beforeEach(async ({ page }) => {
  // Record every note the page starts, on the real Web Audio API.
  await page.addInitScript(() => {
    window.__notes = [];
    const start = OscillatorNode.prototype.start;
    OscillatorNode.prototype.start = function (when) { window.__notes.push({ f: this.frequency.value, t: when || 0 }); return start.apply(this, arguments); };
  });
});

test('one keyboard press plays three rising notes and says so in words', async ({ page }) => {
  await page.goto(URL);
  await expect(page.locator('h1')).toHaveText('Headset sound test');
  await expect(page.locator('main')).toContainText('Put your headset on. Click the button. You should hear three notes in your headset, not the speakers.');
  const play = page.getByRole('button', { name: 'Play test sound' });
  await play.focus();
  await page.keyboard.press('Enter');
  await expect.poll(() => page.evaluate(() => window.__notes.length)).toBe(3);
  const notes = await page.evaluate(() => window.__notes);
  expect(notes[0].f).toBeLessThan(notes[1].f);
  expect(notes[1].f).toBeLessThan(notes[2].f);
  expect(notes[0].t).toBeLessThan(notes[1].t);
  expect(notes[1].t).toBeLessThan(notes[2].t);
  await expect(page.getByRole('status')).toContainText('three notes');
  await play.click();
  await expect.poll(() => page.evaluate(() => window.__notes.length)).toBe(6);
});

test('letterhead page, no media files or outside requests, text-size script last', async ({ page }) => {
  const outside = [];
  page.on('request', r => { if (!r.url().startsWith('http://localhost:3939/')) outside.push(r.url()); });
  await page.goto(URL);
  await expect(page.locator('.letterhead')).toContainText('New River Community and Technical College');
  await expect(page.locator('audio, video, source')).toHaveCount(0);
  expect(await page.evaluate(() => [...document.scripts].pop().getAttribute('src'))).toBe('/shared/text-size.js');
  expect(outside).toEqual([]);
});
