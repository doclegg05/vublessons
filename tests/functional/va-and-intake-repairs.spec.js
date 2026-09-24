const { test, expect } = require('@playwright/test');
const AxeBuilder = require('@axe-core/playwright').default;
const fs = require('fs');
const path = require('path');

const root = path.join(__dirname, '../..');

test('VA teaching and handouts direct learners to current sign-in and health tools', async ({ page }) => {
  const lessonPath = '/courses/computer-skills/weeks/week-01/presentation.html';
  await page.goto(lessonPath);
  await page.locator('.slide-link[data-slide="4"]').click();
  const slide = page.locator('.slide.active');
  await expect(slide).toContainText('Two supported sign-in choices');
  await expect(slide).toContainText('Login.gov');
  await expect(slide).toContainText('ID.me');
  await expect(slide).toContainText('no longer sign you in to VA services');
  await expect(slide.getByRole('link', { name: 'VA sign-in guidance' })).toHaveAttribute('href', 'https://www.va.gov/initiatives/prepare-for-vas-secure-sign-in-changes/');

  const files = [lessonPath.slice(1), 'courses/computer-skills/weeks/week-01/handouts/myhealthevet-guide.html', 'courses/computer-skills/weeks/week-01/handouts/va-portals-quick-reference.html'];
  for (const file of files) {
    const source = fs.readFileSync(path.join(root, file), 'utf8');
    expect(source, file).toContain('va.gov/health-care/manage-health/');
    expect(source, file).not.toMatch(/still work fine|Use Login.gov, ID.me, or DS Logon|www\.myhealth\.va\.gov/);
  }
});

test('intake confirmation action resolves and displays success without sending form data', async ({ page }) => {
  const posts = [];
  page.on('request', request => { if (request.method() === 'POST') posts.push(request.url()); });
  await page.goto('/instructors/intake.html');
  await expect(page.locator('#intakeForm')).toBeVisible();
  await expect(page.locator('#successPane')).toBeHidden();
  const action = await page.locator('#intakeForm').getAttribute('action');
  expect(action).toBe('/instructors/intake?success=1');
  const response = await page.goto(action);
  expect(response.status()).toBe(200);
  await expect(page).toHaveURL(/\/instructors\/intake\?success=1$/);
  await expect(page.locator('#successPane')).toBeVisible();
  await expect(page.locator('#intakeForm')).toBeHidden();
  expect(posts).toEqual([]);
});

for (const route of ['/instructors/intake.html', '/instructors/classes/']) {
  test(`instructor footer contrast meets AA: ${route}`, async ({ page }) => {
    await page.goto(route);
    await page.locator('footer').scrollIntoViewIfNeeded();
    const result = await new AxeBuilder({ page }).include('footer').withRules(['color-contrast']).analyze();
    expect(result.violations).toEqual([]);
  });
}
