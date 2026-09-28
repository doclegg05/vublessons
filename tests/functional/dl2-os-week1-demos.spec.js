// tests/functional/dl2-os-week1-demos.spec.js
// Every Week 1 demo plays to its last step with every target present and no console errors.
const { test, expect } = require('@playwright/test');
const BASE = 'http://localhost:3939/courses/digital-literacy-2/os/';
const IDS = ['w1-scale', 'w1-sound', 'w1-print', 'w1-calendar', 'w1-autocorrect'];

for (const id of IDS) test(`${id} runs to the end`, async ({ page }) => {
  const errors = [];
  page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
  page.on('pageerror', e => errors.push(e.message));
  await page.emulateMedia({ reducedMotion: 'reduce' });
  await page.goto(BASE + 'fonts.css');
  await page.setContent(`<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><base href="${BASE}">
    <link rel="stylesheet" href="fonts.css"><link rel="stylesheet" href="deck.css"><link rel="stylesheet" href="win11.css"></head>
    <body class="dl2-os"><div class="demo" data-demo="${id}" style="width:1600px;height:700px"></div>
    <script src="demo.js"></script><script src="demos/week-01.js"></script></body></html>`, { waitUntil: 'load' });
  const total = await page.locator('.demo-todo li').count();
  expect(total).toBeGreaterThanOrEqual(5);
  for (let i = 1; i < total; i++) {
    await page.locator('[data-act="next"]').click();
    await expect(page.locator('.demo-stepno')).toHaveText(`STEP ${i + 1} / ${total}`);
  }
  expect(await page.evaluate(k => DL2Demo.get(k).next(), id)).toBe(false);
  expect(errors).toEqual([]);
});

test('scale demo ends at 125% with a bigger window', async ({ page }) => {
  await page.emulateMedia({ reducedMotion: 'reduce' });
  await page.goto(BASE + 'fonts.css');
  await page.setContent(`<!DOCTYPE html><html><head><base href="${BASE}"><link rel="stylesheet" href="win11.css"></head><body><div class="demo" data-demo="w1-scale" style="width:1600px"></div><script src="demo.js"></script><script src="demos/week-01.js"></script></body></html>`, { waitUntil: 'load' });
  for (let i = 0; i < 4; i++) await page.locator('[data-act="next"]').click();
  await expect(page.locator('#scale-val')).toHaveText('125%');
});

// Final review minor: two w1-calendar steps shared one caption, so Next seemed to do nothing. Every step's
// caption changes on Next, in every Week 1 demo.
test('every Week 1 demo step has its own caption', async ({ page }) => {
  await page.goto(BASE + 'fonts.css');
  await page.setContent(`<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><base href="${BASE}"></head><body>
    <script src="demo.js"></script>
    <script>window.__defs = []; var define = DL2Demo.define; DL2Demo.define = function (d) { __defs.push(d); return define(d); };</script>
    <script src="demos/week-01.js"></script></body></html>`, { waitUntil: 'load' });
  const defs = await page.evaluate(() => __defs.map(d => ({ id: d.id, caps: d.steps.map(s => s.cap), checks: d.steps.map(s => s.check) })));
  expect(defs.map(d => d.id)).toEqual(IDS);
  for (const d of defs) expect(new Set(d.caps).size, d.id).toBe(d.caps.length);
  const cal = defs.find(d => d.id === 'w1-calendar');
  expect(cal.caps.slice(3, 5)).toEqual(['Open the <em>Repeat</em> menu.', 'Choose <em>Weekly on Monday</em>.']);
  expect(cal.checks.slice(3, 5)).toEqual(['Make it repeat', 'Weekly on Monday']);
});
