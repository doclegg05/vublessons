# Site audit repairs — September 21, 2026

Three parallel agents implemented the assessment/print, Computer Skills shell, and VA/instructor-page repairs from [the site review](2026-09-21-site-review.md). The parent integrated the changes, repaired Financial Readiness contrast, expanded the accessibility gate, reviewed the result, and ran the full quality suite. An independent agent cross-reviewed assessment pairing and verified completed reports remain stable when another tab changes the saved pre-test.

## Outcome

| Finding | Result |
|---|---|
| F1: mixed-student comparisons | Fixed. Comparison requires a deliberate saved-attempt choice and matching entered name; names alone never enable it. Editing identity or replacing the baseline before grading revokes pairing. Completed screen/export/print results retain their own snapshot. Saved names are concealed until requested. Clear-results affects only the current course. |
| F2: outdated VA sign-in | Fixed across teaching, handouts, course/catalog/syllabus references, and assessment wording. See [official sources and detailed scope](2026-09-21-va-intake-repairs.md). |
| F3: mobile slide overflow | Fixed across all eight Computer Skills decks, including menu/focus behavior and keyboard-scrollable tables. |
| F4: missing text sizing | Fixed across all eight decks; 32px slide body floor and 36/40/44px enlargement. Controls do not overlap Help. |
| F5: hosted preview failure | Resolved by the fresh branch deployment of `c946373`. Netlify reports success, hosted assets match local SHA-256 hashes, and the hosted mobile/intake/assessment smoke checks pass. The earlier failure's cause remains unknown because the Netlify connector needs reauthentication. Production was not changed. |
| F6: intake success redirect | Fixed to the actual canonical page: `/instructors/intake?success=1`. Tested through GET navigation with no form submission. |
| F7: contrast | Fixed reported lesson labels, instructor footers, and Financial Readiness assessment button (light/dark/hover). Removed the gradient text override from financial statistics, retaining its solid theme-aware foreground. |
| F8: blank DL1 print sheets | Fixed pre/post print flow by removing non-report content from layout. Letter/A4 checks preserve all 20 answer rows without empty trailing sheets. |

## Verification

- **117 tests passed in the full local quality gate**, including 35 new tests at the time of that run. Two additional completed-report immutability tests were subsequently added; the complete 14-test assessment file also passed separately against the built tree (119 distinct passing tests total). No learner source changed after the full build.
- **34 page states passed expanded axe WCAG A/AA checks with zero violations.** These include every catalog lesson's initial state, course/assessment entries and instructor intake/classes. Removed the previous financial contrast allowance. Finite entrance animations are settled before measurement.
- Build and catalog passed; internal link check reported zero broken references. Readability's report-only check scored all 19 presentations within its existing ceiling.
- The 17 Computer Skills regressions exercise **all 140 slides at 320px and 390px**, at default and largest text sizes (560 slide states), plus keyboard menus, boundaries, Help, text controls and table scrolling. The agent also checked all slides at 1440px and inspected desktop/mobile captures.
- Financial Readiness button contrast passed light/dark mode, with and without hover.
- The assessment agent checked eight DL1 PDF combinations with bundled pypdf: short/long names, pre/post, Letter/A4. Every page contains text. The long-name fixtures each have three pages; the short pre-test A4 has two. A short post-test A4 can still use a third page for its closing line; this is not an empty page. Print optimization beyond removing blank layout space was not part of this repair.
- A three-page long-name post-test rendering was visually reviewed; all twenty question rows and report identifiers are readable. See [report rendering](site-repairs-2026-09-21/dl1-post-report.png).
- No real student records, real submissions, emails, or care-team messages were used.

Evidence: [full quality log](site-repairs-2026-09-21/quality.log), [desktop slide](site-repairs-2026-09-21/computer-skills-desktop.png), [mobile slide](site-repairs-2026-09-21/computer-skills-mobile.png).

The original review remains a dated record of the pre-fix state. Its screenshots and findings should not be mistaken for the repaired build.

## Design detector review

The modified/new Computer Skills shell has no deterministic detector findings. The financial gradient-text finding was corrected with a solid token. Existing accent borders and progress animations elsewhere in the financial stylesheet express navigation, callouts and progress; they were reviewed as inherited design patterns rather than evidence of a new functional defect. No detector exceptions or suppressions were added.

## Remaining release checks

The [updated preview](https://deploy-preview-17--vubcourse.netlify.app) contains these repairs and the exact local DL2 question-bank file (post-test version 3). The [successful deploy](https://app.netlify.com/projects/vubcourse/deploys/6ab164357026800008b625be) also passes its header and redirect checks. Hosted smoke checks confirmed Word slides fit a 390px viewport, the intake success pane resolves, and DL1 offers the explicit comparison flow. Reconnecting Netlify is only needed to inspect the earlier failure or manage the connector directly. External Google Form delivery, third-party video availability, screen-reader behavior beyond automated checks, and lab/projector/speaker/printer acceptance remain separate checks. Production remains unchanged until separately approved.
