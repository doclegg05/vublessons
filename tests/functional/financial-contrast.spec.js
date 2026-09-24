const { test, expect } = require('@playwright/test');
const { AxeBuilder } = require('@axe-core/playwright');

for (const theme of ['light', 'dark']) {
  test(`Financial Readiness pre-test link stays readable in ${theme} mode and on hover`, async ({ page }) => {
    await page.addInitScript((value) => localStorage.setItem('theme', value), theme);
    await page.goto('/courses/financial-readiness/financial-readiness.html');
    await expect(page.locator('body')).toHaveClass(new RegExp(`${theme}-mode`));
    const link = page.locator('.btn-pre-test');
    await expect(link).toBeVisible();
    for (const hovered of [false, true]) {
      if (hovered) await link.hover();
      await page.evaluate(async () => {
        await document.fonts.ready;
        for (const animation of document.getAnimations()) {
          if (Number.isFinite(animation.effect?.getComputedTiming().endTime)) animation.finish();
        }
      });
      const audit = await new AxeBuilder({ page }).include('.btn-pre-test').withRules(['color-contrast']).analyze();
      expect(audit.violations, `${theme}, hovered=${hovered}`).toEqual([]);
    }
  });
}
