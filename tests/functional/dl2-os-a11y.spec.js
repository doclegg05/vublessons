// Automated accessibility scan (axe) of the Mission Control page types: deck, letterhead missions, run sheet, sound test,
// the pre/post test and an answer key. Serious and critical findings fail the test.
const { test, expect } = require('@playwright/test');
const AxeBuilder = require('@axe-core/playwright').default;

const PAGES = [
  'weeks/week-01/presentation.html',
  'weeks/week-01/worksheet.html',
  'weeks/week-01/run-sheet.html',
  'weeks/week-01/files/sound-test.html',
  'assessments/pre-test.html',
  'assessments/post-test.html',
  'assessments/pre-test-answer-key.html',
];

for (const p of PAGES) test(`axe: ${p}`, async ({ page }) => {
  await page.goto('/courses/digital-literacy-2/' + p);
  await page.evaluate(() => document.fonts.ready);
  const r = await new AxeBuilder({ page }).disableRules(['region']).analyze();
  const bad = r.violations.filter(v => ['serious', 'critical'].includes(v.impact));
  expect(bad.map(v => ({ id: v.id, nodes: v.nodes.map(n => n.target) }))).toEqual([]);
});

// The "Not you? Start over" note on a resumed test (final review I5).
test('axe: pre-test resumed on a shared PC', async ({ page }) => {
  await page.goto('/courses/digital-literacy-2/assessments/pre-test.html');
  await page.evaluate(() => {
    localStorage.clear();
    localStorage.setItem('dl2os:test:pre', JSON.stringify({ phase: 'q', name: 'Pat Smith', started: new Date().toISOString(), at: 0, answers: Array(20).fill(null) }));
  });
  await page.reload();
  await expect(page.locator('.resume-note')).toBeVisible();
  await page.evaluate(() => document.fonts.ready);
  const r = await new AxeBuilder({ page }).disableRules(['region']).analyze();
  const bad = r.violations.filter(v => ['serious', 'critical'].includes(v.impact));
  expect(bad.map(v => ({ id: v.id, nodes: v.nodes.map(n => n.target) }))).toEqual([]);
});
