# Week 4 video: render review, 2026-10-08, re-rendered 2026-10-09

File: `courses/digital-literacy-2/media/week-04.mp4`, 537.5 s, 1280×720, 24 fps, normalized to −18.0 LUFS (from −15.9). Its hash is in `media/manifest.json`.

## Tier 0, deterministic: pass

- `verify-media.py --profile brad-refresh --week 4`: full decode, no black frames, loudness, captions match the script word for word, fast start, strict source check. PASS.
- `verify-screen-share-frames.py`: every encoded screen-demo state matches its source; no failures.
- `hyperframes check --strict --contrast` (`video-check-04.json`): no lint, runtime, layout or contrast findings.
- `check-text-floor.py`: no text under 24 px. `check-captions.py`: all caption files pass (127 Week 4 cues).
- Narration: every take matched its script at 0.94 or better on both `base.en` and `small.en`; pace 129 to 160 words per minute. Chapter 9's base-model text had two extra "now"s; the small model heard none, and both models heard none in an isolated 2-second slice. Not a defect.

## Tier 2, whole-video model review: PASS after one fix

First run, 2026-10-09, with a new OpenRouter key (`render-review.mjs`, google/gemini-3.5-flash, given the teaching script, `beats.json`, `cards.json` and `elevenlabs-brad-v3-refresh/render-review-context.md`): REVISE, 1 major and 1 minor (`elevenlabs-brad-v3-refresh/week-04/render-review-before-fix.json`). Frames confirmed both:

- Chapter 1 opened on the photo note "Agree where the shared file lives." while the narrator asked about a group task you have organized.
- Chapter 10, the wrap-up, showed the shared tiles "Saved work, Test evidence, Next step" and "Show the result. Explain why you trust it.", which suit Week 6's testing lesson, not this one.

Fix, in `scripts/dl2/video-scenes.py`: `WRAPUPS` gives Week 4 its own tiles (Clear request, Shared copy, Cost checked) and the line "Pick one habit to use this week."; `NOTE_CUES` gives chapter 1 the opening note "Think of a group task you have helped organize." and brings each bottom line in on the phrase that names it ("You wrote the handout", "Alex runs the session", "The goal is not"; chapter 10 "Sam knows what", "one shared copy", "Before you pay"). A cue phrase the narrator never says now stops the build. Narration, captions and pause times did not change; only scenes 1 and 10 differ, and Weeks 2 and 3 rebuild unchanged.

Second run on the new file (sha256 `0b03269c10ee3299…`): PASS, 0 blocker, 0 major, 2 minor (`elevenlabs-brad-v3-refresh/week-04/render-review.json`). Both minors are new and were not acted on: the picture stays on one diagram during the short passage on working at different times (3:59), and the wrap-up names request, copy and pay but not the meeting habits the narrator also lists.

## Tier 1, frames and sound checked by hand

- Silence map (−45 dB, 1.5 s): every long silence is a planned card. Pause cards run 11 s, or 14 s when a divider follows; the first divider follows chapter 1's hold (4.6 s). The rest are 1.5 to 2.1 s sentence pauses and the 2 s closing hold.
- Contact sheets at one frame every 6 s: seven pause cards match the narration before them; five dividers name the topic and mission. The email demo follows the one cast (To Sam, Cc Pat; then the volunteer notice with Bcc). The feedback demo uses the worksheet's two-step handout and adds Room A, first floor to step 2 after the reply.
- After the fix, frames at 2, 14, 17, 23, 506 and 528 s show the hook note over the photo, "Cast" as the narrator introduces you, Sam and Pat, "Session" when Alex is named, and the new wrap-up tiles with "Request" and then "Pay" under them. Every label fits its tile.
- Not judged by hand: voice warmth and how it sounds on the lab speakers. Britt listens before the PR merges.
