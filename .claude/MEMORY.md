# Project Memory

## Project Overview
- **Name**: VUB Learning platform (`vublessons`)
- **Description**: Static site hosting three Veterans Upward Bound courses — Intermediate Computer Skills (8 wks), Financial Readiness (5 modules), Digital Literacy L1 (5 wks)
- **Tech stack**: Static HTML/CSS/JS, no framework. Node build script (copy-only), Playwright tests, Python link checker
- **Repo**: https://github.com/doclegg05/vublessons — renamed from `VUB-Financial-Readiness` on 2026-07-28; GitHub redirects the old URL
- **Live**: https://vublessons.com (Netlify project `vubcourse`, builds `main` → `dist/site`)

## Current Status
Four courses, all on `main` and live. Digital Literacy Level 2 merged 2026-09-24 (PR #17) with the review fixes (PR #18). Full Playwright
suite 128/128, link check 0 broken. Cohort starts 2026-09-28 per the DL2 syllabus.

## Last Session
- **Date**: 2026-09-24
- **What we worked on**: Two six-agent reviews of Digital Literacy Level 2 (course pages and assessments; then the six lesson videos), then fix passes for both: the six High course findings in the `scripts/dl2/` generators plus `course.css` and `assessment.js`, and every visual and caption video finding in `screen-share-scenes.py`, `video-scenes.py` and `build-media.py`, with all six videos re-rendered, normalized and re-verified. Review reports were delivered to Britt as files (session scratchpad, not in the repo). Merged as PRs #17 (course), #18 (fixes) and #19 (memory); live on vublessons.com.
- **What we decided**: Course content does not need veteran / VA / telehealth framing unless the topic calls for it (auto-memory holds the detail: `dl2-veteran-framing-not-required`). Decks keep starting keyboard focus inside the current slide; the skip link only had to become focusable. Topic-button accessible names come from a synced `aria-label`, not a hidden span (a hidden span escaped the scrolling row and broke mobile).
- **Where we left off**: PR #17 (course) and PR #18 (review fixes) both merged to main and deployed. Quality gate passed before push. Six videos re-rendered and re-verified. Remaining course findings (2 mobile Highs from the UI pass, 32 Mediums) not yet actioned. Video narration items need a re-record (listed in HANDOFF.md).

## Open Items
- [x] ~~DL2 video review fixes~~ done 2026-09-24: all visual and caption findings fixed in the generators and re-rendered (see HANDOFF.md "Video review fixes"). Still open, need a re-record: pause-prompt timing, fast chapters, week 3 formula cause, week 6 undefined terms, week 5 challenge setup.
- [x] ~~Merge PR #17 then PR #18~~ both merged to main 2026-09-24; Netlify deployed the DL2 course and the review fixes to vublessons.com.
- [ ] DL2 UI Highs still open: Text Size widget covers text on `activities/resource-finder.html` at mobile width (page loads no course CSS); syllabus and sources tables overflow at 375px (`.table-scroll` exists, unused).
- [ ] DL2 Mediums from the 2026-09-24 review (post-test guessability, throwaway knowledge-check distractors, four untested IC3 objective groups, answer key reachable from learner nav, no `<h1>` in decks, undefined terms, thin instructor guide).
- [x] ~~Disable GitHub Pages on `doclegg05/VUB-Course`~~ — done 2026-07-28. `doclegg05.github.io/VUB-Course/` now 404s.
- [x] ~~Re-archive `doclegg05/VUB-Course` read-only~~ — done 2026-07-28. Archived, public, content preserved at `2870359` (includes the retired Video Conferencing Week 2).
### ⚠️ ON THE WINDOWS MACHINE — two tasks, can't be done from the Mac
Britt asked to be reminded of both (2026-07-28).

- [ ] **W1. Push the VUB-Course freeze refs.** *(data-loss risk — do this first)*

  `preflight-freeze-2026-06-03` (`42619ff`) and branch `freeze/preflight-2026-06-03` exist **only** in the Windows machine's local `_archive/VUB-Course-2026-06-03/`. `git ls-remote doclegg05/VUB-Course` returns `refs/heads/main` and nothing else. That commit captured ~33 files never merged to `main` — this is the sole copy. If that machine dies, so does the snapshot.

  **`doclegg05/VUB-Course` is archived read-only, and archived repos reject pushes.** Unarchive first or the push fails confusingly:

  ```bash
  gh api -X PATCH repos/doclegg05/VUB-Course -f archived=false
  cd "C:/Users/Instructor/Dev/curriculum/VUB Lessons/_archive/VUB-Course-2026-06-03"   # verify path
  git push origin preflight-freeze-2026-06-03 freeze/preflight-2026-06-03
  gh api -X PATCH repos/doclegg05/VUB-Course -f archived=true
  ```

  Verify with `git ls-remote --tags origin`, then tick this box.

- [ ] **W2. Repoint this clone at the renamed remote.** *(cosmetic — GitHub redirects, nothing is broken)*

  This repo was renamed `VUB-Financial-Readiness` → `vublessons` on 2026-07-28. Run inside the Windows clone:

  ```bash
  git remote set-url origin https://github.com/doclegg05/vublessons.git
  git remote -v   # confirm, then tick this box
  ```

  Consider renaming the Windows folder to match too (on the Mac it's now `MacDev/projects/vublessons`).
- [x] ~~5 failing `tests/functional/dl1-sidebar-scroll.spec.js` cases~~ — fixed 2026-07-28. Suite now **18/18**.
- [x] ~~Rename repo → `vublessons`~~ — done 2026-07-28. Netlify survived (new deploy `6a68ddbd` built from `doclegg05/vublessons`, state ready). Local folder also renamed to `MacDev/projects/vublessons`.

## Key Decisions Log
| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-07-28 | Keep Windows Tips as Week 2; rewrite the 6 Video Conferencing test questions | Windows was the deployed canonical curriculum; the tests were the thing out of sync, not the lesson |
| 2026-07-28 | Delete the 3 Zoom/telehealth handouts | Orphaned under a Windows lesson after the topic swap; nothing else linked them |
| 2026-07-28 | Retire `VUB-Course` instead of merging | Platform copy was strictly ahead (a11y fixes, resources sections, shared/ integration); only Week 2 differed, and that was a deliberate curriculum change |
| 2026-07-28 | Defer repo rename | Only step with real deploy risk; no functional benefit today |
| 2026-07-28 | **Reversed the above — renamed to `vublessons`** | Britt asked for it. Preflight showed the risk was low: Netlify links via the GitHub App (repo ID, not name) and the repo had no classic webhooks. Confirmed after by a fresh deploy building from `doclegg05/vublessons` |
| 2026-07-28 | Fix the DL1 sidebar *tests*, not the page | The feature works — verified by scrolling the real container and by a real mouse wheel. The tests drove `.sidebar`, which never overflows, so the scroll was a no-op. Wrong expectation in the test |

## Architecture Notes
- `courses.json` is the **catalog source of truth** — drives the homepage and course consoles. It is *not* generated from the course trees; adding a lesson means editing both.
- `scripts/build-site.js` is a **copy, not a bundler**. New load-bearing top-level files must be added to its `PUBLISH` array or they silently won't deploy.
- `shared/` (brand.css, shell.js, text-size.js, progress.js, glossary.js…) is referenced with **root-absolute** paths, so pages only work when served from the site root — not opened off disk.
- **GitHub Pages is also enabled on this repo** and serves the repo root, ignoring `netlify.toml`. The pretty URLs (`/financial-readiness`, `/computer-skills`, `/syllabus`, `/intake`) 404 there. `vublessons.com` is the real site.
- Docs under `docs/` are historical and contain dead Windows paths (`C:/Users/Instructor/Dev/...`). Treat as history, not instructions.
- **`.gitignore` uses `.claude/*`, not `.claude/`, on purpose.** Only `MEMORY.md` is tracked under `.claude/`; the negation that allows it can't work under the trailing-slash form, because git won't re-include a file whose parent directory is excluded. Keep the `/*` form if you add another tracked file there.
- **DL1 lesson sidebar scrolls on an INNER element.** `.sidebar` (the `<nav>`) carries `overflow-y: auto` but never overflows; the real scroller is `.sidebar-scroll-container` (`flex: 1; overflow-y: auto`), which keeps the sidebar header and slide counter fixed. Script or test the inner element — driving `.sidebar.scrollTop` is a silent no-op.
- **DL2 media pipeline (2026-09-24).** Generators in `scripts/dl2/` (`video-scenes.py` diagrams, `screen-share-scenes.py` demos, `build-media.py` compositions and caption cues). Rebuild order after a visual edit: `build-media.py` (full mode rewrites the .vtt), `check-screen-shares.mjs`, `check-text-floor.py`, `check-captions.py`, then per week `npx hyperframes@0.8.58 check --strict --contrast --json > docs/digital-literacy-2/video-check-0N.json` and `render`, then `normalize-loudness.py`, `verify-screen-share-frames.py`, `verify-media.py` (rewrites `media/manifest.json`; `build-site.js` asserts those hashes). Strict check about 2 min and render about 4.5 min per video on the M4; two renders in parallel are fine. Full write-up in `docs/digital-literacy-2/HANDOFF.md` "Video review fixes".
- **DL2 git-ignored working files.** `video/digital-literacy-2/week-0N/narration/*.wav` and `generated-screen-share/workstation.mp4` are ignored and exist only in the main checkout at `MacDev/companies/education/vublessons/`. A fresh worktree cannot build or strict-check the videos until they are copied in; `verify-media.py` checks the WAV hashes against `*.words.json`.

## Known Issues
- **Video visual reviewers measure ink, not font size.** In the 2026-09-24 review, "text at 17 to 23 px" came from glyph-row measurements on frames; those are about 70% of the CSS font size, and only the brand mark (21px) and a few labels (23px) were really under the 24px floor. Brief reviewers to report font-size, or run `check-text-floor.py`. Auto-memory holds the general rule.
- `week-04.mp4` kept its original higher-bitrate AAC track because it was already at -18 LUFS when `normalize-loudness.py` ran (13.9 MB vs about 10.5 MB for the others). Harmless; drop the skip branch if uniform encoding matters.
- **Assessment drift is the recurring failure mode here.** Week 2's lesson changed in June 2026 but its pre/post questions weren't updated until 2026-07-28 — veterans were tested on Zoom and VA Video Connect for a lesson that taught Windows shortcuts. `AGENTS.md` now carries a rule: changing what a week teaches means updating the interactive test, the printable test, the printable **answer key**, the intro topic list, and `syllabus-overview.html` in the same commit.
- **Assert on behaviour, not styling.** The DL1 sidebar tests failed from the day the feature landed (2026-06-29) to 2026-07-28 while a sibling assertion — `overflow-y` is `auto` on `.sidebar` — kept passing on an element that never scrolls. Style properties prove intent, not effect; pair them with a `scrollHeight > clientHeight`-style check.
- The `_archive/README.md` claim that Copy #2 "differs from canonical only by baked cohort dates + 1 pedagogical line" is **wrong** — Week 2 was an entirely different lesson. Don't trust that assessment for other files without re-diffing.
- DL1 per-week lesson MP4s still unrendered (needs ElevenLabs key + hero assets; see `video/digital-literacy-1/README.md`).
