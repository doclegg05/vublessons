# Digital Literacy Level 2 narration refresh

Prepared September 28, 2026 on `codex/dl2-narration-refresh`, from base
`3cdc6fa2e6cf4a11e94ba443413703ed1fb46864`. The user approved the narrator and
instructional pace on September 28, 2026
and authorized updating, merging and deploying this release. The branch now
includes the graded-PDF email release from `main` at `b976c2f`.

## Review

Open the [six-video gallery](http://127.0.0.1:3948/docs/digital-literacy-2/review/narration-refresh/index.html).
Each video includes English captions, an MP4 download, and a transcript page with
ten working chapter controls. To restart the preview, serve this worktree root
with `npx serve . -l tcp://127.0.0.1:3948 --no-clipboard` (supports video byte ranges).

| Week | Duration | Size |
|---|---:|---:|
| 1 | 7:24 | 10.51 MiB |
| 2 | 7:23 | 10.84 MiB |
| 3 | 7:24 | 9.86 MiB |
| 4 | 7:33 | 10.25 MiB |
| 5 | 7:41 | 10.59 MiB |
| 6 | 7:38 | 10.32 MiB |

The provider display name for the requested voice `Dslrhjl3ZpzrctukrQSN` is
**Hey Its Brad - Clear Narrator for Documentary**. No claim of voice ownership is
made. All takes use ElevenLabs `eleven_v3`, Natural stability `0.5`, similarity
`0.8`, and Voice Isolator cleanup. Default requested speed is `0.95`; four final
pacing takes use `0.85` with sentence pause tags. Nothing is time-stretched.
Per-take settings and receipts take precedence over the profile defaults.

## Scope and preservation

All **6,480 authored teaching words**, 60 chapter IDs/titles and visual labels
match the base release. The existing photographs, generated workstation intro,
diagrams and fictional screen demonstrations remain. Demonstration actions,
chapter windows, word alignments and captions follow the newly recorded audio.
Only chapter timestamps and media URL versions changed across twelve learner pages.
The media URLs include content hashes so returning learners receive the new audio
and matching captions despite the one-day browser media cache.

The current 27-slide Week 1 Mission Control presentation, its `os/` layer,
assessments, backend, deployment configuration, catalog and teaching scripts
match the updated `main` release. The work was isolated from the primary checkout
and incorporated its completed assessment-email release before publication. The
initial review did not deploy; publication was authorized after that review.

Earlier Britt profiles and the original media manifest are retained. Selected
source settings, prompts and receipts are in
`video/digital-literacy-2/elevenlabs-brad-v3-refresh/`. Raw/isolated MP3s, rejected
accuracy takes, unselected pacing candidates and earlier versions are retained
locally in that profile and/or `~/Desktop/vub-brad-narration-refresh/`. Source
MP3/WAV files follow the repository's existing ignore policy; the six compact
final MP4s are tracked delivery assets.

## Pacing and listening review

The existing **135–145 WPM house-style band is advisory**. The waveform/clip defect
gate is separate. No audit threshold was altered or warnings suppressed.
The four fastest original takes received targeted new recordings:

| Chapter | Before WPM | Final take WPM | Including scene holds |
|---|---:|---:|---:|
| Week 1, 3 — scope of settings | 165.6 | 141.8 | 137.1 |
| Week 1, 4 — sound destination | 171.8 | 150.3 | 145.1 |
| Week 2, 2 — useful search | 168.1 | 144.4 | 139.6 |
| Week 6, 6 — working version | 166.0 | 138.5 | 134.1 |

Final cleaned-take rates range from **130.3–163.6 WPM**. The AV sync audit reports
**zero failures and 45 advisory pace warnings**. Its tokenizer produces slightly
different word counts from the source-script transcription report. The complete
chapter warning list is retained in `av-sync-report.json` and the profile's
`pacing-review.json`; the project is not represented as uniformly within 135–145.

Two independent unprompted recognizers (`base.en` and `small.en`) checked all sixty
final audio hashes. Two earlier accuracy retakes addressed clear/clearer and
and/in ambiguities. Week 5 chapter 3 uses the independent small recognizer's exact
match after the base recognizer missed a phrase; both results are preserved and
the import threshold remains unchanged. Week 3 chapter 3's Track/Tracked ending
remains an ASR inflection ambiguity for listening review. Numeric spelling,
compound-word and punctuation differences are documented in
`transcription-review.json`.

These checks establish technical delivery and transcription evidence. They do
not establish subjective warmth, natural inflection, every consonant, or comfort
on classroom speakers. The review gallery is the place to make that judgment,
particularly for the remaining faster chapters. Existing learner practice pauses
remain available through ordinary player controls.

## Validation

All final checks passed:

- `bash scripts/quality.sh`: build passed, 198 pages; 1,314 internal references
  with zero broken links; four-course catalog consistent; **304 Playwright tests
  passed, plus all 10 graded-PDF email server checks**; all 34 scanned accessibility routes clean. Readability remains the
  existing report-only baseline, not a new gate.
- `verify-media.py --profile brad-refresh`: all six complete video/audio streams
  decoded without errors or black frames; source/receipt/alignment hashes and
  exact caption text passed; fast-start H.264 1280×720 at 24 fps with AAC audio;
  every file below the existing 20 MiB budget. Final integrated loudness is
  −18.04 to −18.05 LUFS; true peaks are −3.38 to −3.80 dBTP.
- `verify-narration-playback.cjs`: **60 keyboard chapter seeks**, paused-seek
  behavior, **18 actual playback/caption/audio-decode samples**, zero page errors,
  and zero gallery WCAG A/AA findings at desktop and 390-pixel mobile widths.
  All six gallery players and poster images passed, with only one video playing
  at a time. Browser playback is muted automation; it is not a subjective
  listening pass.
- Staged Gitleaks scan: no leaks found.
- The local review server returns **206 Partial Content** for byte-range requests.
  An initial Python-server seek failure was fixed by using `serve`; no classroom
  player code needed changing.

Evidence: `brad-refresh-quality.log`, `media-verification.json`,
`screen-share-frame-verification.json`, `av-sync-report.json`,
`brad-refresh-captions.log`, `brad-refresh-audio-guard.log`,
`review/narration-refresh/playback-verification.json`, and the profile's source
and transcription receipts.

Additional verified checks: 60 waveform/pacing defect passes; six draft-audio guards;
strict caption text, line, duration and reading-rate checks; all six HyperFrames
strict source checks; 73/73 source demonstration states; 73/73 encoded state
comparisons (minimum structural similarity 0.974507, required 0.95); and final
contact-sheet inspection for all six lessons.

Caption grouping now rebalances phrase boundaries and shares at most 0.6 seconds
of display time between neighboring phrases. Every cue remains within its actual
audio clip. The 20/22 characters-per-second, two-line, 42-character, phrase-boundary
and duration checks are unchanged. This corrects the first draft's nine caption
boundary failures. Rendered source hashes remained identical through the caption
repair. HyperFrames is pinned to 0.8.82; GSAP remains locally hosted at 3.14.2.

## Usage evidence

There were **68 successful TTS generations and 68 successful isolation calls**,
including retakes and unselected pacing candidates. The subscription counter
changed from **314,314 to 403,136**, an **account-wide increase of 88,822 credits**.
The ending balance was **278,332 credits**, with **$0 reported current overage**.
This is not a per-call billing ledger or an exact task cost: simultaneous account
activity would be included, and these tools expose no per-call dollar price.
Compact before/after snapshots are in `usage-start.json` and `usage-end.json`.

## Maintenance

Use the `brad-refresh` profile with the transcription checker, importer and final
media verifier. The importer checks the unmodified teaching words, source hashes
and transcription evidence; the verifier also compares each script hash with
its earlier approved Britt receipt. `refresh-video-chapters.py` updates existing
chapter controls without regenerating the classroom or assessment release.
See the current instructions at the top of `HANDOFF.md`.
