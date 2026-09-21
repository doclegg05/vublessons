# Digital Literacy Level 2 course

## Photographic teaching revision

The approved September visual refinement is mapped in `PHOTOGRAPHIC-VISUAL-PLAN.md` and its three linked slide/chapter audits. It uses fictional West Virginia community/home scenes, original instructional interfaces, and the existing Britt narration. Selected photographs and generation provenance are recorded in `photo-assets.json`; originals and contact sheets are in `review/photo-refresh/`.

`scripts/dl2/photo_scenes.py` now controls explicit slide-photo placements, authored artifacts and additional local practice views. Photos establish the scenario; procedural scenes prioritize readable controls and visible outcomes. The safety-photo screen replacements are authored SVG overlays registered to the original image dimensions. Keep them aligned if resizing or changing that image.

Video `CHAPTERS` in `video-scenes.py` maps every chapter to a scene and optional scenario photo. `python3 scripts/dl2/build-media.py --visual-only` rebuilds compositions while preserving audio/caption metadata; do not run `author-media.py` for this visual-only path. The production CLI pin advanced from HyperFrames 0.8.48 to 0.8.58 and passed strict source validation. Use the current production pin for subsequent exports. See `VALIDATION.md` for the actual delivery-verification status rather than inferring it from source generation.

The fourth VUB Learning course teaches IC3 GS6 Level 2 across five two-hour sessions, followed by a two-hour web app building extension. The cohort calendar appears only in `courses/digital-literacy-2/syllabus.html`; presentations and resources can be reused.

## Entry points

- Course home: `/courses/digital-literacy-2/index.html`
- Netlify shortcut: `/digital-literacy-2`
- Syllabus: `/courses/digital-literacy-2/syllabus.html`
- Instructor plans: `/courses/digital-literacy-2/instructor-guide.html`
- Pre-test: `/courses/digital-literacy-2/assessments/pre-test.html`
- Post-test: `/courses/digital-literacy-2/assessments/post-test.html`
- Research and objective map: `/courses/digital-literacy-2/sources.html`

## Included

Six presentations contain 137 slides in total, including title and completion slides. Each week has a two-hour lesson plan, eight worksheet tasks, an answer guide, two knowledge checks, a narrated video, captions and a transcript. The week 6 resource finder is a working, downloadable HTML/CSS/JavaScript example with fictional data and an account-free manual editing path.

The parallel pre/post tests each contain 28 original questions, four per GS6 domain. Results include the score, domain breakdown, every response with feedback, optional pre/post growth comparison, browser Print / Save as PDF, and a standalone HTML download. Paper tests and answer keys accompany both versions. The week 6 app uses a separate eight-point rubric. These are classroom assessments, not Certiport exam questions or certification predictions.

Assessment drafts and results use sessionStorage in the learner's tab. There is no server submission or instructor dashboard. On shared computers, save or print results and select **Clear my assessment**. Slide progress uses the existing `VubProgress` localStorage layer. Worksheets keep typed answers only in the open page and include them when printed.

## Video production

The user-requested **Explain Video Generator** was tried first. Its nine-scene, 2:32 trial completed, and narration/caption playback was checked in the browser. Source: `video/digital-literacy-2/explain-generator-trial.opml`. The plain player URL required sign-in; the tool's full claim link played without sign-in. That ownership-bearing claim link is kept out of the public repository and course pages. The trial remains a comparison, not a required course dependency.

The initial narration previews used Kokoro, Sarah, and then Britt's saved voice. The current teaching revision uses **Britt — Mild Appalachian Male Voice** (`iKrofGyA12WC0e6AhZ8B`) through **ElevenLabs MCP**, model `eleven_v3`, followed by **ElevenLabs Voice Isolator**. It contains ten authored chapters per week, sixty total. Settings and original/cleaned source hashes are recorded in `video/digital-literacy-2/elevenlabs-britt-v3-deep/week-*/beat-*/receipt.json`; credentials are never stored in course sources. Speech is not time-stretched. Local transcription aligns the complete authored captions, rejecting weak matches.

Each video connects a familiar task to worked explanations, visible decisions, common mistakes, paused practice and transfer. Original illustrations accompany topic-specific demonstrations rather than recurring text-list layouts. Chapter buttons let learners replay a skill without automatic playback. The research rationale is in `research/video-teaching-redesign.md`.

Delivered videos are 1280×720 H.264/AAC at 24 fps with fast-start playback, optional WebVTT captions and text transcripts. Visuals use original text/layouts, the existing VUB seal and self-hosted fonts, with no software screenshots or music. GSAP is local to production sources; no CDN is added to learner pages.

The build retains exactly the six MP4s declared by path and SHA-256 in `courses/digital-literacy-2/media/manifest.json`, with a 20 MB per-file ceiling. Other MP4/MP3/MOV files retain the repository's stripping policy. This explicit exception makes the new course self-contained without requiring a YouTube upload.

## Editing and rebuilding

The Python authoring files under `scripts/dl2/` are source; generated HTML and JSON are committed so production needs only the existing Node build. Edit content in `author-content.py` and questions in `author-assessments.py`, then run:

```sh
python3 scripts/dl2/author-content.py
python3 scripts/dl2/author-assessments.py
python3 scripts/dl2/build-pages.py
```

Video scripts live in `video/digital-literacy-2/teaching-scripts/`; `author-media.py` imports them. Visual compositions are authored in `video-scenes.py`, and interactive lesson models in `workshops.py`. Production source, narration, provenance, word alignments, captions and scene HTML are under `video/digital-literacy-2/`. Install that directory's pinned Python requirements into an isolated venv and run `npm ci --prefix video/digital-literacy-2/production` for local GSAP. FFmpeg/FFprobe and HyperFrames 0.8.58 are media-authoring dependencies.

Generate matching takes using the Desktop workflow in **Expanded teaching-video rebuild** below. Keep delivery tags in `prompt.txt`, not learner captions. The pacing step measures the natural take and allocates a 0.45-second scene lead-in plus 1.1-second closing hold (2 seconds for the final practice chapter). Source MP3s and WAVs are local working assets excluded from Git; delivered MP4s, receipts and hashes are tracked. Preserve source audio locally to rebuild without another generation.

```sh
python3 scripts/dl2/author-media.py
# First generate matching ElevenLabs takes as described above.
# Use the media Python venv for the next three commands.
python scripts/dl2/import-elevenlabs-narration.py
python scripts/dl2/normalize-pace.py
python scripts/dl2/align-captions.py
python3 scripts/dl2/build-media.py
python3 scripts/dl2/build-pages.py
# For each week-01 through week-06:
npx hyperframes@0.8.58 check video/digital-literacy-2/week-01 --strict --contrast --json
npx hyperframes@0.8.58 render video/digital-literacy-2/week-01 --output courses/digital-literacy-2/media/week-01.mp4 --fps 24 --quality delivery --workers 2 --crf 24
python3 scripts/dl2/verify-media.py
scripts/quality.sh
```

When updating a video, save each strict check JSON to the matching `docs/digital-literacy-2/video-check-NN.json` before `verify-media.py`. The verifier decodes every delivered frame and audio sample, checks captions against the complete script, checks sound levels and black frames, then updates the manifest hashes. Never update hashes to bypass an unsuccessful verification.

## Evidence

- `av-sync-report.json`: Sandra toolkit assembly audit.
- `video-check-01.json` through `video-check-06.json`: strict HyperFrames lint/runtime/layout/contrast checks.
- `media-verification.json`: delivered MP4 checks.
- `video/digital-literacy-2/week-*/narration/pacing-report.json`: Sandra toolkit take pacing.
- `review/`: desktop/mobile screenshots and print proofs.
- `VALIDATION.md`: final checks and review disposition.

Run Sandra's existing checks from the education workspace (toolkit is a sibling repository):

```sh
for week in video/digital-literacy-2/week-*; do
  node ../toolkit/tools/test-narration-pacing.mjs "$week"
  node ../toolkit/tools/check-draft-audio.mjs "$week"
done
node ../toolkit/tools/audit-av-sync.mjs video/digital-literacy-2/week-* --json docs/digital-literacy-2/av-sync-report.json
```

No live deployment, merge to main, account creation, purchase or learner record collection is part of this delivery.

## Illustrated learning-app design

The approved A+B+C compositions are combined across the DL2 course: a navy course rail, original illustrations, six-week overview with saved continuation, topic navigation and a focused assessment workspace. `scripts/dl2/learning.py` authors the shared course frame, home and assessments; `learning-app.css` and `learning-app.js` provide responsive styling and truthful browser-local course progress. Regenerate pages with `python3 scripts/dl2/build-pages.py`.

Assessments show one question at a time, preserve position and answers, offer Review all, and retain existing grading, printable/downloadable results and clearing controls. Topic counts are actual answers, not estimated completion. Illustrations and provenance live under the course assets and `.impeccable/asset-manifest.json`; approved comps are in `.impeccable/mocks/`. The user's default preference is this illustrated, modern learning-app direction.

The learning-app revision expanded the quality gate to 60 browser tests, including three dedicated learning-app state/mobile tests. Final evidence is in VALIDATION.md and `review/learning-app/`. All six Britt voice videos remain unchanged by this visual pass.


## Topic-specific slide enrichment

The six decks now add 53 illustrated, choice-based topic examples and dedicated chart, image-edit and video-edit demonstrations. Teaching prose, assessment alignment and existing models are preserved. Edit the examples in `scripts/dl2/scenes.py`, regenerate with `build-pages.py`, then run the quality gate. New styling and logic live in `assets/slide-scenes.css` and `assets/slide-scenes.js` and load only on presentation pages.

Six new original illustration assets (about 463 KiB total) are tracked with `slide-illustrations.json`. `capture-slide-scenes.cjs` records desktop/mobile examples under `review/slide-scenes/`. Ten new tests verify all 53 topic selectors with keyboard and enlarged mobile text, plus chart consistency, crop/resize, trim/split, practice toggles and print content. The slide-enrichment revision brought the suite to 70 tests. These interactions are browser-local demonstrations; they do not perform real edits, payments, messages or account operations. Practice-step selections reset when the page is reloaded.


## Branded results reports

Pre/post grading uses a shared branded report theme in `assets/results-report.css`. The page builder embeds its CSS and the official white seal in assessment pages; downloads reuse both without external resources. Results include learner metadata, the actual score, domain bars with numeric equivalents, up to two lowest-scoring practice domains and all answer explanations. Perfect scores receive an application task instead of invented weak areas. Existing comparison wording, grading, clearing and optional learner information are preserved.

The print layout isolates report colors/type from the shared handout and text-size overrides, reserves the first page for the summary, and avoids splitting answer sections. Samples with fictional learner data, screen captures and PDFs live in `review/results-report/`; reproduce them with `node scripts/dl2/capture-results.cjs`. The report test file covers offline branding, accessibility, scoring edge cases and mobile/print behavior. The results-report revision brought the suite to 73 tests.


V3 delivery guidance: [ElevenLabs prompting and pause controls](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices). The sibling pacing checker uses 100–210 WPM as its defect band; the A/V audit separately warns outside 135–145 WPM. Retain and report those style warnings rather than mechanically retiming speech. Automated timing/defect checks do not certify the subjective quality of the cloned voice.


## Expanded teaching-video rebuild

The current narration source is `video/digital-literacy-2/teaching-scripts/week-NN.txt`: ten chapters per week. Run `author-media.py` only when intentionally replacing the narration script; it resets timing pending audio generation. Generate each chapter using the saved Britt voice and V3 settings, then apply ElevenLabs Voice Isolator to a local Desktop copy. The working directory is `~/Desktop/vub-deep-narration/week-NN/beat-NN/`, with `prompt.txt`, one MP3 in `raw/`, and one MP3 in `clean/`. The importer copies both into `elevenlabs-britt-v3-deep` and records the original and cleaned hashes. Preserve rejected candidates separately rather than overwriting their receipts.

The importer, natural-pacing allocator and aligner accept an optional `week-NN` argument for incremental production. After the initial Whisper model download, `HF_HUB_OFFLINE=1` avoids network checks during repeated alignment runs. Rebuild media sources and pages after alignment so captions, chapter seek positions and transcripts agree. Chapter navigation is keyboard accessible and intentionally does not autoplay.

The research and teaching rationale are in `research/video-teaching-redesign.md`. The curriculum and scheduled contact time remain unchanged; show chapters within the planned demonstrations and use the scheduled lab time for paused practice.

The expanded-video quality gate passes 75 browser tests. `capture-video-review.py` captures each exported chapter; `capture-video-chapters.cjs` records desktop/mobile navigation and its accessibility scan. See `VALIDATION.md` for current evidence and the distinction between technical audio checks and listening judgment.
