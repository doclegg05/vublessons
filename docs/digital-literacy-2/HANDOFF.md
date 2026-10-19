# Weeks 3 to 6: the Week 2 method, pause cards, new videos (October 2026)

Week 3 was rebuilt first (taught 2026-10-12). Spec, rebuild order and facts that must stay the same: `week-03-spec.md`. Weeks 4 to 6 follow the same recipe, one PR each, with their own spec.

- Lesson data lives in one module per week (`mission-control/week2.py`, `week3.py`); shared helpers are in `mission-control/lessonkit.py`. No capstone after Week 2 (Britt, 2026-10-08).
- Video cards: `video/digital-literacy-2/week-NN/cards.json` (topic dividers and 10-second pause cards), drawn by `scripts/dl2/video-cards.py`, timed by `normalize-pace.py`, checked by `tests/content/dl2-video-cards.spec.js`.
- Narration tools now take a week: `author-media.py week-NN`, `tag-narration.py week-NN` (delivery tags from `week-NN/delivery.json`), `elevenlabs-takes.py --week week-NN [--speed 0.85]`, `check-expressive-takes.py --week week-NN`, `verify-media.py --week N`. Set `VUB_TAKES_DIR` to the take folder, which moved from the Desktop to the main checkout.
- `verify-media.py` now checks each take's words against the week's teaching script, not the September 2026 wording.
- `refresh-video-text.py week-NN` updates chapter labels and transcript text after a narration rewrite.

# Current opening order — draft PR #28

Week 1: pre-test directions and a labeled new-tab link (slide 1), approved captioned Brad video (slide 2), then existing lesson. Weeks 2–6: approved captioned Brad video (slide 1), then existing lesson. Totals are 28 / 24 / 24 / 24 / 24 / 24. The scoped generator, media-controls behavior, saved-position migration, 120-minute pacing, and Week 6 video alignment limitation are documented in `MISSION-CONTROL-WEEKS-2-6.md`. Production media from PR #29 is already live; the design/placement change remains preview-only.

# Digital Literacy Level 2 course

## Narration refresh — approved September 28, 2026

The narration-only refresh uses ElevenLabs voice `Dslrhjl3ZpzrctukrQSN`, whose
provider display name is **Hey Its Brad - Clear Narrator for Documentary**.
Sources, settings, usage snapshots and receipts are under
`video/digital-literacy-2/elevenlabs-brad-v3-refresh/`. Earlier Britt profiles
remain provenance; raw/isolated sources and rejected candidates are also retained
under `~/Desktop/vub-brad-narration-refresh/`. Per-take settings override the profile
default. HyperFrames advanced from 0.8.58 to 0.8.82 with source validation.

Use `check-expressive-takes.py --profile brad-refresh` with both `--model base.en`
and `--model small.en`, then `import-elevenlabs-narration.py --profile brad-refresh`,
`normalize-pace.py`, `align-captions.py` and a normal `build-media.py` run. Use the
media Python environment for transcription, import and alignment.

For this scope, run `refresh-video-chapters.py` instead of the broad page generator.
Then run `python3 scripts/dl2/mission-control/build.py` to refresh opening-player hashes and practice-library times from the approved manifest and chapter JSON. The chapter refresher updates existing chapter times and content-hash media URL versions, including
the Week 1 archived presentation,
and preserves the Mission Control deck and assessment release. Caption grouping
shares up to 0.6 seconds of display time between neighboring phrases for readability,
while keeping every cue inside its audio clip and leaving speech unstretched.

After strict source checks, renders and loudness normalization, run
`verify-media.py --profile brad-refresh` and the complete quality gate.
`build-narration-preview.py` creates the six-video local gallery after the new
manifest verifies. `verify-narration-playback.cjs` checks all sixty keyboard seeks,
eighteen actual playback/caption/audio-decode samples, and gallery accessibility.
It defaults to `http://127.0.0.1:3948` (`DL2_REVIEW_URL` overrides the port).

The 135–145 WPM audit band is advisory, not the separate defect gate. Retain and
report its warnings. Targeted pacing revisions must preserve words and natural
pronunciation; do not change thresholds or mechanically stretch speech to pass.
The user approved publication on September 28, 2026. See `NARRATION-REFRESH.md`
for validation evidence and the retained pacing observations.

## Mission Control (Sep 2026)

All six main presentations now use the Mission Control deck engine. Week 1 now opens with the pre-test and video; its teaching units are preserved. Weeks 2–6 each have four Tell/Show/Do/Review missions, a protected eight-minute break, and a 120-minute plan. The older detailed interactive simulations remain available in each week's `practice.html` library; they do not change main lesson progress. Existing video/transcript pages and media are unchanged.

**Weeks 2–6 authoring:** edit `scripts/dl2/mission-control/content.py` (teaching sequence), `visuals.py` (original task diagrams), and `build.py` (rendering and matched paper materials), then run `python3 scripts/dl2/mission-control/build.py` from the repository root. Detailed task/answer/quick-card content comes from `scripts/dl2/curriculum.json`. The canonical practice-library templates are in `scripts/dl2/mission-control/practice/`. Do not edit the generated week files directly.

Shared extension files: `os/missions.css`, `missions.js`, `mission-paper.css`, `mission-paper.js`, and `mission-practice.css`. All changes are scoped away from Week 1. Each week includes `presentation`, `worksheet`, `answer-key`, `lesson-plan`, `run-sheet`, `instructor-notes`, and `practice` pages. Dates are excluded from these reusable materials.

**Current assessment copy:** `os/test.js` is canonical. Both forms describe submission to the instructor without naming a hosting provider. A successful HTTP response means submitted for Britt, not confirmed inbox receipt. Failure/retry, saved-PDF backup, data disclosure, hidden form registration and server/email logic remain intact.

**Files map** (paths under `courses/digital-literacy-2/`)

| Path | What it is |
|:-----|:-----------|
| `os/deck.css`, `os/deck.js` | Projector deck engine. One slide at a time. → / PageDown reveal the next `.build` part, then step a Show demo, then change slides. N notes, six clickable phase buttons, F fullscreen, B blank, number + Enter jumps. Nothing auto-advances. |
| `os/win11.css`, `os/demo.js`, `os/demos/week-01.js` | "Show" demos: Windows 11 + Microsoft 365 recreations with a guided cursor, captions and a checklist. |
| `os/items.js` | **The item bank**, the single source for the pre/post tests, grading, answer keys, printables and the results PDF. There are 20 parallel items per form: item N on each form checks the same skill, domain and week. |
| `os/grade.js`, `os/test.js`, `os/test.css` | Grading and record IDs. The test app: name → 20 questions → review → submit → PDF → copy to Britt. Answers survive a reload. Unsent copies wait in the `dl2os:outbox` localStorage key and retry on the next visit. |
| `os/pdf.js`, `os/vendor/` | Graded results PDF on the letterhead (pdf-lib + fontkit, self-hosted). `clean()` keeps every drawn string WinAnsi-safe for the standard-font fallback. |
| `os/paper.css`, `os/paper.js`, `os/keys.js` | Letterhead paper system. `keys.js` renders the answer keys and printable tests from the item bank. |
| `os/fonts.css`, `os/fonts/`, `os/img/` | Self-hosted fonts and the seal (no CDN). |
| `weeks/week-01/presentation.html` | The 28-slide Week 1 deck (five units, WIPPEA phases). |
| `weeks/week-01/worksheet.html`, `answer-key.html`, `run-sheet.html` | Letterhead Missions 1A–1E, their key, and the one-page landscape run sheet. |
| `weeks/week-01/files/` | Class files: `Community Supper Flyer.docx` (Mission 1C) and `sound-test.html` (Mission 1B). Rebuild the flyer with `python3 docs/digital-literacy-2/class-files/make-community-supper-flyer.py`. Its docstring has the page math: exactly one line spills at Normal margins, and it fits at Narrow. |
| `weeks/week-01/presentation-legacy.html` | The previous generated Week 1 deck, kept for reference. |
| `assessments/pre-test.html`, `post-test.html` + `-answer-key`, `-printable` | 20-question tests, keys and paper backups. Keep these URLs stable. |

**The legacy `scripts/dl2/build-pages.py` now refuses to run. Do not run `learning.py` to regenerate the course.**
They regenerate `weeks/week-01/presentation.html`, `worksheet.html`,
`answer-key.html`, the assessment keys, `syllabus.html`, `sources.html` and the
lesson plans from `curriculum.json`. That would overwrite the Mission Control
files and the 20-question wording. The scoped Mission Control generator writes the Week 1 deck from its explicit template and Weeks 2–6 materials; it does not write assessments, syllabus or the hand-authored Week 1 paper materials.

**Add a slide.** Add a `<section class="slide" data-phase="…" data-stage="…" data-unit="…">`
in `scripts/dl2/mission-control/week-01.html` for Week 1, then run the scoped generator. Phases: warm-up, intro, present, practice, evaluate,
apply. Stages: tell, show, do, review. Put teaching words in the slide and
presenter words in `<aside class="notes">`. Mark reveal-one-at-a-time parts
`class="build"`. The current classroom version has no timer or scheduled break. On a dense
slide, `data-fit="tight"` caps text growth (1.1×) so it still fits at large text sizes. Run
`tests/functional/dl2-os-week1-deck.spec.js`: slide count, fit at 1920×1080
and at every text size, and body text ≥ 32px.

**Add a demo.** Append a `DL2Demo.define({ id, title, start, scene, steps })`
to `os/demos/week-01.js` (one file per week). Each step has a caption, a
target, an action and the resulting state. Mount it on a slide with
`<div class="demo" data-demo="<id>"></div>`. The deck lets the demo take
its steps before moving on. Windows text in a scene uses div/span only (see
the file header). Check it with `dl2-os-demo.spec.js` and `dl2-os-week1-demos.spec.js`.

**Add a mission.** Copy an `<article class="mission">` in `worksheet.html`:
letterhead, Point A → Point B, 5–6 steps (each with a `.see` "You should
see" line and a check box), If you get stuck, Check yourself and Take it home. Add
its model answer to `answer-key.html` and a row to the run sheet. Each
mission starts on its own letter page. `dl2-os-week1-print.spec.js` checks
the structure.

**Change a test question.** Edit only `os/items.js`. Keep item N parallel
across forms and keep the answers balanced (5 each A–D). The keys,
printables, grading and PDF all follow. `dl2-os-items.spec.js` and
`dl2-os-pdf-text.spec.js` guard the bank.

**Netlify forms.** Results post to `dl2-pretest` and `dl2-posttest` (hidden static forms).
Form detection is enabled on the `vubcourse` project. Both forms are registered,
with individual `submission_created` email notifications to the verified instructor
address, `britt.legg76@gmail.com`. Netlify stores name, record ID, test version,
timestamps, score, domain totals and answer letters. The notification contains
fields, **not a PDF attachment**. See the instructor guide for the Forms dashboard.

The results screen distinguishes HTTP acceptance from a queued copy; it never
claims inbox delivery. A failed post keeps the same record ID in the browser outbox
and retries on the next visit or the Retry button. Web Locks serialize retries
across tabs where supported. If an HTTP response is lost after Netlify stores a
record, a retry can still create a duplicate: deduplicate exports by record ID.
IDs include a random suffix so learners with matching initials in the same minute
do not collide. If storage is blocked, the page explicitly asks for the PDF backup.

**USB backup.** After grading, each learner downloads the existing graded PDF,
chooses Britt's supplied drive in Save As or copies the file from Downloads, opens
it from the drive to check identity/test/score, then safely ejects and returns it.
This is independent of Netlify submission. Filenames include type, surname, date,
time and the unique suffix. The page cannot detect a physical USB save.

**Shared lab computers.** The course home's *Start fresh on this computer*
clears lesson progress and any pre/post test in progress (`dl2os:test:*`).
It keeps `dl2os:outbox`, so unsent results still reach Britt.

**Checks.** `npm run build:site && npx playwright test` runs the whole suite. The
Mission Control specs are `tests/*/dl2-os-*.spec.js`. Old DL2 cases that
asserted the replaced Week 1 and 28-question files were retired or narrowed
on 2026-09-28, and each carries a dated comment. For links, run
`python3 tools/link-check.py`: `npm run links` calls `python`, which macOS
doesn't ship. For site-wide WCAG checks, run `node scripts/a11y-check.mjs`.

## Screen-share task walkthroughs

The six videos include twelve screen-share chapters (9m14s total), mapped in
`SCREEN-SHARE-VIDEO-PLAN.md`. Original fictional interfaces, pointer movement,
clicks, and typing are synchronized to Britt’s existing word alignment. Chapter
menus identify the demonstrations; transcript sections provide visual step guides.
`SCREEN-SHARE-VIDEO-VERIFICATION.md` records delivery and preview checks.

Edit `scripts/dl2/screen-share-scenes.py`, then run the visual-only media builder.
`node scripts/dl2/check-screen-shares.mjs` checks every state; after rendering,
`python3 scripts/dl2/verify-screen-share-frames.py` compares encoded video frames
with the independently sought source states. Keep the local generated week-1
opening clip under `video/digital-literacy-2/generated-screen-share/`; its receipt
is tracked, while the working MP4 is excluded like the source narration.

## Photographic teaching revision

The approved September visual refinement is mapped in `PHOTOGRAPHIC-VISUAL-PLAN.md` and its three linked slide/chapter audits. It uses fictional West Virginia community/home scenes, original instructional interfaces, and the existing Britt narration. Selected photographs and generation provenance are recorded in `photo-assets.json`; originals and contact sheets are in `review/photo-refresh/`.

`scripts/dl2/photo_scenes.py` now controls explicit slide-photo placements, authored artifacts and additional local practice views. Photos establish the scenario; procedural scenes prioritize readable controls and visible outcomes. The safety-photo screen replacements are authored SVG overlays registered to the original image dimensions. Keep them aligned if resizing or changing that image.

Video `CHAPTERS` in `video-scenes.py` maps every chapter to a scene and optional scenario photo. `python3 scripts/dl2/build-media.py --visual-only` rebuilds compositions while preserving audio/caption metadata; do not run `author-media.py` for this visual-only path. The production CLI pin advanced from HyperFrames 0.8.48 to 0.8.58 and passed strict source validation. Use the current production pin for subsequent exports. See `VALIDATION.md` for the actual delivery-verification status rather than inferring it from source generation.

The fourth VUB Learning course teaches IC3 GS6 Level 2 across five two-hour sessions, followed by a two-hour extension on directing an AI coding agent and SaaS basics. The cohort calendar appears only in `courses/digital-literacy-2/syllabus.html`; presentations and resources can be reused.

## Curriculum review fixes (2026-09-24)

Six High findings from the six-agent review were fixed in the generators, with regression tests in
`tests/content/dl2-review-fixes.spec.js` and `tests/functional/dl2-review-fixes.spec.js`.

- Every slide's teaching sentence renders as a visible `p.slide-lead` above its simulation. The
  collapsed "Read the explanation" note is gone; the objectives note opens by default.
- Week 6 slide 10 checks `skills finds Community Skills Desk`, matching the worksheet rename.
- Week 6 has a `procedures` key (title, steps) rendered on the worksheet above the test log, plus a
  Download editable HTML link there.
- Week 5 has a `challenge` key (`item`, `intro`, `ratings`, `tasks` as task / materials / evidence).
  `build-pages.py` renders it as a table with a response box and an instructor rating per row, and
  lists the evidence in the answer key.
- `course.css` no longer sets `visibility:hidden` on the skip link, which had blocked focus.
- Assessment topic buttons carry an `aria-label` that includes the visible short label, the full
  domain, and the live answered count (`labelTopic` in `assessment.js`).

Regenerate with `python3 scripts/dl2/author-content.py` then `python3 scripts/dl2/build-pages.py`.

## Present mode for the projector (2026-09-26)

Decks had most slides taller than a projector screen (119 of 137 at 1366×768). Press **P** (or
"Present on a projector (P)") to present; **Esc** or P stops. Source: `assets/lesson.js` (present mode block)
and `assets/present.css`; tests: `tests/functional/dl2-present-mode.spec.js`.

- While presenting, lesson.js moves each slide's text into `.present-copy` and its visuals into
  `.present-stage` inside `.present-frame`, and restores the original children (and their exact class
  attributes) on exit. Generated HTML and the learner layout are unchanged.
- Per slide and screen size it picks side by side, stacked, or a **build** (parts shown in steps, words
  first, packed so each step holds as much as fits). Next/Previous and the arrow and Page keys step through a
  build before changing slide; going back lands on the last part.
- The frame is zoomed down only to 0.75, so 32px slide text never drops below 24px. Screen-relative limits
  do not scale with zoom, so fit() sets a scale, measures the real bottom, and adjusts.
- Every slide in all six decks fits at 1024×768, 1280×720, 1366×768 and 1920×1080 (the test steps through
  every build part). At 1366×768, 103 slides fit on one screen and 34 use 2–3 steps.
- Full screen is requested on entry; a late full-screen signal from an earlier exit does not end a new
  presentation (`reachedFullscreen`).

## Week 1: Tell, Show, Do, Review (2026-09-26)

The instructor's teaching method is **Tell, Show, Do, Review** inside the WIPPEA cycle (TEAL Fact Sheet
No. 8) with Knowles' adult learning principles. Week 1 was reviewed against it by Gemini 3.1 Pro (video;
video + materials) and Claude; reports and the framework are in `review/week-01-tsdr/`. Tests:
`tests/content/dl2-week1-tsdr.spec.js`.

- The week 1 `agenda` is now five cycles (A reading comfort, B hearing and screen, C connections and
  printing, D calendar, E automation and help). Each names its Tell, Show, Do and Review, plays its
  video chapter as the Show, and gives the video pause points (1:24, 2:02, 5:36, 6:28). Every learner
  does each task; the lab block and driver/coach swap are gone. Slide order is unchanged, so the
  instructor jumps to slides 20 and 21 for the in-cycle checks.
- New optional week keys: `outcomes` (measurable ABCD statements, shown in the lesson plan instead of
  `objectives`), `prep` (week-specific "Prepare the room") and `lab_paths` (rows of task and Windows 11
  steps, rendered as a "Lab quick card" on the lesson plan and worksheet). Only week 1 uses them so far.
  The Week 6 editor sentence now appears only in the week 6 plan.
- The lab runs Windows 10, but the instructor chose Windows 11 steps for the card. Card steps were
  checked against Microsoft and Google support pages (`review/week-01-tsdr/windows-click-paths-verified.md`).
- Content fixes: default printer (browsers pick the last one used), laser vs inkjet use, monitor
  brightness buttons, USB power, "mail rule" wording, zoom remembered per site, test-print rule,
  believable knowledge-check options, and worksheet tasks 4, 5 (paper fallback), 7 and 8 ("teh").
- Still open for week 1: an event-builder practice for task 5; the video re-render (ch5 connector
  visual, Tuesday vs Monday in ch7, ch4 label order, silent holds after prompts); post-test item 3
  still says "Leave the rule alone" about a repeating reminder.

## Pre-cohort fixes (2026-09-26)

From the seven-part full review before the 2026-09-28 cohort. Tests: `tests/content/dl2-monday-fixes.spec.js`
and `tests/functional/dl2-monday-fixes.spec.js`.

- Learner pages no longer link answer keys, lesson plans or the instructor guide. `page()`/`doc()` take
  `instructor=True` for the guide, lesson plans and every answer key: those pages get `noindex` and an
  "Instructor materials" rail item. `resources(n, instructor)` adds the plan and answer guide only for
  lesson plans. Instructors reach the guide from `/instructors/` (new DL2 card).
- Course home has "Start fresh on this computer" (confirm, then `VubProgress.reset('dl2')` and every
  `vub:dl2:assessment:*` sessionStorage key).
- "Clear my assessment" asks first. Enter in the name/score field moves to the questions instead of
  grading. The name field starts open. Reports show the date graded (`gradedAt`, kept on reload).
- Worksheets warn before leaving when any answer is typed.
- Decks: arrow keys work after clicking an in-slide button; focusable scroll regions (`[tabindex="0"]`,
  such as the calendar) keep their keys; Previous/Next are sticky; the first load writes no hash, so the
  page no longer jumps down.
- Contrast: flip-card hover, the selected phishing clue, gold buttons on navy completion slides, gold
  focus rings on navy/teal. Assessment topic tabs size to their label and the strip scrolls.

## Week 6 redesign: an instructor-led AI coding agent demo (2026-09-26)

Week 6 now teaches the basics of agentic engineering a SaaS website. The instructor runs an AI coding agent
on the projector; learners need no account or AI access. They write the spec and acceptance checks, predict
the change, review the agent's diff, test with a five-check log, write a repair request, retest, and learn
SaaS basics (hosting, sign-in, data, API keys, cost and upkeep) through the same resource finder. Six Tell,
Show, Do, Review cycles; slide order, count and kinds are unchanged. Tests:
`tests/content/dl2-week6-agent.spec.js`, `tests/functional/dl2-week6-agent.spec.js` and week 6 in
`tests/content/dl2-weeks-tsdr.spec.js`.

**Three practice pages** in `courses/digital-literacy-2/activities/` (hand-authored, not generated):

- `resource-finder.html`: version 1, the starter. Its script is now one statement per line so a live
  agent's diff is short on the projector. Behaviour and the top-level `const resources` are unchanged.
- `resource-finder-agent.html`: version 2, the prepared "agent result". It adds the requested category
  search, a harmless unrequested placeholder change and a Version 2 line, and it contains a
  **deliberate defect: the query line is `const query=search.value.trim();` without `.toLowerCase()`, so
  LIBRARY and Learning find nothing. Do not fix it.** Slide 10's diff, the Ctrl+F `toLowerCase` count
  (1 in version 2, 2 in versions 1 and 3), task 5's mixed-case check, the answer guide and video chapter 9
  all depend on it, and tests fail if it is repaired.
- `resource-finder-agent-fixed.html`: version 3, the one-line repair used for the retest.

If version 1 changes, re-derive versions 2 and 3 with exactly those edits and keep slide 10's diff
(`photo_scenes.py` (6,10)) matching the real lines; a content test compares them.

New optional week keys: `rubric` (criterion plus 0/1/2 descriptors; a table on the worksheet and in the
answer guide, with a Total line) and `glossary` (term and definition; the "Words in this video" box above
the week 6 transcript). The worksheet shows the version buttons and procedures before the tasks, then the
App test log and a Retest table with typed cells.

**Still open**

- Video re-record: done 2026-10-08. The video was rewritten to follow Missions 6A to 6D, with spoken definitions, pause cards and screen demos of the diff and of testing version 2. See `week-06-spec.md`.
- The floating Text size button can cover the search box on narrow screens (AX-07). The proposed
  `shared/text-size.js` change was skipped because it is platform-wide; the answer guide tells the
  instructor this is not the agent's change.
- Positioning text left as it was: the `courses.json` DL2 subtitle ("building a small web app with AI") and
  `sources.html` ("app-building week").

**Instructor demo notes** (tool names belong here and in prep, not in learner text): rehearse the exact demo
the week before with the tool you will use (for example Claude Code) and record it as a backup. Keep the
practice folder under git so `git diff` shows the change and `git restore` is the way back. Start in plan
mode (`claude --permission-mode plan`), read the plan aloud, then approve with manual edit approval so each
edit waits; Esc stops the agent. If the live run gets the change right, say so and switch to the prepared
version 2 ("another run of the same request produced this one"). Never show a sign-in page, key or bill;
enlarge the terminal font.

## Video review fixes (2026-09-24)

The six videos were re-rendered (visual-only; narration audio, beats and SCRIPT.md unchanged) after
a six-agent review. What changed and where:

- `screen-share-scenes.py`: week 1 Month view is a dated 5-row grid; zoom steps to 110%; week 3
  Navigation lists only real headings; week 4 email puts the reviewer in To with the organizer in Cc
  and shows the response window in the body; week 6 demo app mirrors `activities/resource-finder.html`
  (heading, labels, three records, no-results text, Reset). Secondary lines lifted to 26 to 28px.
- `video-scenes.py`: `.video-note` 28px, `.video-brand` 24px, no SVG text under 24; week 2 source
  cards differ; week 4 chapter 5 draws three competing copies; week 6 chapter 9 loop no longer
  overlaps the arrow; smaller fixes in weeks 1 to 3.
- `build-media.py`: caption cues break at sentence and clause boundaries, never on a function word,
  two lines max. Cue counts rose from 109 to 113 per video to 124 to 135. Mid-clause endings fell from
  about 20% to 77 to 89%.
- Week 5 video poster is `media/week-05-poster.webp`, extracted from the render at 0.5 s.
- Audio normalized to -18 LUFS / -1.5 dBTP after render with `normalize-loudness.py`
  (video stream copied, AAC 128k, faststart).

New checks, all run from the repo root:

```sh
python3 scripts/dl2/check-text-floor.py        # every composition font-size >= 24px
python3 scripts/dl2/check-captions.py --script video/digital-literacy-2   # cue shape; --strict makes pace warnings fatal
python3 scripts/dl2/normalize-loudness.py      # after every render, before verify-media.py
```

Not changed, because they need a re-record: pause-prompt timing, chapters above 165 wpm, the week 3
formula explanation, undefined terms in week 6, and week 5 not naming the skills challenge.

Working files that are git-ignored and must exist locally before a build: `video/digital-literacy-2/
week-0N/narration/*.wav` and `generated-screen-share/workstation.mp4`. Copy them from the main
checkout; `verify-media.py` checks the WAV hashes.

## Entry points

- Course home: `/courses/digital-literacy-2/index.html`
- Netlify shortcut: `/digital-literacy-2`
- Syllabus: `/courses/digital-literacy-2/syllabus.html`
- Instructor plans: `/courses/digital-literacy-2/instructor-guide.html`
- Pre-test: `/courses/digital-literacy-2/assessments/pre-test.html`
- Post-test: `/courses/digital-literacy-2/assessments/post-test.html`
- Research and objective map: `/courses/digital-literacy-2/sources.html`

## Included

Six presentations contain 137 slides in total, including title and completion slides. Each week has a two-hour lesson plan, eight worksheet tasks, an answer guide, two knowledge checks, a narrated video, captions and a transcript. Week 6 has three practice pages (the resource finder before the agent, the agent's result with one planted defect, and the repair), each a working, downloadable HTML/CSS/JavaScript example with fictional data; learners need no account or AI access.

The parallel pre/post tests each contain 28 original questions, four per GS6 domain. Results include the score, domain breakdown, every response with feedback, optional pre/post growth comparison, browser Print / Save as PDF, and a standalone HTML download. Paper tests and answer keys accompany both versions. The week 6 app uses a separate eight-point rubric. These are classroom assessments, not Certiport exam questions or certification predictions.

Assessment drafts and results use sessionStorage in the learner's tab. There is no server submission or instructor dashboard. On shared computers, save or print results and select **Clear my assessment**. Slide progress uses the existing `VubProgress` localStorage layer. Worksheets keep typed answers only in the open page and include them when printed.

## Assessment scenario revision

Current pairing: **pre-test version 2 / post-test version 3**. The pre-test is unchanged. The new post-test applies the same objective groups in different decisions and situations; see `review/post-test-v3.md` for the exact lesson map and version behavior. Its separate storage key avoids applying old post answers to new items, while existing pre-test results remain available.

Assessment version 2 uses 56 complete, fictional community/library scenarios with lesson-aligned choices and fuller feedback. The source remains `scripts/dl2/author-assessments.py`; run it, then `build-pages.py`, to regenerate the browser bank, printable tests and keys together. Version 2 uses its own session-storage key to avoid applying old answers to new questions. Use version 2 pre/post scores together; the post-test entry help explains this restriction. Pair-to-slide evidence and checks are in `review/assessment-v2.md`.

## Video production

The user-requested **Explain Video Generator** was tried first. Its nine-scene, 2:32 trial completed, and narration/caption playback was checked in the browser. Source: `video/digital-literacy-2/explain-generator-trial.opml`. The plain player URL required sign-in; the tool's full claim link played without sign-in. That ownership-bearing claim link is kept out of the public repository and course pages. The trial remains a comparison, not a required course dependency.

The initial narration previews used Kokoro, Sarah, and then Britt's saved voice. The current teaching revision uses **Britt — Mild Appalachian Male Voice** (`iKrofGyA12WC0e6AhZ8B`) through **ElevenLabs MCP**, model `eleven_v3`, followed by **ElevenLabs Voice Isolator**. It contains ten authored chapters per week, sixty total. Settings and original/cleaned source hashes are recorded in `video/digital-literacy-2/elevenlabs-britt-v3-deep/week-*/beat-*/receipt.json`; credentials are never stored in course sources. Speech is not time-stretched. Local transcription aligns the complete authored captions, rejecting weak matches.

Each video connects a familiar task to worked explanations, visible decisions, common mistakes, paused practice and transfer. Original illustrations accompany topic-specific demonstrations rather than recurring text-list layouts. Chapter buttons let learners replay a skill without automatic playback. The research rationale is in `research/video-teaching-redesign.md`.

Delivered videos are 1280×720 H.264/AAC at 24 fps with fast-start playback, optional WebVTT captions and text transcripts. Visuals use original text/layouts, the existing VUB seal and self-hosted fonts, with no software screenshots or music. GSAP is local to production sources; no CDN is added to learner pages.

The build retains exactly the six MP4s declared by path and SHA-256 in `courses/digital-literacy-2/media/manifest.json`, with a 20 MB per-file ceiling. Other MP4/MP3/MOV files retain the repository's stripping policy. This explicit exception makes the new course self-contained without requiring a YouTube upload.

## Editing and rebuilding

The Python authoring files under `scripts/dl2/` are source; generated HTML and JSON are committed so production needs only the existing Node build. Edit content in `author-content.py` and questions in `author-assessments.py`, then run:

```sh
python3 scripts/dl2/author-content.py
python3 scripts/dl2/author-assessments.py
python3 scripts/dl2/build-pages.py
```

Video scripts live in `video/digital-literacy-2/teaching-scripts/`; `author-media.py` imports them. Visual compositions are authored in `video-scenes.py`, and interactive lesson models in `workshops.py`. Production source, narration, provenance, word alignments, captions and scene HTML are under `video/digital-literacy-2/`. Install that directory's pinned Python requirements into an isolated venv and run `npm ci --prefix video/digital-literacy-2/production` for local GSAP. FFmpeg/FFprobe and HyperFrames 0.8.58 are media-authoring dependencies.

Generate matching takes using the Desktop workflow in **Expanded teaching-video rebuild** below. Keep delivery tags in `prompt.txt`, not learner captions. The pacing step measures the natural take and allocates a 0.45-second scene lead-in plus 1.1-second closing hold (2 seconds for the final practice chapter). Source MP3s and WAVs are local working assets excluded from Git; delivered MP4s, receipts and hashes are tracked. Preserve source audio locally to rebuild without another generation.

```sh
python3 scripts/dl2/author-media.py
# First generate matching ElevenLabs takes as described above.
# Use the media Python venv for the next three commands.
python scripts/dl2/import-elevenlabs-narration.py
python scripts/dl2/normalize-pace.py
python scripts/dl2/align-captions.py
python3 scripts/dl2/build-media.py
python3 scripts/dl2/build-pages.py
# For each week-01 through week-06:
npx hyperframes@0.8.58 check video/digital-literacy-2/week-01 --strict --contrast --json
npx hyperframes@0.8.58 render video/digital-literacy-2/week-01 --output courses/digital-literacy-2/media/week-01.mp4 --fps 24 --quality delivery --workers 2 --crf 24
python3 scripts/dl2/verify-media.py
scripts/quality.sh
```

When updating a video, save each strict check JSON to the matching `docs/digital-literacy-2/video-check-NN.json` before `verify-media.py`. The verifier decodes every delivered frame and audio sample, checks captions against the complete script, checks sound levels and black frames, then updates the manifest hashes. Never update hashes to bypass an unsuccessful verification.

## Evidence

- `av-sync-report.json`: Sandra toolkit assembly audit.
- `video-check-01.json` through `video-check-06.json`: strict HyperFrames lint/runtime/layout/contrast checks.
- `media-verification.json`: delivered MP4 checks.
- `video/digital-literacy-2/week-*/narration/pacing-report.json`: Sandra toolkit take pacing.
- `review/`: desktop/mobile screenshots and print proofs.
- `VALIDATION.md`: final checks and review disposition.

Run Sandra's existing checks from the education workspace (toolkit is a sibling repository):

```sh
for week in video/digital-literacy-2/week-*; do
  node ../toolkit/tools/test-narration-pacing.mjs "$week"
  node ../toolkit/tools/check-draft-audio.mjs "$week"
done
node ../toolkit/tools/audit-av-sync.mjs video/digital-literacy-2/week-* --json docs/digital-literacy-2/av-sync-report.json
```

No live deployment, merge to main, account creation, purchase or learner record collection is part of this delivery.

## Illustrated learning-app design

The approved A+B+C compositions are combined across the DL2 course: a navy course rail, original illustrations, six-week overview with saved continuation, topic navigation and a focused assessment workspace. `scripts/dl2/learning.py` authors the shared course frame, home and assessments; `learning-app.css` and `learning-app.js` provide responsive styling and truthful browser-local course progress. Regenerate pages with `python3 scripts/dl2/build-pages.py`.

Assessments show one question at a time, preserve position and answers, offer Review all, and retain existing grading, printable/downloadable results and clearing controls. Topic counts are actual answers, not estimated completion. Illustrations and provenance live under the course assets and `.impeccable/asset-manifest.json`; approved comps are in `.impeccable/mocks/`. The user's default preference is this illustrated, modern learning-app direction.

The learning-app revision expanded the quality gate to 60 browser tests, including three dedicated learning-app state/mobile tests. Final evidence is in VALIDATION.md and `review/learning-app/`. All six Britt voice videos remain unchanged by this visual pass.


## Topic-specific slide enrichment

The six decks now add 53 illustrated, choice-based topic examples and dedicated chart, image-edit and video-edit demonstrations. Teaching prose, assessment alignment and existing models are preserved. Edit the examples in `scripts/dl2/scenes.py`, regenerate with `build-pages.py`, then run the quality gate. New styling and logic live in `assets/slide-scenes.css` and `assets/slide-scenes.js` and load only on presentation pages.

Six new original illustration assets (about 463 KiB total) are tracked with `slide-illustrations.json`. `capture-slide-scenes.cjs` records desktop/mobile examples under `review/slide-scenes/`. Ten new tests verify all 53 topic selectors with keyboard and enlarged mobile text, plus chart consistency, crop/resize, trim/split, practice toggles and print content. The slide-enrichment revision brought the suite to 70 tests. These interactions are browser-local demonstrations; they do not perform real edits, payments, messages or account operations. Practice-step selections reset when the page is reloaded.


## Branded results reports

Pre/post grading uses a shared branded report theme in `assets/results-report.css`. The page builder embeds its CSS and the official white seal in assessment pages; downloads reuse both without external resources. Results include learner metadata, the actual score, domain bars with numeric equivalents, up to two lowest-scoring practice domains and all answer explanations. Perfect scores receive an application task instead of invented weak areas. Existing comparison wording, grading, clearing and optional learner information are preserved.

The print layout isolates report colors/type from the shared handout and text-size overrides, reserves the first page for the summary, and avoids splitting answer sections. Samples with fictional learner data, screen captures and PDFs live in `review/results-report/`; reproduce them with `node scripts/dl2/capture-results.cjs`. The report test file covers offline branding, accessibility, scoring edge cases and mobile/print behavior. The results-report revision brought the suite to 73 tests.


V3 delivery guidance: [ElevenLabs prompting and pause controls](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices). The sibling pacing checker uses 100–210 WPM as its defect band; the A/V audit separately warns outside 135–145 WPM. Retain and report those style warnings rather than mechanically retiming speech. Automated timing/defect checks do not certify the subjective quality of the cloned voice.


## Expanded teaching-video rebuild

The current narration source is `video/digital-literacy-2/teaching-scripts/week-NN.txt`: ten chapters per week. Run `author-media.py` only when intentionally replacing the narration script; it resets timing pending audio generation. Generate each chapter using the saved Britt voice and V3 settings, then apply ElevenLabs Voice Isolator to a local Desktop copy. The working directory is `~/Desktop/vub-deep-narration/week-NN/beat-NN/`, with `prompt.txt`, one MP3 in `raw/`, and one MP3 in `clean/`. The importer copies both into `elevenlabs-britt-v3-deep` and records the original and cleaned hashes. Preserve rejected candidates separately rather than overwriting their receipts.

The importer, natural-pacing allocator and aligner accept an optional `week-NN` argument for incremental production. After the initial Whisper model download, `HF_HUB_OFFLINE=1` avoids network checks during repeated alignment runs. Rebuild media sources and pages after alignment so captions, chapter seek positions and transcripts agree. Chapter navigation is keyboard accessible and intentionally does not autoplay.

The research and teaching rationale are in `research/video-teaching-redesign.md`. The curriculum and scheduled contact time remain unchanged; show chapters within the planned demonstrations and use the scheduled lab time for paused practice.

The expanded-video quality gate passes 75 browser tests. `capture-video-review.py` captures each exported chapter; `capture-video-chapters.cjs` records desktop/mobile navigation and its accessibility scan. See `VALIDATION.md` for current evidence and the distinction between technical audio checks and listening judgment.

## Expressive narration revision

The latest narration pass uses the same Britt voice and teaching words with
chapter-specific V3 performance direction. See `EXPRESSIVE-NARRATION.md` and
`video/digital-literacy-2/elevenlabs-britt-v3-expressive/` for prompts, actual
per-take settings, source hashes, and unprompted transcription checks. The
original `elevenlabs-britt-v3-deep` receipts remain historical provenance.

Use `import-elevenlabs-narration.py --profile expressive`, followed by natural
pacing measurement, word alignment, a normal `build-media.py` run, and
`build-pages.py`. Do not use visual-only mode after changing audio. Screen-share
cursor actions, captions, scene windows, and chapter links must all be rebuilt
from the new word timings before rendering. The prior screen-share-only
audio-preservation report does not apply to this intentional narration change.
