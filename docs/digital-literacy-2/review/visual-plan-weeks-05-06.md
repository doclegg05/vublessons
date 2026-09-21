# Photographic refinement audit: Weeks 5–6

Plan only. Audited 2026-09-21 against the generated `presentation.html` files, `scripts/dl2/scenes.py`, `scripts/dl2/video-scenes.py`, and both full teaching scripts. No learner content, media, assessments, or deployment changed.

## Direction and implementation boundaries

Preserve the approved navy/gold learning interface, all existing interactions, objectives, lesson order, and assessment alignment. Use believable photographs to establish a situation; use authored HTML/SVG and actual local starter-app demonstrations to explain behavior. Generated device screens must not carry instructional text. Compose readable fictional examples separately. Photographs are neither proof of a real event nor screenshots of the software being taught.

The supplied context recommends the fourth photographic workstation and third photographic safety candidate. Before integration, visually review their full-resolution files, confirm the actual selected generation, and test the existing crop slots. Do not assume suitability from candidate numbering alone.

Week 5 has 20 slides; Week 6 has 24. Each has ten video chapters. Videos currently reuse one `assets/topic.webp` image in a fixed narrow photographic strip, while authored SVG diagrams animate to narration. Retain semantic instructional diagrams, but replace repeated decorative strips with topic-specific establishing images and larger demonstrations. User decision: retain current Britt narration except verified teaching gaps. A mismatched diagram is a visual repair, not by itself a reason to regenerate narration. Use specifically West Virginia home, library and community themes with fictional names and data; do not invent claims about real institutions.

## Week 5: exact slide map

| Slide and exact title | Current visual/feature | Decision and specific change |
|---|---|---|
| 1 — Week 5: Protect your work and show your skills | Functional fictional phishing inbox + objectives | **Refine:** selected safety photo as scenario opener beside the existing inspect/verify controls; keep those controls reachable and visually dominant. Never bake the urgent message into the photo. |
| 2 — Safety is a set of decisions | Discussion with reused security illustration | **Replace illustration:** same person calmly checking devices; two compact response cards, “Protect my work” and “Work comfortably,” to support the existing prompt without creating a new scored task. |
| 3 — A comfortable workstation | Screen/Input/Break selectable concept panels + workstation artwork | **Replace image, retain panels:** selected realistic workstation with keyboard-focusable numbered hotspots matching Screen/Input/Break. Use flexible setup language; do not label a single posture universally correct. |
| 4 — Universal design helps more people | Captions/Keyboard/Readable controls panels | **Refine diagram:** a fictional media panel, visible Tab focus sequence, and large-text before/after. Keep existing tabs; no photo needed because the settings themselves teach the concept. |
| 5 — Protect attention and wellbeing | Alerts/FOMO/Stopping point panels | **Refine UI:** authored notification stack switches to a quiet task view; learner controls the switch. Optional unobtrusive natural desk photo only in the surrounding scenario frame. |
| 6 — An online identity can be invented | Profile/Pressure/Verify panels | **Refine UI:** fictional profile and message pair, with pressure/request details revealed separately; show independent-contact route. Do not use a realistic portrait to imply a real person is fraudulent. |
| 7 — Respond to harmful posts | Pause/Record/Support panels | **Refine UI:** neutral fictional conversation, overflow menu, report/block options and support route. All actions remain a clearly marked local simulation; no graphic or humiliating message content. |
| 8 — An urgent message is not proof | Functional inspect-link and independent-check phishing simulation | **Keep core:** expand authored inbox and verified-route panels, with restrained photo thumbnail tying back to slide 1. The evidence and learner decision receive most space. |
| 9 — Choose a safer next step | Three flip cards: unknown USB, calculator camera request, benefits-payment message | **Refine fronts:** real-looking disconnected USB still life, authored camera request, authored message. Retain answers, keyboard flip behavior, and explicit labels; no real benefits-site branding. |
| 10 — Encryption protects readable data | Original/Read-only/Encrypted functioning simulation | **Keep and clarify:** paired “Can read?” and “Can edit?” indicators with text/icons. Remove decorative photo from this teaching area. Any scrambled text stays explicitly illustrative. |
| 11 — Passwords protect different actions | Open/Edit/Recovery concept panels | **Refine diagram:** side-by-side fictional “password to open” and “restrict editing” controls, followed by a separate recovery-location card. Do not show a real password or imply every password encrypts a file. |
| 12 — Unknown devices can carry risk | Found/Pause/Procedure concept panels | **Replace illustration:** close-up of ordinary disconnected USB drive on a lab desk. Sequence ends at a labeled authorized-staff tray; never depict plugging it in. |
| 13 — Control camera and microphone access | Functional Allow/Deny camera simulation | **Keep; add visual contrast:** authored meeting versus text-resource-page contexts so task need is visible. Preserve current question and feedback; adding a second scored question would require content review. |
| 14 — Watch: pause, verify, protect | Player, transcript and ten chapter buttons | **Refine poster/chapter imagery:** use safety scenario photo with short title; distinct chapter thumbnails for workstation, inbox, file protection, USB and permission topics. Preserve explicit Play and chapter-pauses behavior. |
| 15 — Practice the whole routine | Worksheet link + repeated security illustration | **Replace decoration with task map:** source → useful file → limited access → recovery choice, with small evidence slots matching the worksheet. Photo is optional; task evidence is primary. |
| 16 — Knowledge check: encryption | Multiple-choice question | **Keep:** neutral file/key diagram only if it does not reveal the answer before selection. No change to choices, scoring or feedback. |
| 17 — Knowledge check: camera access | Multiple-choice question | **Keep:** show a neutral fictional text-page frame without a pre-highlighted allow/deny answer. |
| 18 — Take the post-test | Assessment link + security illustration | **Keep action:** replace decoration with an unscored fictional results-sheet motif; do not expose test answers or imply certification. |
| 19 — Read your results as a learning plan | Summary + repeated security illustration | **Refine:** authored sample domain-score card → missed-skill explanation → chosen practice task. Clearly fictional; match current results interface and avoid real learner records. |
| 20 — You completed this lesson | Completion + repeated security illustration | **Refine:** calm scenario photo crop and two visual reflection slots (skill/next step); preserve completion and next-week navigation. |

## Week 5: exact video chapter map

Current chapter identifiers below are visible teaching-script titles. The existing `kind` names identify the diagram dispatched by `video-scenes.py`.

| Chapter | Current diagram | Specific treatment |
|---|---|---|
| 1 — Use judgment, not fear, to stay safer | `verify`: Evidence/Verify/Safer action tiles | Safety photo establishes ordinary home context; transition to three authored actions. Keep learner experience question and pause. |
| 2 — Set up for comfort and control | `routine` | Workstation photo with screen/input callouts, then large caption/text-size/focus demonstrations. Avoid an entire chapter of a static photo. |
| 3 — Recognize pressure in a message | `phishing` | Large fictional inbox, staged emphasis on claim, requested action and pressure. Reveal only the element discussed; no click on a real link. |
| 4 — Verify through a route you already trust | `verify` repeats generic three tiles | Replace generic repetition with a split-path diagram: message-supplied route versus independently opened fictional contact page. Visually follow only the safer independent route. |
| 5 — Separate editing restrictions from encryption | `encrypt` currently includes unrelated unknown USB tile | Remove USB from this chapter. Demonstrate readable-but-not-editable file versus protected unreadable data; key unlock transition with explicit limits. |
| 6 — Treat unknown devices cautiously | `usb`: drive/do-not-connect/staff tiles | USB photograph → visible disconnected state → authorized-staff handoff illustration. Keep no-connection rule visible throughout. |
| 7 — Grant camera and microphone access for a reason | `access` | Two readable fictional permission prompts, meeting versus text page. Show task justification before allow/deny outcome. |
| 8 — Protect attention and respond to harmful behavior | `attention` primarily notification stack/break | Broaden visuals to cover the actual narration: fictional identity claim, notification controls, then report/block/support menu. Existing single attention graphic misses the latter teaching points. |
| 9 — Practice the complete decision process | `phishing` repeated inbox | New fictional appointment-code message; three separate evidence/unverified/next-action cards. Pause card before explanation, avoiding answer disclosure too early. |
| 10 — Use results to choose your next practice | `verify` generic tiles | Replace with fictional current-style results report → choose practice → demonstrate a skill. Keep classroom-score/non-certification explanation visually available. |

## Week 6: exact slide map

| Slide and exact title | Current visual/feature | Decision and specific change |
|---|---|---|
| 1 — Week 6: Build a small web app with AI | Functional fictional resource search + objectives | **Refine:** natural community-workspace photo establishes a useful task; enlarge the working app and retain live search controls. |
| 2 — Solve one small problem | Discussion + repeated building illustration | **Replace:** photographed blank resource notebook/ordinary planning desk beside an authored fictional list transforming into the finder. No generated names or contact details. |
| 3 — Website, web app, and SaaS | Website/Web app/SaaS selectable panels | **Refine diagram:** same resource content presented as static list, filtered interactive list, then hosted service boundary with ongoing responsibilities. Keep differences explicit without implying all websites lack interaction. |
| 4 — Vibe coding starts with clear instructions | Describe/Generate/Test concept panels | **Refine:** three connected authored artifacts: task statement, proposed code, observed result. Avoid generic robot/AI art. |
| 5 — Three parts of a browser app | Working HTML/CSS/JavaScript layer simulation + flip cards | **Keep:** highlight corresponding structure, presentation and behavior in the same starter UI. Ensure an authored readable code excerpt; no screenshot of tiny code. |
| 6 — Write acceptance checks first | Three practice checklist buttons | **Refine:** expected-result cards for named match, keyboard focus and no-results state; maintain existing practiced markers. |
| 7 — A prompt with useful boundaries | Interactive local prompt builder | **Keep:** visually group task/controls/data/checks; show generated prompt as selectable readable text. No image in the prompt field. |
| 8 — Ask the AI to explain its work | Data/Files/Checks concept panels | **Refine:** three linked views of starter source, rendered app and test evidence. Select an explanation to highlight the matching real artifact. |
| 9 — Start with a working reference | Live search simulation; starter open/download | **Keep functional demo:** show version filename badge and three test-state tabs. Avoid photo overlay across the actual app. |
| 10 — No AI account? You can still build | Copy/Edit/Open concept panels | **Refine:** authored editor → save as `.html` → browser view sequence using the supplied starter. Show actual heading/resource changes; preserve no-account pathway. |
| 11 — Make one change at a time | Save/Compare/Retest concept panels | **Refine:** version cards plus small readable before/after diff of a single change and pass/fail labels. |
| 12 — A useful revision request | Problem/Request/Preserve panels | **Refine interactive preview:** weak focus versus visible focus on the same search/filter controls. Preserve search; learner can Tab through both examples safely. |
| 13 — Where does the data live? | Page array/Browser storage/Database panels | **Refine diagram:** file, one-browser container and authorized shared-service boundary; explicit “not synchronized” label on local storage. Do not imply adding a database is part of this lab. |
| 14 — Keep secrets out of browser code | Inspect/Exclude/Practice panels | **Refine:** authored source drawer containing only fictional resource data; excluded-secret labels remain placeholders, never usable credentials. |
| 15 — A mock sign-in is not security | Screen/Rules/Prototype panels | **Refine diagram:** decorative form separated from actual server access boundary. Do not implement a login or collect password input. |
| 16 — Watch: prompt, test, revise | Player/transcript/chapter buttons | **Refine poster and chapter thumbnails:** realistic planning photo, working app, test log, versions. Preserve player and navigation. |
| 17 — Test more than the happy path | Live finder + practice checklist | **Keep/expand presentation only:** show blank, no-match, mixed-case, category, narrow-screen and keyboard evidence as selectable test cards. Any new test logic must reflect actual starter behavior. |
| 18 — Fix what you can demonstrate | Steps/Expected/Actual panels | **Refine:** reproducible uppercase failure shown only in an explicitly broken demonstration; side-by-side expected/actual followed by repaired state. Do not introduce the bug into the downloadable reference. |
| 19 — Hosting is a separate decision | Local/Hosted/Maintain concept panels | **Refine diagram:** saved file on one device → hosting boundary → visitors, with ownership/cost/data/backup responsibilities. No deployment or account signup added. |
| 20 — Knowledge check: AI confidence | Multiple choice | **Keep:** neutral test-log motif; no preselected correct evidence cue. |
| 21 — Knowledge check: a secret key | Multiple choice | **Keep:** neutral code-file motif with no example credential and no answer giveaway. |
| 22 — Lab: build, test, explain | Worksheet link + building illustration | **Replace decoration:** four concrete evidence cards: saved app, revision, test log, limitation. Optional community-workspace photo in secondary frame. |
| 23 — You can direct a build and judge it | Summary + building illustration | **Refine:** deliverables portfolio strip (prompt/source/tests/next step) using fictional authored examples. |
| 24 — You completed this lesson | Completion + building illustration | **Replace image:** natural peer-demonstration photo; retain skill/next-step prompt and return-to-course navigation. No fake certification badge. |

## Week 6: exact video chapter map

| Chapter | Current diagram | Specific treatment |
|---|---|---|
| 1 — Build something small enough to understand | `app`: search/filter/result diagram | Planning-desk photo → fictional paper list → real local starter working in browser. Introduce all controls with brief callouts. |
| 2 — Distinguish a website, an app, and a service | `parts`: HTML/CSS/JavaScript tiles | **Correct visual-topic mismatch:** replace programming-layer graphic with static content / interactive task / operated hosted service comparison. |
| 3 — Understand the three parts of the page | `parts` again | Keep layers concept, but highlight actual heading/input structure, layout and filter behavior in the starter. |
| 4 — Write checks before asking for code | `prompt`: Task/Controls/Tests/Boundaries tiles | Replace repeated generic tiles with written observable test → browser action → expected result, three compact examples. |
| 5 — Give the AI a bounded, useful request | `prompt` again | Build a readable authored prompt in four labeled chunks; keep private-data boundary visible. No vendor UI dependency. |
| 6 — Open a working version before changing it | `app` repeats search | Show save/copy filename, `.html` extension, local open, heading edit and refresh. Keep both AI and no-account paths clear. |
| 7 — Test the happy path and the missing result | `app` animated match/no-match | Preserve and extend actual demonstration to uppercase and category intersection, with expected/actual rows tied to narration. |
| 8 — Test access, screen size, and data assumptions | `keyboard`: focus graphic + short footer | Show real Tab focus progression, narrow viewport without clipping, then separate bundled/local/shared-data diagram. Current mostly-keyboard visual underrepresents the latter topics. |
| 9 — Request one repair and retest what worked | `versions`: version cards + restore | Show uppercase bug report, focused change, failed test now passing, previous category check still passing, and preserved old file. Tiny code is optional; observed behavior is essential. |
| 10 — Demonstrate the result and name its limits | `versions` repeats same version diagram | Peer-demo photo briefly, then saved app/test log/limitation evidence. End with explicit local-prototype versus public-service boundary, not another version graphic. |

## Asset briefs and reuse

1. **Approved workstation photo:** Week 5 slide 3/video chapter 2. Retain natural light, ordinary gear, uncluttered neutral monitor, room for authored hotspots. Check narrow crop does not omit keyboard/input device. Existing selected candidate should be reused if it passes review; no need to generate another by default.
2. **Approved safety photo:** Week 5 slides 1/2/8/14/20 and video chapters 1/4. Older adult comparing phone and laptop; neutral unreadable device content replaced with separate authored panels. Crop subject and both devices together. Reuse thoughtfully rather than showing identical full image every chapter.
3. **Disconnected USB still life:** one new realistic asset, ordinary unlabeled USB on lab desk, device visibly separate from ports; no dramatic hacker aesthetic. Week 5 slides 9/12 and chapter 6.
4. **Community planning desk:** one new realistic asset for Week 6 slides 1/2/16 and chapter 1. Everyday West Virginia community-room or home setting, notebook, pencil, laptop, no readable text, no brands, believable lighting; subtle wooded-hills context through a window is optional, never a stereotype. Author resource list on top or alongside in HTML.
5. **Peer app demonstration:** one optional new photo for Week 6 slides 22/24 and chapter 10. Two older adult learners at an ordinary fictional West Virginia community-library workstation, adult-to-adult collaboration, readable screens authored separately. Avoid military insignia, stereotypes and implied real endorsement.
6. **Authored instructional assets:** fictional inbox/contact page, permission panels, file-protection states, report sample, actual starter states, test log, version comparison and service/data boundaries. Build from existing semantic components wherever possible rather than generated raster UI.

## Resolved choices and remaining options

Resolved: West Virginia themes; retain current Britt narration except verified teaching gaps. Place names, schedules and service records in examples remain fictional. Do not imply a generated room belongs to a real library, VA office or other institution.

- Recommend **a small coherent photo set plus exact interactive UI**, not a photo on every slide. Most Week 6 teaching needs visible working behavior, not additional decorative pictures.
- Recommend actual course-starter recordings/authoring for Week 6; vendor-specific AI UI would age rapidly and exclude the no-account route.
- Decide whether optional peer-demo photo adds enough value to justify another generated asset; a real app/result montage may be clearer and cheaper.
- Follow the resolved narration choice: reuse Britt narration and caption timing for visual-only changes. Several chapter graphics need remapping; no verified teaching gap was found in these twenty chapter scripts. Escalate only a concrete instructional gap that cannot be repaired visually.
- Do not add new scored assessment behavior, accounts, real contact records or publication steps as part of a visual pass.

## Verification and authoring risks

- Make changes in source generators, not only generated pages; regenerate once centrally to avoid multi-agent write collisions.
- Every slide button remains semantic and keyboard accessible; hover/hotspots require equivalent focus/activation and visible focus. No automatic slide progression.
- Check authored labels, captions and existing site text-size controls at desktop, narrow screen and enlarged text. Slide body text stays at least the repository's 24pt requirement.
- New photos require useful alt text only where they convey information; decorative repeats keep empty alt text. A scene's teaching meaning must also exist in text/controls.
- Check selected images for hands, hardware, fake text, recognizable real logos and crop loss. Do not call them final-quality without full-resolution visual review.
- Video updates must rebuild manifests/hashes and captions only as needed, test all six packaged media files, verify each changed chapter against narration, and retain intentional learner pauses.
- Preserve pre/post parallel content and question ordering. Do not add contextual imagery that reveals a correct answer before submission.
