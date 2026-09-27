# Weeks 2–6: Tell, Show, Do, Review treatment (2026-09-26)

Same method as Week 1 ([week-01-tsdr/README.md](week-01-tsdr/README.md)): each week was reviewed by **Gemini 3.1 Pro** through OpenRouter (the video alone, then the video plus all the week's materials; $1.88 for all ten runs) and by **Claude**. Claude checked every Gemini claim against the frames and sources, verified the content against Microsoft, Google, FTC, VA and Apple pages, and drafted the changes (`proposal.json` in each week's folder). The framework is [week-01-tsdr/framework.md](week-01-tsdr/framework.md): Tell, Show, Do, Review inside the WIPPEA cycle (TEAL Fact Sheet No. 8), with Knowles' adult learning principles.

**Correction:** the Gemini structure prompts for weeks 2–6 wrongly asked Gemini to "keep the 25-minute pre-test" in its suggested running order. Only week 1 has a pre-test. The Claude reviews set Gemini's running orders aside for that reason, and nothing built here uses them. The prompt template has since been fixed.

## What every week had in common

Every week ran as **lecture, then lab**: 15–20 minute blocks of slides, the whole video played after the slides, one 30-minute lab with partners swapping halfway, then one 10-minute check. Every week now runs as **short cycles**. Each cycle names its Tell, Show, Do and Review, plays its own video chapter as the Show with pause points, and has **every learner** do the task at their own seat. Each week also gets:
- measurable (ABCD) outcomes in the lesson plan
- a week-specific prep list
- a Windows 11 lab quick card, with every step checked on an official page
- believable knowledge-check options
- a home task that feeds the next week's warm-up

## By week

| Week | Date | Verdict before | Main changes |
|:--|:--|:--|:--|
| 2 Find, judge, organize | Oct 5 | Search half close; files half a lecture that could not fit its time. Content correct. | Six cycles. Hands-on folder, Save As, ZIP and Recycle Bin work; sharing and version history marked simulated (they need an online account). One practice file name, `library-help-v1.docx`, everywhere (it had four names). Search example is `site:gov`; AI answers at the top of results are not the source. |
| 3 Create something people can use | Oct 12 | Overloaded: five apps in about 50 minutes; the crop task was impossible (SVG). | One app at a time (Word, Excel, PowerPoint). A croppable **practice photo** replaces the SVG. Seat swap for the tracked edit. The SUM formula is typed live, and the video is paused before it gives the answer. |
| 4 Communicate and collaborate | Oct 19 | Two tell-then-do blocks; missing topics; tasks needed accounts. | Five cycles; account-free email and comment tasks. **Payments:** card vs digital wallet vs payment app, and money sent by app is hard to get back. Streaming examples named. Task 8 no longer gives away its answer. |
| 5 Protect your work and show your skills | Oct 26 | One long tell; a challenge that could not give individual ratings. | Three short cycles, then the challenge, a break and the post-test. The challenge is **individual, five computer rows**, with a fresh `supplies.csv`. Word's "password to open" is encryption and cannot be recovered. Windows 10 end of support is used as the updates example. |
| 6 Bonus: agentic engineering | Nov 2 | Did not teach its goal; the hands-on path broke itself. | Redesigned around **your AI coding agent demo** (see below). |

## Week 6 redesign (instructor decision: instructor-led agent demo)

Learners need no accounts or AI access. The loop is **spec → plan → change → review → test → revise**:
- Learners write a plain-English change request and acceptance checks.
- They predict what will change, then read the agent's plan and its diff (slide 10).
- They test with a checklist: happy path, no match, mixed case, keyboard, narrow screen.
- They write a repair request and retest.
- SaaS basics (hosting, sign-in, where data lives, API keys, cost and upkeep) are taught through the same example.

**Fallback if the live agent misbehaves:** two prepared pages next to the original starter:
- `resource-finder-agent.html`: adds search by category, with **one deliberate mistake**: capital letters no longer match ("LIBRARY" finds nothing).
- `resource-finder-agent-fixed.html`: the repaired version.

## Still open (not in these PRs)
- **Video re-records and re-renders**, which need the narration files on the other machine:
  - silent holds after practice prompts (all weeks)
  - fast chapters
  - week 2: the "+" signs in the ch2 search, and the file names in ch6–7
  - week 3: ch5 formula order and the "Supplies" label
  - week 4: pause holds and the payments line
  - week 5: ch10 naming the challenge, and the "Choose alerts" placeholder
  - week 6: ch5–6 re-recorded for the agent loop

  Before any re-rendered video ships mid-cohort, add a version tag to the media URLs, so browsers don't pair an old cached video with new chapter times.
- **Post-test rewrite** (before Oct 19): believable wrong answers and shuffled positions; new situations for items that repeat slides (items 14, 16, 23, 26, 27, 28); "rule" wording in item 3.
- A per-learner challenge roster on the week 5 answer guide.
- The Text Size widget covers content on the activity pages at phone width (shared `text-size.js`).
