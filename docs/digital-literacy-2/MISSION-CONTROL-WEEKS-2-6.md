# Weeks 2–6 Mission Control review

This extension carries the existing Week 1 navy, gold, cyan, typography, panel, stage-badge and phase-navigation system through the remaining five weeks. Each lesson has 24 slides: playable captioned opening video, welcome and prior experience, an overview, four Tell/Show/Do/Review missions, a protected eight-minute break, individual evidence, transfer and completion.

## Exact teaching and material map

Each mission has a matching worksheet section (`m2A`, for example), answer/observation guide section, and instructor notes. Each week has a date-free 120-minute lesson plan, landscape run sheet and a detailed interactive practice library. The presentation’s Do slide links to its worksheet section and related practice exercise.

| Week | Mission A | Mission B | Mission C | Mission D |
|---|---|---|---|---|
| 2 | Search, evaluation, source trail | Required fields, privacy, confirmation | Naming, ZIP/extract, recovery | Access roles, ownership, sync/backup |
| 3 | Heading structure, shortcuts, tracked edits | Predict and check SUM | Three slides, crop, alt text, credit | Formats, PDF inspection, trim/split |
| 4 | Channel, account, email, recipient roles | Shared-copy roles and comment resolution | Meeting controls, captions, community norms | Payment, total cost, renewal and cancellation |
| 5 | Comfort, accessibility and attention | Phishing, identity and independent verification | Permissions, updates, locking and encryption | Five observed skills; post-test follows separately |
| 6 | Bounded agent spec and predictions | Requested versus unrequested diff | Reproduce, report, repair and retest | Browser/server boundary and operating responsibilities |

Main-deck routes are `weeks/week-02/presentation.html` through `week-06/presentation.html`. Slides 5–8, 9–12, 14–17 and 18–21 hold missions A–D; slide 13 is the break. Each Show has three manually advanced visual states with Previous/Next/Replay. Each Review accepts keyboard-operated choices and gives explanatory feedback. F toggles fullscreen; N toggles notes. A visible toolbar and mission selector supplement the six phase buttons.

The existing full computer simulations now live at each week's `practice.html`, retaining their exercise numbers and functionality. They include form validation, file recovery, spreadsheet calculation, crop/trim models, email drafting, meeting controls and the real three-version resource finder. Browsing practice does not overwrite main-deck progress. The diagrams in the main deck are clearly labeled fictional demonstrations; they are not claims of operating an actual signed-in account.

## Pacing and alternatives

All plans total 120 minutes and protect the eight-minute break. Week 3 runs Word, Excel and PowerPoint sequentially using supplied wording and the fresh CSV. Charts, extra decoration and advanced media edits are optional; document structure, a tested formula, three simple slides with image treatment, and checked PDF remain essential.

Week 5 reserves 26 minutes for the observed five-task challenge and 22 minutes for the existing 20-question post-test. Independent / With prompt / Needs practice observations remain separate from the test score. Week 6 uses the prepared app versions by default and its separate 8-point extension rubric. An instructor-led live agent demonstration and hand repair are optional. No new learner account or purchase is required.

Account-free browser simulations and paper annotations are available where software or accounts are unavailable. Instructors record the route used; a paper prediction is not reported as an observed application skill. The opening video occupies minutes 0–8, followed by three minutes of welcome/prior experience and two minutes of mission overview. Later chapter replay is optional. All mission, break and assessment blocks retain their durations.

## Authoring and protected boundaries

Run `python3 scripts/dl2/mission-control/build.py` from the repository root. Edit `content.py` for sequence, `visuals.py` for original diagrams, and `build.py` for output. Detailed lab procedures and evidence remain in `scripts/dl2/curriculum.json`; practice templates live under `mission-control/practice/`. The old whole-course generator refuses to run because it would overwrite Mission Control and the current assessments.

Week 1 now has 28 slides: pre-test directions/link first, playable captioned video second, then the existing welcome and teaching slides. Its first 20 minutes remain the pre-test, followed by 8 minutes of video, 8 minutes of welcome/intro, the unchanged mission durations and 12 minutes to close. Assessment items/keys/printables, published media, transcripts, collection identifiers and email/PDF infrastructure are preserved. The shared assessment app has only two learner-copy substitutions: answers/score are stored for the instructor; accepted results are described as submitted for Britt. It does not claim inbox delivery. Failure, retry and saved-PDF instructions remain intact. Copy verification intercepts submissions locally; no learner record or outgoing email is generated.

The Start fresh action now also clears the new worksheet session evidence and Mission Control slide positions while preserving the pending-submission outbox. Course-home Continue links carry the saved slide, so resuming works in a new tab as well as the original tab.

## Validation

Local evidence: the full quality gate passed with 329 Playwright tests, 10 server/email tests, 1,559 internal links and zero broken references, and the accessibility ratchet. Eleven dedicated opening-media checks passed, including real playback/captions for all six weeks, native video keys, leaving-slide pause, new-tab pre-test return, projector/mobile fit, and saved-state migration. Fifteen focused Week 1 content/print checks passed. All six run sheets print on one landscape page. The retained practice-library fullscreen exit/restart race was reproduced, repaired, and passed eight repeated transition checks.

- Full repository quality gate, including build, links, catalog, server email tests, Playwright, accessibility and readability report.
- Dedicated all-week slide checks at 1366×768 and 1920×1080, default and enlarged text, including every guided state and answer explanation.
- Keyboard choices, phase/mission controls, notes, reload, week isolation, shared-PC clearing, mobile overflow and printable typed evidence.
- Preserved simulation regression coverage follows the new practice-library routes; main-deck behavior has dedicated new tests.
- Printed five single-page landscape run sheets and representative Week 3/6 worksheets; inspected mobile, projector, and print output.

This is a draft review change. Production deployment requires the separate release decision. The Brad narration refresh from merged PR #29 is live and its approved media/caption hashes are used here. The Mission Control design and opening placement remain preview-only in draft PR #28.

## Opening placement and resume contract

`mission-control/week-01.html` is now the canonical Week 1 deck template. `opening.py` builds the shared media slide using the approved manifest and independent content hashes for MP4/captions. The generator owns the rendered Week 1 presentation and Weeks 2–6 materials; Week 1 worksheet, answer key, run sheet and lesson plan remain hand-authored. Practice snapshot timings/URLs match the approved Brad media.

Videos do not autoplay. Native controls retain their keyboard shortcuts. Leaving a video slide or leaving the page pauses it; returning keeps its position but does not resume playback. Transcript/chapter and pre-test links are clearly labeled new tabs. The Continue button, phase strip, arrow keys outside the player and Weeks 2–6 mission chooser navigate the deck.

Session positions migrate once using the opening-v1 marker. Week 1 old title moves to slide 3, old pre-test moves to slide 1, other old slides shift by one. Weeks 2–6 old positions shift by one. Course-home Continue links carry the previous total to identify older layouts; unrecognized legacy deck totals restart at the opening. Explicit numeric and #slide-N links use current numbering, except a hash matching an unversioned saved session is treated as that session's old position. Invalid bounds clamp to the deck. New saved positions persist normally, including reload and browser back/forward hash navigation. Worksheet mission anchors and practice exercise numbers do not change.

Existing limitation: Week 6's approved video is a general app-building introduction. It does not demonstrate every step of the specific three-version diff/repair/retest missions. The video notes disclose this; the worksheet and guided missions remain the source for those steps. No narration or curriculum rewrite was included.
