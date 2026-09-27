# Week 1 structure and content review (Tell, Show, Do, Review + WIPPEA + adult learning) — Claude

Scope: Digital Literacy Level 2, week 1 "Make technology work for you", class Monday 2026-09-28. Reviewed read-only against `vublessons` `main` at b421f7b. That commit includes the 2026-09-26 pre-cohort fixes, which changed navigation, shared-computer reset and contrast, not week 1 content.

Conventions:
- Slide numbers are as learners see them (slide 1 = title, 24 slides).
- Lesson-plan minutes come from `weeks/week-01/lesson-plan.html` (generated from `scripts/dl2/author-content.py` week 1 `agenda`).
- Video times are m:ss in `media/week-01.mp4` (7:08). Chapter starts: ch1 0:00, ch2 0:39, ch3 1:25, ch4 2:08, ch5 2:47, ch6 3:33, ch7 4:17, ch8 4:58, ch9 5:44, ch10 6:25.
- Frames were extracted at the start, middle and end of every chapter, at all 15 screen-share actions (ch2 and ch7) and at narration-specific moments, and each one was inspected. They are in `scratchpad/video-eval/w1frames-claude/`.

## Verdict

**Monday 2026-09-28 is teachable. Week 1 is not yet a Tell, Show, Do, Review lesson.** It has the right parts in the wrong order. Most of the technical content is correct.

**Strengths**
- A clear routine that learners can repeat: Choose → Test → Restore (slides 1, 4 and 23; video ch1 and ch10).
- Low-risk practice with fictional data.
- Working simulations on slides 5–7, 14 and 15.
- A captioned video whose two screen demonstrations are good models: ch2 (page zoom) and ch7 (calendar entry).
- Week 2 opens by asking learners to repeat this routine, which is exactly the follow-up WIPPEA wants.

**Problems**
- **Big blocks, not cycles.** 35–55 covers nine slides of Tell. 65–80 covers six more slides plus the whole 7:08 video. Then one 30-minute lab covers 8 tasks, and a 10-minute check closes the session.
  - Most skills are practised 25–75 minutes after they are taught.
  - The best Show (the video) plays after all the Tell. For zoom, learners even try it on slide 6 before they see the video demo.
- **Warm-up does not use prior learning.** It never recalls Level 1, which already taught USB, HDMI and Ethernet, and memory versus storage.
- **Practice is thin and shared.** Pairs "switch driver and coach roles halfway", so each learner personally does only about half of the tasks.
- **Five skills are only told:** browser settings, brightness/contrast controls, processing, choosing a default printer, and cloud. Learners never practise them and nothing checks them.
- **Evaluation is thin.**
  - Two knowledge checks cover two of the three objectives, and their wrong answers are too silly to reveal a real misunderstanding.
  - Each learner demonstrates one adjustment in about 35–40 seconds.
- **Task 5 is impossible as written** (create a calendar appointment). The lab has no calendar tool without an account, and no simulation can create an event.

**Correctness:** 1 High (task 5), 4 Medium, 10 Low. No slide teaches something that would harm a learner. The Medium items:
- The default-printer definition does not match how Chrome and Edge pick a printer.
- Brightness and contrast controls are misplaced for desktop monitors.
- Laser versus inkjet is given no "which to choose" guidance.
- The "autocorrect a name" task is unreliable on a desktop.

**For Monday:** use the revised running order below. Play each chapter next to its slide, and have every learner do each core task right after its demo. Supply a named one-page file for task 7 and a "teh" trigger for task 8. Run task 5 as a paper or simulated entry that copies ch7's form. The authoring changes can follow.

## WIPPEA map

| Stage | Where it happens | Rating | Evidence | What to change |
|:--|:--|:--|:--|:--|
| **W — Warm-up** | 0–10 "Welcome and goals"; slides 1–2; worksheet task 1 (not reached until 80–110); no video | **Weak** | <ul><li>Slide 2 ("Name a digital task you already do well. Choose one task you want to make easier.") draws out experience, but nothing reviews earlier coursework.</li><li>DL1 week 1 already taught "Recognize cables, ports, and connectors (USB, HDMI, Ethernet)" and "the difference between memory (RAM) and storage" (`digital-literacy-1/weeks/week-01/syllabus.html`). DL2 slides 9–10 re-teach both without mentioning it.</li><li>The same 10 minutes also carries welcome, logins and "Demonstrate text size and lesson navigation".</li></ul> | <ul><li>A 4-minute recall with real HDMI, USB and Ethernet cables (use the slide 10 cards as the answer check).</li><li>A 2-minute pair share for slide 2.</li><li>Have learners write task 1 now.</li></ul> |
| **I — Introduction** | Slide 1 objectives (0–10); slide 4 routine (after the pre-test, ~35); video ch1 0:00–0:39 is not scheduled | **Adequate** | <ul><li>Objectives are shown in writing with the Choose/Test/Restore organiser, and ch1 links to daily life ("read a letter, hear instructions, or remember an appointment").</li><li>The objectives are not measurable, and they leave out 1.3 (automation, cloud, autocorrect) and 2.3 (help, feedback), which slides 16, 17 and 19 and task 8 teach.</li><li>The 25-minute pre-test separates the objectives from the lesson.</li></ul> | <ul><li>Restate the objectives in ABCD form at 35.</li><li>Play ch1 (39 s) as the bridge, then slide 4.</li></ul> |
| **P — Presentation** | 35–55: slides 4–12 (9 slides). 65–80: slides 13–17 and 19, plus slide 18 (video) | **Adequate** content, **Weak** pacing | <ul><li>Several modes: photo scenes, simulations (5–7, 14, 15), flip cards (10), step lists (4, 12), video, transcript and captions.</li><li>Undefined terms: site permissions, display scaling, the monitor's contrast control, mail rule.</li><li>About 2.2 minutes per slide at 35–55. At 65–80, 15 minutes must hold six slides plus a 7:08 video.</li><li>Slides 17 (cloud) and 19 (help) are named in no phase.</li><li>No planned check of understanding in either block, apart from slide 6.</li></ul> | <ul><li>Teach one skill at a time; play each chapter with its slide.</li><li>End each skill with a one-question check.</li></ul> |
| **P — Practice** | <ul><li>Instructor model: 35–55 "Think aloud through one change and its check"; 65–80 "Model a fictional appointment…".</li><li>Guided: slide 6.</li><li>Lab 80–110: worksheet tasks 1–8.</li></ul> | **Weak** | <ul><li>Modelling is planned for one change and one appointment only. Zoom (slide 6) is the only guided in-lesson try.</li><li>8 tasks in 30 minutes is about 3.75 minutes each, including typing answers.</li><li>"Partners switch driver and coach roles halfway", so each learner drives about half the tasks.</li><li>Task 5 has no tool (see Content correctness, row 1).</li><li>No task covers browser settings (slide 8), setting a default printer (slide 11) or cloud (slide 17).</li><li>Sound is taught around minute 45 but practised at 80–110.</li></ul> | <ul><li>Every learner does each core task on their own workstation right after its Show. The partner coaches but never takes over.</li><li>The lab time is spread across the skill cycles instead.</li></ul> |
| **E — Evaluation** | 110–120: slides 20–21 plus "each learner demonstrates one adjustment"; answer guide; pre/post items 1.1, 1.2, 1.3, 1.5, 2.3 | **Weak** | <ul><li>The knowledge checks cover sound (objective 1) and calendar privacy (objective 2). Nothing checks objective 3 (connection and printer).</li><li>The wrong answers are "Buy a new monitor", "Erase the browser history" and "Publish your account password". They are not believable mistakes, so a right answer shows little.</li><li>One demo per learner in the minutes left after the checks is about 35–40 seconds each for 12 learners.</li><li>The plan asks for Independent / With prompt / Needs practice ratings but gives no record sheet. Typed worksheet answers stay only on that page ("print before closing").</li></ul> | <ul><li>A short Review in each cycle (partner check plus an instructor scan).</li><li>A final 3-item individual performance checklist.</li><li>Believable wrong answers; add a printing check.</li></ul> |
| **A — Application** | Slides 23–24; video ch10 6:25–7:08; week 2 agenda 0–10 "Reconnect: Ask learners to demonstrate last week's check-one-change routine" | **Adequate** | <ul><li>Transfer prompts exist: slide 24 "Name one thing you can now do and one next practice step", and ch10 "choose one improvement that matters to your own routine".</li><li>Week 2 follows up.</li><li>Missing: a concrete task on the learner's own device at home, and an example drawn from veterans' lives.</li></ul> | Home task: "On your own device, make one change from today, note the path and how you undid it, and bring it to week 2 Reconnect." |

**Overall flow.** The order is W → pre-test → P (35–55) → break → P (65–80) → Practice (80–110) → E and A (110–120).
- No objective gets presentation → practice → check before the next one starts. All three objectives are presented before any practice, and they are all checked together in the last 10 minutes. WIPPEA and Tell/Show/Do/Review both ask for mastery at each step.
- The video belongs chapter by chapter inside each skill cycle, as the Show. It does not belong as one block after all the slides.
  - Slide 18 sits after slides 13–17, and the plan plays it at 65–80, 30–40 minutes after zoom, sound and printing were taught.
  - Learners try zoom on slide 6 about 30 minutes before ch2 demonstrates it.
- The pre-test's position (before instruction) is correct.

## Tell, Show, Do, Review by skill

| Skill | Tell (where) | Show (where) | Do (where; minutes available) | Review (where) | Missing or weak steps |
|:--|:--|:--|:--|:--|:--|
| Choose/Test/Restore routine | Slides 1, 4; ch1 0:00–0:39 | Slide 4 before/change/check/restore list; ch1 diagram | Embedded in every task | Slide 23; ch10; 110–120 demo | ch1 not scheduled. Otherwise sound: it is the week's backbone. |
| Page zoom | Slide 5; ch2 narration | Slide 5–6 simulation (100/125/150%); ch2 0:39–1:25 screen demo (menu → Zoom → 110% → check → Ctrl+0) | Slide 6 inside 35–55 (no minutes set); task 2 at 80–110 (~3.75 min) | Answer guide task 2; pre-test Q1; 110–120 demo only if the learner chooses zoom | The Show (ch2 at 65–80) comes after the Do (slide 6). Does not say that Chrome and Edge remember zoom per site. |
| Display scaling / text size | Slide 5 (one sentence); ch3 1:25–2:08 | ch3 diagram only; "exact controls depend on your computer" (1:44). The real path is never shown. | None (sensible: shared machines) | Post-test Q1 only | Needs a projector-only Show of Settings > System > Display > Scale and Settings > Accessibility > Text size, plus a home Do. |
| Sound output and mute | Slide 7; ch4 2:08–2:47 | Slide 7 simulation (Headphones/Speakers, Mute, visual test); ch4 diagram (Computer → Headset). The Windows UI is never shown. | Task 3 at 80–110 | Slide 20 at 110–120; answer guide task 3 | Show the Windows 11 path (Quick Settings volume arrow, or Settings > System > Sound > Output), and the Volume mixer for a meeting app. Taught at ~45, practised at 80+. |
| Brightness vs contrast | Slide 7 sentence | Slide 7 "Check the screen too" compares text colour contrast (content), not the monitor's control; no video | Task 3 asks only to "explain" | Answer guide task 3 (definition) | No Show of where the controls are (monitor buttons on desktops; Windows slider on laptops) or of Windows Contrast themes. |
| Browser settings (home page, downloads, permissions) | Slide 8 | Slide 8 scene: three fixed text panels; no video | **None** (no worksheet task) | None in class (pre/post 2.3 item mentions a download folder) | Show, Do and Review all missing. GS6 1.1.2 is not practised. |
| Processing / memory / storage | Slide 9; ch5 2:47–3:13 | Slide 9 scene; ch5 workbench/cabinet diagram | None | None | Repeats DL1 week 1. Could be warm-up recall. |
| Connections (HDMI, Ethernet, USB) | Slides 9–10; ch5 3:14–3:31 | Slide 10 flip cards and connector icons. ch5 shows the memory/storage diagram while narrating connectors. No real cables. | Task 4 at 80–110 (its three tasks are not listed on the worksheet) | Answer guide task 4 | Real cables as props (DL1 did this). List the three tasks on the worksheet. |
| Printer type and default printer | Slide 11 | Slide 11 scene; no video (ch6 is about preview) | None ("select a default printer" is never done) | None | GS6 1.5.1 and 1.5.3: no Show of Settings > Bluetooth & devices > Printers & scanners, no Do, no check. |
| Print preview / one test page | Slide 12; ch6 3:33–4:17 | Slide 12 preview simulation; ch6 diagram (no real print dialog) | Task 7 at 80–110 ("a one-page handout", none supplied) | Answer guide task 7; pre/post 1.5 | Needs a live Ctrl+P Show on a named page, and a named file for the Do. |
| Calendar entry | Slide 13; ch7 4:17–4:41 | **ch7 screen demo** (New event → title → 2–3 PM → Room A → 30-minute reminder → Save → Day/Week/Month → Reopen, "Time zone: Eastern"), the week's best Show; 65–80 "Model a fictional appointment" | Task 5 at 80–110: **no tool.** Slide 13 only reveals fixed fields; Windows Calendar is retired. | Answer guide task 5 | The Do is impossible as written. The Show happens at 65–80, 15 minutes before the Do. |
| Calendar views | Slide 15; ch7 4:41–4:51 | Slide 15 view switcher; ch7 Week/Month | Slide 15 (learner deck); task 6 | Answer guide task 6; post-test 1.2 | Adequate. |
| Free/busy sharing | Slide 14; ch8 4:58–5:44 | Slide 14 toggle; ch8 "Your calendar" / "Partner sees Busy" | Task 6 (a decision plus explanation, which the simulation supports) | Slide 21; pre-test 1.2 | Adequate as a decision. No real-service Show (Outlook "Can view when I'm busy", Google "See only free/busy"). |
| Automation (rules, autocorrect, autocomplete) | Slide 16 | Slide 16 fixed scenes. ch9 covers account, reminder permission and help, **not** autocorrect or rules. | Task 8 part 1: "a name that autocorrect changes" (unreliable on desktop) | Answer guide task 8; pre-test 1.3, post-test 1.3 | No real Show; the Do trigger is unreliable. |
| Cloud | Slide 17; ch9 5:50–5:59 | Slide 17 scene | None | None | Named in no plan phase. A one-question oral check would suffice (GS6 1.3.2 is "describe"). |
| Getting help and feedback | Slide 19; ch9 6:05–6:22 | Slide 19 help-request scene | Task 8 part 2 | Answer guide task 8; pre/post 2.3 | Named in no plan phase. Fine once scheduled. |

**Week 1 runs as big blocks, not short cycles.** The Tell for 15 skills sits in two blocks of 20 and 15 minutes. The Show (video) is one block after all the Tell. The Do is one 30-minute block, and the Review is one 10-minute block.
- Only zoom has any in-lesson Do.
- Five skills have Tell only: browser settings, brightness/contrast controls, processing, default printer and cloud.
- One skill has Tell and Show but an impossible Do (calendar entry).

For older learners who need time to read, try and ask, this has three effects:
- They must hold 9–15 new procedures in memory for up to 75 minutes before trying them.
- Mistakes surface only in the lab, when the instructor can no longer re-model to the whole class.
- The confidence that comes from "I just did it" is postponed to the end.

## Objectives

GS6 Level 2 groups claimed: 1.1–1.6 and 2.3.

**1. "Adjust device and browser settings for a task."**
- **ABCD rewrite:** On a Windows 11 lab workstation with Edge or Chrome and the course practice page, each learner:
  - enlarges webpage content with browser zoom (menu or Ctrl + plus) and returns it to 100% with Ctrl + 0;
  - selects the headset as the audio output and confirms it with a test sound;
  - states which control (page zoom, display scale, brightness) fits a described reading problem.

  Degree: all three correct, with at most one prompt, and lab settings restored.
- **Taught:** slides 4–8; video ch2, ch3, ch4.
- **Practised:** slide 6; tasks 2–3. Browser settings (slide 8) are not practised.
- **Evaluated:** slide 20; one demo at 110–120; pre/post Q1.
- **Status:** Partly met. The browser-settings half (GS6 1.1.2) is told only.

**2. "Create a practice appointment and choose what others can see."**
- **ABCD rewrite:** Using the practice calendar (an instructor-provided account or a course simulation), each learner:
  - creates a fictional event with title, day, start and end, location and a reminder;
  - reopens it to confirm all five fields;
  - chooses free/busy sharing for a scheduling partner and says what the partner will see.

  Degree: all five fields correct after reopening; sharing choice and explanation correct.
- **Taught:** slides 13–15; video ch7–8.
- **Practised:** tasks 5–6. Task 5 cannot be done without a tool.
- **Evaluated:** slide 21; pre/post 1.2. No performance check of creating an event.
- **Status:** The creation half cannot be practised or checked as written.

**3. "Select a connection and a printer; verify the result."**
- **ABCD rewrite:** Given three tasks (external display, wired network, flash drive) and their own workstation, each learner:
  - matches HDMI, Ethernet and USB to the tasks and identifies one real port;
  - opens print preview (Ctrl + P) for a named one-page document, confirms the destination printer's name, sets Pages to 1 and Copies to 1, and records the orientation, without printing unless directed.

  Degree: all items correct.
- **Taught:** slides 9–12; video ch5–6.
- **Practised:** tasks 4 and 7.
- **Evaluated:** answer guide only; pre/post 1.5. No knowledge check.
- **Status:** "Select a printer" is ambiguous. Choosing a default printer (GS6 1.5.3) and confirming the printer is connected (1.5.2) are not practised. "Verify the result" conflicts with task 7's "Do not print".

**Missing objective A (GS6 1.3), taught but not stated.**
- **Proposed:** Given a word processor, the learner triggers an AutoCorrect change ("teh" → "the"), undoes it with Ctrl + Z, accepts or rejects one suggestion, and describes in one sentence what a mail rule and a cloud service do.
- **Taught:** slides 16–17, ch9. **Practised:** task 8. **Evaluated:** pre/post 1.3.

**Missing objective B (GS6 2.3), taught but not stated.**
- **Proposed:** The learner writes a help request naming the app and version, the task, what was tried and the exact message, and records one specific piece of partner feedback.
- **Taught:** slide 19, ch9. **Practised:** task 8. **Evaluated:** pre/post 2.3.
- GS6 2.3.1 ("be aware of technological advancements") is not covered anywhere in week 1.

**Backward design.** The evidence list in the plan copies the worksheet. It was not designed first. Two of five taught outcome groups have no stated objective, and objective 3 has no in-class check.

## Adult learning principles

| Principle | Rating | Evidence | Improvement |
|:--|:--|:--|:--|
| 1. Need to know | Adequate | <ul><li>Slide 2 asks for a task the learner wants to make easier; ch1 opens with letters, instructions and appointments.</li><li>The routine tells learners why to check and restore.</li><li>Individual slides state *what* (for example slide 11 "Laser printers use toner…") more than *why it matters to me*.</li><li>Scenarios are library or community examples; none is drawn from veterans' lives.</li></ul> | Open each cycle with a one-line problem veterans have, using fictional details: reading a small-print benefits letter online, hearing a telehealth call through the right headset, printing clinic directions once, a fictional clinic reminder. |
| 2. Self-concept | Adequate | <ul><li>Learners choose their task (slide 2, ch10); "Keep or undo the change" (slide 4); partner roles; fictional data.</li><li>Throwaway wrong answers such as "Publish your account password" (slide 21) and "Buy a new monitor" (slide 20) can read as talking down to capable adults.</li><li>Driver/coach sharing means half the learners watch rather than do.</li></ul> | Use believable wrong answers (for example "Raise the volume slider", "Restart the computer"). Each learner drives their own workstation. |
| 3. Experience | **Weak** | <ul><li>No link to Basic or DL1, though DL1 taught cables, memory versus storage (week 1) and browsers (week 2).</li><li>Slide 2's "task you already do well" is never used again.</li><li>No "What do you do now when there's no sound?" prompt.</li></ul> | Warm-up recall with real cables. Ask "what do you try first?" before each Show, and correct habits that need unlearning (for example, pressing Print repeatedly, as ch6 warns). |
| 4. Readiness | Adequate | <ul><li>The skills (reading comfortably, hearing, printing once, appointments, getting help) are ones these learners need now.</li><li>The calendar and sharing tasks assume accounts learners may not have.</li><li>Nothing links the skills to the learner's own home device.</li></ul> | Home-device transfer task. Name which calendar learners will actually use (Outlook.com, Google or a phone). |
| 5. Orientation (problem-centred) | Adequate | <ul><li>Strongly problem-framed: slides 4, 12 ("Print one page before twenty"), 20 ("The video is playing silently"), 19; ch2 and ch4 scenarios.</li><li>Subject-centred titles: slide 9 "Processing, storage, and connections", slide 11 "Printer choices", slide 17 "Cloud services use another computer".</li></ul> | Recast 9, 11 and 17 as problems: "Computer slow or full?", "Which printer for 200 flyers?", "Where did my file save?" |
| 6. Motivation | Adequate | <ul><li>A confidence-building routine, "Mark practiced" buttons (slides 4, 12), a completion slide, and ch10 "choose one improvement that matters to your own routine".</li><li>Visible success is delayed to the lab.</li></ul> | A quick "I did it" check after every cycle; end with each learner naming a change they can now make at home. |

## Content correctness

| # | Where | What it says | What is correct (source) | Severity |
|:--|:--|:--|:--|:--|
| 1 | Worksheet task 5; lesson plan "Prepare the room"; slide 13 | "Create a fictional library appointment with a reminder." Prep lists only "a word processor and spreadsheet app" and "instructor-provided fictional accounts". | Windows Mail and Calendar support ended 31 December 2024; new Outlook is the replacement and needs an account ([Microsoft](https://support.microsoft.com/en-us/office/outlook-for-windows-the-future-of-mail-calendar-and-people-on-windows-11-715fc27c-e0f4-4652-9174-47faa751b199)). The slide 13 scene only reveals fixed fields (`scenes.py` (1,13)); no simulation can create an event. **Task 5 cannot be done as written on a lab PC without an account.** Task 6 can be done as a decision with the slide 14–15 simulations. | **High** |
| 2 | Slide 11 | "A default printer is the device an app initially selects." | <ul><li>Windows 11: Settings > Bluetooth & devices > Printers & scanners. With "Let Windows manage my default printer" on, Windows picks the last printer used, and "Set as default" is hidden ([Microsoft](https://support.microsoft.com/en-us/windows/hardware/printer/set-a-default-printer-in-windows)).</li><li>Chrome and Edge print preview select the **most recently used** printer, not the system default, unless a policy is set ([Chrome Enterprise](https://chromeenterprise.google/policies/print-preview-use-system-default-printer/), [Edge policy](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-browser-policies/printpreviewusesystemdefaultprinter)).</li><li>The pre-test item 1.5 itself says "the print dialog shows the one used yesterday".</li><li>The slide's advice ("Check before sending") is right, but the definition is misleading and GS6 1.5.3 (select a default) is never taught.</li></ul> | Medium |
| 3 | Slide 7 | "Brightness changes light output; contrast changes separation between light and dark." Simulation: "Low contrast / Readable contrast" grey-versus-dark text. | <ul><li>The definitions are correct ([Display contrast](https://en.wikipedia.org/wiki/Display_contrast); [Lenovo](https://www.lenovo.com/us/en/knowledgebase/why-monitor-brightness-and-contrast-ratios-are-key-to-display-quality/)).</li><li>The simulation shows text-colour contrast (content), not the monitor's contrast control.</li><li>On desktops with an external monitor, "You might not see the Brightness slider… use the buttons on it" ([Microsoft](https://support.microsoft.com/en-us/windows/change-display-brightness-and-color-in-windows-3f67a2f2-5c65-ceca-778b-5858fc007041)).</li><li>Windows' own readability setting is Settings > Accessibility > Contrast themes ([Microsoft](https://support.microsoft.com/en-us/accessibility/windows/change-color-contrast-in-windows)).</li><li>Learners are not told where any of these controls are.</li></ul> | Medium |
| 4 | Slide 11 | "Laser printers use toner; inkjet printers use liquid ink. Choose for the task and running cost." | <ul><li>Consumables are correct.</li><li>GS6 1.5.1 asks learners to *distinguish* the two. The usual distinction: laser has lower cost per page and suits high-volume text; inkjet is cheaper to buy and better for colour and photos ([CDW](https://www.cdw.com/content/cdw/en/articles/hardware/inkjet-vs-laser-printers.html)).</li><li>The slide never says which suits which job.</li></ul> | Medium |
| 5 | Slide 16 "Maren → Marine"; worksheet task 8 | "Type a sentence with a name that autocorrect changes." | <ul><li>Office AutoCorrect uses "a standard list of typical misspellings and symbols", and Ctrl + Z undoes a correction ([Microsoft](https://support.microsoft.com/en-us/excel/autocorrect-features-in-excel)).</li><li>Windows' own "Autocorrect misspelled words" applies to the touch keyboard; physical keyboards get only optional text suggestions ([ElevenForum](https://www.elevenforum.com/t/turn-on-or-off-autocorrect-misspelled-words-in-windows-11.9982/); [Microsoft](https://support.microsoft.com/en-us/accessibility/windows/enable-text-suggestions-in-windows)).</li><li>Whether a given name is changed on a lab desktop is unpredictable; name changes are typical of phone keyboards.</li><li>Use a listed entry ("teh" + space → "the") and test it on a lab machine.</li></ul> | Medium |
| 6 | Slide 8 simulation | "Home page: Community learning resources / Startup: Open the home page" | Chrome: "Your startup page and homepage aren't the same unless you set them to be". Startup options are New Tab page, continue where you left off, or specific pages ([Google](https://support.google.com/chrome/answer/95314)). Edge sets the home button under "Start, home, and new tab page" ([Microsoft](https://support.microsoft.com/en-us/microsoft-edge/change-your-browser-home-page-a531e1b8-ed54-d057-0262-cc5983a065c6)). | Low |
| 7 | Slide 10 card | "USB carries data; USB-C also has charging and optional display uses." | USB-A ports also supply power (USB 2.0: 5 V, 500 mA) ([USB hardware](https://en.wikipedia.org/wiki/USB_hardware)). The video is more accurate: "may carry data or power depending on the equipment" (3:22). | Low |
| 8 | Slide 16 | "A rule can sort mail or repeat a reminder." | Mail rules are correct: new Outlook Settings > Mail > Rules, with an option to run a new rule on existing messages ([Microsoft](https://support.microsoft.com/en-us/office/manage-email-messages-by-using-rules-in-outlook-c24f5dea-9465-4df4-ad17-a50704d66c59)). Gmail calls them "filters" ([Google](https://support.google.com/mail/answer/6579)). A repeating reminder is a recurrence setting, not a rule. The post-test 1.3 item repeats this wording ("Leave the rule alone…"). | Low |
| 9 | Slide 4 vs ch2 (0:54) | Slide 4: "page zoom to 125%"; ch2: "increase it one step" → 110%. | Both are correct. Chromium zoom steps run …1.0, 1.1, 1.25, 1.5… ([Chromium source](https://github.com/chromium/chromium/blob/main/third_party/blink/common/page/page_zoom.cc)), so 125% takes two presses. Say so, or align the two. | Low |
| 10 | Slides 4–6; ch2 | Restore with Ctrl + 0. | Correct, but add why: Chrome and Edge remember zoom **per site** ([Google](https://support.google.com/chrome/answer/96810); [Microsoft](https://support.microsoft.com/en-us/accessibility/edge/accessibility-features-in-microsoft-edge)). An unreset zoom persists for the next person on a shared lab machine. | Low |
| 11 | Slides 13–15 vs ch7 | Slides: "Monday · 2:00–3:00 p.m." Video: "Tuesday, October 13" (4:17–4:55; `screen-share-scenes.py` lines 69, 83). | The materials should agree. Use Monday in both, or say "any day". | Low |
| 12 | ch5 3:14–3:31 | Narration on connections ("A display connection carries a picture…") | The screen shows the Processing / Working memory / Saved storage diagram with the caption "Storage · Saved file in the cabinet" (frames 3:16, 3:24). `video-scenes.py` line 19 has no connections beat. The visual does not match the narration. | Low |
| 13 | Lesson plan "Prepare the room" | "…a word processor and spreadsheet app… For week 6, supply a plain-text editor…" | Week 1 uses no spreadsheet. The week 6 sentence is template text shared by all six plans (`build-pages.py` ~line 90); it appears in every plan, including week 1. Headphones, cables, a one-page file and the calendar tool are not listed. | Low |
| 14 | Slide 14; ch8 | "Free/busy… without the title or location." | Correct: Outlook "Can view when I'm busy" ([Microsoft](https://support.microsoft.com/en-us/office/share-an-outlook-calendar-as-view-only-with-others-353ed2c1-3ec5-449d-8c73-6931a0adab88)); Google "See only free/busy (hide details)" ([Google](https://support.google.com/calendar/answer/37082)). Add Google's caveat: if the calendar is public, anyone can see event details, including someone given free/busy access. | Low |

**Totals:** High 1, Medium 4, Low 10 (rows 6–14 plus the ch4 item below). One more Low was found in the video: the ch4 on-screen captions run Destination → App setting → Test, while the narration runs mute → output → test → app (`video-scenes.py` line 18).

**Verified as correct**
- **Browser zoom:** Ctrl + / Ctrl − / Ctrl 0 and Command on a Mac (slide 6; ch2 0:56–1:03); menu → Zoom (ch2 0:51). Page zoom changes page content but not the browser controls (slide 5) ([Google](https://support.google.com/chrome/answer/96810); [Microsoft Edge](https://support.microsoft.com/en-us/accessibility/edge/accessibility-features-in-microsoft-edge)).
- **Display scaling versus text size (ch3 1:33–1:43):** Settings > System > Display > Scale; Settings > Accessibility > Text size ([Microsoft](https://support.microsoft.com/en-us/accessibility/windows/make-text-and-apps-bigger)).
- **Sound (slide 7; slide 20; ch4):** check mute and output first, then the meeting app's own choice. Microsoft paths: Settings > System > Sound > Output, the arrow beside the volume slider, and "Apps can use a different output device… Volume mixer" ([Microsoft](https://support.microsoft.com/en-us/windows/fix-sound-or-audio-problems-in-windows-73025246-b61c-40fb-671a-2535c7cd56c8); [Microsoft](https://support.microsoft.com/en-us/windows/hardware/audio/fix-app-audio-not-working-while-system-sounds-work-in-windows)).
- **Browser settings on slide 8** (home page, downloads location, site permissions) exist as described:
  - Edge: Settings > Downloads > Location > Change ([Microsoft](https://support.microsoft.com/en-us/microsoft-edge/change-the-downloads-folder-location-in-microsoft-edge-4049e93b-0ef6-e44f-aca0-7d5f37a39294)); Settings > Privacy, search, and services > Site Permissions ([Microsoft](https://support.microsoft.com/en-us/windows/windows-camera-microphone-and-privacy-a83257bc-e990-d54a-d212-b5e41beba857)).
  - Chrome: Settings > Privacy and security > Site settings ([Google](https://support.google.com/chrome/answer/114662)).
- **Processor, memory and storage (slide 9; ch5):** "closing an unused app… does not create a reliable backup" ([HP](https://www.hp.com/us-en/shop/tech-takes/computer-memory-vs-storage)).
- **Connections (slide 10):**
  - HDMI carries video and sound ([HDMI](https://en.wikipedia.org/wiki/HDMI)).
  - USB-C video depends on the device and cable (DisplayPort Alt Mode) ([Plugable](https://kb.plugable.com/understanding-usb-c-alt-mode)).
  - Ethernet is a wired network connection.
- **Printing (slide 12; ch6):** preview, destination, range, orientation, copies and one test page. "Save as PDF" differs from a physical printer. Check status or queue rather than pressing Print again ([Microsoft print queue](https://support.microsoft.com/en-us/windows/view-a-printer-s-print-queue-in-windows-71505b3a-ba6b-14b2-b7f9-fd6204675ab5)).
- **Calendar entry fields (slide 13; ch7):** title, day, start and end, location, reminder, time zone. Outlook's default reminder is 15 minutes, and it has a Time Zones control ([Microsoft](https://support.microsoft.com/en-us/outlook/create-or-schedule-an-appointment)). Google also has a Time zone option ([Google](https://support.google.com/calendar/answer/37064)).
- **Calendar views and tasks (slide 15):** a task can have a deadline without a time block ([Google](https://support.google.com/calendar/answer/9901136)).
- **Automation (slide 16):** autocorrect replaces text from a list; autocomplete or prediction suggests the rest (Tab to accept) ([Microsoft](https://support.microsoft.com/en-us/word/editor-text-predictions-in-word)). Test a mail rule on existing messages.
- **Cloud (slide 17; ch9):** a provider's computers reached over a network ([NIST SP 800-145](https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-145.pdf)).
- **Help (slide 19; ch9):** use official help that matches your version, and state the task, what you tried and the exact message.
- **Knowledge checks:** the answers to slides 20 and 21 are correct.

## Does the content make sense for this audience?

**Undefined terms at first use**
- "site permissions" (slide 8).
- "display scaling" (slide 5: only "the wider desktop").
- "contrast": the monitor control versus colour contrast (slide 7).
- "rule" (slide 16).
- "default printer" (slide 11, defined imprecisely; see Content correctness, row 2).
- "time zone" when "another region" is involved (slide 13) is fine. "Free/busy" is well defined.

**Logic leaps**
- Slide 9 says "A matching connector shape alone does not guarantee every feature" before slide 10 has introduced any connector.
- Slide 15 introduces "tasks" in its last sentence with no example.
- Slide 16 moves from mail rules to autocorrect to autocomplete in one body with no bridge.
- ch9 packs account, reminder permissions, cloud and help into 41 seconds.

**Missing steps**
- Apart from ch2's "browser menu → Zoom" and ch7's simulated calendar, no real click path appears anywhere, not even in the instructor plan. Missing paths:
  - display scale and text size;
  - sound output and the Volume mixer;
  - where brightness is on a desktop monitor;
  - downloads location and site permissions in Edge or Chrome;
  - how to set a default printer;
  - how to check a printer is Ready or print a Windows test page;
  - Ctrl + P;
  - Outlook or Google free/busy sharing.
- ch3 says "The exact controls depend on your computer" (1:44).
- For learners who finished Level 1, a missing step is the most likely point of failure.

**Tasks impossible or unreliable as written**

| Task | Problem |
|:--|:--|
| Task 5 | No tool. |
| Task 4 | "three tasks" are not listed on the worksheet (only on the slide 10 cards). |
| Task 7 | "a one-page handout" is not supplied or named. |
| Task 8 | The name trigger is unreliable (see Content correctness, row 5). |
| Task 3 | Picking the output is meaningful only if the workstation has more than one device (headset plus speakers or monitor). "Explain brightness versus contrast" cannot be demonstrated on desktops without touching monitor buttons. |
| Slide 12 | "Send a test page and check the output" contradicts task 7's "Do not print unless the instructor directs it". The instructor needs a stated rule. |

**Pacing is unrealistic in three places**
- 35–55: 9 slides (4 with simulations or cards) in 20 minutes, after the pre-test; slow finishers will cut into it.
- 65–80: 6 slides plus the 7:08 video in 15 minutes, leaving about 1.3 minutes per slide with no time for the planned pauses.
- 80–110: 8 tasks in 30 minutes (~3.75 minutes each, including typing answers) with a mid-lab role swap.
- 110–120 is also tight: two knowledge checks plus an individual demo for every learner.
- The pre-test is 28 items (the printable says "Total: 28") in 25 minutes. That is feasible, but the plan does not say what late finishers do.

**Earlier findings re-checked**

| Earlier finding | Status | Evidence |
|:--|:--|:--|
| CP-03: no click paths | **Confirmed** | See "Missing steps" above. |
| CP-02 / IR-06: calendar tasks need accounts | **Confirmed for task 5, partly refuted for task 6** | Task 6 is a choose-and-explain task that slides 14–15 support without an account. |
| CP-19 / IR-10: "Model the setup" overloaded | **Confirmed**, and the 65–80 block is worse | Video ch1–6 (0:00–4:17), which match slides 4–12, are not scheduled in 35–55 at all. |
| CP-18 / IR-02: generic lesson-plan boilerplate | **Confirmed** | The "For week 6…" sentence is in all six plans; the prep, video, facilitation and feedback text is identical. |
| CP-16: task inputs missing | **Confirmed** (tasks 4, 7, 8) | See the task table above. |
| CP-11: jargon | **Confirmed** for week 1 terms | See "Undefined terms" above. |

**New in this review**
- Driver/coach sharing halves each learner's practice.
- Browser settings have no practice or check.
- Objectives omit 1.3 and 2.3.
- Warm-up ignores DL1.
- Knowledge-check wrong answers are not believable.
- The video's two think-questions (ch3 at 2:02, ch8 at 5:36) are answered less than 1 second after they are asked.
- ch5's visual does not match its narration.
- Monday versus Tuesday between slides and video.
- The default-printer definition does not match browser behaviour.
- Brightness and contrast controls are misplaced for desktops.

## Video structure

**Sequence.** The 10 chapters (38–46 seconds each) follow a sensible teaching order that mirrors the slides: routine (ch1) → zoom (ch2) → scope (ch3) → sound (ch4) → parts and connections (ch5) → print (ch6) → calendar entry and views (ch7) → sharing (ch8) → automation, cloud and help (ch9) → independent check (ch10). Opening and closing on the routine gives it a coherent frame. Captions are present for all chapters, positioned at the top during the screen demos.

**Model → prompt → answer, chapter by chapter**

| Chapter | Model | Prompt and answer | Rating |
|:--|:--|:--|:--|
| ch2 (0:39–1:25) | **Strong.** Six-step screen demo: 100% → menu → Zoom → 110% → "Check the search field and button" → Ctrl+0 restored to 100%. Checked in frames 0:39, 0:52, 0:53, 0:55, 1:08, 1:23. | "Pause the video, try one zoom step" (1:18) leaves 7 seconds before ch3; the instructor must pause. | Strong |
| ch7 (4:17–4:58) | **Strong.** Nine-step screen demo through to "Reopen • verify the saved details", which shows "Time zone: Eastern" and "Details verified" (frame 4:55). | No prompt. | Strong |
| ch3 (1:25–2:08) | Diagram. | "Which would you try first…?" (1:59–2:02) is answered at 2:03, 0.7 seconds later. | Good question, no think time |
| ch8 (4:58–5:44) | Diagram. | "Pause and decide…" (5:30–5:36) is answered "No." at 5:37. | Good question, no think time |
| ch4, ch6, ch9 | Diagram tiles and on-screen captions; no real UI. | ch4's caption order differs from the narration. | Tell only. They model the idea, not the task learners will do. |
| ch5 (2:47–3:33) | Its connectors half (3:14–3:31) has no connector visual. | — | Weak |
| ch10 (6:25–7:08) | Recap. | Clear independent-practice prompt. | Good |

**Coverage gaps.** No chapter shows browser settings, brightness or contrast, laser versus inkjet, setting a default printer, autocorrect or autocomplete, or a mail rule. Autocorrect is what task 8 depends on.

**Where it should play.** Play it chapter by chapter as the Show inside each skill cycle, as in the restructure below. Stop at the prompts: 1:18, 2:02, 5:36 and 6:28.
- The current plan says to play the explainer "within the existing time allocation" at 65–80, after the zoom, sound and print slides have already been taught. Then the Show follows the Do for zoom and repeats the Tell for everything else.
- Slide 18 becomes a chapter menu for replay, and the whole video is assigned as home review (captions and a transcript are available).

## Recommended restructure

This is a 120-minute running order built from short Tell, Show, Do, Review cycles inside the WIPPEA stages. It keeps the 25-minute pre-test and existing materials, and uses only current slide numbers, chapters and tasks. "Live" means the instructor demonstrates on the projector in the lab's real browser or Windows.

| Minutes | WIPPEA | Tell, Show, Do, Review cycle | Slides | Video | Worksheet / check | Notes |
|:--|:--|:--|:--|:--|:--|:--|
| 0–10 | W + I | Warm-up recall and goals | 1, 2, 10 (cards used as the recall answer) | — | Task 1 written now | Logins and text-size demo (as planned). Hold up real HDMI, USB and Ethernet cables for DL1 recall (4 min). Read the objectives aloud. |
| 10–35 | Diagnostic | — | 3 | — | Pre-test | Early finishers read slide 4. Late finishers may run to 38. |
| 35–38 | I | **Tell:** the routine and the ABCD objectives | 4 | ch1 0:00–0:39 | — | "Choose → Test → Restore" becomes every cycle's Review language. |
| 38–50 | P → P → E | **Cycle A, reading comfort.** Tell: slide 5. Show: ch2 plus live Ctrl + in Edge. Do: slide 6, then task 2, every learner. Review: partner confirms the reset to 100%; instructor scans. Then **Tell/Show** ch3 (pause at 2:02 for the prediction) and live Settings > System > Display > Scale and Settings > Accessibility > Text size, projector only. | 5, 6; 8 on projector only | ch2 0:39–1:25; ch3 1:25–2:08 | Task 2 | **Slide 8:** 2-minute projector Show of Edge Downloads and Site Permissions, no learner change. Extension for fast finishers: find the downloads location. |
| 50–60 | P → P → E | **Cycle B, hearing and screen.** Tell: slide 7. Show: ch4 plus live Quick Settings output switch. Do: task 3 with a headset. Review: slide 20. Brightness: show the monitor buttons or laptop slider and Contrast themes; do not apply them. | 7, 20 | ch4 2:08–2:47 | Task 3 | Use more believable wrong answers on slide 20 (change 3). |
| 60–70 | — | Break | — | — | — | Screen-free. |
| 70–80 | P → P → E | **Cycle C, connection and printer.** Tell: slides 11–12. Show: ch6 plus live Ctrl + P on the worksheet page (destination name, Pages = 1, Layout, Copies = 1) and Printers & scanners printer status. Do: task 7 (named page, no print) and task 4 "check one actual port". Review: partner reads back printer, orientation and range; oral question "laser or inkjet for 200 text flyers?" | 11, 12 (9 optional) | ch6 3:33–4:17 (ch5 optional) | Tasks 4, 7 | **Optional:** slide 9 and ch5 (DL1 already covered them). One named test print by the instructor only. |
| 80–95 | P → P → E | **Cycle D, calendar.** Tell: slides 13, 15. Show: ch7 (plus a live demo if a demo account exists). Do: task 5 in the named tool or, if there is none, on paper or a simulation copying ch7's form, marked "simulated"; switch views on slide 15. Tell/Show: slide 14 and ch8 (pause at 5:36). Do: task 6. Review: slide 21; partner checks the five fields. | 13, 15, 14, 21 | ch7 4:17–4:58; ch8 4:58–5:44 | Tasks 5, 6 | Task 5 stays achievable without accounts. |
| 95–103 | P → P → E | **Cycle E, automation and help.** Tell: slide 16. Show: ch9 plus live Word "teh" + space → "the", then Ctrl + Z. Do: task 8 part 1 with the "teh" trigger, part 2 help search. Review: partner gives one specific piece of feedback (the rest of task 8). | 16, 19 (17 as a 1-minute Tell) | ch9 5:44–6:25 | Task 8 | **Slide 17 (cloud):** a 1-minute Tell with one oral question, or **move** to the week 2 files block. |
| 103–113 | E | **Review, individual.** Watch ch10, then each learner performs 3 items for a partner while the instructor circulates and records ratings: (1) zoom and reset; (2) select the headset and test; (3) preview page 1 on the correct printer. Mark Independent / With prompt / Needs practice on a class roster. | — | ch10 6:25–7:08 | Roster | Re-model only the missing step. |
| 113–120 | A | Transfer and close | 23, 24 | — | Print or save the worksheet | Home task on the learner's own device, reported at week 2 Reconnect. Restore lab settings. |

Timing check: 10 + 25 + 3 + 12 + 10 + 10 + 10 + 15 + 8 + 10 + 7 = 120 minutes.

**Moved or optional**
- The separate 80–110 lab is dissolved into cycles A–E. Remaining lab time goes to catch-up and extensions.
- Slide 18 becomes the chapter launcher, not a block.
- Slide 9 and ch5: optional, or home review.
- Slide 17: brief, or moved to week 2.
- Slide 8: projector Show only, plus an extension task.

## Top 10 changes, ranked

| # | Change | Where | Why (Tell/Show/Do/Review, WIPPEA or andragogy) | Effort | Source file to edit |
|:--|:--|:--|:--|:--|:--|
| 1 | Replace the 7-row agenda with five skill cycles (see Recommended restructure). Name the slides, chapters (with pause times) and worksheet tasks for each cycle. | Lesson plan agenda; slide 18 role | Each skill gets its own Tell → Show → Do → Review; WIPPEA mastery before moving on; chunking for older learners | Medium | `scripts/dl2/author-content.py` week 1 `agenda` (line 11) → `curriculum.json`; `build-pages.py` "Using the chaptered video" text (~line 96) |
| 2 | Every learner does each core task on their own workstation right after its Show. Replace "Partners switch driver and coach roles halfway" with "partner coaches, never takes over". | Lesson plan 80–110; worksheet intro | The Do must be each learner's own; self-concept; practice moves from guided to independent | Small | `author-content.py` week 1 agenda; `build-pages.py` facilitation text |
| 3 | Make task 5 doable: add an event-creation practice using ch7's "Practice Calendar" form (title, day, start/end, location, reminder, Save, reopen), or name the calendar tool and account source. | Slide 13; task 5; plan prep | The Do is missing for objective 2; High correctness item | Medium | `scripts/dl2/workshops.py` (new kind; `MAP[1][13]`); reuse `screen-share-scenes.py` calendar states; `author-content.py` `lab[4]` |
| 4 | Add real click paths to the Show for the lab stack (Windows 11 + Edge/Chrome), as a per-week "lab quick card". Cover: zoom and Ctrl + 0, Display > Scale, Accessibility > Text size, Sound output and Volume mixer, monitor brightness buttons, Downloads location, Site permissions, Printers & scanners (default and status), Ctrl + P, Outlook and Google free/busy. | Slides 5, 7, 8, 11, 12, 14; lesson plan | The Show must be the same task as the Do; content correctness; fixes CP-03 | Medium | `author-content.py` (new `lab_paths` key or slide bodies); `build-pages.py` plan template |
| 5 | Rewrite the objectives in ABCD form and add the two missing ones (1.3 automation/cloud, 2.3 help/feedback). Design the checks first (backward design). | Slide 1; lesson plan outcomes | WIPPEA Introduction and Evaluation; need to know | Small | `author-content.py` week 1 `objectives` |
| 6 | Rebuild the Evaluation: a short Review at the end of each cycle, a final 3-item individual checklist with a class roster, and a printing knowledge check. Replace throwaway wrong answers with believable ones (slide 20: "Raise the volume slider", "Restart the computer"; slide 21: "Share titles and locations", "Share all details"). | Slides 20–21; answer guide; 110–120 | WIPPEA Evaluation; Review checks each learner; respectful tone (self-concept) | Small–medium | `author-content.py` week 1 check slides and `answers`; `build-pages.py` answer-key and plan |
| 7 | Warm-up that uses DL1: real HDMI, USB and Ethernet cables plus memory-versus-storage recall; use slide 2 answers later. Mark slide 9 and ch5 optional. | 0–10; slides 2, 9, 10 | WIPPEA Warm-up; the experience principle | Small | `author-content.py` week 1 agenda and slide 2 body; plan prep list |
| 8 | Fix the correctness items: default printer (slide 11 plus how to set one); laser versus inkjet use cases; where brightness and contrast controls are, plus Contrast themes (slide 7); home page versus startup (slide 8); USB-A power (slide 10); "rule… repeat a reminder" (slide 16 and the post-test 1.3 wording); note that zoom is remembered per site. | Slides 7, 8, 10, 11, 16 | Tell must be accurate; content correctness | Small | `author-content.py` slide bodies and cards; `photo_scenes.py` (1,7), (1,8), (1,11), (1,16); `author-assessments.py` post 1.3 |
| 9 | Fix task inputs: list the three connection tasks (task 4); name the page to preview, for example "page 1 of this worksheet" (task 7); give the "teh" + space trigger with Ctrl + Z (task 8); state whether a test print is allowed. | Worksheet and answer guide | Do must be possible and reliable; readiness | Small | `author-content.py` week 1 `lab` and `answers` |
| 10 | Video and plan polish. Add pause cues to the plan (1:18, 2:02, 5:36, 6:28) or 3–5 seconds of silence before answers. Add a connector beat to ch5 (3:14–3:31). Change ch7 "Tuesday, October 13" to Monday. Match ch4's caption order to the narration. Remove the week 6 sentence and "spreadsheet" from the week 1 prep; list headphones, cables, a one-page file and the calendar tool. Add a home-device transfer task. | Video ch4, ch5, ch7; lesson plan prep; slides 23–24 | Show quality and think time (Knowles: time to try); WIPPEA Application | Small (plan) / medium (re-render) | `build-pages.py` ~line 90 (prep); `author-content.py` (a per-week `prep` key); `scripts/dl2/video-scenes.py` lines 18–19; `scripts/dl2/screen-share-scenes.py` lines 69, 83; then rebuild media |
