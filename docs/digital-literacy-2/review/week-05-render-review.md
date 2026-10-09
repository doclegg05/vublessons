# Week 5 video: render review, 2026-10-08, re-rendered 2026-10-09

File: `courses/digital-literacy-2/media/week-05.mp4`, 490.4 s, 1280×720, 24 fps, normalized to −18.0 LUFS. Its hash is in `media/manifest.json`.

## Tier 0, deterministic: pass

- `verify-media.py --profile brad-refresh --week 5`: full decode, no black frames, loudness, captions match the script word for word, fast start, strict source check. PASS.
- `verify-screen-share-frames.py`: every encoded screen-demo state matches its source; no failures.
- `hyperframes check --strict --contrast` (`video-check-05.json`): no lint, runtime, layout or contrast findings.
- `check-text-floor.py` and `check-captions.py`: pass.
- Narration: four chapters first ran 168 to 181 words per minute. Each was retaken as three candidates at speed 0.85 with sentence pauses, and the slowest kept (1: 146.7, 3: 151.5, 9: 147.6, 10: 139.2). Final range 139 to 159. Every take matched its script at 0.95 or better on both recognizers; the remaining differences are spellings and sound-alikes (fishing for phishing, Brit for Britt, 20 for twenty).

## Tier 2, whole-video model review: PASS after one fix

First run, 2026-10-09, with a new OpenRouter key (`render-review.mjs`, google/gemini-3.5-flash, given the teaching script, `beats.json`, `cards.json` and `elevenlabs-brad-v3-refresh/render-review-context.md`): REVISE, 1 major (`elevenlabs-brad-v3-refresh/week-05/render-review-before-fix.json`). Frames and captions confirmed it: in chapter 8 the "Read-only" line came in at 357 s, after the narrator had said it (348 to 353 s) and moved on to device encryption, and device encryption and Windows+L never had a line.

Fix, in `scripts/dl2/video-scenes.py`: chapter 8 now has five lines (password to open, read-only, device encryption, lock with Windows+L, accounts), and `NOTE_CUES` brings each in on the phrase that names it, after the opening note "Different protections do different jobs." Narration, captions and pause times did not change; only scene 8 differs.

The new file (sha256 `37a5ccca5423…`) was sampled twice, because the first sample raised a blocker:

- Sample 1: REVISE, 1 blocker and 1 minor (`render-review-after-fix-sample-1.json`). Neither held up. The minor said the 0:17 line reads "What evidence do have?"; the full-size frame reads "What evidence do I have?". The blocker called chapter 9's first sentence (6:38, "Now you get to show what you can do") an extremely slow, creepy whisper. Measured, it is voiced like the rest (62% of frames, against 52 to 70% for the chapter), as loud (−21.1 dBFS), and slower (152 against 183 to 256 words per minute). A scan of all 90 sentences found none whispered.
- Sample 2: PASS, 0 blocker, 0 major, 1 minor (`render-review.json`): the same sentence has a drop in pitch and slow pacing. That is true and comes from the `[calmly] [slowly]` delivery tags: its median pitch is 112 Hz against 122 to 126 Hz for the next sentences, and chapter 1's opener, with the same tags, drops further (105 against 137 Hz). Changing it would need a new recording, so it was left for Britt to judge by ear.
- The chapter 8 finding did not come back in either sample.

## Tier 1, frames and sound checked by hand

- Silence map (−45 dB, 1.5 s): every long silence is a planned card (11 s, or 14 s with a divider). A 3 s gap at 5:38 is the boundary into chapter 8 (normal hold plus the take's tail). The rest are sentence pauses and the closing hold.
- Contact sheets at one frame every 6 s found one defect: the chapter 3 diagram's three captions ran into each other. They were shortened, the video was rebuilt and re-rendered, and the new frame at 2:00 shows them clear. The strict layout check does not measure text inside one SVG, which is why it passed.
- The rest matches the narration: the one scam message, the bookmark route ending in "Two-step verification: On", Windows Update before camera permissions and the USB drive, the five challenge tasks, and the results shown as a plan.
- After the fix, frames at 342, 346, 351, 356, 364 and 369 s show "Different protections do different jobs.", then "Password to open", "Read-only", "Device encryption", "Lock · Windows + L, or sign out" and "Accounts", each as the narrator says it.
- Not judged by hand: voice warmth and how it sounds on the lab speakers. Britt listens before the PR merges.
