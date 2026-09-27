# DL2 "Mission Control": design spec

**Date:** 2026-09-27 · **Status:** approved in brainstorming · **Owner:** Britt Legg
**Course:** Digital Literacy Level 2 (IC3 GS6 Level 2 + AI agent/SaaS week), Mondays Sep 28 – Nov 2, 2026, 4:30–6:30 PM ET, New River Community and Technical College. Three adult learners (veterans).
**Approved mockups:** `docs/superpowers/specs/2026-09-27-dl2-mission-control-mockups/` (1 style, 2 Show demo, 3 test and PDF, 4 worksheet and Do slide). They are the visual source of truth.

## 1. Goal

Replace the DL2 teaching materials with a fresh, high-craft system: animated build-step slides styled as a futuristic OS, faithful Windows 11 demos with a guided cursor, printed missions on official letterhead, and 20-question parallel pre-tests and post-tests that produce an audit-ready graded PDF. The lessons follow WIPPEA at the lesson level and Tell → Show → Do → Review inside each unit, grounded in andragogy: a real problem first, a clear reason why, hands-on practice, and a take-home use.

## 2. Scope and boundaries

- **In scope:** everything under `courses/digital-literacy-2/`, the DL2 Playwright tests, and one syllabus sentence (28 → 20 questions).
- **Out of scope (must not change):** the site homepage, the American flag, the course cards, the other three courses, `instructors/`, `shared/`, `assets/`, `courses.json`, and the site build. DL2 pages may *load* shared files (`shared/text-size.js` is required on learner pages) and the self-hosted fonts in `assets/fonts/`, but must not edit them.
- **Branch:** `feat/dl2-mission-control`, cut from `origin/main`, which is the live site. It supersedes the unmerged PR doclegg05/vublessons#24.
- **Go-live:** nothing is deployed until Britt reviews it on Monday, Sep 28 (target: by noon). Until then the live Week 1 deck is the fallback. After go-live, the previous deck stays reachable at `weeks/week-01/presentation-legacy.html`.
- **URLs stay stable:** `weeks/week-0N/presentation.html`, `weeks/week-0N/worksheet.html`, `assessments/pre-test.html` and `assessments/post-test.html` keep their paths, so `courses.json` and the course home links keep working.

## 3. Decisions

| Topic | Decision |
|:--|:--|
| Teaching slides | **Command Deck:** dark space, animated perspective grid floor, cut-corner panels with a slowly tracing neon edge, mono HUD labels, phase strip |
| Big moments | **Dusk New River Gorge** (sky gradient, sun, layered ridges, the New River Gorge Bridge silhouette) for the week opener, break, finale and the Week 6 launch |
| Show | Coded Windows 11 recreations with ghost cursor, camera zoom, spotlight, click ripple, big captions and a step checklist. Controls: Back, Next, Auto, Replay, ½× |
| Test screen | **Clean light:** navy header, white card, one question per screen, big A–D buttons, 20-segment progress, review screen before submit |
| Graded PDF | As mocked: letterhead, record ID, form version, times, score, 7-domain breakdown, every item with both answers and "✓ Correct / ✗ Incorrect" in words, signature lines on the last page |
| Results copy | The PDF saves on the lab PC **and** a copy (name, answers, score, record ID, times) is sent to Britt's Netlify Forms inbox, the same mechanism `instructors/intake.html` uses |
| Worksheets | Letterhead "missions": Point A → Point B, numbered steps each with "You should see:", a checkbox, If you get stuck, Check yourself, Take it home |
| Lab software | Windows 11 + **Microsoft 365 desktop apps** (Word, Excel, new Outlook). Demos match these |
| Presenter machine | The Windows PC in the room. Demos use the native `Segoe UI Variable` / `Segoe UI`, with system-ui fallback |
| AI video | Not used for Show (it can't draw Windows UI accurately). Optional later for fictional Warm-up hooks and the Week 6 trailer |

## 4. Visual system

### 4.1 Deck (dark)
- Tokens: background `#050814`, panel `rgba(6,14,34,.93)`, cyan `#00e5ff`, magenta `#ff3cac`, gold `#ffc400`, text `#e9fbff`, muted `#8fe4f2`. Dusk scene: `#0b0a2a → #2a1850 → #7a2d6b → #e2735a → #f4b76a`, peach accent `#ffc79a`.
- Type: Space Grotesk (headings and body), JetBrains Mono (HUD labels, step numbers, timer). Both are self-hosted woff2 files in `courses/digital-literacy-2/os/fonts/` (OFL).
- Canvas: 16:9, authored with container-query units so a 1920×1080 projector gets body text ≥ 32px (24pt). HUD and chrome labels ≥ 21px. Nothing that learners must read is smaller.
- Motion: the grid floor drifts (4s loop) and the panel edge traces (9s loop). Build steps enter with a 550ms ease-out, and slide changes use an OS-style window open/close (scale + fade, ~450ms). No scanlines. Under `prefers-reduced-motion` everything is static and build steps still appear on click.
- Legibility: every line of text sits on a panel of ≥ .9 opacity, and color is never the only signal (the current phase is lit *and* labelled; selected items show text).

### 4.2 Paper (light): test screen, PDF, worksheets, answer keys, run sheet
- Navy `#1B365D`, gold `#C9A227`, red `#B31942`, ink `#15213A`, rules `#E3E8F1`. Playfair Display (organization name, document titles) and Source Sans 3 (everything else), both reused from `assets/fonts/`.
- **Letterhead:** tricolor top bar (navy / gold / red), VUB seal, "WEST VIRGINIA" in letterspaced gold, "Veterans Upward Bound", "A TRIO program funded by the U.S. Department of Education", and a meta block with Course (Digital Literacy Level 2), Cohort (Fall 2026 · Sep 28 – Nov 2), Instructor (Britt Legg), Date & time (the class date · 4:30–6:30 PM ET) and Location (New River Community and Technical College). A navy/gold double rule closes the header.

## 5. Architecture

Everything new lives in `courses/digital-literacy-2/os/`. It has no framework, no CDN, and works offline except for the results copy.

| File | Responsibility |
|:--|:--|
| `os/deck.css` | Command Deck and dusk scene styles, panel, HUD, phase strip, build-step states, transitions, reduced motion |
| `os/deck.js` | Slide engine: builds, navigation, strip/tag/timer, notes, resume, fullscreen |
| `os/win11.css` | Windows 11 kit: wallpaper, taskbar, window chrome, Settings nav/cards/combo/flyout, Quick Settings, Word, Outlook, dialogs |
| `os/demo.js` | Show engine: scene scaling, camera, cursor, spotlight, ripple, typing, step runner, controls |
| `os/demos/week-01.js` | Week 1 demo step lists (one per unit) |
| `os/paper.css` | Letterhead and paper system shared by the test, PDF preview, worksheets, keys and run sheet |
| `os/items.js` | Pre-test and post-test item bank, parallel by item number |
| `os/test.js` + `os/test.css` | Test flow: name → 20 questions → review → submit → grade → PDF → Netlify copy → result screen |
| `os/pdf.js` + `os/vendor/pdf-lib.min.js` + `os/vendor/fontkit.umd.min.js` | Graded PDF built with pdf-lib and @pdf-lib/fontkit (both MIT, vendored). Playfair Display and Source Sans 3 are embedded from font files kept in `os/fonts/`, with the standard Times/Helvetica fonts as fallback |
| `os/fonts/` | Space Grotesk and JetBrains Mono woff2 |

### 5.1 Slide authoring model
Each deck is one hand-written HTML file. A slide is `<section class="slide" data-phase="warm-up|intro|present|practice|evaluate|apply" data-stage="tell|show|do|review" data-unit="A">`, optionally with `data-scene="gorge"`. Elements marked `.build` appear one per click, in DOM order. Speaker notes go in `<aside class="notes">`.

**Engine behavior:**
- Next and Previous are driven by → ← PageDown PageUp Space, clicker, and swipe. Home and End jump to the ends, and number + Enter jumps to a slide.
- Next reveals the next build step or starts the next demo step. Only when a slide has nothing left does it move to the next slide.
- The phase strip, stage tag and slide counter update from the data attributes.
- `T` starts or stops the activity timer, which reads `data-minutes` on Do slides.
- `N` toggles the notes overlay, and `F` toggles fullscreen.
- Position is saved in `localStorage` (wrapped in try/catch).
- No auto-advance, ever.

### 5.2 Show engine
- Scenes are authored at 1280×720 inside `.screen` and scaled to the bezel.
- A demo is `{ id, scene, steps: [{ cap, target, action: 'click'|'type'|'hover'|'none', text?, state, zoom? }] }`. `state` is a small object applied to the scene through `data-*` attributes and classes, the same model as the approved mockup. Back re-applies the previous state instantly.
- Per-step timing: zoom out, move the cursor (750ms), spotlight and zoom to 2.1× (700ms), press and ripple, apply the state, hold. The ½× button doubles every duration.
- The side panel shows `STEP n / N`, a large caption (≥ 32px on a 1920 screen) and the checklist. The wording is identical to the worksheet steps.

### 5.3 Test engine and data flow
1. **Start screen:** student name (required) and a form label. The start time is recorded.
2. **Questions:** 20 screens, one question each. Choices are radio inputs styled as big tiles, with full keyboard support. Back and Next are available, and answers are kept in memory plus `localStorage` so a page reload doesn't lose them.
3. **Review screen:** all 20 with the chosen letters. Skipped questions are flagged in words, and the student can jump back to them. Submit asks for confirmation.
4. **Grading:** done locally against `items.js`. It computes the total and the 7 domain scores.
5. **PDF:** built with pdf-lib and downloaded as `DL2-PreTest-<LastName>-<YYYYMMDD-HHMM>.pdf`. A "Print my results" button opens it for printing. PDF generation never depends on the network.
6. **Results copy:** a URL-encoded POST to `/` with `form-name=dl2-pretest` (or `dl2-posttest`) and fields `record-id, student, form, started, submitted, score, domains, answers`, plus a honeypot. A hidden static `<form data-netlify="true" netlify-honeypot=…>` in the page registers the form at deploy. Britt turns on the form's email notification once in the Netlify dashboard (Forms ▸ notifications). On failure (offline) the payload is queued in `localStorage` and retried on the next load, and the result screen says "Saved on this computer. Tell Britt."
7. **Record ID:** `DL2-PRE-YYYYMMDD-HHMM-<initials>` (or `DL2-POST-…`).
8. **Also generated from `items.js`:** `pre-test-answer-key.html`, `post-test-answer-key.html` (instructor), and `pre-test-printable.html` / `post-test-printable.html` (a paper backup on letterhead with bubbles).

### 5.4 Error handling
- If the PDF library fails to load, the result screen shows the full graded report as a letterhead HTML page with a Print button, so nothing is lost.
- A demo target that's missing is reported with `console.error` and the step is skipped without breaking the deck.
- Every `localStorage` access is wrapped in try/catch.

## 6. Lesson shape

| WIPPEA phase | What happens | Stage tag |
|:--|:--|:--|
| Warm-up | A real problem from the learners' lives (fictional person, real situation), plus a quick "has this happened to you?" | none |
| Introduction | Tonight's mission: the objectives as chips, and why they matter | none |
| Presentation | Per unit: problem, then a Tell slide with build steps, then a Show demo (repeat live on the PC if needed) | Tell, Show |
| Practice | Per unit: a Do slide mirroring the printed mission, with a timer | Do |
| Evaluation | Per unit: a Review question, click to reveal the answer and the why | Review |
| Application | A take-home card: one thing to try at home this week | none |

Units interleave: A (Tell, Show, Do, Review), then B … The strip shows the phase of the current slide.

## 7. Week 1: "Make technology work for you" (Mon Sep 28)

| Time | Segment | Notes |
|:--|:--|:--|
| 4:30 | Welcome and **pre-test** (20 min) | Dusk opener, then the pre-test link on each PC |
| 4:50 | Warm-up and Introduction | "It's Monday night…", with five mission chips |
| 4:58 | **Unit A: Make text readable, then put it back** | Settings ▸ System ▸ Display ▸ Scale & layout ▸ Scale 125%, check File Explorer and Edge, back to 100%. Review: browser zoom vs. display scale |
| 5:13 | **Unit B: Send sound to the right device** | Taskbar speaker (Quick Settings) ▸ arrow beside the volume slider ▸ choose Headphones. Settings ▸ System ▸ Sound ▸ Output as the alternative. Test with a sound |
| 5:25 | Break (10 min) | Dusk scene with a countdown |
| 5:35 | **Unit C: One clean printed page** | Word ▸ File ▸ Print (Ctrl+P). The preview shows a last line spilling onto page 2 ▸ Layout ▸ Margins ▸ Narrow ▸ re-check the preview ▸ print one test copy |
| 5:50 | **Unit D: A calendar entry others can act on** | New Outlook ▸ Calendar ▸ New event: title, date, time, Repeat weekly on Monday, reminder, invite attendee, Save. Check the next occurrence in Week view. Review: a repeating reminder is on the wrong day, so edit the whole series |
| 6:05 | **Unit E: Check an automatic change, then ask for help clearly** | Word AutoCorrect: typing `(c)` becomes ©. Undo with Ctrl+Z or the AutoCorrect Options button. Help request = app + version (File ▸ Account ▸ About Word), what you were doing, what you tried, the exact message |
| 6:20 | Application and finale | Take-home card, then the dusk finale slide |

**Deliverables:**
- `weeks/week-01/presentation.html` (~30 slides)
- `weeks/week-01/worksheet.html` (missions 1A–1E, printable)
- `weeks/week-01/answer-key.html` (Check-yourself answers)
- `weeks/week-01/run-sheet.html` (one page: timings, what to click, what to say)
- `weeks/week-01/presentation-legacy.html` (the previous deck, unchanged)

All Windows paths must be verified against current Windows 11 and Microsoft 365 behavior before shipping. Where versions differ (for example the location of the Quick Settings output picker), the worksheet's "If you get stuck" box names the alternative route.

## 8. Assessment blueprint (20 items, parallel)

Item N on the pre-test and item N on the post-test check the same skill with a different real-life scenario, and options are shuffled per item at authoring time. The domain counts are Technology Basics 3, Digital Citizenship 3, Information Management 3, Content Creation 3, Communication 3, Collaboration 2 and Safety & Security 3. Items follow the order of the weeks.

| # | Wk | Domain | Skill checked |
|:--|:--|:--|:--|
| 1 | 1 | Technology Basics | Make text bigger in every app (display scale, not browser zoom) |
| 2 | 1 | Technology Basics | Fix a page that spills onto a second sheet (preview, adjust, re-preview) |
| 3 | 1 | Technology Basics | Fix a repeating calendar event on the wrong day (edit the series, check the next one) |
| 4 | 1 | Communication | Write a help request that can be answered (app + version, task, what you tried, exact message) |
| 5 | 2 | Information Management | Narrow a search (place + one filter) |
| 6 | 2 | Information Management | Judge whether a source fits (who runs it, how current, what they sell) |
| 7 | 2 | Information Management | A confirmation shows the wrong choice (use the stated correction route) |
| 8 | 2 | Collaboration | Share with the right roles (reviewer Editor, others Viewer) |
| 9 | 3 | Content Creation | Real heading styles, so titles show in navigation |
| 10 | 3 | Content Creation | A SUM total updates when a value changes |
| 11 | 3 | Digital Citizenship | Use a licensed photo properly (crop a copy, keep the credit) |
| 12 | 3 | Content Creation | Share a handout that looks the same everywhere (export a PDF, open and check it) |
| 13 | 4 | Communication | A clear email request with a specific deadline |
| 14 | 4 | Communication | What Bcc does and doesn't do |
| 15 | 4 | Digital Citizenship | Replace an assumption with respectful, inclusive wording |
| 16 | 4 | Collaboration | Use comments on one shared draft and respond to feedback |
| 17 | 4 | Safety & Security | "Free for 7 days, then $8/month" means a recurring charge |
| 18 | 5 | Digital Citizenship | Status shown by color alone, so add text labels |
| 19 | 5 | Safety & Security | A new account gets a unique strong password and MFA |
| 20 | 5 | Safety & Security | A suspicious call or message, so verify through a known number |

Each item has: `id`, `n`, `form`, `week`, `domain`, `skill`, `stem`, `options[4]`, `answer`, `why` (one plain sentence, used in the key). Distractors are plausible real mistakes, never jokes. Reading level: plain English, short sentences.

The syllabus sentence "Each has 28 questions, four per domain" becomes "Each has 20 questions across the seven IC3 domains".

## 9. Worksheets (missions)

Each mission is a letter page (or half a page for short ones) containing:
- the letterhead, then Name and Workstation # lines
- `WEEK n · MISSION X` and the title, with DO and minutes badges
- Point A and Point B
- 3–6 steps, each with a bold action, the exact path (mono chip), a green "You should see:" line and a checkbox
- If you get stuck (1–2 real snags), Check yourself (2–3 blanks), and Take it home (one line)

Print rules: `@page { size: letter; margin: 0.5in }`, the letterhead repeats per mission, no page breaks inside a step, and it prints correctly in black and white.

## 10. Quality gates

- **New Playwright specs**, under `tests/content/dl2-os-*.spec.js` and `tests/functional/dl2-os-*.spec.js`, check that:
  - the deck keys, build steps and strip work
  - every Week 1 demo runs to its last step without errors
  - the test flow, review-screen skip flags, grading and the PDF all work (download produced, page count, score text)
  - the Netlify POST payload is correct (mocked route) and the offline queue works
  - slide body text is ≥ 32px at 1920×1080
  - no external requests are made
  - keyboard-only operation works
- The existing DL2 specs that assert the replaced files are retired or updated in the same change. Specs for untouched weeks keep passing.
- `node scripts/build-site.js` passes, and axe finds no serious or critical violations on the new pages.
- Every slide, demo and worksheet is screenshot-reviewed at 1920×1080 before Britt sees it.

## 11. Later phases (separate plans)

| Deadline | Work |
|:--|:--|
| Oct 4 | Week 2 deck, demos and missions |
| Oct 11 | Week 3 |
| Oct 18 | Week 4 (heaviest on the test) |
| Oct 25 | Week 5 and the skills challenge (the post-test is already built) |
| Before Nov 2 | Week 6: its own brainstorm. A one-hour, agent-built simple app/SaaS demo, plus the honest back-end story (domains and DNS, hosting, databases, logins, payments, costs, and where things break) |
| Anytime | MP4 exports of the demos, and fictional AI-video warm-up hooks |
