# Video source implementation evidence

2026-09-21. Video sources rebuilt; MP4 rendering remains with the integrator.

- Explicit `CHAPTERS` mapping covers all 60 chapters; machine-readable coverage is `video-photographic-coverage.json`.
- Full landscape photographs establish context for seven seconds in mapped scenario chapters, then hand off to full-stage authored diagrams. Procedural chapters have no decorative photograph strip.
- Safety phone/laptop displays use authored SVG screen replacements in original source coordinates. Full-frame visual inspection confirmed both devices remain visible and generated display text is covered; no arbitrary crop changes overlay registration.
- Existing diagrams are retained where pedagogically appropriate. New settings, scope, source-comparison, file browser, selection/comment, slide/crop, account/channel, community/source, workstation, wellbeing controls, appointment decision, results, website/app/service and acceptance-test diagrams cover new scene kinds. Missing diagram kinds fail generation instead of falling back to text cards.
- Short chapter-specific evidence captions supplement the diagrams. They do not replace the diagram with text panels. Recovery transitions to a separate approved-files → ZIP → extracted-files sequence.
- Library practice is consistent with the unchanged narration; encryption no longer shows the unrelated USB; worksheet-reading chapter no longer prematurely changes the input and total; search refinement and zoom restoration are visible state changes.
- `build-media.py --visual-only` copies only referenced photographs and rebuilds scene HTML/storyboards while retaining audio/caption/beat metadata. No audio generation or processing performed.

Verification:

- All 60 source WAV hashes equal `photo-audio-baseline.json`.
- All 60 scene generations checked for duplicate IDs and missing GSAP ID targets: zero failures.
- All 60 generated SVG scenes checked in Chromium for horizontal text overflow outside the 760-unit viewBox: zero failures (before final photo overlay; authored diagram text unchanged by overlay).
- All six HyperFrames 0.8.58 `check --strict --json` invocations exited zero, including final Week 5 screen-overlay font revision. Reports: `video-check-01.json` through `video-check-06.json`.
- This is source/runtime/layout validation. Rendered MP4 decode, file-size ceiling, final scene-transition review and playback checks remain for integration. These diagrams are authored instructional representations, not a recording of every actual software operation. Existing narration and learner practice provide the detailed procedure.
