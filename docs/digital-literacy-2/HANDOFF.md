# Digital Literacy Level 2 course

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

ElevenLabs returned `401 Invalid API key` from its subscription check. No credentials were read or changed. The six deployable explainers therefore use local **Kokoro ONNX 0.6.1**, voice `af_heart`, and HyperFrames 0.8.47. Pitch-preserving tempo adjustment brings narration into Sandra's 135–145 word-per-minute band. Final audio was transcribed locally to align original captions; the matcher refuses weak alignments rather than inventing word times.

Delivered videos are 1280×720 H.264/AAC at 24 fps with fast-start playback, optional WebVTT captions and text transcripts. Visuals use original text/layouts, the existing VUB seal and self-hosted fonts, with no software screenshots or music. GSAP is local to production sources; no CDN is added to learner pages.

The build retains exactly the six MP4s declared by path and SHA-256 in `courses/digital-literacy-2/media/manifest.json`, with a 20 MB per-file ceiling. Other MP4/MP3/MOV files retain the repository's stripping policy. This explicit exception makes the new course self-contained without requiring a YouTube upload.

## Editing and rebuilding

The Python authoring files under `scripts/dl2/` are source; generated HTML and JSON are committed so production needs only the existing Node build. Edit content in `author-content.py` and questions in `author-assessments.py`, then run:

```sh
python3 scripts/dl2/author-content.py
python3 scripts/dl2/author-assessments.py
python3 scripts/dl2/build-pages.py
```

Video scripts live in `author-media.py`. Production source, original narration text, take provenance, word alignments, caption files and scene HTML are under `video/digital-literacy-2/`. Python 3.12 dependencies are pinned in that directory's `requirements.txt`; install them into an isolated venv. Run `npm ci --prefix video/digital-literacy-2/production` for local GSAP. Kokoro model files use HyperFrames' local TTS cache; initialize it with HyperFrames TTS if absent. FFmpeg/FFprobe and HyperFrames 0.8.47 are also required only for media authoring.

```sh
python3 scripts/dl2/author-media.py
# Use the media Python venv for the next three commands.
python scripts/dl2/generate-narration.py
python scripts/dl2/normalize-pace.py
python scripts/dl2/align-captions.py
python3 scripts/dl2/build-media.py
python3 scripts/dl2/build-pages.py
# For each week-01 through week-06:
npx hyperframes@0.8.47 check video/digital-literacy-2/week-01 --strict --json
npx hyperframes@0.8.47 render video/digital-literacy-2/week-01 --output courses/digital-literacy-2/media/week-01.mp4 --fps 24 --quality high --workers 2 --crf 24
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
