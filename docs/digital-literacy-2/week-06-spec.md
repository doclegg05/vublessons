# Week 6 guide an agent: the agent loop, the roadblocks to a real service, and a new video

Approved direction (Britt, 2026-10-08): keep the agent workflow (write the request, review the change, test, report, retest) and use the three prepared versions of the resource finder. Mission D teaches what stands between a page on your computer and a real service. The instructor's live agent run stays optional. Same method as Week 3 (`week-03-spec.md`): no capstone, no break, 10-second pause cards and topic dividers in a video rewritten to match. Week 6 is taught Monday, November 2.

## What changed and why

- The old video taught building an app from scratch: "agent", "diff", "server" and "domain" each appeared nowhere in its script, and the opening slide warned that the video did not match the missions. The new video follows the missions, defines each new word once, and the warning is gone.
- The glossary said "You approve each step". Agents can now work on their own for a while; the glossary says you choose how much they may do and review every change before accepting it.
- The secret-key example was a map service, whose browser keys are often meant to be public. It is now a payment service.
- Domain name and Back end join the glossary, because Mission D and the video use them.

## Facts that must stay the same (pinned by `dl2-week6-agent.spec.js`)

- Version 2 keeps its planted defect: the search line lost `.toLowerCase()`, so LIBRARY and Learning find nothing. Version 3 is the one-line repair. Do not fix version 2.
- Expected counts: version 1 finds library 1, LIBRARY 1, learning 0; version 2 finds learning 2, library 1, zzz 0, LIBRARY 0; version 3 finds LIBRARY 1, Learning 2. Ctrl+F for toLowerCase: 2 in versions 1 and 3, 1 in version 2.
- The worksheet's procedures, test logs and 8-point rubric are unchanged; their steps now point to the Open version buttons and the Mission 6B practice page instead of practice-library slide numbers.

## Lesson

Source: `scripts/dl2/mission-control/week6.py`. 35 slides, no break, no timer, no capstone. Minutes: video with pauses 30, welcome and overview 5, 6A 18, 6B 20, 6C 18, 6D 15, individual check 7, close 7.

- 6A Specify the change (Mission 6A practice page, the spec builder): rounds Baseline first (version 1); Rescue the vague request; Can a stranger run it?
- 6B Review the proposed change (Mission 6B practice page, the diff): rounds Count it yourself (Ctrl+U on version 2); Scope creep; Approve this plan?
- 6C Test, report, repair, retest (versions 2 and 3, opened from the slide): rounds Hunt the capitals; Report it so it can be fixed; Retest plus one.
- 6D Know what "ready" means: the six roadblocks (domain name, hosting, back end, server-checked sign-in, secret keys, a caretaker). Rounds Local or hosted?; What can a visitor see?; Roadblock cards.

## Video

Script: `video/digital-literacy-2/teaching-scripts/week-06.txt`. Cards: `week-06/cards.json`. Delivery tags: `week-06/delivery.json` (calm openers and a pause at most sentences, because Weeks 3 and 5 ran fast without them).

| Ch | Title | Serves | Ends on |
|---|---|---|---|
| 1 | Direct an agent, then check its work | Intro; defines an AI coding agent | |
| 2 | Start from what already works | 6A, after a Spec divider | Pause card: Mission 6A, Round 2 |
| 3 | Write a spec the agent can follow | 6A; defines spec and acceptance check | Pause card: Mission 6A, tasks 1 and 2 |
| 4 | Ask for a plan, then predict | 6B, after a Review divider | Pause card: Mission 6B, task 1 |
| 5 | Read the diff before you trust it | 6B, screen demo; defines diff | Pause card: Mission 6B, task 2 |
| 6 | Test the agent's version | 6C, after a Test divider, screen demo; defines happy path and regression | Pause card: Mission 6C, task 1 |
| 7 | Report it so it can be fixed | 6C | Pause card: Mission 6C, task 2 |
| 8 | Retest the repair | 6C | Pause card: Mission 6C, task 3 |
| 9 | What stands between a page and a service | 6D, after a Ready? divider; defines domain name, hosting, back end, API key | Pause card: Mission 6D, task 1 |
| 10 | Direct it, check it, own it | Wrap-up | |

The diff demo shows the real changed lines of versions 1 and 2, then Ctrl+U and Ctrl+F counting toLowerCase. The app demo now runs version 2, where LIBRARY fails.

Rebuild order: as in `week-03-spec.md`, with `week-06` and `--week 6`.
