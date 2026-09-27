# Week 5 structure and content review (Tell, Show, Do, Review + WIPPEA + adult learning) — Claude

Scope: Digital Literacy Level 2, week 5 "Protect your work and show your skills", class Monday 2026-10-26. Reviewed read-only against `vublessons` `main` at 9270815 (after the week 1 Tell, Show, Do, Review merge). Week 5 content has not changed since the 2026-09-26 full review, apart from the pre-cohort fixes (the selected phishing clue is now readable: `workshop.css` `.message-preview button.inspected{…;color:#1b365d}`).

Conventions:
- Slide numbers are as learners see them (slide 1 = title, 20 slides).
- Lesson-plan minutes come from `weeks/week-05/lesson-plan.html` (generated from `scripts/dl2/author-content.py` week 5 `agenda`, line 120).
- Video times are m:ss in `media/week-05.mp4` (7:31). Chapter starts: ch1 0:00, ch2 0:42, ch3 1:27, ch4 2:09, ch5 2:50, ch6 3:38, ch7 4:19, ch8 5:02, ch9 5:54, ch10 6:43.
- Pause points are the ends of the prompt sentences from the narration word timings: 1:23 (ch2), 2:43 (ch4, answer 0.5 s later), 3:36 (ch5), 4:55 (ch7), 6:13 (ch9, answer 0.7 s later). I re-checked each against `week-05.vtt`.
- 45 frames were extracted at the start, middle and end of every chapter, at all 10 screen-share actions (ch4 and ch7) and at the moments the Gemini reviews cite. Each was inspected. They are in `scratchpad/video-eval/w5frames-claude/` (tiled in `grids/`).

## Verdict

**Week 5 is teachable on 2026-10-26, but not as written.** The safety content is mostly accurate and well chosen for this audience. The day's shape is the problem: one long Tell, a short practice that is mostly the video, and a skills challenge that cannot produce the individual ratings it asks for.

**Strengths**
- The topics matter to these learners now: urgent messages, fake identities, unknown USB drives, camera permissions, file protection.
- Two good screen demonstrations: ch4 (leave the message, open a saved bookmark, use Contact, verify with a fictional number) and ch7 (allow for a meeting, block for a text page, review the permission).
- Three working simulations: slide 8 (inspect subject, sender and link), slide 10 (original, read-only, encrypted), slide 13 (allow or deny the camera).
- A repeatable routine in ch1: pause, inspect the evidence, verify independently.
- Respectful framing of the post-test: "one piece of evidence, not a judgment" (ch10; slide 19).

**Problems**
- **Big blocks, not cycles.** 11 teaching slides (3–13) in 20 minutes, then 15 minutes of "scenario practice" that must also hold the 7:31 video. Worksheet tasks 1–6 have no scheduled time at all.
- **The Do is mostly writing.** Tasks 1–6 ask learners to "define" or "explain". The simulations on slides 8, 10 and 13, the best practice in the deck, are named in no phase.
- **The skills challenge cannot do its job.**
  - Pairs cannot show "Independent" performance.
  - One instructor cannot rate 7 rows for about 12 learners (84 ratings) in 25 minutes.
  - Row 4 opens "supplies.csv from week 3". Week 3 task 5 changed paper to 15, so a saved file shows 28, not the expected 25. A shared lab machine may not keep the file at all.
  - Row 3 asks for a "bulleted" list of steps; week 3 taught numbered lists.
  - Nothing records the ratings: the radio buttons live on the learner's page and are not saved (IR-15).
- **Two knowledge checks, both on devices and files, placed directly before the post-test.** Slide 17 is nearly word for word post-test item 27. One option is a throwaway ("Share your password instead").
- **Gaps against the week's own topics:** no software updates, no account protection after a scam (change the password, two-step verification), no lock-the-screen habit, and no encryption methods named (GS6 7.3.2).

**Correctness:** 0 High, 5 Medium, 11 Low. Nothing on the slides would harm a learner. The Medium items:
- The challenge's CSV row: a stale week 3 file, and a .csv file that keeps the result, not the formula.
- Password-to-open is presented as separate from encryption, but in Word it *is* encryption ("Encrypt with Password").
- Slide 11 implies a password "recovery method"; Word cannot recover a lost document password.
- Software updates and account recovery are missing, even though the lab's own PCs run Windows 10 (support ended October 14, 2025).

**For Monday:** use the running order below: three short cycles, then a 5-row individual challenge, a break, the post-test and a real close. Replace the slide 17 question, fix the challenge rows, and put a paper roster on your clipboard.

## WIPPEA map

| Stage | Where it happens | Rating | Evidence | What to change |
|:--|:--|:--|:--|:--|
| **W — Warm-up** | 0–10 "Retrieve and preview"; slide 2 not scheduled | **Adequate** | <ul><li>"Name a source check, a file permission and a useful feedback habit" recalls weeks 2–4, which prepares the challenge.</li><li>Nothing points toward today's topic. Week 2 already taught "Read-only is not encryption" and week 4 taught multifactor authentication; neither is used.</li><li>No Reconnect of last week's home task.</li></ul> | <ul><li>Reconnect (week 4 home task).</li><li>Recall read-only vs encryption (week 2) and two-step verification (week 4).</li><li>Pair share on slide 2; ask who has had an urgent text or email.</li></ul> |
| **I — Introduction** | Slide 1 objectives; ch1 (0:00–0:42) not scheduled | **Adequate** | <ul><li>Objectives are in writing, next to a phishing simulation.</li><li>They are not measurable, and comfort, universal design and attention (slides 3–5, GS6 7.1, 7.2.2) sit in no objective.</li><li>"Complete the parallel post-test" is an activity, not a learning outcome.</li><li>Nobody tells learners the day has two halves: new habits, then showing what they can do.</li></ul> | <ul><li>Four ABCD objectives (below).</li><li>Play ch1 as the bridge; name the routine.</li><li>Say how the day runs.</li></ul> |
| **P — Presentation** | 10–30 "Safety model": slides 3–13 (11 slides) | **Adequate** content, **Weak** pacing | <ul><li>About 1.8 minutes per slide, including three simulations and a flip-card slide.</li><li>"Phishing" (slide 8) and "malicious software" (slide 12) are used without a definition; slide 4 never defines universal design, though task 2 asks learners to.</li><li>No check of understanding is planned inside the block.</li><li>The video is not placed; the plan says only "Use the flip cards and explainer".</li></ul> | <ul><li>Teach one skill group at a time, each with its own chapter as the Show.</li><li>Define the terms on first use.</li></ul> |
| **P — Practice** | 30–45 "Scenario practice"; worksheet tasks 1–6 (no time) | **Weak** | <ul><li>15 minutes must hold the 7:31 video plus flip cards, which leaves about 7 minutes of learner activity.</li><li>Tasks 1–6 are written explanations; none uses the slide 8, 10 or 13 simulations, Windows or Edge.</li><li>No instructor model is planned.</li></ul> | <ul><li>Every learner does each Do at their own seat right after its Show.</li><li>Make tasks 2, 3, 5 and 6 hands-on (captions and Tab, inspect the message, look at real settings, open Word's Protect Document).</li></ul> |
| **E — Evaluation** | 55–80 performance challenge (pairs, 7 rows); 80–105 post-test; slides 16–17 (not scheduled) | **Adequate**: post-test strong, challenge **weak** | <ul><li>The post-test is individual and covers all seven domains.</li><li>The challenge is done "with a partner", so a rating cannot show individual performance.</li><li>84 ratings in 25 minutes is about 18 seconds per rating while also answering questions.</li><li>No roster; the page's radio buttons are not saved (IR-15).</li><li>Both knowledge checks test objective 1; nothing checks the scam objective in class.</li><li>Slide 17 rehearses post-27 one slide before the test (AS-08).</li></ul> | <ul><li>Individual 5-row challenge, one visit per learner, paper roster.</li><li>Knowledge checks inside cycle C; ch9 as the scam Review.</li><li>A new slide 17 question.</li></ul> |
| **A — Application** | 105–120 "Review and next steps"; slides 19–20; ch10 | **Adequate** | <ul><li>Slide 19 turns results into a learning plan and says the score is not certification.</li><li>No home task, and nothing asks learners to check their own devices.</li><li>Week 6 has no follow-up of week 5.</li></ul> | Home task: check for updates or turn on two-step verification for one account; report at week 6 warm-up. |

**Overall flow.** W → Tell (20) → mixed video/flip cards (15) → break → challenge (25) → post-test (25) → review (15).
- No objective gets presentation → practice → check before the next one starts.
- The video is one asset in one block, not the Show inside each cycle.
- The knowledge checks (16–17) sit immediately before the post-test (18), so they work as a rehearsal, not as a check that can lead to re-teaching.
- The challenge and the post-test run back to back: 50 minutes of assessment with no break for older learners.

## Tell, Show, Do, Review by skill

| Skill | Tell (where) | Show (where) | Do (where; minutes available) | Review (where) | Missing or weak steps |
|:--|:--|:--|:--|:--|:--|
| Decision routine (pause, inspect, verify) | ch1 0:00–0:42; slide 2 | ch1 diagram (Evidence → Verify → Safer action) | Embedded in scenarios | ch9 (6:05–6:13 prompt) | ch1 not scheduled; ch9's prompt is answered 0.7 s later. |
| Workstation comfort (7.1.1) | Slide 3; ch2 0:42–1:27 | Slide 3 photo hotspots (Screen, Input, Break); ch2 icon diagram | Task 1 (no time) | Answer guide only | No live Show; slide gives no concrete setup (OSHA: 20–40 in., top at or slightly below eye level). |
| Universal design (7.1.3) | Slide 4 (not defined); ch2 | Slide 4 scene (captions, keyboard, labels) | Task 2 "Define…" | Answer guide; post-25 | The Do is a definition. Captions and Tab work in the lab without any setup. |
| Attention / FOMO (7.2.2) | Slide 5; ch8 5:02–5:54 | Slide 5 scene; ch8 panel with "Choose alerts" three times (placeholder, frames 5:05, 5:28, 5:50) | Task 4 "Explain" | Post-26 only | No Show of Windows notification settings or Do not disturb. |
| Catfishing (7.2.1) | Slide 6; ch8 | Slide 6 scene | Task 4 "Explain" | Pre-26 only | Fine as a decision; add the money rule (FTC). |
| Harmful posts (7.2.3) | Slide 7; ch8 | Slide 7 scene | Task 4 "Explain" | None | Fine as a decision. |
| Phishing and independent verification (7.1.2) | Slides 1, 8; ch3 1:27–2:09 | Slide 8 simulation (inspect subject, sender, link); **ch4 2:09–2:50 screen demo** (strong) | Task 3 "write a plan" (no time); slide 9 card 3 | None in class (no knowledge check); ch9 prompt with no think time | Strong Show; the Do is unscheduled and the check is missing. No "what if I already typed my password" step (Microsoft: change it, turn on MFA). |
| Unknown USB media (7.3.1) | Slide 12; ch6 3:38–4:19 | Slide 12 scene; ch6 photo and diagram | Slide 9 card 1; task 5 | Pre-27 only | Adequate as a decision; hold up a real drive (never plugged in). |
| Camera and microphone permissions (7.3.3) | Slide 13; ch7 4:19–5:02 | Slide 13 simulation; **ch7 screen demo** (strong) | Slide 9 card 2; task 5 | Slide 17 knowledge check (rehearses post-27) | No real Edge or Windows setting shown. |
| Encryption vs read-only (7.3.2, 4.2.4) | Slide 10; ch5 2:50–3:38 | Slide 10 simulation | Task 6 "Explain" | Slide 16 knowledge check | No encryption methods named (BitLocker, Device encryption, FileVault). |
| File passwords (7.4.1, 4.2.5) | Slide 11; ch5 | Slide 11 scene | Task 6 | None | No Show of Word's Protect Document menu; "recovery" is misleading. |
| Updates, account protection, locking | — | — | — | — | Missing. GS6 7.3 is device security; week 5 claims group 2.1 (manage credentials) but never teaches it (CP-10). |
| Skills challenge (weeks 2–4 skills) | — | — | 25 min, in pairs, 7 rows | Instructor ratings: 84 in 25 min, no roster | Invalid individual ratings; row 4 file state; row 3 "bulleted"; slide 15 does not describe the challenge (CP-26). |
| Post-test | Slide 18 | — | 25 min | Results report; slide 19 | Sound, but slides 16–17 and the challenge's row 4 and row 6 rehearse items 27, 14 and 23 minutes before it. |

**Week 5 runs as big blocks, not short cycles.** The Tell for 11 slides sits in one 20-minute block, the video and flip cards in one 15-minute block, and the written Do has no time. For older learners who need time to read, try and ask:
- They hold six safety decisions in memory for up to 35 minutes before any practice.
- The strongest practice (slides 8, 10, 13) may never be used.
- Mistakes surface only on the post-test, when nobody can re-teach.

## Objectives

GS6 Level 2 groups claimed: 7.1, 7.2, 7.3, 7.4, 2.1, 4.2.

**1. "Explain device, file and account protections."**
- **ABCD rewrite (Devices and files):** Using slide 9, Edge settings, Windows Update and Word's Protect Document menu without changing anything, each learner:
  - chooses safe responses to an unknown USB drive and an unneeded camera request;
  - says why updates matter;
  - tells a password to open (encryption) apart from read-only;
  - says what device encryption protects and when to lock the screen.

  Degree: both knowledge checks correct.
- **Taught:** slides 10–13; ch5–7. **Practised:** tasks 5–6 (written). **Evaluated:** slides 16–17; post 27–28.
- **Status:** Partly met. "Account" protection is in the title but not taught (no passwords, MFA or locking).

**2. "Recognize manipulation and choose a safe next step."**
- **ABCD rewrite (Scams):** Given the fictional message on slide 8, each learner:
  - names two warning signs;
  - names an independent check that does not use the message's link or number;
  - says what to do after typing a password;
  - gives a safe next step for a catfishing request, fear of missing out and a hurtful post.

  Degree: no more than one prompt.
- **Taught:** slides 5–9; ch3, ch4, ch8, ch9. **Practised:** tasks 3–4 (unscheduled). **Evaluated:** post 26 only. No in-class check.
- **Status:** Taught well, practised thinly, never checked in class.

**3. "Demonstrate core tasks and complete the parallel post-test."**
- **ABCD rewrite (Skills challenge and post-test):** Working alone, each learner completes five challenge rows (refined search, structured paragraph, formula total, undo recovery, useful feedback), each rated Independent, With prompt or Needs practice. They then complete the 28-question post-test and record the score and one next practice task.
- **Status:** As written, the paired format makes the ratings invalid, and "complete the post-test" is an activity rather than an outcome. The rewrite makes the evidence individual and observable.

**Missing objective (taught but not stated): comfort, access and attention (7.1.1, 7.1.3, 7.2.2).**
- **Proposed (Comfort and access):** At a lab workstation, each learner makes one comfort change (chair, screen distance, text size or Magnifier) and says what it made easier. They then name two universal design features and who each helps. The change is visible, and settings are restored afterwards.
- **Taught:** slides 3–5, ch2. **Practised:** tasks 1–2. **Evaluated:** post-25, post-26.

**Backward design.** The "Evidence to collect" list copies the worksheet; it was not designed first. The challenge was designed as evidence, but its paired format cannot produce individual evidence, and its decision rows (source, sharing) duplicate what post-test items 10, 11 and 22 already measure. The rewrite keeps only performance rows that the multiple-choice test cannot see.

## Adult learning principles

| Principle | Rating | Evidence | Improvement |
|:--|:--|:--|:--|
| 1. Need to know | Adequate | <ul><li>Slide 2 frames safety as decisions; ch1 starts from everyday requests; slide 9 card 3 "A message demands payment to keep benefits" is directly relevant.</li><li>Otherwise the examples are generic ("your service will stop").</li></ul> | Use verified real-world anchors: VA says it never charges a fee to apply for benefits and never threatens by email; the FTC warns that romance scammers use stolen photos of real military personnel; Windows 10 lost free security updates on October 14, 2025. |
| 2. Self-concept | Adequate | <ul><li>Learners choose a control (ch2) and a next practice (slide 19); the score is framed as "not a judgment".</li><li>Throwaway options ("Always allow every request", "Share your password instead") talk down.</li><li>The paired challenge denies each learner the chance to show independent skill.</li></ul> | Believable wrong answers; an individual challenge where the quick card counts as Independent. |
| 3. Experience | Adequate | <ul><li>The warm-up recalls weeks 2–4.</li><li>Week 2 (read-only vs encryption) and week 4 (MFA) taught overlapping content that week 5 never references.</li><li>Learners' own experience of scam calls and texts is not invited.</li></ul> | Recall both; invite stories without private details. Optional: compare verification in the service (challenge and password) with checking a caller. |
| 4. Readiness | **Strong** | Scams, permissions and file protection are real risks for this group now. | Add updates: many older adults still run Windows 10 at home. |
| 5. Orientation (problem-centred) | Adequate | <ul><li>Flip cards and simulations are problem-framed.</li><li>Tasks 1–6 are subject-centred ("Define universal design", "Explain device encryption…").</li></ul> | Make the Do a task: inspect, look, choose, then write the evidence. |
| 6. Motivation | **Strong** | Results become a learning plan; "not certification"; ch10 "confidence grows from being able to explain and repeat". No home task. | Add a home task that protects the learner's own account or device. |

## Content correctness

| # | Where | What it says | What is correct (source) | Severity |
|:--|:--|:--|:--|:--|
| 1 | Challenge row 4; agenda 55–80 | "Open supplies.csv from week 3." "Keep supplies.csv from week 3 open on each workstation." | Week 3 task 5 says "verify 25, then change paper to 15 and verify 28" (`author-content.py` week 3 `lab`). A learner who saved that file now sees 28, not the expected 25. Shared lab machines may not keep the file. The worksheet already has a "Practice workbook data" download button (`build-pages.py` line 90). Use a fresh copy. | Medium |
| 2 | Challenge row 4 evidence | "The cell holds the formula, not a typed number." | A .csv file is plain text. Week 3's own slide says "CSV carries simple table data but loses formatting and formulas." Microsoft: saving in a text format removes formatting and "saves only the active sheet" ([Microsoft](https://support.microsoft.com/en-us/office/save-a-workbook-to-text-format-txt-or-csv-3e9a9d6c-70da-4255-aa28-fcacf1f081e6)). The formula works while the file is open, so the instructor must check it before the file is closed. | Medium |
| 3 | Slides 10–11; task 6 ("without treating them as identical"); ch5 3:11–3:15 ("do not assume every password prompt means the file is encrypted") | Presents file passwords and encryption as different things. | True for a password to modify. But in Word, File › Info › Protect Document › **Encrypt with Password** is the password to open, and it encrypts the file ([Microsoft](https://support.microsoft.com/en-us/office/add-or-remove-protection-in-your-document-workbook-or-presentation-05084cc3-300d-4c1a-8416-38d3e37d6826)). As written, learners may conclude a file password never encrypts. Read-only "doesn't prevent someone from making a new copy" ([Microsoft](https://support.microsoft.com/en-us/word/make-a-document-read-only-in-word)). | Medium |
| 4 | Slide 11 body; scene (5,11) | "Check which protection is enabled and how recovery works." Scene: "Recovery: Keep recovery method separately." | "If you lose or forget your document password, Word won't be able to recover it for you" ([Microsoft](https://support.microsoft.com/en-us/office/add-or-remove-protection-in-your-document-workbook-or-presentation-05084cc3-300d-4c1a-8416-38d3e37d6826)). There is no recovery method to keep. | Medium |
| 5 | Whole week | No software updates; the "if you already acted" advice (ch4 2:26) does not mention changing the password or MFA; the week claims group 2.1 (manage credentials) but teaches none of it (CP-10). | <ul><li>Windows 10 support ended October 14, 2025: no security updates or fixes ([Microsoft](https://support.microsoft.com/en-us/windows/windows-10-support-has-ended-on-october-14-2025-2ca8b313-1946-43d3-b55c-2b95b107f281)).</li><li>Consumer Extended Security Updates cover enrolled PCs until October 12, 2027 (free with PC settings sync, 1,000 Rewards points, or $30) ([Microsoft](https://www.microsoft.com/en-us/windows/extended-security-updates)).</li><li>Edge keeps updating on Windows 10 22H2 until at least October 2028 ([Microsoft Learn](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-supported-operating-systems)). Microsoft 365 apps get security updates on Windows 10 until October 10, 2028.</li><li>After responding to a phish, Microsoft advises changing the passwords of affected accounts right away and enabling multifactor authentication where available ([Microsoft](https://support.microsoft.com/en-us/windows/protect-yourself-from-phishing-0c7ea947-ba98-3bd9-7184-430e1f860a44)).</li><li>The lab PCs themselves run Windows 10, so learners will ask.</li></ul> | Medium |
| 6 | Slide 10 | "Encryption scrambles data so a key is needed…" No methods named. | GS6 7.3.2 asks learners to "identify encryption methods". Device encryption enables BitLocker; BitLocker is on Pro, Enterprise and Education; Device encryption also runs on Home ([Microsoft](https://support.microsoft.com/en-us/windows/device-encryption-in-windows-cf7e2b6f-3e70-4882-9532-18633605b7df)). Mac: FileVault ([Apple](https://support.apple.com/guide/mac-help/protect-data-on-your-mac-with-filevault-mh11785/mac)). HTTPS encrypts the connection but does not make a site trustworthy ([Google](https://support.google.com/chrome/answer/95617)). | Low |
| 7 | Slides 8, 12, 4 | "may be phishing"; "malicious software"; "Universal design helps more people" | None of the three is defined; task 2 asks learners to define universal design (CP-11). | Low |
| 8 | Challenge row 3 | "a three-step bulleted list" | Week 3 taught numbered lists for steps (task 2). Word: Home › Numbering ([Microsoft](https://support.microsoft.com/en-us/office/create-a-bulleted-or-numbered-list-9ff81241-58a8-4d88-8d8c-acab3006a23e)) (CP-22). | Low |
| 9 | Slide 13 simulation; ch7 4:20–4:42 | Two-button "Block / Allow" prompt | Chrome: "choose Allow while visiting the site, Allow this time, or Never allow" ([Google](https://support.google.com/chrome/answer/2693767)). The "menus vary" footer partly covers it (VM-15). | Low |
| 10 | Slide 3 | "Place the screen where you can read without strain." | Correct but vague. OSHA: 20–40 inches from the eyes, top of the monitor "at or slightly below eye level" ([OSHA](https://www.osha.gov/etools/computer-workstations/components/monitors)). | Low |
| 11 | Slide 4 scene | "Keyboard route: Tab: Search, Tab: Filter, Enter: select action" | This is the example page's order; tab order differs by page. Label it as an example (Gemini). | Low |
| 12 | ch10 6:43–7:31 | "review the skills you can demonstrate: adjust a setting and check it, justify a source, choose file access, test a calculation…"; bars "Settings / Files / Communication" | Never says "challenge"; the list does not match the rows, and the bars do not match the report's seven domains (VM-08). | Low |
| 13 | ch8 5:02–5:54 | Notification panel reads "Choose alerts" three times | Placeholder (frames 5:05, 5:28, 5:50) (VM-11). | Low |
| 14 | Lesson plan "Prepare the room" | Headphones, "a word processor and spreadsheet app", "fictional accounts… for cloud tasks", printer destination | Week 5 has no cloud or print task. It needs Word and Excel, a USB prop, a paper roster and the week 1 scores. | Low |
| 15 | Slides 16–17 | "Make every message trustworthy"; "Always allow every request"; "Share your password instead" | Not believable misconceptions (CP-08, AS-11). "Make a file smaller" is a real one (compression), so keep that idea. | Low |
| 16 | ch4 2:15 | "Use Contact on the known website" | Fine. Many sites label it Help or Support, so say "Contact or Help" (Gemini). | Low |

**Totals:** High 0, Medium 5, Low 11.

**Verified as correct**
- **Phishing signs and the independent check (slides 1, 8; ch3–4):** urgency and threats, mismatched sender or link, hover to see the real address, contact the organization "using official phone numbers or websites" ([Microsoft](https://support.microsoft.com/en-us/windows/protect-yourself-from-phishing-0c7ea947-ba98-3bd9-7184-430e1f860a44)); "contact the company using a phone number or website you know is real — not the information in the email" ([FTC](https://consumer.ftc.gov/articles/how-recognize-and-avoid-phishing-scams)). Ch4's advice not to use the message's own number is right.
- **Benefits-fee scam (slide 9 card 3):** VA: "We'll never charge you any fees to apply for VA benefits or health care", and never asks for personal information or pressures you in an email ([VA](https://www.va.gov/resources/how-to-protect-your-identity-and-your-va-benefits-from-scammers/)).
- **Unknown USB drives (slides 9, 12; ch6):** "Do not plug an unknown USB drive into your computer… give it to the appropriate authorities" ([CISA](https://www.cisa.gov/news-events/news/using-caution-usb-drives)).
- **Camera permissions (slide 13; ch7):** Windows Settings › Privacy & security › Camera, and Edge site permissions, where a site can be set to Block ([Microsoft](https://support.microsoft.com/en-us/windows/windows-camera-microphone-and-privacy-a83257bc-e990-d54a-d212-b5e41beba857)); Chrome Site settings › Camera ([Google](https://support.google.com/chrome/answer/2693767)).
- **Read-only vs encryption (slide 10 simulation; ch5):** read-only restricts changes, and the content stays readable ([Microsoft](https://support.microsoft.com/en-us/word/make-a-document-read-only-in-word)). Mark as Final "is not a security feature" ([Microsoft](https://support.microsoft.com/en-us/office/help-prevent-changes-to-a-final-version-of-a-file-b1af610f-f172-42c9-85fc-a178a503cc81)).
- **Catfishing (slide 6; ch8):** fake profiles, "sometimes using photos of other people — even stolen pictures of real military personnel" ([FTC](https://consumer.ftc.gov/features/pass-it-on/impersonator-scams/romance-scams)); "Never send money or gifts to a sweetheart you haven't met in person" ([FTC](https://consumer.ftc.gov/articles/what-know-about-romance-scams)).
- **Harmful posts (slide 7; ch8):** don't respond, keep evidence, block, report ([StopBullying.gov](https://www.stopbullying.gov/cyberbullying/how-to-report); the page returned 403 to the fetch tool; wording confirmed from the site's search listing).
- **Notifications (slide 5):** Settings › System › Notifications; the bell with zZ turns on Do not disturb ([Microsoft](https://support.microsoft.com/en-us/windows/change-notification-settings-in-windows-8942c744-6198-fe56-4639-34320cf9444e)).
- **Challenge evidence:** a SUM formula stays visible in the formula bar ([Microsoft](https://support.microsoft.com/en-us/excel/functions/sum-function)); a Commenter can view and comment but not edit ([Google](https://support.google.com/docs/answer/2494822)); "You can undo changes, even after you have saved… as long as you are within the undo limits" ([Microsoft](https://support.microsoft.com/en-us/office/undo-redo-or-repeat-an-action-84bdb9bc-4e23-4f06-ba78-f7b893eb2d28)); version history "only works for files stored in OneDrive or SharePoint" ([Microsoft](https://support.microsoft.com/en-us/office/collab-files/view-previous-versions-of-office-files)). The lab has no OneDrive, so the recovery row must use Undo.
- **Knowledge checks:** the keyed answers on slides 16 and 17 are correct.
- **Post-test framing (slides 18–19; ch10):** "not certification" is accurate.

### Lab quick card: verified steps and sources

Windows 11 and Edge, as the instructor chose. Tasks learners do on the Windows 10 lab PCs give the Windows 10 path too (Windows Update is the only place the two differ in this week's Do).

| Row | Steps (summary) | Source |
|:--|:--|:--|
| Zoom in with Magnifier | Windows logo key and + ; close with Windows logo key and Esc (same on Windows 10) | [Keyboard shortcuts in Windows](https://support.microsoft.com/en-us/windows/keyboard-shortcuts-in-windows-dcc61a57-8ff0-cffe-9796-cb9706c75eec) |
| Quiet your notifications | Start › Settings › System › Notifications; bell with zZ = Do not disturb | [Change notification settings](https://support.microsoft.com/en-us/windows/change-notification-settings-in-windows-8942c744-6198-fe56-4639-34320cf9444e) |
| See where a link really goes | Point without clicking; read the address | [Protect yourself from phishing](https://support.microsoft.com/en-us/windows/protect-yourself-from-phishing-0c7ea947-ba98-3bd9-7184-430e1f860a44) |
| Report a phishing email | Outlook.com: Report › Report phishing. Gmail: More › Report phishing | [Outlook](https://support.microsoft.com/en-us/outlook/mail/phishing-and-suspicious-behavior-in-outlook); [Gmail](https://support.google.com/mail/answer/8253) |
| Turn on two-step verification (at home) | account.microsoft.com/security › Manage how I sign in › Two-step verification › Turn on | [Microsoft account](https://support.microsoft.com/en-us/account-billing/how-to-use-two-step-verification-with-your-microsoft-account-c7910146-672f-01e9-50a0-93b4585e7eb4) |
| Check for Windows updates | Start › Settings › Windows Update › Download & install. Windows 10: Update & Security › Windows Update | [Install Windows updates](https://support.microsoft.com/en-us/windows/install-windows-updates-3c5ae7fc-9fb6-9af1-1984-b5e0412c556a) |
| Review which websites can use your camera | Edge Settings › search "permissions" › Camera. Official path: Privacy, search, and services › Site permissions; the label varies by build, hence the search box | [Windows camera, microphone, and privacy](https://support.microsoft.com/en-us/windows/windows-camera-microphone-and-privacy-a83257bc-e990-d54a-d212-b5e41beba857) |
| Lock the computer | Windows logo key and L (same on Windows 10) | [Keyboard shortcuts in Windows](https://support.microsoft.com/en-us/windows/keyboard-shortcuts-in-windows-dcc61a57-8ff0-cffe-9796-cb9706c75eec) |
| Require a password to open a Word file | File › Info › Protect Document › Encrypt with Password; Word cannot recover it | [Add or remove protection](https://support.microsoft.com/en-us/office/add-or-remove-protection-in-your-document-workbook-or-presentation-05084cc3-300d-4c1a-8416-38d3e37d6826) |
| Stop changes but not reading | Protect Document › Always Open Read-Only, or Review › Restrict Editing | [Make a document read-only](https://support.microsoft.com/en-us/word/make-a-document-read-only-in-word) |
| Check device encryption | Start › Settings › Privacy & security › Device encryption; missing = unsupported or standard user | [Device encryption in Windows](https://support.microsoft.com/en-us/windows/device-encryption-in-windows-cf7e2b6f-3e70-4882-9532-18633605b7df) |
| Bring back something you just deleted | Ctrl and Z (works after saving, until closing); OneDrive file: file name › Version history | [Undo](https://support.microsoft.com/en-us/office/undo-redo-or-repeat-an-action-84bdb9bc-4e23-4f06-ba78-f7b893eb2d28); [Version history](https://support.microsoft.com/en-us/office/collab-files/view-previous-versions-of-office-files) |
| Total a column in Excel | =SUM(B2:B5), Enter; the formula shows in the formula bar | [SUM function](https://support.microsoft.com/en-us/excel/functions/sum-function) |

**Not used, on purpose:** Windows Live captions (Windows logo key + Ctrl + L) is "available in Windows 11, version 22H2 and later" ([Microsoft](https://support.microsoft.com/en-us/windows/use-live-captions-to-better-understand-audio-b52da59c-14b8-4031-aeeb-f6a47e6055df)), so it will not work on the Windows 10 lab PCs. The course video's own captions are used instead.

### Post-test rehearsal check (AS-08)

The post-test questions are out of scope. These week 5 items rehearse a post-test item nearly word for word, or with the same numbers, minutes before the test:

| Week 5 material | Post-test item | Overlap | Proposed action |
|:--|:--|:--|:--|
| **Slide 17 knowledge check:** "A simple text webpage asks to use your camera… Deny access when it is not needed for the task" | **post-27:** "A webpage that only displays a written community schedule asks to use your camera… Deny camera access because the permission does not fit the task" | Near word for word; slide 17 is the slide right before "Take the post-test" | Replace with a new question: reviewing a clinic site's permission after a video visit (slide_changes). |
| Slide 13 simulation ("A text-only resource page wants camera access"); ch7 demo ("reading.example · Plain text article → Block") | post-27 | Same scenario, paraphrased | Keep as teaching; the post-test rewrite should use a different permission or situation. |
| Slide 10 body: "an unlocked signed-in session still needs protection"; ch5 3:23–3:28 "That does not remove the need to manage who can access an unlocked device or account" | **post-28 key:** "Lock the session so another person cannot use the open account" (the pre-28 explanation says the same) | Restates the key | The idea must be taught. The proposed wording differs ("a signed-in computer is open to anyone at the keyboard… Windows logo key and L"); post-28 needs a new situation. |
| Slide 5 body: "Adjust notifications and choose a stopping point"; ch8 "Choose notification settings and breaks that support your own goals" | **post-26 key:** "Adjust nonessential alerts and choose a planned time to check the group" | Close paraphrase of the key | Proposed slide 5 names the feeling and Do not disturb; post-26 needs a new situation. |
| Challenge row 4 data: paper 12, folders 8, pens 5 = 25 | **post-14:** "three costs: 12, 8 and 5, with a total of 25… Change 12 to 15… 28" | Same numbers 25 minutes before the test | New row: add Tape, 4 and total four costs (29). |
| Challenge row 6: "Call the library with no phone number or hours" | **post-23:** "Add the help desk's contact method after step 3" | Same missing-contact idea | New feedback case: a flyer with no a.m./p.m., date or room. |
| Challenge rows 2 and 5 (old forum post; Commenter) | post-11 (three-year-old announcement); post-22 (reviewer → editor) | Adjacent subskills | Rows removed from the challenge (the post-test measures them). |
| Slide 16 knowledge check (encryption) | pre-28, not post | — | None needed; wrong answers improved anyway. |

## Does the content make sense for this audience?

**Undefined terms at first use**
- "phishing" (slide 8), "malicious software" (slide 12), "universal design" (slide 4; task 2 asks for a definition that no slide gives).
- "key" (slide 10): never said what the key is (often the password).
- "session" (slide 10: "an unlocked signed-in session").
- "FOMO" and "catfishing" are well defined.

**Logic leaps**
- Slide 10 packs encryption, device encryption, a lost powered-off device and an unlocked session into two sentences.
- Slide 11 says "check… how recovery works" without saying there is usually no recovery.
- Slide 15 ("Find a source, create a useful file, limit access and explain a recovery choice") does not describe the challenge learners actually do (CP-26).
- Slide 9's "Explain what evidence would change your decision" has no follow-up prompt.

**Missing steps**
- No real click path anywhere in week 5: notification settings, camera permissions (Edge or Windows), Windows Update, Word's Protect Document, locking the screen.
- The Gemini structure review suggested `edge://settings/content/camera`; the Settings search box is more robust because Edge renamed the page across builds.

**Tasks impossible or unreliable as written**

| Task | Problem |
|:--|:--|
| Challenge row 4 | Depends on a week 3 file that may show 28 or be missing; the formula is lost if the .csv is saved and closed before the check. |
| Challenge (all rows) | "Work each row with a partner" cannot show independent performance; 84 ratings in 25 minutes. |
| Challenge row 5 (sharing) | Needs an account; only a decision is possible in the lab. |
| Challenge row 7 (recovery) | "Names version history": version history needs OneDrive or SharePoint, which the lab lacks. Undo is the only real path on a lab PC. |
| Tasks 1–6 | No scheduled time; all written explanations. |
| Gemini's suggested Do: Windows Live captions | Not available on Windows 10. |

**Pacing is unrealistic in three places**
- 10–30: 11 slides with three simulations and a flip-card slide in 20 minutes.
- 30–45: 15 minutes for a 7:31 video plus flip cards, with five pause prompts.
- 55–80: 7 paired rows plus 84 ratings in 25 minutes. Then 50 minutes of assessment with no break before the post-test.
- The 28-item post-test in 25 minutes is feasible, but the plan says nothing about late finishers.

**Earlier findings re-checked**

| Earlier finding | Status | Evidence |
|:--|:--|:--|
| CP-07: week 5 agenda unrealistic | **Confirmed** | 11 slides in 20 min; tasks 1–6 unscheduled; 84 ratings in 25 min. |
| CP-13: challenge cannot produce individual ratings; stale supplies.csv | **Confirmed** | `challenge.intro` "Work each row with a partner"; week 3 task 5 changes paper to 15. |
| CP-22: "bulleted" list | **Confirmed** | Row 3 materials. |
| CP-26: slide 15 does not describe the challenge | **Confirmed** | Slide 15 body vs challenge rows. |
| CP-10: 2.1 claimed, not taught | **Confirmed** | No slide carries a 2.1 ref. |
| CP-11 / CP-12: phishing, malicious software undefined; no encryption methods | **Confirmed** | Slides 8, 10, 12. |
| CP-08 / AS-11: throwaway distractors | **Confirmed** | "Share your password instead", "Always allow every request". |
| AS-08: slides rehearse post items | **Confirmed**, plus post-26 (slide 5), post-14 and post-23 (challenge) | See the table above. |
| IR-15: no record path for ratings | **Confirmed** | `challenge_table()` radios on the learner page; nothing saved. |
| VM-08, VM-11, VM-15 | **Confirmed** | Frames 6:45–7:29 (bars), 5:05/5:28/5:50 ("Choose alerts" ×3), 4:20–4:42 (two-button prompt). |
| AX-03: selected phishing clue unreadable | **Fixed** | `workshop.css` `.message-preview button.inspected{…;color:#1b365d}` now wins over the pressed style. |

**New in this review**
- Word's password to open is encryption; the course implies otherwise.
- Word cannot recover a lost password; slide 11's scene implies a recovery method.
- No updates content, although the lab PCs run Windows 10 (support ended October 14, 2025).
- No "already typed my password" step (change it, turn on two-step verification).
- Both knowledge checks test objective 1; the scam objective has no in-class check.
- The CSV row loses its formula if saved and closed before the check.
- The challenge's row 4 and row 6 rehearse post-14 and post-23.
- Live captions (a Gemini suggestion) do not exist on Windows 10.
- The worksheet intro ("Work with a partner, take turns") and the plan's "Pair a driver and coach, then switch" were shared template text that contradicts an individual challenge. Both are already replaced in the working tree (uncommitted `build-pages.py` changes seen at the end of this review).

## Video structure

**Sequence.** The ten chapters (41–52 seconds each) follow a sensible order: routine (ch1) → comfort and access (ch2) → pressure in a message (ch3) → verify through a trusted route (ch4) → editing restrictions vs encryption (ch5) → unknown devices (ch6) → camera and microphone (ch7) → attention and harmful behavior (ch8) → the whole decision process (ch9) → results and next practice (ch10). Opening on the routine and returning to it in ch9 gives the week a frame. Captions are present throughout (the deck's `<track>` is `default`).

**Model → prompt → answer, chapter by chapter**

| Chapter | Model | Prompt and answer | Rating |
|:--|:--|:--|:--|
| ch4 (2:09–2:50) | **Strong.** Five-step screen demo: leave the message (2:10) → saved bookmark (2:13) → Contact us (2:15) → "Contact found on the known website · 304-555-0142 · Ask: Does the claimed issue exist?" (2:22). The message itself shows the trap: "Call the number in this message for reassurance." | "Pause and choose between replying… and checking through a known route" ends 2:43; answer at 2:43.3 (0.5 s). | Strong model, no think time |
| ch7 (4:19–5:02) | **Strong.** Allow for the practice meeting (4:33) → "Site permissions: Camera: Allowed" (4:35) → Block on the reading page (4:39) → "Review access when the task ends" (4:41). | "Pause and compare our two examples" ends 4:55; the next sentence continues to 5:00, then ch8 starts at 5:02. | Strong; same scenario as post-27 |
| ch9 (5:54–6:43) | Diagram (appointment message, "A private code is requested", "Pause before sharing"). | "Pause the video and state three things…" ends 6:13; answer at 6:14 (0.7 s). | Excellent question, no think time |
| ch2 (0:42–1:27) | Photo, then icon diagram (captions, readable screen, breaks, input within reach). | "Pause and choose one control…" ends 1:23; ch3 starts 1:27. | Good prompt; Tell only |
| ch5 (2:50–3:38) | Diagram: Read-only "Still readable"; Original data → "Key required"; "7fA2 · 9cD4 · e18B" (frames 2:53–3:20). | "Pause and explain which protection fits…" ends 3:36; ch6 starts 3:38. | Good; add that a password to open is encryption |
| ch3, ch6 | Diagrams with step captions ("Evidence · A convincing logo is not proof"; "Pause · Keep the drive disconnected"). | — | Tell only, well paced |
| ch8 (5:02–5:54) | Placeholder panel ("Choose alerts" ×3) and "Report / Block / Ask trusted support". | — | Weak visual |
| ch10 (6:43–7:31) | "My next practice" bars (Settings, Files, Communication). | Never names the challenge; its skill list does not match. | Weak for its job |
| ch1 (0:00–0:42) | Photo, then Evidence → Verify → Safer action. Step captions start "Pause ·", "Inspect ·", "Verify ·". | — | Good framing |

**Coverage gaps.** No chapter shows software updates, two-step verification, locking the screen, Word's Protect Document menu, notification settings or a real browser permission page.

**Where it should play.** Chapter by chapter as the Show inside each cycle (running order below). Stop by hand at 1:23, 2:43, 3:36, 4:55 and 6:13; at 2:43 and 6:13 the answer starts in under a second. Ch9 becomes the Review of the scam cycle. Ch10 introduces the challenge, with the instructor naming it. Slide 14 becomes a replay menu, not a block.

## Recommended restructure

A 120-minute running order built from three Tell, Show, Do, Review cycles inside WIPPEA. It keeps the 25-minute skills challenge and the 25-minute post-test, and uses only current slide numbers, chapters and tasks. The slide order is unchanged; the instructor jumps with the sidebar. "Live" means the instructor demonstrates on the projector.

| Minutes | WIPPEA | Tell, Show, Do, Review cycle | Slides | Video | Worksheet / check | Notes |
|:--|:--|:--|:--|:--|:--|:--|
| 0–6 | W | **Warm-up and reconnect.** Week 4 home task; recall two-step verification (week 4) and read-only vs encryption (week 2); pair share on slide 2; "who has had an urgent text?" | 2 | — | — | No private details. |
| 6–9 | I | **Introduction.** Read the four ABCD goals; say how the day runs; name the routine. | 1 | ch1 | — | "Pause, inspect, verify" is the Review language all day. |
| 9–17 | P → P → E | **Cycle A, comfort, access and attention.** Tell: slides 3–5. Show: ch2 (pause at 1:23) + live Magnifier and the Notifications page. Do: tasks 1 and 2, every learner. Review: a partner says what changed and why; settings back. | 3, 4, 5 | ch2 | Tasks 1, 2 | Captions via the slide 14 video, muted; Tab to watch focus. |
| 17–31 | P → P → E | **Cycle B, scams and fake identities.** Tell: slide 8 (define phishing), then 6 and 7. Show: ch3, ch4 (pause at 2:43, show of hands), ch8; live: point at a link without clicking. Do: slide 8 simulation, then tasks 3 and 4, every learner. Review: ch9 (pause at 6:13), each learner tells a partner evidence / unverified / next step; flip slide 9 card 3. | 8, 6, 7, 9 | ch3, ch4, ch8, ch9 | Tasks 3, 4 | VA never charges a fee to apply; FTC: never send money to someone you have not met. |
| 31–45 | P → P → E | **Cycle C, protect devices and files.** Tell: slides 12, 13, 10, 11. Show: ch6, ch7 (pause at 4:55), ch5 (pause at 3:36); live: Edge Settings › search permissions › Camera, then Windows logo key and L. Do: slide 9 cards 1, 2, 4 and tasks 5–6, every learner, looking only. Review: knowledge checks 16 and 17; re-teach anything more than two learners miss. | 12, 13, 10, 11, 9, 16, 17 | ch6, ch7, ch5 | Tasks 5, 6 | Hold up a USB drive; never plug it in. Windows 10 path for Windows Update in task 5. |
| 45–47 | I | **Introduce the challenge.** Play ch10, then slide 15 and task 7. "Five rows from weeks 2 to 4, on your own; the quick card is allowed; a spoken prompt counts as With prompt." | 15 | ch10 | Task 7 | Say "challenge": ch10 does not. |
| 47–72 | E | **Individual check: skills challenge.** Every learner works five rows alone. From minute 8, one visit per learner (about a minute), all five rows rated on the paper roster; one return visit. | — | — | Task 7, roster | Check row 3 in the formula bar before the file closes. |
| 72–82 | — | Break | — | — | — | Screen-free; finish ratings. |
| 82–107 | E | **Post-test.** Name first; work alone; optional week 1 score for comparison; record each score out of 28; print page 1 only. | 18 | — | Post-test | Late finishers may run to minute 110. |
| 107–120 | A | **Apply and close.** Slide 19: domain scores, task 8, one practice task; discuss the two or three items missed most. Slide 20. Home task: check for updates or turn on two-step verification for one account; share at week 6. Restore lab settings; Start fresh on this computer. | 19, 20 | — | Task 8 | Week 6 warm-up follows up. |

Timing check: 6 + 3 + 8 + 14 + 14 + 2 + 25 + 10 + 25 + 13 = 120 minutes.

**Why the break moves.** A break between the challenge and the post-test splits 50 minutes of assessment in two, gives older learners a rest before the test, and gives the instructor time to finish the ratings.

**Tight spots.** Cycles B and C (14 minutes each) are full. If you run long: move task 4 to home practice, and show the Magnifier on the projector only. Never shorten the challenge or the post-test.

**Moved or optional**
- Slide 14 becomes the chapter menu for replay; the whole video is home review (captions and transcript).
- Slides 16–17 move from "just before the post-test" to the end of cycle C.
- The old 30–45 "scenario practice" dissolves into the three cycles.

## Top 10 changes, ranked

| # | Change | Where | Why (Tell/Show/Do/Review, WIPPEA or andragogy) | Effort | Source file to edit |
|:--|:--|:--|:--|:--|:--|
| 1 | Replace the 7-row agenda with the running order above: three cycles naming slides, chapters with pause times and tasks, then the challenge, break, post-test and close. | Lesson plan agenda | Each skill group gets Tell → Show → Do → Review; mastery before moving on; chunking for older learners | Medium | `scripts/dl2/author-content.py` week 5 `agenda` (line 120) → `curriculum.json` |
| 2 | Reshape the challenge: individual, 5 rows done at the computer (search, structured paragraph, total of four costs, Undo recovery, feedback); a fresh supplies.csv; a numbered list; new numbers (29) and a new feedback case; one visit per learner; paper roster. | Worksheet task 7; answer guide; slide 15 | Valid individual evidence (WIPPEA Evaluation); feasible load; no rehearsal of post-14 and post-23 | Medium | `author-content.py` week 5 `challenge`, `lab[6]`, `answers[6]`; `tests/content/dl2-review-fixes.spec.js` lines 43, 47, 48 (7 → 5) |
| 3 | Make tasks 1–6 hands-on and schedule them inside the cycles: Magnifier or a chair/screen change; captions and Tab; inspect the slide 8 message; look at Edge Camera permissions and Windows Update; open Word's Protect Document menu. | Worksheet tasks 1–6 | The Do must repeat the Show on the learner's own workstation (orientation) | Small | `author-content.py` week 5 `lab`, `answers` |
| 4 | Rewrite the objectives as four ABCD outcomes, including the missing comfort/access/attention group; design the checks first. | Slide 1; lesson plan outcomes | WIPPEA Introduction and Evaluation; backward design | Small | `author-content.py` week 5 `objectives`, new `outcomes` |
| 5 | Correct the Tell on file protection: Word's password to open (Encrypt with Password) encrypts the file; read-only only limits changes; Word cannot recover a lost password; name BitLocker/Device encryption and FileVault. | Slides 10, 11; scene (5,11) | Content correctness; GS6 7.3.2, 7.4.1 | Small | `author-content.py` slide bodies; `scenes.py` and `photo_scenes.py` (5,11) |
| 6 | Add updates and account protection: slide 12 updates sentence; slide 9 card 4 on Windows 10 (end of support October 14, 2025; ESU to October 12, 2027); slide 8 "typed a password? change it and turn on two-step verification"; lock with Windows logo key and L. | Slides 8, 9, 10, 12; home task | Readiness (their own home PCs); GS6 7.3 and 2.1 | Small | `author-content.py` slide bodies and `cards` |
| 7 | Knowledge checks: a new slide 17 question (review a clinic site's permission after a video visit) that no longer repeats post-27; slide 16 wrong answers from real misconceptions (compression, read-only). | Slides 16, 17 | Evaluation that can lead to re-teaching; respectful tone; AS-08 | Small | `author-content.py` week 5 check slides |
| 8 | Add the 13-row Windows 11 lab quick card (Magnifier, notifications, link check, report phishing, two-step verification, updates, camera permissions, lock, Word protection ×2, device encryption, Undo/version history, SUM). | Lesson plan and worksheet | The Show must be the same task as the Do; CP-03 | Small | `author-content.py` week 5 `lab_paths` |
| 9 | Week-specific prep: Word and Excel, a USB prop, paper roster and week 1 scores, ask IT about ESU, check look-only settings under a learner login, Start fresh. (The shared "work with a partner / switch driver" text is already replaced in the working tree, uncommitted, as of this review.) | Lesson plan prep | Instructor readiness; the challenge must be individual | Small | `author-content.py` week 5 `prep` |
| 10 | Hand-off and later polish: post-test rewrite gives items 26, 27 and 28 new situations; printable roster in the answer guide; re-render ch10 (name the challenge), ch8 labels, ch7 three-choice prompt, 2–3 s holds after 2:43 and 6:13. | Assessments; answer guide; video | Valid pre/post comparison; think time (Knowles) | Medium / large | `author-assessments.py`; `build-pages.py`; `video/digital-literacy-2/week-05/` then rebuild media |

## Gemini claims checked

**Video review (`week-05-video-gemini-3.1-pro-preview.md`)**

| Claim | Verdict | Evidence |
|:--|:--|:--|
| Accuracy 5/5 | **Mostly agree** | The advice is sound. Ch5 (3:11–3:15) implies password prompts are not encryption; in Word the password to open is encryption (Microsoft). |
| 2:09 "typing a URL and clicking a bookmark" | **Disagree (detail)** | No URL is typed. The demo opens "Community desk — saved bookmark" (frame 2:13, step 03/05). |
| 3:20 padlock timed with "key" | **Agree** | Frame 3:20: padlock "Key required", "7fA2 · 9cD4 · e18B". |
| 4:33 "realistic, modern browser permission prompts" | **Partly disagree** | Two buttons (Block / Allow). Chrome offers Allow while visiting the site / Allow this time / Never allow (Google). |
| 4:38 Block clicked on "Deny an unrelated request" | **Agree** | `screen-share-actions.json`: 258.85 + 19.69 s = 4:38.5, phrase "Deny an unrelated request". |
| Prompts give zero seconds (1:19, 2:38, 3:29, 4:53, 6:05); pause at 1:26, 2:43, 3:36, 5:00, 6:14 | **Agree**, with timing corrected | Word-timed prompt ends: 1:23, 2:43, 3:36, 4:55, 6:13. The 2:43 and 6:13 answers follow in 0.5 and 0.7 s. Gemini's 1:26 and 5:00 are the chapter ends; also workable. |
| 0:05 "Pause · What is being requested?" is confusing; remove "Pause" | **Partly agree (Low)** | Frame 0:05 confirmed. "Pause" is step 1 of the routine the narration names at 0:26 ("pause, inspect the evidence, verify independently"), so it is deliberate. Explain it once rather than re-render. |
| 3:53 "Pause · Keep the drive disconnected" means stop acting, not pause the video | **Partly agree (Low)** | Shown at 3:58 (frame 238 s), not 3:53. Same routine word as above. |
| Legibility 5/5; thick progress bars at 6:42 | **Agree on legibility** | Frames 6:45–7:29 are readable. The bars do not match the report's seven domains or the challenge (VM-08). |
| Accessibility 5/5; no reliance on color | **Agree** | Captions default-on; narration describes each state (Allowed / Blocked). |
| Tip: hold up a real USB drive at 3:37 | **Agree** | In prep and cycle C; never plugged in. |
| Tip: tell learners to ignore the on-screen "Pause" | **Disagree** | Better to explain it as step 1 of the routine than to teach learners to ignore screen text. |

**Structure review (`week-05-structure-gemini-3.1-pro-preview.md`)**

| Claim | Verdict | Evidence |
|:--|:--|:--|
| Evaluation is **Strong** | **Disagree** | The post-test is strong. The paired challenge cannot give individual ratings; 84 ratings in 25 minutes; no roster; slide 17 rehearses post-27. |
| Application is **Strong** | **Disagree (Adequate)** | No home task and no week 6 follow-up. |
| Warm-up retrieves weeks 3/4 | **Agree** (weeks 2–4) | "a source check, a file permission and a useful feedback habit". It never points to today's topic. |
| CSV does not save formulas — **High** | **Partly agree (Medium)** | True, and week 3's own slide says so. But the task works while the file is open, and a live check avoids the loss. The bigger problem is the stale week 3 file (28 vs 25). |
| A password to open *is* encryption in Microsoft 365 (AES-256) — Medium | **Agree on substance** | Microsoft's menu is literally "Encrypt with Password". I did not verify the cipher strength; learners do not need it. |
| Slide 4 keyboard route needs "Example:" | **Agree (Low)** | Tab order is page-specific. |
| "Use Contact on the known website" — sites use Help or chatbots | **Partly agree (Low)** | Say "Contact or Help". |
| Change worksheet Q2–Q6 to hands-on tasks | **Agree** for 2, 3, 5, 6 | Task 4 stays a short written decision: the lab has no social accounts. |
| Learners open Edge camera settings | **Agree** | Look only, via the Settings search box; the page label varies by Edge build. |
| Turn on Windows Live Captions (Win + Ctrl + L) | **Disagree** | Windows 11 22H2 and later only; the lab runs Windows 10 (Microsoft). Use the course video's captions and Magnifier. |
| Instructor demonstrates a Word password | **Agree, as a Show only** | Learners open the menu but set no password on lab files. |
| Move FOMO and catfishing to week 6 or the warm-up | **Disagree** | They are GS6 7.2 objectives and post-26 tests FOMO. Keep them short inside cycles A and B with a written decision. |
| Hook: "a text about a package you didn't order" | **Agree** | In the warm-up. |
| Veterans must "unlearn the military firehose" | **Disagree with the framing** | A stereotype. Chunking stands on adult-learning grounds for everyone. |
| Ask how veterans verified orders or identities in the service | **Agree, optional** | Good use of experience (Knowles 3). |
| Tell learners the challenge covers past weeks | **Agree** | In the 2-minute challenge introduction. |
| Ensure learners can reach post-test results from home | **Disagree** | Results live in that browser tab only (IR-03). Learners must print page 1 or save a PDF before closing, and the instructor records the score. |
