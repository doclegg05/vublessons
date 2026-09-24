# VA teaching and instructor-page repairs

Source guidance checked September 21, 2026. This repair addresses F2, F6, and the instructor footer portion of F7 in the site review.

## Current VA workflow

- Teach Login.gov and ID.me as the two supported VA sign-in providers. Describe DS Logon and the old My HealtheVet username as retired **for VA sign-in**, without claiming retirement from other systems.
- Locate My HealtheVet on VA.gov and begin benefit-letter, rating, and claims tasks at VA.gov.
- Update all three Week 1 handouts, the weekly syllabus, both syllabus overviews, the course entry/catalog, and Week 8 review references. Printable assessment and answer-key wording now says “My HealtheVet on VA.gov.” Questions still assess the same three VA concepts; categories, counts, and correct answers are unchanged.
- Correct the adjacent misleading “only .gov” rule: ID.me is a supported non-.gov provider reached through VA's sign-in flow. A browser lock does not establish trust.
- Replace classroom instructions to send a test message to a care team with an offline fictional draft. Keep personal accounts off the projector.

Primary sources:

- [VA sign-in changes](https://www.va.gov/initiatives/prepare-for-vas-secure-sign-in-changes/), updated July 7, 2026.
- [VA account creation and verification options](https://www.va.gov/resources/creating-an-account-for-vagov/), updated July 16, 2026.
- [My HealtheVet on VA.gov](https://www.va.gov/health-care/manage-health/), updated June 12, 2026.
- [VA medications tool](https://www.va.gov/health-care/manage-prescriptions-medications/), updated June 12, 2026.
- [VA secure messaging](https://www.va.gov/health-care/send-receive-messages/), updated June 12, 2026.
- [VA benefit letters](https://www.va.gov/records/download-va-letters/), updated April 16, 2026.

## Instructor pages

The intake form now returns to `/instructors/intake?success=1`, the actual page's canonical extensionless route. This also avoids the local static server dropping the query when redirecting from `.html`. The existing success pane is preserved. Footer metadata in Intake and Classes now uses opaque `#C6D0DF` against navy and passes the focused axe contrast check.

## Verification

`tests/functional/va-and-intake-repairs.spec.js` adds four checks: visible current VA sign-in content with an official reference, the real intake action resolving with its query and showing the success state, and each instructor footer passing axe color contrast. All four passed against a separate source-tree server. The intake test performs only GET navigation and explicitly checks that no POST was made. It does not claim Netlify form receipt or email delivery was tested. The parent integration run will verify the built tree and broader quality gate.
