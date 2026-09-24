// Reflow and keyboard regressions for all eight legacy Computer Skills decks.
const { test, expect } = require('@playwright/test');

for (let week = 1; week <= 8; week++) {
  const route = `/courses/computer-skills/weeks/week-${String(week).padStart(2, '0')}/presentation.html`;
  test(`Computer Skills week ${week}: every slide reflows with readable and enlarged text`, async ({ page }) => {
    await page.emulateMedia({ reducedMotion: 'reduce' });
    await page.goto(route);
    const count = await page.locator('.slide').count();
    for (const width of [320, 390]) {
      await page.setViewportSize({ width, height: 844 });
      for (const size of ['', 'xxl']) {
        await page.evaluate(value => VubTextSize.apply(value), size);
        for (let index = 0; index < count; index++) {
          // Exercise each deck's real chapter handler; the collapsed menu is
          // opened and tested with native keyboard actions in the next test.
          await page.evaluate(i => document.querySelector(`.slide-link[data-slide="${i}"], .slide-item[data-slide="${i}"]`).click(), index);
          const metrics = await page.evaluate(() => {
            const active = document.querySelector('.slide.active');
            const text = [...active.querySelectorAll('p,li,td,th')].filter(node => node.getBoundingClientRect().height);
            return {
              documentWidth: document.documentElement.scrollWidth,
              contentOutside: [...active.querySelectorAll('*')].filter(node => {
                const rect = node.getBoundingClientRect();
                return rect.width && rect.right > innerWidth + 1 && !node.closest('.ics-table-scroll');
              }).map(node => node.className || node.tagName),
              fontSizes: text.map(node => parseFloat(getComputedStyle(node).fontSize)),
              controls: [...document.querySelectorAll('#prevBtn, #nextBtn')].map(node => {
                const rect = node.getBoundingClientRect();
                return { left: rect.left, right: rect.right, height: rect.height };
              }),
            };
          });
          const context = `week ${week}, slide ${index + 1}, width ${width}, size ${size || 'default'}`;
          expect(metrics.documentWidth, context).toBeLessThanOrEqual(width + 1);
          expect(metrics.contentOutside, context).toEqual([]);
          expect(metrics.fontSizes.every(value => value >= (size ? 44 : 32)), context).toBeTruthy();
          for (const control of metrics.controls) {
            expect(control.left, context).toBeGreaterThanOrEqual(0);
            expect(control.right, context).toBeLessThanOrEqual(width + 1);
            expect(control.height, context).toBeGreaterThanOrEqual(44);
          }
        }
      }
    }
  });

  test(`Computer Skills week ${week}: menu and text controls work by keyboard`, async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto(route);
    const menu = page.getByRole('button', { name: 'Lesson menu', exact: true });
    const sidebar = page.getByRole('navigation', { name: 'Lesson chapters' });
    const activeIndex = () => page.locator('.slide').evaluateAll(slides => slides.findIndex(slide => slide.classList.contains('active')));
    await expect(sidebar).toBeHidden();
    await menu.focus();
    await page.keyboard.press('Space');
    await expect(sidebar).toBeVisible();
    await expect(menu).toHaveAttribute('aria-expanded', 'true');
    await expect(menu).toBeFocused();
    expect(await menu.evaluate(node => getComputedStyle(node).outlineStyle)).not.toBe('none');
    await page.keyboard.press('Escape');
    await expect(sidebar).toBeHidden();
    await expect(menu).toBeFocused();
    const initial = await activeIndex();
    const increase = page.getByRole('button', { name: 'Increase text size' });
    await increase.focus();
    await page.keyboard.press('Space');
    await expect(page.locator('html')).toHaveAttribute('data-text-size', 'lg');
    expect(await activeIndex()).toBe(initial);
    // The glossary and text-size controls must not cover one another.
    const noOverlap = await page.evaluate(() => {
      const a = document.querySelector('.vub-textsize-fab').getBoundingClientRect();
      const b = document.querySelector('.vub-help-fab').getBoundingClientRect();
      return a.right <= b.left || b.right <= a.left || a.bottom <= b.top || b.bottom <= a.top;
    });
    expect(noOverlap).toBeTruthy();
    await page.getByRole('button', { name: 'Open glossary and quick help' }).click();
    const help = page.getByRole('dialog');
    await expect(help).toBeVisible();
    await page.getByRole('searchbox', { name: 'Search glossary terms' }).focus();
    await page.keyboard.press('Space');
    expect(await activeIndex()).toBe(initial);
    await page.keyboard.press('Escape');
    await expect(help).toBeHidden();
    await page.evaluate(() => document.activeElement.blur());
    await page.keyboard.press('Home');
    expect(await activeIndex()).toBe(0);
    await page.keyboard.press('PageDown');
    expect(await activeIndex()).toBe(1);
    await menu.click();
    // Week 2 nests slide buttons under collapsible chapter buttons.
    await page.locator('.chapter-item').evaluateAll(chapters => chapters.forEach(chapter => chapter.classList.add('expanded')));
    const lastLink = sidebar.locator('.slide-link, .slide-item').last();
    await lastLink.click();
    expect(await activeIndex()).toBe(await page.locator('.slide').count() - 1);
    await expect(sidebar).toBeHidden();
    await expect(menu).toBeFocused();
    await page.setViewportSize({ width: 1440, height: 900 });
    await expect(sidebar).toBeVisible();
    await expect(menu).toBeHidden();
    await expect(sidebar.locator('.resource-link').last()).toBeAttached();
  });
}

test('Computer Skills tables scroll by keyboard without changing slides', async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto('/courses/computer-skills/weeks/week-05/presentation.html');
  const tableSlide = await page.locator('.slide').evaluateAll(slides => slides.findIndex(slide => slide.querySelector('table')));
  expect(tableSlide).toBeGreaterThanOrEqual(0);
  await page.evaluate(index => document.querySelector(`.slide-link[data-slide="${index}"]`).click(), tableSlide);
  const table = page.locator('.slide.active .ics-table-scroll').first();
  await table.focus();
  await page.keyboard.press('ArrowRight');
  await expect.poll(() => table.evaluate(node => node.scrollLeft)).toBeGreaterThan(0);
  expect(await page.locator('.slide').evaluateAll(slides => slides.findIndex(slide => slide.classList.contains('active')))).toBe(tableSlide);
});
