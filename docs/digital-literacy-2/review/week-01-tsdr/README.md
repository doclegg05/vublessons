# Week 1 review: Tell, Show, Do, Review + WIPPEA + adult learning

**Lesson:** Digital Literacy Level 2, Week 1, "Make technology work for you". Class Monday 2026-09-28, 4:30–6:30 p.m.
**Framework:** [framework.md](framework.md). **Frame:** Tell, Show, Do, Review as the teaching method, inside the WIPPEA cycle (U.S. Dept. of Education, TEAL Fact Sheet No. 8, adapted from Hunter 1982), with Knowles' adult learning principles.

| Reviewer | What it saw | Cost | Full report |
|:--|:--|:--|:--|
| Gemini 3.1 Pro (OpenRouter) | Video only | $0.17 | [gemini-video.md](gemini-video.md) |
| Gemini 3.1 Pro (OpenRouter) | Video + all Week 1 materials, Tell/Show/Do/Review + WIPPEA | $0.18 | [gemini-structure.md](gemini-structure.md) |
| Claude | Materials, 40+ video frames, captions, and every technical claim checked against Microsoft and Google documentation | — | [claude-structure.md](claude-structure.md) |

---

## Bottom line

**The content is right; the order is wrong.** Every reviewer found the technical content accurate for 2026, with one real problem (calendar task 5) and a handful of imprecise sentences. Every reviewer also found the same structural issue: Week 1 runs as **lecture, then lab**, not as Tell, Show, Do, Review.

- **Tell:** about 15 skills are told in two blocks (20 minutes, then 15 minutes).
- **Show:** the video, the best "Show", plays as one block *after* all the slides. For zoom, learners try it on slide 6 about 30 minutes before the video demonstrates it.
- **Do:** one 30-minute lab covers all 8 tasks, 25–75 minutes after each skill was taught. Partners "switch driver and coach halfway", so each learner does only about half the tasks.
- **Review:** everything is checked together in the last 10 minutes.

**The fix doesn't need new content.** Re-sequence the existing slides, video chapters and worksheet tasks into **five short Tell, Show, Do, Review cycles**, one per skill group, as in the running order below.

---

## Where all reviewers agree (firm findings)

1. **Big blocks, not cycles.** Restructure into short cycles for each skill. (All three structure reviews.)
2. **Play the video chapter by chapter, as the Show,** right after the slide that tells that skill. Don't play it as one block at 65–80. (All three.)
3. **Practice prompts in the video leave no thinking time.** The narrator asks, then answers within about a second, or rolls into the next chapter. **Pause by hand at 1:24, 2:02, 5:36 and 6:28.** (Gemini video review, Claude, and the earlier word-timing measurement.)
4. **Move the knowledge checks into the cycles:** slide 20 after sound, slide 21 after calendar sharing. Don't hold them to the end. (All three.)
5. **The objectives aren't measurable.** Rewrite them in ABCD form: who, what they will do, under what conditions, how well. (All three.)
6. **Slides 8 (browser settings) and 17 (cloud) are told only,** with no practice. Make them optional, or project-only. (Both structure reviews.)
7. **Relevance is strong:** everyday tasks, respectful tone, low-risk fictional practice, and the "workbench and filing cabinet" comparison. The Choose → Test → Restore routine is a good backbone. (All.)
8. **Tie the warm-up to Level 1.** DL1 already taught USB, HDMI and Ethernet, and memory vs storage, and Week 1 re-teaches both without saying so. (Both structure reviews.)

## Where they disagree, and my call

| Topic | Gemini | Claude | My call |
|:--|:--|:--|:--|
| Calendar task 5 (create an appointment) | Doable | **Impossible as written.** Windows Calendar was retired in Dec 2024, the lab has no calendar account, and no slide simulation can create an event. | **Claude.** Verified with Microsoft's retirement notice and the slide code. For Monday, do task 5 on paper, copying the form shown in video chapter 7. |
| Sound-to-picture timing | 5/5, "perfect" | Chapter 5 narrates cables (3:14–3:31) over the memory/storage picture. The video says "Tuesday, October 13", the slides say Monday. Chapter 4's on-screen labels run in a different order from the narration. | **Claude.** I checked the 3:20 frame myself: the narration is about connections, the picture shows processing and storage. Gemini read the video at low resolution. |
| Legibility | 5/5 | Not scored (the earlier review found a few labels under 24 px) | Readable on a projector; take Gemini's perfect score with a grain of salt. |
| Evaluation stage | Adequate | Weak: two checks cover two of three objectives, and there's about 35 seconds of demo per learner | **Weak.** No check covers the connection/printer objective, and the ratings have no record sheet. |
| Application stage | Strong | Adequate: no task on the learner's own device | **Adequate.** Add a home task reported at the Week 2 warm-up. |
| Narration voice | "Synthetic, a bit monotone" (3/5) | Not assessed | This is the AI clone of your voice. Your call on how to introduce it. The monotone note is fair for the fast chapters. |
| Veteran-specific examples | Suggests VA appointments or VFW events | Suggests a small-print benefits letter, a telehealth headset, clinic directions | Both suggest it, independently. It was decided on Sept 24 that DL2 doesn't *require* veteran framing, but a few fictional veteran-life examples would strengthen "need to know". Your call. |

---

## Content correctness (verified against Microsoft and Google sources; details and links in Claude's report)

| Severity | Where | Issue | Fix |
|:--|:--|:--|:--|
| **High** | Worksheet task 5 | "Create a fictional appointment with a reminder": there's no tool on a lab PC without an account | Monday: paper or simulated entry copying ch7's form. Later: an event-builder practice on slide 13, or name the calendar tool and account source |
| Medium | Slide 11 | "A default printer is the device an app initially selects." Chrome and Edge actually open the **most recently used** printer, and Windows 11 may be managing the default. | Say "Always check the printer name in the print window; Windows and browsers may pick the last one you used." Show Settings › Bluetooth & devices › Printers & scanners |
| Medium | Slide 11 | Laser vs inkjet: consumables only, no "which for which job" | Laser: cheaper per page, big text jobs. Inkjet: cheaper to buy, colour and photos |
| Medium | Slide 7 | Brightness/contrast: doesn't say where the controls are. Desktop monitors use their own buttons, and Windows' readability setting is Contrast themes | Add one sentence plus a projector-only Show |
| Medium | Task 8 | "A name that autocorrect changes" won't reliably trigger on a desktop | Use "type *teh* and a space", then Ctrl+Z |
| Low | Slide 8 | Home page vs startup page are different settings in Chrome | Adjust wording |
| Low | Slide 10 | "USB carries data" (USB-A also carries power) | The video's wording is better; copy it |
| Low | Slide 16 | "A rule can… repeat a reminder": that's a recurrence, not a rule (the same wording is in post-test item 3) | Fix both |
| Low | Slides 4–6 | Zoom reset: doesn't mention that Chrome and Edge remember zoom **per site** | Add "reset so the next person isn't surprised" |
| Low | Slide 4 vs video | 125% vs "one step" (110%) | Say "two steps to 125%" |
| Low | Slides 13–15 vs video ch7 | Monday vs Tuesday | Align (needs a re-render) |
| Low | Video ch5 3:14–3:31 | Connections narrated over the storage diagram | Add a connector visual (needs a re-render) |
| Low | Video ch4 | On-screen label order doesn't match the narration | Re-render |
| Low | Lesson plan prep | Lists a spreadsheet app and carries a Week 6 sentence; leaves out the headset, cables, a named page and the calendar plan | Week-specific prep list |

**Verified correct:** zoom shortcuts and behaviour, display scale vs text size paths, sound output and Volume mixer, the browser settings that exist, processor/memory/storage, HDMI/USB-C/Ethernet, print preview and the print queue advice, calendar fields and time zone, free/busy sharing in Outlook and Google, autocorrect/autocomplete, cloud (NIST definition), help requests, and both knowledge-check answers.

---

## Tell, Show, Do, Review by skill (current state)

| Skill | Tell | Show | Do | Review | Gap |
|:--|:--|:--|:--|:--|:--|
| Page zoom | Slide 5 | Slide 6 sim; ch2 demo (strong) | Slide 6; task 2 | Answer guide | Show comes *after* Do; Do delayed |
| Display scaling | Slide 5, ch3 | Diagram only | — | — | Projector-only Show of the real setting |
| Sound output | Slide 7 | Slide 7 sim; ch4 | Task 3 (at 80+ min) | Slide 20 (at 110) | Do and Review delayed; no real Windows Show |
| Brightness/contrast | Slide 7 | — | "Explain" only | — | No Show of where the controls are |
| Browser settings | Slide 8 | Scene | — | — | Tell only |
| Parts and connections | Slides 9–10, ch5 | Flip cards | Task 4 (tasks not listed) | Answer guide | Repeats DL1; the ch5 visual doesn't match |
| Default printer | Slide 11 | — | — | — | Tell only (IC3 1.5.3) |
| Print preview | Slide 12, ch6 | Sim; ch6 diagram | Task 7 (no page named) | Answer guide | Needs a live Ctrl+P Show |
| Calendar entry | Slide 13 | ch7 demo (strong) | Task 5: **impossible** | Answer guide | Do missing |
| Calendar views | Slide 15 | Sim; ch7 | Slide 15; task 6 | Answer guide | OK |
| Free/busy sharing | Slide 14 | Sim; ch8 | Task 6 | Slide 21 | OK, except the video answers before learners can think |
| Automation | Slide 16 | Scenes | Task 8 (unreliable trigger) | Answer guide | Needs a live "teh" Show |
| Cloud / help | Slides 17, 19; ch9 | Scenes | Task 8 part 2 | Answer guide | Not scheduled in any lesson-plan block |

---

## Recommended Monday running order (five Tell, Show, Do, Review cycles inside WIPPEA)

Based on Claude's plan, with my adjustments. It uses only existing slides, chapters and worksheet tasks. **Live** = you demonstrate on the projector in the lab's real browser or Windows.

| Min | WIPPEA | What happens | Slides | Video | Worksheet |
|:--|:--|:--|:--|:--|:--|
| 0–10 | Warm-up + Intro | Logins; show text size and navigation. **Warm-up:** hold up HDMI, USB and Ethernet cables: "What did we use these for in Level 1?" Pair-share slide 2. Read the objectives aloud. | 1, 2 | — | Task 1 |
| 10–35 | (Diagnostic) | **Pre-test.** Learners type their name first. **Record each score out of 28 on your roster**; print page 1 only if needed. Early finishers read slide 4; late finishers may run to 38. | 3 | — | — |
| 35–38 | Intro | **Tell** the Choose → Test → Restore routine | 4 | ch1 (0:00–0:39) | — |
| 38–50 | P → P → E | **Cycle A, reading comfort.** Tell: slide 5 · Show: ch2 + live Ctrl + in Edge · Do: slide 6 and task 2, *every learner at their own seat* · Review: partner confirms reset to 100%. Then Tell/Show only: ch3 (**pause at 2:02** for the prediction) + live Settings › System › Display › Scale. | 5, 6 | ch2, ch3 | Task 2 |
| 50–60 | P → P → E | **Cycle B, hearing and screen.** Tell: slide 7 · Show: ch4 + live Quick Settings sound output · Do: task 3 with a headset · Review: **slide 20** knowledge check. Point to the monitor's brightness buttons; don't change them. | 7, 20 | ch4 | Task 3 |
| 60–70 | — | Break (screen-free) | — | — | — |
| 70–80 | P → P → E | **Cycle C, connections and printing.** Tell: slides 11–12 (say the laser/inkjet use cases) · Show: ch6 + live Ctrl+P on page 1 of the worksheet (printer name, Pages = 1, Copies = 1) · Do: task 7 (**don't print**) and task 4 (find one real port) · Review: partner reads back printer and pages; ask aloud "laser or inkjet for 200 flyers?" | 11, 12 | ch6 | Tasks 4, 7 |
| 80–95 | P → P → E | **Cycle D, calendar.** Tell: slides 13, 15 · Show: ch7 · Do: **task 5 on paper**, copying ch7's form (title, day, start/end, place, reminder) and marked "simulated"; switch views on slide 15 · Tell/Show: slide 14 + ch8 (**pause at 5:36**) · Do: task 6 · Review: **slide 21**; partner checks the five fields. | 13, 15, 14, 21 | ch7, ch8 | Tasks 5, 6 |
| 95–103 | P → P → E | **Cycle E, automation and help.** Tell: slides 16, 19 · Show: ch9 + live Word "teh" + space → "the", then Ctrl+Z · Do: task 8 · Review: partner gives one specific piece of feedback. | 16, 19 | ch9 | Task 8 |
| 103–113 | Evaluation | **Individual check.** Play ch10 (**pause at 6:28**). Each learner shows you 3 things: (1) zoom and reset; (2) choose the headset and test; (3) print preview page 1 on the right printer. Mark Independent / With prompt / Needs practice on the roster. | — | ch10 | Roster |
| 113–120 | Application | Slides 23–24. **Home task:** "On your own device, make one change from today, write down how you undid it, and tell us at the start of Week 2." Restore lab settings, then **Start fresh on this computer**. | 23, 24 | — | Print or save the worksheet |

**Optional or skipped:** slide 8 (browser settings) as a fast-finisher extension. Slide 9 and ch5 (DL1 covered them). Slide 17 (cloud) as one sentence, or move it to Week 2. Slide 18 becomes a replay menu, not a block. Partners **coach but never take over**.

**Tight spots:** cycle A (12 min) and cycle D (15 min) are full. If you're running long, drop the display-scaling Show in A and the slide 15 view switching in D.

---

## Objectives rewritten (ABCD)

1. **Settings:** On a lab workstation with Edge or Chrome, each learner enlarges a webpage with browser zoom and returns it to 100% (Ctrl + 0), selects the headset as sound output and confirms it with a test, and says which control (page zoom, display scale, brightness) fits a described reading problem. All three are correct with at most one prompt, and settings are restored.
2. **Calendar:** Using a calendar form (a real account or the course practice), each learner creates a fictional event with title, day, start and end, place and reminder, reopens it to confirm all five, and chooses free/busy sharing for a partner, explaining what the partner will see.
3. **Connections and printing:** Given three jobs (external screen, wired network, flash drive), each learner matches HDMI, Ethernet and USB and finds one real port. They then open print preview for page 1 of the worksheet, confirm the printer's name, and set Pages = 1 and Copies = 1 without printing.
4. **New (IC3 1.3):** The learner triggers an AutoCorrect change ("teh" → "the"), undoes it with Ctrl+Z, and says in one sentence what a mail rule and a cloud service do.
5. **New (IC3 2.3):** The learner writes a help request naming the app, the task, what they tried and the exact message.

---

## What to fix, and when

**Before Monday: I can do these in the course scripts (small, one PR):**
1. Rewrite the Week 1 lesson-plan agenda as the five-cycle running order above, with pause times, slide numbers and "every learner does it".
2. Rewrite the objectives in ABCD form, and add the two missing ones.
3. Worksheet inputs:
   - Task 4: list the three jobs.
   - Task 7: name "page 1 of this worksheet" and say "don't print".
   - Task 8: "teh" + space, then Ctrl+Z.
   - Task 5: add "if you have no calendar app, fill in the form on paper".
4. Slide wording fixes:
   - Slide 11: the default-printer sentence and when to use laser vs inkjet.
   - Slide 7: where the brightness controls are.
   - Slide 10: USB power.
   - Slide 16: the "rule" wording.
   - Slides 4–6: zoom is remembered for each site.
5. Believable wrong answers on the slide 20–21 knowledge checks.
6. A Week 1 prep list: headset, cables, named page, calendar plan. Remove the Week 6 sentence and the spreadsheet.
7. Pre-test instruction: "record the score; print page 1 only".
8. **Needs your input:** a quick card with click-by-click steps for the lab (Windows 11 + Edge/Chrome). I can draft it for both browsers if you confirm Windows 11.

**After Monday:**
- An event-builder practice on slide 13, so task 5 works without paper.
- The same Tell, Show, Do, Review restructure for Weeks 2–6.
- Video re-render: the ch5 connector visual, Monday instead of Tuesday, ch4 label order, silent holds after prompts. This needs the narration files on your other computer.
- Believable wrong answers on the post-test before Oct 19, the "rule" wording in post-test item 3, and the Week 6 SaaS redesign question.
