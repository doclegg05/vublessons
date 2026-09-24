# Photographic slide implementation review

21 September 2026. Source changes regenerated with `python3 scripts/dl2/build-pages.py` and built with `npm run build:site` (193 published HTML pages).

Targeted verification: `npx playwright test tests/functional/dl2-slide-scenes.spec.js tests/functional/dl2-learning-app.spec.js --workers=2` — **15 passed** in the final run. Tests exercise all six weeks' authored scene choices with keyboard activation, enlarged mobile text, relevant accessibility scans, preserved assessment state, the new email draft and recovery branch, charts, crop/resize, editing timeline and printable explanations.

Visual review used one desktop/mobile capture batch, followed by one correction/confirmation batch. Seven representative surfaces cover all six weeks: print preview, recovery, three-slide storyboard, email composer, safety scenario, comfort hotspots and data boundaries. All fourteen captures have no document horizontal overflow. The safety photo's authored phone/laptop masks cover the generated lettering in both layouts. Desktop and mobile screenshots were visually inspected, including the three corrected print/comfort captures in the confirmation pass.

Corrections from the review:
- Print preview states now change the selected setting and a concrete check instruction; they no longer differ only by color/outline. Added a paper/print-area diagram instead of showing every setting as a long table.
- Removed the duplicated comfort-control row; numbered photo controls remain keyboard accessible and move below the image on narrow screens.
- Standalone instructional fields now explicitly use the 32px slide-body minimum.

The page model is vertically scrollable, including on desktop. Long mobile slides preserve large readable text rather than compressing it into a single screen. This is not evidence of classroom projector/speaker evaluation or complete-course test coverage; the integrator owns the broader release gate and video verification.

`measurements.json` records viewport-specific overflow and slide height. Capture utility: `scripts/dl2/capture-photo-slides.cjs` (expects a local server on port3939).

Independent review follow-up: week3 slide9's illustrated supply values previously stayed at the initial values when the live paper-cost input changed. Replaced the static sequence with a semantic B2–B5 worksheet table driven by the existing input calculation. Input15 now yields paper15/total28 in both views; input0 yields paper0/total13; empty/invalid input removes misleading numbers. The regression covers15,0,12 and empty. Regenerated/built193pages; the final targeted suite now reports **16 passed**.
