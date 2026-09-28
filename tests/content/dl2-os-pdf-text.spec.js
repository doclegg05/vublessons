// Every string the results PDF draws must survive pdf-lib's StandardFonts (WinAnsi) fallback, which throws on any
// character outside its encoding. The real os/pdf.js clean() is exercised (exposed as DL2Pdf._clean) in the page that
// ships it, over the whole item bank, the letterhead and the report's fixed text, plus hostile samples.
const { test, expect } = require('@playwright/test');

test('clean() makes every PDF string encodable in the WinAnsi fallback fonts', async ({ page }) => {
  await page.goto('/courses/digital-literacy-2/assessments/pre-test.html');
  const out = await page.evaluate(async () => {
    const L = window.PDFLib, I = window.DL2Items, P = window.DL2Paper, clean = window.DL2Pdf && window.DL2Pdf._clean;
    if (typeof clean !== 'function') return { missing: true };
    const M = P.META, LETTERS = ['A', 'B', 'C', 'D'];
    const t = d => d.toLocaleTimeString('en-US', { hour: 'numeric', minute: '2-digit' });
    const started = new Date(2026, 8, 28, 16, 31), submitted = new Date(2026, 8, 28, 16, 52);
    const strings = [];
    for (const form of ['pre', 'post']) {
      const label = form === 'pre' ? 'Pre-Test' : 'Post-Test';
      strings.push(label + ' · Graded Results', M.org + ' · ' + label + ' · Graded Results (continued)',
        'Form: ' + form + ' ' + I.version + ' · 20 items');
      for (const it of I[form]) {
        strings.push(it.skill, it.stem, it.why);
        it.options.forEach((o, k) => strings.push(LETTERS[k] + ' · ' + o));
      }
    }
    I.domains.forEach(d => strings.push(d.name));
    strings.push(M.state.split('').join(' '), M.org, M.trio, M.course, M.cohort, M.instructor, M.location,
      P.classDate(submitted), 'Not answered', 'Instructor signature · ' + M.instructor,
      t(started) + ' / ' + t(submitted) + ' (21 min)', 'Page 1 of 2 · Record DL2-PRE-20260928-1652-JD',
      'Scores guide practice. They are not a certification.');
    const hostile = ['−3 points', '4:30 PM', 'José 🙂 Núñez', '李 Wei', 'O’Brien–Smith', 'tab\there', '✓ Correct ✗ ⚠', 'a​b'];
    const fonts = {};
    const doc = await L.PDFDocument.create();
    for (const name of ['Helvetica', 'HelveticaBold', 'TimesRomanBold']) fonts[name] = await doc.embedFont(L.StandardFonts[name]);
    const failures = [];
    for (const s of strings.concat(hostile)) for (const [name, font] of Object.entries(fonts)) {
      try { font.encodeText(clean(s)); } catch (e) { failures.push(name + ': ' + JSON.stringify(s) + ' -> ' + e.message); }
    }
    // The bank's words must survive untouched: only symbols may be mapped or dropped.
    const alnum = s => s.replace(/[^A-Za-z0-9]/g, '');
    const lostWords = strings.filter(s => alnum(clean(s)) !== alnum(s));
    return { count: strings.length, failures, lostWords,
      samples: { minus: clean('−3 points'), nnbsp: clean('4:30 PM'), accents: clean('José Núñez'), emoji: clean('José 🙂 Núñez') } };
  });
  expect(out.missing, 'DL2Pdf._clean is exposed for testing').toBeUndefined();
  expect(out.count).toBeGreaterThan(200);
  expect(out.failures).toEqual([]);
  expect(out.lostWords).toEqual([]);
  expect(out.samples).toEqual({ minus: '-3 points', nnbsp: '4:30 PM', accents: 'José Núñez', emoji: 'José  Núñez' });
});
