# Week 3 resource pack: the Week 2 method, pause cards and a new video

Approved direction (Britt, 2026-10-08): Weeks 3 to 6 follow how Week 2 works, with three changes Britt asked for. There is no capstone, because capstones do not work with this class. Every "pause and try it" moment in a video ends on a full-screen pause card held for about 10 seconds of silence, so there is time to press Pause. Each topic change in a video opens on a divider card. Britt confirmed that a 30-minute video block is welcome, since class usually runs short.

This file covers Week 3, taught Monday, October 12. Weeks 4 to 6 get their own spec when they are built.

## Lesson

Source: `scripts/dl2/mission-control/week3.py`. 34 slides, no break, no timer, no capstone.

| Block | Minutes |
|---|---|
| Opening video with pause cards | 30 |
| Welcome and mission overview | 5 |
| 3A Structure, then suggest (Word) | 20 |
| 3B Make the total recalculate (Excel) | 20 |
| 3C Show the message clearly (PowerPoint) | 16 |
| 3D Export, then inspect (Word PDF, clip editing) | 14 |
| Individual check | 8 |
| Close | 7 |

Learners do each mission's first worksheet tasks at the video's pause cards, so each Your turn slide checks that work and moves on to the rounds. Rounds:

- 3A: Bold is not a heading (Navigation Pane, Check Accessibility, Table of Contents as the Done early line); Check the AI draft (worksheet; the Week 2 idea that an AI answer is a lead).
- 3B: Typed total versus formula; Add a row; CSV keeps values only (a chart is the Done early line).
- 3C: Alt text that helps (worksheet; check any suggested alt text like an AI answer); Crop is not delete (Compress Pictures › Delete cropped areas); Use, credit, ask or skip? (worksheet).
- 3D: Check before you export; Which format for whom? (worksheet); Trim and split a clip on the Mission 3D practice page.

Practice pages: only `practice-3d.html` (the existing trim and split simulation), opened in a new tab from Round 4. Missions 3A to 3C are done in the real apps, so they have no practice link, as Week 2 Mission 2A has none.

## Facts to keep the same everywhere

- Supplies, in the order of `assets/supplies.csv`: Paper 12, Folders 8, Pens 5. The deck used to list pens before folders.
- The CSV heading is Cost. Mission 3B task 1 has learners change B1 to Cost in dollars; the video says so.
- Handout lines: Computer help at the library (Heading 1); Who it helps and Steps (Heading 2); Choose one task. Visit the learning desk. Ask how to repeat it at home.
- Tracked edit: Visit the learning desk becomes Ask at the learning desk.
- The practice clip: Start 0 to 3 s, Explain 3 to 9, Pause 9 to 12, Next step 12 to 17, End 17 to 20. Trim leaves 14 seconds; removing the pause leaves 17.
- Round numbers avoid the test items (pre-test item 10 uses 28 to 31; post-test item 10 uses 40 to 44). Paper at 20 gives 33; Envelopes $6 gives 34.
- PowerPoint slides are named in words ("the second slide"). `build.py` turns "slide N" in lab text into a practice-library exercise.

## Video

Script: `video/digital-literacy-2/teaching-scripts/week-03.txt`. Cards: `video/digital-literacy-2/week-03/cards.json`. Delivery tags: `video/digital-literacy-2/week-03/delivery.json`. Voice and settings are the approved Brad ones (`eleven_v3`, voice `Dslrhjl3ZpzrctukrQSN`, stability 0.5, similarity 0.8). Chapters 1 and 7 use speed 0.85 with sentence pauses because the first takes ran at 182 and 165 words per minute. Final takes run 127 to 158 words per minute and match the script at 0.96 or better on both recognition models.

| Ch | Title | Serves | Ends on |
|---|---|---|---|
| 1 | Make it for a reader | Intro | Pause card: Mission 3A, task 1 |
| 2 | Give the handout real structure | 3A, after a Word divider | Screen demo |
| 3 | Suggest a change and let the owner decide | 3A | Pause card: Mission 3A, tasks 2 to 4 |
| 4 | Enter the costs, then a formula | 3B, after an Excel divider | Pause card: Mission 3B, task 1, with the prediction |
| 5 | Check your prediction and keep the formula | 3B | Pause card: Mission 3B, task 2 |
| 6 | Three slides, one message | 3C, after a PowerPoint divider | |
| 7 | Crop, describe and credit the photo | 3C | Pause card: Mission 3C, tasks 1 and 2 |
| 8 | Save a PDF, then open it and check | 3D, after a Save and share divider | Pause card: Mission 3D, task 1 |
| 9 | Trim and split a short clip | 3D | Pause card: Mission 3D, Round 4 |
| 10 | Check your pack like its reader | Wrap-up, after a divider | |

The prediction now comes before the answer: chapter 4 ends by asking learners to predict, and chapter 5 changes the cost. The old chapter 5 said both totals first.

### How the cards work

- `normalize-pace.py` gives a divider chapter 3 seconds of silent lead-in and a pause chapter a 10.5-second silent hold.
- `scripts/dl2/video-cards.py` writes one card composition per divider and pause. `build-media.py` plays the chapter's scene only between its divider and its pause card, so no card covers a live scene. A chapter button lands on the divider.
- A narrator line "Pause the video now." always ends the chapter; `tests/content/dl2-video-cards.spec.js` checks that every such line has a card, every card names a worksheet task or round that exists, and the transcript carries the card's steps.
- Cards show no countdown or progress bar.

## Rebuild

From the repository root, with the media Python environment for the starred steps:

```sh
python3 scripts/dl2/author-media.py week-03
python3 scripts/dl2/tag-narration.py week-03
python3 scripts/dl2/elevenlabs-takes.py stage --week week-03     # then: generate beat-NN ... --week week-03 --go
*python scripts/dl2/check-expressive-takes.py --profile brad-refresh --week week-03 --model base.en   # and --model small.en
*python scripts/dl2/import-elevenlabs-narration.py week-03 --profile brad-refresh
*python scripts/dl2/normalize-pace.py week-03
*python scripts/dl2/align-captions.py week-03
python3 scripts/dl2/build-media.py week-03
python3 scripts/dl2/check-text-floor.py; python3 scripts/dl2/check-captions.py --script video/digital-literacy-2; node scripts/dl2/check-screen-shares.mjs
npx hyperframes@0.8.82 check video/digital-literacy-2/week-03 --strict --contrast --json > docs/digital-literacy-2/video-check-03.json
npx hyperframes@0.8.82 render video/digital-literacy-2/week-03 --output courses/digital-literacy-2/media/week-03.mp4 --fps 24 --quality delivery --workers 2 --crf 24
python3 scripts/dl2/normalize-loudness.py
python3 scripts/dl2/verify-media.py --profile brad-refresh --week 3
python3 scripts/dl2/refresh-video-text.py week-03; python3 scripts/dl2/refresh-video-chapters.py
python3 scripts/dl2/mission-control/build.py
```

`VUB_TAKES_DIR` points the take scripts at the local take folder, which now lives in the main checkout (`vub-brad-narration-refresh/`), not on the Desktop. The ElevenLabs key is read from `ELEVENLABS_API_KEY` in a gitignored `.env` or the environment.
