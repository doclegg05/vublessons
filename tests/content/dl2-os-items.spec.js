// The DL2 pre-test and post-test are parallel: same skill, domain and week for each item number.
const { test, expect } = require('@playwright/test');
const path = require('path');
const OS = path.join(__dirname, '../../courses/digital-literacy-2/os');
const Items = require(path.join(OS, 'items.js'));
const Grade = require(path.join(OS, 'grade.js'));

test('20 items per form, parallel by number', () => {
  expect(Items.pre).toHaveLength(20);
  expect(Items.post).toHaveLength(20);
  Items.pre.forEach((p, i) => {
    const q = Items.post[i];
    expect(p.n).toBe(i + 1); expect(q.n).toBe(i + 1);
    expect(q.domain).toBe(p.domain); expect(q.week).toBe(p.week); expect(q.skill).toBe(p.skill);
    expect(q.stem).not.toBe(p.stem);
  });
});

test('domain counts match the blueprint', () => {
  const count = form => Items[form].reduce((m, it) => (m[it.domain] = (m[it.domain] || 0) + 1, m), {});
  const want = { tb: 3, dc: 3, im: 3, cc: 3, com: 3, col: 2, ss: 3 };
  expect(count('pre')).toEqual(want);
  expect(count('post')).toEqual(want);
  expect(Items.domains.map(d => d.id).sort()).toEqual(Object.keys(want).sort());
});

test('every item is well formed, answers are balanced', () => {
  for (const form of ['pre', 'post']) {
    const letters = { A: 0, B: 0, C: 0, D: 0 };
    for (const it of Items[form]) {
      expect(it.options).toHaveLength(4);
      expect(new Set(it.options).size).toBe(4);
      expect(['A', 'B', 'C', 'D']).toContain(it.answer);
      expect(it.stem.length).toBeGreaterThan(20);
      expect(it.why.length).toBeGreaterThan(20);
      expect([1, 2, 3, 4, 5]).toContain(it.week);
      letters[it.answer]++;
    }
    expect(letters).toEqual({ A: 5, B: 5, C: 5, D: 5 });
  }
});

test('grade counts correct answers overall and by domain', () => {
  const answers = Items.pre.map(it => it.answer);
  answers[0] = answers[0] === 'A' ? 'B' : 'A';
  answers[4] = null;
  const r = Grade.grade(Items.pre, answers);
  expect(r.correct).toBe(18); expect(r.total).toBe(20); expect(r.percent).toBe(90);
  expect(r.rows[4]).toMatchObject({ n: 5, chosen: null, correct: false });
  expect(r.rows[1].correct).toBe(true);
  const tb = r.byDomain.find(d => d.id === 'tb');
  expect(tb).toMatchObject({ correct: 2, total: 3, name: 'Technology Basics' });
});

test('record id is stable and readable', () => {
  const id = Grade.recordId('pre', new Date(2026, 8, 28, 16, 52), 'James  Doe');
  expect(id).toBe('DL2-PRE-20260928-1652-JD');
  expect(Grade.initials('cher')).toBe('C');
  expect(Grade.initials('')).toBe('X');
});

// I4 (final review): the record ID is built from the name, so initials take only the first A–Z letter
// of each name part (accents folded first) and fall back to 'X'. A record ID can never carry markup.
test('initials are letters only, so a record ID never carries markup', () => {
  const hostile = Grade.initials('<img src=x onerror=alert(1)>');
  expect(hostile).toMatch(/^[A-Z]{1,2}$/);
  expect(hostile).toBe('IO');
  expect(Grade.initials('<x onmouseover=window.__pwn=1 y')).toBe('XY');
  expect(Grade.initials('José Núñez−Smith')).toBe('JN');
  expect(Grade.initials('Émile  Zola')).toBe('EZ');
  expect(Grade.initials("  o'brien ")).toBe('O');
  expect(Grade.initials('123 !!! <>')).toBe('X');
  expect(Grade.recordId('pre', new Date(2026, 8, 28, 16, 52), '<b>Pat</b> Smith')).toBe('DL2-PRE-20260928-1652-BS');
});

// I1 (final review): the correct option was the longest on 18 of 20 items per form, so a test-wise learner could
// pass by picking the longest answer. Length must not point to the key: per form it is strictly the longest option
// on at most 6 items, never more than 1.3 × its longest distractor, and no option runs past 110 characters.
const LETTERS = ['A', 'B', 'C', 'D'];
const keyed = it => it.options[LETTERS.indexOf(it.answer)];
const longestDistractor = it => Math.max(...it.options.filter((_, k) => k !== LETTERS.indexOf(it.answer)).map(o => o.length));

for (const form of ['pre', 'post']) {
  test(`${form}: the correct option is strictly the longest on at most 6 of 20 items`, () => {
    const giveaways = Items[form].filter(it => keyed(it).length > longestDistractor(it)).map(it => it.n);
    expect(giveaways.length, `correct option is longest on items ${giveaways.join(', ')}`).toBeLessThanOrEqual(6);
  });

  test(`${form}: no correct option is more than 1.3 × its longest distractor`, () => {
    const over = Items[form].filter(it => keyed(it).length > 1.3 * longestDistractor(it))
      .map(it => `${it.n}: ${keyed(it).length} vs ${longestDistractor(it)}`);
    expect(over).toEqual([]);
  });

  test(`${form}: every option is at most 110 characters`, () => {
    const long = Items[form].flatMap(it => it.options.filter(o => o.length > 110).map(o => `${it.n}: ${o.length}`));
    expect(long).toEqual([]);
  });
}
