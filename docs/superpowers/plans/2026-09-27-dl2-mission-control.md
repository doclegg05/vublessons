# DL2 Mission Control: Phase 1 Implementation Plan (Week 1 + tests, for Mon Sep 28)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship the new DL2 "Mission Control" system for Week 1: deck engine, Windows 11 Show engine with five Week 1 demos, the Week 1 deck, printable missions 1A–1E with a run sheet and answer key, and 20-question parallel pre-tests and post-tests that grade locally, save a letterhead PDF, and send a copy to Netlify Forms.

**Architecture:** Hand-written HTML pages plus a small shared engine in `courses/digital-literacy-2/os/` (plain ES5-compatible JavaScript IIFEs exposing `window.DL2Deck`, `window.DL2Demo`, `window.DL2Items`, `window.DL2Grade`, `window.DL2Paper`, `window.DL2Pdf`). No framework, no CDN. pdf-lib and @pdf-lib/fontkit are vendored. Pure logic (`items.js`, `grade.js`) is UMD so Node tests can `require` it.

**Tech Stack:** HTML/CSS/JS, pdf-lib 1.17.1, @pdf-lib/fontkit 1.1.1, @fontsource Space Grotesk and JetBrains Mono 5.x (woff2), Playwright 1.58 tests against `dist/site` on port 3939.

**Spec:** `docs/superpowers/specs/2026-09-27-dl2-mission-control-design.md`. **Visual source of truth:** `docs/superpowers/specs/2026-09-27-dl2-mission-control-mockups/` (1 style, 2 Show demo, 3 test and PDF, 4 worksheet and Do slide).

## Global Constraints

- Only touch `courses/digital-literacy-2/**`, `tests/**/dl2-*.spec.js`, and `docs/**`. Never edit the homepage, `shared/`, `assets/`, `instructors/`, other courses, `courses.json`, `package.json`, or `scripts/build-site.js`.
- No external network requests from any page (no CDN, no Google Fonts). Fonts are self-hosted.
- Slide body text ≥ 32px at a 1920×1080 viewport (24pt). HUD and chrome labels ≥ 21px at 1920.
- Never rely on color alone: selected, current, correct and incorrect states always carry words.
- No auto-advancing slides. Demo "Auto" only plays demo steps after an explicit press.
- Every learner page loads `/shared/text-size.js` (last script). The deck gives it a `.vub-appbar .vub-textsize` host so it doesn't add a floating button, and deck typography uses `!important` with ≥ (0,2,0) specificity so the injected text-size rules can't distort projector layout.
- Wrap every `localStorage` access in try/catch.
- Letterhead text, exactly: "WEST VIRGINIA" / "Veterans Upward Bound" / "A TRIO program funded by the U.S. Department of Education" / Course "Digital Literacy Level 2" / Cohort "Fall 2026 · Sep 28 – Nov 2" / Instructor "Britt Legg" / Date & time "<Weekday, Mon D, YYYY> · 4:30–6:30 PM ET" / Location "New River Community and Technical College".
- Lab software: Windows 11 + Microsoft 365 desktop apps (Word, Excel, new Outlook). Demo UI must match them.
- Stable URLs: `weeks/week-01/presentation.html`, `weeks/week-01/worksheet.html`, `assessments/pre-test.html`, `assessments/post-test.html`.
- Tests run against the build: `npm run build:site && npx playwright test <spec>`.
- Commit after every task on branch `feat/dl2-mission-control`, and end each message with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. Never pass `-n`/`--no-verify`.

## File Map

| Path (under `courses/digital-literacy-2/`) | Responsibility | Task |
|:--|:--|:--|
| `os/fonts/*`, `os/fonts.css` | Self-hosted fonts (deck woff2, PDF woff) | 1 |
| `os/vendor/pdf-lib.min.js`, `os/vendor/fontkit.umd.min.js` | Vendored PDF libs | 1 |
| `os/img/vub-seal-360.png` | Small seal for PDF/paper | 1 |
| `os/deck.css`, `os/deck.js` | Deck engine and Command Deck / gorge scenes | 2 |
| `os/win11.css`, `os/demo.js` | Windows 11 kit (Settings) and Show engine | 3 |
| `os/items.js`, `os/grade.js` | Item bank (pre + post) and grading/record ID | 4 |
| `os/paper.css`, `os/paper.js` | Letterhead/paper system and letterhead renderer | 5 |
| `os/test.css`, `os/test.js`, `assessments/pre-test.html`, `assessments/post-test.html` | Test flow, Netlify copy, offline outbox | 5 |
| `os/pdf.js` | Graded PDF | 6 |
| `os/keys.js`, `assessments/*-answer-key.html`, `assessments/*-printable.html`, `syllabus.html` (one sentence) | Keys, paper backups, syllabus alignment | 7 |
| `os/win11.css` (Quick Settings, Word, Outlook), `os/demos/week-01.js` | The five Week 1 demos | 8 |
| `weeks/week-01/presentation.html`, `weeks/week-01/presentation-legacy.html` | Week 1 deck and the old deck kept | 9 |
| `weeks/week-01/worksheet.html`, `weeks/week-01/answer-key.html`, `weeks/week-01/run-sheet.html` | Missions 1A–1E, key, run sheet | 10 |
| `tests/**/dl2-*.spec.js` | Retire replaced-file specs, full verification | 11 |

**Dependency order:** Task 1 comes first. Then Tasks 2, 3, 4 and 5 can run in parallel (5 needs 4's `grade.js` interface only). Task 6 needs 4+5. Task 7 needs 4+5. Task 8 needs 3. Task 9 needs 2+8. Task 10 needs 5. Task 11 comes last.

Test helper used by the engine specs (identical in every file that needs it):

```js
// Load engine files into a blank page served from the built site, so relative URLs resolve.
const BASE = 'http://localhost:3939/courses/digital-literacy-2/os/';
const fixture = (body, scripts) => `<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><base href="${BASE}">
<link rel="stylesheet" href="fonts.css"><link rel="stylesheet" href="deck.css"><link rel="stylesheet" href="win11.css">
</head><body class="dl2-os">${body}${scripts.map(s => `<script src="${s}"></script>`).join('')}</body></html>`;
```

---

### Task 1: Scaffold, fonts, vendored libraries

**Files:**
- Create: `courses/digital-literacy-2/os/fonts/` (woff2 + woff), `os/fonts.css`, `os/vendor/pdf-lib.min.js`, `os/vendor/fontkit.umd.min.js`, `os/img/vub-seal-360.png`
- Test: `tests/content/dl2-os-assets.spec.js`

**Interfaces:**
- Produces the font family names `"DL2 Space Grotesk"` (400/500/600/700) and `"DL2 JetBrains Mono"` (500/700), declared in `os/fonts.css`. It also produces WOFF files for the PDF at `os/fonts/playfair-display-latin-800-normal.woff`, `os/fonts/source-sans-3-latin-400-normal.woff` and `os/fonts/source-sans-3-latin-700-normal.woff`. `window.PDFLib` and `window.fontkit` come from the vendor files.

- [ ] **Step 1: Write the failing test**

```js
// tests/content/dl2-os-assets.spec.js
// DL2 Mission Control ships its own fonts and PDF libraries (no CDN).
const { test, expect } = require('@playwright/test');
const path = require('path');
const fs = require('fs');
const OS = path.join(__dirname, '../../courses/digital-literacy-2/os');

test('fonts, vendor libraries and the seal are served', async ({ request }) => {
  for (const f of ['fonts.css', 'fonts/space-grotesk-latin-400-normal.woff2', 'fonts/space-grotesk-latin-700-normal.woff2',
    'fonts/jetbrains-mono-latin-500-normal.woff2', 'fonts/playfair-display-latin-800-normal.woff',
    'fonts/source-sans-3-latin-400-normal.woff', 'fonts/source-sans-3-latin-700-normal.woff',
    'vendor/pdf-lib.min.js', 'vendor/fontkit.umd.min.js', 'img/vub-seal-360.png']) {
    const r = await request.get(`/courses/digital-literacy-2/os/${f}`);
    expect(r.status(), f).toBe(200);
  }
});

test('pdf-lib embeds the Playfair WOFF through fontkit', async () => {
  const { PDFDocument } = require(path.join(OS, 'vendor/pdf-lib.min.js'));
  const fontkit = require(path.join(OS, 'vendor/fontkit.umd.min.js'));
  const doc = await PDFDocument.create();
  doc.registerFontkit(fontkit);
  const font = await doc.embedFont(fs.readFileSync(path.join(OS, 'fonts/playfair-display-latin-800-normal.woff')));
  expect(font.widthOfTextAtSize('Veterans Upward Bound', 20)).toBeGreaterThan(100);
});
```

- [ ] **Step 2: Run it to verify it fails**

Run: `npm run build:site && npx playwright test tests/content/dl2-os-assets.spec.js`
Expected: FAIL (404s, and `Cannot find module …/vendor/pdf-lib.min.js`).

- [ ] **Step 3: Fetch the packages into the scratchpad (no package.json change) and copy files**

```bash
S="$TMPDIR/dl2-vendor" && rm -rf "$S" && mkdir -p "$S" && cd "$S"
npm pack pdf-lib@1.17.1 @pdf-lib/fontkit@1.1.1 @fontsource/space-grotesk@5 @fontsource/jetbrains-mono@5 @fontsource/playfair-display@5 @fontsource/source-sans-3@5 >/dev/null
for t in *.tgz; do mkdir -p "${t%.tgz}" && tar -xzf "$t" -C "${t%.tgz}"; done
OS=~/dev/active/vublessons/courses/digital-literacy-2/os && mkdir -p "$OS/fonts" "$OS/vendor" "$OS/img"
cp pdf-lib-1.17.1/package/dist/pdf-lib.min.js "$OS/vendor/"
cp pdf-lib-fontkit-1.1.1/package/dist/fontkit.umd.min.js "$OS/vendor/"
for w in 400 500 600 700; do cp fontsource-space-grotesk-*/package/files/space-grotesk-latin-$w-normal.woff2 "$OS/fonts/"; done
for w in 500 700; do cp fontsource-jetbrains-mono-*/package/files/jetbrains-mono-latin-$w-normal.woff2 "$OS/fonts/"; done
cp fontsource-playfair-display-*/package/files/playfair-display-latin-800-normal.woff "$OS/fonts/"
for w in 400 700; do cp fontsource-source-sans-3-*/package/files/source-sans-3-latin-$w-normal.woff "$OS/fonts/"; done
sips -Z 360 ~/dev/active/vublessons/"assets/VUB Logo.png" --out "$OS/img/vub-seal-360.png" >/dev/null
ls "$OS/fonts" "$OS/vendor" "$OS/img"
```

Expected: 6 woff2 files, 3 woff files, 2 vendor files and 1 png listed. If a fontsource file name differs, list `…/package/files/` and use the matching latin file.

- [ ] **Step 4: Write `os/fonts.css`**

```css
/* DL2 Mission Control fonts: self-hosted, OFL (Space Grotesk, JetBrains Mono). */
@font-face { font-family: "DL2 Space Grotesk"; src: url("fonts/space-grotesk-latin-400-normal.woff2") format("woff2"); font-weight: 400; font-display: swap; }
@font-face { font-family: "DL2 Space Grotesk"; src: url("fonts/space-grotesk-latin-500-normal.woff2") format("woff2"); font-weight: 500; font-display: swap; }
@font-face { font-family: "DL2 Space Grotesk"; src: url("fonts/space-grotesk-latin-600-normal.woff2") format("woff2"); font-weight: 600; font-display: swap; }
@font-face { font-family: "DL2 Space Grotesk"; src: url("fonts/space-grotesk-latin-700-normal.woff2") format("woff2"); font-weight: 700; font-display: swap; }
@font-face { font-family: "DL2 JetBrains Mono"; src: url("fonts/jetbrains-mono-latin-500-normal.woff2") format("woff2"); font-weight: 500; font-display: swap; }
@font-face { font-family: "DL2 JetBrains Mono"; src: url("fonts/jetbrains-mono-latin-700-normal.woff2") format("woff2"); font-weight: 700; font-display: swap; }
@font-face { font-family: "Playfair Display"; src: url("/assets/fonts/playfair-display-latin-800-normal.woff2") format("woff2"); font-weight: 800; font-display: swap; }
@font-face { font-family: "Playfair Display"; src: url("/assets/fonts/playfair-display-latin-700-normal.woff2") format("woff2"); font-weight: 700; font-display: swap; }
@font-face { font-family: "Source Sans 3"; src: url("/assets/fonts/source-sans-3-latin-400-normal.woff2") format("woff2"); font-weight: 400; font-display: swap; }
@font-face { font-family: "Source Sans 3"; src: url("/assets/fonts/source-sans-3-latin-600-normal.woff2") format("woff2"); font-weight: 600; font-display: swap; }
@font-face { font-family: "Source Sans 3"; src: url("/assets/fonts/source-sans-3-latin-700-normal.woff2") format("woff2"); font-weight: 700; font-display: swap; }
```

- [ ] **Step 5: Run the test to verify it passes**

Run: `npm run build:site && npx playwright test tests/content/dl2-os-assets.spec.js`
Expected: 2 passed. If `require` of the vendor file fails, the UMD file is wrong: re-copy from `dist/`, not `es/`.

- [ ] **Step 6: Commit**

```bash
git add courses/digital-literacy-2/os tests/content/dl2-os-assets.spec.js
git commit -m "feat(dl2): scaffold Mission Control os/ with self-hosted fonts and vendored pdf-lib" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 2: Deck engine (`deck.css`, `deck.js`)

**Files:**
- Create: `courses/digital-literacy-2/os/deck.css`, `courses/digital-literacy-2/os/deck.js`
- Test: `tests/functional/dl2-os-deck.spec.js`

**Interfaces:**
- Consumes: `os/fonts.css` (Task 1).
- Produces:
  - `window.DL2Deck = { go(i, dir), next(), prev(), index(), count(), registerStepper(slideEl, { next(): boolean, back(): boolean, reset(): void }) }`
  - A `dl2:slide` CustomEvent on `document` with `detail: { index, slide }`
  - **Authoring contract:** `<body class="dl2-os"><main class="deck">` holds `<section class="slide" data-phase="warm-up|intro|present|practice|evaluate|apply" data-stage="tell|show|do|review" data-scene="deck|gorge" data-minutes="N">` elements, with `.build` parts, an `.panel` (with modifier `.full`, `.left` or `.center`), a `.hud` header, and `<aside class="notes">`
  - At runtime: slide `.is-active`, `data-step`, `data-steps`; build `.on` and `.now`; strip `.seg.now` with `aria-current="step"`; `body[data-scene]`.

- [ ] **Step 1: Write the failing test**

```js
// tests/functional/dl2-os-deck.spec.js
// Mission Control deck engine: builds before slides, phase strip, notes, timer, no auto-advance.
const { test, expect } = require('@playwright/test');
const BASE = 'http://localhost:3939/courses/digital-literacy-2/os/';
const page3 = `<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><base href="${BASE}">
<link rel="stylesheet" href="fonts.css"><link rel="stylesheet" href="deck.css"></head><body class="dl2-os"><main class="deck">
<section class="slide" data-phase="warm-up" data-scene="gorge"><div class="panel center"><h1>One</h1></div><aside class="notes"><p>Say hello.</p></aside></section>
<section class="slide" data-phase="present" data-stage="tell"><div class="panel full"><div class="hud">WK-01</div><h1>Two</h1><ol class="steps"><li class="build">First</li><li class="build">Second</li></ol></div></section>
<section class="slide" data-phase="practice" data-stage="do" data-minutes="1"><div class="panel full"><h1>Three</h1></div></section>
</main><script src="deck.js"></script></body></html>`;

async function open(page) {
  await page.goto('http://localhost:3939/courses/digital-literacy-2/os/fonts.css'); // same origin for storage
  await page.setContent(page3, { waitUntil: 'load' });
}
const active = page => page.locator('.slide.is-active h1');

test('Next reveals build parts before moving on, and Back reverses', async ({ page }) => {
  await open(page);
  await expect(active(page)).toHaveText('One');
  await page.keyboard.press('ArrowRight');
  await expect(active(page)).toHaveText('Two');
  await expect(page.locator('.slide.is-active .build.on')).toHaveCount(0);
  await page.keyboard.press('PageDown');
  await expect(page.locator('.slide.is-active .build.on')).toHaveCount(1);
  await page.keyboard.press('Space');
  await expect(page.locator('.slide.is-active .build.on')).toHaveCount(2);
  await expect(page.locator('.slide.is-active .build.now')).toHaveText('Second');
  await page.keyboard.press('ArrowRight');
  await expect(active(page)).toHaveText('Three');
  await page.keyboard.press('ArrowLeft');
  await expect(active(page)).toHaveText('Two');
  await expect(page.locator('.slide.is-active .build.on')).toHaveCount(2);
  await page.keyboard.press('Home');
  await expect(active(page)).toHaveText('One');
  await page.keyboard.press('End');
  await expect(active(page)).toHaveText('Three');
});

test('phase strip, counter, stage tag and scene follow the slide', async ({ page }) => {
  await open(page);
  await expect(page.locator('.strip .seg.now')).toHaveText('Warm-up');
  await expect(page.locator('.strip .count')).toHaveText('1 / 3');
  await expect(page.locator('body')).toHaveAttribute('data-scene', 'gorge');
  await page.keyboard.press('ArrowRight');
  await expect(page.locator('.strip .seg.now')).toHaveText('Present');
  await expect(page.locator('.strip .seg.now')).toHaveAttribute('aria-current', 'step');
  await expect(page.locator('.strip .seg.done')).toHaveCount(2);
  await expect(page.locator('.slide.is-active .hud .tag')).toHaveText('TELL');
  await expect(page.locator('body')).toHaveAttribute('data-scene', 'deck');
});

test('N shows notes; typed number + Enter jumps; nothing auto-advances', async ({ page }) => {
  await open(page);
  await page.keyboard.press('n');
  await expect(page.locator('.notes-panel')).toBeVisible();
  await expect(page.locator('.notes-panel')).toContainText('Say hello.');
  await page.keyboard.press('n');
  await expect(page.locator('.notes-panel')).toBeHidden();
  await page.waitForTimeout(2500);
  await expect(active(page)).toHaveText('One');
  await page.keyboard.press('3');
  await page.keyboard.press('Enter');
  await expect(active(page)).toHaveText('Three');
});

test('Do-slide timer counts down after T and says TIME\'S UP in words', async ({ page }) => {
  await page.clock.install();
  await open(page);
  await page.keyboard.press('End');
  await expect(page.locator('.strip .t')).toHaveText('T-01:00');
  await page.keyboard.press('t');
  await page.clock.runFor(2000);
  await expect(page.locator('.strip .t')).toHaveText('T-00:58');
  await page.clock.runFor(60000);
  await expect(page.locator('.strip .t')).toHaveText("TIME'S UP");
});

test('a registered stepper consumes Next before the slide changes', async ({ page }) => {
  await open(page);
  await page.evaluate(() => {
    const s = document.querySelectorAll('.slide')[2]; let n = 0;
    window.DL2Deck.registerStepper(s, { next: () => (n < 2 ? (++n, true) : false), back: () => (n > 0 ? (--n, true) : false), reset: () => { n = 0; } });
    window.__steps = () => n;
  });
  await page.keyboard.press('End');
  await page.keyboard.press('ArrowRight');
  await page.keyboard.press('ArrowRight');
  expect(await page.evaluate(() => window.__steps())).toBe(2);
  await expect(active(page)).toHaveText('Three');
});

test('text-size host exists so no floating button is added', async ({ page }) => {
  await open(page);
  await expect(page.locator('.strip .vub-appbar .vub-textsize [data-vub-textsize-plus]')).toHaveCount(1);
});
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `npm run build:site && npx playwright test tests/functional/dl2-os-deck.spec.js`
Expected: FAIL (`window.DL2Deck` undefined, `.strip` missing).

- [ ] **Step 3: Write `os/deck.js`**

```js
/* DL2 Mission Control deck engine.
 * One slide shows at a time. Next reveals the next .build part, then lets a registered
 * stepper (a Show demo) take a step, then moves to the next slide. Nothing auto-advances. */
(function (global) {
  'use strict';

  var PHASES = [['warm-up', 'Warm-up'], ['intro', 'Intro'], ['present', 'Present'], ['practice', 'Practice'], ['evaluate', 'Evaluate'], ['apply', 'Apply']];
  var STAGES = { tell: 'TELL', show: 'SHOW', do: 'DO', review: 'REVIEW' };
  var LEAVE_MS = 480;
  var GORGE_SVG = '<svg class="gorge-land" viewBox="0 0 1600 560" preserveAspectRatio="xMidYMax slice" aria-hidden="true"><defs>' +
    '<linearGradient id="dl2g1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7a3f80"/><stop offset="1" stop-color="#3a1f55"/></linearGradient>' +
    '<linearGradient id="dl2g2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3f2360"/><stop offset="1" stop-color="#1c1236"/></linearGradient>' +
    '<linearGradient id="dl2g3" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1d1233"/><stop offset="1" stop-color="#0b0718"/></linearGradient>' +
    '<linearGradient id="dl2gr" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ffb36b" stop-opacity="0"/><stop offset=".5" stop-color="#ffd2a1" stop-opacity=".95"/><stop offset="1" stop-color="#ffb36b" stop-opacity="0"/></linearGradient></defs>' +
    '<path fill="url(#dl2g1)" d="M0 250 L120 190 L230 230 L360 150 L470 210 L600 170 L720 220 L860 140 L980 200 L1110 160 L1240 215 L1380 150 L1500 200 L1600 170 L1600 560 L0 560Z"/>' +
    '<path fill="url(#dl2g2)" d="M0 330 L140 260 L260 310 L400 240 L520 300 L660 250 L800 310 L940 270 L1060 330 L1100 360 L1100 560 L0 560Z M1310 360 L1350 320 L1450 280 L1600 300 L1600 560 L1310 560Z"/>' +
    '<path fill="url(#dl2gr)" d="M1080 478 Q1200 462 1330 478 L1330 487 Q1200 474 1080 487Z"/>' +
    '<g stroke="#150c28" fill="none" stroke-width="5" stroke-linecap="round"><path d="M950 330 L1450 330" stroke-width="7"/><path d="M1080 470 Q1200 230 1320 470" stroke-width="10"/>' +
    '<path d="M1100 330V433 M1125 330V397 M1150 330V371 M1175 330V355 M1200 330V350 M1225 330V355 M1250 330V371 M1275 330V397 M1300 330V433"/></g>' +
    '<path fill="url(#dl2g3)" d="M0 390 L110 350 L240 372 L380 340 L520 380 L660 350 L800 380 L940 340 L1040 360 L1085 470 L1085 560 L0 560Z M1315 470 L1360 350 L1450 372 L1530 345 L1600 360 L1600 560 L1315 560Z"/></svg>';

  var deck, slides = [], index = 0, steppers = new Map(), ui = {}, typed = '';
  var timer = { left: 0, total: 0, running: false, expired: false, handle: null };
  var storeKey = 'dl2os:slide:' + location.pathname;

  function safeGet(key) { try { return localStorage.getItem(key); } catch (e) { return null; } }
  function safeSet(key, value) { try { localStorage.setItem(key, value); } catch (e) { /* storage blocked */ } }

  function parts(slide) { return Array.prototype.slice.call(slide.querySelectorAll('.build')); }
  function shown(slide) { return Number(slide.dataset.step || 0); }
  function setStep(slide, n) {
    var list = parts(slide);
    n = Math.max(0, Math.min(list.length, n));
    list.forEach(function (el, k) { el.classList.toggle('on', k < n); el.classList.toggle('now', k === n - 1); });
    slide.dataset.step = String(n);
    slide.dataset.steps = String(list.length);
  }

  function pad(n) { return (n < 10 ? '0' : '') + n; }
  function renderTimer() {
    var seg = ui.timer;
    seg.classList.toggle('expired', timer.expired);
    seg.classList.toggle('running', timer.running);
    seg.textContent = timer.expired ? "TIME'S UP" : timer.total ? 'T-' + pad(Math.floor(timer.left / 60)) + ':' + pad(timer.left % 60) : 'T--:--';
  }
  function stopTimer() { timer.running = false; clearInterval(timer.handle); timer.handle = null; }
  function setTimer(minutes) { stopTimer(); timer.total = timer.left = Math.round(minutes * 60); timer.expired = false; renderTimer(); }
  function toggleTimer() {
    if (!timer.total || timer.expired) return;
    if (timer.running) { stopTimer(); renderTimer(); return; }
    timer.running = true;
    timer.handle = setInterval(function () {
      timer.left = Math.max(0, timer.left - 1);
      if (timer.left === 0) { stopTimer(); timer.expired = true; }
      renderTimer();
    }, 1000);
    renderTimer();
  }

  function renderChrome() {
    var slide = slides[index];
    var at = PHASES.map(function (p) { return p[0]; }).indexOf(slide.dataset.phase || '');
    ui.segs.forEach(function (seg, k) {
      seg.classList.toggle('done', at > -1 && k < at);
      seg.classList.toggle('now', k === at);
      if (k === at) seg.setAttribute('aria-current', 'step'); else seg.removeAttribute('aria-current');
    });
    ui.count.textContent = (index + 1) + ' / ' + slides.length;
    var note = slide.querySelector('.notes');
    ui.notes.innerHTML = '<h2>Notes · slide ' + (index + 1) + '</h2>' + (note ? note.innerHTML : '<p>No notes for this slide.</p>');
    document.body.setAttribute('data-scene', slide.dataset.scene || 'deck');
  }

  function go(to, dir) {
    to = Math.max(0, Math.min(slides.length - 1, to));
    var old = slides[index], next = slides[to];
    if (old !== next) {
      old.classList.remove('is-active');
      old.classList.add('is-leaving');
      old.setAttribute('aria-hidden', 'true');
      old.inert = true;
      setTimeout(function () { old.classList.remove('is-leaving'); }, LEAVE_MS);
    }
    index = to;
    next.classList.add('is-active');
    next.removeAttribute('aria-hidden');
    next.inert = false;
    setStep(next, dir === 'back' ? parts(next).length : 0);
    var stepper = steppers.get(next);
    if (stepper) stepper.reset();
    if (next.dataset.minutes) setTimer(Number(next.dataset.minutes));
    renderChrome();
    safeSet(storeKey, String(index));
    if (history.replaceState) history.replaceState(null, '', '#' + (index + 1));
    document.dispatchEvent(new CustomEvent('dl2:slide', { detail: { index: index, slide: next } }));
  }

  function next() {
    var slide = slides[index];
    if (shown(slide) < parts(slide).length) { setStep(slide, shown(slide) + 1); return; }
    var stepper = steppers.get(slide);
    if (stepper && stepper.next()) return;
    if (index < slides.length - 1) go(index + 1, 'forward');
  }
  function prev() {
    var slide = slides[index];
    var stepper = steppers.get(slide);
    if (stepper && stepper.back()) return;
    if (shown(slide) > 0) { setStep(slide, shown(slide) - 1); return; }
    if (index > 0) go(index - 1, 'back');
  }

  function toggleNotes() { ui.notes.hidden = !ui.notes.hidden; }
  function toggleFullscreen() {
    if (document.fullscreenElement) document.exitFullscreen();
    else if (document.documentElement.requestFullscreen) document.documentElement.requestFullscreen().catch(function () {});
  }

  function onKey(e) {
    if (e.defaultPrevented || e.altKey || e.ctrlKey || e.metaKey) return;
    var t = e.target, tag = t && t.tagName;
    if (tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT' || (t && t.isContentEditable)) return;
    var onControl = tag === 'BUTTON' || tag === 'A';
    var k = e.key;
    if (/^[0-9]$/.test(k)) { typed += k; return; }
    if (k === 'Enter' && typed) { e.preventDefault(); go(Number(typed) - 1, 'forward'); typed = ''; return; }
    typed = '';
    if (k === 'ArrowRight' || k === 'PageDown' || (k === ' ' && !onControl)) { e.preventDefault(); next(); }
    else if (k === 'ArrowLeft' || k === 'PageUp' || k === 'Backspace') { e.preventDefault(); prev(); }
    else if (k === 'Home') { e.preventDefault(); go(0, 'forward'); }
    else if (k === 'End') { e.preventDefault(); go(slides.length - 1, 'forward'); }
    else if (k === 'n' || k === 'N') toggleNotes();
    else if (k === 't' || k === 'T') toggleTimer();
    else if (k === 'f' || k === 'F') toggleFullscreen();
    else if (k === 'b' || k === 'B' || k === '.') document.body.classList.toggle('blackout');
  }

  function onSwipe() {
    var x0 = null;
    deck.addEventListener('pointerdown', function (e) { if (e.pointerType === 'touch') x0 = e.clientX; });
    deck.addEventListener('pointerup', function (e) {
      if (x0 === null) return;
      var dx = e.clientX - x0; x0 = null;
      if (dx < -60) next(); else if (dx > 60) prev();
    });
  }

  function buildChrome() {
    var scenes = document.createElement('div');
    scenes.className = 'scenes';
    scenes.setAttribute('aria-hidden', 'true');
    scenes.innerHTML = '<div class="scene scene-deck"><div class="grid"></div></div>' +
      '<div class="scene scene-gorge"><div class="stars"></div><div class="sun"></div>' + GORGE_SVG + '</div>';
    document.body.insertBefore(scenes, document.body.firstChild);

    var strip = document.createElement('nav');
    strip.className = 'strip';
    strip.setAttribute('aria-label', 'Lesson phase');
    ui.segs = PHASES.map(function (p) {
      var s = document.createElement('span');
      s.className = 'seg'; s.dataset.phase = p[0]; s.textContent = p[1];
      strip.appendChild(s);
      return s;
    });
    ui.timer = document.createElement('span'); ui.timer.className = 'seg t'; ui.timer.setAttribute('role', 'timer'); strip.appendChild(ui.timer);
    ui.count = document.createElement('span'); ui.count.className = 'seg count'; strip.appendChild(ui.count);
    var host = document.createElement('span');
    host.className = 'seg vub-appbar';
    host.innerHTML = '<span class="vub-textsize" role="group" aria-label="Text size"><button type="button" data-vub-textsize-minus aria-label="Decrease text size">A−</button><button type="button" data-vub-textsize-plus aria-label="Increase text size">A+</button></span>';
    strip.appendChild(host);
    deck.appendChild(strip);

    ui.notes = document.createElement('aside');
    ui.notes.className = 'notes-panel';
    ui.notes.hidden = true;
    document.body.appendChild(ui.notes);
    renderTimer();
  }

  function tagStages() {
    slides.forEach(function (s) {
      var label = STAGES[s.dataset.stage], hud = s.querySelector('.hud');
      if (label && hud && !hud.querySelector('.tag')) {
        var tag = document.createElement('span');
        tag.className = 'tag tag-' + s.dataset.stage; tag.textContent = label;
        hud.appendChild(tag);
      }
    });
  }

  function init() {
    deck = document.querySelector('.deck');
    if (!deck) return;
    slides = Array.prototype.slice.call(deck.querySelectorAll('.slide'));
    if (!slides.length) return;
    slides.forEach(function (s) { s.setAttribute('aria-hidden', 'true'); s.inert = true; setStep(s, 0); });
    tagStages();
    buildChrome();
    var fromHash = parseInt((location.hash || '').slice(1), 10);
    var saved = parseInt(safeGet(storeKey) || '', 10);
    var start = fromHash > 0 ? fromHash - 1 : (saved >= 0 ? saved : 0);
    index = 0;
    go(isNaN(start) ? 0 : start, 'forward');
    document.addEventListener('keydown', onKey);
    onSwipe();
  }

  global.DL2Deck = {
    go: go, next: next, prev: prev,
    index: function () { return index; },
    count: function () { return slides.length; },
    registerStepper: function (slide, stepper) { steppers.set(slide, stepper); if (slide === slides[index]) stepper.reset(); }
  };
  init();
})(window);
```

- [ ] **Step 4: Write `os/deck.css`**

Port the teaching-slide styles from mockup `1-style-command-deck-and-gorge.html` (option 2 teaching slide: `.deck` grid wall, `.edge`/`.panel`, `.hud`, `.steps`, `.num`, `kbd`, `.strip`/`.seg`) and the dusk scene (`.dusk .wall`, `.stars`, `.sun`, `.opener` styles), with these mappings. The panel edge is drawn with pseudo-elements so no extra markup is needed.

```css
/* DL2 Mission Control deck. Stage is 16:9, sized to the viewport; type is in cqw so a
 * 1920-wide projector gets ≥32px body text. !important on text rules keeps shared/text-size.js
 * from resizing projector type; the deck applies text size through --ts instead. */
:root { --c-bg:#050814; --c-panel:rgba(6,14,34,.93); --c-cyan:#00e5ff; --c-mag:#ff3cac; --c-gold:#ffc400; --c-ink:#e9fbff; --c-soft:#8fe4f2; --c-peach:#ffc79a; }
html, body { margin:0; height:100%; background:var(--c-bg); overflow:hidden; }
body.dl2-os { color:var(--c-ink); font-family:"DL2 Space Grotesk", "Segoe UI", system-ui, sans-serif; }
.deck { --ts:1; position:fixed; left:50%; top:50%; width:min(100vw, calc(100vh * 16 / 9)); aspect-ratio:16/9; transform:translate(-50%,-50%); container-type:inline-size; z-index:1; }
html[data-text-size="sm"] .deck { --ts:.95; } html[data-text-size="lg"] .deck { --ts:1.08; }
html[data-text-size="xl"] .deck { --ts:1.16; } html[data-text-size="xxl"] .deck { --ts:1.24; }

/* scenes (full viewport, behind the stage) */
.scenes { position:fixed; inset:0; z-index:0; }
.scene { position:absolute; inset:0; opacity:0; transition:opacity .8s ease; overflow:hidden; }
body[data-scene="deck"] .scene-deck, body[data-scene="gorge"] .scene-gorge { opacity:1; }
.scene-deck { background:radial-gradient(80% 60% at 50% 110%, rgba(0,220,255,.28), transparent 60%), radial-gradient(50% 40% at 85% 10%, rgba(255,60,172,.22), transparent 70%), radial-gradient(40% 40% at 10% 20%, rgba(255,196,0,.12), transparent 70%), var(--c-bg); }
.scene-deck .grid { position:absolute; left:-50%; right:-50%; bottom:-10%; height:50%; background-image:linear-gradient(rgba(0,229,255,.55) 1px, transparent 1px), linear-gradient(90deg, rgba(0,229,255,.55) 1px, transparent 1px); background-size:4vw 4vw; transform:perspective(30vw) rotateX(62deg); transform-origin:bottom; animation:dl2-grid 4s linear infinite; -webkit-mask-image:linear-gradient(to top,#000 20%,transparent 90%); mask-image:linear-gradient(to top,#000 20%,transparent 90%); }
@keyframes dl2-grid { to { background-position:0 4vw; } }
.scene-gorge { background:linear-gradient(180deg,#0b0a2a 0%, #2a1850 34%, #7a2d6b 55%, #e2735a 70%, #f4b76a 78%, #2a1a3e 79%); }
.scene-gorge .gorge-land { position:absolute; left:0; bottom:0; width:100%; height:62%; }
.scene-gorge .sun { position:absolute; left:74%; top:50%; width:22vw; height:22vw; transform:translate(-50%,-50%); border-radius:50%; background:radial-gradient(circle, rgba(255,214,150,.95), rgba(255,140,110,.45) 45%, transparent 70%); filter:blur(.6vw); animation:dl2-breathe 8s ease-in-out infinite alternate; }
@keyframes dl2-breathe { to { transform:translate(-50%,-46%) scale(1.06); } }
.scene-gorge .stars { position:absolute; inset:0 0 45% 0; opacity:.8; background-image:radial-gradient(1px 1px at 12% 18%, #fff 50%, transparent 51%), radial-gradient(1px 1px at 32% 8%, #fff 50%, transparent 51%), radial-gradient(1.5px 1.5px at 58% 22%, #fff 50%, transparent 51%), radial-gradient(1px 1px at 76% 12%, #fff 50%, transparent 51%), radial-gradient(1px 1px at 88% 30%, #fff 50%, transparent 51%), radial-gradient(1px 1px at 22% 34%, #fff 50%, transparent 51%), radial-gradient(1.5px 1.5px at 44% 4%, #fff 50%, transparent 51%); animation:dl2-twinkle 6s ease-in-out infinite alternate; }
@keyframes dl2-twinkle { to { opacity:.35; } }

/* slides and transitions */
.slide { position:absolute; inset:0; visibility:hidden; }
.slide.is-active, .slide.is-leaving { visibility:visible; }
.slide.is-active { animation:dl2-open .45s cubic-bezier(.2,.8,.2,1) both; }
.slide.is-leaving { animation:dl2-close .45s cubic-bezier(.4,0,.2,1) both; }
@keyframes dl2-open { from { opacity:0; transform:scale(.965) translateY(1.2cqw); filter:blur(4px); } }
@keyframes dl2-close { to { opacity:0; transform:scale(1.02); filter:blur(3px); } }
.slide .notes { display:none; }

/* panel with tracing neon edge (pseudo-elements; clip-path clips both) */
@property --dl2-ang { syntax:'<angle>'; inherits:false; initial-value:0deg; }
.panel { position:absolute; isolation:isolate; clip-path:polygon(2cqw 0,100% 0,100% calc(100% - 2cqw),calc(100% - 2cqw) 100%,0 100%,0 2cqw); padding:2.6cqw 3.4cqw; }
.panel::before { content:""; position:absolute; inset:0; z-index:-2; background:conic-gradient(from var(--dl2-ang), var(--c-cyan), var(--c-mag), var(--c-gold), var(--c-cyan)); animation:dl2-edge 9s linear infinite; }
.panel::after { content:""; position:absolute; inset:2px; z-index:-1; background:var(--c-panel); clip-path:polygon(calc(2cqw - 1px) 0,100% 0,100% calc(100% - 2cqw + 1px),calc(100% - 2cqw + 1px) 100%,0 100%,0 calc(2cqw - 1px)); }
@keyframes dl2-edge { to { --dl2-ang:360deg; } }
.panel.full { left:4.5%; right:4.5%; top:6%; bottom:17%; }
.panel.left { left:4.5%; right:40%; top:7%; bottom:20%; }
.panel.center { left:12%; right:12%; top:16%; bottom:24%; text-align:center; }
.panel.bare::before, .panel.bare::after { display:none; } /* gorge slides: text straight on the scene */

/* type (≥32px body at 1920 ⇒ ≥1.67cqw) */
.dl2-os .deck .slide h1 { font-size:calc(4.1cqw * var(--ts)) !important; line-height:1.06 !important; font-weight:700; letter-spacing:-.02em; margin:1.4cqw 0 0; }
.dl2-os .deck .slide h1 em { font-style:normal; color:var(--c-gold); }
.dl2-os .deck .slide h2 { font-size:calc(2.8cqw * var(--ts)) !important; line-height:1.15 !important; margin:0; }
.dl2-os .deck .slide p, .dl2-os .deck .slide li, .dl2-os .deck .slide td, .dl2-os .deck .slide th { font-size:calc(1.9cqw * var(--ts)) !important; line-height:1.35 !important; }
.hud { display:flex; align-items:center; gap:1.1cqw; font-family:"DL2 JetBrains Mono", monospace; font-size:1.15cqw; letter-spacing:.12em; text-transform:uppercase; color:#6ff3ff; }
.hud img { width:2.4cqw; height:auto; }
.hud .tag { margin-left:auto; padding:.25cqw .9cqw; font-weight:700; color:#021018; }
.tag-tell { background:#6ff3ff; } .tag-show { background:#ff6fc1; } .tag-do { background:var(--c-gold); } .tag-review { background:#a6ff8f; }
.steps { list-style:none; margin:2.2cqw 0 0; padding:0; display:flex; flex-direction:column; gap:1.2cqw; }
.steps li { display:flex; align-items:center; gap:1.3cqw; }
.num { flex:none; width:3.3cqw; height:3.3cqw; display:grid; place-items:center; font-family:"DL2 JetBrains Mono", monospace; font-weight:700; font-size:1.4cqw; border:1px solid rgba(0,229,255,.5); color:#6ff3ff; background:rgba(0,229,255,.08); clip-path:polygon(.8cqw 0,100% 0,100% calc(100% - .8cqw),calc(100% - .8cqw) 100%,0 100%,0 .8cqw); }
.build { opacity:0; transform:translateX(-1.5cqw); transition:opacity .55s cubic-bezier(.2,.8,.2,1), transform .55s cubic-bezier(.2,.8,.2,1); }
.build.on { opacity:1; transform:none; }
.build.now .num { background:var(--c-cyan); color:#021018; box-shadow:0 0 2cqw var(--c-cyan); }
.dl2-os kbd, .path { font-family:"DL2 JetBrains Mono", monospace; font-size:.9em; color:#021018; background:var(--c-gold); padding:.1cqw .7cqw; font-weight:700; }

/* phase strip */
.strip { position:absolute; left:4.5%; right:4.5%; bottom:4.5%; height:7.5%; display:grid; grid-template-columns:repeat(6,1fr) auto auto auto; gap:.5cqw; font-family:"DL2 JetBrains Mono", monospace; font-size:1.1cqw; letter-spacing:.1em; z-index:5; }
.seg { border:1px solid rgba(0,229,255,.35); display:flex; align-items:center; justify-content:center; color:var(--c-soft); background:rgba(4,10,26,.75); text-transform:uppercase; padding:0 1cqw; }
.seg.done { background:rgba(0,229,255,.2); color:#d4fbff; }
.seg.now { background:linear-gradient(90deg,rgba(255,60,172,.55),rgba(255,196,0,.45)); color:#fff; border-color:#ff6fc1; box-shadow:0 0 1.6cqw rgba(255,60,172,.6); }
.seg.t { color:var(--c-gold); border-color:rgba(255,196,0,.5); min-width:9cqw; }
.seg.t.expired { background:var(--c-gold); color:#1a1305; animation:dl2-blink 1s steps(2) infinite; }
.seg.vub-appbar button { font:inherit; color:var(--c-ink); background:none; border:0; padding:0 .4cqw; cursor:pointer; }
.seg.vub-appbar button:focus-visible, .dl2-os button:focus-visible { outline:3px solid var(--c-gold); outline-offset:2px; }
@keyframes dl2-blink { 50% { opacity:.5; } }

/* notes, blackout */
.notes-panel { position:fixed; left:2vw; right:2vw; bottom:2vw; max-height:40vh; overflow:auto; z-index:20; background:rgba(4,8,20,.96); border:1px solid rgba(0,229,255,.5); padding:1.2vw 1.6vw; font-size:20px; line-height:1.5; color:var(--c-ink); }
.notes-panel h2 { font-family:"DL2 JetBrains Mono", monospace; font-size:14px; letter-spacing:.14em; color:#6ff3ff; margin:0 0 .5em; }
body.blackout::after { content:""; position:fixed; inset:0; background:#000; z-index:30; }

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation:none !important; transition:none !important; }
  .build { opacity:0; transform:none; } .build.on { opacity:1; }
}
```

Also port the Do-slide styles from mockup 4 (`.dohead`, `.timer`, `.sab` with `.a`/`.b`/`.arr`, `.dsteps`, `.sheet`) and add Review styles (`.answer` card: cyan left rule, dark panel; `.choices` three cards for slide 26; `.compare` two columns for slide 23). Minimum sizes at the 1920 stage: `.sab > div` 1.8cqw, `.dsteps div` 1.75cqw, `.answer` 2cqw, `.choices div` 1.8cqw, `.sheet` 1.3cqw (chrome), and `.timer b` 3.6cqw. Anything a learner must read is ≥ 1.67cqw.

Also port the gorge "opener" slide styles from the mockup under `.slide[data-scene="gorge"] .opener …` (seal 7cqw with a cyan glow, kicker in mono with a gold number, h1 at 5.6cqw, chips with a staggered entrance, `.go` blinking, `.where` top-right). Keep every font size at ≥ 1.2cqw for chrome and ≥ 1.67cqw for body.

- [ ] **Step 5: Run the test to verify it passes**

Run: `npm run build:site && npx playwright test tests/functional/dl2-os-deck.spec.js`
Expected: 6 passed.

- [ ] **Step 6: Commit**

```bash
git add courses/digital-literacy-2/os/deck.css courses/digital-literacy-2/os/deck.js tests/functional/dl2-os-deck.spec.js
git commit -m "feat(dl2): Mission Control deck engine with build steps, phase strip, timer and notes" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 3: Show engine (`demo.js`) and the Windows 11 Settings kit (`win11.css`)

**Files:**
- Create: `courses/digital-literacy-2/os/demo.js`, `courses/digital-literacy-2/os/win11.css`
- Test: `tests/functional/dl2-os-demo.spec.js`

**Interfaces:**
- Consumes: `window.DL2Deck.registerStepper` (optional, Task 2).
- Produces `window.DL2Demo = { define(def), mount(hostEl) → controller, get(id) }`.
  - `def = { id: string, title: string, screenClass?: string, scene: string /* HTML authored at 1280×720 */, start?: [x, y], steps: Step[] }`
  - `Step = { cap: string /* HTML */, check: string /* short checklist label */, target?: string /* CSS selector inside the scene */, action?: 'click'|'type'|'hover'|'none', text?: string /* for type */, at?: [fx, fy] /* point within target, default [.5,.5] */, zoom?: number|false /* default 2.1 */, zoomOut?: boolean /* zoom back out after the state applies */, state?: { attr?: {name: value} /* sets data-name on .screen */, cls?: {name: bool} /* toggles class on .screen */, text?: {selector: string} /* sets textContent */, css?: {'--var': value} /* sets style on .screen */ } }`
  - The controller is `{ next(): boolean, back(): boolean, reset(): void, index(): number }`. States are cumulative: rendering step *i* rebuilds the scene from `def.scene` and applies `steps[0..i].state` in order.
  - Hosts: `<div class="demo" data-demo="<id>"></div>`. It auto-mounts on DOMContentLoaded and registers with DL2Deck when inside a `.slide`.
  - DOM produced: `.demo-bezel > .demo-viewport > .screen`, `.demo-side` with `.demo-stepno`, `.demo-cap[aria-live=polite]`, `ol.demo-todo > li.done|.now`, and `.demo-controls` buttons with `data-act="back|next|auto|replay|slow"`.
  - Win11 kit class names (Settings): `.w11-wall`, `.w11-taskbar`, `.w11-tbi` (`.open`), `.w11-tray`, `.w11-win` (font-size `var(--ui)`), `.w11-title` + `.w11-ctl`, `.w11-body`, `.w11-nav`, `.w11-acct`, `.w11-avatar`, `.w11-search`, `.w11-navi` (`.sel`), `.w11-content`, `.w11-h1` (`.parent`, `.sep`), `.w11-page` (shown when `.screen[data-page=<name>] .w11-page[data-page=<name>]`), `.w11-sect`, `.w11-card` (`.ci`, `.ct`, `.chev`), `.w11-combo`, `.w11-flyout` (shown when `.screen.menu-open`), `.w11-opt` (`.sel`), `.w11-toggle`.

- [ ] **Step 1: Write the failing test**

```js
// tests/functional/dl2-os-demo.spec.js
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
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `npm run build:site && npx playwright test tests/functional/dl2-os-demo.spec.js`
Expected: FAIL (`DL2Demo is not defined`).

- [ ] **Step 3: Write `os/demo.js`**

```js
/* DL2 Show engine: plays a Windows 11 recreation one step at a time with a guided cursor,
 * camera zoom, spotlight and click ripple. States are cumulative, so Back rebuilds instantly. */
(function (global) {
  'use strict';
  var W = 1280, H = 720;
  var registry = {}, controllers = {};
  var reduce = !!(global.matchMedia && global.matchMedia('(prefers-reduced-motion: reduce)').matches);
  var CURSOR = '<svg viewBox="0 0 22 30" aria-hidden="true"><path d="M1.5 1.5 L1.5 23 L7 17.8 L10.8 27 L14.4 25.5 L10.7 16.5 L18 16.5 Z" fill="#fff" stroke="#000" stroke-width="1.6" stroke-linejoin="round"/></svg>';

  function define(def) { registry[def.id] = def; return def; }
  function make(tag, cls, html) { var e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; }

  function applyState(screen, st) {
    if (!st) return;
    Object.keys(st.attr || {}).forEach(function (k) { screen.setAttribute('data-' + k, st.attr[k]); });
    Object.keys(st.cls || {}).forEach(function (k) { screen.classList.toggle(k, !!st.cls[k]); });
    Object.keys(st.text || {}).forEach(function (sel) { screen.querySelectorAll(sel).forEach(function (n) { n.textContent = st.text[sel]; }); });
    Object.keys(st.css || {}).forEach(function (k) { screen.style.setProperty(k, st.css[k]); });
  }
  function offset(el, root) {
    var x = 0, y = 0, e = el;
    while (e && e !== root) { x += e.offsetLeft; y += e.offsetTop; e = e.offsetParent; }
    return { x: x, y: y, w: el.offsetWidth, h: el.offsetHeight };
  }

  function mount(host) {
    var def = registry[host.dataset.demo];
    if (!def) { console.error('DL2Demo: no demo named', host.dataset.demo); return null; }
    host.innerHTML = '';
    host.classList.add('demo');
    var bezel = make('div', 'demo-bezel'), vp = make('div', 'demo-viewport');
    bezel.setAttribute('role', 'img');
    bezel.setAttribute('aria-label', 'Windows 11 demonstration: ' + def.title);
    bezel.appendChild(vp);
    var side = make('div', 'demo-side');
    var stepno = make('div', 'demo-stepno'), cap = make('div', 'demo-cap'), todo = make('ol', 'demo-todo');
    cap.setAttribute('aria-live', 'polite');
    def.steps.forEach(function (s, k) { todo.appendChild(make('li', '', '<i>' + (k + 1) + '</i><span>' + s.check + '</span>')); });
    var controls = make('div', 'demo-controls',
      '<button type="button" data-act="back">◀ Back</button><button type="button" data-act="next">Next ▶</button>' +
      '<button type="button" data-act="auto" aria-pressed="false">Auto</button>' +
      '<button type="button" data-act="replay" aria-label="Replay from the start">↺</button>' +
      '<button type="button" data-act="slow" aria-pressed="false" aria-label="Half speed">½×</button>');
    side.appendChild(stepno); side.appendChild(cap); side.appendChild(todo); side.appendChild(controls);
    host.appendChild(bezel); host.appendChild(side);

    var screen, cursor, spot, idx = 0, token = 0, busy = false, spd = 1, auto = false, base = 1, cam = { z: 1, px: W / 2, py: H / 2 };
    var wait = function (ms) { return new Promise(function (r) { setTimeout(r, reduce ? 0 : ms * spd); }); };

    function camera(anim) {
      var s = base * cam.z, bw = vp.clientWidth, bh = vp.clientHeight;
      var tx = Math.min(0, Math.max(bw - W * s, bw / 2 - cam.px * s));
      var ty = Math.min(0, Math.max(bh - H * s, bh / 2 - cam.py * s));
      screen.style.transition = anim && !reduce ? 'transform ' + 700 * spd + 'ms cubic-bezier(.65,0,.35,1)' : 'none';
      screen.style.transform = 'translate(' + tx + 'px,' + ty + 'px) scale(' + s + ')';
    }
    function fit() { base = vp.clientWidth / W || 1; if (screen) camera(false); }
    if (global.ResizeObserver) new ResizeObserver(fit).observe(vp);

    function ui(i) {
      stepno.textContent = 'STEP ' + (i + 1) + ' / ' + def.steps.length;
      cap.innerHTML = def.steps[i].cap;
      Array.prototype.forEach.call(todo.children, function (li, k) { li.className = k < i ? 'done' : k === i ? 'now' : ''; });
    }
    function point(step) {
      var t = step.target && screen.querySelector(step.target);
      if (!t) return null;
      var p = offset(t, screen), at = step.at || [0.5, 0.5];
      return { box: p, x: p.x + p.w * at[0], y: p.y + p.h * at[1] };
    }
    function place(x, y, anim) {
      cursor.style.transition = anim && !reduce ? 'left ' + 750 * spd + 'ms cubic-bezier(.45,0,.2,1), top ' + 750 * spd + 'ms cubic-bezier(.45,0,.2,1)' : 'none';
      cursor.style.left = x + 'px'; cursor.style.top = y + 'px';
    }
    function render(i) {
      var fresh = make('div', 'screen ' + (def.screenClass || ''), def.scene);
      spot = make('div', 'demo-spot'); cursor = make('div', 'demo-cursor', CURSOR);
      fresh.appendChild(spot); fresh.appendChild(cursor);
      if (screen) vp.replaceChild(fresh, screen); else vp.appendChild(fresh);
      screen = fresh;
      for (var k = 0; k <= i; k++) applyState(screen, def.steps[k].state);
      var start = def.start || [640, 400], last = null;
      for (var j = i; j >= 0 && !last; j--) last = def.steps[j].target ? point(def.steps[j]) : null;
      place(last ? last.x : start[0], last ? last.y : start[1], false);
      cam = { z: 1, px: W / 2, py: H / 2 }; fit();
    }
    function jump(i) { token++; busy = false; idx = i; render(i); ui(i); }

    function play(i) {
      var my = ++token, step = def.steps[i];
      busy = true; idx = i; ui(i);
      if (reduce || !step.target) { render(i); busy = false; return Promise.resolve(); }
      var p = point(step);
      if (!p) { console.error('DL2Demo: missing target', step.target, 'in', def.id); render(i); busy = false; return Promise.resolve(); }
      cam = { z: 1, px: W / 2, py: H / 2 }; camera(true);
      return wait(450).then(function () {
        if (my !== token) return;
        place(p.x, p.y, true);
        return wait(800);
      }).then(function () {
        if (my !== token) return;
        Object.assign(spot.style, { left: p.box.x - 6 + 'px', top: p.box.y - 6 + 'px', width: p.box.w + 12 + 'px', height: p.box.h + 12 + 'px' });
        spot.classList.add('on');
        if (step.zoom !== false) { cam = { z: step.zoom || 2.1, px: p.x, py: p.y }; camera(true); }
        return wait(750);
      }).then(function () {
        if (my !== token) return;
        if (step.action === 'type' && step.text) {
          var t = screen.querySelector(step.target), chars = step.text.split(''), n = 0;
          return new Promise(function (done) {
            (function tick() {
              if (my !== token) return done();
              if (n >= chars.length) return done();
              if ('value' in t) t.value += chars[n++]; else t.textContent += chars[n++];
              setTimeout(tick, 55 * spd);
            })();
          });
        }
        if (step.action !== 'hover' && step.action !== 'none') {
          cursor.classList.add('press');
          var r = make('div', 'demo-ripple'); r.style.left = p.x + 'px'; r.style.top = p.y + 'px'; screen.appendChild(r);
          setTimeout(function () { r.remove(); cursor.classList.remove('press'); }, 700 * spd);
        }
        return wait(380);
      }).then(function () {
        if (my !== token) return;
        spot.classList.remove('on');
        applyState(screen, step.state);
        if (step.zoomOut) { cam = { z: 1, px: W / 2, py: H / 2 }; camera(true); }
        busy = false;
      });
    }

    var ctl = {
      index: function () { return idx; },
      next: function () {
        if (busy) jump(idx);
        if (idx >= def.steps.length - 1) return false;
        play(idx + 1); return true;
      },
      back: function () { if (idx <= 0) return false; setAuto(false); jump(idx - 1); return true; },
      reset: function () { setAuto(false); jump(0); }
    };
    function setAuto(on) {
      auto = on;
      controls.querySelector('[data-act="auto"]').setAttribute('aria-pressed', String(on));
      if (!on) return;
      (function loop() {
        if (!auto) return;
        if (idx >= def.steps.length - 1) { setAuto(false); return; }
        Promise.resolve(play(idx + 1)).then(function () { if (auto) setTimeout(loop, 2200 * spd); });
      })();
    }
    controls.addEventListener('click', function (e) {
      var b = e.target.closest('button'); if (!b) return;
      var act = b.dataset.act;
      if (act === 'next') { setAuto(false); ctl.next(); }
      else if (act === 'back') ctl.back();
      else if (act === 'replay') ctl.reset();
      else if (act === 'auto') setAuto(!auto);
      else if (act === 'slow') { spd = spd === 1 ? 2 : 1; b.setAttribute('aria-pressed', String(spd === 2)); }
    });

    jump(0);
    controllers[def.id] = ctl;
    var slide = host.closest('.slide');
    if (slide && global.DL2Deck) global.DL2Deck.registerStepper(slide, ctl);
    return ctl;
  }

  function mountAll() { Array.prototype.forEach.call(document.querySelectorAll('[data-demo]'), mount); }
  global.DL2Demo = { define: define, mount: mount, get: function (id) { return controllers[id]; } };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', mountAll);
  else setTimeout(mountAll, 0);
})(window);
```

- [ ] **Step 4: Write `os/win11.css`**

Port the Windows 11 recreation from mockup `2-show-demo-engine.html`: the `.screen`, `.bloom`, `.taskbar`, `.tbi`, `.tray`, `.win`, `.wtitle`, `.wbody`, `.nav`, `.acct`, `.avatar`, `.search`, `.navi`, `.content`, `.page`, `.card`, `.sect`, `.combo`, `.toggle`, `.flyout`, `.opt`, `.cursor`, `.ripple` and `.spot` rules, plus the demo chrome (`.bezel`, `.viewport`, `.side`, `.stepno`, `.caption`, `.todo`, `.controls`). Rename them with the prefixes `w11-` (Windows parts) and `demo-` (engine parts) listed in the Interfaces, and make these required adjustments:

```css
/* Show slides: HUD on top, demo fills the rest of the panel */
.slide[data-stage="show"] .panel { display:flex; flex-direction:column; gap:1.3cqw; }
.slide[data-stage="show"] .demo { flex:1; min-height:0; }
/* Engine chrome: a two-column Show layout inside a slide panel */
.demo { display:grid; grid-template-columns:1fr 27%; gap:2cqw; height:100%; min-height:0; }
.demo-bezel { position:relative; align-self:start; aspect-ratio:16/9; border-radius:.9cqw; padding:.5cqw; background:linear-gradient(180deg,#1b2336,#0b0f1a); box-shadow:0 0 0 1px rgba(0,229,255,.35), 0 0 3cqw -.5cqw rgba(0,229,255,.45); }
.demo-viewport { position:relative; width:100%; height:100%; overflow:hidden; border-radius:.5cqw; background:#000; }
.screen { position:absolute; left:0; top:0; width:1280px; height:720px; transform-origin:0 0; overflow:hidden; --ui:14px;
  font-family:"Segoe UI Variable Text","Segoe UI",system-ui,sans-serif; color:#1a1a1a; }
.demo-stepno { font-family:"DL2 JetBrains Mono", monospace; font-size:1.15cqw; letter-spacing:.16em; color:var(--c-gold,#ffc400); }
.dl2-os .deck .slide .demo-cap { font-size:calc(2.1cqw * var(--ts,1)) !important; font-weight:600; line-height:1.25 !important; min-height:8cqw; margin:.8cqw 0 1.2cqw; }
.demo-cap em { font-style:normal; color:var(--c-gold,#ffc400); }
.dl2-os .deck .slide .demo-todo li { font-size:calc(1.7cqw * var(--ts,1)) !important; }
.demo-todo { list-style:none; margin:0; padding:0; display:flex; flex-direction:column; gap:.6cqw; }
.demo-todo li { display:flex; gap:.8cqw; align-items:center; color:#7f93b0; }
.demo-todo li i { font-style:normal; width:2.4cqw; height:2.4cqw; display:grid; place-items:center; font-family:"DL2 JetBrains Mono", monospace; font-size:1.1cqw; border:1px solid rgba(0,229,255,.35); flex:none; }
.demo-todo li.done { color:#bfe9f2; } .demo-todo li.done i { background:rgba(0,229,255,.2); color:#6ff3ff; }
.demo-todo li.done i::after { content:"✓"; margin-left:.2em; }
.demo-todo li.now { color:#fff; } .demo-todo li.now i { background:#00e5ff; color:#021018; box-shadow:0 0 1.2cqw #00e5ff; }
.demo-controls { margin-top:auto; display:flex; gap:.6cqw; flex-wrap:wrap; padding-top:1.2cqw; }
.demo-controls button { font-family:"DL2 JetBrains Mono", monospace; font-size:1.2cqw; color:#d9f7ff; background:rgba(0,229,255,.08); border:1px solid rgba(0,229,255,.4); padding:.6cqw .9cqw; cursor:pointer; }
.demo-controls button[aria-pressed="true"] { background:#ffc400; color:#1a1305; border-color:#ffc400; }
.demo-side { display:flex; flex-direction:column; min-height:0; }
.demo-cursor { position:absolute; left:640px; top:400px; width:22px; height:30px; z-index:50; pointer-events:none; filter:drop-shadow(0 2px 3px rgba(0,0,0,.35)); }
.demo-cursor svg { width:100%; height:100%; transform-origin:0 0; transition:transform .12s; }
.demo-cursor.press svg { transform:scale(.85); }
.demo-ripple { position:absolute; width:14px; height:14px; margin:-7px 0 0 -7px; border-radius:50%; border:3px solid #ffc400; z-index:49; pointer-events:none; animation:demo-rip .6s ease-out forwards; }
@keyframes demo-rip { to { transform:scale(4.5); opacity:0; } }
.demo-spot { position:absolute; z-index:40; border-radius:8px; border:3px solid #00e5ff; box-shadow:0 0 0 4000px rgba(4,8,20,.32), 0 0 22px rgba(0,229,255,.8); pointer-events:none; opacity:0; transition:opacity .3s; }
.demo-spot.on { opacity:1; }
/* pages: .screen[data-page="x"] shows .w11-page[data-page="x"]; flyouts open with .screen.menu-open */
.w11-page { display:none; }
.screen[data-page="system"] .w11-page[data-page="system"], .screen[data-page="display"] .w11-page[data-page="display"],
.screen[data-page="sound"] .w11-page[data-page="sound"] { display:block; }
.w11-flyout { display:none; } .screen.menu-open .w11-flyout { display:block; }
```

Because `.screen` lives inside `.slide`, the deck's `!important` `p`/`li` rules would also hit Windows text. Scenes therefore use `div`/`span` only (no `p`/`li`/`td`) for Windows text. That constraint is part of the Win11 kit contract.

- [ ] **Step 5: Run the test to verify it passes**

Run: `npm run build:site && npx playwright test tests/functional/dl2-os-demo.spec.js`
Expected: 5 passed.

- [ ] **Step 6: Commit**

```bash
git add courses/digital-literacy-2/os/demo.js courses/digital-literacy-2/os/win11.css tests/functional/dl2-os-demo.spec.js
git commit -m "feat(dl2): Show engine with guided cursor, camera zoom and Windows 11 Settings kit" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 4: Item bank and grading (`items.js`, `grade.js`)

**Files:**
- Create: `courses/digital-literacy-2/os/items.js`, `courses/digital-literacy-2/os/grade.js`
- Test: `tests/content/dl2-os-items.spec.js`

**Interfaces:**
- Produces `DL2Items = { version: 'v1-2026-09', domains: [{id,name}], pre: Item[20], post: Item[20] }`.
  - `Item = { n, week, domain /* id */, skill, stem, options: [A,B,C,D], answer: 'A'|'B'|'C'|'D', why }`
- Produces `DL2Grade = { grade(items, answers /* array of 'A'..'D'|null */) → Result, recordId(form /* 'pre'|'post' */, date, name) → string, initials(name) → string }`.
  - `Result = { correct, total, percent, byDomain: [{id,name,correct,total}], rows: [{n, skill, chosen /* letter|null */, chosenText, answer, answerText, correct: bool}] }`
- Both files are UMD: `if (typeof module === 'object' && module.exports) module.exports = X; else global.X = X;`

- [ ] **Step 1: Write the failing test**

```js
// tests/content/dl2-os-items.spec.js
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
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `npx playwright test tests/content/dl2-os-items.spec.js`
Expected: FAIL (`Cannot find module …/os/items.js`).

- [ ] **Step 3: Write `os/grade.js`**

```js
/* DL2 grading and record IDs. UMD so Node tests can require it. */
(function (global) {
  'use strict';
  var LETTERS = ['A', 'B', 'C', 'D'];
  function pad(n) { return (n < 10 ? '0' : '') + n; }
  function initials(name) {
    var parts = String(name || '').trim().split(/\s+/).filter(Boolean);
    if (!parts.length) return 'X';
    return (parts[0][0] + (parts.length > 1 ? parts[parts.length - 1][0] : '')).toUpperCase();
  }
  function recordId(form, d, name) {
    return 'DL2-' + String(form).toUpperCase() + '-' + d.getFullYear() + pad(d.getMonth() + 1) + pad(d.getDate()) + '-' + pad(d.getHours()) + pad(d.getMinutes()) + '-' + initials(name);
  }
  function grade(items, answers) {
    var domains = (global.DL2Items || (typeof require === 'function' ? require('./items.js') : null)).domains;
    var byId = {};
    domains.forEach(function (d) { byId[d.id] = { id: d.id, name: d.name, correct: 0, total: 0 }; });
    var rows = items.map(function (it, i) {
      var chosen = answers[i] || null, ok = chosen === it.answer;
      byId[it.domain].total++; if (ok) byId[it.domain].correct++;
      return { n: it.n, skill: it.skill, chosen: chosen, chosenText: chosen ? it.options[LETTERS.indexOf(chosen)] : '', answer: it.answer, answerText: it.options[LETTERS.indexOf(it.answer)], correct: ok };
    });
    var correct = rows.filter(function (r) { return r.correct; }).length;
    return { correct: correct, total: items.length, percent: Math.round(100 * correct / items.length), byDomain: domains.map(function (d) { return byId[d.id]; }), rows: rows };
  }
  var api = { grade: grade, recordId: recordId, initials: initials, LETTERS: LETTERS };
  if (typeof module === 'object' && module.exports) module.exports = api; else global.DL2Grade = api;
})(typeof window !== 'undefined' ? window : globalThis);
```

- [ ] **Step 4: Write `os/items.js` (the full item bank; option order fixes the answer letter)**

```js
/* DL2 pre-test and post-test item bank (v1, Sept 2026). Item N on each form checks the same
 * skill, domain and week with a different real-life scenario. Answers are balanced A–D (5 each). */
(function (global) {
  'use strict';
  var domains = [
    { id: 'tb', name: 'Technology Basics' }, { id: 'dc', name: 'Digital Citizenship' },
    { id: 'im', name: 'Information Management' }, { id: 'cc', name: 'Content Creation' },
    { id: 'com', name: 'Communication' }, { id: 'col', name: 'Collaboration' }, { id: 'ss', name: 'Safety & Security' }
  ];
  var S = {
    1: 'Make text bigger in every app', 2: 'Fix a page that spills onto a second sheet', 3: 'Fix a repeating calendar event',
    4: 'Write a help request that can be answered', 5: 'Narrow a web search', 6: 'Judge whether a source fits',
    7: 'Act on a wrong confirmation', 8: 'Share with the right permissions', 9: 'Use real heading styles',
    10: 'Check that a SUM total updates', 11: 'Use a licensed photo properly', 12: 'Share a file that looks the same everywhere',
    13: 'Write a clear request with a deadline', 14: 'Know what Bcc does', 15: 'Use respectful, inclusive wording',
    16: 'Give and answer feedback on one shared copy', 17: 'Spot a recurring charge', 18: "Don't rely on color alone",
    19: 'Secure a new account', 20: 'Check a suspicious contact a safer way'
  };
  var W = { 1: 1, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 2, 8: 2, 9: 3, 10: 3, 11: 3, 12: 3, 13: 4, 14: 4, 15: 4, 16: 4, 17: 4, 18: 5, 19: 5, 20: 5 };
  var D = { 1: 'tb', 2: 'tb', 3: 'tb', 4: 'com', 5: 'im', 6: 'im', 7: 'im', 8: 'col', 9: 'cc', 10: 'cc', 11: 'dc', 12: 'cc', 13: 'com', 14: 'com', 15: 'dc', 16: 'col', 17: 'ss', 18: 'dc', 19: 'ss', 20: 'ss' };
  function it(n, stem, options, answer, why) { return { n: n, week: W[n], domain: D[n], skill: S[n], stem: stem, options: options, answer: answer, why: why }; }

  var pre = [
    it(1, 'Text is too small in every app you use. Zooming in the web browser only fixed one website. What should you change?',
      ['Zoom in the web browser again', 'The Scale setting in Settings ▸ System ▸ Display', 'The screen resolution, to its lowest setting', 'Nothing. Text size can’t be changed.'], 'B',
      'Display Scale changes text size in every app. Browser zoom only changes web pages.'),
    it(2, 'In print preview, your one-page flyer shows a second page with only the last line on it. What should you do first?',
      ['Print it anyway and throw away page 2', 'Delete the last line of the flyer', 'Make the margins a little smaller, then check the preview again', 'Switch to a different printer'], 'C',
      'Adjusting the layout and re-checking the preview fixes the spill without losing words or paper.'),
    it(3, 'Your weekly Monday class reminder keeps showing up on Tuesdays. What is the best fix?',
      ['Open the event, edit the whole series to repeat weekly on Monday, then check next week', 'Change only this week’s reminder', 'Delete it and try to remember instead', 'Turn off all reminders'], 'A',
      'Editing the series fixes every future reminder; checking the next one proves it worked.'),
    it(4, 'Word shows an error every time you try to save. Which help request will get you the fastest useful answer?',
      ['“Word is broken. Help!”', '“Can someone fix my computer tomorrow?”', '“My computer hates me.”', '“Word (Microsoft 365, Version 2408): when I click Save I see ‘Document not saved.’ I restarted Word and tried Save As. Same message.”'], 'D',
      'Naming the app and version, the task, what you tried and the exact message lets a helper act right away.'),
    it(5, 'You searched for “classes” and got millions of results. You want a beginner computer class near Beckley, WV. Which search is best?',
      ['beginner computer classes Beckley WV, then add a filter such as a date range', 'classes', 'computer', 'free stuff near me'], 'A',
      'Specific words plus a place narrow the results; one filter narrows them further.'),
    it(6, 'A website says its $499 course is “the only way” to pass a computer skills test. What should you do?',
      ['Trust it because the website looks professional', 'Notice the seller profits from that claim, and compare other sources such as the library or a college', 'Buy it now before the price goes up', 'Share it with friends first'], 'B',
      'A source that profits from a claim has a reason to exaggerate, so compare it with independent sources.'),
    it(7, 'After you sign up for a workshop online, the confirmation page shows the wrong date. What should you do?',
      ['Nothing. The confirmation is probably wrong.', 'Submit the form five more times', 'Use the correction or contact method on the confirmation, and keep a copy of it', 'Close the page and forget it'], 'C',
      'The confirmation is your record of what they received, so use their stated way to fix it and keep proof.'),
    it(8, 'You are sharing a budget sheet. One person should fix mistakes; three others only need to look. Which permissions fit?',
      ['Everyone gets Editor', 'Everyone gets Viewer, including the person fixing mistakes', 'Post the link publicly', 'The person fixing mistakes gets Editor; the other three get Viewer'], 'D',
      'Give each person only the access their job needs: Editor to change, Viewer to look.'),
    it(9, 'You made your section titles big and bold, but they don’t appear in Word’s Navigation pane. What should you do?',
      ['Apply real heading styles (Heading 1, Heading 2) from the Home tab', 'Make the titles even bigger', 'Underline the titles', 'Type the titles in all capital letters'], 'A',
      'Word builds navigation and tables of contents from heading styles, not from big bold text.'),
    it(10, 'Cell B7 contains =SUM(B2:B6) and shows 28. You change B3 from 12 to 15. What should B7 show now?',
      ['28', '31', '15', 'An error'], 'B',
      'SUM recalculates: 28 − 12 + 15 = 31. If it didn’t change, the cells aren’t in the range.'),
    it(11, 'A photo’s license says you may crop it if you credit the photographer. How do you use it on your flyer?',
      ['Crop it and leave off the credit', 'Use it with no credit, uncropped', 'Crop a copy and include the photographer’s credit', 'Find the same photo on another site so you don’t need credit'], 'C',
      'Follow the license: cropping is allowed, and the credit is required.'),
    it(12, 'You made a handout in Word for neighbors who may not have Word. How should you share it?',
      ['Send the Word file and hope it opens', 'Take a photo of your screen', 'Copy the text into a text message', 'Save it as a PDF, open the PDF to check it, then share it'], 'D',
      'A PDF looks the same on any device; opening it first catches problems before others see them.'),
    it(13, 'Which email is the clearest request?',
      ['“Please review the attached flyer and reply with any changes by Thursday at noon.”', '“Hey, can you look at this sometime?”', '“FYI.”', '“Here is the flyer.”'], 'A',
      'A clear request says what to do, with what, and by when.'),
    it(14, 'You email 30 veterans about a meeting and put their addresses in Bcc. What does Bcc do?',
      ['Stops anyone from forwarding the email', 'Hides each person’s address from the others', 'Encrypts the email', 'Deletes the email after it’s read'], 'B',
      'Bcc keeps addresses private from the group. It does not stop forwarding or protect the message.'),
    it(15, 'A flyer says: “Older folks probably can’t use video calls, so we’ll call them instead.” What’s the best rewrite?',
      ['Leave it as is. It’s helpful.', '“Video only.”', '“Join by video call, or ask us for a phone call instead.”', '“Young people only.”'], 'C',
      'Offer choices to everyone instead of assuming what a group can or can’t do.'),
    it(16, 'Two people need to suggest edits to the same document, but they can’t work at the same time. What works best?',
      ['Email copies back and forth', 'Everyone makes their own copy', 'Print it and mail it', 'Add comments on one shared draft'], 'D',
      'Comments on one shared copy keep every suggestion in one place, in order.'),
    it(17, 'An app says: “Free for 7 days, then $8/month.” What does this mean?',
      ['After 7 days you’ll be charged $8 every month until you cancel', 'It’s free forever', 'You’ll pay $8 one time', 'You’ll pay only if you like it'], 'A',
      'A trial that turns into a monthly price is a recurring charge. Note the date to cancel if you don’t want it.'),
    it(18, 'A class sign-in sheet shows who is done using only red and green dots. Some people can’t tell red from green. What’s the best fix?',
      ['Make the dots bigger', 'Use a brighter red', 'Add words such as “Complete” and “Not yet” next to the dots', 'Remove the dots and all color'], 'C',
      'Words next to the color make the meaning clear to everyone.'),
    it(19, 'You are creating a new account for a volunteer website. What is the best security choice?',
      ['Reuse your email password so you won’t forget it', 'Use a new, long password you use nowhere else, and turn on two-step verification (MFA)', 'Use “password123”', 'Write your password on a sticky note on the monitor'], 'B',
      'A unique long password plus MFA protects the account even if another site is breached.'),
    it(20, 'A caller says they’re from the VA and need your Social Security number to “keep your benefits.” What should you do?',
      ['Give it. They said they’re from the VA.', 'Call back the number they gave you', 'Text them the number instead', 'Hang up, then call the VA yourself using a number from VA.gov or your VA card'], 'D',
      'Contact the organization through a number you already trust, not one the caller gives you.')
  ];

  var post = [
    it(1, 'A friend says the words in File Explorer, Word and Settings are all hard to read. What is the best single change?',
      ['Turn on Night light', 'Change the desktop background to a darker picture', 'Set Scale in Settings ▸ System ▸ Display to a larger size, such as 125%', 'Zoom in each app one at a time'], 'C',
      'One Display Scale change enlarges text in every app at once.'),
    it(2, 'Before printing 20 copies of a sign-up sheet, what should you do?',
      ['Check print preview, fix anything that spills, then print one test copy', 'Print all 20 and check the first one', 'Make the font tiny so it surely fits', 'Email it to the printer'], 'A',
      'Preview first and test one copy, so a mistake costs one sheet instead of twenty.'),
    it(3, 'You set a repeating reminder to take your medicine at 8:00 AM, but it pops up at 8:00 PM. What should you do?',
      ['Edit only today’s reminder', 'Make a second reminder and keep both', 'Silence the computer at night', 'Edit the whole series to 8:00 AM, then check the next reminder'], 'D',
      'Fix the series so every future reminder is right, then confirm with the next one.'),
    it(4, 'You need to ask the help desk about a printing problem. Which details matter most?',
      ['Your password, so they can log in and check', 'The app and version, what you were doing, what you already tried, and the exact message', 'Just “Printer doesn’t work.” They’ll figure it out.', 'The model number of your monitor'], 'B',
      'Those four details let a helper reproduce the problem. Never share your password.'),
    it(5, 'You want a food pantry that is open on Saturdays in Summers County, WV. Which search is best?',
      ['food', 'pantry recipes', 'Saturday', 'food pantry open Saturday Summers County WV'], 'D',
      'Name the thing, the time and the place to get results that fit.'),
    it(6, 'You find a page listing free tax help, but it was last updated three years ago. What should you do?',
      ['Use it. Tax help never changes.', 'Print it and go without calling', 'Check a current official source or call to confirm the program still runs this year', 'Assume all free tax help is fake'], 'C',
      'Old information may be out of date, so confirm it with a current source before you rely on it.'),
    it(7, 'A confirmation email for your appointment shows the wrong location. What is the best next step?',
      ['Use the change or contact option in the confirmation, give your confirmation number and the right location, and save their reply', 'Reply “wrong” and nothing else', 'Show up at both locations', 'Book a second appointment without canceling the first'], 'A',
      'Use the official route with your confirmation number, and keep the reply as proof.'),
    it(8, 'You want a friend to suggest changes to your résumé without changing it directly. Which permission fits best?',
      ['Editor', 'Commenter', 'Owner', 'Anyone with the link can edit'], 'B',
      'Commenter lets someone suggest without changing your document.'),
    it(9, 'You want Word to build a table of contents from your section titles. What must the titles use?',
      ['Bold text', 'A different font color', 'Font size 20', 'Heading styles, such as Heading 1 and Heading 2'], 'D',
      'Tables of contents and navigation come from heading styles.'),
    it(10, 'Your grocery total uses =SUM(C2:C5) and shows $40. You change one item from $6 to $10. What should the total show?',
      ['$44', '$40', '$10', '$46'], 'A',
      'The total goes up by the $4 difference: $40 + $4 = $44.'),
    it(11, 'You find a great photo online but can’t find any license or permission. What is the safest choice?',
      ['Use it. If it’s online, it’s free.', 'Choose a photo with a clear license and follow its credit rules', 'Use it and write “Found on Google”', 'Take a screenshot so it becomes yours'], 'B',
      'No license means no permission. Use a photo whose license you can follow.'),
    it(12, 'A form must look exactly the same when anyone prints it. Which file should you send?',
      ['A Word document so people can change it', 'A plain text file', 'A PDF, after opening it once to check it', 'A screenshot pasted into an email'], 'C',
      'PDFs keep their layout everywhere; check it before sending.'),
    it(13, 'You need three volunteers to say whether they can help at Saturday’s event. Which subject line and first line work best?',
      ['Subject: “Hi” — “Just checking in.”', 'Subject: “Event” — “See attached.”', 'No subject — “Let me know.”', 'Subject: “Reply by Wed: Can you help Sat 9–11?” — “Please reply yes or no by Wednesday at 5 PM.”'], 'D',
      'Put the request and the deadline where people see them first.'),
    it(14, 'Why use Bcc when writing to a big group who don’t know each other?',
      ['So everyone’s email address stays private from the rest of the group', 'So nobody can reply', 'So the email arrives faster', 'So the message can’t be forwarded'], 'A',
      'Bcc protects the group’s addresses. It doesn’t stop replies or forwarding.'),
    it(15, 'A class announcement says “Guys, bring your laptops.” What is a more welcoming version?',
      ['“Guys and gals, bring laptops.”', '“Everyone, please bring a laptop if you have one. We have loaners too.”', '“Only people with laptops should come.”', 'Leave it the same.'], 'B',
      'Address everyone and remove barriers, such as offering loaner laptops.'),
    it(16, 'A reviewer comments: “Add the help desk phone number after step 3.” What is the best response?',
      ['Delete the comment', 'Reply “OK” and change nothing', 'Add the verified number after step 3, reply “Added,” and resolve the comment', 'Add any phone number you can find quickly'], 'C',
      'Make the change with accurate information, then answer and close the comment so everyone knows.'),
    it(17, 'Before you tap “Start free trial,” what should you check?',
      ['The app’s colors', 'How many stars it has, and nothing else', 'Nothing. Trials are always free.', 'When the trial ends, what it will cost, how often, and how to cancel'], 'D',
      'Know the end date, the price, how often you’ll pay, and how to cancel before you agree.'),
    it(18, 'A chart uses only color to show “on time” and “late.” How do you make it readable for everyone?',
      ['Add labels or patterns so it doesn’t depend on color alone', 'Use even more colors', 'Make it smaller', 'Turn it black and white with no labels'], 'A',
      'Labels or patterns carry the meaning for people who can’t see the colors.'),
    it(19, 'A website asks you to create a password. Which choice is strongest?',
      ['Your pet’s name', 'The same password you use for email', 'A long passphrase you use nowhere else, such as “Maple-River-Tractor-42!”, plus two-step verification', '12345678'], 'C',
      'Long, unique and backed by MFA is the strongest combination.'),
    it(20, 'An email says your bank account is locked and gives a link to “unlock it now.” What is the safest move?',
      ['Click the link quickly', 'Don’t click. Open your bank’s app or call the number on your card to check.', 'Reply with your account number', 'Forward it to friends, then click'], 'B',
      'Go to the bank through a route you already trust, never through the message’s link.')
  ];

  var api = { version: 'v1-2026-09', domains: domains, pre: pre, post: post };
  if (typeof module === 'object' && module.exports) module.exports = api; else global.DL2Items = api;
})(typeof window !== 'undefined' ? window : globalThis);
```

- [ ] **Step 5: Run the test to verify it passes**

Run: `npx playwright test tests/content/dl2-os-items.spec.js`
Expected: 5 passed. If the balance test fails, a letter was mistyped: fix the `answer` to match the option order above (pre: B C A D A B C D A B C D A B C D A C B D; post: C A D B D C A B D A B C D A B C D A C B). If the pre list shows A:5, B:5, C:5, D:5 but differs from this sequence, the sequence above is authoritative.

- [ ] **Step 6: Commit**

```bash
git add courses/digital-literacy-2/os/items.js courses/digital-literacy-2/os/grade.js tests/content/dl2-os-items.spec.js
git commit -m "feat(dl2): parallel 20-item pre/post bank and grading" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 5: Test engine (paper system, test flow, Netlify copy, offline outbox)

**Files:**
- Create: `courses/digital-literacy-2/os/paper.css`, `os/paper.js`, `os/test.css`, `os/test.js`
- Replace: `courses/digital-literacy-2/assessments/pre-test.html`, `courses/digital-literacy-2/assessments/post-test.html`
- Test: `tests/functional/dl2-os-test.spec.js`

**Interfaces:**
- Consumes: `DL2Items`, `DL2Grade` (Task 4). `DL2Pdf.build(opts) → Promise<Uint8Array>` (Task 6) when present. If it's absent or throws, the engine falls back to an HTML report.
- Produces:
  - `DL2Paper = { letterhead(opts) → HTML, classDate(date) → 'Mon, Sep 28, 2026 · 4:30–6:30 PM ET', META }`
  - `META = { state:'WEST VIRGINIA', org:'Veterans Upward Bound', trio:'A TRIO program funded by the U.S. Department of Education', course:'Digital Literacy Level 2', cohort:'Fall 2026 · Sep 28 – Nov 2', instructor:'Britt Legg', location:'New River Community and Technical College', classTime:'4:30–6:30 PM ET' }`
  - `DL2Test = { state() }` for tests
  - Netlify form names `dl2-pretest` and `dl2-posttest`, with fields `form-name, record-id, student, form, started, submitted, score, domains, answers, bot-field`
  - Outbox key: `dl2os:outbox`

- [ ] **Step 1: Write the failing test**

```js
// tests/functional/dl2-os-test.spec.js
// DL2 pre/post test flow: name, 20 questions, review with skip flags, grading, results copy, offline outbox.
const { test, expect } = require('@playwright/test');
const Items = require('../../courses/digital-literacy-2/os/items.js');
const URL = '/courses/digital-literacy-2/assessments/pre-test.html';

async function start(page, name = 'James Doe') {
  await page.goto(URL);
  await page.evaluate(() => { try { localStorage.clear(); } catch (e) {} });
  await page.reload();
  await page.getByLabel('Your full name').fill(name);
  await page.getByRole('button', { name: 'Start the pre-test' }).click();
}
async function answerAll(page, pick = i => Items.pre[i].answer, skip = []) {
  for (let i = 0; i < 20; i++) {
    await expect(page.locator('.q-count')).toHaveText(`Question ${i + 1} of 20`);
    if (!skip.includes(i)) await page.locator(`.opt[data-letter="${pick(i)}"]`).click();
    await page.getByRole('button', { name: i === 19 ? 'Review answers' : 'Next' }).click();
  }
}

test('name is required and the letterhead header shows', async ({ page }) => {
  await page.goto(URL);
  await expect(page.locator('.test-top')).toContainText('Digital Literacy Level 2 · Pre-Test');
  await page.getByRole('button', { name: 'Start the pre-test' }).click();
  await expect(page.locator('.field-error')).toContainText('Please type your name');
});

test('selection shows in words; Back is disabled on question 1', async ({ page }) => {
  await start(page);
  await page.locator('.opt[data-letter="B"]').click();
  await expect(page.locator('.opt[data-letter="B"] .pick')).toHaveText('✓ Selected');
  await expect(page.locator('.opt[data-letter="B"]')).toHaveAttribute('aria-checked', 'true');
  await expect(page.getByRole('button', { name: 'Back' })).toBeDisabled();
});

test('full run: skip one, review, submit, grade, send copy', async ({ page }) => {
  const posts = [];
  await page.route('**/', async route => {
    if (route.request().method() === 'POST') { posts.push(route.request().postData()); return route.fulfill({ status: 200, body: 'ok' }); }
    return route.continue();
  });
  await start(page);
  await answerAll(page, i => (i === 0 ? (Items.pre[0].answer === 'A' ? 'B' : 'A') : Items.pre[i].answer), [4]);
  await expect(page.locator('.review-row.skipped')).toHaveCount(1);
  await expect(page.locator('.review-row.skipped')).toContainText('Not answered');
  await page.getByRole('button', { name: 'Submit my test' }).click();
  await page.getByRole('button', { name: 'Yes, submit' }).click();
  await expect(page.locator('.result-score')).toContainText('18 of 20');
  await expect(page.locator('.copy-status')).toContainText('A copy was sent to Britt');
  expect(posts).toHaveLength(1);
  const body = new URLSearchParams(posts[0]);
  expect(body.get('form-name')).toBe('dl2-pretest');
  expect(body.get('student')).toBe('James Doe');
  expect(body.get('score')).toBe('18/20');
  expect(body.get('record-id')).toMatch(/^DL2-PRE-\d{8}-\d{4}-JD$/);
  expect(body.get('answers').split(',')).toHaveLength(20);
});

test('offline: result is queued and sent on the next visit', async ({ page }) => {
  let fail = true; const posts = [];
  await page.route('**/', async route => {
    if (route.request().method() !== 'POST') return route.continue();
    if (fail) return route.abort();
    posts.push(route.request().postData()); return route.fulfill({ status: 200, body: 'ok' });
  });
  await start(page, 'Ann Lee');
  await answerAll(page);
  await page.getByRole('button', { name: 'Submit my test' }).click();
  await page.getByRole('button', { name: 'Yes, submit' }).click();
  await expect(page.locator('.copy-status')).toContainText('Saved on this computer. Tell Britt.');
  expect(await page.evaluate(() => JSON.parse(localStorage.getItem('dl2os:outbox')).length)).toBe(1);
  fail = false;
  await page.goto(URL);
  await expect.poll(() => posts.length).toBe(1);
  expect(await page.evaluate(() => JSON.parse(localStorage.getItem('dl2os:outbox') || '[]').length)).toBe(0);
});

test('a reload keeps answers in progress', async ({ page }) => {
  await start(page);
  await page.locator('.opt[data-letter="C"]').click();
  await page.reload();
  await expect(page.locator('.q-count')).toHaveText('Question 1 of 20');
  await expect(page.locator('.opt[data-letter="C"]')).toHaveClass(/sel/);
});

test('the page registers its Netlify form and loads no external resources', async ({ page }) => {
  const external = [];
  page.on('request', r => { if (!r.url().startsWith('http://localhost:3939')) external.push(r.url()); });
  await page.goto(URL);
  await expect(page.locator('form[name="dl2-pretest"][data-netlify="true"]')).toHaveCount(1);
  expect(external).toEqual([]);
});
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `npm run build:site && npx playwright test tests/functional/dl2-os-test.spec.js`
Expected: FAIL (the old pre-test page has no `Your full name` label or `.q-count`).

- [ ] **Step 3: Write `os/paper.js`**

```js
/* DL2 paper system: the official letterhead used by the graded report, answer keys,
 * printable tests and (as static copies) the worksheets. */
(function (global) {
  'use strict';
  var META = {
    state: 'WEST VIRGINIA', org: 'Veterans Upward Bound', trio: 'A TRIO program funded by the U.S. Department of Education',
    course: 'Digital Literacy Level 2', cohort: 'Fall 2026 · Sep 28 – Nov 2', instructor: 'Britt Legg',
    location: 'New River Community and Technical College', classTime: '4:30–6:30 PM ET'
  };
  var DAYS = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
  var MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  function classDate(d) { return DAYS[d.getDay()] + ', ' + MONTHS[d.getMonth()] + ' ' + d.getDate() + ', ' + d.getFullYear() + ' · ' + META.classTime; }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function letterhead(opts) {
    var date = opts && opts.date ? classDate(opts.date) : (opts && opts.dateText) || '';
    var seal = (opts && opts.seal) || '/courses/digital-literacy-2/os/img/vub-seal-360.png';
    return '<header class="letterhead"><div class="lh-bar" aria-hidden="true"></div>' +
      '<img class="lh-seal" src="' + seal + '" alt="Veterans Upward Bound seal">' +
      '<div class="lh-org"><div class="lh-state">' + META.state + '</div><div class="lh-name">' + META.org + '</div><div class="lh-trio">' + META.trio + '</div></div>' +
      '<dl class="lh-meta"><div><dt>Course</dt><dd>' + META.course + '</dd></div><div><dt>Cohort</dt><dd>' + META.cohort + '</dd></div>' +
      '<div><dt>Instructor</dt><dd>' + META.instructor + '</dd></div><div><dt>Date &amp; time</dt><dd>' + esc(date) + '</dd></div>' +
      '<div><dt>Location</dt><dd>' + META.location + '</dd></div></dl><div class="lh-rule" aria-hidden="true"></div></header>';
  }
  global.DL2Paper = { META: META, classDate: classDate, letterhead: letterhead, esc: esc };
})(window);
```

- [ ] **Step 4: Write `os/paper.css`**

Port the paper styles from mockup `3-test-screen-and-graded-pdf.html` (`.paper`, `.tri`, `.lh`, `.org`, `.meta`, `.rule2`, `.doc-title`, `.who`, `.score`, `.doms`, `.dom`, `table`, `td.r.ok/.no`, `tr.miss`, `.sig`, `.fine`) and from mockup `4-worksheet-and-do-slide.html` (`.namerow`, `.mhead`, `.badges`, `.ab`, `ol.steps`, `.see`, `.box`, `.path`, `kbd`, `.two`, `.stuck`, `.check`, `.home`). Convert `cqw` sizes to print-safe `pt`: base 12pt body, 11pt small, 24pt org name, 20pt mission titles. Rename the letterhead classes to the `lh-*` names produced by `DL2Paper.letterhead()`:

```css
/* DL2 paper: letter-size documents on official letterhead. Prints in black and white. */
@page { size: letter; margin: 0.5in; }
.paper-doc { --navy:#1B365D; --gold:#C9A227; --red:#B31942; --ink:#15213A; --rule:#E3E8F1; font-family:"Source Sans 3", "Segoe UI", sans-serif; color:var(--ink); background:#fff; max-width:8.5in; margin:0 auto; padding:0.5in; font-size:12pt; line-height:1.4; }
.letterhead { position:relative; display:grid; grid-template-columns:auto 1fr auto; gap:14pt; align-items:center; padding-top:10pt; }
.lh-bar { position:absolute; left:-0.5in; right:-0.5in; top:-0.5in; height:7pt; background:linear-gradient(90deg,var(--navy) 0 60%, var(--gold) 60% 80%, var(--red) 80%); -webkit-print-color-adjust:exact; print-color-adjust:exact; }
.lh-seal { width:62pt; height:62pt; }
.lh-state { font-size:8.5pt; letter-spacing:.34em; font-weight:700; color:#8a6d12; }
.lh-name { font-family:"Playfair Display", Georgia, serif; font-weight:800; font-size:24pt; line-height:1.02; color:var(--navy); }
.lh-trio { font-size:9pt; font-style:italic; color:#4a5874; margin-top:3pt; }
.lh-meta { margin:0; font-size:8.5pt; line-height:1.5; border-left:2pt solid var(--gold); padding-left:9pt; }
.lh-meta div { display:flex; gap:6pt; } .lh-meta dt { font-weight:700; color:var(--navy); min-width:52pt; } .lh-meta dd { margin:0; }
.lh-rule { grid-column:1 / -1; height:5pt; border-top:2pt solid var(--navy); border-bottom:1pt solid var(--gold); margin-top:4pt; }
@media print { .no-print { display:none !important; } }
```

- [ ] **Step 5: Write `os/test.css`**

Port `.scr.light` from mockup 3 as a full-page layout: a navy top bar `.test-top` (seal, title, student line, `.q-count`), `.ticks` with 20 `i` (`.a` answered, `.c` current, each with a `title` "Question n: answered/not answered"), a centered `.test-card` (max-width 980px) holding the question, `.opt` tiles (`button`, `role="radio"`, `aria-checked`) with a `b` letter badge, the option text, and a `.pick` "✓ Selected" span shown when `.sel`. Also style `.test-nav` buttons (Back outline navy, Next/Review solid red `#B31942`) and `.review-row` (`.skipped` with a pink background and "⚠ Not answered" text). The dialog `.confirm` uses `<dialog>`. Result screen styles: `.result-score` (Playfair, navy), `.copy-status`. Sizes: question text 26px, options 22px, buttons 20px, all at least 44px tall. Background `#eef2f9 → #e4eaf5`. `.test-textsize` is `position:fixed; top:14px; right:16px; z-index:10`, with white A−/A+ buttons on the navy header (`.test-top` reserves 150px of right padding for it).

- [ ] **Step 6: Write `os/test.js`**

```js
/* DL2 pre/post test: name → 20 questions → review → submit → grade → PDF → copy to Britt.
 * Answers survive a reload. If sending fails, the copy waits in an outbox and retries next visit. */
(function (global) {
  'use strict';
  var root = document.querySelector('[data-dl2-test]');
  if (!root) return;
  var FORM = root.dataset.form === 'post' ? 'post' : 'pre';
  var LABEL = FORM === 'pre' ? 'Pre-Test' : 'Post-Test';
  var ITEMS = global.DL2Items[FORM];
  var KEY = 'dl2os:test:' + FORM, OUTBOX = 'dl2os:outbox';
  var LETTERS = ['A', 'B', 'C', 'D'];
  var esc = global.DL2Paper.esc;
  var st = load() || { phase: 'start', name: '', started: null, at: 0, answers: ITEMS.map(function () { return null; }) };

  function load() { try { return JSON.parse(localStorage.getItem(KEY)); } catch (e) { return null; } }
  function save() { try { localStorage.setItem(KEY, JSON.stringify(st)); } catch (e) { /* storage blocked */ } }
  function clear() { try { localStorage.removeItem(KEY); } catch (e) { /* storage blocked */ } }
  function readOutbox() { try { return JSON.parse(localStorage.getItem(OUTBOX) || '[]'); } catch (e) { return []; } }
  function writeOutbox(list) { try { localStorage.setItem(OUTBOX, JSON.stringify(list)); } catch (e) { /* storage blocked */ } }

  function top(extra) {
    return '<header class="test-top"><img src="/courses/digital-literacy-2/os/img/vub-seal-360.png" alt="" width="44" height="44">' +
      '<div class="ttl">Digital Literacy Level 2 · ' + LABEL + (st.name ? '<small>' + esc(st.name) + '</small>' : '') + '</div>' +
      (extra || '') + '</header>';
  }
  function ticks() {
    return '<div class="ticks" aria-hidden="true">' + ITEMS.map(function (_, i) {
      return '<i class="' + (st.answers[i] ? 'a' : '') + (i === st.at ? ' c' : '') + '"></i>';
    }).join('') + '</div>';
  }

  function renderStart(error) {
    root.innerHTML = top() + '<main class="test-card start" id="main"><h1>' + LABEL + '</h1>' +
      '<p>20 questions · about 20 minutes. Pick the best answer for each. You can go back and change answers before you submit.</p>' +
      '<p>' + (FORM === 'pre' ? 'This shows where to start. It is not a grade.' : 'This shows how far you’ve come since the pre-test.') + '</p>' +
      '<label for="name">Your full name</label><input id="name" autocomplete="name" value="' + esc(st.name) + '">' +
      (error ? '<p class="field-error" role="alert">' + error + '</p>' : '') +
      '<div class="test-nav"><span></span><button type="button" class="primary" data-go="begin">Start the ' + LABEL.toLowerCase() + '</button></div></main>';
    root.querySelector('#name').focus();
  }

  function renderQuestion() {
    var it = ITEMS[st.at], chosen = st.answers[st.at];
    root.innerHTML = top('<div class="q-count">Question ' + (st.at + 1) + ' of 20</div>') + ticks() +
      '<main class="test-card" id="main"><h1 class="q" id="q-stem">' + esc(it.stem) + '</h1><div class="opts" role="radiogroup" aria-labelledby="q-stem">' +
      it.options.map(function (o, k) {
        var L = LETTERS[k], on = chosen === L;
        return '<button type="button" class="opt' + (on ? ' sel' : '') + '" role="radio" aria-checked="' + on + '" data-letter="' + L + '"><b>' + L + '</b><span>' + esc(o) + '</span><span class="pick">' + (on ? '✓ Selected' : '') + '</span></button>';
      }).join('') + '</div>' +
      '<div class="test-nav"><button type="button" data-go="back"' + (st.at === 0 ? ' disabled' : '') + '>◀ Back</button>' +
      '<button type="button" class="primary" data-go="next">' + (st.at === 19 ? 'Review answers' : 'Next ▶') + '</button></div></main>';
    var sel = root.querySelector('.opt.sel') || root.querySelector('.opt');
    sel.focus();
  }

  function renderReview() {
    var answered = st.answers.filter(Boolean).length;
    root.innerHTML = top('<div class="q-count">Review</div>') + '<main class="test-card" id="main"><h1>Check your answers</h1>' +
      '<p>You answered <strong>' + answered + ' of 20</strong>. Select any question to change it.</p><div class="review">' +
      ITEMS.map(function (it, i) {
        var a = st.answers[i];
        return '<button type="button" class="review-row' + (a ? '' : ' skipped') + '" data-jump="' + i + '"><b>' + (i + 1) + '</b><span>' + esc(it.stem) + '</span><em>' + (a ? 'Answer: ' + a : '⚠ Not answered') + '</em></button>';
      }).join('') + '</div><div class="test-nav"><button type="button" data-go="last">◀ Back to question 20</button><button type="button" class="primary" data-go="submit">Submit my test</button></div>' +
      '<dialog class="confirm"><h2>Submit your test?</h2><p>You answered ' + answered + ' of 20. You can’t change answers after you submit.</p>' +
      '<div class="test-nav"><button type="button" data-go="cancel">Go back</button><button type="button" class="primary" data-go="confirm">Yes, submit</button></div></dialog></main>';
  }

  function download(bytes, filename) {
    var url = URL.createObjectURL(new Blob([bytes], { type: 'application/pdf' }));
    var a = document.createElement('a'); a.href = url; a.download = filename; document.body.appendChild(a); a.click(); a.remove();
    return url;
  }
  function send(payload) {
    var body = new URLSearchParams(payload).toString();
    return fetch('/', { method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: body })
      .then(function (r) { if (!r.ok) throw new Error('HTTP ' + r.status); return true; });
  }
  function flushOutbox() {
    var list = readOutbox();
    if (!list.length) return;
    var remaining = [];
    list.reduce(function (p, item) {
      return p.then(function () { return send(item).catch(function () { remaining.push(item); }); });
    }, Promise.resolve()).then(function () { writeOutbox(remaining); });
  }

  function submit() {
    var submitted = new Date(), started = new Date(st.started);
    var result = global.DL2Grade.grade(ITEMS, st.answers);
    var rid = global.DL2Grade.recordId(FORM, submitted, st.name);
    var payload = {
      'form-name': 'dl2-' + FORM + 'test', 'bot-field': '', 'record-id': rid, student: st.name, form: FORM + ' ' + global.DL2Items.version,
      started: started.toISOString(), submitted: submitted.toISOString(), score: result.correct + '/' + result.total,
      domains: result.byDomain.map(function (d) { return d.id + ':' + d.correct + '/' + d.total; }).join(' '),
      answers: st.answers.map(function (a) { return a || '-'; }).join(',')
    };
    var report = { form: FORM, label: LABEL, items: ITEMS, result: result, name: st.name, started: started, submitted: submitted, recordId: rid };
    clear();
    renderResult(report, payload);
  }

  function renderResult(report, payload) {
    var r = report.result, last = String(report.name).trim().split(/\s+/).pop().replace(/[^A-Za-z0-9-]/g, '') || 'Student';
    var filename = 'DL2-' + report.label.replace('-', '') + '-' + last + '-' + report.recordId.split('-').slice(2, 4).join('-') + '.pdf';
    root.innerHTML = top() + '<main class="test-card result" id="main"><h1>Thank you, ' + esc(report.name) + '!</h1>' +
      '<p class="result-score">' + r.correct + ' of 20 correct</p><p class="pdf-status" role="status">Making your results PDF…</p>' +
      '<p class="copy-status" role="status">Sending a copy to Britt…</p>' +
      '<div class="test-nav"><button type="button" data-go="pdf" disabled>Save my PDF again</button><button type="button" class="primary" data-go="print" disabled>Print my results</button></div>' +
      '<div class="html-report" hidden></div></main>';
    var pdfUrl = null, bytes = null;
    var build = global.DL2Pdf ? global.DL2Pdf.build(report) : Promise.reject(new Error('PDF library not loaded'));
    build.then(function (b) {
      bytes = b; pdfUrl = download(bytes, filename);
      root.querySelector('.pdf-status').textContent = 'Your PDF is saved in Downloads as ' + filename + '.';
      root.querySelectorAll('[data-go="pdf"],[data-go="print"]').forEach(function (btn) { btn.disabled = false; });
    }).catch(function (err) {
      console.error('DL2 PDF failed', err);
      root.querySelector('.pdf-status').textContent = 'The PDF could not be made on this computer. Your full report is below. Use Print.';
      var box = root.querySelector('.html-report'); box.hidden = false; box.innerHTML = htmlReport(report);
      root.querySelector('[data-go="print"]').disabled = false;
    });
    root.addEventListener('click', function (e) {
      var go = e.target.closest('[data-go]'); if (!go) return;
      if (go.dataset.go === 'pdf' && bytes) download(bytes, filename);
      if (go.dataset.go === 'print') { if (pdfUrl) global.open(pdfUrl, '_blank'); else global.print(); }
    });
    send(payload).then(function () {
      root.querySelector('.copy-status').textContent = '✓ A copy was sent to Britt.';
    }).catch(function () {
      var list = readOutbox(); list.push(payload); writeOutbox(list);
      root.querySelector('.copy-status').textContent = 'Saved on this computer. Tell Britt.';
    });
  }

  function htmlReport(report) {
    var r = report.result;
    return '<div class="paper-doc">' + global.DL2Paper.letterhead({ date: report.submitted }) +
      '<h2>' + report.label + ' · Graded Results</h2><p>Record ' + report.recordId + ' · ' + esc(report.name) + ' · ' + r.correct + '/20</p>' +
      '<table><thead><tr><th>#</th><th>Skill checked</th><th>Your answer</th><th>Correct answer</th><th>Result</th></tr></thead><tbody>' +
      r.rows.map(function (row) {
        return '<tr' + (row.correct ? '' : ' class="miss"') + '><td>' + row.n + '</td><td>' + esc(row.skill) + '</td><td>' + (row.chosen ? row.chosen + ' · ' + esc(row.chosenText) : 'Not answered') + '</td><td>' + row.answer + ' · ' + esc(row.answerText) + '</td><td>' + (row.correct ? '✓ Correct' : '✗ Incorrect') + '</td></tr>';
      }).join('') + '</tbody></table></div>';
  }

  function render() {
    if (st.phase === 'start') renderStart();
    else if (st.phase === 'q') renderQuestion();
    else if (st.phase === 'review') renderReview();
  }

  root.addEventListener('click', function (e) {
    var opt = e.target.closest('.opt');
    if (opt) { st.answers[st.at] = opt.dataset.letter; save(); renderQuestion(); return; }
    var jump = e.target.closest('[data-jump]');
    if (jump) { st.at = Number(jump.dataset.jump); st.phase = 'q'; save(); render(); return; }
    var go = e.target.closest('[data-go]'); if (!go) return;
    var act = go.dataset.go;
    if (act === 'begin') {
      var name = root.querySelector('#name').value.trim().replace(/\s+/g, ' ');
      if (name.length < 2) return renderStart('Please type your name so your results are yours.');
      st.name = name; st.started = new Date().toISOString(); st.phase = 'q'; st.at = 0; save(); render();
    } else if (act === 'next') { if (st.at === 19) st.phase = 'review'; else st.at++; save(); render(); }
    else if (act === 'back') { st.at = Math.max(0, st.at - 1); save(); render(); }
    else if (act === 'last') { st.phase = 'q'; st.at = 19; save(); render(); }
    else if (act === 'submit') root.querySelector('dialog.confirm').showModal();
    else if (act === 'cancel') root.querySelector('dialog.confirm').close();
    else if (act === 'confirm') { root.querySelector('dialog.confirm').close(); submit(); }
  });
  root.addEventListener('keydown', function (e) {
    if (st.phase !== 'q') return;
    var k = e.key.toUpperCase();
    if (LETTERS.indexOf(k) > -1 && !e.target.matches('input')) { st.answers[st.at] = k; save(); renderQuestion(); }
  });

  flushOutbox();
  render();
  global.DL2Test = { state: function () { return st; } };
})(window);
```

- [ ] **Step 7: Write `assessments/pre-test.html` (post-test is identical with `pre`→`post`, `Pre-Test`→`Post-Test`, `dl2-pretest`→`dl2-posttest`)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Pre-Test · Digital Literacy Level 2 · VUB Learning</title>
<link rel="icon" href="/assets/favicon-32.png">
<link rel="stylesheet" href="/courses/digital-literacy-2/os/fonts.css">
<link rel="stylesheet" href="/courses/digital-literacy-2/os/paper.css">
<link rel="stylesheet" href="/courses/digital-literacy-2/os/test.css">
</head>
<body class="dl2-test-page">
<a class="skip" href="#main">Skip to the test</a>
<!-- Text-size host lives outside the re-rendered test root so shared/text-size.js stays bound to it. -->
<div class="vub-appbar test-textsize"><span class="vub-textsize" role="group" aria-label="Text size"><button type="button" data-vub-textsize-minus aria-label="Decrease text size">A−</button><button type="button" data-vub-textsize-plus aria-label="Increase text size">A+</button></span></div>
<div data-dl2-test data-form="pre"></div>
<!-- Registers the form with Netlify at deploy time; the script posts the same fields. -->
<form name="dl2-pretest" data-netlify="true" netlify-honeypot="bot-field" hidden>
  <input type="hidden" name="form-name" value="dl2-pretest">
  <input name="bot-field"><input name="record-id"><input name="student"><input name="form"><input name="started">
  <input name="submitted"><input name="score"><input name="domains"><input name="answers">
</form>
<noscript><p>This test needs JavaScript. Ask Britt for the paper copy.</p></noscript>
<script src="/courses/digital-literacy-2/os/items.js"></script>
<script src="/courses/digital-literacy-2/os/grade.js"></script>
<script src="/courses/digital-literacy-2/os/paper.js"></script>
<script src="/courses/digital-literacy-2/os/vendor/pdf-lib.min.js"></script>
<script src="/courses/digital-literacy-2/os/vendor/fontkit.umd.min.js"></script>
<script src="/courses/digital-literacy-2/os/pdf.js"></script>
<script src="/courses/digital-literacy-2/os/test.js"></script>
<script src="/shared/text-size.js"></script>
</body>
</html>
```

(`pdf.js` arrives in Task 6. Until then the script tag 404s harmlessly and the HTML-report fallback runs.)

- [ ] **Step 8: Run the test to verify it passes**

Run: `npm run build:site && npx playwright test tests/functional/dl2-os-test.spec.js`
Expected: all pass. (The PDF status may show the fallback text until Task 6. The assertions here don't check it.)

- [ ] **Step 9: Commit**

```bash
git add courses/digital-literacy-2/os/paper.* courses/digital-literacy-2/os/test.* courses/digital-literacy-2/assessments/pre-test.html courses/digital-literacy-2/assessments/post-test.html tests/functional/dl2-os-test.spec.js
git commit -m "feat(dl2): 20-question pre/post test with review screen, results copy and offline outbox" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 6: Graded PDF (`pdf.js`)

**Files:**
- Create: `courses/digital-literacy-2/os/pdf.js`
- Test: `tests/functional/dl2-os-pdf.spec.js`

**Interfaces:**
- Consumes: `window.PDFLib`, `window.fontkit` (Task 1), `DL2Paper.META` / `classDate` (Task 5), and the report object `{ form, label, items, result, name, started: Date, submitted: Date, recordId }` (Task 5).
- Produces `DL2Pdf = { build(report) → Promise<Uint8Array> }`. PDF metadata: Title = recordId, Subject = `DL2 <label> graded results`, Author = `West Virginia Veterans Upward Bound`.

- [ ] **Step 1: Write the failing test**

```js
// tests/functional/dl2-os-pdf.spec.js
// Submitting the pre-test downloads a letterhead PDF whose metadata carries the record ID.
const { test, expect } = require('@playwright/test');
const fs = require('fs');
const { PDFDocument } = require('../../courses/digital-literacy-2/os/vendor/pdf-lib.min.js');
const Items = require('../../courses/digital-literacy-2/os/items.js');

test('pre-test PDF: 2 pages, record-id title, named file', async ({ page }) => {
  await page.route('**/', r => r.request().method() === 'POST' ? r.fulfill({ status: 200, body: 'ok' }) : r.continue());
  await page.goto('/courses/digital-literacy-2/assessments/pre-test.html');
  await page.evaluate(() => { try { localStorage.clear(); } catch (e) {} });
  await page.reload();
  await page.getByLabel('Your full name').fill('James Doe');
  await page.getByRole('button', { name: 'Start the pre-test' }).click();
  for (let i = 0; i < 20; i++) {
    await page.locator(`.opt[data-letter="${Items.pre[i].answer}"]`).click();
    await page.getByRole('button', { name: i === 19 ? 'Review answers' : 'Next' }).click();
  }
  await page.getByRole('button', { name: 'Submit my test' }).click();
  const [download] = await Promise.all([page.waitForEvent('download'), page.getByRole('button', { name: 'Yes, submit' }).click()]);
  expect(download.suggestedFilename()).toMatch(/^DL2-PreTest-Doe-\d{8}-\d{4}\.pdf$/);
  const bytes = fs.readFileSync(await download.path());
  expect(bytes.subarray(0, 4).toString()).toBe('%PDF');
  const doc = await PDFDocument.load(bytes);
  expect(doc.getPageCount()).toBe(2);
  expect(doc.getTitle()).toMatch(/^DL2-PRE-\d{8}-\d{4}-JD$/);
  expect(doc.getAuthor()).toBe('West Virginia Veterans Upward Bound');
  await expect(page.locator('.pdf-status')).toContainText('saved in Downloads');
});
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `npm run build:site && npx playwright test tests/functional/dl2-os-pdf.spec.js`
Expected: FAIL (no download event, because pdf.js is missing).

- [ ] **Step 3: Write `os/pdf.js`**

```js
/* DL2 graded-results PDF on the official letterhead (pdf-lib + fontkit, fonts self-hosted).
 * Letter size, 44pt margins. Items 1–14 on page 1, 15–20 plus signatures on page 2. */
(function (global) {
  'use strict';
  var here = (document.currentScript && document.currentScript.src) || location.href;
  var asset = function (p) { return new URL(p, here).href; };
  var NAVY = [27, 54, 93], GOLD = [201, 162, 39], RED = [179, 25, 66], INK = [21, 33, 58], MUTED = [91, 104, 131], RULE = [227, 232, 241], MISS = [253, 245, 246], OK = [29, 107, 58], NO = [163, 20, 47];
  var PW = 612, PH = 792, M = 44;

  function rgbOf(L, c) { return L.rgb(c[0] / 255, c[1] / 255, c[2] / 255); }
  function clean(s) { return String(s).replace(/▸/g, '>').replace(/[✓✗⚠]/g, '').replace(/[“”]/g, '"').replace(/[‘’]/g, "'"); }
  function fetchBytes(url) { return fetch(url).then(function (r) { if (!r.ok) throw new Error(url); return r.arrayBuffer(); }); }
  function wrap(font, text, size, width) {
    var words = clean(text).split(/\s+/), lines = [], line = '';
    words.forEach(function (w) {
      var t = line ? line + ' ' + w : w;
      if (font.widthOfTextAtSize(t, size) > width && line) { lines.push(line); line = w; } else line = t;
    });
    if (line) lines.push(line);
    return lines;
  }
  function spaced(s) { return s.split('').join(' '); }

  function build(report) {
    var L = global.PDFLib, META = global.DL2Paper.META;
    return L.PDFDocument.create().then(function (doc) {
      doc.registerFontkit(global.fontkit);
      var f = {};
      return Promise.all([
        fetchBytes(asset('fonts/playfair-display-latin-800-normal.woff')).then(function (b) { return doc.embedFont(b); }).catch(function () { return doc.embedFont(L.StandardFonts.TimesRomanBold); }),
        fetchBytes(asset('fonts/source-sans-3-latin-400-normal.woff')).then(function (b) { return doc.embedFont(b); }).catch(function () { return doc.embedFont(L.StandardFonts.Helvetica); }),
        fetchBytes(asset('fonts/source-sans-3-latin-700-normal.woff')).then(function (b) { return doc.embedFont(b); }).catch(function () { return doc.embedFont(L.StandardFonts.HelveticaBold); }),
        doc.embedFont(L.StandardFonts.Courier),
        fetchBytes(asset('img/vub-seal-360.png')).then(function (b) { return doc.embedPng(b); }).catch(function () { return null; })
      ]).then(function (res) {
        f.serif = res[0]; f.sans = res[1]; f.bold = res[2]; f.mono = res[3]; var seal = res[4];
        var r = report.result;
        doc.setTitle(report.recordId); doc.setSubject('DL2 ' + report.label + ' graded results');
        doc.setAuthor('West Virginia Veterans Upward Bound'); doc.setCreator('VUB Learning · DL2 Mission Control');
        doc.setCreationDate(report.submitted);

        var p1 = doc.addPage([PW, PH]), p2 = doc.addPage([PW, PH]);
        function text(p, s, x, y, size, font, color) { p.drawText(clean(s), { x: x, y: y, size: size, font: font, color: rgbOf(L, color || INK) }); }
        function right(p, s, xr, y, size, font, color) { text(p, s, xr - font.widthOfTextAtSize(clean(s), size), y, size, font, color); }
        function line(p, x1, y1, x2, y2, w, color) { p.drawLine({ start: { x: x1, y: y1 }, end: { x: x2, y: y2 }, thickness: w, color: rgbOf(L, color) }); }
        function box(p, x, y, w, h, fill, border) { p.drawRectangle({ x: x, y: y, width: w, height: h, color: fill ? rgbOf(L, fill) : undefined, borderColor: border ? rgbOf(L, border) : undefined, borderWidth: border ? 0.8 : 0 }); }

        function letterhead(p) {
          box(p, 0, PH - 8, PW * 0.6, 8, NAVY); box(p, PW * 0.6, PH - 8, PW * 0.2, 8, GOLD); box(p, PW * 0.8, PH - 8, PW * 0.2, 8, RED);
          if (seal) p.drawImage(seal, { x: M, y: PH - 116, width: 74, height: 74 });
          text(p, spaced(META.state), M + 88, PH - 58, 7.5, f.bold, [138, 109, 18]);
          text(p, META.org, M + 88, PH - 84, 21, f.serif, NAVY);
          text(p, META.trio, M + 88, PH - 100, 8.5, f.sans, MUTED);
          var mx = 392, my = PH - 56, rows = [['Course', META.course], ['Cohort', META.cohort], ['Instructor', META.instructor], ['Date & time', global.DL2Paper.classDate(report.submitted)], ['Location', META.location]];
          line(p, mx - 8, my + 10, mx - 8, my - 60, 1.6, GOLD);
          rows.forEach(function (row, k) { text(p, row[0], mx, my - k * 12.5, 7.5, f.bold, NAVY); text(p, row[1], mx + 50, my - k * 12.5, 7.5, f.sans, INK); });
          line(p, M, PH - 130, PW - M, PH - 130, 1.6, NAVY); line(p, M, PH - 134, PW - M, PH - 134, 0.7, GOLD);
        }
        function footer(p, n) {
          line(p, M, 40, PW - M, 40, 0.5, RULE);
          text(p, 'Page ' + n + ' of 2 · Record ' + report.recordId, M, 28, 7.5, f.sans, MUTED);
          right(p, 'Scores guide practice. They are not a certification.', PW - M, 28, 7.5, f.sans, MUTED);
        }
        function tableHead(p, y) {
          var cols = [[M, '#'], [M + 18, 'SKILL CHECKED'], [M + 212, 'YOUR ANSWER'], [M + 338, 'CORRECT ANSWER'], [M + 470, 'RESULT']];
          cols.forEach(function (c) { text(p, c[1], c[0], y, 6.8, f.bold, MUTED); });
          line(p, M, y - 5, PW - M, y - 5, 1.2, NAVY);
          return y - 7;
        }
        function row(p, y, rw) {
          var size = 8, lh = 10, skill = wrap(f.sans, rw.skill, size, 186), mine = wrap(f.sans, rw.chosen ? rw.chosen + ' · ' + rw.chosenText : 'Not answered', size, 118), key = wrap(f.sans, rw.answer + ' · ' + rw.answerText, size, 124);
          var n = Math.max(skill.length, mine.length, key.length), h = n * lh + 8;
          if (!rw.correct) box(p, M, y - h, PW - 2 * M, h, MISS);
          text(p, String(rw.n), M + 2, y - 12, size, f.bold, NAVY);
          skill.forEach(function (s, k) { text(p, s, M + 18, y - 12 - k * lh, size, f.sans); });
          mine.forEach(function (s, k) { text(p, s, M + 212, y - 12 - k * lh, size, f.sans); });
          key.forEach(function (s, k) { text(p, s, M + 338, y - 12 - k * lh, size, f.sans); });
          var ok = rw.correct, cx = M + 472, cy = y - 10;
          if (ok) { line(p, cx, cy, cx + 3, cy - 3, 1.3, OK); line(p, cx + 3, cy - 3, cx + 8, cy + 4, 1.3, OK); }
          else { line(p, cx, cy + 3, cx + 7, cy - 4, 1.3, NO); line(p, cx, cy - 4, cx + 7, cy + 3, 1.3, NO); }
          text(p, ok ? 'Correct' : 'Incorrect', cx + 12, y - 12, size, f.bold, ok ? OK : NO);
          line(p, M, y - h, PW - M, y - h, 0.5, RULE);
          return y - h;
        }

        // Page 1
        letterhead(p1);
        text(p1, report.label + ' · Graded Results', M, PH - 164, 17, f.serif, NAVY);
        right(p1, 'Record ' + report.recordId, PW - M, PH - 156, 7.5, f.mono, MUTED);
        right(p1, 'Form: ' + report.form + ' ' + global.DL2Items.version + ' · 20 items', PW - M, PH - 166, 7.5, f.mono, MUTED);
        var by = PH - 222, t = function (d) { return d.toLocaleTimeString('en-US', { hour: 'numeric', minute: '2-digit' }); };
        var mins = Math.max(1, Math.round((report.submitted - report.started) / 60000));
        box(p1, M, by, 190, 42, null, RULE); text(p1, 'STUDENT', M + 9, by + 28, 6.8, f.bold, MUTED); text(p1, report.name, M + 9, by + 12, 10.5, f.sans);
        box(p1, M + 198, by, 160, 42, null, RULE); text(p1, 'STARTED / SUBMITTED', M + 207, by + 28, 6.8, f.bold, MUTED); text(p1, t(report.started) + ' / ' + t(report.submitted) + ' (' + mins + ' min)', M + 207, by + 12, 9.5, f.sans);
        box(p1, M + 366, by, PW - 2 * M - 366, 42, NAVY); text(p1, r.correct + '/' + r.total, M + 378, by + 12, 22, f.serif, [255, 255, 255]);
        text(p1, 'SCORE', M + 452, by + 26, 6.8, f.bold, [201, 214, 238]); text(p1, r.percent + '% correct', M + 452, by + 12, 9.5, f.sans, [255, 255, 255]);
        var dy = by - 18;
        r.byDomain.forEach(function (d, k) {
          var col = k % 2, rowk = Math.floor(k / 2), x = M + col * 266, y = dy - rowk * 14;
          text(p1, d.name, x, y, 8, f.sans);
          box(p1, x + 128, y, 90, 6, RULE); box(p1, x + 128, y, 90 * (d.total ? d.correct / d.total : 0), 6, NAVY);
          right(p1, d.correct + '/' + d.total, x + 250, y, 8, f.bold, NAVY);
        });
        var y1 = tableHead(p1, dy - 70);
        r.rows.slice(0, 14).forEach(function (rw) { y1 = row(p1, y1, rw); });
        footer(p1, 1);

        // Page 2
        box(p2, 0, PH - 8, PW * 0.6, 8, NAVY); box(p2, PW * 0.6, PH - 8, PW * 0.2, 8, GOLD); box(p2, PW * 0.8, PH - 8, PW * 0.2, 8, RED);
        if (seal) p2.drawImage(seal, { x: M, y: PH - 76, width: 40, height: 40 });
        text(p2, META.org + ' · ' + report.label + ' · Graded Results (continued)', M + 50, PH - 58, 11, f.serif, NAVY);
        text(p2, report.name + ' · Record ' + report.recordId, M + 50, PH - 72, 8, f.sans, MUTED);
        line(p2, M, PH - 86, PW - M, PH - 86, 1.2, NAVY);
        var y2 = tableHead(p2, PH - 108);
        r.rows.slice(14).forEach(function (rw) { y2 = row(p2, y2, rw); });
        var sy = y2 - 90;
        line(p2, M, sy, M + 240, sy, 0.8, INK); text(p2, 'Student signature', M, sy - 12, 8, f.sans, MUTED); line(p2, M + 260, sy, M + 330, sy, 0.8, INK); text(p2, 'Date', M + 260, sy - 12, 8, f.sans, MUTED);
        line(p2, M, sy - 50, M + 240, sy - 50, 0.8, INK); text(p2, 'Instructor signature · ' + META.instructor, M, sy - 62, 8, f.sans, MUTED); line(p2, M + 260, sy - 50, M + 330, sy - 50, 0.8, INK); text(p2, 'Date', M + 260, sy - 62, 8, f.sans, MUTED);
        footer(p2, 2);
        return doc.save();
      });
    });
  }
  global.DL2Pdf = { build: build };
})(window);
```

- [ ] **Step 4: Run the test to verify it passes**

Run: `npm run build:site && npx playwright test tests/functional/dl2-os-pdf.spec.js tests/functional/dl2-os-test.spec.js`
Expected: all pass.

- [ ] **Step 5: Visual check**

Open the downloaded PDF from a manual run (`npx serve dist/site -l 3939`, take the test) and compare page 1 with mockup 3. Required: the letterhead lines don't overlap the meta block, no text runs past the right margin, and wrong rows are shaded. Fix the coordinates if needed and re-run Step 4.

- [ ] **Step 6: Commit**

```bash
git add courses/digital-literacy-2/os/pdf.js tests/functional/dl2-os-pdf.spec.js
git commit -m "feat(dl2): graded results PDF on official letterhead" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 7: Answer keys, printable paper backups, syllabus alignment

**Files:**
- Create: `courses/digital-literacy-2/os/keys.js`
- Replace: `assessments/pre-test-answer-key.html`, `assessments/post-test-answer-key.html`, `assessments/pre-test-printable.html`, `assessments/post-test-printable.html`
- Modify: `courses/digital-literacy-2/syllabus.html` (one sentence)
- Test: `tests/content/dl2-os-keys.spec.js`

**Interfaces:**
- Consumes: `DL2Items`, `DL2Paper.letterhead` (Tasks 4–5).
- Produces pages with `<main class="paper-doc" data-dl2-doc="key|printable" data-form="pre|post">`.
  - **Key:** letterhead, the title "<Label> · Answer Key (instructor)", then a table `#, Skill, Domain, Answer (letter + text), Why`.
  - **Printable:** letterhead, a name/date line, instructions, and 20 questions each with ○ A–D bubbles. Items never split across pages.

- [ ] **Step 1: Write the failing test**

```js
// tests/content/dl2-os-keys.spec.js
// Keys and paper tests come from the same item bank as the online test (assessment alignment rule).
const { test, expect } = require('@playwright/test');
const Items = require('../../courses/digital-literacy-2/os/items.js');
const A = '/courses/digital-literacy-2/assessments/';

for (const form of ['pre', 'post']) {
  test(`${form} key lists all 20 answers with reasons`, async ({ page }) => {
    await page.goto(`${A}${form}-test-answer-key.html`);
    await expect(page.locator('.letterhead')).toContainText('Veterans Upward Bound');
    const rows = page.locator('tbody tr');
    await expect(rows).toHaveCount(20);
    for (const i of [0, 9, 19]) await expect(rows.nth(i)).toContainText(Items[form][i].answer + ' · ');
  });
  test(`${form} printable has 20 questions with four bubbles each`, async ({ page }) => {
    await page.goto(`${A}${form}-test-printable.html`);
    await expect(page.locator('.pq')).toHaveCount(20);
    await expect(page.locator('.pq').first().locator('.bubble')).toHaveCount(4);
    await expect(page.locator('.pq').nth(19)).toContainText(Items[form][19].stem.slice(0, 30));
  });
}

test('syllabus states 20 questions', async ({ page }) => {
  await page.goto('/courses/digital-literacy-2/syllabus.html');
  await expect(page.locator('main')).toContainText('Each has 20 questions across the seven IC3 domains');
  await expect(page.locator('main')).not.toContainText('28 questions');
});
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `npm run build:site && npx playwright test tests/content/dl2-os-keys.spec.js`
Expected: FAIL.

- [ ] **Step 3: Write `os/keys.js`**

```js
/* Renders DL2 answer keys and printable paper tests from the item bank. */
(function (global) {
  'use strict';
  var root = document.querySelector('[data-dl2-doc]');
  if (!root) return;
  var form = root.dataset.form === 'post' ? 'post' : 'pre', label = form === 'pre' ? 'Pre-Test' : 'Post-Test';
  var items = global.DL2Items[form], esc = global.DL2Paper.esc, L = ['A', 'B', 'C', 'D'];
  var dom = {}; global.DL2Items.domains.forEach(function (d) { dom[d.id] = d.name; });
  var head = global.DL2Paper.letterhead({ dateText: 'Class meeting · ' + global.DL2Paper.META.classTime });
  if (root.dataset.dl2Doc === 'key') {
    root.innerHTML = head + '<h1 class="doc-h1">' + label + ' · Answer Key <small>(instructor)</small></h1>' +
      '<p class="doc-sub">Form ' + form + ' ' + global.DL2Items.version + '. Item N checks the same skill on both forms.</p>' +
      '<table class="key"><thead><tr><th>#</th><th>Skill · domain</th><th>Answer</th><th>Why</th></tr></thead><tbody>' +
      items.map(function (it) {
        return '<tr><td>' + it.n + '</td><td>' + esc(it.skill) + '<br><small>' + dom[it.domain] + ' · Week ' + it.week + '</small></td><td><strong>' + it.answer + ' · ' + esc(it.options[L.indexOf(it.answer)]) + '</strong></td><td>' + esc(it.why) + '</td></tr>';
      }).join('') + '</tbody></table>';
  } else {
    root.innerHTML = head + '<h1 class="doc-h1">' + label + ' · Paper copy</h1>' +
      '<div class="namerow"><span>Name</span><span>Date</span></div>' +
      '<p class="doc-sub">Fill in one circle for each question. 20 questions.</p>' +
      items.map(function (it) {
        return '<section class="pq"><h2><b>' + it.n + '.</b> ' + esc(it.stem) + '</h2><div class="pq-opts">' +
          it.options.map(function (o, k) { return '<div class="pq-opt"><span class="bubble" aria-hidden="true">○</span><b>' + L[k] + '</b> ' + esc(o) + '</div>'; }).join('') + '</div></section>';
      }).join('');
  }
})(window);
```

Add to `paper.css`: `.doc-h1{font-family:"Playfair Display",serif;color:var(--navy);font-size:20pt;margin:14pt 0 4pt}`, `.doc-sub{color:#4a5874}`, `table.key{width:100%;border-collapse:collapse;font-size:10.5pt}`, `table.key th{text-align:left;border-bottom:2pt solid var(--navy);font-size:8.5pt;letter-spacing:.1em;text-transform:uppercase;color:#5b6883}`, `table.key td{border-bottom:1px solid var(--rule);padding:5pt 4pt;vertical-align:top}`, `.pq{break-inside:avoid;margin:10pt 0;padding:8pt 10pt;border:1px solid var(--rule);border-radius:6pt}`, `.pq h2{font-size:12pt;margin:0 0 6pt;font-weight:600}`, `.pq-opts{display:grid;grid-template-columns:1fr 1fr;gap:4pt 14pt}`, `.bubble{font-size:15pt;margin-right:4pt}`, and `.namerow{display:grid;grid-template-columns:2fr 1fr;gap:24pt;margin:12pt 0}` with `.namerow span{border-bottom:1px solid var(--ink)}`.

- [ ] **Step 4: Write the four pages**

Each page is the following, varying `data-dl2-doc`, `data-form` and the `<title>`:

```html
<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Pre-Test Answer Key · Digital Literacy Level 2</title>
<link rel="stylesheet" href="/courses/digital-literacy-2/os/fonts.css"><link rel="stylesheet" href="/courses/digital-literacy-2/os/paper.css"></head>
<body><div class="no-print paper-actions"><button type="button" onclick="print()">Print</button></div>
<main class="paper-doc" data-dl2-doc="key" data-form="pre"></main>
<script src="/courses/digital-literacy-2/os/items.js"></script><script src="/courses/digital-literacy-2/os/paper.js"></script>
<script src="/courses/digital-literacy-2/os/keys.js"></script><script src="/shared/text-size.js"></script></body></html>
```

- [ ] **Step 5: Edit the syllabus sentence**

In `courses/digital-literacy-2/syllabus.html`, replace `Each has 28 questions, four per domain, and produces printable graded results.` with `Each has 20 questions across the seven IC3 domains, and produces printable graded results.` Change nothing else.

- [ ] **Step 6: Run the test to verify it passes**

Run: `npm run build:site && npx playwright test tests/content/dl2-os-keys.spec.js`
Expected: 5 passed.

- [ ] **Step 7: Commit**

```bash
git add courses/digital-literacy-2/os/keys.js courses/digital-literacy-2/os/paper.css courses/digital-literacy-2/assessments/*answer-key.html courses/digital-literacy-2/assessments/*printable.html courses/digital-literacy-2/syllabus.html tests/content/dl2-os-keys.spec.js
git commit -m "feat(dl2): letterhead answer keys and paper backups from the item bank; syllabus says 20 questions" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 8: Week 1 demos (Settings, Quick Settings, Word, Outlook)

**Files:**
- Modify: `courses/digital-literacy-2/os/win11.css` (add the Quick Settings, Word and Outlook kits)
- Create: `courses/digital-literacy-2/os/demos/week-01.js`
- Test: `tests/functional/dl2-os-week1-demos.spec.js`

**Interfaces:**
- Consumes: `DL2Demo.define` (Task 3).
- Produces five demo ids: `w1-scale`, `w1-sound`, `w1-print`, `w1-calendar` and `w1-autocorrect`.

Scene rules (all demos): 1280×720 authored pixels, the Windows 11 light theme, Bloom-style blue wallpaper (`.w11-wall`), and a centered taskbar with Start, Search, File Explorer, Edge, Word, Outlook and Settings icons (show only apps relevant to the demo, with `.open` under the running app). Clock `4:52 PM` / `9/28/2026`. Use `div`/`span` only for Windows text. All names and data are fictional: user "Veteran Learner", organization "Community Skills Desk".

**`w1-scale`**: port directly from mockup 2 (System page → Display → Scale flyout → 125% → the whole `.w11-win` grows via `--ui` 14px→17.5px).

| # | check | cap | target / action | state |
|:--|:--|:--|:--|:--|
| 1 | System page | Settings is open to the <em>System</em> page. | none | `attr:{page:'system'}` |
| 2 | Click Display | Click <em>Display</em>. | `#card-display` click, `at:[.3,.5]` | `attr:{page:'display'}` |
| 3 | Open Scale | Under Scale &amp; layout, open the <em>Scale</em> menu. | `#scale-dd` click | `cls:{'menu-open':true}` |
| 4 | Choose 125% | Choose <em>125%</em>. Everything gets bigger, right away. | `#opt-125` click, `zoomOut:true` | `cls:{'menu-open':false}, css:{'--ui':'17.5px'}, text:{'#scale-val':'125%'}` |
| 5 | Check, then undo | Check each app. To undo it, choose <em>100%</em> again. | none | none |

**`w1-sound`**: the desktop with the taskbar tray showing network, speaker and battery icons (`#tray-sound` wraps the speaker). The Quick Settings flyout (`.w11-qs`, bottom-right above the taskbar, 360×400) has Wi-Fi, Bluetooth, Airplane mode, Accessibility tiles, a brightness slider row, and a volume row: a speaker icon, a slider at 40%, and a `#qs-output` chevron button (`>`, aria "Select a sound output"). The Sound output panel (`.w11-qs-out`, the same flyout area) has the title "Sound output" and rows `#out-speakers` "Speakers (Realtek(R) Audio)" (✓ selected initially), `#out-headphones` "Headphones (USB Audio Device)", a divider, and the link "More volume settings".

| # | check | cap | target / action | state |
|:--|:--|:--|:--|:--|
| 1 | Headset plugged in | Plug your headset in first. Sound is still going to the speakers. | none | `attr:{qs:'closed',out:'speakers'}` |
| 2 | Click the speaker | Click the <em>speaker</em> icon on the taskbar. | `#tray-sound` click | `attr:{qs:'open'}` |
| 3 | Open outputs | Click the arrow beside the volume slider. | `#qs-output` click | `attr:{qs:'outputs'}` |
| 4 | Pick headphones | Choose <em>Headphones</em>. | `#out-headphones` click | `attr:{out:'headphones'}` |
| 5 | Test it | Play a sound. It should be in your headset now. | `#out-headphones` hover, `zoom:false` | none |

CSS: `.screen[data-qs="closed"] .w11-qs{display:none}`, `.screen[data-qs="open"] .w11-qs-out{display:none}`, `.screen[data-qs="outputs"] .w11-qs-main{display:none}`, `.screen[data-out="speakers"] #out-speakers .tick, .screen[data-out="headphones"] #out-headphones .tick{visibility:visible}` (`.tick` is hidden by default and shows "✓").

**`w1-print`**: a Word window titled "Community Supper Flyer.docx - Word". Its File ▸ Print backstage view (`[data-page="print"]`) has a left rail (Home, New, Open, Info, Save, Save As, **Print** selected, Share, Export, Close, Account), the Print column (a Copies box "1", a Print button `#print-btn`, Printer "Lab Printer (HP LaserJet)"), a Settings list (Print All Pages, Print One Sided, Collated, Portrait Orientation, Letter, and `#margins-dd` "Normal Margins"), a flyout `.w11-flyout` with `#m-normal` Normal, `#m-narrow` Narrow (0.5" all sides), Moderate and Wide, and a preview pane. The preview shows `.pv-page` with the flyer (title "Community Supper", date line, 8 lines of details) and a `#pv-count` pager reading "1 of 2". A second small page shows the one spilled line when `data-margins="normal"`.

| # | check | cap | target / action | state |
|:--|:--|:--|:--|:--|
| 1 | Open Print | Press <kbd>Ctrl</kbd> + <kbd>P</kbd> (or File ▸ Print) to see the preview. | none | `attr:{page:'print',margins:'normal'}` |
| 2 | Spot the spill | The preview says <em>1 of 2</em>. One line spilled onto page 2. | `#pv-count` hover | none |
| 3 | Open margins | Under Settings, click <em>Normal Margins</em>. | `#margins-dd` click | `cls:{'menu-open':true}` |
| 4 | Choose Narrow | Choose <em>Narrow</em>. | `#m-narrow` click, `zoomOut:true` | `cls:{'menu-open':false}, attr:{margins:'narrow'}, text:{'#pv-count':'1 of 1','#margins-val':'Narrow Margins'}` |
| 5 | Print one test copy | One page now. Print <em>one</em> test copy first. | `#print-btn` click | none |

**`w1-calendar`**: the new Outlook window: a left app bar (Mail, **Calendar** selected, People), a toolbar with a `#new-event` button "New event", and Week view Sep 27 – Oct 3, 2026 (Sun–Sat columns, 8 AM – 7 PM rows). A `#next-week` arrow shows Oct 4 – 10 when `data-week="2"`. The event form (`.ol-form`, shown when `data-form="open"`) has a `#ev-title` title box "Add a title", `#ev-attendees` "Invite attendees", a date "Mon 9/28/2026", times "4:30 PM" to "6:30 PM", a `#ev-repeat` dropdown "Don't repeat" with options `#rep-weekly` "Weekly on Monday", a `#ev-remind` reminder "Remind me: 15 minutes before", and a `#ev-save` Save button. After saving, the event block "VUB class" shows on Monday 4:30–6:30 PM with a ↻ repeat icon. On week 2, the same block shows on Monday Oct 5.

| # | check | cap | target / action | state |
|:--|:--|:--|:--|:--|
| 1 | Calendar open | Outlook is open to <em>Calendar</em>, Week view. | none | `attr:{form:'closed',week:'1',saved:'no'}` |
| 2 | New event | Click <em>New event</em>. | `#new-event` click | `attr:{form:'open'}` |
| 3 | Add a title | Type a clear title. | `#ev-title` type "VUB class" | none |
| 4 | Make it repeat | Set Repeat to <em>Weekly on Monday</em>. | `#ev-repeat` click → then `#rep-weekly` click (two steps: 4a opens with `cls:{'menu-open':true}`, 4b selects with `cls:{'menu-open':false}, text:{'#ev-repeat-val':'Weekly on Monday'}`) | as noted |
| 5 | Invite and save | Invite your partner, keep the 15-minute reminder, then <em>Save</em>. | `#ev-save` click, `zoomOut:true` | `attr:{form:'closed',saved:'yes'}` |
| 6 | Check next week | Click the next-week arrow. Is it on <em>Monday</em>? | `#next-week` click | `attr:{week:'2'}` |

(Step 4 becomes two table rows in code, so the demo has 7 steps.)

**`w1-autocorrect`**: a Word window "Help Desk Note.docx - Word" with the Home ribbon (Clipboard, Font, Paragraph, Styles groups drawn as simple labeled blocks) and a document page. `#doc-line` holds the text being typed. An `#ac-button` AutoCorrect Options lightning button (shows when `data-ac="shown"`) has a menu `#ac-undo` "Change back to "(c)"" and "Stop Automatically Correcting "(c)"". The File ▸ Account page (`data-page="account"`) shows Product Information "Microsoft 365" and `#about-word` "About Word". The About panel (`data-about="open"`) reads "Microsoft® Word for Microsoft 365 MSO (Version 2408 Build 16.0.17928.20114) 64-bit".

| # | check | cap | target / action | state |
|:--|:--|:--|:--|:--|
| 1 | Word open | A note in Word. Watch what happens when we type <em>(c)</em>. | none | `attr:{page:'doc',ac:'none',about:'closed'}` |
| 2 | Type (c) | Type <em>Copyright (c) 2026</em>. | `#doc-line` type "Copyright (c) 2026" | `text:{'#doc-line':'Copyright © 2026'}, attr:{ac:'shown'}` |
| 3 | Spot the change | Word changed <em>(c)</em> into <em>©</em>. That's AutoCorrect. | `#ac-button` click | `cls:{'menu-open':true}` |
| 4 | Change it back | Choose <em>Change back</em>. (Or press <kbd>Ctrl</kbd> + <kbd>Z</kbd> right away.) | `#ac-undo` click | `cls:{'menu-open':false}, text:{'#doc-line':'Copyright (c) 2026'}, attr:{ac:'none'}` |
| 5 | Find the version | For a help request: File ▸ Account ▸ <em>About Word</em>. | `#about-word` click | `attr:{page:'account',about:'open'}` |
| 6 | Copy the version | Write down the version number (2408) for your request. | `#about-version` hover, `zoom:2.4` | none |

- [ ] **Step 1: Write the failing test**

```js
// tests/functional/dl2-os-week1-demos.spec.js
// Every Week 1 demo plays to its last step with every target present and no console errors.
const { test, expect } = require('@playwright/test');
const BASE = 'http://localhost:3939/courses/digital-literacy-2/os/';
const IDS = ['w1-scale', 'w1-sound', 'w1-print', 'w1-calendar', 'w1-autocorrect'];

for (const id of IDS) test(`${id} runs to the end`, async ({ page }) => {
  const errors = [];
  page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
  page.on('pageerror', e => errors.push(e.message));
  await page.emulateMedia({ reducedMotion: 'reduce' });
  await page.goto(BASE + 'fonts.css');
  await page.setContent(`<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><base href="${BASE}">
    <link rel="stylesheet" href="fonts.css"><link rel="stylesheet" href="deck.css"><link rel="stylesheet" href="win11.css"></head>
    <body class="dl2-os"><div class="demo" data-demo="${id}" style="width:1600px;height:700px"></div>
    <script src="demo.js"></script><script src="demos/week-01.js"></script></body></html>`, { waitUntil: 'load' });
  const total = await page.locator('.demo-todo li').count();
  expect(total).toBeGreaterThanOrEqual(5);
  for (let i = 1; i < total; i++) {
    await page.locator('[data-act="next"]').click();
    await expect(page.locator('.demo-stepno')).toHaveText(`STEP ${i + 1} / ${total}`);
  }
  expect(await page.evaluate(k => DL2Demo.get(k).next(), id)).toBe(false);
  expect(errors).toEqual([]);
});

test('scale demo ends at 125% with a bigger window', async ({ page }) => {
  await page.emulateMedia({ reducedMotion: 'reduce' });
  await page.goto(BASE + 'fonts.css');
  await page.setContent(`<!DOCTYPE html><html><head><base href="${BASE}"><link rel="stylesheet" href="win11.css"></head><body><div class="demo" data-demo="w1-scale" style="width:1600px"></div><script src="demo.js"></script><script src="demos/week-01.js"></script></body></html>`, { waitUntil: 'load' });
  for (let i = 0; i < 4; i++) await page.locator('[data-act="next"]').click();
  await expect(page.locator('#scale-val')).toHaveText('125%');
});
```

The engine already logs `console.error` for a missing target, so the `errors` assertion catches any mis-authored selector.

- [ ] **Step 2: Run the test to verify it fails**

Run: `npm run build:site && npx playwright test tests/functional/dl2-os-week1-demos.spec.js`
Expected: FAIL (`no demo named w1-scale`).

- [ ] **Step 3: Write `os/demos/week-01.js`**

Structure (repeat for each demo; scene HTML strings are built from small helpers so the taskbar and window chrome are shared):

```js
/* Week 1 Show demos: Windows 11 + Microsoft 365, fictional data. Scenes are 1280×720. */
(function () {
  'use strict';
  var I = { /* inline SVG icon strings: start, search, explorer, edge, word, outlook, settings, speaker, wifi, battery, gear, calendar, mail, people, bolt, repeat */ };
  function taskbar(apps, open) {
    return '<div class="w11-taskbar">' + apps.map(function (a) { return '<span class="w11-tbi' + (a === open ? ' open' : '') + '" data-app="' + a + '">' + I[a] + '</span>'; }).join('') +
      '<span class="w11-tray"><span class="w11-tray-icons"><span>' + I.wifi + '</span><span id="tray-sound">' + I.speaker + '</span><span>' + I.battery + '</span></span><span class="w11-clock">4:52 PM<br>9/28/2026</span></span></div>';
  }
  function win(title, icon, body, cls) {
    return '<div class="w11-win ' + (cls || '') + '"><div class="w11-title">' + I[icon] + '<span>' + title + '</span><span class="w11-ctl"><span>—</span><span>☐</span><span>✕</span></span></div>' + body + '</div>';
  }
  DL2Demo.define({ id: 'w1-scale', title: 'Change display scale in Settings', start: [640, 420],
    scene: '<div class="w11-wall"></div>' + win('Settings', 'gear', /* nav + System page + Display page, ported from mockup 2 */ '', 'w11-settings') + taskbar(['start', 'search', 'explorer', 'edge', 'settings'], 'settings'),
    steps: [ /* the rows from the w1-scale table above, as Step objects */ ] });
  /* w1-sound, w1-print, w1-calendar, w1-autocorrect: same pattern, using the tables above */
})();
```

Write every scene fully (no empty strings in the final file). Use the tables above verbatim for `cap` and `check`. Put the Word ribbon, backstage and Outlook calendar CSS in `win11.css` under the `ol-*` and `wd-*` prefixes. Keep the Windows 11 details accurate: Segoe UI, 4px corners on controls and 8px on windows, the `#005fb8` accent, `#f3f3f3` Mica-grey window background, `#fbfbfb` cards with `#e5e5e5` borders, and the Word title bar in `#185abd` Word blue with a white title. The new Outlook uses a `#0f6cbd` accent with a white surface.

- [ ] **Step 4: Run the test to verify it passes**

Run: `npm run build:site && npx playwright test tests/functional/dl2-os-week1-demos.spec.js`
Expected: 6 passed.

- [ ] **Step 5: Screenshot review at 1920×1080**

For each demo, capture every step (motion allowed) with a throwaway script. Check that each capture looks like Windows 11 / Microsoft 365, that the cursor lands on the right control, that the zoom frames the control, and that no text overflows. Fix and re-run Step 4.

- [ ] **Step 6: Commit**

```bash
git add courses/digital-literacy-2/os/win11.css courses/digital-literacy-2/os/demos/week-01.js tests/functional/dl2-os-week1-demos.spec.js
git commit -m "feat(dl2): five Week 1 Show demos (display scale, sound output, print margins, Outlook series, AutoCorrect + version)" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 9: Week 1 deck (`presentation.html`)

**Files:**
- Rename: `courses/digital-literacy-2/weeks/week-01/presentation.html` → `presentation-legacy.html` (`git mv`, content unchanged)
- Create: `courses/digital-literacy-2/weeks/week-01/presentation.html`
- Test: `tests/functional/dl2-os-week1-deck.spec.js`

**Interfaces:**
- Consumes: the Task 2 deck contract, the Task 8 demo ids, and `os/img/vub-seal-360.png` (not white). Use `/assets/vub-seal-white.png` on dark slides.

Page shell:

```html
<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Week 1 · Make technology work for you · Digital Literacy Level 2</title>
<link rel="icon" href="/assets/favicon-32.png">
<link rel="stylesheet" href="/courses/digital-literacy-2/os/fonts.css">
<link rel="stylesheet" href="/courses/digital-literacy-2/os/deck.css">
<link rel="stylesheet" href="/courses/digital-literacy-2/os/win11.css"></head>
<body class="dl2-os"><main class="deck" aria-label="Week 1 slides. Use the arrow keys.">
  <!-- slides below -->
</main>
<script src="/courses/digital-literacy-2/os/deck.js"></script>
<script src="/courses/digital-literacy-2/os/demo.js"></script>
<script src="/courses/digital-literacy-2/os/demos/week-01.js"></script>
<script src="/shared/text-size.js"></script></body></html>
```

Slide list (exact content; `B:` marks a `.build` element; HUD text is `<div class="hud"><img src="/assets/vub-seal-white.png" alt=""> …</div>`):

| # | phase / stage / scene / minutes | Content |
|:--|:--|:--|
| 1 | — / — / gorge | Opener (`.panel.bare .opener`): seal; kicker `MISSION 01 OF 06 // DIGITAL LITERACY L2`; h1 "Make technology work for you"; chips: Readable text · Right speaker · Clean print · Shared calendar · Clear help request; `.where` "NEW RIVER CTC / MON 09·28·2026 · 16:30"; `.go` "PRESS → TO BEGIN". Notes: welcome, names, where the restrooms are, the class runs 4:30–6:30 with one break. |
| 2 | — / — / gorge / 20 | Pre-test (`.panel.center`): h1 "First: a 20-minute check-in"; B: "Open the course page ▸ <kbd>Pre-test</kbd>"; B: "Type your name. One question per screen."; B: "Review, then Submit. Your PDF saves itself."; B: "It shows where to start. It's not a grade." Notes: press T for the 20-minute timer; the paper copy is in `assessments/pre-test-printable.html`. |
| 3 | warm-up / — / deck | HUD `WK-01 // WARM-UP`. h1 "It's Monday night." B: "Frank's VA appointment reminder popped up on <em>Tuesday</em>." B: "The words on his screen are so small he squints." B: "His video visit starts. The sound blasts from the speakers, not his headset." B: "His flyer prints on <em>two</em> pages." B (h2): "Sound familiar? Tonight we fix all of it." Notes: ask "Has this happened to you?" and let two people answer. |
| 4 | intro / — / deck | HUD `WK-01 // TONIGHT'S MISSION`. h1 "Make the computer fit <em>you</em>." `.steps` with B items: A "Make text readable, then put it back"; B "Send sound to the right device"; C "Print one clean page"; D "Make a calendar entry others can act on"; E "Undo an automatic change and ask for help clearly". Notes: why it matters: independence at home, telehealth, appointments. |
| 5 | present / tell / deck (Unit A) | HUD `WK-01 // UNIT A`. h1 "Text too small?<br><em>Fix it for the whole computer.</em>" steps B: 01 "Open <kbd>Settings</kbd> ▸ System ▸ Display"; 02 "Scale &amp; layout ▸ Scale ▸ <kbd>125%</kbd>"; 03 "Check every app, then set it back to 100%". Notes: browser zoom (Ctrl +) only changes web pages; Scale changes everything. |
| 6 | present / show / deck | HUD `WK-01 // UNIT A // TEXT TOO SMALL`. `<div class="demo" data-demo="w1-scale"></div>` inside `.panel.full`. Notes: then do it live on the room PC if anyone wants to see it again. |
| 7 | practice / do / deck / 10 | Do slide per mockup 4: h1 "Make text readable,<br><em>then put it back.</em>"; Point A "Scale is 100%. Text looks small."; Point B "Tried 125%, checked 2 apps, back to 100%."; the 5 steps "Open Settings", "System ▸ Display", "Scale ▸ 125%", "Check 2 apps", "Back to 100%"; `.sheet` "▸ WORKSHEET 1A · RAISE YOUR HAND IF STEP 3 LOOKS DIFFERENT". |
| 8 | evaluate / review / deck | h1 "Browser zoom fixed one website. What fixes <em>every</em> app?" B (answer card): "Display <strong>Scale</strong> in Settings ▸ System ▸ Display." B: "Why: Scale resizes Windows and every app. Browser zoom only resizes web pages." |
| 9 | present / tell / deck (Unit B) | h1 "Sound in the wrong place?<br><em>Pick the output.</em>" steps B: 01 "Plug in the headset first"; 02 "Click the <kbd>speaker</kbd> on the taskbar ▸ the arrow beside the volume slider"; 03 "Choose <kbd>Headphones</kbd>, then play a sound". |
| 10 | present / show | `data-demo="w1-sound"` |
| 11 | practice / do / 7 | Mission 1B: Point A "Sound plays from the speakers." Point B "A test sound plays in your headset, and you know how to switch back." Steps: "Plug in headset", "Click speaker icon", "Open outputs (›)", "Choose Headphones", "Play a test sound". `.sheet` "▸ WORKSHEET 1B" |
| 12 | evaluate / review | h1 "Video call sound comes from the speakers, not your headset. Check first?" B: "The <strong>sound output</strong> device: speaker icon ▸ › ▸ Headphones." B: "Why: Windows sends sound to one output at a time. Plugging in doesn't always switch it." |
| 13 | — / — / gorge / 10 | Break (`.panel.bare`): kicker `INTERMISSION`; h1 "Ten-minute break"; p "Stand up, stretch, refill. Back at 5:35." Notes: press T to start the 10-minute countdown. |
| 14 | present / tell (Unit C) | h1 "One page means <em>one page.</em>" steps B: 01 "<kbd>Ctrl</kbd> + <kbd>P</kbd>: read the preview. Does it say 1 of 2?"; 02 "Settings ▸ <kbd>Normal Margins</kbd> ▸ Narrow"; 03 "Preview says 1 of 1? Print <em>one</em> test copy". Notes: Layout tab ▸ Margins is the same setting. |
| 15 | present / show | `data-demo="w1-print"` |
| 16 | practice / do / 12 | Mission 1C: Point A "The Community Supper flyer previews as 1 of 2." Point B "The preview says 1 of 1 and one test copy is printed." Steps: "Open the flyer", "Ctrl + P", "Narrow margins", "Check 1 of 1", "Print 1 copy". `.sheet` "▸ WORKSHEET 1C · FILE: Community Supper Flyer.docx" |
| 17 | evaluate / review | h1 "The preview shows page 2 with one line. First move?" B: "Adjust the layout (margins), then <strong>check the preview again</strong>." B: "Why: you keep every word, and you only print once it fits." |
| 18 | present / tell (Unit D) | h1 "A calendar entry<br><em>others can act on.</em>" steps B: 01 "Outlook ▸ Calendar ▸ <kbd>New event</kbd>"; 02 "Clear title, date, time, and Repeat: Weekly on Monday"; 03 "Invite, keep a reminder, then Save"; 04 "Check next week: is it on Monday?" |
| 19 | present / show | `data-demo="w1-calendar"` |
| 20 | practice / do / 12 | Mission 1D: Point A "No reminder for class." Point B "A weekly Monday 4:30 PM event with a reminder, an invite to your partner, and next week checked." Steps: "New event", "Title + time", "Repeat weekly Mon", "Invite + Save", "Check next week". `.sheet` "▸ WORKSHEET 1D · INVITE THE PERSON BESIDE YOU" |
| 21 | evaluate / review | h1 "A repeating reminder shows up on the wrong day. Fix?" B: "Open it and edit <strong>the whole series</strong>, then check the next one." B: "Why: editing one occurrence leaves every future one wrong." |
| 22 | present / tell (Unit E) | h1 "Did the computer change<br><em>what you typed?</em>" steps B: 01 "Watch: <kbd>(c)</kbd> became ©"; 02 "Undo it right away: <kbd>Ctrl</kbd> + <kbd>Z</kbd> or the ⚡ button"; 03 "Still stuck? Ask for help clearly." |
| 23 | present / tell | h1 "A help request <em>that gets answered</em>" steps B: 01 "App + version: File ▸ Account ▸ About"; 02 "What you were doing"; 03 "What you already tried"; 04 "The exact message, word for word". Then B (two-column compare): ✗ "Word is broken. Help!" vs ✓ "Word (Microsoft 365, Version 2408): when I click Save I see 'Document not saved.' I restarted Word and tried Save As." |
| 24 | present / show | `data-demo="w1-autocorrect"` |
| 25 | practice / do / 10 | Mission 1E: Point A "Word keeps changing (c) into ©." Point B "You undid it, found Word's version, and wrote a four-part help request." Steps: "Type (c)", "Undo it", "Find version", "Write the request", "Swap with partner". `.sheet` "▸ WORKSHEET 1E" |
| 26 | evaluate / review | h1 "Which request gets the fastest answer?" B (3 options as cards A/B/C): A "Help! Nothing works." B "Word, Version 2408. Save shows 'Document not saved.' Restarted, tried Save As." C "Please fix my computer tomorrow." B (answer): "<strong>B</strong>: app + version, what you did, what you tried, the exact message." |
| 27 | apply / — | h1 "Take it home." `.steps` B: "Set the Scale that's easiest for <em>your</em> eyes"; "Make your headset the output before your next video visit"; "Add one repeating reminder you actually need". p: "Write it on your worksheet: Take it home." |
| 28 | — / — / gorge | Finale (`.panel.bare .opener`): kicker `MISSION 01 // COMPLETE`; h1 "You made the computer fit you."; chips ✓ Readable text · ✓ Right speaker · ✓ Clean print · ✓ Shared calendar · ✓ Clear help request; `.go` "NEXT MONDAY · OCT 5 · FIND, JUDGE & ORGANIZE INFORMATION". |

Every slide gets `<aside class="notes">` with 2–4 sentences: what to say, what to click, and the timing target from the run sheet.

- [ ] **Step 1: Write the failing test**

```js
// tests/functional/dl2-os-week1-deck.spec.js
// Week 1 deck: 28 slides, WIPPEA order, every Show mounts, text floor, no external requests.
const { test, expect } = require('@playwright/test');
const URL = '/courses/digital-literacy-2/weeks/week-01/presentation.html';

test('structure: 28 slides, phases in order, five demos, five Do timers', async ({ page }) => {
  await page.goto(URL);
  await expect(page.locator('.slide')).toHaveCount(28);
  await expect(page.locator('.slide[data-stage="show"] .demo-bezel')).toHaveCount(5);
  await expect(page.locator('.slide[data-stage="do"][data-minutes]')).toHaveCount(5);
  const phases = await page.locator('.slide[data-phase]').evaluateAll(s => s.map(x => x.dataset.phase));
  const order = ['warm-up', 'intro', 'present', 'practice', 'evaluate', 'apply'];
  expect(phases[0]).toBe('warm-up'); expect(phases.at(-1)).toBe('apply');
  expect(phases.every(p => order.includes(p))).toBe(true);
  await expect(page.locator('a[href*="legacy"]')).toHaveCount(0);
});

test('every slide fits 1920×1080 and body text is at least 32px', async ({ page }) => {
  await page.setViewportSize({ width: 1920, height: 1080 });
  await page.emulateMedia({ reducedMotion: 'reduce' });
  await page.goto(URL + '#1');
  const n = await page.locator('.slide').count();
  const problems = [];
  for (let i = 0; i < n; i++) {
    await page.evaluate(k => DL2Deck.go(k, 'back'), i); // back = all build parts shown
    const r = await page.evaluate(() => {
      const s = document.querySelector('.slide.is-active');
      const texts = [...s.querySelectorAll('p, li, .demo-cap, .ab div, .sab div, .dsteps div')].filter(e => e.offsetParent && !e.closest('.screen'));
      const small = texts.filter(e => parseFloat(getComputedStyle(e).fontSize) < 31.5).map(e => e.textContent.trim().slice(0, 40));
      const deck = document.querySelector('.deck').getBoundingClientRect();
      const over = [...s.querySelectorAll('*')].filter(e => !e.closest('.screen') && e.getBoundingClientRect().bottom > deck.bottom + 1).map(e => e.className);
      return { small, over };
    });
    if (r.small.length || r.over.length) problems.push({ slide: i + 1, ...r });
  }
  expect(problems).toEqual([]);
});

test('no external requests', async ({ page }) => {
  const ext = [];
  page.on('request', r => { if (!r.url().startsWith('http://localhost:3939')) ext.push(r.url()); });
  await page.goto(URL);
  await page.waitForLoadState('networkidle');
  expect(ext).toEqual([]);
});

test('legacy deck still opens', async ({ page }) => {
  const r = await page.goto('/courses/digital-literacy-2/weeks/week-01/presentation-legacy.html');
  expect(r.status()).toBe(200);
});
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `npm run build:site && npx playwright test tests/functional/dl2-os-week1-deck.spec.js`
Expected: FAIL (the old deck has a different structure, and no legacy file exists).

- [ ] **Step 3: `git mv` the old deck, then write the new `presentation.html` with all 28 slides per the table.**

- [ ] **Step 4: Run the test to verify it passes**

Run: `npm run build:site && npx playwright test tests/functional/dl2-os-week1-deck.spec.js`
Expected: 4 passed.

- [ ] **Step 5: Screenshot every slide at 1920×1080 (all builds shown) and review against mockups 1 and 4. Fix any spacing or overflow, then re-run Step 4.**

- [ ] **Step 6: Commit**

```bash
git add courses/digital-literacy-2/weeks/week-01/presentation.html courses/digital-literacy-2/weeks/week-01/presentation-legacy.html tests/functional/dl2-os-week1-deck.spec.js
git commit -m "feat(dl2): Week 1 Mission Control deck (28 slides, five units, WIPPEA)" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 10: Week 1 missions, answer key, run sheet

**Files:**
- Replace: `courses/digital-literacy-2/weeks/week-01/worksheet.html`, `courses/digital-literacy-2/weeks/week-01/answer-key.html`
- Create: `courses/digital-literacy-2/weeks/week-01/run-sheet.html`
- Test: `tests/content/dl2-os-week1-print.spec.js`

**Interfaces:**
- Consumes: `os/paper.css` (Task 5) and the letterhead markup (static copy of `DL2Paper.letterhead({dateText:'Mon, Sep 28, 2026 · 4:30–6:30 PM ET'})`, using `/courses/digital-literacy-2/os/img/vub-seal-360.png`). Missions are `<article class="mission" id="m1A">` … `m1E`, each with `.mission-ab` (`.a`, `.b`), `ol.mission-steps > li` (`.act`, `.see`, `.box`), `.stuck`, `.check` and `.home`.

Mission content (exact):

**1A · Make text readable, then put it back** (10 min)
- A: "Settings is at 100%. Text in File Explorer and Edge looks small." B: "You tried 125%, checked two apps, and set it back to 100% for the next person."
- Steps:
  1. **Open Settings.** Click Start ▸ Settings, or press Windows + I. *You should see:* a window named Settings.
  2. **Go to Display.** Click System ▸ Display. *You should see:* "System › Display" across the top.
  3. **Make it bigger.** Under Scale & layout, open Scale and choose 125%. *You should see:* everything gets bigger, right away.
  4. **Check two apps.** Open File Explorer and Edge. Easier to read? Circle: Yes / No. *You should see:* bigger text in both apps, not just one website.
  5. **Put it back.** Set Scale to 100% (Recommended). *You should see:* text back to its normal size.
- Stuck: "Can't find Display? Click Find a setting, type **scale**, press Enter." / "Different numbers? Your screen may recommend 150%. Pick one step above Recommended."
- Check: "Browser zoom (Ctrl +) changes ____" / "Display Scale changes ____" / "To fix every app, I use ____"
- Home: "At home, the setting that's easiest for me is: ____"

**1B · Send sound to the right device** (7 min)
- A: "Sound plays from the speakers." B: "A test sound plays in your headset, and you can switch back."
- Steps:
  1. **Plug in the headset.** Use the USB or headphone jack. *You should see:* nothing yet. That's normal.
  2. **Open Quick Settings.** Click the speaker icon on the taskbar (bottom right). *You should see:* a panel with Wi-Fi, Bluetooth and a volume slider.
  3. **Open the outputs.** Click the arrow › beside the volume slider. *You should see:* "Sound output" with a list of devices.
  4. **Choose the headset.** Click Headphones (or your headset's name). *You should see:* a check mark next to it.
  5. **Test it.** Play the test sound Britt shares. *You should see (hear):* the sound in your headset only.
- Stuck: "No arrow? Settings ▸ System ▸ Sound ▸ Output does the same thing." / "Headset not listed? Unplug it, wait 5 seconds, and plug it back in."
- Check: "Sound goes to one ____ at a time." / "Before a video visit, I check the ____."
- Home: "My headset is called: ____"

**1C · Print one clean page** (12 min)
- A: "Community Supper Flyer.docx previews as 1 of 2." B: "The preview says 1 of 1 and one test copy is printed."
- Steps:
  1. **Open the flyer.** Open Community Supper Flyer.docx from the class folder. *You should see:* the flyer in Word.
  2. **Preview it.** Press Ctrl + P. *You should see:* the preview on the right, with "1 of 2" at the bottom.
  3. **Narrow the margins.** Under Settings, click Normal Margins ▸ Narrow. *You should see:* the preview redraw.
  4. **Check again.** Look at the pager. *You should see:* "1 of 1".
  5. **Print one copy.** Copies: 1 ▸ Print. *You should see:* one page at the printer. Pick it up and check it.
- Stuck: "Still 1 of 2? Delete one blank line at the end, then check again." / "Can't find Margins? Layout tab ▸ Margins ▸ Narrow is the same setting."
- Check: "Before printing many copies, I print ____ test copy." / "The pager should say ____."
- Home: "Something I print at home: ____"

**1D · A calendar entry others can act on** (12 min)
- A: "No reminder for Monday class." B: "A weekly Monday 4:30 PM event with a reminder and an invite, and next week checked."
- Steps:
  1. **Open the calendar.** In Outlook, click Calendar on the left. *You should see:* the week, Sep 27 – Oct 3.
  2. **Start a new event.** Click New event. *You should see:* a form that says Add a title.
  3. **Fill it in.** Title "VUB class" · Mon 9/28/2026 · 4:30 PM – 6:30 PM. *You should see:* the date and times filled in.
  4. **Make it repeat.** Set Repeat to Weekly on Monday. Keep the reminder at 15 minutes before. *You should see:* "Weekly on Monday".
  5. **Invite and save.** Invite your partner's practice address, then Save. *You should see:* the event on Monday with a ↻ symbol.
  6. **Check next week.** Click the next-week arrow. *You should see:* VUB class on Monday, Oct 5.
- Stuck: "Don't see Repeat? Look for Make recurring (↻) near the time." / "Wrong day next week? Open it, choose Edit the series, and fix the day."
- Check: "To fix every future reminder I edit the ____." / "I proved it worked by checking ____."
- Home: "A repeating reminder I need: ____"

**1E · Undo an automatic change and ask for help clearly** (10 min)
- A: "Word keeps changing (c) into ©." B: "You undid it, found Word's version, and wrote a four-part help request."
- Steps:
  1. **Type it.** In a new Word document type: Copyright (c) 2026. *You should see:* (c) turn into ©.
  2. **Undo it.** Press Ctrl + Z right away (or click the ⚡ button ▸ Change back). *You should see:* (c) again.
  3. **Find the version.** File ▸ Account ▸ About Word. *You should see:* "Version 2408" (or similar). Write it here: ____
  4. **Write your request.** Fill in the four boxes below. *You should see:* all four boxes filled in.
  5. **Swap.** Trade with your partner. Could they help you from this alone? Circle: Yes / No.
- Four boxes: "App + version" / "What I was doing" / "What I already tried" / "The exact message"
- Stuck: "No ⚡ button? Ctrl + Z works the same, right after the change."
- Home: "An app at home I might need help with: ____"

Answer key (`answer-key.html`, letterhead, "Week 1 · Answer Key (instructor)"):
- **1A:** "web pages only / every app / Display Scale."
- **1B:** "output (device) / sound output."
- **1C:** "one / 1 of 1."
- **1D:** "series / the next week's event."
- **1E:** "a good request names the app + version, the task, what was tried, the exact message."
- Plus the 5 Review answers from the deck (slides 8, 12, 17, 21, 26).

Run sheet (`run-sheet.html`, letterhead, one page, landscape allowed): a table `Time | Slide | Segment | You do | Learners do`, following spec §7 times: 4:30 (1–2), 4:50 (3–4), 4:58 (5–8), 5:13 (9–12), 5:25 (13), 5:35 (14–17), 5:50 (18–21), 6:05 (22–26), 6:20 (27–28). Add a key strip: "→ / PageDown next · ← back · N notes · T timer · F fullscreen · B blank screen · number + Enter jumps". Add a before-class checklist: "Print worksheets 1A–1E (1 per learner + 1 spare) · Print 1 paper pre-test per learner as a backup · Put Community Supper Flyer.docx in the class folder · Headsets at each station · Test the room printer · Open presentation.html and press F".

- [ ] **Step 1: Write the failing test**

```js
// tests/content/dl2-os-week1-print.spec.js
// Week 1 printouts: five letterhead missions with Point A/B and "You should see" on every step.
const { test, expect } = require('@playwright/test');
const W = '/courses/digital-literacy-2/weeks/week-01/';

test('five missions, each complete', async ({ page }) => {
  await page.goto(W + 'worksheet.html');
  const m = page.locator('article.mission');
  await expect(m).toHaveCount(5);
  for (let i = 0; i < 5; i++) {
    const one = m.nth(i);
    await expect(one.locator('.letterhead')).toContainText('A TRIO program funded by the U.S. Department of Education');
    await expect(one.locator('.mission-ab .a')).toContainText('POINT A');
    await expect(one.locator('.mission-ab .b')).toContainText('POINT B');
    const steps = one.locator('ol.mission-steps > li');
    expect(await steps.count()).toBeGreaterThanOrEqual(5);
    expect(await one.locator('ol.mission-steps > li .see').count()).toBe(await steps.count());
  }
});

test('each mission prints on its own page(s), letter size', async ({ page }) => {
  await page.goto(W + 'worksheet.html');
  await page.emulateMedia({ media: 'print' });
  const breaks = await page.locator('article.mission').evaluateAll(a => a.slice(1).map(x => getComputedStyle(x).breakBefore));
  expect(breaks.every(b => b === 'page')).toBe(true);
});

test('run sheet and key exist with the letterhead', async ({ page }) => {
  for (const f of ['run-sheet.html', 'answer-key.html']) {
    await page.goto(W + f);
    await expect(page.locator('.letterhead')).toContainText('New River Community and Technical College');
  }
  await page.goto(W + 'run-sheet.html');
  await expect(page.locator('table tbody tr')).toHaveCount(9);
});
```

- [ ] **Step 2: Run the test to verify it fails.** Run: `npm run build:site && npx playwright test tests/content/dl2-os-week1-print.spec.js`. Expected: FAIL.
- [ ] **Step 3: Write the three pages per the content above.** Add `.mission{break-before:page}` and `.mission:first-of-type{break-before:auto}` to `paper.css`, along with the mission styles ported from mockup 4.
- [ ] **Step 4: Run the test to verify it passes.** Expected: 3 passed.
- [ ] **Step 5: Print-preview check.** In Chromium, print to PDF: `page.pdf({format:'Letter'})` into the scratchpad. Each mission fits on one page (1E may take two). The letterhead is on every mission, and the result reads in grayscale.
- [ ] **Step 6: Commit**

```bash
git add courses/digital-literacy-2/weeks/week-01/worksheet.html courses/digital-literacy-2/weeks/week-01/answer-key.html courses/digital-literacy-2/weeks/week-01/run-sheet.html courses/digital-literacy-2/os/paper.css tests/content/dl2-os-week1-print.spec.js
git commit -m "feat(dl2): Week 1 letterhead missions 1A–1E, answer key and run sheet" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 11: Retire replaced-file specs, full verification, handoff

**Files:**
- Modify or delete: the `tests/content/dl2-*.spec.js` and `tests/functional/dl2-*.spec.js` cases that assert the *replaced* files (the Week 1 deck/worksheet/answer key, the pre/post tests and keys, printables, `assets/assessment.js` behavior)
- Modify: `docs/digital-literacy-2/HANDOFF.md` (add a "Mission Control (Sep 2026)" section)

- [ ] **Step 1: Run the full suite and list failures**

Run: `npm run build:site && npx playwright test 2>&1 | tail -80`
Expected: only failures in old DL2 specs that target replaced files.

- [ ] **Step 2: For each failing old spec case:**
  - If it targets a replaced file, delete that case (or the whole file if every case targets replaced files). Record it in the commit body.
  - If it targets Weeks 2–6 or unchanged pages, it must pass. Investigate and fix the regression in the new code, never in the old test.
- [ ] **Step 3: Links, build, accessibility**

Run: `npm run links` (expect no broken DL2 links), then `node scripts/build-site.js` (expect success), then `node scripts/a11y-check.mjs` if it accepts page paths, or add an axe check for the four new page types in `tests/functional/dl2-os-a11y.spec.js`:

```js
const { test, expect } = require('@playwright/test');
const AxeBuilder = require('@axe-core/playwright').default;
for (const p of ['weeks/week-01/presentation.html', 'weeks/week-01/worksheet.html', 'assessments/pre-test.html', 'assessments/pre-test-answer-key.html'])
  test(`axe: ${p}`, async ({ page }) => {
    await page.goto('/courses/digital-literacy-2/' + p);
    const r = await new AxeBuilder({ page }).disableRules(['region']).analyze();
    expect(r.violations.filter(v => ['serious', 'critical'].includes(v.impact)).map(v => v.id)).toEqual([]);
  });
```

- [ ] **Step 4: Full suite green.** Run: `npx playwright test`. Expected: 0 failed.
- [ ] **Step 5: Update `docs/digital-literacy-2/HANDOFF.md`** with a short section covering: the Mission Control files map, how to add a slide/demo/mission, the Netlify form names (and the need to enable email notifications in the Netlify dashboard), the item bank as the single source for tests/keys/printables, and the legacy Week 1 deck path.
- [ ] **Step 6: Commit**

```bash
git add -A tests docs/digital-literacy-2/HANDOFF.md
git commit -m "test(dl2): retire specs for replaced Week 1 and assessment files; add a11y checks; handoff notes" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

- [ ] **Step 7: Stop for Britt's review.** Do not push or deploy. Report what's ready, with screenshots, and ask for approval to push the branch and open a PR (the deploy happens on merge to `main`).
