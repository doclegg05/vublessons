# Week 6 video: render review, 2026-10-08

File: `courses/digital-literacy-2/media/week-06.mp4`, 558.8 s, 1280×720, 24 fps, normalized to −18.0 LUFS, 12.7 MB. Its hash is in `media/manifest.json`.

## Tier 0, deterministic: pass

- `verify-media.py --profile brad-refresh --week 6`: full decode, no black frames, loudness, captions match the script word for word, fast start, strict source check. PASS.
- `verify-screen-share-frames.py`: every encoded screen-demo state matches its source; no failures.
- `hyperframes check --strict --contrast` (`video-check-06.json`): no lint, runtime, layout or contrast findings.
- `check-text-floor.py` and `check-captions.py`: pass.
- Narration runs 126 to 163 words per minute (chapter 1 is the fastest). Every chapter carries delivery tags: a calm opener and a pause at most sentences, because Weeks 3 and 5 ran fast without them.
- Chapter 5 was re-recorded after the voice misread "toLowerCase". The script now says "to lower case", and both recognizers hear it.
- Transcript match is 0.967 or better on base.en for every chapter. On small.en it is 0.97 or better except chapter 5 at 0.918. The differences are spellings and sound-alikes: "two lowercase" for "to lower case", CTRL for Control, and digits for numbers.
- Each recognizer also heard one doubled word in chapter 5: "letters" on base.en, "page" on small.en. Both slices were cut and transcribed alone with both models, and neither repeats, so the doubles come from the recognizers, not the audio.

## Delivered file, checked again 2026-10-09

The checks above heard the takes. These ran on the MP4 and the page learners get.

- `check-render-narration.py --week 6` is new. It transcribes `week-06.mp4` with small.en and lines the words up against the script. All 10 chapters score 0.926 or better, each chapter's words fall inside its own audio clip, and no word is heard during a pause or topic card. Exit 0.
- Chapter 5 is lowest at 0.926 for the known reasons: "2 lowercase", Ctrl for Control, digits for numbers. Chapter 6 is 0.963: "no match" for no-match, "version2", and "a happy path" for "the happy path". Chapter 6 transcribed alone with small.en hears "the", so the swap came from the recognizer.
- base.en on the whole file flagged one word: "the" from "Pause the video now." at the end of chapter 9, placed outside the clip, with "video now." dropped. A 9-second slice from 497 s has the full line in both models, ending at 501.9 s, before the clip ends at 502.2 s, then 4 s of silence for the pause card. The flag came from the recognizer, so the check now defaults to small.en.
- `verify-narration-playback.cjs`, run with `DL2_SKIP_GALLERY=1` against the built site: all six weeks pass. On Week 6 the page loads the video and captions whose hashes match the manifest, the duration matches, all 10 chapter buttons seek by keyboard, and three playback samples show frames, decoded audio and a caption on screen.
- That check had been failing on Weeks 3 to 6. It sampled 2 s after each chapter start, but a chapter that opens on a topic card has no caption yet, and Week 6 clears captions in the pauses between sentences. It now samples the middle of the chapter's first caption.

## Tier 2, whole-video model review: PASS

Run 2026-10-09 with a new OpenRouter key, after the old one returned HTTP 401. `render-review.mjs` (toolkit copy, google/gemini-3.5-flash, $0.13) watched and heard the whole file, sha256 `2cb673b3e2d90ee4…`. It got the teaching script, `beats.json`, `cards.json` and a note listing the planned silences (`video/digital-literacy-2/elevenlabs-brad-v3-refresh/render-review-context.md`). Verdict PASS: 0 blocker, 0 major, 0 minor. Report: `video/digital-literacy-2/elevenlabs-brad-v3-refresh/week-06/render-review.json`.

## Tier 1, frames and sound checked by hand

- Silence map (−45 dB, 1.5 s): every long silence is a planned card. Pause cards give 11 s, or 14 to 15 s when a topic divider follows. The 4.7 s gap at 0:41 is the end of chapter 1 plus the Spec divider. The rest are sentence pauses and the closing hold.
- Contact sheets at one frame every 6 s found no defects. The five dividers fall between samples, so frames were pulled inside each 3 s window: Spec, Review, Test, Ready? and Wrap-up all render, including the quotes in "Know what “ready” means".
- The frames match the narration:
  - The diff demo shows the real changed lines of versions 1 and 2, marks the category line "Asked for" and the lost toLowerCase "Not asked for", then counts toLowerCase with Ctrl+U and Ctrl+F: one match in version 2, two in version 1.
  - The app demo runs version 2: learning finds 2, zzz shows the no-match message, LIBRARY finds nothing, and Tab draws an outline.
  - The six roadblock tiles fit with their labels.
  - The retest diagram shows LIBRARY going from 0 to 1 with the passing checks kept.
- Not judged by hand: voice warmth and how it sounds on the lab speakers. Britt listens before the PR merges.
