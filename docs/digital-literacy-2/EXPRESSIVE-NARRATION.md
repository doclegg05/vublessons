# Expressive Britt narration

## Request and performance direction

Replace the flat delivery with an engaged instructor performance throughout all
six videos. Preserve Britt's saved voice, the full teaching script, and the
approved illustrated and screen-share demonstrations.

The performance plan uses warm introductions, curiosity in questions, enthusiasm
when an action succeeds, and encouragement before practice. Safety chapters use
reassurance and firm emphasis rather than excitement. Tags direct individual
teaching moments; they are never displayed in captions or transcripts.

ElevenLabs V3 settings: Britt `iKrofGyA12WC0e6AhZ8B`, stability 0 (Creative),
similarity 0.8, speed 0.95, style 0, speaker boost disabled. Selected takes use
Natural stability (0.5) after pronunciation or pause-artifact review; each
receipt records the actual settings. Voice Isolator retains
the previous cleanup approach for the user's echo concern. No added reverb,
background music, artificial breath effects, or post-generation time stretching.
Direction follows the official [V3 prompting guidance](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices).

## Reproduction and safeguards

- `prepare-expressive-narration.py` creates the 60 performance prompts while
  asserting that removing tags produces the exact original teaching words.
- Generate one take per chapter with ElevenLabs MCP, then isolate it. Source
  workspace: `~/Desktop/vub-expressive-narration/week-NN/beat-NN/{raw,clean}`.
- Run `check-expressive-takes.py` with the video virtual environment. It uses
  unprompted ASR to expose missing words, inserted directions, and pacing issues.
  Review differences: a recognizer may spell spoken numbers as digits.
- Import with `import-elevenlabs-narration.py --profile expressive`. The entire
  batch must have matching source hashes, transcription matches of at least
  0.87, and 100–185 WPM before any working narration is replaced.
- Run `normalize-pace.py`, `align-captions.py`, `build-media.py` (normal mode),
  and `build-pages.py`. Word alignment drives screen actions, captions, chapter
  navigation, and scene durations. There is no global audio speed-up.
- Render all six videos and rerun strict source, encoded screen-state, final
  media, and site checks before refreshing the media manifest.

Previous deep-narration receipts are retained. The old audio and MP4s are also
saved in `~/Desktop/vub-before-expressive-narration`. The audio-preservation
report from the earlier screen-share-only revision is historical; this revision
intentionally changes narration and caption timing.

## Verification boundary

ASR, timing, decoding, and level checks detect technical problems. They do not
certify whether the delivery sounds lively or natural to a listener. A playable
formula-chapter sample was provided during authoring; instructor listening on
the intended classroom speakers remains the subjective acceptance check.

## Source verification

The delivered plan contains all 6,480 original teaching words across 60 chapters
(about 44 minutes). Fifty takes use Creative stability and ten use Natural
stability after candidate review. Every take retains Britt's voice and V3, with
no time stretching. Eleven candidates were replaced for a pronunciation, pace,
or pause-artifact concern.

All 60 final takes pass the Sandra toolkit pacing/short-pause defect checks and
all six draft-audio checks pass. Unprompted recognition covered every take;
49 current takes also received a second recognizer check to resolve ambiguous
words or missing phrases. The final word alignments match at least 0.9449 of
script tokens; number spelling and hyphenation account for remaining gaps in
the lowest-scoring formula example. The narrower 135–145 WPM house-style audit
reports 51 warnings and zero failures; measured take rates range from 128 to
181.4 WPM, with a median of 153.8. These warnings are retained for listening
review, rather than silently time-stretching expressive speech.

All 73 screen states pass reverse-seek, visible-label, and bounds checks. All
six HyperFrames strict checks pass, including 254 computed contrast checks.
The final timing also exposed two click pulses that overlapped by 0.01 seconds;
the generator now limits a pulse to the space before the next click.

Source hashes, settings, word counts, and pacing evidence are in
`expressive-narration-verification.json`.

## Export verification

All six final MP4s pass full audio/video decode, duration, H.264/AAC format,
black-frame, volume, fast-start, caption coverage, and 20 MiB delivery-budget
checks. All 73 encoded screen states match the independently sought source
frames: minimum structural similarity 0.977869 against the 0.95 threshold.
`media-verification.json`, `screen-share-frame-verification.json`, and the
public media manifest hold the final delivery evidence.

## Site verification

The full local quality gate passed: 120 Chromium tests, the 193-page static
build, 1,380 internal references with zero broken links, catalog consistency,
the accessibility ratchet, and the report-only readability check. This remains
a draft-preview change; production publication is separate.
