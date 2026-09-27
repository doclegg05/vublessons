# Week 6 structure and content review (Tell, Show, Do, Review + WIPPEA + adult learning) — Claude

Scope: Digital Literacy Level 2, week 6 (bonus week) "Build a small web app with AI", class Monday 2026-11-02, 4:30–6:30 p.m. Reviewed read-only against `vublessons` `main` at 9270815 (the week 1 Tell, Show, Do, Review merge). The instructor's goal for this week is **the basics of agentic engineering a SaaS website**, delivered as an **instructor-led AI coding agent demo**. Learners have no accounts and no AI access of their own. That decision is binding, so this review judges the current week against it and then proposes the redesign.

Conventions:
- Slide numbers are as learners see them (slide 1 = title, 24 slides).
- Lesson-plan minutes come from `weeks/week-06/lesson-plan.html` (week 6 `agenda` in `scripts/dl2/author-content.py`).
- Video times are m:ss in `media/week-06.mp4` (7:31). Chapter starts: ch1 0:00, ch2 0:46, ch3 1:32, ch4 2:14, ch5 3:00, ch6 3:44, ch7 4:27, ch8 5:11, ch9 5:55, ch10 6:44.
- Prompt times come from the narration word timings (`video/digital-literacy-2/week-06/narration/beat-NN.words.json`).
- Frames were extracted at the start, middle and end of every chapter, at all 12 screen-share actions (ch6, ch7) and at the prompts, and each one was inspected. They are in `scratchpad/video-eval/w6frames-claude/`.
- I built the proposed "agent result" pages as prototypes in `scratchpad/w6proto/` and ran every checklist test on them and on the real starter in Chromium.

## Verdict

**Week 6 as written does not teach its stated goal, and its hands-on path does not work.** It teaches "vibe coding" (a learner asks an AI for a whole page) in big blocks. No AI coding agent, plan or diff appears anywhere: not on a slide, not in the video, not in the plan. The lab has no AI accounts, so the "approved AI tool" path never happens. The no-AI path then breaks itself:
- The required rename ("Community library" → "Community Skills Desk") removes the only record that contains "library". After it, the course's own "library" and "LIBRARY" checks fail, on the one skill the week exists to teach.
- The starter already passes all seven logged tests, so "fix one defect" (task 7) has nothing to fix.

**What is good and should be kept**
- A small, concrete, fictional problem (a community resource finder) and a working starter page.
- Acceptance checks written before any code (slide 6, ch4).
- Accurate security messages: browser code is visible, a sign-in picture is not security, private keys stay off the page (slides 13–15, 21; ch2, ch5, ch10).
- Two strong screen demos: ch6 (save a working version, .html not .html.txt) and ch7 (library, zzz, LIBRARY, category + search). Chapter 9 already describes exactly the defect the redesign plants ("LIBRARY returns no result, but library returns Community library").

**Problems**
- **Goal gap (High).** Nothing shows or practises the agent loop: spec → plan → agent changes → review the diff → test → revise.
- **Big blocks, not cycles.** 10–30 tells six slides of concepts. 30–50 is a build no one can do. 60–75 plays the explainer. 75–105 is a 30-minute "improve" block with nothing to improve.
- **Four SaaS topics are told only:** where data lives, API keys, authentication and hosting (slides 13, 14, 15, 19) sit in no plan phase except a line at 60–75 ("privacy checks") and 105–120 ("discuss hosting").
- **Evaluation is thin.** The 8-point rubric has no level descriptors. The answer guide has no expected test results. Slide 20's wrong answers ("Skip testing", "Add real personal records immediately") are not believable.
- **Terms are undefined:** agent, API key, authentication, hosting, happy path, external dependencies, semantic buttons, and "vibe coding" itself.

**Correctness:** 2 High, 6 Medium, 13 Low (table below). No slide teaches anything unsafe; the security content is right. The High items are the goal gap and the self-breaking rename.

**The fix.** Keep the starter page. The instructor runs an AI coding agent on the projector. Learners do the thinking: they write the spec and checks, predict the change, review the diff, test the result with a five-item checklist, write a repair request and retest. A prepared "agent result" page with one realistic, findable defect makes the lesson work whatever the live agent does. SaaS basics are taught through the same finder. Six short Tell, Show, Do, Review cycles fit in 120 minutes (running order below).

## WIPPEA map

| Stage | Where it happens | Rating | Evidence | What to change |
|:--|:--|:--|:--|:--|
| **W — Warm-up** | 0–10 "Choose the problem" | **Missing** | <ul><li>The plan starts with the new problem. Nothing recalls weeks 1–5.</li><li>Week 1 taught "Check what an automatic feature changed before you accept it" (AutoCorrect, teh → the). That is the core habit of reviewing an agent's work, and week 6 never connects them.</li><li>Week 5 taught keeping passwords private; slide 14 repeats it for API keys without saying so.</li></ul> | An 8-minute warm-up: week 5 reconnect, then "In week 1 you checked what AutoCorrect changed; today a bigger automatic helper changes a web page". Pairs discuss slide 2. |
| **I — Introduction** | Slides 1–2; ch1 0:00–0:46 (not scheduled) | **Adequate** | <ul><li>Goals are on slide 1 in writing. Slide 2 and ch1 frame one small, fictional problem.</li><li>The three goals are not measurable, and none mentions an agent or SaaS basics.</li><li>"Vibe coding" (week title summary, slide 4) is never defined.</li></ul> | ABCD objectives that match the goal; one-minute SaaS definition (slide 3); play ch1; open the starter as "version 1". |
| **P — Presentation** | 10–30 (slides 3–8), 60–75 (explainer + checks) | **Weak** | <ul><li>Six concept slides in 20 minutes, then the video as one block 30 minutes later.</li><li>The goal's core, an agent making a change you then review, is never presented. Slide 4 describes "ask AI to produce code" with no tool, plan or diff.</li><li>Slides 13–15 and 19 appear in no phase.</li><li>Undefined terms (see Content correctness row 8).</li></ul> | Teach one step of the loop per cycle, each with its slide, its video chapter and a live Show on the projector. |
| **P — Practice** | 30–50 "Build round one"; 75–105 "Improve and retest"; worksheet tasks 1–8 | **Weak** | <ul><li>"Learners use an approved AI tool or edit the supplied starter." No tool is named, and learners have no accounts.</li><li>The no-AI path (task 4) breaks the library checks (CP-04).</li><li>Task 7 has nothing to fix (CP-05): the starter passes every test.</li><li>"Pairs swap tester/builder roles", so each learner drives half the work.</li><li>Editing raw HTML and JavaScript in Notepad is a big step from Level 1.</li></ul> | Every learner does the thinking work at their own seat: spec, checks, prediction, diff review, checklist test on a prepared agent result, repair request, retest. Hand-editing becomes optional. |
| **E — Evaluation** | 105–120 "Demo and reflection"; slides 20–21; rubric; answer guide | **Weak** | <ul><li>The rubric has four criteria scored 0/1/2 but no descriptors or score lines, and the answer guide has no rubric (AS-20).</li><li>The answer guide says "All seven paths tested" with no expected results (IR-16).</li><li>Slide 20's wrong answers are throwaways (AS-11). Slide 21 is good.</li><li>Fifteen minutes for every learner's demo, the rubric and a hosting discussion.</li></ul> | A Review inside each cycle; a 10-minute individual check with three items; rubric with 0/1/2 descriptors aligned to spec, prediction and review, testing, and SaaS trade-offs; expected results in the answer guide. |
| **A — Application** | Slide 19; slides 22–24; ch10 | **Weak** | <ul><li>Slide 19 and ch10 name hosting, costs and maintenance, which is a start.</li><li>No home task and no link to services learners already use (web email is SaaS).</li><li>This is the last class, so there is no next-week follow-up.</li></ul> | Home task: pick a SaaS website you use; write where your data lives, how you sign in, and one check you would run after the company changes the site. |

**Overall flow.** The order is concepts (10–30) → build (30–50) → break → video (60–75) → improve (75–105) → demo (105–120).
- No step of the loop gets presentation → practice → check before the next starts.
- The video, the best Show, plays as one block after the build it should have modelled.
- The build and improve blocks (50 minutes together) depend on AI access the lab does not have, or on a no-AI path that has no defect to find.

## Tell, Show, Do, Review by skill

| Skill | Tell (where) | Show (where) | Do (where; minutes available) | Review (where) | Missing or weak steps |
|:--|:--|:--|:--|:--|:--|
| Website, web app, SaaS | Slide 3; ch2 0:46–1:32 | Slide 3 explorer; ch2 diagram (the word "SaaS" is on screen, "software as a service" is only spoken) | Task 8 (explain) at 105–120 | Rubric row 4 | Taught at 10–30, practised at the end. SaaS is never tied to services learners use. |
| Three parts (HTML, CSS, JavaScript) | Slide 5; ch3 1:32–2:14 | Slide 5 workshop shows `<h1>Find a resource</h1>`, which is not in the starter | Task 4 (find the `<h1>`); task 8 (explain) | Rubric row 4 | Slide code does not match the file (CP-15). ch3's prompt at 2:07 gives 1.0 s. |
| Acceptance checks | Slide 6; ch4 2:14–3:00 | ch4 table (library, zzz, Tab key); slide 6 supplement | Task 1 at 30–50 | None planned | ch4's "Pause and write three checks" ends at 2:52, next sentence at 2:54 (1.6 s). No partner check in the plan. |
| Prompt / spec | Slide 7; ch5 3:00–3:44 | Slide 7 builder; "demonstrate a bounded AI prompt" at 10–30 | Task 2 | Answer guide only | The prompt is a whole-app build request and is never sent anywhere, so learners never see a result from it. |
| Ask for a plan / explanation | Slide 8 | Slide 8 scene | None | None | Tell only. |
| AI builds the page (the week's goal) | Slide 4 | None: no tool named, no output shown | Task 5 "ask an approved AI tool…", impossible without accounts | Answer guide | Show and Do missing. No agent, plan or diff anywhere. |
| Save, edit and open a local file | Slides 9–10; ch6 3:44–4:27 | **ch6 screen demo** (save v1, "Keep .html • not .html.txt", open in browser) | Tasks 3–4 at 30–50 | Answer guide | Mac steps wrong (CP-06); heading mismatch (CP-15); rename breaks the checks (CP-04); procedures print after the tasks. |
| Review what changed (diff) | Slide 11 | Slide 11 scene says "Only the heading changes in v2", but task 4 changes a record too | Task 5 "record exactly what changed" | None | No diff view is ever taught. |
| Test edge cases | Slide 17; ch7 4:27–5:11, ch8 5:11–5:55 | **ch7 screen demo** (library → 1; zzz → no match; LIBRARY → same; Learning + LIBRARY → match; Community + LIBRARY → none); slide 17 sim; 60–75 live test | Task 6 at 75–105 | Answer guide: no expected results | The Show is strong. The slide 9/17 simulation lists records the starter does not have (CP-25). |
| Repair request and regression | Slides 12, 18; ch9 5:55–6:44 | Slide 18 "explicitly broken demonstration" (no broken file exists) | Task 7 at 75–105: nothing to fix | Answer guide | Slide 12's example (focus hard to see) cannot be reproduced: the starter has a 4px outline. ch9's prompt at 6:37 gives 1.1 s. |
| Where data lives | Slide 13; ch8 5:30–5:47 | Slide 13 scene | Task 8 (explain) | Rubric row 4 | Named in no plan phase. |
| Secrets and API keys | Slide 14; ch5 3:29–3:36 | Slide 14 scene | None | Slide 21 | "API key" is never defined. |
| Authentication (sign-in) | Slide 15; ch2 1:14–1:19; ch10 7:14 | Slide 15 scene | None | None | Tell only; the word "authentication" is only in ch2. |
| Hosting, cost and upkeep | Slide 19; ch10 6:44–7:31 | Slide 19 scene | Task 8 | 105–120 discussion | Tell, then a discussion at the end. |

**Week 6 runs as big blocks, not short cycles.** Fourteen skills are told in two blocks (10–30 and 60–75). The goal skill (directing an agent and judging its work) has no Show and no possible Do. Two practice blocks totalling 50 minutes rest on AI access the learners do not have, or on a path with no defect. For older learners who finished Level 1, that means long stretches of listening, then a Notepad task at the edge of their skills, then 30 minutes looking for a bug that does not exist.

## Objectives

Extension objective group (outside the 28-point GS6 assessment).

**1. "Describe a small app and write a bounded AI prompt."**
- **ABCD rewrite:** Given the starter page and a one-sentence need, each learner writes a plain-English change request naming the one change, who it helps and two things that must stay the same, plus three acceptance checks ("I do this, I expect that"). Degree: a partner can run every check without asking what it means.
- **Taught:** slides 6–7; ch4–5. **Practised:** tasks 1–2. **Evaluated:** answer guide only.
- **Status:** Practised, but the prompt is never used, so learners never learn whether it worked.

**2. "Explain HTML, CSS, JavaScript and browser storage."**
- **ABCD rewrite (as a prediction task):** Before the agent runs, each learner states which part of the page (HTML, CSS or JavaScript) a described change needs and one thing that could break, then compares it with the agent's plan. Degree: part named with a reason; one match or difference named.
- **Taught:** slides 5, 13; ch3, ch8. **Practised:** task 8 only (explain at the end). **Evaluated:** rubric row 4.
- **Status:** Explained but never used. Browser storage is described, but the starter uses none.

**3. "Test a prototype, revise one behavior and explain what a hosted service still needs."**
- **ABCD rewrite:** At their own workstation, each learner runs five checklist tests (happy path, no match, mixed case, keyboard, narrow screen) on the agent's version, records expected, actual and pass or fail, writes a repair request, and after the repair reruns the failed check and two that passed. Degree: all five recorded; the failure found; the retest done.
- **Taught:** slides 12, 17–19; ch7–10. **Practised:** tasks 6–7. **Evaluated:** answer guide ("all seven paths tested").
- **Status:** Testing is practised; revising is impossible (nothing fails). "What a hosted service still needs" is a separate objective and is only discussed.

**Missing for the stated goal (not stated, not taught)**
- **Review:** reading an agent's change (a diff) and finding what was not asked for.
- **SaaS basics:** hosting, sign-in (authentication), where data lives, where a private key goes, cost and who maintains it, explained with a reason.

**Backward design.** The evidence list in the plan copies the worksheet. It was not designed from the goal. Nothing the learners produce shows they can direct or judge an agent.

## Adult learning principles

| Principle | Rating | Evidence | Improvement |
|:--|:--|:--|:--|
| 1. Need to know | Adequate | <ul><li>ch1: "You do not need to become a professional programmer today… You will practice directing a build, checking what it does".</li><li>Why these learners should care about agents or SaaS is never said. They already use SaaS every day (web email, online banking, patient portals).</li></ul> | Open with: "Most websites you sign in to are SaaS, and AI agents now help build them. Knowing how to judge that work protects you and your data." |
| 2. Self-concept | Adequate | <ul><li>Fictional data; learner choice in ch1.</li><li>"Use an approved AI tool only if available" splits the room into those who can and those who cannot.</li><li>Tester/builder role swaps halve each learner's practice.</li></ul> | Everyone does the same thinking work without accounts; the instructor is the only one who needs AI access. Each learner writes their own spec. |
| 3. Experience | **Weak** | No link to week 1 (check what an automatic change did), week 2 (judge a source), or week 5 (keep passwords private). | Warm-up and Tell lines that name those weeks. |
| 4. Readiness | **Weak** | Editing JavaScript arrays in Notepad, "semantic buttons", "external dependencies". Gemini also rated this Weak. | Review and test instead of hand-editing; plain definitions of each term; hand repair optional. |
| 5. Orientation (problem-centred) | Strong | One concrete task throughout (find a resource). Slide 13 and 5 titles are subject-centred, but the bodies are task-framed. | Keep; frame SaaS slides as "What would it take to run this finder for the public?" |
| 6. Motivation | Adequate | <ul><li>Reassuring tone; a completion slide.</li><li>The no-AI path ends with nothing to fix, so the "I found and fixed it" moment never comes.</li></ul> | Planting one findable defect gives every learner the win of catching what the AI missed. |

## Content correctness

| # | Where | What it says | What is correct (source) | Severity |
|:--|:--|:--|:--|:--|
| 1 | Whole week vs the stated goal | Title "Build a small web app with AI"; summary "basic vibe coding"; slide 4 "ask AI to produce code, then inspect and test". | The goal is agentic engineering: an agent reads files, plans, edits and checks in a loop, and the person reviews each change ([Claude Code: the agentic loop](https://code.claude.com/docs/en/how-claude-code-works); [permission modes and plan mode](https://code.claude.com/docs/en/permission-modes)). No slide, chapter or task shows an agent, a plan or a diff. | **High** |
| 2 | Worksheet task 4; slides 6, 8, 10, 17; ch4, ch9 | Rename "Community library" to "Community Skills Desk", then test "library" and "LIBRARY". | After the rename no record contains "library" (the other names are Community Makers Group and Practice Workbook Workshop; no description has "library"). "library" and "LIBRARY" then return "No matching resources", so task 6's mixed-case test and task 7's regression check fail by design (CP-04, confirmed from `resource-finder.html` lines 6–10). | **High** |
| 3 | Tasks 5–7; plan 75–105 | "Fix one defect or improve one requirement." | The starter passes every logged test. Prototype run in Chromium: blank → "3 fictional resources found."; library → 1; zzz → "No matching resources. Try a different word or reset the filters."; LIBRARY → 1; Learning + library → 1; Community + library → none; 4px solid focus outline on every control; no sideways scroll at 320px. There is nothing to fix without writing new code (CP-05). | Medium |
| 4 | Worksheet procedure, step 2 | "On a Mac, open TextEdit, choose Format, then Make Plain Text, then open the file." | Apple: choose TextEdit › Settings › Open and Save and select "Display HTML files as HTML code instead of formatted text", or tick "Ignore rich text commands" when opening; when saving, click "Use .html" ([Apple](https://support.apple.com/guide/textedit/work-with-html-documents-txted0b6cd61/mac)). Make Plain Text only converts the open document; an HTML file opened afterwards shows as formatted text, and saving it replaces the code (CP-06). | Medium |
| 5 | Slides 5 and 10 | `<h1>Find a resource</h1>` → `<h1>Community resources</h1>` | The starter's heading is `<h1>Community resource finder</h1>` (`resource-finder.html` line 4; the ch6 frame at 3:44 shows the real one). Sources: `workshops.py` 'parts', `photo_scenes.py` (6,10) (CP-15). | Medium |
| 6 | Answer guide task 6 | "All seven paths tested; honest failures and expected/actual evidence recorded." | No expected results are given (IR-16). The real starter results are in row 3 above. | Medium |
| 7 | Slide 20 | Options "Run the acceptance checks yourself / Skip testing / Add real personal records immediately". | Answer is correct, but two options are throwaways that no learner would choose (AS-11), so the check shows little. | Medium |
| 8 | Slides 3, 7, 14, 15, 17; ch2, ch5, ch10 | "SaaS", "API keys", "authentication", "hosting", "happy path", "external dependencies", "semantic buttons", "vibe coding". | None is defined at first use (CP-11, VM-07). Plain definitions: SaaS is software run by a provider and used through a browser ([NIST SP 800-145](https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-145.pdf)); authentication is "verifying the identity of a user, process, or device" ([NIST glossary](https://csrc.nist.gov/glossary/term/authentication)); an API key lets an app use another service, and hardcoded keys "are open to interception or theft" ([Google Cloud](https://docs.cloud.google.com/docs/authentication/api-keys-best-practices)). | Medium |
| 9 | Slides 1, 9, 17 'app' simulation | "Computer help desk", "Neighborhood center". | The starter has Community Makers Group and Practice Workbook Workshop (CP-25). The video already uses the real records. | Low |
| 10 | Slide 11 scene | "Only the heading changes in v2." | Task 4 changes the heading and a record (CP-24). | Low |
| 11 | Worksheet task 3 | "Save a copy as resource-finder-v1.html." | The download is already named resource-finder-v1.html (`build-pages.py` line 92) (CP-24). | Low |
| 12 | Slide 12 | "The filter works with a mouse but the focus is hard to see." | The starter already draws a 4px outline (`:focus-visible{outline:4px solid #a65a00}`), so learners cannot reproduce this problem. | Low |
| 13 | `resource-finder.html` | Floating Text size button. | Confirmed again: at 320×600 the 112×82 button covers the search box (AX-07). The narrow-screen test can show a failure that is not the page's own. | Low |
| 14 | `resource-finder.html` | `<script src="/shared/text-size.js">` and a root-absolute return link. | From a downloaded `file://` copy both fail, but the page itself works; only the optional text-size widget is lost. The link text already says "(when hosted)". | Low |
| 15 | Slide 18 scene; slide 14 scene | "Find Community Library"; "Community Library / Learning Desk". | The record is "Community library"; "Learning Desk" is not in the starter. | Low |
| 16 | Worksheet rubric | Four criteria scored 0, 1 or 2; 8 points. | No level descriptors, no score lines, and no rubric in the answer guide (AS-20). | Low |
| 17 | Lesson plan "Prepare the room" | Workstation, word processor, spreadsheet, printer; "use an approved AI tool only if available". | Generic text shared by all weeks. Week 6 needs no spreadsheet or printer, and the AI tool is never named or set up (CP-18). | Low |
| 18 | Worksheet | The procedures that tasks 3–4 depend on print after all eight tasks. | Render them first or link them (CP-15). | Low |
| 19 | ch4, ch9 prompts | "Pause and write three checks…" (ends 2:52.2); "Pause and make one small improvement or repair." (ends 6:36.9). | The next sentence starts 1.6 s and 1.1 s later (word timings). The instructor must pause by hand. | Low |
| 20 | ch6, ch7 labels | "Save a distinct working version" (0.54 s); "Clear the search…" (0.94 s). | Screen-demo labels flash by (VM-06, from `screen-share-actions.json`). | Low |
| 21 | Slide 21 | "Where should a private API key go in a browser prototype?" | Correct. Worth adding one nuance to the explanation: some services issue public keys made for browser code, such as Stripe's publishable key, while private or secret keys must stay on a server ([Stripe](https://docs.stripe.com/keys)). "In a public JavaScript variable" gives the answer away. | Low |

**Totals:** High 2, Medium 6, Low 13 (rows 9–21). Nothing unsafe is taught.

**Verified as correct**
- **SaaS (slide 3; ch2):** "software operated as an ongoing online service; it may need accounts, shared storage, support and maintenance" matches NIST's definition: "use the provider's applications running on a cloud infrastructure… accessible from various client devices through… a web browser… The consumer does not manage or control the underlying cloud infrastructure" ([NIST SP 800-145](https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-145.pdf)).
- **HTML, CSS and JavaScript (slide 5; ch3):** structure, style and behavior ([MDN](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/What_is_JavaScript)).
- **Browser storage (slide 13; ch8):** tied to one origin in one browser, kept across sessions, cleared with site data or when the last private tab closes ([MDN localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)). "Not automatically a shared database or a backup" is right.
- **Browser code is visible (slides 14, 21; ch5):** Ctrl+U shows a page's source in Edge and Chrome ([Microsoft Edge shortcuts](https://support.microsoft.com/en-us/microsoft-edge/keyboard-shortcuts-in-microsoft-edge-50d3edab-30d9-c7e4-21ce-37fe2713cfad); [Chrome shortcuts](https://support.google.com/chrome/answer/157179)); keys in code "are open to interception or theft" ([Google Cloud](https://docs.cloud.google.com/docs/authentication/api-keys-best-practices)).
- **A sign-in picture is not security (slide 15; ch2, ch10):** "Developers must never rely on client-side access control checks… Access control checks must be performed server-side" ([OWASP](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)).
- **Hosting (slide 19; ch10):** a web server stores and serves a site's files; a dynamic site adds an application server and a database ([MDN](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_web_server)).
- **Acceptance checks (slide 6; ch4):** "a formal description of the behavior… generally expressed as an example… pass or fail" ([Agile Alliance](https://agilealliance.org/glossary/acceptance-testing/)).
- **Regression (ch9):** "A degradation in the quality of a component or system due to a change" ([ISTQB glossary](https://glossary.istqb.org/search/regression)); ch9's "fixing one behavior breaks another" says it plainly.
- **Notepad "All files" and the .html.txt warning (worksheet; ch6):** correct; typing the name in quotation marks also works ([Microsoft Q&A](https://learn.microsoft.com/en-us/answers/questions/3832577/html-in-notepad)).
- **The ch7 demo matches the real starter:** library 1; zzz no match; LIBRARY 1; Learning + LIBRARY 1; Community + LIBRARY none (frames 4:28–4:55 and my prototype run).
- **Knowledge checks:** both keyed answers are correct.

**Lab quick card (proposed `lab_paths`), each row checked on an official page**

| Row | Steps (short) | Source |
|:--|:--|:--|
| Put two pages side by side | Ctrl+N new window; Windows logo key + Left arrow; or hover Maximize for a layout | [Edge shortcuts](https://support.microsoft.com/en-us/microsoft-edge/keyboard-shortcuts-in-microsoft-edge-50d3edab-30d9-c7e4-21ce-37fe2713cfad) ("Ctrl+N Open a new window"); [Snap your windows](https://support.microsoft.com/en-us/windows/snap-your-windows-885a9b1e-a983-a3b1-16cd-c531795e6241) |
| See a page's code | Ctrl+U | [Edge shortcuts](https://support.microsoft.com/en-us/microsoft-edge/keyboard-shortcuts-in-microsoft-edge-50d3edab-30d9-c7e4-21ce-37fe2713cfad) ("View source"); [Chrome](https://support.google.com/chrome/answer/157179) ("non-editable HTML source code") |
| Find a word | Ctrl+F; matches highlighted; Ctrl+G next | [Edge shortcuts](https://support.microsoft.com/en-us/microsoft-edge/keyboard-shortcuts-in-microsoft-edge-50d3edab-30d9-c7e4-21ce-37fe2713cfad) ("Ctrl+G Jump to the next result"); [Chrome find](https://support.google.com/chrome/answer/95440) ("Matches are highlighted") |
| Reload a page | F5 or Ctrl+R | [Edge shortcuts](https://support.microsoft.com/en-us/microsoft-edge/keyboard-shortcuts-in-microsoft-edge-50d3edab-30d9-c7e4-21ce-37fe2713cfad) |
| Keyboard only | Tab / Shift+Tab; arrows on Category; Enter on Reset filters | [Edge shortcuts](https://support.microsoft.com/en-us/microsoft-edge/keyboard-shortcuts-in-microsoft-edge-50d3edab-30d9-c7e4-21ce-37fe2713cfad) ("Go to next tab stop"); list and button keys from [WebAIM](https://webaim.org/techniques/keyboard/) (no Microsoft or Google page covers them) |
| Narrow screen | Ctrl + to 400%; Ctrl+0 back | [Edge accessibility features](https://support.microsoft.com/en-us/accessibility/edge/accessibility-features-in-microsoft-edge); 400% zoom as the reflow test ([W3C 1.4.10](https://www.w3.org/WAI/WCAG21/Understanding/reflow.html)) |
| Show file name extensions | File Explorer › View › Show › File name extensions | [Microsoft](https://support.microsoft.com/en-us/windows/common-file-name-extensions-in-windows-da4a4430-8e76-89c5-59f7-1cdbbc75cb01) |
| Find a downloaded file | Ctrl+J; the Downloads folder | [Edge shortcuts](https://support.microsoft.com/en-us/microsoft-edge/keyboard-shortcuts-in-microsoft-edge-50d3edab-30d9-c7e4-21ce-37fe2713cfad); [Find where your browser saves downloads](https://support.microsoft.com/en-us/microsoft-edge/find-where-your-browser-is-saving-downloads-d3e83af6-68bb-aa90-3167-eeb657013902) |
| Open an HTML file in Notepad | Right-click › Open with › Notepad (or Choose another app) | [Microsoft](https://support.microsoft.com/en-us/windows/common-file-name-extensions-in-windows-da4a4430-8e76-89c5-59f7-1cdbbc75cb01) |
| Save from Notepad as .html | File › Save as; Save as type: All files; or quote the name | [Microsoft Q&A](https://learn.microsoft.com/en-us/answers/questions/3832577/html-in-notepad) (a community answer; the official [Help in Notepad](https://support.microsoft.com/en-us/windows/help-in-notepad-4d68c388-2ff2-0e7f-b706-35fb2ab88a8c) page does not cover Save as) |
| Mac hand repair (procedure, not the card) | TextEdit › Settings › Open and Save › "Display HTML files as HTML code instead of formatted text"; "Use .html" | [Apple](https://support.apple.com/guide/textedit/work-with-html-documents-txted0b6cd61/mac) |
| Agent settings (instructor notes) | `claude --permission-mode plan`; approve with "Yes, manually approve edits"; recent versions start in auto mode; Esc stops; Esc twice rewinds | [Claude Code permission modes](https://code.claude.com/docs/en/permission-modes); [How Claude Code works](https://code.claude.com/docs/en/how-claude-code-works) |

Caveats: Edge's page says Ctrl+Plus zooms "by 25%" but the real steps are uneven, so the card says "until the zoom reaches 400%". The Edge find box also shows a match count, but no official page says so, so the card only says matches are highlighted.

## Does the content make sense for this audience?

**Undefined terms at first use**
- "vibe coding" (week summary, slide 4, syllabus).
- "SaaS" (slide 3 uses it, ch2 shows it alone on screen).
- "API key" (slide 14), "authentication" (ch2 only), "hosting" (slide 19, ch10).
- "happy path" (slide 17 and ch7 titles), "external dependencies" and "semantic buttons" (slide 7), "JavaScript array" and "database" (slide 13), "`<h1>`", "source", "resources array" (task 4).
- The goal's own words (agent, spec, diff) never appear.

**Logic leaps**
- Task 2 writes a prompt for a whole new app; tasks 3–4 then edit a supplied file by hand. Gemini flagged this too: learners cannot tell whether they are building or editing.
- Slide 18 is labelled an "explicitly broken demonstration" but no broken file exists.
- Slide 12's repair (focus outline) targets a problem the starter does not have.

**Missing steps**
- How to find the `<h1>` in a 1,155-character line (line 4; no Ctrl+F step).
- How to see what changed between two versions (no diff view, no side-by-side).
- How to test a narrow screen (no zoom or resize step).

**Tasks impossible or broken as written**

| Task | Problem |
|:--|:--|
| Task 4 | The rename breaks the library checks in tasks 6 and 7. |
| Task 5 | "Ask an approved AI tool": none is set up; learners have no accounts. |
| Task 7 | "Fix one defect": the starter has none. |
| Procedure (Mac) | The TextEdit steps produce a broken file. |

**Pacing.** 30–50 asks for a first build in 20 minutes; 75–105 gives 30 minutes to fix nothing; 105–120 asks for every learner's demo, the rubric and a hosting discussion in 15 minutes.

**Earlier findings re-checked**

| Earlier finding | Status | Evidence |
|:--|:--|:--|
| CP-04 rename breaks library tests | **Confirmed** | Row 2 above. |
| CP-05 no-AI path has nothing to fix | **Confirmed** | Prototype run: the starter passes every test. |
| CP-06 Mac TextEdit steps wrong | **Confirmed** | Apple's TextEdit guide. |
| CP-15 heading mismatch; edit target hard to find | **Confirmed** | `workshops.py` 'parts'; `photo_scenes.py` (6,10); starter line 4. |
| CP-24, CP-25 redundancy and mismatched records | **Confirmed** | Slide 11 scene; 'app' workshop. |
| IR-16 no expected results | **Confirmed** | `answers[5]`. |
| AS-11 throwaway options; AS-20 rubric descriptors | **Confirmed** | Slide 20; `build-pages.py` line 92. |
| VM-07 undefined terms; VM-06 fast labels | **Confirmed** | Transcript; `screen-share-actions.json`. |
| AX-07 Text size button covers content | **Confirmed** | Covers the search box at 320×600. |

## Video structure

**Sequence.** Ten chapters of 41–48 seconds at 138–158 words a minute (`pacing-report.json`). The order follows the old build-then-test design: small scope (ch1) → website/app/SaaS (ch2) → three parts (ch3) → checks (ch4) → prompt (ch5) → open a working version (ch6) → test (ch7) → access, screen size, data (ch8) → repair and retest (ch9) → limits (ch10). Captions are on; the screen-demo chapters move them to the top.

**Which chapters still fit the agent design**

| Chapter | Fit | Use in the new plan | Notes |
|:--|:--|:--|:--|
| ch1 0:00–0:46 Build something small | Fits | Introduction | "Practice directing a build, checking what it does" suits the agent framing. |
| ch2 0:46–1:32 Website, app, service | Fits | Cycle F Show | Good SaaS picture (frame 1:00). Add the term "authentication" in a re-record. |
| ch3 1:32–2:14 Three parts | Fits | Cycle B (prediction) | Optional pause at 2:07. |
| ch4 2:14–3:00 Checks before code | Fits well | Cycle A Show; pause at **2:52** | Two-column table: check and expected result (frames 2:37, 2:52). |
| ch5 3:00–3:44 Bounded request | Partly | Cycle A Show | Models a whole-page build prompt, not a change request; no "show me your plan". Keep for the boundaries and the API-key sentence (3:29). **Re-record.** |
| ch6 3:44–4:27 Working version | Partly | Cycle C, 3:44–4:01 only | Screen demo is good (save v1, .html not .html.txt, open in browser), but 4:03–4:25 teaches the Notepad no-AI path and "the instructor-approved tool". **Re-record** as "Review the agent's change": plan, approve, diff, way back. |
| ch7 4:27–5:11 Happy path and missing result | Fits well | Cycle D Show | The strongest Show for the checklist. |
| ch8 5:11–5:55 Access, screen size, data | Fits | Cycle D Show | Keyboard, narrow window and "where the data lives". |
| ch9 5:55–6:44 Repair and retest | Fits exactly | Cycle E Show; pause at **6:37** | Its example ("LIBRARY returns no result, but library returns Community library") is the planted defect. |
| ch10 6:44–7:31 Limits | Fits | Cycle F Show | Hosting is "a separate choice"; a real service needs security and support. |

**Missing from the video:** no chapter shows an agent, a plan or a diff, which is the heart of the goal. The live demo is the Show for those steps on November 2; the re-record can add them later.

**Prompts and think time**

| Chapter | Prompt | Ends | Next sentence | Think time | Action |
|:--|:--|:--|:--|:--|:--|
| ch3 | "Open the supplied starter… identify a visible example of each part." | 2:07.0 | 2:08.0 | 1.0 s | Optional pause |
| ch4 | "Pause and write three checks for a small app idea of your own." | 2:52.2 | 2:53.9 | 1.6 s | **Pause at 2:52** |
| ch9 | "Pause and make one small improvement or repair." | 6:36.9 | 6:38.0 | 1.1 s | **Pause at 6:37** (learners write the repair request) |

**Screen demos, checked frame by frame.** ch6: five steps (editor with the real `<h1>Community resource finder</h1>` → Save dialog "resource-finder-v1.html", "File type: All files • UTF-8" → "Keep .html • not .html.txt" → browser "3 fictional resources found." → check the parts). The code is five short lines at a large size. ch7: seven states that match the starter exactly. A click ring appears on Save (frame 3:50). Text appears in one step rather than being typed.

## Redesign toward agentic engineering a SaaS website

**The idea in one sentence.** The instructor drives an AI coding agent on the projector; every learner is the person who decides what to ask for and whether to trust the result.

**What an AI coding agent is (as learners will hear it).** A program that reads the files in a project, makes a plan, edits the code and can run checks, all from a plain-English request. It works in a loop, and a person approves each step and owns the result. That is "agentic engineering" at its most basic: you direct and you judge; the agent types.

**The one change the class asks for.** The finder works, but visitors type a kind of help ("learning") rather than a name, and today that finds nothing. The class asks the agent: "Let the search box also find resources by category. Keep capital-letter matching, the no-match message and keyboard use the same. Change only this file. Show your plan first."

**The loop, one short cycle at a time**
1. **Spec** (cycle A). Learners write the request and three checks ("I type learning, I expect two resources"). One check is about something that must not break ("I type LIBRARY, I still get Community library").
2. **Plan** (cycle B). Before the agent does anything, learners predict: HTML, CSS or JavaScript? What could break? Then the agent shows its plan on the projector and the class compares.
3. **Agent changes, you review** (cycle C). The agent makes the change. The class reads the diff: lines with a minus sign were removed, lines with a plus sign were added. For each line: did we ask for this?
4. **Test** (cycle D). Every learner opens the agent's version on their own screen and runs five checks: happy path, no match, mixed case, keyboard only, narrow screen.
5. **Revise** (cycle E). Learners write a repair request: steps, expected, actual, what to keep. The agent repairs it; learners retest the failed check and two that passed before. That second part is the regression check.
6. **SaaS** (cycle F). The same finder answers "what would it take to run this for the public?": hosting, sign-in (authentication), where saved data lives, where a private API key goes, what it costs and who looks after it.

**Why a prepared "agent result".** A live agent is unpredictable: it may get the change right, do something different, or be slow. So the course ships a prepared version 2 (`activities/resource-finder-agent.html`) that shows what another run of the same request produced. It adds the feature correctly, changes a hint harmlessly, and makes one realistic mistake: while editing the search line it drops `.toLowerCase()`, so "LIBRARY" and "Learning" stop matching. Learners can catch it three ways:
- **In the Review:** slide 10's diff shows the minus/plus pair where `.toLowerCase()` disappears. Nobody asked for that.
- **In the code:** Ctrl+U, then Ctrl+F for "toLowerCase": version 1 has it in 2 places, version 2 in 1.
- **In the test:** the mixed-case check fails. Typing "Learning" exactly as it appears on screen finds nothing.

A prepared version 3 (`resource-finder-agent-fixed.html`) restores the one line so every learner can retest. If the live agent does the whole job cleanly, the instructor says so and uses the prepared version for the class's review: "Another run of the same request produced this one; that is why we review and test every time."

**What learners never need:** an account, AI access, or to edit code. Hand-repairing the line in Notepad is an optional extension for fast finishers, with corrected Windows and Mac steps.

**Terms learners get, in plain words (each on the slide where it is used)**

| Term | Plain definition | Slide |
|:--|:--|:--|
| Agent | A program that plans and makes code changes from a plain-English request, while you approve each step | 4 |
| Prompt / spec | A prompt is what you type to the agent; a spec is a careful prompt: one change, what stays the same, how you will check it | 7 |
| Acceptance check | A test anyone can run: I do this, I expect that | 6 |
| Diff | A view of exactly what changed: minus = removed, plus = added | 10 |
| Regression | Something that worked before and broke after a change | 18 |
| Hosting | Putting the page on a web server so anyone with the address can use it | 19 |
| SaaS | Software you use in a browser while a company runs it, keeps the data and updates it | 3 |
| API key | A secret code that lets your app use another company's service, which bills you | 14 |
| Authentication | Proving who you are, usually by signing in; a real service checks it on its server | 15 |

**How it fixes the earlier problems**
- No rename: the "library" checks stay true in every version (CP-04).
- The no-AI path now has a real, findable defect (CP-05).
- Mac steps follow Apple's guide (CP-06).
- Slides show the real heading and records (CP-15, CP-25).
- The answer guide lists every expected result (IR-16), and the rubric has 0/1/2 descriptors (AS-20).

**Extension rubric (8 points, 0/1/2 each)**

| Criterion | 0 | 1 | 2 |
|:--|:--|:--|:--|
| Spec and checks | No clear change or no checks | A change and checks, but a check is vague or nothing says what must stay the same | One clear change, what must stay the same, and three checks a partner can run |
| Prediction and review | No prediction and no marked diff | Predicts or marks the diff with help | Predicts the part that will change and, alone, finds the change the spec did not ask for |
| Testing and retest | Fewer than three checks run | Checks run but expected and actual not both recorded, or the failure missed | All five checks recorded with expected, actual and pass or fail; failure reported; failed check and two others retested |
| SaaS trade-offs | Cannot say what would change | Names two or three of hosting, sign-in, data, API key, cost and upkeep | Explains at least four, each with a reason |

## Recommended restructure

A 120-minute running order of six short Tell, Show, Do, Review cycles inside WIPPEA. It keeps the slide order, count and kinds. "Live" means the instructor's AI coding agent or browser on the projector.

| Minutes | WIPPEA | Tell, Show, Do, Review cycle | Slides | Video | Worksheet / check | Notes |
|:--|:--|:--|:--|:--|:--|:--|
| 0–8 | W | Reconnect (week 5 practice step); recall week 1 AutoCorrect and week 5 passwords; pairs discuss slide 2 | 2 | — | — | "A bigger automatic helper; the same rules." |
| 8–15 | I | Goals; SaaS in one minute; every learner opens version 1 | 1, 3, 9 | ch1 0:00–0:46 | — | Write the loop on the board. |
| 15–30 | P → P → E | **Cycle A, spec and checks.** Tell: slides 4, 6, 7. Show: ch4 (pause at 2:52), ch5; build the class spec on slide 7. Do: tasks 1–2, every learner. Review: partner reads each check aloud. | 4, 6, 7 | ch4, ch5 | Tasks 1, 2 | Pick one learner's checks for the demo. |
| 30–40 | P → P → E | **Cycle B, predict and plan.** Tell: slides 5, 8. Show: ch3; then the agent's plan, live, in plan mode. Do: task 3 (predict before the plan, then compare). Review: show of hands; approve the plan. | 5, 8 | ch3 | Task 3 | Plan mode keeps the agent from editing yet. |
| 40–52 | P → P → E | **Cycle C, the agent changes, you review.** Tell: slides 11, 10. Show: live change and diff; ch6 3:44–4:01. Do: task 4 on slide 10's diff. Review: partners compare; which change was not asked for? | 11, 10 | ch6 (first part) | Task 4 | Fallback: slide 10 and the prepared version 2. |
| 52–62 | — | Break | — | — | — | Screen-free. |
| 62–77 | P → P → E | **Cycle D, test.** Tell: slide 17. Show: ch7, ch8; live test of the agent's page. Do: task 5 on version 2 at each seat. Review: slide 20. | 17, 20 | ch7, ch8 | Task 5 | App test log. |
| 77–90 | P → P → E | **Cycle E, repair and retest.** Tell: slides 18, 12. Show: ch9 (pause at 6:37); a learner's repair request given to the agent; one-line diff. Do: tasks 6–7 (retest version 3). Review: partner confirms nothing that passed now fails. | 18, 12 | ch9 | Tasks 6, 7 | Regression check. |
| 90–103 | P → P → E | **Cycle F, what makes it SaaS.** Tell: slides 3, 13, 14, 15, 19. Show: ch2, ch10; Ctrl+U on the agent's page. Do: task 8. Review: slide 21; two learners explain a trade-off. | 3, 13–15, 19, 21 | ch2, ch10 | Task 8 | Slide 16 is the chapter launcher throughout. |
| 103–113 | E | **Individual check.** Each learner shows one check and its result, the change nobody asked for, and one SaaS trade-off. Score the rubric; mark the roster. | — | — | Rubric, roster | Re-model only the missing step. |
| 113–120 | A | Close and home task; Start fresh on this computer | 22, 23, 24 | — | — | Home task on a SaaS website they already use. |

Timing check: 8 + 7 + 15 + 10 + 12 + 10 + 15 + 13 + 13 + 10 + 7 = 120 minutes.

**Tight spots.** Cycle A (15) holds two chapters and two writing tasks; if it runs long, skip ch5 and show slide 7 only. Cycle F (13) has five Tell slides; teach 13 and 19 as one idea ("where it lives and who keeps it running") if short of time.

## Top 10 changes, ranked

| # | Change | Where | Why (Tell/Show/Do/Review, WIPPEA or andragogy) | Effort | Source file to edit |
|:--|:--|:--|:--|:--|:--|
| 1 | Replace the seven-row agenda with the six-cycle agent loop above, naming slides, chapters (pause at 2:52 and 6:37) and tasks, with "every learner" in each Do. | Lesson plan | Teaches the stated goal; each step gets Tell → Show → Do → Review; chunking | Medium | `author-content.py` week 6 `agenda` |
| 2 | Ship the prepared agent result (`resource-finder-agent.html`) with one planted defect, and the repaired version 3. Spec in the proposal's `other_changes`. | New activity pages | Makes Review and Test work whatever the live agent does; gives every learner a real catch (motivation) | Small | `courses/digital-literacy-2/activities/` |
| 3 | Rewrite the eight tasks and answers: spec, checks, prediction, diff review, checklist test, repair request, retest, SaaS table; remove the rename; list every expected result. | Worksheet and answer guide | Fixes CP-04, CP-05, IR-16; Do matches Show | Small | `author-content.py` week 6 `lab`, `answers` |
| 4 | Slide bodies that define the nine terms at first use and teach one loop step each; retitle the vibe-coding slides. | Slides 2–23 | Tell must be plain and accurate (CP-11, VM-07) | Small | `author-content.py` slides; titles in `other_changes` |
| 5 | Make slide 10 the diff (minus and plus lines), slide 8 the plan, and update the slide 4, 6, 11, 12, 17, 18 and 19 scenes to the new example. Fix the `<h1>` and the simulation records. | Slide scenes | Show must be the same task as the Do (CP-15, CP-24, CP-25) | Medium | `photo_scenes.py`, `scenes.py`, `workshops.py`, `workshop.js` |
| 6 | New App test log (five checks plus a retest table) and a rubric with 0/1/2 descriptors on the worksheet and the answer guide. | Worksheet; answer guide | WIPPEA Evaluation (AS-20) | Medium | `build-pages.py` line 92 |
| 7 | New procedures: open the three versions, check the change with Ctrl+U and Ctrl+F, optional hand repair with corrected Windows and Mac steps. | Worksheet | Account-free path; fixes CP-06 | Small | `author-content.py` week 6 `procedures` |
| 8 | Believable knowledge-check options: slide 20 (agent says "all checks pass"), slide 21 (hidden comment, separate script file, the server). | Slides 20, 21 | Evaluation that reveals misconceptions (AS-11); respectful tone | Small | `author-content.py` |
| 9 | Week 6 prep, quick card (10 Windows 11 rows), instructor notes, and the syllabus and guide wording for an instructor-led agent demo. Update the two tests that assert the rename. | Plan; syllabus; tests | Instructor readiness; keeps the test suite honest | Small–medium | `author-content.py` `prep`, `lab_paths`; `build-pages.py` lines 97–122; `tests/content/dl2-review-fixes.spec.js`, `tests/functional/dl2-review-fixes.spec.js` |
| 10 | Video: add a "Words in this video" box now; later re-record ch5 (change-request spec) and ch6 (review the agent's plan and diff), add spoken definitions and 3–5 s holds after the prompts. | Transcript page; video | Show quality and think time; VM-06, VM-07 | Small now / large later | `build-pages.py` transcript; `teaching-scripts/week-06.txt`, `video-scenes.py`, `screen-share-scenes.py`, then rebuild media |

Also before November 2 (small): reformat the starter's `render()` to one statement per line so the live diff is readable, and fix the Text size button overlap (AX-07) so the narrow-screen check is fair.

## Gemini claims checked

**Video review (`week-06-video-gemini-3.1-pro-preview.md`)**

| Claim | Verdict | Evidence |
|:--|:--|:--|
| Accuracy 5/5; realistic security and file-extension advice | **Agree** on the facts | See "Verified as correct". It does not notice that the video never shows an agent, which matters for the goal. |
| Pacing 2/5: nearly continuous narration | **Agree** | 138–158 words a minute in every chapter; about 1–2 s between sentences. |
| Prompts at 2:02, 2:48, 6:34 give no time | **Agree, with corrected numbers** | Gemini timed from the start of each prompt. From the end of the prompt: 1.0 s (ch3), 1.6 s (ch4, ends 2:52.2), 1.1 s (ch9, ends 6:36.9). The pause points are 2:52 and 6:37, not its tip list's "2:02, 3:00 and 6:44" (3:00 and 6:44 are chapter starts, after the prompts). |
| Audio-visual alignment 5/5, "perfect" | **Partly agree** | Labels change on the spoken phrase (`screen-share-actions.json` phrases), but two ch6/ch7 labels show for under 1 s (VM-06). |
| Code at 3:44 "too small and dense" for a projector | **Disagree** | Frame 3:44: five short lines of code shown at about the same size as the step label below the window. It is not dense. |
| No cursor highlight | **Partly disagree** | A click ring shows on Save (frame 3:50). Between clicks the cursor is a plain arrow. |
| Text appears instantly, not typed | **Agree** | The demo jumps between states. |
| Narration synthetic and flat | **Note** | This is the AI clone of the instructor's voice (week 1 review). The flatness note is fair. |
| The narrator doesn't read the result counts | **Agree** (minor) | ch7 says "compare the result" and "should find the same record", never "1 fictional resource found." |
| Relevance 5/5, "veteran-appropriate" | **Partly agree** | The finder is concrete but not veteran-specific. That is fine (veteran framing is optional). |

**Structure review (`week-06-structure-gemini-3.1-pro-preview.md`)**

| Claim | Verdict | Evidence |
|:--|:--|:--|
| The lesson "structurally fails its stated goal" | **Agree** | No agent, plan or diff anywhere (Content correctness row 1). |
| Fix: change the goal to "build and test a local prototype" | **Disagree** | The instructor's decision keeps the goal. The instructor-led agent demo teaches it without learner accounts. |
| Warm-up missing; "add the required 25-minute pre-test" | **Agree it is missing; disagree on the pre-test** | Week 6 has no pre-test: the pre-test is week 1 and the post-test week 5 (`build-pages.py` lines 119–120; syllabus). The prompt Gemini received carried a leftover "keeps the 25-minute pre-test" line from week 1. |
| Introduction "Strong" | **Partly disagree** | Goals are shown, but they are not measurable and do not mention the stated goal. |
| Evaluation "Strong": the rubric measures the objectives | **Disagree** | No descriptors, no score lines, no rubric or expected results in the answer guide (AS-20, IR-16); slide 20 has throwaway options. |
| Video timestamps "1:31 (Ch 2)", "3:16 (Ch 4)", "4:15 (Ch 5)", "5:17 (Ch 6)", "6:35 (Ch 7)", "8:44 (Ch 9)" | **Disagree** | Chapters start 0:46, 2:14, 3:00, 3:44, 4:27, 5:55; the video is 7:31, so 8:44 does not exist. |
| `/shared/text-size.js` from `file://` is a High, "broken script" | **Disagree on severity** | The page works; only the optional widget fails to load. Low. In the redesign learners use the hosted pages. |
| Notepad: quotes are "foolproof"; "All files" can still save .html.txt when extensions are hidden | **Partly agree** | "All files" saves the name as typed (earlier review verified); quotes are an alternative. The real risk is that hidden extensions hide a mistake, so the card adds "Show file name extensions". |
| Remove the Mac instructions | **Disagree** | Fix them (they are wrong, CP-06) and keep one line for learners who practise at home on a Mac. |
| Define "API key" | **Agree** | Slide 14 body now defines it. |
| Cut the tests from seven to four | **Partly agree** | Five checks, per the instructor's checklist: happy path, no match, mixed case, keyboard, narrow screen. |
| Make manual editing primary, AI optional | **Superseded** | Learners do the thinking work; the instructor runs the agent; hand repair is optional. |
| Readiness Weak: the jump to raw HTML and JavaScript | **Agree** | The redesign replaces required editing with review and testing. |
