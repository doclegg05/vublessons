# Week 4 video: render review, 2026-10-08

File: `courses/digital-literacy-2/media/week-04.mp4`, 537.5 s, 1280×720, 24 fps, normalized to −18.0 LUFS (from −15.9). Its hash is in `media/manifest.json`.

## Tier 0, deterministic: pass

- `verify-media.py --profile brad-refresh --week 4`: full decode, no black frames, loudness, captions match the script word for word, fast start, strict source check. PASS.
- `verify-screen-share-frames.py`: every encoded screen-demo state matches its source; no failures.
- `hyperframes check --strict --contrast` (`video-check-04.json`): no lint, runtime, layout or contrast findings.
- `check-text-floor.py`: no text under 24 px. `check-captions.py`: all caption files pass (127 Week 4 cues).
- Narration: every take matched its script at 0.94 or better on both `base.en` and `small.en`; pace 129 to 160 words per minute. Chapter 9's base-model text had two extra "now"s; the small model heard none, and both models heard none in an isolated 2-second slice. Not a defect.

## Tier 2, whole-video model review: not run

`render-review.mjs` cannot run while OpenRouter rejects the stored key (HTTP 401). No PASS is claimed from this tier.

## Tier 1, frames and sound checked by hand

- Silence map (−45 dB, 1.5 s): every long silence is a planned card. Pause cards run 11 s, or 14 s when a divider follows; the first divider follows chapter 1's hold (4.6 s). The rest are 1.5 to 2.1 s sentence pauses and the 2 s closing hold.
- Contact sheets at one frame every 6 s: seven pause cards match the narration before them; five dividers name the topic and mission. The email demo follows the one cast (To Sam, Cc Pat; then the volunteer notice with Bcc). The feedback demo uses the worksheet's two-step handout and adds Room A, first floor to step 2 after the reply.
- Not judged by hand: voice warmth and how it sounds on the lab speakers. Britt listens before the PR merges.
