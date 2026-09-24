# Photographic realism plan — weeks 3 and 4

Plan-only audit, 2026-09-21. User-resolved direction: specifically West Virginia themes and current Britt narration retained except verified teaching gaps. No learner page, image, narration or video changed. Grounded in the current generated presentations, `scripts/dl2/scenes.py`, `workshops.py`, `video-scenes.py`, and both ten-chapter teaching scripts. Slide numbers below are the one-based visible navigation numbers. Video chapters use exact script titles; timestamps may change on a later rebuild.

## Direction and source ownership

Keep the approved navy/gold learning-app shell, progressive explanations, keyboard controls and interactive models. Use natural photographs to establish people, tasks and familiar surroundings; use authored HTML/SVG fictional interfaces for the actual instruction. Generated screen lettering is never the teaching surface. Avoid replacing informative diagrams with decorative photography.

The current conceptual scenes repeat `slide-creation.webp` throughout week 3 and `slide-collaboration.webp` throughout week 4. Replace those repeated side illustrations with topic-specific authored artifacts, using a photograph only where it adds context. Editing only the generated HTML would be overwritten: implementation belongs in `scenes.py`, `workshops.py`, relevant content authoring entries and `video-scenes.py`, then regenerated pages. Keep audio/captions unless a factual script change proves necessary.

## Week 3 — Create something people can use

| Slide | Exact title | Current feature | Specific decision |
|---|---|---|---|
| 1 | Week 3: Create something people can use | Welcome art, supply formula simulation, objectives | Change welcome art to P3-A community resource-planning photo. Keep working formula teaser and objectives; photo supports purpose, not calculation. |
| 2 | Create for someone specific | Discussion prompt | Add P3-A cropped on learner/handout with three authored audience-needs cards: find service, know next step, find help. Keep open question and invite a task from learners' lives. |
| 3 | A document needs structure | Plain/heading+steps simulation | Keep simulation; add visible document outline linked to true heading structure, before/after state labels. No photograph. |
| 4 | Keyboard shortcuts with a purpose | Copy/paste/undo/save choice scene and repeated creation image | Replace side image with authored keyboard keycaps and selection/cursor demo. Show Ctrl and Command alternatives without implying identical physical keyboards. Keep all four states. |
| 5 | Make one clear paragraph | Vague/useful toggle | Keep wording comparison; render it as the same handout with highlighted service/next action. Replace generic image with handout preview. |
| 6 | Track a proposed change | Propose/accept/reject scene | Upgrade to readable fictional editor: insertion/deletion markup, two labeled decision buttons and document result. Preserve original state and undo/reset. |
| 7 | Prepare a handout someone can read | Heading/link/image choices | Show one document with navigable heading, meaningful link and alt-text example. Use small P3-B image only inside the image example; teach informative versus decorative purpose explicitly. |
| 8 | A workbook has rows, columns, and cells | Highlighted row/column/cell table | Keep authored grid, selected-address readout and all labels. Remove repeated decorative creation image to increase cell size. |
| 9 | Build a fictional supply budget | Editable paper cost, calculated total, CSV link | Keep functional input/download. Add formula-range bracket and item icons for paper/folders/pens; icons supplement labels, never replace values. |
| 10 | Check the formula, not just the appearance | Working 12→15 cost/25→28 total simulation | Keep interaction; show prediction-before-change and visually connected changed input/result. Add a labeled manually typed stale-total comparison without changing correct underlying calculation. |
| 11 | A chart answers a question | Interactive labeled bars and data table | Keep model and accessible table; use cost→bar correspondence outlines, consistent zero baseline and labels. No decorative photo. |
| 12 | Three slides; one useful message | Need/steps/help choice scene | Replace repeated image with three actual miniature slides that expand into readable views. First uses P3-A, second authored steps, third authored next-action/contact card. |
| 13 | Crop, resize, and preserve the original | Original/crop/resize demo using original community SVG | Keep existing artwork as default, since its labels/credit make cropping consequences explicit. Offer P3-B as an optional second example only if scope allows; never crop away a necessary action or attribution. |
| 14 | Basic video editing | 20-second timeline trim/split demo | Keep timeline; add authored storyboard thumbnails and caption/audio lanes so retained speech and removed pause are visible. No new paid video generation required. |
| 15 | Watch: create, check, and export | Chaptered video and transcript | Keep controls/transcript; refresh video per chapter map below and choose poster from P3-A plus authored pack preview. |
| 16 | Reusing content requires permission | Find/check/credit choice scene | Replace repeated image with fictional asset-detail panel containing clearly illustrative license/credit fields. Do not imply any actual third-party asset is licensed merely because the mockup says so. |
| 17 | Choose a format for the next person | DOCX/PDF/CSV preview plus flip cards | Keep interaction and flip cards; display same source as editable page, fixed layout and plain rows. Explicitly visualize formatting/formula loss for CSV. |
| 18 | Inspect the export | Open/inspect/locate choice scene | Replace repeated image with side-by-side authored editor/export previews and keyboard-operable issue hotspots for page break, link and missing image; final state shows correct filename/folder. |
| 19 | Knowledge check: a changing total | Multiple-choice formula question | Keep question/answers/scoring. Add neutral worksheet context with row/column labels, avoiding a highlighted answer range before submission. |
| 20 | Knowledge check: a proposed edit | Multiple-choice review question | Keep question/answers/scoring. Small neutral proposed-change preview; reveal accept/reject explanation only after response. |
| 21 | Lab: your resource pack | Worksheet link and lab prompt | Add three authored artifact previews and task-completion checklist with links to the existing worksheet; use P3-A as restrained context if space permits. |
| 22 | Useful beats elaborate | Summary | Show completed handout, checked $28 workbook and export inspection as three visual evidence cards. Keep summary and readable text. |
| 23 | You completed this lesson | Reflection and next-week link | Keep completion/navigation; show small resource-pack evidence motif, not another large photo. |

### Week 3 video chapter map

Current video uses original SVG diagrams; the mapping below targets the exact visual topic attached to each chapter. Retain explanations, practice pauses and narration length. Each chapter should move through context → close-up action → visible result as applicable, with only short labels outside captions.

| Chapter | Exact title | Current visual | Planned treatment |
|---|---|---|---|
| 1 | Create for a person and a purpose | `document`: numbered handout | Open with P3-A and three finished artifacts; move into a legible authored handout, identifying audience and next action. |
| 2 | Give the document a readable structure | `document`: same handout | Show plain page → applied heading style → outline entry → numbered steps and meaningful link. Keep selected text readable for the sentence explaining it. |
| 3 | Edit without losing useful work | `feedback`: contact comment diagram | Replace with select/copy/undo sequence followed by comment versus tracked suggestion. Current generic feedback diagram underrepresents selection and recoverability. |
| 4 | Read a worksheet like a labeled table | `sheet`: grid plus formula/total | Reveal rows, columns, B2 and units progressively. Keep initial values 12/8/5; defer formula change to next chapter to avoid premature visual result. |
| 5 | Build a formula and challenge it | `sheet`: 12→15, total25→28 | Show cursor entering `=SUM(B2:B4)`, range emphasis, prediction pause, changed input and total. Include quick stale typed-total contrast. |
| 6 | Choose a chart that answers a question | `chart`: bar chart with15/8/5 | Keep bars, add linked source table and title/units. Show the chart updating only after paper changes; keep numeric state continuous from chapter5. |
| 7 | Make slides and images serve the message | `bundle`: artifact icons | Show actual three-slide storyboard using P3-A and authored steps. Demonstrate crop versus proportional resize on P3-B or original artwork; original remains visible. |
| 8 | Edit a short clip for understanding | `media-edit`: labeled timeline blocks | Add thumbnails, playhead, trim handles, split removal and readable caption cue; visually inspect both cut boundaries. Keep actual speech intelligibility, no decorative transitions over editing steps. |
| 9 | Choose a format and inspect what survives | `export`: DOCX/PDF/CSV tiles | Show same source through three export outputs, preserving/layout/data distinctions, followed by reopened file inspection and credit record. |
| 10 | Test the pack with another person | `bundle`: handout/workbook/slides icons | P3-A brief partner-review context, then annotated completed artifacts showing next action, responsive total and one corrected confusion. End with learner-selected transfer task, not extra stock imagery. |

## Week 4 — Communicate and collaborate with care

| Slide | Exact title | Current feature | Specific decision |
|---|---|---|---|
| 1 | Week 4: Communicate and collaborate with care | Welcome art and feedback simulation | Add P4-A small-group planning photo as welcome image. Keep the feedback teaser and objectives. |
| 2 | Choose a channel for the task | Discussion prompt | Add task cards connected to message, shared document and live conversation icons; include response-time/sensitivity labels. Use P4-A only as context, not an answer. |
| 3 | Personal and professional identities | Account/tone/protection choices | Replace collaboration image with authored account-switcher showing fictional Training and Personal profiles plus explicit active-account label. No real account names or credentials. |
| 4 | Write an email someone can act on | **Currently reuses shared-document feedback simulation** | Replace mismatched simulation with fictional email composer: subject, request, context, attachment and recipient review. Keep draft-only behavior; no Send/network action. This is the clearest functional mismatch found. |
| 5 | To, Cc, and Bcc | Recipient-field choices | Keep fields; add recipient-view comparison so Bcc visibility is demonstrated, not inferred. Retain warning that Bcc is not encryption. |
| 6 | Timing changes how a message lands | Deadline/hours/schedule choices | Replace repeated photo/illustration with authored day timeline and send-later preview. Include response deadline and final review state; no cohort dates. |
| 7 | Inclusive language helps people respond | Name/abbreviation/invitation choices | Show before/after message cards with change emphasis. Keep respectful wording; no stereotyped older-adult imagery. |
| 8 | Participate in a community | Read/disagree/share choices | Pair optional small P4-A crop with fictional community thread; selectable guideline, respectful response and permission checkpoint. Never imply photo subjects are real group members. |
| 9 | Verify a community service | Lead/confirm/use choices | Replace generic illustration with side-by-side fictional directory and official-contact record. User-triggered highlights identify what still needs confirmation; avoid inventing real hours/eligibility. |
| 10 | Collaborate on one shared copy | Owner/writer/reviewer choices | Keep diagram, replace generic art with actual common document thumbnail and named role/access badges. Show all roles pointing to one authoritative copy. |
| 11 | Live editing or later feedback? | Synchronous/asynchronous flip cards | Keep accessible cards; add two visual timelines with simultaneous cursors versus staged comment→response. No auto-advance. |
| 12 | Feedback names an improvement | Feedback simulation | Keep and enhance selected passage, comment anchor, requested change and resulting paragraph. This is the correct location for the current feedback model. |
| 13 | Acknowledge and resolve | Read/respond/resolve choices | Show fictional threaded comment and resolved state plus version-history recovery preview. Keep “decline with reason” path visible. |
| 14 | Meetings and webinars | Simulated mute/raise-hand controls | Keep no-device-permission simulation. Add P4-B contextual inset/poster, then authored sound selector, caption toggle and backup-notes pathway; all controls explicitly simulated. |
| 15 | Watch: collaborate without confusion | Chaptered video/transcript | Keep accessible controls; replace poster with P4-A and refresh scenes below. |
| 16 | Goods, services, and subscriptions | Three category choices | Replace repeated collaboration illustration with distinct physical keyboard photo crop, authored service appointment and recurring calendar receipt. Use P4-C for good, icons/UI for abstract categories. |
| 17 | Review a digital payment | Seller/total/terms choices | Build readable fictional checkout with item$10+delivery$2=$12, renewal/terms and disabled-by-design payment capability. User selects details to inspect; do not add real payment fields. |
| 18 | Small in-app purchases add up | Download/extras/controls choices | Authored fictional app receipt adds three$2 items and updates total$6; clearly label practice. Keep purchase-settings concept; no gamified pressure to buy. |
| 19 | Knowledge check: useful feedback | Multiple-choice question | Keep unchanged scoring/wording. Add neutral document excerpt; do not preview the correct comment. |
| 20 | Knowledge check: a trial offer | Multiple-choice question | Keep unchanged scoring/wording. Add neutral fictional offer card; after response reveal price/timing/cancel checklist. |
| 21 | Lab: coordinate a small team | Worksheet link and lab prompt | Add visual draft→comment→decision sequence and fictional offer comparison. Keep partner-role swap and worksheet. |
| 22 | Leave a clear next step | Summary | Three visual evidence cards: actionable draft, revised handout, recorded decision. Keep concise recap. |
| 23 | You completed this lesson | Reflection/next link | Keep completion behavior; use small collaboration evidence motif rather than repeated large photo. |

### Week 4 video chapter map

| Chapter | Exact title | Current visual | Planned treatment |
|---|---|---|---|
| 1 | Coordinate a task people recognize | `roles`: owner/writer/reviewer→one copy | P4-A planning context, then reveal familiar task, needed output and role diagram. Avoid starting with unexplained role icons alone. |
| 2 | Choose the channel and identity deliberately | `timing`: together/later rows | Show task→channel choice, active fictional account and permission context. Retain timing diagram for the partner-who-cannot-meet example. |
| 3 | Write a message someone can act on | `message`: three message strips | Full readable fictional composer with subject, requested section, response time and attached common handout; highlight each during narration, keep no-send cue. |
| 4 | Check who receives the message | `email-fields`: To/Cc/Bcc definitions | Animate recipient chips and separate recipient-view panel; show reply-all list inspection and realistic response window. No actual email addresses required. |
| 5 | Work from one shared copy | `roles`: three roles→common file | Start with three conflicting fictional files, consolidate into one agreed copy; then roles/access and synchronous/asynchronous timelines. |
| 6 | Give feedback that leads to a useful change | `feedback`: add-contact comment/result | Vague→specific anchored comment, writer question/acceptance/alternative, edited contact section and resolved thread. Keep explanation of reason. |
| 7 | Join a meeting prepared to participate | `meeting`: participant tiles and controls | P4-B short contextual opening; authored device selector/test, mute, hand, captions and notes fallback. Show recording permission as request/choice, not default capture. |
| 8 | Participate in a community thoughtfully | `verify`: safety-style independent-contact visual | Replace generic verification scene with fictional community post→official-source comparison, privacy-safe draft and unanswered facts checklist. Preserve independent verification principle. |
| 9 | Review a digital purchase before committing | `commerce`: trial→$12 monthly | Readable fictional offer, timeline due-now/future-charge, cancellation section and explicit stop-if-missing-data state. Carry current$12/month example consistently; do not confuse with slide17’s one-time$12 checkout. |
| 10 | Leave a clear record of the next step | `message`: subject/request/time strips | Completed draft, shared document access and recorded decision arranged as evidence; brief P4-A partner-review return. Finish on transferable habit and pause prompt. |

## New asset briefs and reuse limits

| ID | Asset brief | Exact planned uses | Requirement |
|---|---|---|---|
| P3-A | Natural editorial photograph of two older adults collaboratively planning a fictional community computer-help handout at an ordinary fictional West Virginia community-library table, with understated Appalachian landscape visible through a window; full-size laptop, paper draft and supplies, comfortable daylight, varied capable adults, realistic anatomy, no logos/uniforms/readable generated text. | W3 slides1,2,12,optional21; video chapters1,7,10 and poster. | One source with several intentional crops; keep documents large enough for context but add legible examples as separate authored UI. |
| P3-B | Overhead photo of simple community-event materials: notebook, pencil, blank handout and a small original illustrative photograph, ordinary table, edge details that permit useful crop/resize demonstration. | W3 slide7 image example; optional13 second sample; video7. | Optional asset: current original community SVG already teaches crop/resize correctly; no regeneration necessary if budget constrained. |
| P4-A | Three older adults planning a small volunteer/community computer-help session around one laptop and paper notes, equal participation, ordinary accessible fictional West Virginia community room, subtle Appalachian surroundings, natural colors/light, no real identifying records or insignia. | W4 slides1,optional2/8; video1/10 and poster. | Favor believable interaction and uncluttered space, not staged corporate handshake imagery. |
| P4-B | Older adult at modest West Virginia home workstation preparing a video call, well-fitted headset, natural daylight, laptop screen oblique/neutral and no readable generated text. | W4 slide14 inset/poster; video7. | Optional: approved workstation photo can cover context if visible person not needed. Do not depict a live identifiable participant grid. |
| P4-C | Natural close photo of ordinary full-size keyboard on table, neutral background, no logos. | W4 slide16 goods example. | Prefer crop of approved workstation photograph if resolution/composition permits; no separate generation by default. |

## Options to surface before implementation

1. **Photo budget:** recommend two new core photos P3-A/P4-A; P3-B/P4-B optional; P4-C from approved workstation crop. Most improvement comes from authored demonstrations, not a photo per slide.
2. **Software specificity:** recommend product-neutral fictional interfaces consistent with existing course. Real Word/Excel/Gmail screenshots would require explicit product/version choices and copyright/fair-use review and can age quickly.
3. **Video scope — resolved:** retain current Britt V3 cleaned narration unless a verified teaching gap requires a change. This audit found visual underrepresentation, not a demonstrated narration gap. Rebuild visuals/captions timing only as necessary; do not silently incur new narration generation or repeat the echo-cleanup work.
4. **Local setting — resolved:** use specifically West Virginia themes in fictional community/library/home scenarios: recognizable Appalachian surroundings and ordinary local spaces. Never label generated buildings/people as a real institution or actual VUB participants. Real local photography needs supplied licensed imagery and participant permission.
5. **Assessment scope:** no question/category/scoring changes needed; avoid visual hints that expose correct answers before response.

## Specific risks and acceptance checks

- `concept()` currently chooses one week-level image globally. Add a per-scene visual decision map so removing a repeated illustration does not erase a useful photo elsewhere.
- Week4 slide4 currently shows shared-document feedback instead of email composition. Fix the matching workshop assignment, not just the background image.
- The photo generation used16:9 while prior slots are3:2. Inspect crop/focal point at desktop, projector and narrow mobile; never stretch images.
- New fictional UI must remain legible, keyboard-operable and labeled as practice; no hover-only answers, color-only changes, live send/payment/media permissions, or personal records.
- Enlarge chart/formula/document artifacts by removing decorative side panels where needed. Test increased text settings, slide fit, focus/arrow navigation, reduced motion and print resources.
- Video visuals need chapter-by-chapter inspection for literal sync: paper12→15,total25→28; trial$12/month distinct from one-time checkout$12; closed comments only after decision. Keep optional captions clear of focal actions.
- Before delivery run targeted slide-scene and workshop tests, full relevant DL2 tests/build, media decode/caption/hash verification, and visual checks of changed chapters. Rebuilding photos into video may increase files beyond the current20MB allowance; optimize encoding and document any proposed limit change rather than bypass it.
- This is a source audit and plan, not a completed visual/browser or rendered-media verification of proposed changes.
