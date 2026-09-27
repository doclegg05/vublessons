# Week 3 structure and content review (Tell, Show, Do, Review + WIPPEA + adult learning) — Claude

Scope: Digital Literacy Level 2, week 3 "Create something people can use", class Monday 2026-10-12, 4:30–6:30 p.m. (a federal holiday; the class is still scheduled). Reviewed read-only against `vublessons` `main` at 9270815, which includes the week 1 Tell, Show, Do, Review change but no week 3 content changes. The lab has Microsoft Word, Excel and PowerPoint on Windows 10; quick-card steps are written for Windows 11, and the Office steps are the same on both.

Conventions:
- Slide numbers are as learners see them (slide 1 = title, 23 slides).
- Lesson-plan minutes come from `weeks/week-03/lesson-plan.html` (generated from `scripts/dl2/author-content.py` week 3 `agenda`).
- Video times are m:ss in `media/week-03.mp4` (7:12). Chapter starts: ch1 0:00, ch2 0:39, ch3 1:19, ch4 2:04, ch5 2:43, ch6 3:31, ch7 4:14, ch8 4:57, ch9 5:39, ch10 6:23. Screen demos: ch2 and ch5 (`screen-share-actions.json`).
- Pause and answer times come from the narration word timings (`narration/beat-NN.words.json` plus each beat's start).
- 45 frames were extracted (every chapter's middle, every ch2 and ch5 screen-demo state, and narration-specific moments) and each one was inspected. They are in `scratchpad/video-eval/w3frames-claude/`. Text size was not estimated from pixels.

## Verdict

**Monday 2026-10-12 is teachable, but only with a lighter load and a different order.** Week 3 has the same shape as the old week 1: two 20-minute demonstration blocks, then two labs, then one 10-minute review. It is also overloaded. It asks older novices to use five tools (word processor, spreadsheet, presentation app, image editor, PDF export) in about 50 minutes of lab.

**Strengths**
- One realistic purpose runs through the week: a resource pack (handout, workbook, three slides) for a neighbor who needs computer help (slide 2, ch1, ch10).
- The formula lesson is sound and self-checking: 12 + 8 + 5 = 25, then 28 after paper changes to 15. This agrees on the slides, the CSV, the worksheet, the answer guide and the video.
- Good simulations: headings (slide 3), shortcuts (4), tracked change (6), live formula (1, 9, 10), chart (11), crop (13), trim and split (14), export (17).
- Two useful screen demos: ch2 (Heading 1 and the Navigation pane) and ch5 (the SUM formula).
- Accessibility habits are taught as part of the task (real headings, link text, alt text, not color alone), and all are correct.
- Week 4 opens with "Share one improvement from the resource-pack review", which is exactly the follow-up WIPPEA wants.

**Problems**
- **Big blocks, not cycles.** 10–30 demonstrates the document skills and the export; 30–50 practises them. 60–80 demonstrates the CSV, SUM, units, chart, cropping, trimming and captions, and plays the whole 7:12 video. 80–110 practises everything else. The formula is practised up to 50 minutes after it is shown, and the export 50–90 minutes after.
- **Too many tools in too little time.** Tasks 5–8 give each learner about 7.5 minutes for an Excel file, a three-slide deck with a chart or table, an image crop and a PDF export.
- **Task 7 cannot be done as written.** The "original practice image" is an SVG of abstract shapes (`assets/community-resource.svg`). Paint and Photos cannot crop it, the task names no tool, and the image has nothing to describe for alt text (task 6).
- **Task 4 has no mechanism.** "Suggest or track one partner edit" needs a shared file or account; the lab has neither. Swapping seats works, but the plan does not say so.
- **The formula Show gives away its own answer.** Ch5 says "twenty-five dollars" at 3:01 and "twenty-eight" at 3:07, then asks learners to predict at 3:22–3:25. It never says to type the equals sign or the colon, or to press Enter.
- **Evaluation is thin.** Two knowledge checks cover the formula and tracked changes only. Nothing checks each learner's headings, slides, crop or PDF. Slide 20 has a throwaway answer ("Delete their document").

**Correctness:** 1 High (task 7 image), 4 Medium, 12 Low. The Medium items:
- Slide 6 says "The reviewer accepts or rejects it", which contradicts its own scene and slide 20 (the owner decides).
- Task 4 cannot be done on separate workstations without a seat swap.
- Task 5 names no cell and no Enter, and pressing Ctrl+S keeps the CSV format, which drops the formula.
- Ch5 asks for a prediction after it has given the answer.

**For Monday:** use the five-cycle running order below.
- One app per cycle: Word, then Excel, then PowerPoint.
- Crop inside PowerPoint, using a JPG photo in place of the SVG.
- Chart and video editing become Show-only, with an oral check.
- Pause ch5 at 2:59 and type the formula live.
- Swap seats for the tracked edit.
- Save every file in one "Resource pack" folder.

## WIPPEA map

| Stage | Where it happens | Rating | Evidence | What to change |
|:--|:--|:--|:--|:--|
| **W — Warm-up** | 0–10 "Retrieve: Review last week's source trail and folder choices." No slide, no video. | **Adequate** | <ul><li>It recalls week 2, which is right, but only generally. It does not point toward today's task.</li><li>DL1 week 3 already had learners "create a short Word document… and save it with a clear file name", and demonstrated a basic presentation (`digital-literacy-1/weeks/week-03/syllabus.html`). Week 3 never says so.</li><li>No home task from week 2 is collected.</li></ul> | <ul><li>Recall DL1 (a saved Word document) and week 2 slide 11 (clear file names, one folder).</li><li>Every learner makes a "Resource pack" folder in Documents now; all files tonight go there.</li></ul> |
| **I — Introduction** | Slides 1–2 (no time slot of their own); ch1 0:00–0:39 not scheduled | **Adequate** | <ul><li>Slide 2 names the audience ("a neighbor looking for computer help"). Ch1 ties the week to "a notice, set of directions, or supply list that was easy to use".</li><li>The three objectives are not measurable. Objective 3 bundles presentation, image, video and licensing.</li><li>The plan never says which apps learners will use.</li></ul> | Read the ABCD goals aloud, say "Word, then Excel, then PowerPoint", play ch1, and have learners write task 1. |
| **P — Presentation** | 10–30 "Document model" (slides 3–7, plus export); 60–80 "Workbook and media model" (slides 8–14 and 16) plus "Play the explainer" (7:12) | **Adequate** content, **Weak** pacing | <ul><li>Several modes: photo scenes, simulations, flip cards, two screen demos, captions and transcript.</li><li>60–80 must hold 8 slides with simulations plus a 7:12 video: about 1.6 minutes per slide.</li><li>The "reviewed export" is demonstrated at 10–30, before any learner has a handout, and practised at 80–110.</li><li>No real click path appears anywhere for the lab's apps (CP-03). Examples: Styles, Track Changes, opening a CSV, the Crop button, alt text, Save as PDF.</li><li>Undefined terms: assistive technology, alternative text, CSV, "artifact".</li></ul> | Teach one app at a time. Play each chapter with its slide. Model each step live in the lab's real Office apps. |
| **P — Practice** | 30–50 "Document lab" (tasks 1–4); 80–110 "Creation lab" (tasks 5–8) | **Weak** | <ul><li>Five tools in 50 minutes.</li><li>Task 7's image cannot be cropped in Paint or Photos. Task 4 has no way to edit a partner's file.</li><li>Task 5 does not name the total cell or say "press Enter".</li><li>Task 6 asks for "a data table or labeled chart" in the slides, but moving Excel content into PowerPoint is never shown.</li><li>The plan's "Pair a driver and coach, then switch" (Facilitation) halves each learner's hands-on time.</li></ul> | <ul><li>Every learner does each task at their own seat, right after its Show.</li><li>Crop inside PowerPoint.</li><li>The chart and the video editor are Show-only.</li><li>Task 4 is done by swapping seats.</li></ul> |
| **E — Evaluation** | 110–120 "Show and explain: peer review… Use knowledge checks." Slides 19–20; answer guide; post-test items 14 and 16 | **Weak** | <ul><li>The checks cover the formula (slide 19) and tracked changes (slide 20). Nothing checks headings, slides, crop, alt text, credit or the PDF per learner.</li><li>Peer review of three artifacts plus two knowledge checks in 10 minutes cannot give an individual record.</li><li>Slide 20's "Delete their document" is not a believable mistake. Slide 19's "=SUM(A1:A2)" is weak.</li></ul> | <ul><li>Move slide 20 to cycle B and slide 19 to cycle C.</li><li>Add a 3-item individual check (Navigation pane, B5 formula, PDF opened) with a roster.</li><li>Use believable wrong answers.</li></ul> |
| **A — Application** | Slide 23; ch10 6:23–7:12 ("Carry the same routine into a household budget, a community notice…") is not scheduled; week 4 Reconnect "Share one improvement from the resource-pack review" | **Adequate** | <ul><li>Good transfer language in ch10, and week 4 follows up.</li><li>No concrete home task, and ch10's partner test ("use your resource pack without your explanation first") has no time.</li></ul> | Use ch10 for the partner test during the individual check. Home task: one real notice or a three-line SUM list, reported at week 4 Reconnect. |

**Overall flow.** The order is W → P (10–30) → Practice (30–50) → break → P (60–80) → Practice (80–110) → E and A (110–120).
- The document half is closer to cycles than week 1 was: demonstration, then lab. But four skills (structure, shortcuts, tracked change, and an export shown before it can be done) still share one block.
- The workbook-and-media half is one big block: formula, chart, slides, crop, video and licensing are all shown before any of them is tried.
- The video belongs chapter by chapter as the Show inside each cycle. It does not belong as one 7:12 block at 60–80, where ch2–ch3 (document skills) play 30 minutes after learners practised them.

## Tell, Show, Do, Review by skill

| Skill | Tell (where) | Show (where) | Do (where; minutes available) | Review (where) | Missing or weak steps |
|:--|:--|:--|:--|:--|:--|
| Audience and purpose | Slide 2; ch1 | Ch1 photo and "Purpose · A clear next action" | Task 1 at 30–50 | Peer review 110–120 | Fine. Ch1 is not scheduled. |
| Heading styles and structure | Slides 3, 7; ch2 0:39–1:19 | Slide 3 simulation; **ch2 screen demo**: select title → Heading 1 → "The title now appears in Navigation". But the Heading 1 step is on screen for 0.86 s, under a label ("Open Styles") that does not match the control ("Normal text"). 10–30 demo. | Task 2 at 30–50 | Peer review only | No Word path (Home › Styles; View › Navigation Pane). No check that each learner used styles, not bold. |
| One clear paragraph | Slide 5 | Slide 5 vague/useful comparison | Task 2 ("a short paragraph") | Peer review | Adequate. |
| Meaningful link text | Slides 7; ch2 1:05 | Ch2 final state "Read the computer-help guide" | Task 2 | Peer review | No path to insert a link (Ctrl+K). No address given, so learners must invent one. |
| Keyboard shortcuts | Slide 4 | Slide 4 simulation. Ch3 says "your instructor can show the keys for your computer" (1:30) and shows none. | Task 3 ("use copy, paste and undo") | None | No live Show; no named text to practise on. |
| Track Changes | Slide 6; ch3 1:38–1:53 | Slide 6 propose/accept/reject; ch3 diagram "Comment ≠ tracked suggestion". The Word UI is never shown. | Task 4 at 30–50: **no mechanism** on separate PCs | Slide 20 at 110–120 | Needs a seat swap and a live Show of Review › Track Changes, Accept and Reject. Slide 6 body says the *reviewer* decides. |
| Alt text and color | Slide 7; ch2 1:10; ch7 4:50 | Slide 7 image tab (definition only) | Task 6 "useful image alt text", on an abstract SVG | Peer review | No definition, no path (View Alt Text), and nothing meaningful to describe. |
| Cells, rows, columns and units | Slide 8; ch4 2:04–2:43 | Slide 8 simulation; ch4 table (which already shows "Total 25" and "=SUM(B2:B4)") | Inside task 5 | None | Fine, except ch4 reveals ch5's formula and answer early. |
| SUM formula and recalculation | Slides 9–10; ch5 2:43–3:31 | Slides 1, 9, 10 live simulations; **ch5 screen demo** (select B5 → formula → 25 → predict → 15 → 28 → check). 60–80 demo. | Task 5 at 80–110 (20–50 min after the Show) | Slide 19 at 110–120; post-test 14 | Ch5 gives both answers before asking for a prediction. Neither the video nor task 5 says to type "=" and ":" or to press Enter, or which cell to use. Saving as CSV drops the formula. |
| Chart | Slide 11; ch6 3:31–4:14 | Slide 11 simulation; ch6 static bar chart (not a screen demo) | Task 6 "a data table or labeled chart" inside slides | Peer review | No Excel steps, and no Show of moving a chart into PowerPoint. Make it Show-only. |
| Three slides and one theme | Slide 12; ch7 4:14–4:57 | Slide 12 storyboard; ch7 diagram only | Task 6 at 80–110 | Peer review | No PowerPoint Show (Blank Presentation, Design theme, New Slide). |
| Crop and resize | Slide 13; ch7 4:34 | Slide 13 simulation (on the SVG); ch7 icons | Task 7: **cannot be done as written** | Peer review | No tool named. Needs a JPG and PowerPoint's Picture Format › Crop. |
| Video editing (describe) | Slide 14; ch8 4:57–5:39 | Slide 14 trim/split simulation; ch8 diagram | Task 7 "Describe trimming, splitting and captions" | Peer review | Right level: GS6 4.1.5 is "Describe". Clipchamp needs a Microsoft account, so the slide 14 simulation is the right Do. |
| Licensing and credit | Slide 16; ch9 6:05 | Slide 16 find/check/credit | Task 7 "Record any source and license" | Peer review | Needs a real credit line on the slide. |
| File format choice | Slide 17; ch9 | Slide 17 flip cards and export simulation | Task 8 explanation | Peer review; post-test 16 | Adequate. |
| Export to PDF and inspect | Slide 18; ch9 | Slide 18 simulation; 10–30 "reviewed export" demo | Task 8 at 80–110 (50–90 min after the demo) | Peer review | No Save-as-PDF path; the Show and the Do are far apart. |
| Organize files (4.2, claimed) | Slide 18 "Verify the filename and folder" | — | No task says where to save | — | No slide carries a 4.2 ref (CP-10). |

**Week 3 runs as big blocks, not short cycles.** Fifteen skills are shown in two 20-minute blocks and practised in two labs.
- Only the formula has an in-lesson Do (the slide 9–10 simulations).
- One Do is impossible as written (crop).
- One Do has no mechanism (tracked partner edit).
- Two Dos have no Show of the real app (chart into slides; three slides with a theme).

For older learners, the cost is the same as week 1's. They hold many procedures in memory for up to 50 minutes. Mistakes appear in the lab, when the instructor can no longer re-model for everyone. Switching between five applications adds a new interface to every task.

## Objectives

GS6 Level 2 groups claimed: 4.1, 4.2, 4.3, 4.4.

**1. "Structure a document for reading and revision."**
- **ABCD rewrite:** In Word at a lab workstation, each learner:
  - types given handout lines;
  - applies Heading 1 and Heading 2 styles and a numbered list;
  - adds a link whose text names the destination;
  - confirms both headings appear in the Navigation pane.

  Degree: all correct, with at most one prompt, and no heading made with bold alone.
- **Taught:** slides 3, 5, 7; ch2.
- **Practised:** task 2.
- **Evaluated:** peer review only.
- **Status:** Taught and practised. Not checked per learner. "Revision" is really objective 2 (shortcuts and tracked changes, GS6 4.1.7–4.1.8), which is not stated.

**2. (Hidden inside objective 1) Edit safely and review.**
- **ABCD rewrite:**
  - In their own handout, each learner copies, pastes and undoes a phrase and saves the file in a named folder.
  - At a partner's seat, the learner turns on Track Changes and makes one edit.
  - Back at their own seat, the learner accepts or rejects the partner's edit and gives a reason.
- **Taught:** slides 4, 6; ch3.
- **Practised:** tasks 3–4 (task 4 has no mechanism).
- **Evaluated:** slide 20.
- **Status:** The practice depends on a seat swap the plan does not mention.

**3. "Use a formula and format a small workbook."**
- **ABCD rewrite:** Given supplies.csv in Excel, each learner:
  - types =SUM(B2:B4) in B5 and presses Enter, and confirms 25;
  - writes a prediction, then changes paper to 15 and confirms 28;
  - saves as an Excel workbook so the formula is kept.

  Degree: all steps correct, with at most one prompt.
- **Taught:** slides 8–10; ch4–5.
- **Practised:** task 5.
- **Evaluated:** slide 19; post-test 14.
- **Status:** Met, apart from the missing entry steps and the CSV save trap. "Format" is barely taught: units in the header is the only formatting.

**4. "Adapt a presentation and media for an audience and credit reused work."**
- **ABCD rewrite:** In PowerPoint, each learner:
  - builds three slides (need, steps, help) with one theme;
  - inserts the practice photo and crops it without changing the photo file;
  - adds alt text that says what the photo shows, and a credit line;
  - says in one sentence what trimming and splitting remove from a clip.
- **Taught:** slides 11–14, 16; ch6–8.
- **Practised:** tasks 6–7 (the crop cannot be done as written).
- **Evaluated:** peer review only.
- **Status:** Overloaded. It holds GS6 4.1.2, 4.1.4, 4.1.5, 4.3.1 and 4.3.2 in one objective and 15 minutes.

**5. (Taught but not stated) Export and choose a format (GS6 4.4.2, 4.2.1).**
- **ABCD rewrite:**
  - Each learner saves the handout as a PDF in the Resource pack folder and opens it from File Explorer.
  - The learner checks the headings, steps and link.
  - The learner names the format for a reader (PDF), a co-editor (Word document) and a tool that needs plain rows (CSV).
- **Taught:** slides 17–18; ch9.
- **Practised:** task 8.
- **Evaluated:** post-test 16 only.

**Backward design.** The "Evidence to collect" list copies the worksheet. It was not designed first. The two knowledge checks cover two of five outcome groups. The proposal splits the week into five outcomes, each with an individual check or a partner-verified Review, and a final 3-item performance check.

## Adult learning principles

| Principle | Rating | Evidence | Improvement |
|:--|:--|:--|:--|
| 1. Need to know | **Strong** | Slide 2 and ch1 give one concrete reader (a neighbor who needs computer help). Ch1: "A beautiful page that leaves the reader unsure is unfinished." | Keep. Name the neighbor again at the start of each cycle. |
| 2. Self-concept | Adequate | <ul><li>Slide 6 "The owner decides what stays" respects authorship, and the data is fictional and low-risk.</li><li>"Delete their document" (slide 20) reads as talking down.</li><li>Driver/coach switching halves hands-on time.</li><li>Five apps with no written steps can feel like a test of memory rather than a supported task.</li></ul> | Believable wrong answers. Every learner drives their own seat. Give a quick card so learners can work at their own pace. |
| 3. Experience | **Weak** | DL1 week 3 already covered making and saving a Word document, file naming, Save as PDF from the print screen, and Creative Commons (week 2). Week 3 does not build on any of it or ask what learners already do. | Warm-up recall of DL1 and week 2. Ask "Who has made a flyer or a budget before? What went wrong?" before cycles A and C. |
| 4. Readiness | **Strong** | Handouts, a household or club budget, a short slide show and a PDF to send are things these learners meet now. Ch10 names "a household budget, a community notice". | Home task on a real notice or list. |
| 5. Orientation (problem-centred) | **Strong** | The whole week builds one resource pack. Slide 10 "Check the formula, not just the appearance" is problem-framed. | Keep. Present each cycle as the next part of the pack. |
| 6. Motivation | Adequate | Visible results (a total that updates, a finished PDF) are strong motivators, but they arrive at the end of long labs. Five apps in 50 minutes risks frustration. | A quick "it worked" Review after every cycle. Cut the app load. |

## Content correctness

| # | Where | What it says | What is correct (source) | Severity |
|:--|:--|:--|:--|:--|
| 1 | Worksheet task 7 and the "Original practice image" button (`build-pages.py` line 91); slide 13 crop scene (`scenes.py` `crop()`); task 6 alt text | "Crop a copy of the supplied original image" → `assets/community-resource.svg`. Slide 13 alt text: "Original practice artwork: community resource information". | <ul><li>The file is an SVG of rectangles, lines and a circle, and has no information to describe (read in full).</li><li>Paint opens and saves PNG, JPEG, BMP and GIF ([Microsoft Paint](https://www.microsoft.com/en-us/windows/paint)); SVG is not among them.</li><li>The task names no tool, so a learner's first try (Photos or Paint) fails.</li><li>The alt-text part of task 6 has nothing meaningful to describe.</li><li>Office crops pictures with Picture Format › Crop ([Microsoft](https://support.microsoft.com/en-us/office/crop-a-picture-in-office-14d69647-bc93-4f06-9528-df95103aa1e6)).</li><li>Fix: a JPG made from `assets/photos/resource-pack.webp` (the photo slide 12 already uses for "slide 1"), cropped in PowerPoint.</li></ul> | **High** |
| 2 | Slide 6 body | "Turn on Track Changes or Suggesting in your editor. Make one edit. The reviewer accepts or rejects it." | <ul><li>Word: Review › Tracking › Track Changes; Review › Accept or Reject ([Microsoft](https://support.microsoft.com/en-us/office/track-changes-in-word-197ba630-0f5f-4a8e-9a77-3712475e806a)).</li><li>The person who makes the tracked edit is the reviewer; the document's owner decides.</li><li>The slide's own scene ("The owner decides what stays") and slide 20 ("You want the owner to decide") say so, so the body contradicts both.</li><li>No path is given.</li></ul> | Medium |
| 3 | Worksheet task 4; plan 30–50 "partners suggest and review one edit" | "Suggest or track one partner edit, then accept or reject it with a reason." | <ul><li>Learners work on separate lab PCs with no shared account or file, so a partner cannot edit the learner's document.</li><li>Account-free fix: swap seats, turn on Track Changes, edit, swap back, and the owner accepts or rejects. Gemini found this too.</li></ul> | Medium |
| 4 | Worksheet task 5; slide 9; ch5 2:43–2:53 | "Open supplies.csv in a spreadsheet. Add =SUM(B2:B4)…". Ch5: "enter equals SUM, followed by the range B2 through B4 in parentheses." | <ul><li>SUM syntax and the colon range are correct ([Microsoft](https://support.microsoft.com/en-us/office/sum-function-043e1c7d-7726-4e80-8f32-07b23e057f89)).</li><li>But neither the task nor the video names the cell (B5), says to type the = sign or the colon, or says to press Enter.</li><li>A learner who then presses Ctrl+S keeps the CSV format. CSV "saves only the text and values as they are displayed" ([Microsoft](https://support.microsoft.com/en-us/office/excel-formatting-and-features-that-are-not-transferred-to-other-file-formats-8fdd91a3-792e-4aef-a5bb-46f603d0e585)), so the formula is lost. That is the very lesson of slide 17.</li><li>Save as Excel Workbook (.xlsx) ([Microsoft](https://support.microsoft.com/en-US/Excel/save-a-workbook-in-another-file-format)).</li><li>Slide 9 also says "Enter Paper: 12, Folders: 8, Pens: 5", but supplies.csv already contains them.</li></ul> | Medium |
| 5 | Video ch5 2:59–3:25 | "The expected total is twenty-five dollars" (3:00–3:02), "…should become twenty-eight" (3:06–3:08), then "Pause and predict the result before changing a value" (3:22.3–3:25.2). | <ul><li>The prediction is requested 14 s after the answer.</li><li>The on-screen "Predict: 12 → 15, Total = ?" card shows for 0.76 s (3:02.6–3:03.4; frame 3:02.9).</li><li>Slides 1 and 10 model the right order (predict, then change).</li><li>Monday fix: pause at 2:59 (frame 2:59 shows the formula entered and B5 still empty).</li></ul> | Medium |
| 6 | Slide 7; task 6 | "Add useful alternative text to informative images." | <ul><li>"Alternative text" is never defined, and where to add it is not shown.</li><li>Microsoft 365: right-click › View Alt Text, or Picture Format › Alt Text. One or two sentences; "Mark as decorative" for decoration ([Microsoft](https://support.microsoft.com/en-us/office/add-alternative-text-to-a-shape-picture-chart-smartart-graphic-or-other-object-44989b2a-903c-4d9a-b742-6a75b451c669)).</li></ul> | Low |
| 7 | Slide 13 | "Crop removes outer areas. Resize changes dimensions. Save a copy before editing. Do not stretch an image…" | <ul><li>Definitions are right.</li><li>In Office, "cropped parts of the picture are not removed from the file" until Compress Pictures › Delete cropped areas ([Microsoft](https://support.microsoft.com/en-us/office/crop-a-picture-in-office-14d69647-bc93-4f06-9528-df95103aa1e6)). The picture file on disk never changes, so the original is safe.</li><li>To avoid stretching, "press and hold Shift while you drag a corner sizing handle" ([Microsoft](https://support.microsoft.com/en-us/office/change-the-size-of-a-picture-shape-text-box-or-wordart-98929cf6-8eab-4d20-87e9-95f2d33c1dde)).</li><li>The slide says what, not how.</li></ul> | Low |
| 8 | Slide 3; ch2 0:50 | "Bold alone does not create a heading for assistive technology." | <ul><li>Correct ([Microsoft](https://support.microsoft.com/en-us/accessibility/word/make-your-word-documents-accessible-to-people-with-disabilities)). But "assistive technology" is undefined (CP-11).</li><li>The Word path is missing: Home › Styles gallery ([Microsoft](https://support.microsoft.com/en-us/office/add-a-heading-in-a-word-document-3eb8b917-56dc-4a17-891a-a026b2c790f2)); View › Navigation Pane or Ctrl+F ([Microsoft](https://support.microsoft.com/en-us/word/use-the-navigation-pane-in-word)).</li></ul> | Low |
| 9 | Video ch2 0:43.5 | Step label "Open Styles → choose Heading 1". The control clicked reads "Normal text ▾" (a drop-down like Google Docs'), for 0.86 s (frames 0:43.9, 0:42.9). | Word's heading styles are in the Home tab's Styles gallery ([Microsoft](https://support.microsoft.com/en-us/office/add-a-heading-in-a-word-document-3eb8b917-56dc-4a17-891a-a026b2c790f2)). The label and the control disagree, and the key step is too brief to follow (VM-06). | Low |
| 10 | Video ch4 2:04–2:43 | The table visual shows "Total 25" and "=SUM(B2:B4)" (frames 2:10, 2:38). The narration covers cell addresses and units only. | It reveals the next chapter's formula and answer before ch5 teaches them. | Low |
| 11 | Video ch5 | A stray "Supplies" label sits beside row 5 ("Supplies 5") | Confirmed in frames 2:45–3:16 (VM-12; `screen-share-scenes.py` line 189). | Low |
| 12 | Slide 18 | "The export is a separate artifact to test." | "Artifact" is undefined jargon (CP-11). Say "The PDF is a separate file; test it on its own." | Low |
| 13 | Slides 19–20 | Options "=SUM(A1:A2)"; "Delete their document", "Make a screenshot" | The keys are correct. The distractors are not believable mistakes (CP-08). Use "=SUM(B2,B4)" and "SUM(B2:B4)" (no equals sign), and "Type over the step" and "Email a changed copy". | Low |
| 14 | Week 3 `refs`; `sources.html` | Claims GS6 4.2; no week 3 slide carries 4.2 | Confirmed (CP-10). Saving every file into one named folder practises 4.2.1; add 4.2 to slide 18. | Low |
| 15 | Lesson plan "Prepare the room" | "a word processor and spreadsheet app… instructor-provided fictional accounts or a modeled demonstration for cloud tasks" | Week 3 needs PowerPoint, a picture file and a PDF viewer, and has no cloud task (CP-17, IR-07). | Low |
| 16 | Video ch9 5:39–6:23 | On-screen note "CSV · Inspect values; record image credit" (frame 6:15) | Two unrelated ideas under the CSV icon. The narration covers credit after the formats. | Low |
| 17 | Slide 4 | "On a Mac, use Command." | Correct, but it is a side note in a Windows lab. Reword to "On a Mac at home, use Command instead of Ctrl." | Low |

**Totals:** High 1, Medium 4, Low 12. No slide teaches something that would harm a learner.

**Verified as correct**
- **Headings, link text, alt text and color** (slides 3, 5, 7; ch2): use built-in heading styles; links should "convey clear and accurate information about the destination"; describe informative images; don't rely on color alone ([Microsoft](https://support.microsoft.com/en-us/accessibility/word/make-your-word-documents-accessible-to-people-with-disabilities)). Headings appear in the Navigation pane ([Microsoft](https://support.microsoft.com/en-us/word/use-the-navigation-pane-in-word)).
- **Shortcuts** (slide 4): Ctrl+C, Ctrl+V, Ctrl+Z and Ctrl+S; also Ctrl+K (link), Ctrl+Shift+E (Track Changes), Ctrl+F (Navigation pane) and Ctrl+Alt+1 (Heading 1) ([Microsoft](https://support.microsoft.com/en-us/office/keyboard-shortcuts-in-word-95ef89dd-7142-4b50-afb2-f762f663ceb2)).
- **Comments versus tracked changes** (ch3; slide 6 scene): a tracked edit is a proposal the owner accepts or rejects ([Microsoft](https://support.microsoft.com/en-us/office/track-changes-in-word-197ba630-0f5f-4a8e-9a77-3712475e806a)).
- **Cell addresses and SUM** (slides 8–10; ch4–5): B2 = column B, row 2; =SUM(B2:B4), where the colon means a continuous range ([Microsoft](https://support.microsoft.com/en-us/office/sum-function-043e1c7d-7726-4e80-8f32-07b23e057f89)). `supplies.csv` is `Item,Cost / Paper,12 / Folders,8 / Pens,5`, so 12 + 8 + 5 = 25 and 15 + 8 + 5 = 28. A typed total does not recalculate (slide 10).
- **Chart** (slide 11; ch6): a bar or column chart compares costs; Insert › Recommended Charts; add a title ([Microsoft](https://support.microsoft.com/en-us/office/create-a-chart-from-start-to-finish-0baf399e-dd61-4e18-8a73-b3fd5d5680c2)).
- **Themes** (slide 12): Design tab › theme; Home › New Slide ([Microsoft](https://support.microsoft.com/en-US/PowerPoint/create-a-presentation-in-four-simple-steps-in-powerpoint)).
- **Crop versus resize** (slide 13; ch7): see row 7.
- **Video editing** (slide 14; ch8): trim shortens a clip from its ends; split cuts a clip in two so a part can be deleted ([Clipchamp trim](https://support.microsoft.com/en-us/clipchamp/how-to-trim-videos-images-or-audio-assets), [Clipchamp split](https://support.microsoft.com/en-us/clipchamp/how-to-split-or-cut-videos-and-audio-assets)). Clipchamp, the Windows video editor, requires a Microsoft account ([Microsoft](https://support.microsoft.com/en-us/topic/how-to-connect-clipchamp-with-your-personal-or-family-microsoft-account-fbaf526a-809d-4a1f-aad9-64a72cf35a50)). That confirms "describe on the slide 14 simulation" is the right Do for a lab without accounts.
- **Licensing and credit** (slide 16; ch9): visible in search is not permission; credit title, creator, source and license, which matches Creative Commons' TASL ([Creative Commons](https://wiki.creativecommons.org/wiki/Recommended_practices_for_attribution)).
- **Formats** (slide 17; ch9): an editable document supports revision; PDF keeps the layout ([Microsoft](https://support.microsoft.com/en-us/office/save-or-convert-to-pdf-or-xps-in-office-desktop-apps-d85416c5-7d77-4fd6-a216-6f4bf7c7c110)); CSV keeps values and loses formatting and formulas (row 4 source).
- **Knowledge checks:** the answers to slides 19 and 20 are correct.

### Lab quick card: sources for each row (proposal `lab_paths`)

| Row | Verified on |
|:--|:--|
| Make the Resource pack folder | "Select New > Folder. Type the name… press Enter" ([Microsoft](https://support.microsoft.com/en-us/office/create-a-new-folder-cbbfb6f5-59dd-4e5d-95f6-a12577952e17)). On Windows 10 File Explorer the button is Home › New folder; say so aloud in the lab. |
| Save a file into Resource pack | File › Save As, then "Browse to choose the location on your computer" ([Microsoft](https://support.microsoft.com/en-us/office/save-or-convert-to-pdf-or-xps-in-office-desktop-apps-d85416c5-7d77-4fd6-a216-6f4bf7c7c110); [Microsoft](https://support.microsoft.com/en-US/Excel/save-a-workbook-in-another-file-format)); Ctrl+S ([Microsoft](https://support.microsoft.com/en-us/office/keyboard-shortcuts-in-word-95ef89dd-7142-4b50-afb2-f762f663ceb2)) |
| Apply a heading and check it | Home › Styles gallery ([Microsoft](https://support.microsoft.com/en-us/office/add-a-heading-in-a-word-document-3eb8b917-56dc-4a17-891a-a026b2c790f2)); View › Navigation Pane or Ctrl+F, Headings ([Microsoft](https://support.microsoft.com/en-us/word/use-the-navigation-pane-in-word)) |
| Make a numbered list | "Go to Home > Numbering" ([Microsoft](https://support.microsoft.com/en-us/office/create-a-bulleted-or-numbered-list-9ff81241-58a8-4d88-8d8c-acab3006a23e)) |
| Add a link | Insert › Link, Address box ([Microsoft](https://support.microsoft.com/en-us/office/create-or-edit-a-hyperlink-5d8c0804-f998-4143-86b1-1199735e07bf)); Ctrl+K ([Microsoft](https://support.microsoft.com/en-us/office/keyboard-shortcuts-in-word-95ef89dd-7142-4b50-afb2-f762f663ceb2)). `example.org` is a reserved practice address. |
| Copy, paste and undo | Ctrl+C, Ctrl+V, Ctrl+Z ([Microsoft](https://support.microsoft.com/en-us/office/keyboard-shortcuts-in-word-95ef89dd-7142-4b50-afb2-f762f663ceb2)) |
| Track a change, then decide | Review › Tracking › Track Changes; Review › Accept or Reject ([Microsoft](https://support.microsoft.com/en-us/office/track-changes-in-word-197ba630-0f5f-4a8e-9a77-3712475e806a)); Ctrl+Shift+E ([Microsoft](https://support.microsoft.com/en-us/office/keyboard-shortcuts-in-word-95ef89dd-7142-4b50-afb2-f762f663ceb2)) |
| Open supplies.csv in Excel | Edge Ctrl+J "Open Downloads" ([Microsoft](https://support.microsoft.com/en-us/microsoft-edge/keyboard-shortcuts-in-microsoft-edge-50d3edab-30d9-c7e4-21ce-37fe2713cfad)). Excel File › Open, Text Files, and the CSV "displays the data in a new workbook" ([Microsoft](https://support.microsoft.com/en-us/office/import-or-export-text-txt-or-csv-files-5250ac4c-663c-47ce-937b-339e391393ba)). The "Open file" link in Edge's downloads list is from the product, not quoted on that page. |
| Add a total with SUM | =SUM(A2:A10) form and the colon range ([Microsoft](https://support.microsoft.com/en-us/office/sum-function-043e1c7d-7726-4e80-8f32-07b23e057f89)). Press Enter is standard Excel entry; the page does not spell it out. |
| Keep the formula when you save | Save as type, Excel Workbook .xlsx ([Microsoft](https://support.microsoft.com/en-US/Excel/save-a-workbook-in-another-file-format)); CSV keeps displayed values ([Microsoft](https://support.microsoft.com/en-us/office/excel-formatting-and-features-that-are-not-transferred-to-other-file-formats-8fdd91a3-792e-4aef-a5bb-46f603d0e585)) |
| Start slides with one theme | New › Blank Presentation ([Microsoft](https://support.microsoft.com/en-us/office/create-a-presentation-in-powerpoint-422250f8-5721-4cea-92cc-202fa7b89617)); Design tab theme; Home › New Slide ([Microsoft](https://support.microsoft.com/en-US/PowerPoint/create-a-presentation-in-four-simple-steps-in-powerpoint)) |
| Insert and crop a picture | Insert › Pictures › This Device ([Microsoft](https://support.microsoft.com/en-us/office/insert-a-picture-in-powerpoint-5f7368d2-ee94-4b94-a6f2-a663646a07e1)); Picture Format › Crop, drag handles, Esc ([Microsoft](https://support.microsoft.com/en-us/office/crop-a-picture-in-office-14d69647-bc93-4f06-9528-df95103aa1e6)) |
| Add alt text | Right-click › View Alt Text, or Picture Format › Alt Text ([Microsoft](https://support.microsoft.com/en-us/office/add-alternative-text-to-a-shape-picture-chart-smartart-graphic-or-other-object-44989b2a-903c-4d9a-b742-6a75b451c669)) |
| Save the handout as a PDF | File › Save As or Save a Copy › Browse › PDF › Save ([Microsoft](https://support.microsoft.com/en-us/office/save-or-convert-to-pdf-or-xps-in-office-desktop-apps-d85416c5-7d77-4fd6-a216-6f4bf7c7c110)) |

## Does the content make sense for this audience?

**Undefined terms at first use**
- "assistive technology" (slide 3).
- "alternative text" (slide 7).
- "CSV": used in task 5 before slide 17 describes it, and never expanded ("comma-separated values").
- "artifact" (slide 18).
- "range" is explained well in ch5 ("the colon means include the cells from the first address through the last"), but the slides never say it.

**Logic leaps**
- Slide 9 tells learners to type the values, while task 5 opens a CSV that already has them.
- Task 6 asks for "a data table or labeled chart" in the slides, but getting Excel content into PowerPoint is never taught.
- Ch4 shows the formula and total before ch5 builds them.
- Ch5 asks for a prediction after giving the answer.

**Missing steps**
- No real path appears for any of the lab's apps: Styles, Numbering, Navigation pane, link, Track Changes, Accept and Reject, opening a CSV, Enter, saving as .xlsx, Recommended Charts, theme, New Slide, Insert Picture, Crop, alt text, Save as PDF.
- Nothing says where to save.
- Ch3 defers to the instructor ("your instructor can show the keys for your computer").

**Tasks impossible or unreliable as written**

| Task | Problem |
|:--|:--|
| Task 7 | The SVG cannot be cropped in Paint or Photos, and no tool is named. |
| Task 6 | Alt text for an abstract image has nothing to say. The chart or table requirement has no Show. |
| Task 4 | No way to edit a partner's document on separate PCs without swapping seats. |
| Task 5 | No target cell or Enter. Ctrl+S keeps the CSV format and silently drops the formula. |
| Task 2 | "A meaningful link" with no address supplied; learners must invent a URL. |

**Pacing is unrealistic in three places**
- 60–80: CSV, SUM, units, chart, crop, trim, captions and the 7:12 video in 20 minutes.
- 80–110: tasks 5–8 across Excel, PowerPoint, an image tool and a PDF export, about 7.5 minutes each for older novices, with a mid-lab role swap.
- 110–120: peer review of three artifacts per learner plus two knowledge checks.

**Earlier findings re-checked**

| Earlier finding | Status | Evidence |
|:--|:--|:--|
| CP-07: week 3 agenda not realistic | **Confirmed** | Five tools in 50 minutes of lab; 8 slides plus the video in 20 minutes. |
| CP-14 / CP-27: SVG image can't be cropped; nothing to describe | **Confirmed** | File read in full; Paint formats per Microsoft. |
| CP-03: no click paths | **Confirmed** for week 3 | See "Missing steps". |
| CP-11: jargon | **Confirmed** | assistive technology, alternative text, CSV, artifact. |
| CP-10: 4.2 claimed without a slide ref | **Confirmed** | `curriculum.json` week 3 slide refs contain no 4.2. |
| CP-08: throwaway distractors | **Confirmed** for slide 20; slide 19 has one weak option | See correctness row 13. |
| CP-17 / IR-07: missing apps in prep | **Confirmed** | No presentation app, image tool or PDF viewer listed. |
| VM-01: prompts leave no time | **Confirmed** | Ch3 1:57.7 (0.48 s of silence), ch5 3:25.2 (0.82 s, after the answer), ch10 6:28.2 (1.08 s). |
| VM-03: ch5 answer before prompt; entry steps missing | **Confirmed**, and worse | Ch4 also shows "Total 25" and the formula early. |
| VM-06: Heading 1 step 0.86 s; label vs "Normal text" | **Confirmed** | Frames 0:42.9, 0:43.9. |
| VM-12: stray "Supplies" label | **Confirmed** | Frames 2:45–3:16. |
| AS-08: post-14 repeats slide 10 | Noted, not re-checked | Listed in `other_changes` for before week 5. |

**New in this review**
- Slide 6 says "the reviewer" decides, contradicting its own scene and slide 20.
- Task 5's Ctrl+S keeps CSV and drops the formula. This also affects week 5, whose challenge reopens "supplies.csv from week 3".
- Task 4 needs a seat swap.
- Ch4 reveals the formula early.
- The ch9 caption mixes CSV and credit.
- Clipchamp requires an account, which confirms slide 14 as the Do.
- The generated plan still says "Pair a driver and coach, then switch" in every week (`build-pages.py` facilitation text).
- Gemini's structure review added a 25-minute pre-test that week 3 does not have (see "Gemini claims checked").

## Video structure

**Sequence.** The 10 chapters (37–47 s each) follow the resource pack in a sensible order: purpose (ch1) → document structure (ch2) → editing and review (ch3) → cells (ch4) → formula (ch5) → chart (ch6) → slides and images (ch7) → video edits (ch8) → formats and licensing (ch9) → partner test (ch10). Opening and closing on the reader gives a coherent frame. Captions are a separate VTT track; the earlier review found 0 word differences from the script.

**Model → prompt → answer, chapter by chapter**

| Chapter | Model | Prompt and answer | Rating |
|:--|:--|:--|:--|
| ch2 (0:39–1:19) | **Screen demo**, 5 steps: structure → select title → Heading 1 → "The title now appears in Navigation" → link text (frames 0:40–1:06). | No prompt. | Strong content, but the key step lasts 0.86 s and its label does not match the control. |
| ch5 (2:43–3:31) | **Screen demo**, 7 steps: select B5 → =SUM(B2:B4) → 25 → Predict → 15 → 28 → check (frames 2:45–3:16). | "Pause and predict" at 3:22–3:25 comes **after** "twenty-five" (3:01) and "twenty-eight" (3:07). The Predict card shows for 0.76 s. Never says type "=", ":" or press Enter. | Good model, broken prompt |
| ch3 (1:19–2:04) | Diagram: select, preserve, "Comment ≠ tracked suggestion". No keys, no Word UI. | "Pause and propose one specific improvement…" ends 1:57.7, then 0.48 s of silence. | Good question, no think time |
| ch10 (6:23–7:12) | Recap photo; handout, workbook (28) and slides. | "Pause and ask a partner to use your resource pack…" ends 6:28.2, then 1.08 s. | Good transfer prompt |
| ch4 | Table diagram, but it already shows "Total 25" and "=SUM(B2:B4)". | — | Tell; spoils ch5 |
| ch1, ch6, ch7, ch8, ch9 | Photo, static bar chart, icon diagrams (crop/resize, trim/split, DOCX/PDF/CSV). | ch9 note "CSV · Inspect values; record image credit". | Tell only. They model the idea, not the task. |

**Coverage gaps.** No chapter shows Word's Track Changes, Excel's chart tools, PowerPoint at all, a crop tool, the alt-text pane, or a Save-as-PDF dialog. Those are exactly the Shows the instructor must do live.

**Where it should play.** Play it chapter by chapter as the Show inside each cycle:

| Cycle | Chapters | Pause |
|:--|:--|:--|
| Introduction | ch1 | — |
| A (handout) | ch2 | — |
| B (edit and review) | ch3 | 1:58 |
| C (formula) | ch4 and ch5 | 2:59 (predict); stop at 3:12; skip 3:25 |
| C (chart, Show only) | ch6 | — |
| D (slides and picture) | ch7 | — |
| E (video edits and export) | ch8, ch9 | — |
| Individual check | ch10 | 6:28 |

Slide 15 stays as the chapter launcher.

## Recommended restructure

A 120-minute running order built from five short Tell, Show, Do, Review cycles inside the WIPPEA stages. It uses only current slides, chapters and worksheet tasks (rewritten in the proposal). "Live" means the instructor demonstrates on the projector in the lab's real Office apps. Week 3 has no pre-test.

| Minutes | WIPPEA | Cycle | Slides | Video | Worksheet / check | Notes |
|:--|:--|:--|:--|:--|:--|:--|
| 0–10 | W | **Reconnect.** Collect the week 2 home task. Recall DL1 (a saved Word document) and week 2 slide 11 (file names, one folder). Every learner makes Documents › Resource pack. | 21 (open worksheet) | — | — | Say the lab is Windows 10: New folder is on the Home tab. |
| 10–15 | I | Goals and audience | 1, 2 | ch1 | Task 1 | "Word, then Excel, then PowerPoint." |
| 15–31 | P → P → E | **Cycle A, handout structure.** Tell: slides 3, 5, 7. Show: ch2 and live Home › Styles, Numbering, View › Navigation Pane. Do: task 2, every learner. Review: partner checks the Navigation pane. | 3, 5, 7 | ch2 | Task 2 | Re-model for anyone using bold. |
| 31–44 | P → P → E | **Cycle B, edit and review.** Tell: slides 4, 6. Show: ch3 (**pause at 1:58**) and live Ctrl+K, Ctrl+C/V/Z, Save As into Resource pack, Track Changes, Accept/Reject. Do: task 3, then task 4 by swapping seats. Review: slide 20. | 4, 6, 20 | ch3 | Tasks 3, 4 | The owner always decides. |
| 44–54 | — | Break | — | — | — | Screen-free. |
| 54–73 | P → P → E | **Cycle C, a total that recalculates.** Tell: slides 8–10. Show: ch4, ch5 (**pause at 2:59**, write two predictions; play to 3:12; skip 3:25), then type the formula live, saying each key. Do: task 5, saved as .xlsx. Review: slide 19; partner reads the formula bar. Tell/Show only: slide 11, ch6, Insert › Recommended Charts. | 8, 9, 10, 19, 11 | ch4, ch5, ch6 | Task 5 | Chart is optional for fast finishers. |
| 73–90 | P → P → E | **Cycle D, slides and a picture.** Tell: slides 12, 13, 16. Show: ch7 and live Blank Presentation, Design theme, New Slide, Insert › Pictures, Crop, View Alt Text. Do: tasks 6 and 7 with the JPG. Review: partner reads the alt text aloud without looking and checks the credit. | 12, 13, 16 | ch7 | Tasks 6, 7 | Cut slides 2–3 of task 6 first if late. |
| 90–102 | P → P → E | **Cycle E, video edits and export.** Tell/Show: slide 14 and ch8; each learner tries Trim and Remove a middle section and says what each removes. Tell: slides 17, 18. Show: ch9 and live Save a Copy › PDF, opened from File Explorer. Do: task 8. Review: oral format choice. | 14, 17, 18 | ch8, ch9 | Task 8 | No account needed. |
| 102–112 | E | **Individual check.** Ch10 (**pause at 6:28**): partners try each other's PDF. Each learner shows three things: headings in the Navigation pane, B5 = =SUM(B2:B4) showing 28, and the PDF opened with a working link. Mark on the roster. | — | ch10 | Roster | Re-model only the missing step. |
| 112–120 | A | Transfer and close. Home task: one real notice with a heading and numbered steps, or a three-line SUM list; report at week 4 Reconnect. Save or print the worksheet; copy or delete Resource pack; Start fresh on this computer. | 22, 23 | — | — | — |

Timing check: 10 + 5 + 16 + 13 + 10 + 19 + 17 + 12 + 10 + 8 = 120 minutes.

**Moved or optional**
- The two labs are dissolved into cycles A–E.
- Chart (slide 11, ch6) becomes Show-only, with an extension for fast finishers.
- Video editing (slide 14, ch8) is described on the simulation.
- Image editing moves inside PowerPoint.
- The slide 20 check moves to cycle B and slide 19 to cycle C.

**Tight spots:** C (19 minutes) and D (17 minutes). If running long, first drop the chart Show, then slides 2–3 of task 6. Keep the cropped, described and credited photo on slide 1.

## Top 10 changes, ranked

| # | Change | Where | Why (Tell/Show/Do/Review, WIPPEA or andragogy) | Effort | Source file to edit |
|:--|:--|:--|:--|:--|:--|
| 1 | Replace the 7-row agenda with five cycles, an individual check and apply-and-close, as above. Name the slides, chapters, pause times and tasks. | Lesson plan | Each skill gets its own Tell → Show → Do → Review; WIPPEA mastery before moving on; chunking | Medium | `author-content.py` week 3 `agenda` |
| 2 | Cut the tool load: Word, then Excel, then PowerPoint. Crop inside PowerPoint. Chart and video editing become Show-only; drop "data table or labeled chart" from task 6. | Agenda; tasks 6–7 | Cognitive load for older novices; the Do must be possible in the time | Small | `author-content.py` `agenda`, `lab`, `answers` |
| 3 | Replace the SVG with a JPG (`practice-photo.jpg` from `resource-pack.webp`; ready copy in scratchpad). Update the worksheet button and the slide 13 scene. | Task 7; slide 13 | High correctness item; the Show must match the Do; the alt-text Do needs a describable picture | Small | New asset; `build-pages.py` line 91; `scenes.py` `crop()` |
| 4 | Fix the formula Show: pause ch5 at 2:59, get written predictions, play to 3:12, skip 3:25, then type the formula live saying each key. Re-record ch5 later. | Cycle C; ch5 | Predict-before-reveal; the Show must include the exact keystrokes the Do needs | Small (plan) / large (re-record) | Agenda now; `SCRIPT.md`, beat 5, `screen-share-scenes.py` later |
| 5 | Rewrite all 8 tasks with named inputs. Given lines for the handout; a practice link address; seat swap for task 4; B5, Enter and Save As .xlsx for task 5; exact slide titles; JPG, Crop, View Alt Text and a credit line; one Resource pack folder. | Worksheet and answer guide | Do must be possible and reliable; readiness | Small | `author-content.py` `lab`, `answers` |
| 6 | Rewrite the objectives in ABCD form as five groups (handout, editing and review, workbook, slides and media, export), with checks designed first. | Slide 1; lesson plan | WIPPEA Introduction and Evaluation; backward design | Small | `author-content.py` `objectives`, `outcomes` |
| 7 | Rebuild the Evaluation: slide 20 in B, slide 19 in C, believable wrong answers, and a 3-item individual check with a roster. | Slides 19–20; 102–112 | Review checks each learner; respectful tone | Small | `author-content.py` check slides; agenda |
| 8 | Add the Windows 11 / Office quick card (14 rows, all verified). | Lesson plan and worksheet | The Show must be the same task as the Do; fixes CP-03 | Small | `author-content.py` `lab_paths` |
| 9 | Fix slide wording:<ul><li>Slide 6: the owner decides.</li><li>Slide 7: define alt text and give its path.</li><li>Slides 9–10: the typing steps; predict first.</li><li>Slide 13: how to crop and resize.</li><li>Slide 14: Clipchamp needs an account.</li><li>Slide 17: CSV drops formulas.</li><li>Slide 18: remove "artifact".</li><li>Slide 3: define screen readers.</li><li>Slide 4: Mac note at home.</li></ul> | Slides 3, 4, 6, 7, 9, 10, 11, 12, 13, 14, 17, 18, 21 | Tell must be accurate and in plain words | Small | `author-content.py` slide bodies |
| 10 | Warm-up tied to DL1 and week 2, with the Resource pack folder. A home task that feeds week 4 Reconnect. A week-specific prep list: Office apps, downloads, no accounts, the holiday. A reminder in week 2 that class meets on October 12. Later: re-render ch2 label, ch4 early total, stray label and ch9 caption, and point week 5's challenge at a fresh supplies.csv. | Warm-up; prep; other weeks; video | WIPPEA Warm-up and Application; the experience principle; cross-week consistency | Small / medium | `author-content.py` weeks 2, 3, 5; `build-pages.py`; `video-scenes.py`; `screen-share-scenes.py` |

## Gemini claims checked

**Video review (`week-03-video-gemini-3.1-pro-preview.md`)**

| Claim | Verdict | Evidence |
|:--|:--|:--|
| Accuracy 5/5: "uses standard spreadsheet syntax", formats defined correctly | **Partly agree** | The facts are right (see "Verified as correct"). But Gemini missed several problems:<ul><li>ch5 gives the answer before the prediction;</li><li>ch5 never says to type "=" or ":" or to press Enter;</li><li>ch4 shows the total early;</li><li>the ch2 label does not match its control;</li><li>the stray "Supplies" label.</li></ul> |
| Practice prompts 1/5: at 1:54, 3:22 and 6:23 "the audio continues instantly" | **Agree**, with corrected times | Those are the prompt starts. They end at 1:57.7, 3:25.2 and 6:28.2, with 0.48 s, 0.82 s and 1.08 s of silence. At 3:22 the answer was not revealed "immediately" after; it was given 14 s before. |
| A/V alignment 5/5; "3:32 the chart data selection highlights exactly when the narrator mentions selecting labels" | **Disagree** | Ch6 is not a screen demo: `screen-share-actions.json` lists only ch2 and ch5. Frames 3:35, 3:53 and 4:10 show a static bar chart with no selection highlight. The ch4 table showing "Total 25" before ch5 is a mismatch Gemini did not note. |
| Screen demos 5/5; "2:47 the formula is typed out clearly… exact keystrokes obvious" | **Partly disagree** | The formula is in the formula bar by 2:50, and B5 stays empty until 3:01. Enter is never shown or said. The ch2 Heading 1 step lasts 0.86 s. |
| Legibility 5/5 | Not scored | The frames look readable on a projector; text size was not measured from pixels. |
| Captions "not burned in" | **Agree** | Captions are a VTT track. The earlier review verified the text. |
| Top issue 3 and tip: "show a real video editor (Clipchamp) live" | **Disagree for learners; optional for the instructor** | Clipchamp requires a Microsoft account ([Microsoft](https://support.microsoft.com/en-us/topic/how-to-connect-clipchamp-with-your-personal-or-family-microsoft-account-fbaf526a-809d-4a1f-aad9-64a72cf35a50)), and GS6 4.1.5 is "Describe". The slide 14 simulation is enough. The instructor may show their own account on the projector. |
| Tips: pause at 1:54, 3:22 and 6:23; show the real Word ribbon for Heading 1; show where to add alt text | **Agree with the Word and alt-text tips; change the ch5 pause** | Pause ch5 at 2:59, not 3:22, which is after the answer. |
| Narration "synthetic… lacks warmth" (3/5) | Not assessed | This is the AI clone of the instructor's voice, as noted in the week 1 review. |

**Structure review (`week-03-structure-gemini-3.1-pro-preview.md`)**

| Claim | Verdict | Evidence |
|:--|:--|:--|
| Restructure starts with "Pre-test (25 mins)"; top change 2 "Add the 25-minute pre-test" | **Disagree** | Week 3 has no pre-test. The syllabus: "The pre-test occurs before instruction in week 1." The prompt template sent to Gemini wrongly asked it to "keep the 25-minute pre-test". Its running order therefore squeezes all teaching into 95 minutes. |
| Presentation Weak, Practice Weak; break into micro-cycles per application | **Agree** | Same finding; the proposal uses five cycles. |
| Introduction Strong | **Partly disagree: Adequate** | The objectives are not measurable, ch1 is not scheduled, and the intro has no time slot. |
| Evaluation Adequate | **Disagree: Weak** | Two knowledge checks cover two of five outcome groups, and there is no individual record. |
| Application Strong | **Partly disagree: Adequate** | Ch10 is not scheduled and there is no home task, although week 4 does follow up. |
| Move slides 19 and 20 into their cycles | **Agree** | This is structure, though Gemini listed it under content correctness. |
| Video editing: "not a true Do"; Clipchamp needs an account | **Agree about the account; disagree about the Do** | GS6 4.1.5 asks learners to describe. The slide 14 simulation plus one spoken sentence is a fitting Do. |
| Track Changes on separate workstations needs a seat swap | **Agree** | Correctness row 3. Gemini found it independently. |
| Chart into slides without a Show | **Agree** | The chart becomes Show-only. |
| Show where to add alt text | **Agree** | View Alt Text, verified. |
| Slide 4 Mac reference: remove | **Partly agree** | Keep it as "On a Mac at home, use Command". Learners may own Macs. |
| "Allow learners to choose their own costs" | **Disagree for the core task** | The fixed 12/8/5 → 25 → 28 is what makes the check self-verifying, and week 5 reuses it. Offer it as an extension. |
| Pacing "highly unrealistic" with 4–5 apps | **Agree** | Matches CP-07. |
| Missed by Gemini | — | <ul><li>The SVG practice image (High).</li><li>Slide 6 "reviewer" wording.</li><li>The task 5 CSV-save trap.</li><li>The ch5 order and missing keystrokes.</li><li>The ch4 early total.</li><li>The 4.2 mapping.</li><li>The generic prep.</li></ul> |
