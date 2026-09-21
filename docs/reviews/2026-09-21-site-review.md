# VUB site review — September 21, 2026

Reviewed branch `codex/digital-literacy-level-2`, commit `ff303bc` and selected live production URLs. This is an audit, not a release approval. No learner-facing source files or production services were changed.

## Verdict

The site has a coherent VUB identity, but implementation integrity needs work before calling the entire platform classroom-ready. The main risks are in the older courses: cross-student assessment comparisons, obsolete VA login instructions, and broken mobile slide layouts. DL2 passed the expanded initial-state checks; its newest post-test remains blocked from the hosted preview by a failed deployment.

Eight actionable findings: **5 P1, 3 P2, no P0 identified within the tested scope**. Fix functional and content issues before extending the visual redesign.

| Dimension | Score / 4 | Evidence |
|---|---:|---|
| Accessibility | 2 | Contrast failures on five pages; missing text-size control across eight Computer Skills presentations. |
| Performance | 3 | Static delivery, local media loaded successfully, no runtime errors in the crawl. Provisional: no throttled-network or Core Web Vitals benchmark. |
| Responsive design | 1 | Six Computer Skills presentations overflow at 390px; Word content and navigation visibly clip. |
| Theming | 2 | Shared branding is recognizable, but per-course inline styles and independent tokens create inconsistent behavior. Dark mode was not comprehensively reviewed. |
| Implementation integrity | 2 | Confirmed identity, content, redirect, and print defects despite passing routine checks. |
| **Total** | **10 / 20** | **Acceptable: significant work needed.** This is an audit rubric, not WCAG certification. |

## Coverage and boundaries

- Browser-loaded all **193 built HTML pages** at `http://localhost:3940`: no HTTP page failures, page JavaScript exceptions, failed local resource responses, or broken visible local images observed.
- Ran axe WCAG A/AA checks on **37 initial page states**, including all weekly presentations, course entries, assessment entry pages, and instructor pages. Checked the same sample at **390 × 844** for document overflow. Computer Skills assessments live in weekly folders, so their result flows were checked separately.
- Completed both older native post-tests with synthetic names, recorded results, and generated Letter-size PDF reports. Rechecked result accessibility after animations settled: neither tested results screen had axe violations.
- Manually examined representative desktop/mobile captures and DL1 PDF pages. Captures and machine evidence are in [site-review-2026-09-21](site-review-2026-09-21/).
- Current commit's existing quality gate: **82 tests passed**, build/catalog/link checks passed. This run rechecked GitHub's successful quality status; it did not rerun an unchanged suite. The new browser audit broadens coverage rather than replacing the suite.
- Compared production catalog and selected affected production pages; production advertises three courses, while the branch has four. Verified the live intake confirmation URL returns 404.
- Checked current VA sign-in guidance and one financial figure against official VA sources.
- External requests were deliberately blocked during the bulk crawl. This establishes local resource integrity, **not** third-party video/Google Form availability. No real forms were submitted, no real student data was used, and no live account was accessed.
- Not an exhaustive manual inspection of every slide, every interaction, every external link, every financial statement, screen-reader behavior, all print handouts, classroom projector/speakers, or all browser engines. Those remain release verification tasks.

## Findings

### F1 — P1: A different student inherits another student's pre-test comparison

**Locations:** `courses/digital-literacy-1/assessments/post-test.html:567`, `:744`, `:819`; `courses/computer-skills/weeks/week-08/post-test.html:1549`, `:1780`, `:1842`.

Both pages load a persistent pre-test result and use its score even after the participant name changes. Reproduction: seed a synthetic pre-test for “Learner Alpha TEST” at 20%, open the post-test, replace the name with “Learner Beta TEST,” and complete the assessment. DL1 displays Beta's 25% against Alpha's 20%, reporting +5% improvement. Computer Skills also uses Alpha's 20%. The incorrect comparison is saved and included in the printable report. This is particularly relevant to shared lab workstations. The DL1 identity-unchecked comparison condition is also present in production.

**Recommendation:** Require deliberate learner/attempt pairing and invalidate comparison on identity change. A name match alone is insufficient to distinguish people with identical names. Provide a clear new-learner/reset path and a no-comparison state. Add two-learner regression tests for screen, stored result, export, and PDF. Preserve each course's parallel category counts.

**Evidence:** [synthetic assessment results](site-review-2026-09-21/assessment-confirmation.json), [DL1 report first page](site-review-2026-09-21/dl1-print-first.png).

### F2 — P1: Computer Skills teaches a retired VA sign-in method

**Location:** `courses/computer-skills/weeks/week-01/presentation.html:882`, `:890`, `:1050`.

The lesson says existing DS Logon credentials “still work fine” and includes them in login instructions. The same statements are present on the production page. VA's current guidance says DS Logon was removed for VA sign-in on **November 18, 2025**; the supported choices are ID.me and Login.gov. My HealtheVet is now accessed through VA.gov. See [official VA sign-in guidance](https://www.va.gov/initiatives/prepare-for-vas-secure-sign-in-changes/) (updated July 7, 2026).

**Recommendation:** Update the demonstrated workflow and review the associated handouts, assessments/keys, catalog topic, and syllabus for consistency. Keep My HealtheVet as the health-service topic, but explain its current location and sign-in route. Do not imply that DS Logon is retired from every non-VA system.

### F3 — P1: Computer Skills mobile slides clip content and controls

**Locations:** `courses/computer-skills/weeks/week-04/presentation.html:22`, `:166`, `:529`; equivalent presentation layout rules in weeks 3–8.

At a 390px viewport, document widths were: week 3 **460px**, week 4 **485px**, week 5 **485px**, week 6 **434px**, week 7 **741px**, week 8 **845px**. The Word page screenshot confirms a squeezed sidebar, clipped heading, and partially off-screen Next control. Breakpoint rules change sidebar dimensions but do not fully reconcile the flex body and content sizing. This conflicts with WCAG 1.4.10 reflow for ordinary reading/navigation content.

**Recommendation:** Use one tested responsive slide shell, with a collapsible navigation drawer and a main column allowed to shrink. Recheck at 320/390px, large text, and keyboard focus. Preserve diagrams' own horizontal scrolling only when their meaning requires it.

**Evidence:** [Word presentation at 390px](site-review-2026-09-21/ics-word-mobile.png), browser scan mobile measurements.

### F4 — P1: Computer Skills omits the shared text-size control

**Location:** `courses/computer-skills/weeks/week-01/presentation.html:1301` (script-loading area); all eight weekly presentation files.

None of the eight presentations loads `shared/text-size.js`. DL1, DL2, and the other sampled learner pages do. This violates the repository's explicit learner-page requirement and prevents older learners from using the site's familiar text control in this course. Browser zoom remains available, but does not replace the required site feature.

**Recommendation:** Integrate the shared control and make the legacy slide typography respond to it. Merely adding a script while keeping fixed sizes would be incomplete. Verify slide body text against the repository's 24pt minimum, focus, navigation, and enlarged-text reflow.

### F5 — P1: The newest DL2 post-test is not available in the latest hosted preview

**Evidence:** [PR 17 checks](https://github.com/doclegg05/vublessons/pull/17/checks); [failed Netlify deployment](https://app.netlify.com/projects/vubcourse/deploys/6ab14ad45e19840008d893e6).

GitHub quality is successful for `ff303bc`, but Netlify's deployment and dependent checks report failure. The existing preview predates the distinct post-test revision. Production's catalog still contains Computer Skills, Financial Readiness, and DL1 only. This is a release blocker, not evidence that local post-test grading is broken.

**Recommendation:** Inspect the authenticated Netlify build log, resolve the actual failure, and verify the deployed question version before requesting final course approval. The failure reason remains unconfirmed; do not interpret dependent header/redirect check failures as separate proven configuration defects. Do not publish to production as part of this audit.

### F6 — P2: Instructor intake redirects to a nonexistent confirmation page

**Location:** `instructors/intake.html:494`; the existing pretty route is `/intake` in `netlify.toml:43`.

The form action is `/intake.html?success=1`. A read-only GET to that exact production path returns **404**. The success pane is implemented in `instructors/intake.html`, and no redirect covers `/intake.html`. A successful form submission may therefore leave an instructor uncertain whether it was received. Submission storage/delivery was not tested.

**Recommendation:** Point the form action to the actual hosted intake page or add an explicit legacy route. Validate success navigation separately from Netlify's receipt processing, without sending real intake data during automated tests.

### F7 — P2: Several older pages fail computed text contrast

**Locations:** `courses/computer-skills/weeks/week-02/presentation.html:293`; `courses/computer-skills/weeks/week-08/presentation.html:288`; `courses/financial-readiness/css/styles.css:421`; `instructors/intake.html:422`; `instructors/classes/index.html:262`.

Confirmed examples, normal text requiring 4.5:1 under WCAG 1.4.3:

- Computer Skills week 2 course badge: **2.68:1**; sidebar/counter text: **4.29:1** (four flagged nodes total).
- Computer Skills week 8 gold course label: **2.41:1**.
- Financial Readiness “Take Pre-Test” gold text on white: **2.41:1**.
- Intake and Classes footer metadata: **3.66:1** each.

The routine accessibility gate allows the one Financial Readiness contrast violation and does not sample all these pages. Initial scans also saw transient contrast failures during animations; those were retested after settling and excluded. Both older assessment results pages were clear on the settled rerun.

**Recommendation:** Adjust foreground tokens without changing the recognizable navy/gold identity. Expand the accessibility gate to include older lesson variants and instructor pages; tighten the existing baseline after fixing its known violation.

### F8 — P2: DL1's printable post-test adds blank trailing sheets

**Location:** `courses/digital-literacy-1/assessments/post-test.html:175`.

After using the report-generation function, Chromium's Letter PDF contains five pages: three with report content, then two with no text; the fourth page was visually confirmed as an empty pale sheet. The print stylesheet hides unrelated content with `visibility:hidden`, which retains layout space, while absolutely positioning the report. Computer Skills produced a two-page report in the same synthetic walkthrough.

**Recommendation:** Remove the non-report layout from print flow, rather than only hiding its visibility. Test short and long names, detailed answer review, both assessments, Letter/A4 output, and assert no empty trailing sheets. Check DL1's pre-test for the same pattern before applying a shared correction.

**Evidence:** [empty printed page](site-review-2026-09-21/dl1-print-blank.png).

## What is working

- All 193 local HTML pages opened; no broken visible local images or page JavaScript exceptions were observed.
- The four-course catalog and built tree pass their established checks; the existing suite has 82 passing tests.
- DL2's six lesson entry states, pre/post entry pages, and course home produced no axe violations or document overflow in this expanded initial-state sample. This does not certify every interactive state.
- Both older native post-tests accepted answers, calculated results, and produced readable report content. Their comparison identity handling needs correction.
- The financial course's stated **$163,699** pension net-worth limit agrees with VA for December 1, 2025 through November 30, 2026. [Official pension rates](https://www.va.gov/pension/veterans-pension-rates/). Other financial figures were not comprehensively revalidated.
- The design detector's accent-border, decorative-grid, glow, and em-dash warnings are stylistic advisories, not functional failures. No defect was assigned solely from those warnings. Minor progress-width transition warnings do not establish a measured performance problem.

## Repair order and verification

1. **Assessment integrity and current teaching:** F1 and F2. Validate learner pairing, accurate exports, and the actual supported VA workflow.
2. **Access and navigation:** F3, F4, F6, F7. Repair the older course shell, readable controls, and intake destination. Use Impeccable `harden` / `adapt` for focused work.
3. **Print and release:** F8 and F5. Confirm clean reports, obtain the actual deployment error, and test the updated hosted preview. Production publication remains a separate action.
4. **Visual consistency afterward:** bring older lessons toward the approved image-rich learning-app design, preserving each course's purpose. Use `polish` only after the above issues pass.

Before release, extend tests with shared-workstation identity changes, older mobile slide navigation, print page-count/content checks, and the intake confirmation route. Complete a classroom check on the lab browser, projector, speakers, and printer; exercise external videos and forms without submitting personal information.

## Reproducing the additional audit

From the repo root, build the current tree and serve `dist/site` on port 3940. Run the saved `browser-scan.cjs` and `assessment-confirmation.cjs` with Node. They use the repo's existing Playwright and axe packages and write temporary artifacts under `/tmp/vub-site-review`. The assessment script creates only synthetic browser-local records. The stored scan includes initial animation-state flags; use the settled confirmation files and findings above for adjudicated results.
