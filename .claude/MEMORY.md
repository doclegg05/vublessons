# Project Memory

## Project Overview
- **Name**: VUB Learning platform (`vublessons`)
- **Description**: Static site hosting three Veterans Upward Bound courses — Intermediate Computer Skills (8 wks), Financial Readiness (5 modules), Digital Literacy L1 (5 wks)
- **Tech stack**: Static HTML/CSS/JS, no framework. Node build script (copy-only), Playwright tests, Python link checker
- **Repo**: https://github.com/doclegg05/vublessons — renamed from `VUB-Financial-Readiness` on 2026-07-28; GitHub redirects the old URL
- **Live**: https://vublessons.com (Netlify project `vubcourse`, builds `main` → `dist/site`)

## Current Status
DL2 "Mission Control" (Week 1 with 20-question pre/post tests, plus Weeks 2 to 6 decks) is on `main` (PRs #28 and #31; Netlify builds `main`). Week 2 teaches AI-assisted search as of PR #31. On 2026-10-05 vublessons.com matched `main` for the eight Week 2 pages, the video, captions and deck assets (hash and text compare). Five Week 2 review fixes merged as PR #33 on 2026-10-05 and were confirmed on vublessons.com the same day. PR #34 (practice button opens a new tab) and PR #35 (one practice page per Week 2 mission) merged and were confirmed live the same day. Weeks 3 to 6 still use the original Mission Control content and still carry the 8-minute break slide.

## Last Session
- **Date**: 2026-10-05 (second session of the day: review before Britt taught Week 2)
- **What we worked on**: Reviewed the Week 2 deck, worksheet, practice library and video. Fixed five things Britt picked, in `scripts/dl2/mission-control/` (`week2.py`, `visuals.py`, `build.py`) plus one scoped line in `os/missions.css`, then rebuilt Week 2: slide 6 demo now shows question, AI answer (until 9 p.m.) and library page (until 8 p.m.); slide 11 asks about "open until"; six paper rounds are labelled Worksheet; slide 21 names its folders and has a doable Done early line; each mission answer box now sits before its rounds. New `tests/content/dl2-week2-consistency.spec.js` (5 tests, watched fail first); full suite 334 passed.
- **What we decided**: Fix only what Britt named; report the rest. Britt objected to design and UI changes the earlier session made without being asked (auto-memory `no-unrequested-design-changes` holds the rule).
- **Where we left off**: PRs #33 and #34 merged and confirmed live. The new tab did not fix Britt's real complaint: "Open interactive practice" led into the practice library, which is the older 23-slide Week 2 lesson kept whole, so it read as a second lesson. Britt said the class works through the worksheet, with little projector demonstration, and approved one practice page per mission. Branch `claude/week-2-mission-practice-pages` builds `practice-2b.html`, `practice-2c.html` and `practice-2d.html` for Week 2, repoints the worksheet and slide links, removes the Mission 2A practice link and removes Mission 2D's copy of the ZIP task. Merged as PR #35 and confirmed live. Last change of the session: the lesson plan's video pause point 3:41 became 3:47, where the form prompt ends, on branch `claude/week-2-pause-point`.

## Open Items
- [ ] **DL2 Mission Control go-live checks (Week 1 was taught 2026-09-28; these were not re-verified):** enable Netlify form detection → push `feat/dl2-mission-control`, PR, merge → confirm forms `dl2-pretest`/`dl2-posttest` listed + email notifications on → one test submission → test print.
- [x] ~~DL2 Week 2~~ rebuilt for AI-assisted search and merged 2026-10-05 (PR #31).
- [ ] DL2 Weeks 3 to 6 (weekly); Week 6 needs its own brainstorm (agent-built app + domains/hosting/back-end roadblocks). Review each week's search or tool content for out-of-date techniques before teaching, as Week 2 needed.
- [x] ~~Merge PR #33 (Week 2 review fixes)~~ merged and confirmed live 2026-10-05.
- [x] ~~Ship `claude/week-2-practice-new-tab`~~ merged as PR #34 and confirmed live 2026-10-05.
- [x] ~~Ship `claude/week-2-mission-practice-pages`~~ merged as PR #35 and confirmed live 2026-10-05.
- [ ] Weeks 3 to 6 still link each mission to a numbered slide in their practice library, in the same tab. They need the Week 2 treatment (`practice_pages=True`) before they are taught. At 1366x768 the Week 2 practice form still needs a short scroll to reach its buttons; at 1920x1080 it fits.
- [ ] Decide whether `claude/practice-form-purpose` ships.
- [ ] Week 2 video, found 2026-10-05 (read-only review; nobody listened by ear). Needs a re-render: chapter 1 search box shows "computer help + library + town" from 0:07 to 0:49 while the narrator says to ask in full sentences (`scripts/dl2/video-scenes.py:458`); chapter 4 card rows (Title / address merged, fifth row Interpretation) differ from the five facts spoken. Needs a retake: chapter 4 runs 179 WPM. The doubled "and" near 0:29 was cleared by transcription (8 of 8 decodes). Retake with `scripts/dl2/elevenlabs-takes.py` (Week 2 only until generalized).
- [x] ~~Lesson plan pause point 3:41~~ changed to 3:47 on 2026-10-05, in both the week 2 `agenda` and `prep` text of `scripts/dl2/curriculum.json`.
- [ ] Week 2 deck and worksheet items reported to Britt but not fixed: slide 32 "five-field source note" is never defined on a slide; worksheet Round 3 loophole (library open until 9 p.m. versus learning desk until 8 p.m.) and its "partly right" key; "four missions" on slides 2 and 4 versus five listed; rounds start at Round 2; round tables cannot be typed into and print with 9 mm rows; Mission 2D repeats Mission 2C's ZIP task; Show slides 19 and 26 highlight a row their caption does not describe.
- [ ] Revoke the ElevenLabs key at elevenlabs.io once re-recording is done. It lives in the gitignored file `/Users/brittlegg/MacDev/companies/education/vublessons/.claude/worktrees/digital-literacy-week-2-expand-d3d789/.env`.
- [ ] Decide whether Weeks 3 to 6 drop the break slide (Week 2 did; Britt's standing rule is no breaks). Generator flag: `nobreak` in the week dict.
- [ ] Don't run `scripts/dl2/build-pages.py` — it would overwrite the new Week 1 and test files (see HANDOFF.md).
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
| 2026-09-27 | DL2 rebuilt fresh as "Mission Control" (hand-written HTML + small os/ engine), not the old scripts/dl2 generators | Britt disliked the generated version; hand-authored slides allow build steps, OS transitions and coded Windows demos |
| 2026-09-27 | DL2 pre/post = 20 parallel items (item N same skill), one item bank feeds test, keys, printables, PDF | Britt asked for 20; single source keeps pre/post aligned |
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

- **Per-mission practice pages (Week 2).** A week dict with `practice_pages=True` gets one page per mission simulation (`practice-2b.html` and so on), cut by `activity_page()` in `build.py` from that week's practice library. A mission whose `practice` is `None` gets no practice link. `assets/lesson.js` throws if the deck controls are missing, so the pages keep them in the markup and `os/mission-practice.css` hides them under `.mission-activity`. The practice library is the pre-Mission Control lesson deck kept whole, which is why a link into it reads as a second lesson.

## Known Issues
- **`build.py` drops the second field of every Show tuple, in every week.** The demo picture comes from `visuals.py`, so editing a mission's Show values changes nothing on screen. This left Week 2 Mission A picturing the retired keyword search after PR #31. Week 2 Mission A now reads its three values from `week2.py`; Missions B to D and Weeks 3 to 6 still carry unused values.
- **Three Playwright specs hard-code `http://localhost:3939` as the site's own origin** (`dl2-os-week1-deck`, `dl2-os-sound-test`, `dl2-os-test`). Running the suite against another port fails them for that reason only.
- **The DL2 practice library scrolls at 1366x768** (pages are 1525 to 2390 px tall). The slide-fit work is on the unmerged branch `claude/slide-redesign-presentation-b1ed80`, which predates Mission Control.
- **Video visual reviewers measure ink, not font size.** In the 2026-09-24 review, "text at 17 to 23 px" came from glyph-row measurements on frames; those are about 70% of the CSS font size, and only the brand mark (21px) and a few labels (23px) were really under the 24px floor. Brief reviewers to report font-size, or run `check-text-floor.py`. Auto-memory holds the general rule.
- `week-04.mp4` kept its original higher-bitrate AAC track because it was already at -18 LUFS when `normalize-loudness.py` ran (13.9 MB vs about 10.5 MB for the others). Harmless; drop the skip branch if uniform encoding matters.
- **Assessment drift is the recurring failure mode here.** Week 2's lesson changed in June 2026 but its pre/post questions weren't updated until 2026-07-28 — veterans were tested on Zoom and VA Video Connect for a lesson that taught Windows shortcuts. `AGENTS.md` now carries a rule: changing what a week teaches means updating the interactive test, the printable test, the printable **answer key**, the intro topic list, and `syllabus-overview.html` in the same commit.
- **Assert on behaviour, not styling.** The DL1 sidebar tests failed from the day the feature landed (2026-06-29) to 2026-07-28 while a sibling assertion — `overflow-y` is `auto` on `.sidebar` — kept passing on an element that never scrolls. Style properties prove intent, not effect; pair them with a `scrollHeight > clientHeight`-style check.
- The `_archive/README.md` claim that Copy #2 "differs from canonical only by baked cohort dates + 1 pedagogical line" is **wrong** — Week 2 was an entirely different lesson. Don't trust that assessment for other files without re-diffing.
- DL1 per-week lesson MP4s still unrendered (needs ElevenLabs key + hero assets; see `video/digital-literacy-1/README.md`).
