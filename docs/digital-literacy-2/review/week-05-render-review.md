# Week 5 video: render review, 2026-10-08

File: `courses/digital-literacy-2/media/week-05.mp4`, 490.4 s, 1280×720, 24 fps, normalized to −18.0 LUFS. Its hash is in `media/manifest.json`.

## Tier 0, deterministic: pass

- `verify-media.py --profile brad-refresh --week 5`: full decode, no black frames, loudness, captions match the script word for word, fast start, strict source check. PASS.
- `verify-screen-share-frames.py`: every encoded screen-demo state matches its source; no failures.
- `hyperframes check --strict --contrast` (`video-check-05.json`): no lint, runtime, layout or contrast findings.
- `check-text-floor.py` and `check-captions.py`: pass.
- Narration: four chapters first ran 168 to 181 words per minute. Each was retaken as three candidates at speed 0.85 with sentence pauses, and the slowest kept (1: 146.7, 3: 151.5, 9: 147.6, 10: 139.2). Final range 139 to 159. Every take matched its script at 0.95 or better on both recognizers; the remaining differences are spellings and sound-alikes (fishing for phishing, Brit for Britt, 20 for twenty).

## Tier 2, whole-video model review: not run

`render-review.mjs` cannot run while OpenRouter rejects the stored key (HTTP 401). No PASS is claimed from this tier.

## Tier 1, frames and sound checked by hand

- Silence map (−45 dB, 1.5 s): every long silence is a planned card (11 s, or 14 s with a divider). A 3 s gap at 5:38 is the boundary into chapter 8 (normal hold plus the take's tail). The rest are sentence pauses and the closing hold.
- Contact sheets at one frame every 6 s found one defect: the chapter 3 diagram's three captions ran into each other. They were shortened, the video was rebuilt and re-rendered, and the new frame at 2:00 shows them clear. The strict layout check does not measure text inside one SVG, which is why it passed.
- The rest matches the narration: the one scam message, the bookmark route ending in "Two-step verification: On", Windows Update before camera permissions and the USB drive, the five challenge tasks, and the results shown as a plan.
- Not judged by hand: voice warmth and how it sounds on the lab speakers. Britt listens before the PR merges.
