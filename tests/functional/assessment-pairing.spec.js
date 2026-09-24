const { test, expect } = require('@playwright/test');
const fs = require('fs');
const courses = [
  { id: 'ICS', post: '/courses/computer-skills/weeks/week-08/post-test.html', preKey: 'vub_pretest_results', postKey: 'vub_posttest_results' },
  { id: 'DL1', post: '/courses/digital-literacy-1/assessments/post-test.html', preKey: 'vub_dl1_pretest_results', postKey: 'vub_dl1_posttest_results' }
];
async function open(page, course, name = 'Learner Alpha TEST') {
  await page.goto(course.post);
  await page.evaluate(({ preKey, name }) => localStorage.setItem(preKey, JSON.stringify({ name, date: '9/1/2026', timestamp: '2026-09-01T12:00:00.000Z', score: 20 })), { preKey: course.preKey, name });
  await page.reload();
  await expect(page.locator('#participantName')).toHaveValue('');
  await page.locator('#instructorName').fill('QA Instructor');
  await expect(page.locator('#pairingSummary')).not.toContainText(name);
  await page.getByRole('button', { name: 'Find my saved pre-test' }).click();
}
async function finish(page) {
  await page.locator('#btnStart').click();
  // Pairing is under test; use the actual grading path with a known answer set.
  await page.evaluate(() => { questions.forEach(q => { answers[q.id] = q.correct; }); submitQuiz(); });
  await expect(page.locator('#finalScore')).toHaveText('100%');
}
async function verify(page, course, paired) {
  const result = await page.evaluate(key => ({ saved: JSON.parse(localStorage.getItem(key)), report: window.quizResults }), course.postKey);
  for (const value of Object.values(result)) {
    expect(value.preTestScore).toBe(paired ? 20 : null);
    if (paired) {
      expect(value.preTestAttempt.name).toBe('Learner Alpha TEST');
      expect(value.preTestAttempt.timestamp).toBe('2026-09-01T12:00:00.000Z');
      expect(value.preTestAttempt.confirmedAt).toBeTruthy();
    } else expect(value.preTestAttempt).toBeNull();
  }
  if (paired) await expect(page.locator('#preTestScore')).toHaveText('20%');
  else await expect(page.locator('#comparisonBox')).toContainText('No pre-test attempt was confirmed');
  await page.evaluate(() => { window.print = () => {}; generateReport(); });
  await expect(page.locator('#reportPairingNote')).toContainText(paired ? 'Compared with the pre-test you confirmed' : 'No pre-test comparison');
  expect(await page.locator('#reportComparison').evaluate(el => el.style.display)).toBe(paired ? 'block' : 'none');
  if (course.id === 'DL1') {
    const pending = page.waitForEvent('download');
    await page.getByRole('button', { name: 'Download Results (CSV)' }).click();
    const csv = fs.readFileSync(await (await pending).path(), 'utf8');
    const fields = csv.split('\r\n')[1].split(',');
    expect(fields[6]).toBe(paired ? '"20"' : '""');
    expect(fields[7]).toBe(paired ? '"80"' : '""');
  }
}
for (const course of courses) {
  test(`${course.id}: different learner and unconfirmed same-name learner never inherit a comparison`, async ({ page }) => {
    for (const name of ['Learner Beta TEST', 'Learner Alpha TEST']) {
      await open(page, course);
      await page.locator('#participantName').fill(name);
      await expect(page.locator('#confirmPretest')).not.toBeChecked();
      if (name.includes('Beta')) await expect(page.locator('#confirmPretest')).toBeDisabled();
      await finish(page);
      await verify(page, course, false);
    }
  });
  test(`${course.id}: deliberate attempt pairing reaches results, saved data, export, and print`, async ({ page }) => {
    await open(page, course);
    await page.locator('#participantName').fill('Learner Alpha TEST');
    await expect(page.locator('#pairingSummary')).toContainText('9/1/2026 · 20%');
    await page.locator('#confirmPretest').check();
    await finish(page);
    await verify(page, course, true);
  });
  test(`${course.id}: completed results keep their confirmed baseline after storage changes`, async ({ page }) => {
    await open(page, course);
    await page.locator('#participantName').fill('Learner Alpha TEST');
    await page.locator('#confirmPretest').check();
    await finish(page);
    await page.evaluate(key => localStorage.setItem(key, JSON.stringify({name:'Another learner', date:'9/3/2026', score:90})), course.preKey);
    await verify(page, course, true);
  });
  test(`${course.id}: editing identity and replacing a saved attempt invalidate confirmation`, async ({ page }) => {
    await open(page, course);
    await page.locator('#participantName').fill('Learner Alpha TEST');
    await page.locator('#confirmPretest').check();
    await page.locator('#participantName').fill('Learner Beta TEST');
    await page.locator('#participantName').fill('Learner Alpha TEST');
    await expect(page.locator('#confirmPretest')).not.toBeChecked();
    await page.locator('#confirmPretest').check();
    await page.locator('#instructorName').fill('Another QA Instructor');
    await expect(page.locator('#confirmPretest')).not.toBeChecked();
    await page.locator('#confirmPretest').check();
    await page.locator('#btnStart').click();
    await page.evaluate(key => localStorage.setItem(key, JSON.stringify({ name: 'Learner Alpha TEST', date: '9/2/2026', score: 80 })), course.preKey);
    await page.evaluate(() => { questions.forEach(q => { answers[q.id] = q.correct; }); submitQuiz(); });
    await verify(page, course, false);
  });
  test(`${course.id}: malformed saved results cannot create a comparison`, async ({ page }) => {
    await page.goto(course.post);
    for (const bad of ['invalid JSON', JSON.stringify({name:'Learner Alpha TEST',score:120}), JSON.stringify({name:'Learner Alpha TEST',score:'20'})]) {
      await page.evaluate(({key,bad}) => localStorage.setItem(key,bad), {key:course.preKey,bad});
      await page.reload();
      await page.locator('#participantName').fill('Learner Alpha TEST');
      await expect(page.locator('#confirmPretest')).toBeDisabled();
      await expect(page.locator('#pairingSummary')).toContainText('No usable pre-test');
      expect(await page.evaluate(() => window.assessmentPairing.getConfirmed())).toBeNull();
    }
  });
  test(`${course.id}: new learner clears only this course's saved results`, async ({ page }) => {
    await open(page, course);
    await page.evaluate(key => { localStorage.setItem(key, '{"old":true}'); localStorage.setItem('unrelated-course', 'keep'); }, course.postKey);
    await page.getByRole('button', { name: 'New learner: clear saved assessment results' }).click();
    expect(await page.evaluate(c => [localStorage.getItem(c.preKey), localStorage.getItem(c.postKey), localStorage.getItem('unrelated-course')], course)).toEqual([null, null, 'keep']);
    await expect(page.locator('#confirmPretest')).toBeDisabled();
    await expect(page.locator('#participantName')).toBeFocused();
  });
}
for (const kind of ['pre', 'post']) test(`DL1 ${kind}: print excludes hidden quiz layout and keeps the full report`, async ({ page }, testInfo) => {
  await page.goto(`/courses/digital-literacy-1/assessments/${kind}-test.html`);
  await page.locator('#participantName').fill('A learner with a deliberately long name for report wrapping TEST');
  await page.locator('#instructorName').fill('QA Instructor');
  await finish(page);
  await page.evaluate(() => { window.print = () => {}; generateReport(); });
  await page.emulateMedia({ media: 'print' });
  await expect(page.locator('#resultsSection')).toHaveCSS('display', 'none');
  await expect(page.locator('#quizSection')).toHaveCSS('display', 'none');
  await expect(page.locator('#printReport')).toHaveCSS('position', 'static');
  await expect(page.locator('#printReport')).toBeVisible();
  await expect(page.locator('#reportTableBody tr')).toHaveCount(20);
  for (const format of ['Letter', 'A4']) {
    const pdf = await page.pdf({ path: testInfo.outputPath(`${kind}-${format}.pdf`), format, printBackground: true });
    expect(pdf.length).toBeGreaterThan(10000);
    // A fixed 20-question report fits three sheets; the prior hidden quiz added two blank sheets.
    expect((pdf.toString('latin1').match(/\/Type \/Page\b/g) || []).length).toBe(3);
  }
});
