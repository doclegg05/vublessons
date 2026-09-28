// Automated accessibility scan (axe) of the Mission Control page types: deck, letterhead missions, run sheet,
// the pre/post test and an answer key. Serious and critical findings fail the test.
const { test, expect } = require('@playwright/test');
const AxeBuilder = require('@axe-core/playwright').default;

const PAGES = [
  'weeks/week-01/presentation.html',
  'weeks/week-01/worksheet.html',
  'weeks/week-01/run-sheet.html',
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
