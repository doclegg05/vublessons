// Show engine: steps move a cursor, apply cumulative state, and Back rebuilds the previous state.
const { test, expect } = require('@playwright/test');
const BASE = 'http://localhost:3939/courses/digital-literacy-2/os/';
const html = `<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><base href="${BASE}">
<link rel="stylesheet" href="fonts.css"><link rel="stylesheet" href="deck.css"><link rel="stylesheet" href="win11.css"></head>
<body class="dl2-os"><div class="demo" data-demo="t-two" style="width:1200px"></div>
<script src="demo.js"></script>
<script>DL2Demo.define({ id:'t-two', title:'Test', scene:'<div class="w11-wall"></div><button id="b1" style="position:absolute;left:100px;top:100px;width:200px;height:60px">One</button><div id="lab" style="position:absolute;left:500px;top:300px">start</div>',
 steps:[{cap:'Start here.',check:'Start'},{cap:'Click <em>One</em>.',check:'Click One',target:'#b1',action:'click',state:{attr:{page:'two'},text:{'#lab':'clicked'}}},{cap:'Done.',check:'Done',state:{cls:{finished:true}}}]});</script>
</body></html>`;

async function open(page, opts = {}) {
  if (opts.reduced) await page.emulateMedia({ reducedMotion: 'reduce' });
  await page.goto(BASE + 'fonts.css');
  await page.setContent(html, { waitUntil: 'load' });
}

test('mounts with caption, counter and checklist', async ({ page }) => {
  await open(page);
  await expect(page.locator('.demo-stepno')).toHaveText('STEP 1 / 3');
  await expect(page.locator('.demo-cap')).toHaveText('Start here.');
  await expect(page.locator('.demo-todo li')).toHaveCount(3);
  await expect(page.locator('.demo-todo li.now')).toContainText('Start');
});

test('Next plays the click and applies state; Back restores it', async ({ page }) => {
  await open(page);
  await page.locator('[data-act="next"]').click();
  await expect(page.locator('.screen')).toHaveAttribute('data-page', 'two', { timeout: 8000 });
  await expect(page.locator('#lab')).toHaveText('clicked');
  await expect(page.locator('.demo-stepno')).toHaveText('STEP 2 / 3');
  await page.locator('[data-act="next"]').click();
  await expect(page.locator('.screen')).toHaveClass(/finished/, { timeout: 8000 });
  await page.locator('[data-act="back"]').click();
  await expect(page.locator('.screen')).not.toHaveClass(/finished/);
  await expect(page.locator('.screen')).toHaveAttribute('data-page', 'two');
  await page.locator('[data-act="replay"]').click();
  await expect(page.locator('#lab')).toHaveText('start');
  await expect(page.locator('.demo-stepno')).toHaveText('STEP 1 / 3');
});

test('reduced motion jumps straight to each state', async ({ page }) => {
  await open(page, { reduced: true });
  await page.locator('[data-act="next"]').click();
  await expect(page.locator('.screen')).toHaveAttribute('data-page', 'two', { timeout: 1000 });
});

test('controller refuses Next at the end so the deck can move on', async ({ page }) => {
  await open(page, { reduced: true });
  const r = await page.evaluate(() => { const c = DL2Demo.get('t-two'); return [c.next(), c.next(), c.next()]; });
  expect(r).toEqual([true, true, false]);
});

test('half speed button reports its state in words', async ({ page }) => {
  await open(page);
  const slow = page.locator('[data-act="slow"]');
  await slow.click();
  await expect(slow).toHaveAttribute('aria-pressed', 'true');
});
