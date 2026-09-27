# Week 4 structure and content review (Tell, Show, Do, Review + WIPPEA + adult learning) — Claude

Scope: Digital Literacy Level 2, week 4 "Communicate and collaborate with care", class Monday 2026-10-19, 4:30–6:30 p.m. Reviewed read-only against `vublessons` `main` at 9270815 (after the week 1 Tell, Show, Do, Review merge; week 4 content is unchanged since the pre-cohort fixes).

Conventions:
- Slide numbers are as learners see them (slide 1 = title, 23 slides). The current slides are: 1 title (feedback practice), 2 Choose a channel (discussion), 3 Personal and professional identities, 4 Write an email someone can act on, 5 To, Cc, and Bcc, 6 Timing, 7 Inclusive language, 8 Participate in a community, 9 Verify a community service, 10 Collaborate on one shared copy, 11 Live editing or later feedback? (flip cards), 12 Feedback names an improvement, 13 Acknowledge and resolve, 14 Meetings and webinars, 15 Watch (video), 16 Goods, services, and subscriptions, 17 Review a digital payment, 18 Small in-app purchases add up, 19 Knowledge check: useful feedback, 20 Knowledge check: a trial offer, 21 Lab, 22 Leave a clear next step, 23 completion.
- Lesson-plan minutes come from `weeks/week-04/lesson-plan.html` (generated from the `add(4, …)` call in `scripts/dl2/author-content.py`).
- Video times are m:ss in `media/week-04.mp4` (7:20.6, 1280×720). Chapter starts: ch1 0:00, ch2 0:48, ch3 1:36, ch4 2:19, ch5 3:05, ch6 3:50, ch7 4:28, ch8 5:11, ch9 5:54, ch10 6:37.
- Pause points were measured from `narration/beat-NN.words.json` plus each beat's start.
- 33 frames were extracted and inspected: chapter starts, middles and ends, all 12 screen-demo states (ch4 and ch6, from `screen-share-actions.json`) and every prompt. They are in `scratchpad/video-eval/w4frames-claude/`.
- The proposal (`week-04-proposal.json`) was applied to a copy of the repo in `scratchpad/w4-sandbox/`, rebuilt, and checked with `tests/content/dl2-weeks-tsdr.spec.js`: all 5 week 4 tests pass. The week 1 and other DL2 content specs still pass (the one failure is a sandbox artifact: `instructors/index.html` was not copied).

## Verdict

**Week 4 is teachable on 19 October, but it is two Tell-then-Do blocks, not Tell, Show, Do, Review cycles.** The content that is there is accurate. The gaps are in what is missing: how payments differ, named streaming services, named collaboration tools, and an account-free path for the coauthoring and comment tasks.

**Strengths**
- A single, believable thread runs through the week: coordinating a fictional community computer-help session with one message, one shared handout and one decision.
- Good working simulations: the email draft (slide 4), recipient visibility (slide 5), the feedback workshop (slides 1 and 12), the practice meeting (slide 14) and the practice checkout (slide 17).
- Two strong screen demos in the video: ch4 (To, Cc, Bcc and Reply all, 6 steps) and ch6 (comment, author change, resolve, 6 steps).
- Low-risk practice: fictional names, `example.invalid` addresses, a checkout that "cannot pay", and "draft only · nothing is sent".
- The week 5 warm-up already asks for "a useful feedback habit", so the follow-up WIPPEA wants exists.

**Problems**
- **Blocks, not cycles.** 10–30 tells eight slides (2–9); 30–50 practises. 60–80 tells eight more slides (10–14, 16–18) and plays the whole 7:20 video; 80–110 practises four tasks with a role switch.
  - The video's email chapters (ch2–4) play at 60–80, 10–50 minutes *after* learners drafted their email at 30–50. The Show follows the Do.
  - The second block mixes three unrelated skill groups (coauthoring, meetings, buying) in 20 minutes.
- **Warm-up ignores Level 1.** DL1 week 3 already taught "Use inclusive language & email reply options" and "Collaborate, give feedback & use good etiquette", and its guide says to "Spend real time on Reply vs Reply All vs Forward vs Bcc". Week 4 re-teaches all of it without saying so.
- **Practice is shared and partly without a tool.** "Pairs draft", "Switch roles": each learner does about half. Tasks 5–6 need a shared document, but no handout is supplied, no tool is named and learners have no account. Slides 8–9 (community) have no task at all.
- **Evaluation is thin.** Both knowledge checks have throwaway wrong answers ("This is bad.", "Only the button color"). Nothing checks the email objective. Task 8 prints its own answer ("($60)").
- **Objectives are not measurable** and do not match what is taught: meetings, webinars and communities (6.2, 5.1.3–5.1.4) have no objective, and "digital identities" is attached to the buying objective.

**Correctness:** 0 High, 5 Medium, 11 Low. Nothing taught would harm a learner. The Medium items are omissions against IC3 GS6 objectives or the task design:
- Slide 17 does not explain how cards, digital wallets and person-to-person apps differ, or that money sent by app is hard to get back (5.2.2), which matters for scams aimed at older adults.
- Slide 16 names no streaming service (5.2.4).
- Slides 10–11 name no collaboration tool (6.1.1).
- Task 8 gives away its answer.
- Tasks 5–6 have no handout and no account-free path; the plan's prep promises "instructor-provided fictional accounts" that do not exist.

**For 19 October:** use the five-cycle running order below. Play each chapter next to its slide and pause at 1:29, 2:54, 4:22 and 6:35. Every learner drafts in the worksheet, comments in a local Word file by swapping seats, and uses slide 14 for the meeting controls. The slide, worksheet and quick-card changes are in the proposal JSON.

## WIPPEA map

| Stage | Where it happens | Rating | Evidence | What to change |
|:--|:--|:--|:--|:--|
| **W — Warm-up** | 0–10 "Reconnect: Share one improvement from the resource-pack review." | **Weak** | <ul><li>Recalls last week's product, but not the skills today builds on.</li><li>DL1 week 3 taught Reply, Reply all, Forward, Bcc, inclusive language and collaboration etiquette (`digital-literacy-1/weeks/week-03/syllabus.html`). DL2 week 2 taught Viewer, Commenter and Editor (slide 15), and week 3 taught suggesting changes. None is recalled.</li><li>Nothing points toward today's topic.</li></ul> | <ul><li>Report last week's home task.</li><li>Two recall questions: "Reply vs Reply all vs Forward?" (DL1 week 3) and "Which access lets a partner suggest wording?" (DL2 week 2).</li><li>Click through the slide 1 feedback practice as the hook.</li></ul> |
| **I — Introduction** | Slide 1 objectives and feedback practice; ch1 (0:00–0:48) is not scheduled | **Adequate** | <ul><li>Objectives are shown in writing. ch1 links to learners' lives: "Think of a group task you have helped organize: a family gathering, a volunteer activity, or a meeting."</li><li>The objectives are not measurable, and two taught groups (meetings/webinars 6.2; community 5.1.3–5.1.4) are missing.</li><li>ch1 plays only as part of "play the explainer" at 60–80.</li></ul> | <ul><li>Five ABCD objectives, one per cycle.</li><li>Play ch1 (48 s) at minute 10 and ask each pair for one group task and one message that went wrong.</li></ul> |
| **P — Presentation** | 10–30: slides 2–9 (8 slides, 6 simulations). 60–80: slides 10–14 and 16–18 (8 slides) plus the 7:20 video | **Adequate** content, **Weak** pacing | <ul><li>Several modes: photo scenes, 5 simulations, flip cards, 2 screen demos, captions and a transcript.</li><li>About 2.5 minutes per slide at 10–30. At 60–80, 20 minutes must hold eight slides and the whole video (CP-19).</li><li>Undefined at first use: password manager, multifactor authentication (slide 3), scheduled send (slide 6), webinar, digital wallet.</li><li>Slides 8 and 9 are named in no phase.</li><li>No planned check of understanding in either block.</li></ul> | <ul><li>Teach one skill group at a time; play each chapter with its slide.</li><li>End each cycle with a Review question or check.</li></ul> |
| **P — Practice** | 30–50 "Pairs draft a fictional request…"; 80–110 "Complete the shared-document role play and fictional subscription comparison. Switch roles." | **Weak** | <ul><li>Pairs share one draft and switch roles, so each learner drives about half.</li><li>Tasks 5–6: "the resource handout" is not supplied; no tool or account is named (CP-02, IR-07).</li><li>No task for community participation or checking a service (slides 8–9), for version history, for choosing how to pay, or for the meeting controls (task 7 is a written list).</li><li>The email Do (30–50) comes before its Show (ch2–4 at 60–80).</li></ul> | <ul><li>Every learner does each task at their own seat right after its Show; the partner coaches.</li><li>Account-free paths: the email in the worksheet box; comments in a local Word file by swapping seats; slide 14 for the meeting.</li></ul> |
| **E — Evaluation** | 110–120: slides 19–20; "ask each learner to describe one helpful feedback habit"; answer guide; pre/post items 2.1, 2.2, 5.1, 5.2, 6.1, 6.2 | **Weak** | <ul><li>Slide 19 (feedback) and slide 20 (trial) cover objectives 2 and 3. Nothing checks objective 1 (channel and email).</li><li>Wrong answers are not believable: "This is bad.", "I dislike everything.", "Only the button color", "Whether the site has animations" (CP-08, AS-11).</li><li>Task 8 prints the answer: "Calculate one year of A ($60)" (CP-21).</li><li>Ratings are asked for but there is no record.</li></ul> | <ul><li>A short Review in every cycle.</li><li>A final 3-item individual check on the roster (recipients, resolved comment, offer cost and payment choice).</li><li>Believable wrong answers; remove "($60)".</li></ul> |
| **A — Application** | Slides 22–23; ch10 (6:37–7:21) "For a group task from your own life, choose one habit to transfer"; week 5 warm-up asks for "a useful feedback habit" | **Adequate** | <ul><li>A transfer prompt exists in ch10 and slide 23, and week 5 follows up.</li><li>No concrete home task. The most useful transfer for this audience (checking a real subscription or payment) is not asked for.</li></ul> | Home task: find one subscription or regular charge, write down when it renews and how to cancel it, and report one fact at the week 5 warm-up (no amounts or account numbers). |

**Overall flow.** The order is W → P (10–30) → Practice (30–50) → break → P (60–80, with the whole video) → Practice (80–110) → E (110–120).
- This is better than week 1's single block, because email is practised before collaboration is taught. But each Do still comes 10–50 minutes after its Tell, and no objective gets presentation → practice → check before the next one starts.
- The video belongs chapter by chapter inside each cycle, as the Show. Played as one block at 60–80, it repeats the email Tell after the email Do and rushes the rest.
- The community slides (8–9) sit between email and collaboration, but their video chapter (ch8) comes after the meeting chapter (ch7). Teaching them with slide 14 matches the video.

## Tell, Show, Do, Review by skill

| Skill | Tell (where) | Show (where) | Do (where; minutes available) | Review (where) | Missing or weak steps |
|:--|:--|:--|:--|:--|:--|
| Choose a channel | Slide 2; ch2 0:48–1:05 | ch2 diagram (Message, Shared file, Meeting) | Task 1 in the 30–50 lab (pairs) | Answer guide 1 | ch2's prompt (1:28.6) is answered 0.82 s later. No check. |
| Identity and credentials | Slide 3; ch2 1:05–1:22 | Slide 3 scene; ch2 "Active profile: Training" | Task 3 part ("choose… account") | Answer guide 3; pre/post 2.1 | "Password manager" and "multifactor authentication" undefined at first use. No real Show of which account is signed in. |
| Actionable email | Slide 4; ch3 1:36–2:17 | Slide 4 five-step draft; ch3 diagram | Task 2 at 30–50 (pairs; no place named to write it) | Answer guide 2 | Show (ch3) plays at 60–80, after the Do. |
| To, Cc, Bcc, Reply all | Slide 5 (Reply all not mentioned); ch4 2:19–2:44 | **ch4 screen demo** (inspect → Cc → Bcc → Reply all note → remove class list and Bcc → response window) — strong; slide 5 simulation | Task 3 part ("Explain To, Cc and Bcc") | Answer guide 3; pre/post 5.1 | No scenario to place recipients in. Reply all is in the video only, although DL1 called it "the most common veteran email mistake". |
| Timing and scheduled send | Slide 6; ch4 2:45–2:51 | Slide 6 scene (text only); ch4 step 6 | Task 3 part ("Choose an appropriate time") | Answer guide 3; pre/post 2.2 | "Scheduled send" undefined; no Show of where it is. |
| Inclusive language | Slide 7; ch3 one sentence (1:56) | Slide 7 scene (three examples) | Task 4 (no sentence supplied) | Answer guide 4; pre/post 2.2 | Thin Show; the Do has no input sentence. |
| Community participation, verify a service | Slides 8–9; ch8 5:11–5:52 | Scenes; ch8 diagram | **None** | None in class | Named in no plan phase; no Do; no check. |
| Roles, one shared copy, synchronous vs asynchronous | Slides 10–11; ch5 3:05–3:48 | Scene; flip cards; ch5 diagram | Task 5 at 80–110 | Answer guide 5; pre/post 6.1 | No collaboration tool named (IC3 6.1.1). Coauthoring cannot be done without an account. |
| Comment, respond, resolve | Slides 12–13; ch6 3:50–4:26 | **ch6 screen demo** (vague → specific comment → Add comment → author adds number → acknowledge → Resolve) — strong; slide 12 workshop | Task 6 at 80–110 (no handout, no tool) | Slide 19; answer guide 6; pre/post 6.1 | The Do has no input. Slide 19's wrong answers are throwaway. ch6 runs at 177.6 wpm. |
| Version history | Slide 13 sentence | Slide 13 scene text | None | None | Not said that it needs a file saved online. |
| Meetings and webinars | Slide 14; ch7 4:28–5:09 | Slide 14 practice meeting and device scene; ch7 diagram | Task 7 (a written list) | Answer guide 7; pre/post 6.2 | No one uses the practice controls; no real mic test. |
| Goods, services, streaming | Slide 16 | Slide 16 scene | None | None | No streaming examples (IC3 5.2.4). |
| Digital payments | Slide 17; ch9 6:06–6:13 | Slide 17 practice checkout | Task 8 part ("list questions") | None | No card vs wallet vs person-to-person distinction (IC3 5.2.2). |
| In-app purchases | Slide 18; ch9 6:13–6:19 | Slide 18 receipt scene | None | Pre/post 5.2 | "Security concerns" (5.2.3) reduced to "review purchase controls". |
| Trials and subscriptions | Slides 16, 18; ch9 5:54–6:13 | ch9 diagram (Trial today → $12 each month) | Task 8 (answer printed in the task) | Slide 20; answer guide 8 | The Do gives away its own answer. |

**Week 4 runs as two big blocks.** Each Tell block covers eight slides; the Show (video) plays after the first Do; each Do block covers four tasks with a role switch.
- Three skills have Tell only: community participation, version history and streaming.
- Two skills have a Do with no usable input: task 6 (no handout) and task 4 (no sentence).
- For older learners who need time to read, try and ask, this means holding six or more procedures for 20–50 minutes, finding mistakes only in the lab, and delaying the "I just did it" moment.

## Objectives

GS6 Level 2 groups claimed: 2.1, 2.2, 2.3, 5.1, 5.2, 6.1, 6.2.

**1. "Choose a communication channel and write a clear email."**
- **ABCD rewrite (split into two):**
  - *Channel and account:* given two fictional messages (a detailed request a partner can answer tomorrow and an urgent problem in the room), each learner chooses a suitable channel for each and explains why, and names the account a volunteer notice should come from. Both choices fit the urgency and the audience.
  - *Email:* in the worksheet, each learner writes a practice email with a specific subject, one clear request, a reply-by time and a courteous close; places three fictional recipients correctly in To, Cc and Bcc and says who a Reply all reaches; and rewrites a sentence to spell out abbreviations and remove an assumption about age. All parts correct with no more than one prompt; nothing is sent.
- **Taught:** slides 2–7; ch2–4. **Practised:** tasks 1–4. **Evaluated:** answer guide only; pre/post 2.1, 2.2, 5.1.
- **Status:** Taught and practised; not checked in class.

**2. "Collaborate using comments, coauthoring and version history."**
- **ABCD rewrite:** in a practice handout in Word, each learner adds a comment to a partner's handout that names the place, the change and the reason, then replies to the comment on their own handout, makes or declines the change with a reason, and resolves it. Each learner also chooses live coauthoring or later comments for a given schedule and names the access each role needs.
- **Taught:** slides 10–13; ch5–6. **Practised:** tasks 5–6 (no handout, no tool). **Evaluated:** slide 19; pre/post 6.1.
- **Status:** Coauthoring and version history need a file saved in OneDrive or SharePoint ([Microsoft](https://support.microsoft.com/en-us/word/training/share-a-document); [Microsoft](https://support.microsoft.com/en-us/office/collab-files/view-previous-versions-of-office-files)), so the lab can only describe or simulate them. Comments, replies and resolve work in a local Word document, so that part can be done for real.

**3. "Explain online purchases, subscriptions and digital identities."**
- **ABCD rewrite:** *Purchases and payments:* given two fictional streaming offers, each learner works out what each costs for 12 months and for 3 months, writes two questions to ask before paying, and chooses a way to pay a new website with a reason, explaining why person-to-person apps are only for people they know. The arithmetic is correct and the reason matches the payment protections taught.
- **Taught:** slides 16–18; ch9. **Practised:** task 8. **Evaluated:** slide 20; pre/post 5.2.
- **Status:** "Digital identities" belongs with objective 1 (slide 3 is taught with email). How payments work (5.2.2) and streaming examples (5.2.4) are not taught.

**Missing objective (6.2, 5.1.3, 5.1.4), taught but not stated.**
- **Proposed:** *Meetings and communities:* using the slide 14 practice meeting, each learner unmutes, raises and lowers a hand and mutes again, tests a headset microphone in Windows Settings when one is available, and lists four meeting or webinar habits, including asking before recording, plus one detail to confirm with an organization before trusting a community post.
- **Taught:** slides 8, 9, 14; ch7–8. **Practised:** task 7. **Evaluated:** pre/post 6.2.

**Not covered:** GS6 6.1.1 "List digital tools used for collaboration" and 6.1.2 "Explain the benefits of collaboration" have no content; 2.3.2 (help features and community resources) is covered in week 1 only.

**Backward design.** "Evidence to collect" copies the worksheet. It was not designed first. One of four taught groups has no objective, and the email objective has no in-class check.

## Adult learning principles

| Principle | Rating | Evidence | Improvement |
|:--|:--|:--|:--|
| 1. Need to know | Adequate | <ul><li>ch1 opens with "a family gathering, a volunteer activity, or a meeting" and "The goal is not to send more messages. It is to help the right person take the right next action."</li><li>Slides open with *what* more than *why it matters to me*; the scam risk behind payment choices is never named.</li></ul> | Open each cycle with a real problem: a reply-all that went to the whole group, a handout with three "final" versions, a free trial that became a monthly charge, a caller demanding payment by app. |
| 2. Self-concept | Weak | <ul><li>Throwaway wrong answers ("I dislike everything.", "Whether the site has animations") can read as talking down to capable adults.</li><li>Pairs switching roles means half the learners watch.</li><li>Positive: fictional data, "nothing is sent", "cannot pay".</li></ul> | Believable wrong answers; every learner drives their own workstation. |
| 3. Experience | **Weak** | <ul><li>No link to DL1 week 3 (reply options, inclusive language, etiquette) or DL2 week 2 (Viewer, Commenter, Editor).</li><li>ch1 and ch8 ask learners to use their own experience ("You already use judgment when accepting advice in person"), but the plan schedules no discussion.</li></ul> | Warm-up recall; ask "what do you do now?" before each Show; keep the Tell short where DL1 already taught it. |
| 4. Readiness | Adequate | <ul><li>Email, video calls, subscriptions and payments are things these learners handle now; telehealth and family video calls make meetings immediate.</li><li>The tasks assume shared-document and email accounts the lab does not have.</li></ul> | Account-free Do for every task; a home task on a real subscription. |
| 5. Orientation (problem-centred) | Adequate | <ul><li>Problem-framed: slides 4 ("Write an email someone can act on"), 12, 17 ("Inspect a fictional checkout"), ch4 and ch6 demos.</li><li>Subject-centred: slide 16 "Goods, services, and subscriptions" defines terms rather than solving a problem.</li></ul> | Recast slide 16 around a choice: "Which streaming plan costs less for how you watch?" (task 8 does this). |
| 6. Motivation | Adequate | <ul><li>The coordination story ends with "the partner knows what to do, can open the right file" (ch10).</li><li>Visible success is delayed to the 80–110 lab.</li></ul> | A quick Review after every cycle; the individual check shows each learner three things they did. |

## Content correctness

| # | Where | What it says | What is correct (source) | Severity |
|:--|:--|:--|:--|:--|
| 1 | Slide 17; ch9; task 8 | "A payment service sends an authorized payment request. Check seller, total, recurring terms, delivery and refund information." | <ul><li>Accurate but empty: GS6 5.2.2 asks learners to "Explain how digital payments work", and the practical difference is not taught (CP-12).</li><li>A credit card lets you dispute a wrong or unauthorized charge; liability for unauthorized charges is capped at $50 ([FTC](https://consumer.ftc.gov/articles/using-credit-cards-and-disputing-charges)).</li><li>A digital wallet pays with a saved card; Apple Pay does not share the card number with the merchant ([Apple](https://support.apple.com/en-us/101554)).</li><li>With payment apps, "it's hard for you to get your money back" ([FTC](https://consumer.ftc.gov/articles/mobile-payment-apps-how-avoid-scam-when-you-use-one)). Zelle: send money to "people you know and trust"; a sent payment "cannot be canceled"; "Zelle® does not offer purchase protection" ([Zelle](https://www.zelle.com/faq/who-can-i-send-money-zelle)).</li><li>Anyone who says the only way to pay is by payment app, gift card, wire or crypto is a scammer ([FTC](https://consumer.ftc.gov/consumer-alerts/2026/07/way-spot-scams-how-someone-asks-you-pay)).</li></ul> | Medium |
| 2 | Slide 16; scene (4,16) | "Streaming delivers media over a connection." No example. | GS6 5.2.4 "Identify examples of media streaming services" (Certiport objective list, `dl2-review/gs6.txt`). Name some: Netflix, YouTube, Spotify; hoopla is available with a West Virginia Library Commission statewide card "no matter where you live in West Virginia" ([WVLC](https://wvlcguides.org/howtousehoopla)). | Medium |
| 3 | Slides 10–11 | Roles and synchronous/asynchronous work, with no tool named. | GS6 6.1.1 "List digital tools used for collaboration" and 6.1.2 "Explain the benefits". Common tools: Word with OneDrive (Share, then coauthor) ([Microsoft](https://support.microsoft.com/en-us/word/training/share-a-document)), Google Docs, email, Teams or Zoom. | Medium |
| 4 | Worksheet task 8 | "Calculate one year of A ($60)" | The arithmetic is right ($5 × 12 = $60 vs $48), but the task prints its own answer, so it cannot show whether the learner can do it (CP-21). The more useful question is when each plan is cheaper: B only if kept 10 months or more ($50 > $48). | Medium |
| 5 | Tasks 5–6; plan "Prepare the room"; "Team lab" | "Write a specific comment on the resource handout. Respond, revise and record the decision." Prep: "Use instructor-provided fictional accounts or a modeled demonstration for cloud tasks." | No handout is supplied and no account exists. Real-time coauthoring needs the file in OneDrive or SharePoint ([Microsoft](https://support.microsoft.com/en-us/word/training/share-a-document)). Comments work in a local Word file: Review › New Comment, reply, then More thread actions › Resolve thread ([Microsoft](https://support.microsoft.com/en-us/office/using-modern-comments-in-word-edc6ae71-0a2d-49fe-8faa-986f1e48136a)). A seat swap gives an account-free asynchronous exchange. | Medium |
| 6 | Slide 13 | "Use version history if a useful edit is lost." | True only for files saved online: "Version history in Microsoft 365 only works for files stored in OneDrive or SharePoint" ([Microsoft](https://support.microsoft.com/en-us/office/collab-files/view-previous-versions-of-office-files)). | Low |
| 7 | Slide 3 | "Separate credentials; use a trusted password manager and multifactor authentication where available." | Correct advice ([CISA MFA](https://www.cisa.gov/MFA); [CISA passwords](https://www.cisa.gov/secure-our-world/use-strong-passwords)), but both terms are undefined at first use; MFA is spelled out only on slide 7 (CP-11). | Low |
| 8 | Slide 6 | "Scheduled send can help, but verify its settings…" | Undefined term. It exists in Outlook.com and new Outlook (arrow next to Send › Schedule send) ([Microsoft](https://support.microsoft.com/en-us/outlook/schedule-send-for-outlook-on-the-web)) and Gmail, where "Your emails will be sent based on the timezone you schedule them in" ([Google](https://support.google.com/mail/answer/9214606?hl=en&co=GENIE.Platform%3DDesktop)). | Low |
| 9 | Slide 5; worksheet | Reply all is not on any slide or task. | ch4 teaches it correctly. Reply all goes to "the original sender and all other recipients on the To and Cc lines" ([Microsoft](https://support.microsoft.com/en-us/outlook/reply-to-or-forward-an-email-message)); "If people reply all to a message, people in 'Bcc' won't see the reply" ([Google](https://support.google.com/mail/answer/2819488?hl=en&co=GENIE.Platform%3DDesktop)). DL1 week 3 calls Reply all "the most common veteran email mistake". | Low |
| 10 | Slide 18; scene (4,18) | "Review purchase controls and receipts." | GS6 5.2.3 asks for security concerns. Google Play asks for verification on each purchase by default and lets you change it ([Google](https://support.google.com/googleplay/answer/15711295?hl=en&co=GENIE.Platform%3DDesktop)); "When you uninstall an app, your subscription won't cancel" ([Google](https://support.google.com/googleplay/answer/7018481?hl=en&co=GENIE.Platform%3DDesktop)). | Low |
| 11 | Slide 14 | "A webinar usually gives hosts more control than a small meeting." | Correct: webinar attendees are "view-only participants who can be unmuted if the host chooses" and interact "through the Q&A and the chat" ([Zoom](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0065551)). Add how an attendee asks a question. | Low |
| 12 | Slide 14 practice meeting | Buttons read "Mute microphone" + pressed when the mic is on, and "Lower hand" + pressed (AX-13). | A screen reader hears a label and a state that disagree. Keep a static label and let `aria-pressed` carry the state. | Low |
| 13 | Plan "Prepare the room"; "Facilitation and access"; agenda | "…a word processor and spreadsheet app." "Pair a driver and coach, then switch." "Switch roles." | Week 4 uses no spreadsheet; it needs Word comments, a headset microphone and a decision on accounts. The template text is shared by all six plans (`build-pages.py` `PREP` and plan template). The uncommitted working tree already replaces the driver-and-coach sentence with "Every learner works at their own workstation; a partner coaches but does not take over." | Low |
| 14 | ch2 at 1:28 | While the prompt "Pause and choose a channel…" plays, the caption line reads "Timing · Enough context for a later reply". | The on-screen line hints at the answer before learners think (frame 1:28). | Low |
| 15 | ch10 | Diagram "Saved work → Test evidence → Next step; Show the result. Explain why you trust it." | Reused from week 2 ch10 (SSIM 0.97, VM-21); "Test evidence" does not match the coordination narration. | Low |
| 16 | Post-test, 6.1 feedback pair | Post item repeats slide 13's "Add the contact number after the steps" example (AS-08). | The post-test should use a new situation. The 6.2 pair tests recording consent on the pre-test and muting on the post-test (AS-09). | Low |

**Totals:** High 0, Medium 5 (rows 1–5), Low 11 (rows 6–16). Week 4 audio is also off-spec (185 kbps, not normalized; VM-17), which is not a content issue.

**Verified as correct**
- **To, Cc, Bcc (slide 5; ch4 2:22–2:38):** "Other people who receive the message don't see whose address is on the Bcc line", and "Only the sender of a message can see the names of Bcc recipients" ([Microsoft](https://support.microsoft.com/en-us/outlook/mail/show-hide-and-view-the-bcc-blind-carbon-copy-field-in-outlook-for-windows)). Bcc does not encrypt or stop forwarding.
- **ch4 Reply all note (2:39):** "If the partner clicks Reply all, it reaches you, the organizer and the class list, but not Bcc." Correct ([Microsoft](https://support.microsoft.com/en-us/outlook/reply-to-or-forward-an-email-message); [Google](https://support.google.com/mail/answer/2819488?hl=en&co=GENIE.Platform%3DDesktop)).
- **Timing (slide 6; ch4):** state a response time, consider working hours; scheduled send exists in the major services (row 8).
- **Actionable email (slide 4; ch3):** specific subject, one request, context, response time, check recipient and attachment. Matches pre/post 5.1.
- **Inclusive language (slide 7):** preferred name, explain abbreviations, avoid assumptions about age or ability. Matches pre/post 2.2.
- **Community (slides 8–9; ch8):** members' posts are not verified service information; confirm eligibility and hours with the organization.
- **Synchronous vs asynchronous (slide 11; ch5):** correct definitions; matches pre/post 6.1.
- **Comments (slides 12–13; ch6):** a useful comment names location, change and reason; resolve after the issue is addressed. Resolving "hides it from active review but does not delete it" ([Microsoft](https://support.microsoft.com/en-us/word/mark-comments-as-done)).
- **Meetings (slide 14; ch7):** test the intended speaker and microphone in the app, mute, raise hand or chat, captions, ask before recording, backup plan. Teams captions: More › Language and speech › Show live captions ([Microsoft](https://support.microsoft.com/en-us/teams/meetings/use-live-captions-in-microsoft-teams-meetings)).
- **Trials and in-app purchases (slides 18, 20; ch9):** check renewal price, timing and cancellation; small purchases add up; a free download does not make features free.
- **Arithmetic:** $10 + $2 = $12 (slide 17); 3 × $2 = $6 (slide 18); $5 × 12 = $60 vs $48 (task 8).
- **Knowledge-check keys:** slide 19 (index 2) and slide 20 (index 0) are correct.
- **Fictional data:** `example.invalid` addresses and 304-555-01xx numbers (frames 2:22, 4:11).
- **Transcript step lists** equal the on-screen action labels for ch4 and ch6 (frames match `screen-share-actions.json`).

**Lab quick card (proposal `lab_paths`), each row checked against an official page**

| Row | Steps verified | Source |
|:--|:--|:--|
| Check which account you are using | Edge profile picture opens a menu with the signed-in profile; "Manage profile settings". Microsoft places the icon at the top right; the row says "at the top of the window" in case the layout moves. | [Microsoft Edge](https://www.microsoft.com/en-us/edge/learning-center/how-to-add-new-profiles); [Microsoft](https://support.microsoft.com/en-us/topic/sign-in-and-create-multiple-profiles-in-microsoft-edge-df94e622-2061-49ae-ad1d-6f0e43ce6435) |
| Add Cc or Bcc to an email | Outlook.com: "select Cc or Bcc on the right side of the To line". New Outlook: Options › Show fields › Show Bcc. Gmail: Cc and Bcc fields on the To line. | [Microsoft](https://support.microsoft.com/en-us/office/create-reply-to-or-forward-email-messages-in-outlook-com-5a240eb5-8840-4146-b5e8-b078dce6e5e4); [Microsoft](https://support.microsoft.com/en-us/outlook/mail/show-hide-and-view-the-bcc-blind-carbon-copy-field-in-outlook-for-windows); [Google](https://support.google.com/mail/answer/2819488?hl=en&co=GENIE.Platform%3DDesktop) |
| Reply or Reply all | Reply = sender only; Reply all = sender plus To and Cc; Bcc never receives a Reply all. | [Microsoft](https://support.microsoft.com/en-us/outlook/reply-to-or-forward-an-email-message); [Google](https://support.google.com/mail/answer/2819488?hl=en&co=GENIE.Platform%3DDesktop) |
| Schedule an email | Outlook: "select the dropdown next to the Send button and choose Schedule send". Gmail: "click the down arrow next to Send", "Schedule send"; sent in the time zone you schedule in. | [Microsoft](https://support.microsoft.com/en-us/outlook/schedule-send-for-outlook-on-the-web); [Google](https://support.google.com/mail/answer/9214606?hl=en&co=GENIE.Platform%3DDesktop) |
| Add a comment in Word | Review › New Comment, or Ctrl + Alt + M; Post comment or Ctrl + Enter. | [Microsoft](https://support.microsoft.com/en-us/office/using-modern-comments-in-word-edc6ae71-0a2d-49fe-8faa-986f1e48136a) |
| Reply to and resolve a comment in Word | Reply in the comment; More thread actions (···) › Resolve thread. Older Word shows a Resolve button on the comment (not on an official page; the row says "if the comment shows a Resolve button instead"). | [Microsoft](https://support.microsoft.com/en-us/office/using-modern-comments-in-word-edc6ae71-0a2d-49fe-8faa-986f1e48136a); [Microsoft](https://support.microsoft.com/en-us/word/mark-comments-as-done) |
| Share a Word file to write together | "In the top right corner, above the ribbon, select Share. Save your document in OneDrive, if it's not already there", enter names, set permissions, Send. | [Microsoft](https://support.microsoft.com/en-us/word/training/share-a-document) |
| See earlier versions of a Word file | OneDrive or SharePoint only. Microsoft 365: select the file title › Version history. Office 2021 and earlier: File › History. | [Microsoft](https://support.microsoft.com/en-us/office/collab-files/view-previous-versions-of-office-files) |
| Test your headset microphone | Start › Settings › System › Sound; in Input choose the device and the arrow to its right; Start test; Stop test. The page applies to Windows 11 and Windows 10. | [Microsoft](https://support.microsoft.com/en-us/windows/hardware/drivers/how-to-set-up-and-test-microphones-in-windows) |
| Mute and raise your hand | Teams: Ctrl + Shift + M, Ctrl + Shift + K. Zoom: Alt + A, Alt + Y. | [Microsoft](https://support.microsoft.com/en-us/accessibility/teams/keyboard-shortcuts-for-microsoft-teams); [Zoom](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0067050) |
| Turn on meeting captions | Teams: More actions › Language and speech › Show live captions. Zoom: Show captions, or More › Show captions, if the host has not restricted them. | [Microsoft](https://support.microsoft.com/en-us/teams/meetings/use-live-captions-in-microsoft-teams-meetings); [Zoom](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0059762) |
| Cancel a subscription | Microsoft: account.microsoft.com/services › Manage › Cancel. Google Play: subscriptions › Manage › Cancel subscription; uninstalling does not cancel. | [Microsoft](https://support.microsoft.com/en-us/accounts-billing/subscriptions/cancel-your-microsoft-subscription); [Google](https://support.google.com/googleplay/answer/7018481?hl=en&co=GENIE.Platform%3DDesktop) |

## Does the content make sense for this audience?

**Undefined terms at first use**
- "password manager", "multifactor authentication" (slide 3; spelled out only on slide 7 as an abbreviation example).
- "scheduled send" (slide 6).
- "webinar" (slide 14): an online talk where the host speaks and attendees mostly watch.
- "coauthoring" (slide 11 card; used in week 2 task 7 two weeks earlier).
- "payment service" (slide 17), and no word at all for digital wallets or person-to-person apps.
- "Synchronous" and "asynchronous" are defined well on slide 11 and in ch5.

**Logic leaps**
- Slides 8–9 (community) interrupt the email-to-collaboration thread; the video teaches them after meetings.
- Slide 16 puts "Streaming delivers media…" between goods/services and subscriptions with no link, and no example.
- Slide 17 jumps from "A payment service sends an authorized payment request" to a checklist, without saying what the learner is choosing between.

**Missing steps**
- No real click path anywhere for Cc/Bcc, Reply all, scheduled send, adding or resolving a comment, sharing a file, version history, testing a microphone, meeting mute or captions, or cancelling a subscription. The proposal's quick card adds all of these.

**Tasks impossible or unreliable as written**

| Task | Problem |
|:--|:--|
| Task 2 | Says "Do not send it" but not where to write it. |
| Task 3 | Two skills in one ("Explain To, Cc and Bcc. Choose an appropriate time and account"), with no recipients to place. |
| Task 4 | No sentence is supplied to revise. |
| Task 5 | "justify access" is a decision; "coauthoring" cannot be done without an account. |
| Task 6 | "the resource handout" is not supplied; no tool named. |
| Task 7 | A written list only; no one uses the practice meeting controls. |
| Task 8 | Prints its own answer. |

**Pacing is unrealistic in three places**
- 10–30: eight slides, six with simulations, in 20 minutes.
- 60–80: eight slides plus the 7:20 video in 20 minutes (about 1.6 minutes per slide with no time for the four pauses).
- 80–110: four tasks with a role switch, including a shared-document role play with no document.

**Earlier findings re-checked**

| Earlier finding | Status | Evidence |
|:--|:--|:--|
| CP-21: task 8 gives away "($60)" | **Confirmed** | Worksheet task 8 text. |
| CP-12: payment service explained without cards vs wallets vs P2P; streaming has no examples | **Confirmed** | Slides 16–17; ch9. Sources in rows 1–2. |
| CP-19 / IR: "Collaboration and commerce" overloaded | **Confirmed** | 20 minutes for 8 slides, 4 demos and the 7:20 video. |
| CP-02 / IR-07: week 4 coauthoring needs accounts; demo account not listed | **Confirmed** | Prep text; no handout ships with the course. |
| CP-08 / AS-11: throwaway distractors on slides 19–20 | **Confirmed** | All four wrong answers are in the test's "silly" list. |
| CP-11: MFA, password manager, scheduled send undefined | **Confirmed** | Slides 3 and 6. |
| CP-10: 5.2.4 and 6.1.1–6.1.2 not covered | **Confirmed** | Rows 2–3. |
| VM-01: prompts give no thinking time | **Confirmed** | 1:28.6 (0.82 s, then the answer), 2:53.5 (0.94 s, then the instruction; the demo removes recipients at 2:54.5), 4:21.9 (0.34 s), 6:34.8 (1.9 s, then ch10). |
| VM-02: ch6 demo at 177.6 wpm | **Confirmed** | ch6 states change at 3:49, 3:54, 3:58, 4:09, 4:10, 4:13; "Author adds the fictional help number" is visible for 1.22 s. |
| VM-17: week 4 audio 185 kbps | **Confirmed** (from the review; not re-measured) | — |
| AX-13: slide 14 toggle labels | **Confirmed** from `workshop.js` behaviour described in the review | — |

**New in this review**
- DL1 week 3 already taught Reply all, Bcc, inclusive language and collaboration etiquette; week 4 never recalls it.
- The email Show (ch2–4) plays after the email Do.
- Slides 8–9 are in no plan phase and have no task.
- Task 4 has no sentence and task 7 has no hands-on step.
- ch4's prompt at 2:54 is followed 0.9 s later by the demo doing the task, so the pause must be exact.
- ch2's caption hints the answer during the prompt.
- Collaboration tools (6.1.1) are never named.

## Video structure

**Sequence.** Ten chapters of 38–48 seconds: purpose (ch1) → channel and identity (ch2) → actionable message (ch3) → recipients and timing (ch4, demo) → one shared copy (ch5) → feedback (ch6, demo) → meeting (ch7) → community (ch8) → purchase (ch9) → record the next step (ch10). The order follows the slides except community, which the slides teach before collaboration (slides 8–9) and the video teaches after meetings (ch8). Captions are a separate VTT track, on by default.

**Model → prompt → answer, chapter by chapter**

| Chapter | Slides | Model | Prompt and gap | Rating |
|:--|:--|:--|:--|:--|
| ch1 0:00–0:48 | 1 | Photo of three older adults at a laptop, then the Owner/Writer/Reviewer → One copy diagram (frames 0:03, 0:24). | — | Good hook |
| ch2 0:48–1:36 | 2–3 | Diagram: Active profile: Training; Message, Shared file, Meeting (frame 1:12). | "Pause and choose a channel…" ends 1:28.6; the answer follows **0.82 s** later. The caption line hints the answer (frame 1:28). | Good question, no think time |
| ch3 1:36–2:19 | 4 (7) | Diagram of a three-line request (frames 1:42, 1:58). | — | Tell with a visual |
| ch4 2:19–3:05 | 5–6 | **Screen demo, 6 steps**: inspect → Cc visible → Bcc hides → Reply all note → remove class list and Bcc → reply by Thursday 3 PM (frames 2:18–2:58). Text in the practice window is 26–28 px in a 1:1 1200×500 panel (`screen-share-scenes.py` `email()`, `.screen-state`), above the course's 24 px floor. | "Pause and review your fictional draft." ends 2:53.5; the instruction follows at 2:54.5 and the demo removes the recipients at the same moment. | **Strong**, but pause exactly at 2:54 |
| ch5 3:05–3:50 | 10–11 | Diagram: three "Final" copies → one shared handout (frames 3:15, 3:32). | — | Tell with a visual |
| ch6 3:50–4:28 | 12–13 | **Screen demo, 6 steps**: vague comment → specific comment → Add comment → author adds 304-555-0142 → "Author: Added — thank you" → Resolved ✓ (frames 3:52–4:16). The new comment text swaps in rather than being typed. 177.6 wpm. | "Pause and write one useful comment…" ends 4:21.9; the next instruction follows 0.34 s later. | **Strong** model, fast |
| ch7 4:28–5:11 | 14 | Diagram: You, Host, headset, muted mic, raised hand (frames 4:50, 5:01). No real meeting app. | — | Tell with a visual |
| ch8 5:11–5:54 | 8–9 | Diagram: Community draft / Source check (frames 5:22, 5:30, 5:45). | — | Tell with a visual |
| ch9 5:54–6:37 | 16–18, 20 | Diagram: Trial today → $12 each month; "Seller · renewal · cancellation" (frames 5:58, 6:10, 6:20). No payment method, no streaming example. | "Pause and name the fact you would need…" ends 6:34.8; ch10 starts **1.9 s** later. | Good question, no think time |
| ch10 6:37–7:21 | 21–22 | Reused "Saved work → Test evidence → Next step" diagram (frames 6:52, 7:10). | Transfer prompt at 7:06. | Adequate |

**Coverage gaps.** No chapter shows scheduled send, inclusive-language rewriting beyond one sentence, version history, a real meeting app's controls, streaming services or how to pay. Only ch4 and ch6 model the task learners will do.

**Where it should play.** Chapter by chapter as the Show inside each cycle (below), with the instructor pausing at **1:29, 2:54, 4:22 and 6:35**. Slide 15 stays as the chapter menu for replays; the whole video is home review (captions and transcript are available).

## Recommended restructure

A 120-minute running order of five Tell, Show, Do, Review cycles inside the WIPPEA stages. It uses only current slides, chapters and a rewritten worksheet. "Live" means the instructor shows it on the projector. Nothing needs an account; anything account-based is shown only from a demonstration account or as the slide simulation, marked simulated.

| Min | WIPPEA | Tell, Show, Do, Review | Slides | Video (pause) | Worksheet / check | Notes |
|:--|:--|:--|:--|:--|:--|:--|
| 0–10 | W | Logins; text size and navigation. Report last week's home task. Recall DL1 week 3 (Reply, Reply all, Forward) and DL2 week 2 (Commenter access). Click through the slide 1 feedback practice. | 1 | — | — | Board: learners' Reply all stories. |
| 10–15 | I | Read the five goals aloud. Play ch1. Each pair names a group task and a message that went wrong. | 1 | ch1 | — | Each cycle returns to these stories. |
| 15–33 | P → P → E | **Cycle A, channel, account and a clear email.** Tell: slides 2–4 (define password manager and MFA). Show: ch2 (**pause at 1:29**), ch3, slide 4 draft. Do: tasks 1 and 2, every learner, draft typed in the worksheet box. Review: partner reads the draft as the recipient. | 2, 3, 4 | ch2, ch3 | Tasks 1, 2 | Nothing is sent. |
| 33–45 | P → P → E | **Cycle B, recipients, timing and respectful wording.** Tell: slides 5–7. Show: ch4 demo (**pause at 2:54**, ask which recipients to remove, then read the next line aloud); slides 5–6 practice views; rewrite "Pls RSVP ASAP" aloud. Live Cc, Bcc and Schedule send only from a demonstration account. Do: tasks 3 and 4, every learner. Review: "Who gets Sam's Reply all?"; check each learner's To, Cc and Bcc lines. | 5, 6, 7 | ch4 | Tasks 3, 4 | Slides count as simulated. |
| 45–55 | — | Break | — | — | — | Screen-free. |
| 55–73 | P → P → E | **Cycle C, one shared copy and useful feedback.** Tell: slides 10–13 (name Word with OneDrive and Google Docs; version history needs a file saved online). Show: ch5, ch6 (**pause at 4:22**), then live in Word: comment, reply, change, resolve. Do: task 5 (pair decision), task 6 in Word, every learner, by swapping seats. Review: slide 19; partner checks place, change and reason. | 10, 11, 12, 13, 19 | ch5, ch6 | Tasks 5, 6 | Leave Word open for the individual check. |
| 73–85 | P → P → E | **Cycle D, meetings, webinars and communities.** Tell: slide 14, then jump back to slides 8 and 9. Show: ch7, ch8; live microphone test in Settings › System › Sound. Do: task 7, every learner (slide 14 controls, mic test, habits list). Review: "How do you ask a question in a webinar?" (Q&A or chat); each list includes asking before recording. | 14, 8, 9 | ch7, ch8 | Task 7 | Use the sidebar to jump. |
| 85–100 | P → P → E | **Cycle E, purchases, subscriptions and payments.** Tell: slides 16–18 (streaming examples; card vs wallet vs person-to-person app). Show: ch9 (**pause at 6:35**), slide 17 checkout. Do: task 8, every learner. Review: slide 20; "A caller wants $300 by Zelle today to keep your benefits. What do you do?" | 16, 17, 18, 20 | ch9 | Task 8 | No real store or payment page. |
| 100–112 | E | **Individual check.** ch10 if time allows. Each learner shows three things: To, Cc and Bcc from task 3 and who a Reply all reaches; the answered and resolved comment in Word; the one-year cost of offer A with a payment choice. Mark Independent / With prompt / Needs practice on the roster. | 21 | ch10 | Roster | Re-model only the missing step. |
| 112–120 | A | Home task: one real subscription, its renewal date and how to cancel, reported at week 5. Close Word without saving; restore settings; **Start fresh on this computer**. | 22, 23 | — | — | No amounts or account numbers. |

Timing check: 10 + 5 + 18 + 12 + 10 + 18 + 12 + 15 + 12 + 8 = 120 minutes.

**Moved or optional**
- The 30–50 and 80–110 labs dissolve into the cycles.
- Slide 15 becomes the replay menu, not a block.
- Slides 8–9 are taught with slide 14 (sidebar jump; slide order unchanged).
- **Tight spots:** Cycles A and C (18 minutes each). If running long, make task 5 oral and skip the live microphone test in Cycle D. Do not cut the Do in C or E.

## Top 10 changes, ranked

| # | Change | Where | Why (Tell/Show/Do/Review, WIPPEA or andragogy) | Effort | Source file to edit |
|:--|:--|:--|:--|:--|:--|
| 1 | Replace the 7-row agenda with five cycles (A–E) that name the slides, chapters, pause times (1:29, 2:54, 4:22, 6:35) and tasks, with "every learner" for each Do. | Lesson plan agenda; slide 15 role | Each skill group gets its own Tell → Show → Do → Review; the email Show moves before the email Do; chunking for older learners | Medium | `author-content.py` week 4 `agenda` (proposal) |
| 2 | Rewrite the worksheet so every task is doable in the lab without an account: named recipients (task 3), a sentence to fix (task 4), a two-step handout and a seat swap in Word (task 6), the slide 14 controls and a mic test (task 7), and task 8 without "($60)" and with a payment choice. | Worksheet and answer guide | The Do must be possible and must evidence the objective; fixes CP-21 and CP-02 | Small | `author-content.py` week 4 `lab`, `answers` |
| 3 | Explain payments on slide 17: credit card (dispute), digital wallet (saved card), person-to-person apps (hard to get back; people you know). Add a "Method" choice to the checkout scene. Add the Zelle phone-call question to the Cycle E Review. | Slide 17; scene (4,17) | IC3 5.2.2; directly relevant to scams aimed at older adults | Small | `author-content.py` slide body; `scenes.py` and `photo_scenes.py` (4,17) |
| 4 | Rewrite the objectives as five ABCD outcomes and add the missing meetings/community group; move "digital identities" to the channel objective. Design the individual check first. | Slide 1; lesson plan outcomes | WIPPEA Introduction and Evaluation; backward design | Small | `author-content.py` week 4 `objectives`, `outcomes` |
| 5 | Replace the throwaway knowledge-check options with believable mistakes of similar length, and add a Review in every cycle plus a 3-item individual check on the roster. | Slides 19–20; 100–112 | WIPPEA Evaluation; respect (self-concept) | Small | `author-content.py` slide `options`, `answer`, `why` |
| 6 | Add a Windows 11 lab quick card: account check, Cc/Bcc, Reply all, schedule send, Word comment, reply and resolve, share, version history, mic test, meeting shortcuts, captions, cancel a subscription. | Lesson plan and worksheet | The Show must match the Do; learners need the path at home | Small | `author-content.py` week 4 `lab_paths` |
| 7 | Warm-up that uses DL1 week 3 and DL2 week 2, and a home task on a real subscription reported at week 5. | 0–10; 112–120 | WIPPEA Warm-up and Application; the experience principle | Small | `author-content.py` agenda |
| 8 | Fill the IC3 gaps and define terms: streaming examples (slide 16 and scene), collaboration tools and benefits (slides 10–11), version history needs a file saved online (slide 13), MFA and password manager (slide 3), scheduled send (slide 6), Reply all (slide 5), webinar Q&A (slide 14), purchase verification and "deleting an app does not cancel" (slide 18). | Slides 3, 5, 6, 10, 11, 13, 14, 16, 18 | The Tell must be accurate and complete; CP-10, CP-11, CP-12 | Small | `author-content.py` slide bodies and cards; `scenes.py`/`photo_scenes.py` (4,16), (4,18) |
| 9 | A week 4 prep list: Word comments checked, headset microphones, calculator or paper, the account decision ("demonstration account, never your personal inbox"), rehearsed pauses, Start fresh. Keep the working-tree fix that replaces "Pair a driver and coach, then switch." | Lesson plan | Instructor readiness; account-free path; every learner does the task | Small | `author-content.py` `prep`; `build-pages.py` facilitation text |
| 10 | Video and assessment polish: silent holds after the four prompts, hold ch4's full recipient list until after the pause, a payment-method line and streaming example in ch9, typed text in ch6, ch6 below 150 wpm, AAC 128k audio; post-test feedback item in a new situation and the 6.2 pair on one subskill; static labels on the slide 14 buttons. | Video; post-test; `workshop.js` | Think time (Knowles: time to try); test transfer, not recall; accessible Do | Small (a11y, test) / large (re-render) | `video-scenes.py`, `screen-share-scenes.py`, narration; `author-assessments.py`; `assets/workshop.js` |

## Gemini claims checked

**Video review (`week-04-video-gemini-3.1-pro-preview.md`)**

| Claim | Verdict | Evidence |
|:--|:--|:--|
| Prompts at 1:24, 2:51, 4:18, 6:30 leave 3–5 s before the video continues | **Agree on the finding, disagree on the numbers** | Gemini gave the start of each prompt. The prompts end at 1:28.6, 2:53.5, 4:21.9 and 6:34.8, and the narration continues after 0.82, 0.94, 0.34 and 1.9 s. ch2 gives the answer; ch4's demo removes the recipients 0.9 s after its prompt. |
| Text in the simulated interfaces (e.g. "organizer@example.invalid" at 2:18) is too small at 720p | **Disagree** | The practice window text is set at 26–28 px in a 1200×500 panel placed 1:1 in the 1280×720 composition (`screen-share-scenes.py` `email()`, `txt(value,…,28)`, `.screen-state{width:1200px}`); `check-text-floor.py` passes with 0 sizes under 24 px. Projector legibility depends on the room. |
| "The standard white cursor is quite small" | **Disagree** | The pointer is a 35×45 px gold arrow with a navy outline and a red click ring (`screen-share-scenes.py` `.pointer`, `.click-ring`; frames 2:22–2:58). |
| The comment text appears instantly at 3:54 | **Agree** | `feedback()` swaps state 0 → 1; no typing animation. Low. |
| The abstract email and document windows may not transfer to Gmail or Outlook | **Agree** | Hence the live Show from a demonstration account (optional) and the quick card. |
| Email addresses in To and Cc are not read aloud | **Agree** | ch4 narration names roles, not addresses. Read the addresses aloud during the pause. |
| 0:00 opens with a photograph of three older adults at a laptop | **Agree** | Frame 0:03. |
| At 6:10 "12 dollars each month" is highlighted in a green box when "renewal timing" is said | **Partly** | The green box reads "Seller · renewal · cancellation" and is on screen for all of ch9; only the caption line changes to "Renewal · 12 dollars each month" (frames 5:58, 6:10, 6:20). |
| 2:26 the pointer moves to the Cc line as it is narrated | **Agree** | Action at 146.2 s (2:26), phrase "Cc sends a visible copy". |
| Speech rate is calm and appropriate | **Partly disagree** | The week averages 153.6 wpm; ch6, a screen demo, runs at 177.6 wpm, and one step label is visible for 1.22 s (VM-02, VM-06). |
| Accuracy 4/5; concepts technically sound | **Agree** | See "Verified as correct". Gemini did not notice the missing payment and streaming content. |
| Skip chapter 10 if short on time | **Agree** | ch10 is a recap; the running order makes it optional at the individual check. |
| Captions are not burned in | **Agree** | They are a separate VTT track, on by default. |

**Structure review (`week-04-structure-gemini-3.1-pro-preview.md`)**

| Claim | Verdict | Evidence |
|:--|:--|:--|
| Big Tell/Show blocks followed by long labs; restructure into five short cycles | **Agree** | 10–30 / 30–50 and 60–80 / 80–110. The proposed cycles are close to Gemini's, with community taught with meetings. |
| Add the 25-minute pre-test at the start | **Disagree** | The pre-test is in week 1 (10–35) and the post-test in week 5. Week 4 has no test. |
| Delete slide 15 | **Disagree** | Slide count and kinds must stay the same. Slide 15 is the chapter menu for replays; the fix is in the agenda, which no longer plays the whole video. |
| Move slides 8–9 after slide 14 | **Agree on teaching order, not on moving slides** | Slide order is fixed; the instructor jumps back with the sidebar, which also matches the video (ch8 after ch7). |
| Warm-up "Adequate" (activates week 3) | **Partly** | It recalls week 3's product but not DL1 week 3, which taught Reply all, inclusive language and etiquette. Rated Weak. |
| Introduction "Strong" | **Disagree** | Objectives are not measurable and miss the meetings/community group; ch1 is not scheduled. Rated Adequate. |
| Evaluation "Adequate": checks directly measure the objectives | **Disagree** | Both checks have throwaway wrong answers; the email objective has no check; task 8 prints its answer. Rated Weak. |
| Application "Strong" | **Partly** | ch10 has a transfer prompt and week 5 follows up, but there is no home task. Rated Adequate. |
| Split worksheet task 3 | **Agree in part** | Task 3 now gives a concrete recipient scenario; the explanation of To/Cc/Bcc moves into the Review. The account choice stays with the notice it belongs to. |
| Clarify shared-document logistics | **Agree** | No handout or account exists. The account-free path is a local Word file and a seat swap. |
| Inclusive language has no Show | **Partly** | Slide 7's scene shows three examples and ch3 has one sentence; the instructor adds a live rewrite of "Pls RSVP ASAP". |
| Add an email knowledge-check slide after slide 7 | **Disagree** | Slide count is fixed. The email objective is checked in the Cycle B Review and the individual check. |
| "No errors found" in the content | **Agree for what is taught; missed the gaps** | No false statement was found. Gemini missed the payment, streaming and collaboration-tool gaps and the undefined terms. |
| Adult learning: Experience "Strong" | **Disagree** | The lesson never uses DL1 week 3, which taught the same email and etiquette skills. Rated Weak. |
| Self-concept "Weak" because of the blocks | **Agree, with another reason** | The throwaway wrong answers also talk down to learners. |
| Prompt the instructor to walk the room during each Do | **Agree** | Each Review names what the partner and the instructor check. |
