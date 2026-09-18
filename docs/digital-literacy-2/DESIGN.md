---
name: VUB Digital Literacy Level 2
description: An illustrated learning app and task-first workshop within the VUB course system.
colors:
  primary: "#1b365d"
  primary-hover: "#2c4a7c"
  gold: "#c9a227"
  practice-teal: "#0f655f"
  practice-surface: "#e1efed"
  selected-surface: "#dcece9"
  frame-navy: "#102c4b"
  sidebar: "#102c4b"
  sidebar-hover: "#25486c"
  navigation-current: "#2a5277"
  app-gold: "#e4b62e"
  app-ink: "#173657"
  app-line: "#cbd7e2"
  answer-selected: "#173c61"
  topic-surface: "#eaf1f7"
  workshop-canvas: "#e8eef3"
  workshop-paper: "#f7f9fb"
  discussion-surface: "#e5eff6"
  check-surface: "#eaf3f1"
  check-selected: "#163e38"
  completion-surface: "#e4efeb"
  canvas: "#f4f7fb"
  paper: "#ffffff"
  ink: "#16243a"
  muted: "#46566d"
  divider: "#b5c2cf"
  cool-surface: "#e8eff5"
typography:
  display:
    fontFamily: "Segoe UI, Tahoma, Geneva, Verdana, sans-serif"
    fontSize: "clamp(2.2rem,4vw,3.6rem)"
    fontWeight: 700
    lineHeight: 1.2
  lesson-title:
    fontFamily: "Segoe UI, Tahoma, Geneva, Verdana, sans-serif"
    fontSize: "clamp(36px,3.7vw,58px)"
    fontWeight: 700
    lineHeight: 1.12
  body:
    fontFamily: "Segoe UI, Tahoma, Geneva, Verdana, sans-serif"
    fontSize: "18px"
    lineHeight: 1.8
  slide-body:
    fontFamily: "Segoe UI, Tahoma, Geneva, Verdana, sans-serif"
    fontSize: "max(32px,var(--fs-slide,32px))"
    lineHeight: 1.6
  slide-navigation:
    fontFamily: "Segoe UI, Tahoma, Geneva, Verdana, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.35
rounded:
  navigation: "8px"
  field: "6px"
  control: "8px"
  panel: "12px"
  window: "12px"
spacing:
  compact: ".7rem"
  regular: "1rem"
  section: "2rem"
  spacious: "3rem"
components:
  button-gold:
    backgroundColor: "{colors.app-gold}"
    textColor: "{colors.frame-navy}"
    rounded: "{rounded.control}"
    padding: "12px 24px"
  button-gold-hover:
    backgroundColor: "#f2ce61"
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.paper}"
    rounded: "{rounded.control}"
    padding: ".55em 1em"
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
  button-secondary:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.primary}"
    rounded: "{rounded.control}"
    padding: ".55em 1em"
  button-secondary-hover:
    backgroundColor: "{colors.cool-surface}"
  lesson-panel:
    backgroundColor: "{colors.paper}"
    rounded: "{rounded.panel}"
    padding: "clamp(24px,3vw,48px)"
  practice-note:
    backgroundColor: "{colors.practice-surface}"
    rounded: "{rounded.control}"
    padding: "1rem 1.4rem"
  slide-navigation-current:
    backgroundColor: "{colors.navigation-current}"
    textColor: "{colors.paper}"
    rounded: "{rounded.navigation}"
    padding: "12px"
---

# Design System: VUB Digital Literacy Level 2

## Overview

**Creative North Star: "The VUB guided lab"**

The VUB guided lab now uses the user-approved modern learning-app composition: substantial object illustration, confident humanist type, persistent navy course navigation and visible progress. Put a useful working task in front of the learner, then explain why it works. Original fictional software models make cause and effect visible in an instructor-led computer lab.

The governing visual authority is the existing VUB brand, the approved combination of assessment A, B and C in `.impeccable/mocks/README.md`, the direction contract in `REDESIGN.md`, and the implemented `course.css`, `workshop.css` and final `learning-app.css` cascade. This record applies to Digital Literacy Level 2 only. It does not replace platform-wide design authority or impose this course's layout on other courses.

**Key Characteristics:**

- VUB navy navigation with a narrow gold brand line and gold-underlined current location.
- Task-first white panels beside dark, independently scrollable desktop navigation.
- Rich original laptop, computer, book and notebook illustrations with semantic HTML copy.
- Focused assessment questions, seven-topic answer counts and real browser-saved continuation.
- Familiar Segoe UI typography with an enlarged classroom slide-body scale.
- Original software models, progressively disclosed explanations and explicit outcomes.
- Lesson-kind surfaces distinguish discussion, checks, video and completion.

## Colors

The palette combines an established navy-and-gold frame with quiet reading surfaces and teal practice areas.

### Primary

- **VUB Navy:** headings, primary actions, header and revealed flip-card answers.
- **VUB Navy Hover:** a visible state change for primary controls.

### Secondary

- **Brand Gold:** the thin brand line beneath the header. **App Gold:** welcome/check-in primary actions and current-location emphasis.
- **Practice Teal:** step numbers, progress and selected-answer borders.
- **Practice Surface / Selected Surface:** hands-on notes, card fronts and selected answers.

### Neutral

- **Frame Navy:** header, code blocks and media background.
- **Sidebar / Sidebar Hover / Navigation Current:** dark course and lesson navigation, a lighter hover surface, and a distinct current-location surface with white text and a gold underline.
- **Workshop Canvas / Workshop Paper:** blue-gray lesson surroundings and the modeled software window.
- **Discussion / Check / Completion Surfaces:** cool blue discussion, pale teal knowledge checks and soft green completion. Selected check answers use dark green with white text.
- **Canvas / Paper:** page background and white reading panels.
- **Ink / Muted:** main text and supporting metadata.
- **Divider / Cool Surface:** separators, table headings and secondary hover states.

**The Visible State Rule.** Pair color with text, shape, weight or semantic state; answer feedback explicitly says “Correct” or “Try again.”

## Typography

The Segoe UI stack applies to interface, lesson and document content. It preserves the established lab-computer character and readable line shapes. This is an Operate/Read use of a system face, not a new display-font identity.

Page titles use a fluid scale; lesson titles are slightly tighter. Base reading content uses generous leading, while slide body text uses a larger classroom scale and a shorter line height. General paragraphs and list items have a maximum measure of 72 characters; direct lesson paragraphs tighten to 56 characters. Lesson headings use a compact 1.12 line height and a task-sized measure, with mobile headings at 36px. Sidebar labels are a compact navigation role, separate from instructional body content.

**The Classroom Body Rule.** Instructional slide body content and knowledge-check answer choices retain the 24pt/32px minimum as the shared text-size control enlarges them. Compact navigation, video captions and document metadata are distinct roles; their smaller values must not be reused for lesson explanations.

Printed presentations retain large lesson type. Printable worksheets, instructor material and assessment results use document sizing, with headings above a 12pt body. This print distinction is intentional; it is not a mobile-slide reduction.

The illustrated welcome headline uses a tight 1.09 line height, negative tracking and a fluid 38–58px scale (64px above 1500px; 40px on narrow screens). Assessment introductions use large compact white headings; question legends use a fluid 24–34px base and respect the shared slide-size setting. Assessment answer rows use `max(19px,var(--fs-body,18px))`; they are distinct from the 32px classroom slide answers.

## Layout

Course home, assessments and course documents share a navy course rail: 218px on desktop, 180px at 1200px and below. The home pairs a substantial illustrated welcome with a gold begin/continue action, a real progress strip, six illustrated week rows and a teal assessment companion. Document content inside the shell is capped at 1100px. At 900px and below, a semantic Course navigation button reveals the horizontal link row in normal flow; text-size controls remain beside it. At 650px and below, home art moves below its copy and support areas stack.

Assessments place seven scrollable topic buttons above a portrait illustrated introduction and a focused question. The desktop question layout uses `minmax(265px,.78fr) minmax(0,1.55fr)` columns, changing to 250px plus remaining width at 1200px. At 650px, a compact landscape illustration precedes the question. Results remove the story/topic chrome and use a wide reading area. Review-all mode exposes all question fieldsets.

Desktop lessons use a 270px sidebar and a flexible main region capped at 1600px. At 1100px and below, the sidebar narrows to 230px. It stays sticky with its own vertical scrolling so the active slide and resource links remain reachable. The lesson toolbar, progress indicator, task panel and previous/next navigation establish a consistent reading sequence. The shared text-size toolbar is moved into the toolbar in normal flow, reserving space above the lesson rather than overlaying its example.

Every weekly opening contains a usable model: zoom, source inspection, spreadsheet, feedback, suspicious-message inspection or resource search. Demonstration slides lead with the model and outcome. Native disclosure sections below expose “Read the explanation” and, on openings, “What you will learn.” Task geometry varies deliberately: calendar grids, coordinated spreadsheet cells, file relationships, document structure, comment threads and code/result pairs.

At 760px and below, the page becomes one column. A semantic menu button reveals navigation in the normal flow with a capped scrollable height; cards stack and control groups wrap. Body text keeps its classroom minimum. The desktop panel's 560px minimum height is removed on small screens.

## Elevation & Depth

Tonal separation and borders provide most structure. The final learning-app cascade removes lesson-panel shadows and top borders. Course week rows use a restrained shadow (`0 8px 22px #102c4b08`), with a slightly deeper hover shadow. Current navigation uses an inset gold underline. Generated still-life imagery provides material depth; document models retain their own contextual shadows. Window borders and tinted toolbars distinguish the modeled application from the surrounding lesson. Flip cards use perspective only to expose an answer; reduced-motion mode switches visible faces without rotation. Nothing advances automatically.

## Shapes

Controls use gently rounded corners, fields slightly tighter corners, and larger lesson/flip panels broader corners. The repeated border language uses 2px controls and panels, with 1px document/table separators. Keep the course's soft rectangular forms and readable content alignment.

## Components

### Buttons

Gold marks welcome and assessment-ready primary actions; solid navy marks task navigation and lesson actions; white with navy border marks secondary actions. Controls have a 48px minimum height, clear hover treatment and a subtle 1px pressed displacement. Visible focus uses a 4px warm-brown outline with a 4px offset; the dark header retains pale gold while lesson slide links use brown. Workshop fields use brown focus with a 3px offset. Workshop actions have a 54px minimum height and classroom-scale labels, with selected state exposed through `aria-pressed`. Disabled navigation is visibly dimmed and actually disabled.

### Fields and assessments

Inputs have white backgrounds, strong borders, explicit labels and a shared type stack. Assessment choices are native radios within fieldsets and legends. Validation focuses the first missing answer; results move focus to their heading. Results use a score, domain table and separated answer explanations. Print removes interaction controls and preserves readable results.

Focused assessments show one native-radio fieldset at a time with previous/next actions; Review all questions reveals the complete form. Topic controls show actual answered counts out of four and move to that topic’s first unanswered question. The overall meter counts real selections, not elapsed time or earned proficiency. Selected answer rows use white text on dark blue. Optional learner details remain in a native disclosure. There is no automatic advance after selecting an answer.

### Navigation

Current course and slide links use a lighter navy surface, white text, heavier weight, an inset gold underline and `aria-current` against dark navigation. The sidebar includes weekly resources as links; its scroll region is independent of the lesson. Previous/next controls, slide counter and progress bar remain consistent. Arrow keys, Page Up/Down, Home and End navigate when focus is outside interactive controls, leaving field editing and native control behavior intact.

### Lesson panels and practice notes

Panels carry one slide at a time. Task-first opening panels are white with a desktop title-and-illustration composition above the working model; discussion uses cool blue, checks use pale teal, video uses navy and completion uses soft green. Teal notes mark contextual practice. Numbered steps and explicit instructions explain what to do. Full-page print exposes explanations, all slides and both sides of flip content; workshop controls are hidden.

### Fictional software workspaces

Each model carries “Practice simulation,” a named window or task area, large controls, and an outcome announced through a status region. Calendar Week, Day, Month and List views rearrange the same fictional events; month uses a seven-column numbered grid with contained horizontal scrolling, and narrow week views retain scrollable columns. Privacy compares the owner and partner views. The spreadsheet labels columns A/B and rows 1–5, highlights B2:B4 and B5, and pairs `=SUM(B2:B4)` with an observable total change from $25 to $28.

Sync/deletion and backup recovery, heading-and-step structure, export choices, specific comments, meeting controls, message inspection and access/encryption comparisons each change their own visible model. App examples pair code with output, provide match/no-match search, and build a prompt locally from chosen requirements. No model claims to change real device settings, account access or a message, and no practice prompt is sent to an AI service.

### Flip cards and knowledge checks

Flip cards are real buttons with `aria-expanded`; the hidden face has its own accessibility state. Card fronts use a cool blue reading surface; answers use navy. Knowledge-check buttons identify the selected answer with `aria-pressed`; text feedback supports retrying. Preserve readable answer text and keyboard activation.

### Illustration and course progress

Three locally hosted generated WebP assets supply the welcome, assessment focus and practice companion. `.impeccable/asset-manifest.json` records original sources, prompts and roles. Their blank screens and pages contain no teaching text or answer clues; all meaningful headings and controls remain HTML. Mobile uses the wide welcome illustration for the compact assessment introduction. Preserve the substantial imagery and type hierarchy as the user’s saved design preference.

The home’s begin/continue action and six-lesson progress read `VubProgress`; “viewed to the end” describes navigation state, not mastery or certification. Assessment answer counts read current selections and drafts stay in sessionStorage in the learner’s tab.

### Video

Video uses the available width, a dark resting background, native controls, selectable WebVTT captions and an adjacent transcript link. Playback pauses when its slide is left. The learner chooses when to play or advance.

Implementation sources: course `assets/course.css`, `assets/workshop.css`, `assets/workshop.js`, `assets/learning-app.css`, `assets/learning-app.js`, `assets/assessment.js`, and repository `scripts/dl2/learning.py`, `scripts/dl2/workshops.py` and `scripts/dl2/build-pages.py`. Current captured examples are in `review/learning-app/`; earlier workshop captures remain in `review/redesign/`. The local quality gate passed with 60 browser tests; independent finish review returned ship. See VALIDATION.md for evidence and verification boundaries; local checks do not establish remote CI or production deployment.

## Do's and Don'ts

### Do:

- **Do** keep this system scoped to the Level 2 course extension.
- **Do** preserve the classroom body floor when adding new interactive content.
- **Do** pair state color with words or semantic state.
- **Do** maintain the same task and controls through desktop, mobile, reduced-motion and print modes.
- **Do** retain VUB identity assets and the shared text-size control.
- **Do** lead with the working task and keep its explanation available through native disclosure.
- **Do** label fictional models and show an observable outcome for each action.

### Don't:

- **Don't** add CDN dependencies or assume external fonts are available.
- **Don't** turn compact navigation typography into lesson body typography.
- **Don't** use animation as the only way to reveal an answer.
- **Don't** expand the approved Level 2 composition into a platform redesign without authorization.
- **Don't** substitute repeated title-and-list panels for the approved task-first composition.


## Illustrated lesson scenes

The lesson canvas extends the approved learning-app identity with topic imagery and worked examples. `slide-scenes.css` is loaded only by presentations. Navy example stages, teal consequences and original editorial illustrations give content slides a visual structure; discussion/lab pages use split image and text, summary/completion pages use navy, and video slides provide a dark viewing surface. Existing interactive workshops remain intact.

`scripts/dl2/scenes.py` defines 53 authored choice-based examples plus three dedicated chart, crop/resize and trim/split models. Examples use native buttons with pressed state and a single visible panel; drawings represent actual relationships or field structures, not software screenshots. Six WebP illustrations total 474,230 bytes, with provenance in `slide-illustrations.json`. Images are decorative and lazy-loaded; all teaching information remains text. Workbook cells, recipients and flow relationships use semantic HTML.

Choice controls use immediate state changes to preserve contrast. The chart's values, bar lengths, accessible name and table update together. Crop and resize are distinct reversible previews. The editing timeline labels removed sections and explains the new duration. Procedure steps can be marked practiced and undone within the page. Print reveals every topic explanation. Mobile stacks images and scenes while retaining the 32px instructional body floor and shared text controls.


## Branded results reports

Pre/post grading uses a shared branded report theme in `assets/results-report.css`. The page builder embeds its CSS and the official white seal in assessment pages; downloads reuse both without external resources. Results include learner metadata, the actual score, domain bars with numeric equivalents, up to two lowest-scoring practice domains and all answer explanations. Perfect scores receive an application task instead of invented weak areas. Existing comparison wording, grading, clearing and optional learner information are preserved.

The print layout isolates report colors/type from the shared handout and text-size overrides, reserves the first page for the summary, and avoids splitting answer sections. Samples with fictional learner data, screen captures and PDFs live in `review/results-report/`; reproduce them with `node scripts/dl2/capture-results.cjs`. The report test file covers offline branding, accessibility, scoring edge cases and mobile/print behavior. Current full suite: 73 tests.
