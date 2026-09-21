# Screen-share video verification

## Delivered revision

Twelve screen-share walkthroughs replace selected diagram chapters across all six videos. Total walkthrough time is 553.730 seconds (9m14s). The remaining illustrated explainer chapters are retained. One silent, seven-second ElevenLabs-generated workstation shot introduces week 1; the task interfaces, cursor motion, click indicators, and typing are authored with HyperFrames.

## Verification evidence

- All **73** screen states passed source seeking, visible-state, label, and text-bound checks, including reverse seeking.
- The same **73** states were extracted from the final MP4s and compared to independently sought source frames. All passed the 0.95 structural-similarity threshold; lowest similarity was **0.977686**. Details: `screen-share-frame-verification.json`.
- Six strict HyperFrames **0.8.58** source checks passed runtime, layout, and contrast checks (**273 computed contrast checks** in total).
- All six MP4s passed full video/audio decoding, H.264/AAC and 1280×720/24fps checks, duration matching, black-frame detection, sound-level checks, fast-start layout, caption coverage, and the 20 MiB delivery budget. Details: `media-verification.json`.
- All six delivered AAC streams are **bit-for-bit identical** to the previous deliveries. No narration was regenerated, filtered again, or time-stretched. Caption words and timestamps are also identical; only the screen-demo cues move to the top title band. Details: `screen-share-audio-preservation.json`.
- The full site quality gate passed **120 Chromium tests**, build, internal links, catalog consistency, accessibility scan, and the report-only readability baseline. After the final caption placement and save-step refinements, all **3 focused video/chapter tests passed** against the rebuilt delivery, including top-positioned demo captions.
- Manual review included all twelve interface types, the generated clip at its beginning/middle/end, an encoded spreadsheet sequence, and native browser captions with player controls visible. The caption review exposed and corrected overlap over the result cell.

## Delivery hashes

| Week | Duration | Size | SHA-256 |
|---|---|---|---|
| 1 | 443.625s | 13.54 MiB | 3a79132678b8448d6c755e5dffca64bc072665b9c855a69fd7445a753a83f2a8 |
| 2 | 452.375s | 14.05 MiB | a33ecf43a470665114db2b7f72944c8c49d413d1709e3010467deba6c3b7f8fe |
| 3 | 444.625s | 13.09 MiB | 78b3a2096dd202dca75a4aeadb7c8caf443d7dbf31d906e9da50282942040bfd |
| 4 | 463.000s | 13.76 MiB | 77f0443d785e2ff4e4b9f7d93e56db1e0aab820f26aa097c9c3851865a65db22 |
| 5 | 461.250s | 13.81 MiB | 8b86e82c8ae2e65d0f87b4a6b3ef53ec881b609cab72e00634ab86979b83487b |
| 6 | 452.417s | 13.32 MiB | cd31f687cdccf800294aa3d590b690a6819d4ce995b51df4c2d87bb0ef5f8633 |

The six final MP4s and their manifest are the deployment assets. Working renders, source narration, and the generated opening source remain local and ignored. Representative encoded frames are under `review/screen-share/`.

## Review boundary

Prepared for draft PR 17 and its Netlify preview. Production publication remains separate. Interfaces are original, clearly labeled simulations with fictional data; they are not exact recordings of a particular operating system or commercial application. Menu wording in a learner’s software can vary. Classroom projector/audio checks remain an instructor acceptance step.
