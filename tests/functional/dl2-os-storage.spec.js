// A locked-down lab browser that refuses storage must not break the Week 1 deck or the pre-test.
// Replaces the retired 'DL2 works with blocked storage and reduced motion' case (tests/functional/dl2.spec.js),
// which drove the replaced week 1 deck and 28-question pre-test.
const { test, expect } = require('@playwright/test');
const Items = require('../../courses/digital-literacy-2/os/items.js');

test.beforeEach(async ({ page }) => {
  await page.addInitScript(() => {
    const blocked = () => { throw new Error('blocked'); };
    Storage.prototype.setItem = blocked; Storage.prototype.getItem = blocked; Storage.prototype.removeItem = blocked;
  });
  await page.emulateMedia({ reducedMotion: 'reduce' });
});

test('Week 1 deck moves on with blocked storage and reduced motion', async ({ page }) => {
  const errors = []; page.on('pageerror', e => errors.push(e.message));
  await page.goto('/courses/digital-literacy-2/weeks/week-01/presentation.html');
  await expect(page.locator('.strip .count')).toHaveText('1 / 27');
  await page.keyboard.press('ArrowRight');
  await expect(page.locator('.strip .count')).toHaveText('2 / 27');
  expect(errors).toEqual([]);
});

test('pre-test runs from name to graded result with blocked storage', async ({ page }) => {
  const errors = []; page.on('pageerror', e => errors.push(e.message));
  await page.route('**/', r => r.request().method() === 'POST' ? r.fulfill({ status: 200, body: 'ok' }) : r.continue());
  await page.goto('/courses/digital-literacy-2/assessments/pre-test.html');
  await page.getByLabel('Your full name').fill('James Doe');
  await page.getByRole('button', { name: 'Start the pre-test' }).click();
  for (let i = 0; i < 20; i++) {
    await page.locator(`.opt[data-letter="${Items.pre[i].answer}"]`).click();
    await page.getByRole('button', { name: i === 19 ? 'Review answers' : 'Next' }).click();
  }
  await page.getByRole('button', { name: 'Submit my test' }).click();
  await page.getByRole('button', { name: 'Yes, submit' }).click();
  await expect(page.locator('.result-score')).toContainText('20 of 20');
  await expect(page.locator('.copy-status')).toContainText('Your results were submitted for Britt');
  expect(errors).toEqual([]);
});
