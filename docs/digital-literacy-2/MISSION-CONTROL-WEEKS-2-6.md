# Weeks 2–6 Mission Control review

This extension carries the existing Week 1 navy, gold, cyan, typography, panel, stage-badge and phase-navigation system through the remaining five weeks. Each lesson has 23 slides: welcome and prior experience, an overview, four Tell/Show/Do/Review missions, a protected eight-minute break, individual evidence, transfer and completion.

## Exact teaching and material map

Each mission has a matching worksheet section (`m2A`, for example), answer/observation guide section, and instructor notes. Each week has a date-free 120-minute lesson plan, landscape run sheet and a detailed interactive practice library. The presentation’s Do slide links to its worksheet section and related practice exercise.

| Week | Mission A | Mission B | Mission C | Mission D |
|---|---|---|---|---|
| 2 | Search, evaluation, source trail | Required fields, privacy, confirmation | Naming, ZIP/extract, recovery | Access roles, ownership, sync/backup |
| 3 | Heading structure, shortcuts, tracked edits | Predict and check SUM | Three slides, crop, alt text, credit | Formats, PDF inspection, trim/split |
| 4 | Channel, account, email, recipient roles | Shared-copy roles and comment resolution | Meeting controls, captions, community norms | Payment, total cost, renewal and cancellation |
| 5 | Comfort, accessibility and attention | Phishing, identity and independent verification | Permissions, updates, locking and encryption | Five observed skills; post-test follows separately |
| 6 | Bounded agent spec and predictions | Requested versus unrequested diff | Reproduce, report, repair and retest | Browser/server boundary and operating responsibilities |

Main-deck routes are `weeks/week-02/presentation.html` through `week-06/presentation.html`. Slides 4–7, 8–11, 13–16 and 17–20 hold missions A–D; slide 12 is the break. Each Show has three manually advanced visual states with Previous/Next/Replay. Each Review accepts keyboard-operated choices and gives explanatory feedback. F toggles fullscreen; N toggles notes. A visible toolbar and mission selector supplement the six phase buttons.

The existing full computer simulations now live at each week's `practice.html`, retaining their exercise numbers and functionality. They include form validation, file recovery, spreadsheet calculation, crop/trim models, email drafting, meeting controls and the real three-version resource finder. Browsing practice does not overwrite main-deck progress. The diagrams in the main deck are clearly labeled fictional demonstrations; they are not claims of operating an actual signed-in account.

## Pacing and alternatives

All plans total 120 minutes and protect the eight-minute break. Week 3 runs Word, Excel and PowerPoint sequentially using supplied wording and the fresh CSV. Charts, extra decoration and advanced media edits are optional; document structure, a tested formula, three simple slides with image treatment, and checked PDF remain essential.

Week 5 reserves 26 minutes for the observed five-task challenge and 22 minutes for the existing 20-question post-test. Independent / With prompt / Needs practice observations remain separate from the test score. Week 6 uses the prepared app versions by default and its separate 8-point extension rubric. An instructor-led live agent demonstration and hand repair are optional. No new learner account or purchase is required.

Account-free browser simulations and paper annotations are available where software or accounts are unavailable. Instructors record the route used; a paper prediction is not reported as an observed application skill. Videos remain optional chapter replay resources, without adding hidden viewing time to the lesson plan.

## Authoring and protected boundaries

Run `python3 scripts/dl2/mission-control/build.py` from the repository root. Edit `content.py` for sequence, `visuals.py` for original diagrams, and `build.py` for output. Detailed lab procedures and evidence remain in `scripts/dl2/curriculum.json`; practice templates live under `mission-control/practice/`. The old whole-course generator refuses to run because it would overwrite Mission Control and the current assessments.

Week 1, assessment items/keys/printables, published media, transcripts, collection identifiers and email/PDF infrastructure are preserved. The shared assessment app has only two learner-copy substitutions: answers/score are stored for the instructor; accepted results are described as submitted for Britt. It does not claim inbox delivery. Failure, retry and saved-PDF instructions remain intact. Copy verification intercepts submissions locally; no learner record or outgoing email is generated.

The Start fresh action now also clears the new worksheet session evidence and Mission Control slide positions while preserving the pending-submission outbox. Course-home Continue links carry the saved slide, so resuming works in a new tab as well as the original tab.

## Validation

Local evidence: the full quality gate passed with 317 Playwright tests, 10 server/email tests, 1,527 internal links and zero broken references, and the accessibility ratchet. The final practice-link adjustments were followed by 11 passing Mission Control checks and direct browser verification of each changed destination. All five run sheets print on one landscape page. The retained practice-library fullscreen exit/restart race was reproduced, repaired, and passed eight repeated transition checks.

- Full repository quality gate, including build, links, catalog, server email tests, Playwright, accessibility and readability report.
- Dedicated all-week slide checks at 1366×768 and 1920×1080, default and enlarged text, including every guided state and answer explanation.
- Keyboard choices, phase/mission controls, notes, reload, week isolation, shared-PC clearing, mobile overflow and printable typed evidence.
- Preserved simulation regression coverage follows the new practice-library routes; main-deck behavior has dedicated new tests.
- Printed five single-page landscape run sheets and representative Week 3/6 worksheets; inspected mobile, projector, and print output.

This is a draft review change. Production deployment requires the separate release decision. The separate narration refresh remains unpublished and is not included.
