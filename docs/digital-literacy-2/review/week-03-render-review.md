# Week 3 video: render review, 2026-10-08

File: `courses/digital-literacy-2/media/week-03.mp4`, 558.7 s, 1280×720, 24 fps, normalized to −18.0 LUFS. Its hash is in `media/manifest.json`.

## Tier 0, deterministic: pass

- `verify-media.py --profile brad-refresh --week 3`: full decode, no black frames, loudness, captions match the script word for word, fast start, strict source check. PASS.
- `verify-screen-share-frames.py`: 79 encoded screen-demo states against their sources, minimum structural similarity 0.965 (floor 0.95). No failures.
- `hyperframes check --strict --contrast` (`video-check-03.json`): no lint, runtime, layout or contrast findings; 50 contrast samples.
- `check-text-floor.py`: no text under 24 px. `check-captions.py`: all caption files pass.
- Narration: every take matched its script at 0.96 or better on both `base.en` and `small.en`. Pace 127 to 158 words per minute.

## Tier 2, whole-video model review: not run

`render-review.mjs` could not run. OpenRouter answered HTTP 401 "User not found" for the key in the documented `.env` and for the Keychain key. A PASS from this tier is not claimed.

## Tier 1, frames and sound checked by hand

- Silence map (`silencedetect`, −45 dB, 1.5 s): every long silence is a planned card. Pause cards run 10.5 s (11 s alone, 14 s when a divider follows). The rest are 1.5 to 1.8 s sentence pauses and the 2 s closing hold. No unplanned gap.
- Contact sheets at one frame every 6 s across the whole film, plus full frames at 0:54 (Word divider) and 1:39 (Insert link dialog). Every pause card is readable and matches the narration before it. Dividers name the app and the mission title. The prediction card appears before the answer. The Save As dialog and the Styles gallery cover no text.
- Not judged by hand: voice warmth, natural inflection and how the audio sounds on the lab speakers. Britt listens before the PR merges.
