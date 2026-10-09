# Project Memory

## Project Overview
- **Name**: VUB Learning platform (`vublessons`)
- **Description**: Static site hosting four Veterans Upward Bound courses: Intermediate Computer Skills (8 wks), Financial Readiness (5 modules), Digital Literacy L1 (5 wks), Digital Literacy L2 "Mission Control" (6 wks)
- **Tech stack**: Static HTML/CSS/JS, no framework. Node build script (copy-only), Playwright tests, Python link checker
- **Repo**: https://github.com/doclegg05/vublessons — renamed from `VUB-Financial-Readiness` on 2026-07-28; GitHub redirects the old URL
- **Live**: https://vublessons.com (Netlify project `vubcourse`, builds `main` → `dist/site`)

## Current Status
DL2 Weeks 1 and 2 are live. Weeks 3 to 6 were rebuilt on 2026-10-08 as four stacked PRs: #37 Week 3 (base `main`), #38 Week 4, #39 Week 5, #40 Week 6. Each has lesson rounds, no break, no capstone, per-mission practice pages, and a re-recorded video with 10-second pause cards and topic dividers. Each passed the full quality gate. None is merged; each waits for Britt to listen to its video. Merge in order, 37 first (Week 3 is taught 2026-10-12).

## Last Session
- **Date**: 2026-10-09
- **What we worked on**: Weeks 3 to 6 rebuilt to Week 2's method, one PR each, same recipe (`docs/digital-literacy-2/week-03-spec.md` to `week-06-spec.md`). Week 4: one cast (you, Sam, Pat, Alex), one Bcc meaning, two offers with a free trial. Week 5: one scam message, two-step verification throughout, the skills challenge kept as the transfer task. Week 6: agent workflow on three prepared app versions, new Mission 6D on domain, hosting, back end, sign-in, secret keys and a caretaker. All forty chapters re-recorded (about 67k ElevenLabs characters). Gates: 359, 375, 391 and 405 tests passing, 0 broken links, a11y pass. On 2026-10-09 Week 6 got delivered-file checks: new `scripts/dl2/check-render-narration.py` (small.en transcript of the MP4 against the script, all chapters 0.926 or better, nothing spoken during cards) and the fixed `verify-narration-playback.cjs` (all six weeks pass). Both are in `week-06-render-review.md`.
- **What we decided**: No capstones; pause cards hold about 10 seconds and name the worksheet task; a divider opens every topic. Windows 10 consumer ESU date stays October 12, 2027 (Microsoft's page, checked 2026-10-08). Week 6 narration says "to lower case" because the voice misread toLowerCase.
- **Where we left off**: all four PRs open; Week 6 has nothing left that doesn't need Britt. Britt listens to each video, then merges #37, #38, #39, #40 in order (retarget each to `main` as the one below merges).

## Open Items
- [ ] Listen to and merge, in order: #37 Week 3 (taught 2026-10-12), #38 Week 4 (2026-10-19), #39 Week 5 (2026-10-26), #40 Week 6 (2026-11-02). Week 6 chapter 1 runs 163 words per minute, the fastest kept.
- [ ] OpenRouter rejects the stored key (HTTP 401, checked again 2026-10-09), so `render-review.mjs` (the whole-video model review) cannot run. A new key has to go in two places; auto-memory `openrouter-key-two-places` names them. Weeks 3 to 6 were reviewed by hand instead (`docs/digital-literacy-2/review/week-0{3,4,5,6}-render-review.md`).
- [ ] Weeks 1 and 2 videos have short pause prompts and no pause or divider cards; Britt may want the 10-second cards there too.
- [ ] **DL2 Mission Control go-live checks (Week 1 was taught 2026-09-28; these were not re-verified):** enable Netlify form detection → push `feat/dl2-mission-control`, PR, merge → confirm forms `dl2-pretest`/`dl2-posttest` listed + email notifications on → one test submission → test print.
- [x] ~~DL2 Week 2~~ rebuilt for AI-assisted search and merged 2026-10-05 (PR #31).
- [x] ~~DL2 Weeks 3 to 6~~ rebuilt 2026-10-08 (PRs #37 to #40); content checked for out-of-date techniques during the audits.
- [x] ~~Merge PR #33 (Week 2 review fixes)~~ merged and confirmed live 2026-10-05.
- [x] ~~Ship `claude/week-2-practice-new-tab`~~ merged as PR #34 and confirmed live 2026-10-05.
- [ ] Ship `claude/week-2-mission-practice-pages` (Week 2 per-mission practice pages). Weeks 3 to 6 got per-mission practice pages in PRs #37 to #40. At 1366x768 the Week 2 practice form still needs a short scroll to reach its buttons; at 1920x1080 it fits.
- [ ] Decide whether `claude/practice-form-purpose` ships.
- [ ] Week 2 video, found 2026-10-05 (read-only review; nobody listened by ear). Needs a re-render: chapter 1 search box shows "computer help + library + town" from 0:07 to 0:49 while the narrator says to ask in full sentences (`scripts/dl2/video-scenes.py:458`); chapter 4 card rows (Title / address merged, fifth row Interpretation) differ from the five facts spoken. Needs a retake: chapter 4 runs 179 WPM. The doubled "and" near 0:29 was cleared by transcription (8 of 8 decodes). Retake with `scripts/dl2/elevenlabs-takes.py` (Week 2 only until generalized).
- [ ] Lesson plan pause point 3:41 is early; the form prompt ends at 3:47 (`scripts/dl2/curriculum.json`, week 2 `agenda`).
- [ ] Week 2 deck and worksheet items reported to Britt but not fixed: slide 32 "five-field source note" is never defined on a slide; worksheet Round 3 loophole (library open until 9 p.m. versus learning desk until 8 p.m.) and its "partly right" key; "four missions" on slides 2 and 4 versus five listed; rounds start at Round 2; round tables cannot be typed into and print with 9 mm rows; Mission 2D repeats Mission 2C's ZIP task; Show slides 19 and 26 highlight a row their caption does not describe.
- [ ] Revoke the ElevenLabs key at elevenlabs.io once re-recording is done. It lives in the gitignored file `/Users/brittlegg/MacDev/companies/education/vublessons/.claude/worktrees/digital-literacy-week-2-expand-d3d789/.env`.
- [x] ~~Decide whether Weeks 3 to 6 drop the break slide~~ they do (`nobreak` in each week dict, PRs #37 to #40).
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
| 2026-10-08 | Weeks 3 to 6 follow Week 2's method without capstones; videos get 10-second pause cards and topic dividers | Britt: capstones do not fit the class; Week 1 and 2 pauses were too short to catch; topic changes were hard to follow |
| 2026-10-08 | Week 6 keeps the agent workflow on three prepared app versions; Mission 6D teaches the roadblocks to a real service | Learners need no AI account; the live agent run stays optional; the old video taught building from scratch |
| 2026-10-08 | Windows 10 consumer ESU end date stays October 12, 2027 | The audit said 2026; Microsoft's consumer page says 2027 |
| 2026-10-08 | Re-record all ten chapters for each of Weeks 3 to 6, one PR per week | Britt chose full re-records so each video follows its missions; Week 3 is taught first |
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

- **Week modules and video cards (2026-10-08).** Each rebuilt week has a lesson module (`mission-control/week2.py` to `week6.py`) using `lessonkit.py`. The lesson-plan pause times in `curriculum.json` and `dl2-weeks-tsdr.spec.js` are each pause card's `data-start` in `video/digital-literacy-2/week-NN/index.html`, rounded down. Video cards come from `video/digital-literacy-2/week-NN/cards.json` (see `docs/digital-literacy-2/week-03-spec.md` for the rebuild order). The take folder moved from the Desktop to the main checkout (`vub-brad-narration-refresh/`); point `VUB_TAKES_DIR` at it. Britt's card and capstone preferences live in auto-memory (`video-pause-and-topic-cards`, `no-capstones`).

## Known Issues
- **Delivered-file checks are outside `quality.sh` (2026-10-09).** After a render, run `check-render-narration.py --week N --out <json>` with the `video/digital-literacy-2/.venv` Python, and `DL2_SKIP_GALLERY=1 DL2_REVIEW_OUTPUT=<dir> node scripts/dl2/verify-narration-playback.cjs` against `dist/site` served on 127.0.0.1:3948 by a server that answers range requests (`npx serve`; Python's `http.server` does not).
- **Narration take gotchas.** The narrator misreads camelCase code names, and transcript checks sometimes report a doubled word that is not in the audio. Auto-memory holds both (`tts-code-words-spoken`, `recognizer-doubled-words`).
- **`build.py` drops the second field of every Show tuple, in every week.** The demo picture comes from `visuals.py`, so editing a mission's Show values changes nothing on screen. This left Week 2 Mission A picturing the retired keyword search after PR #31. Week 2 Mission A now reads its three values from `week2.py`; Missions B to D and Weeks 3 to 6 still carry unused values.
- **Three Playwright specs hard-code `http://localhost:3939` as the site's own origin** (`dl2-os-week1-deck`, `dl2-os-sound-test`, `dl2-os-test`). Running the suite against another port fails them for that reason only.
- **The DL2 practice library scrolls at 1366x768** (pages are 1525 to 2390 px tall). The slide-fit work is on the unmerged branch `claude/slide-redesign-presentation-b1ed80`, which predates Mission Control.
- **Video visual reviewers measure ink, not font size.** In the 2026-09-24 review, "text at 17 to 23 px" came from glyph-row measurements on frames; those are about 70% of the CSS font size, and only the brand mark (21px) and a few labels (23px) were really under the 24px floor. Brief reviewers to report font-size, or run `check-text-floor.py`. Auto-memory holds the general rule.
- `week-04.mp4` kept its original higher-bitrate AAC track because it was already at -18 LUFS when `normalize-loudness.py` ran (13.9 MB vs about 10.5 MB for the others). Harmless; drop the skip branch if uniform encoding matters.
- **Assessment drift is the recurring failure mode here.** Week 2's lesson changed in June 2026 but its pre/post questions weren't updated until 2026-07-28 — veterans were tested on Zoom and VA Video Connect for a lesson that taught Windows shortcuts. `AGENTS.md` now carries a rule: changing what a week teaches means updating the interactive test, the printable test, the printable **answer key**, the intro topic list, and `syllabus-overview.html` in the same commit.
- **Assert on behaviour, not styling.** The DL1 sidebar tests failed from the day the feature landed (2026-06-29) to 2026-07-28 while a sibling assertion — `overflow-y` is `auto` on `.sidebar` — kept passing on an element that never scrolls. Style properties prove intent, not effect; pair them with a `scrollHeight > clientHeight`-style check.
- The `_archive/README.md` claim that Copy #2 "differs from canonical only by baked cohort dates + 1 pedagogical line" is **wrong** — Week 2 was an entirely different lesson. Don't trust that assessment for other files without re-diffing.
- DL1 per-week lesson MP4s still unrendered (needs ElevenLabs key + hero assets; see `video/digital-literacy-1/README.md`).
