# Screen-share video revision

The six existing teaching videos now include two task walkthrough chapters each: **12 screen simulations, 9 minutes 14 seconds in total**. They replace the diagrams in those chapters while retaining Britt’s approved V3 narration, Voice Isolator cleanup, full caption text, chapter timing, and overall video lengths. No time stretching or new voice processing is applied.

## Exact placements

Times below identify the chapter start; the chapter menu is the preferred replay control.

| Week | Chapter / task | Start | Walkthrough length |
|---|---|---|---|
| 1 | 2: Make a webpage readable | 0:40 | 44.5s |
| 1 | 7: Make a calendar entry you can act on | 4:24 | 44.8s |
| 2 | 6: Give your files a home you can recognize | 3:38 | 43.5s |
| 2 | 7: Choose access by what the partner must do | 4:22 | 50.8s |
| 3 | 2: Give the document a readable structure | 0:43 | 44.1s |
| 3 | 5: Build a formula and challenge it | 2:53 | 51.9s |
| 4 | 4: Check who receives the message | 2:21 | 51.5s |
| 4 | 6: Give feedback that leads to a useful change | 3:58 | 41.9s |
| 5 | 4: Verify through a route you already trust | 2:17 | 50.7s |
| 5 | 7: Grant camera and microphone access for a reason | 4:38 | 42.8s |
| 6 | 6: Open a working version before changing it | 3:48 | 44.7s |
| 6 | 7: Test the happy path and the missing result | 4:32 | 42.6s |

## Teaching treatment

- An original desktop/application interface fills most of the video. A gold pointer moves to the relevant control, a click ring marks the action, and numbered action labels identify the current step.
- Menus, fields, selected text, typed entries, saved states, and checked outcomes follow the actual word timestamps. A missing narration phrase stops the source build rather than silently guessing the timing.
- Worked outcomes include zoom restoration; a reopened calendar event; a file reopened from its folder; commenter access verified as a partner; a heading appearing in document navigation; a formula changing from $25 to $28; removing an unnecessary email recipient; resolving a comment after the edit; using an independently found contact; blocking an unrelated camera request; keeping an HTML extension; and passing/failing search-and-category combinations.
- Every screen is labeled as a simulation using fictional data, with a reminder that menus vary by application. These are original teaching interfaces, not recordings of Microsoft, Google, or another commercial product. Nothing is sent or purchased.
- During screen demonstrations, WebVTT captions use the title band at the top of the picture so native playback controls cannot push captions over task fields or results. Caption text and timestamps are unchanged.
- All twelve chapters are marked **Screen demo** in both players’ chapter menus. Their transcript sections include expandable, printable visual-step guides, alongside the unchanged narration transcript.
- Week 6’s supplied starter and worksheet now use **Community library**, matching the existing narration and slide examples. The category test uses **Community**, which exists in the supplied starter.

## ElevenLabs generation

One photographic workstation clip was generated through the hosted ElevenLabs video tool with `gemini-omni-1.1-flash`. The model returned 10 seconds; the first seven seconds are used silently at the opening of week 1. The clip is an establishing shot, not the task demonstration itself. Precise UI, text, and pointer actions are authored locally so the instruction remains reliable.

The generation receipt (model, prompt, generation ID, cost, source/delivery hashes) is `video/digital-literacy-2/generated-screen-share/receipt.json`. Keep its local source MP4s to rebuild. Source working clips and narration are intentionally excluded from deployment; only the six verified course MP4s ship.

## Authoring and verification

- `scripts/dl2/screen-share-scenes.py`: original interfaces, task states, and exact narration cues.
- `scripts/dl2/build-media.py --visual-only`: regenerates scenes and `screen-share-actions.json`, without rewriting audio, captions, or chapter files.
- `node scripts/dl2/check-screen-shares.mjs`: seeks all 73 states in reverse order and checks visibility, label consistency, text bounds, and deterministic seeking; writes local screenshots and a report.
- HyperFrames strict source checks cover all six compositions, including runtime, layout, and computed contrast.
- `scripts/dl2/verify-media.py` validates final container/codec/duration, decodes all video and audio, checks levels and black frames, verifies caption/alignment integrity, and refreshes the SHA-256 deployment allowlist only after passing.
- The Playwright chapter test checks discoverability, keyboard replay without autoplay, transcript step guides, and the actual starter app’s narrated search cases.

Delivery results are recorded in `SCREEN-SHARE-VIDEO-VERIFICATION.md` after rendering and preview verification. This revision is for draft PR 17; production publication is separate.
