# DL2 photographic teaching-visual plan

Status: complete placement audit; implementation in progress, 21 September 2026. User approved West Virginia themes and retaining current narration except verified teaching gaps. Implementation is authorized following the placement audit; no learner pages or videos changed by this audit yet.

## Direction and boundaries

Refine the approved VUB guided-lab design across all six weeks. Use realistic generated photographs to establish a familiar task, then use authored diagrams and fictional software demonstrations to explain decisions and outcomes. Preserve the navy/gold frame, large classroom text, working navigation, accessible interactions, assessment alignment and branded results reports. This is an extension of `DESIGN.md`, not a replacement brand.

The audience is adult veterans, including older learners, using individual lab workstations. Each visual should help them recognize a situation, make a choice, observe a consequence or repeat a useful skill. Do not add imagery merely to fill space. Keep meaningful explanations and transcripts; fewer words on the visual does not mean less teaching.

## Exact placement maps

The following companion audits enumerate the existing slides and ten video chapters per week. Each entry identifies a proposed change or a deliberate keep decision:

- [Weeks 1–2](review/visual-plan-weeks-01-02.md)
- [Weeks 3–4](review/visual-plan-weeks-03-04.md)
- [Weeks 5–6](review/visual-plan-weeks-05-06.md)

## Priority corrections established by the audit

- Week 1 calendar visuals: align the event across form, views and privacy demonstration with the existing narration.
- Week 2 slide 18: demonstrate trash versus version-history recovery instead of repeating synchronization. Video chapters 4 and 9 need an actual source record and ZIP extraction sequence.
- Week 4 slide 4: replace the shared-document comment tool with an actionable-email composer.
- Week 5 video chapter 5: remove the unrelated USB from the encryption comparison.
- Week 6 video chapter 2: compare website, app and hosted service rather than HTML/CSS/JavaScript layers.
- Auditors found visual underrepresentation, but no verified narration teaching gap requiring a new take.

## Shared composition rules

1. **Scenario:** a realistic photo with one short task question, followed by an explicit transition to the working example. Use everyday homes, libraries and community learning rooms; show capable adults, not helplessness or stereotypes.
2. **Demonstration:** a large, readable fictional interface or diagram. Show the starting state, action, changed state and verification. Put instructional text in HTML/SVG, not generated pixels.
3. **Comparison:** two synchronized states with labels such as owner/partner, before/after or source/output. Do not imply a difference using color alone.
4. **Practice:** an existing accessible control or a concrete pause-and-try task. Photos do not replace working controls. Preserve keyboard behavior, visible focus, status announcements and printable explanations.
5. **Recap:** a small visual sequence of actions or the finished artifact. Avoid repeating a large decorative hero on every slide.

Photos may establish context for diagrams but must not compete with the instructional focal point. Maintain a caption-safe video band. Use restrained movement to direct attention, never arbitrary animation or automatic slide advancement.

## Initial selected candidates

- Workstation: fourth Nano Banana Pro photographic variation; cleaner screen and balanced everyday equipment.
- Safety: third photographic variation, woman comparing a phone with a laptop; clear device relationship.
- These are recommended source candidates, not yet deployed assets. Review full-resolution anatomy, cables, device geometry and crops before acceptance. Replace or cover artificial screen content with authored fictional examples wherever it is visible enough to distract or teach an incorrect cue.
- Other weeks need topic-specific scenarios; do not stretch these two images across unrelated concepts.

## Asset and production changes

- Add a small explicit visual manifest mapping week, slide/chapter, asset, crop/focal point, alt-text role and instructional purpose. Keep original prompt, generator/model, generation identifier, source, output dimensions and hash for each accepted asset.
- Generate reusable scenario sets through the connected ElevenLabs image tool using the successful photographic model. Produce a contact sheet and select for instructional clarity before integration. Record the actual estimate before a batch; generation costs and retries remain a material implementation consideration.
- Export optimized self-hosted WebP assets, retain originals outside the deployable tree, and avoid remote runtime image dependencies. Size variants for actual use. Do not bake branding or essential instructions into photos.
- Author per-slide mappings in `scripts/dl2/scenes.py` and the page-building sources; adjust `assets/slide-scenes.css` only as needed for scenario versus demonstration layouts. Use the existing `workshops.py` models rather than rebuilding working interactions.
- Change `scripts/dl2/build-media.py` from copying one `topic.webp` per week to copying the explicitly referenced chapter assets. Extend `scripts/dl2/video-scenes.py` with scenario, demonstration and comparison compositions selected per chapter.
- Preserve existing aligned Britt audio by default. Match state changes to actual narration anchors, allow time to inspect the result, and retain chapter replay and pause practice. Avoid adding arbitrary duration or mechanically slowing speech. Only a verified explanation gap should trigger script/audio/caption changes.
- Rebuild all affected videos and their matching chapter/caption metadata. The published MP4s must remain within the current 20 MB per-video limit; if photographic detail cannot remain clear within that ceiling, bring the encoding/hosting tradeoff to the user rather than silently lowering quality or raising the limit.

## Decisions to surface

1. **Regional specificity — resolved:** specifically West Virginia themes, as requested. Use fictional Appalachian homes, community learning rooms, libraries and small-town settings; depict varied capable adults. Do not imply a generated location is an actual local institution.
2. **Narration scope — resolved:** retain current narration and repair verified gaps only. A complete rerecording adds cost, timing work and new voice-quality risk without necessarily improving the visual lesson.
3. **Asset volume:** derive a deduplicated shot list from the exact maps; several slides can reuse a relevant scene with different crops. Do not order a separate generated photo for every slide or chapter.
4. **Software fidelity:** recommend readable fictional interfaces, with clear practice labeling. Real product screenshots would need provenance, version checks and a copyright-use rationale.
5. **Course shell and results:** retain their approved treatment. Limit any image synchronization to course/week entry artwork where it improves continuity; do not redesign the assessment/results experience during this pass.

## Parallel implementation sequence

With the user's regional and narration choices resolved, divide ownership to avoid agents editing shared generators simultaneously:

1. **Asset producer:** deduplicated briefs, generation, contact sheets, accepted exports and provenance. Own asset files and visual manifest only.
2. **Slide implementer:** lesson compositions, semantic overlays, exact slide mappings and responsive behavior. Own slide-specific sources and styles only.
3. **Video implementer:** chapter compositions and asset loading. Own video sources only; render after the shared manifest is stable, with bounded render concurrency.
4. **Integrator/reviewer:** this task owns shared page generation, cross-course build, browser checks, video verification and final review evidence. Schedule a separate review agent once an implementation slot is free.

Start with a representative workstation scenario, safety scenario and one procedural chapter as a vertical slice. Apply the validated pattern to all remaining mapped placements, then run one consolidated review and one correction pass. Keep the current good assets recoverable.

## Acceptance evidence

- Every one of the 137 slides and 60 chapters has a change/keep decision in the audit; final changes are traceable to those entries.
- Check scenario crops and demonstration text on desktop, mobile with enlarged text, and projector-sized video frames. Slide instructional body text remains at least 24pt/32px. No critical meaning relies on small photographed screen text.
- Run slide-scene and learning-app functional tests, keyboard navigation, image-loading checks, print checks and the existing course quality gate after implementation. Plan-only edits require no browser test rerun.
- Strict HyperFrames checks for every rebuilt week; decode every exported video, check caption coverage and chapter seek behavior, run the Sandra pacing/A/V checks, and update media hashes only after successful verification.
- Review exported frames at every scene transition and listen to representative chapter transitions; automated checks do not certify voice naturalness. Reuse audio hashes to demonstrate that a visual-only rebuild did not introduce new voice processing.
- Verify the draft deployment assets and playback. Publishing to production remains a separate release action.

## Generation estimate

Provider estimate for five new core scenes, four candidates each: 24,361.2 credits, approximately US$4.02 total. Existing selected workstation/safety candidates are reused without new generation. Optional scenes use suitable crops or authored diagrams. Actual accepted receipts belong in `photo-assets.json`.

## Implementation result

The six-week revision is implemented. Seven photos, 137 slide decisions and 60 chapter decisions are accounted for. All 78 browser tests pass; both video-specific tests pass again against the final rebuilt MP4s. All six final media verification checks pass, including full decode, captions, audio levels, fast-start and size. See `review/photographic-integration.md` for evidence and representation boundaries. Production has not been changed.
