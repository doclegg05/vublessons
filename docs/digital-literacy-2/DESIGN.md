---
name: VUB Digital Literacy Level 2
description: A task-first visual workshop within the VUB course system.
colors:
  primary: "#1b365d"
  primary-hover: "#2c4a7c"
  gold: "#c9a227"
  practice-teal: "#0f655f"
  practice-surface: "#e1efed"
  selected-surface: "#dcece9"
  frame-navy: "#102c4b"
  sidebar: "#f8fafc"
  sidebar-hover: "#e2ebf1"
  workshop-canvas: "#e8eef3"
  workshop-paper: "#f7f9fb"
  discussion-surface: "#f6ecd6"
  check-surface: "#eaf3f1"
  check-selected: "#163e38"
  completion-surface: "#e5efe9"
  canvas: "#f5f7fa"
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
  panel: "16px"
  window: "12px"
spacing:
  compact: ".7rem"
  regular: "1rem"
  section: "2rem"
  spacious: "3rem"
components:
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
    backgroundColor: "{colors.primary}"
    textColor: "{colors.paper}"
    rounded: "{rounded.navigation}"
    padding: "12px"
---

# Design System: VUB Digital Literacy Level 2

## Overview

**Creative North Star: "The VUB guided lab"**

This name describes the existing VUB world, now expressed as the user-authorized visual workshop in `REDESIGN.md`. Put a useful working task in front of the learner, then explain why it works. Original fictional software models make cause and effect visible in an instructor-led computer lab. A light sidebar keeps the lesson location stable while the central composition follows the task.

The governing visual authority is the existing VUB brand, the direction contract in `REDESIGN.md`, and the implemented `course.css` plus `workshop.css` cascade. This record applies to Digital Literacy Level 2 only. It does not replace platform-wide design authority or impose this course's layout on other courses.

**Key Characteristics:**

- VUB navy with a narrow gold brand line and navy current-slide treatment.
- Task-first white panels beside a light, independently scrollable desktop sidebar.
- Familiar Segoe UI typography with an enlarged classroom slide-body scale.
- Original software models, progressively disclosed explanations and explicit outcomes.
- Lesson-kind surfaces distinguish discussion, checks, video and completion.

## Colors

The palette combines an established navy-and-gold frame with quiet reading surfaces and teal practice areas.

### Primary

- **VUB Navy:** headings, primary actions, header and revealed flip-card answers.
- **VUB Navy Hover:** a visible state change for primary controls.

### Secondary

- **Brand Gold:** the thin brand line beneath the header.
- **Practice Teal:** step numbers, progress and selected-answer borders.
- **Practice Surface / Selected Surface:** hands-on notes, card fronts and selected answers.

### Neutral

- **Frame Navy:** header, code blocks and media background.
- **Sidebar / Sidebar Hover:** light navigation surface and quiet hover state; the current slide uses VUB Navy with white text.
- **Workshop Canvas / Workshop Paper:** blue-gray lesson surroundings and the modeled software window.
- **Discussion / Check / Completion Surfaces:** warm sand discussion, pale teal knowledge checks and soft green completion. Selected check answers use dark green with white text.
- **Canvas / Paper:** page background and white reading panels.
- **Ink / Muted:** main text and supporting metadata.
- **Divider / Cool Surface:** separators, table headings and secondary hover states.

**The Visible State Rule.** Pair color with text, shape, weight or semantic state; answer feedback explicitly says “Correct” or “Try again.”

## Typography

The Segoe UI stack applies to interface, lesson and document content. It preserves the established lab-computer character and readable line shapes. This is an Operate/Read use of a system face, not a new display-font identity.

Page titles use a fluid scale; lesson titles are slightly tighter. Base reading content uses generous leading, while slide body text uses a larger classroom scale and a shorter line height. General paragraphs and list items have a maximum measure of 72 characters; direct lesson paragraphs tighten to 56 characters. Lesson headings use a compact 1.12 line height and a task-sized measure, with mobile headings at 36px. Sidebar labels are a compact navigation role, separate from instructional body content.

**The Classroom Body Rule.** Instructional slide body content and knowledge-check answer choices retain the 24pt/32px minimum as the shared text-size control enlarges them. Compact navigation, video captions and document metadata are distinct roles; their smaller values must not be reused for lesson explanations.

Printed presentations retain large lesson type. Printable worksheets, instructor material and assessment results use document sizing, with headings above a 12pt body. This print distinction is intentional; it is not a mobile-slide reduction.

## Layout

Course and document pages use a centred container capped at 1120px. The landing introduction pairs a text column and a six-week route map; weekly resources are separated by rows rather than arranged as interchangeable dashboard tiles.

Desktop lessons use a 270px sidebar and a flexible main region capped at 1600px. At 1100px and below, the sidebar narrows to 230px. It stays sticky with its own vertical scrolling so the active slide and resource links remain reachable. The lesson toolbar, progress indicator, task panel and previous/next navigation establish a consistent reading sequence. The shared text-size toolbar is moved into the toolbar in normal flow, reserving space above the lesson rather than overlaying its example.

Every weekly opening contains a usable model: zoom, source inspection, spreadsheet, feedback, suspicious-message inspection or resource search. Demonstration slides lead with the model and outcome. Native disclosure sections below expose “Read the explanation” and, on openings, “What you will learn.” Task geometry varies deliberately: calendar grids, coordinated spreadsheet cells, file relationships, document structure, comment threads and code/result pairs.

At 760px and below, the page becomes one column. A semantic menu button reveals navigation in the normal flow with a capped scrollable height; cards stack and control groups wrap. Body text keeps its classroom minimum. The desktop panel's 560px minimum height is removed on small screens.

## Elevation & Depth

Tonal separation and borders provide most structure. Lesson panels use a restrained ambient shadow (`0 12px 32px #16334b0c`); selected navigation and document models carry smaller contextual shadows. Window borders and tinted toolbars distinguish the modeled application from the surrounding lesson. Flip cards use perspective only to expose an answer; reduced-motion mode switches visible faces without rotation. Nothing advances automatically.

## Shapes

Controls use gently rounded corners, fields slightly tighter corners, and larger lesson/flip panels broader corners. The repeated border language uses 2px controls and panels, with 1px document/table separators. Keep the course's soft rectangular forms and readable content alignment.

## Components

### Buttons

Solid navy marks primary actions; white with navy border marks secondary actions. Controls have a 48px minimum height, clear hover treatment and a subtle 1px pressed displacement. Visible focus uses a 4px warm-brown outline with a 4px offset; the dark header retains pale gold while lesson slide links use brown. Workshop fields use brown focus with a 3px offset. Workshop actions have a 54px minimum height and classroom-scale labels, with selected state exposed through `aria-pressed`. Disabled navigation is visibly dimmed and actually disabled.

### Fields and assessments

Inputs have white backgrounds, strong borders, explicit labels and a shared type stack. Assessment choices are native radios within fieldsets and legends. Validation focuses the first missing answer; results move focus to their heading. Results use a score, domain table and separated answer explanations. Print removes interaction controls and preserves readable results.

### Navigation

Current slide links use a navy surface, white text, heavier weight, a small shadow and `aria-current` against the light sidebar. The sidebar includes weekly resources as links; its scroll region is independent of the lesson. Previous/next controls, slide counter and progress bar remain consistent. Arrow keys, Page Up/Down, Home and End navigate when focus is outside interactive controls, leaving field editing and native control behavior intact.

### Lesson panels and practice notes

Panels carry one slide at a time. Task-first opening panels are white with a navy top edge; discussion uses sand, checks use pale teal, video uses navy and completion uses soft green. Teal notes mark contextual practice. Numbered steps and explicit instructions explain what to do. Full-page print exposes explanations, all slides and both sides of flip content; workshop controls are hidden.

### Fictional software workspaces

Each model carries “Practice simulation,” a named window or task area, large controls, and an outcome announced through a status region. Calendar Week, Day, Month and List views rearrange the same fictional events; month uses a seven-column numbered grid with contained horizontal scrolling, and narrow week views retain scrollable columns. Privacy compares the owner and partner views. The spreadsheet labels columns A/B and rows 1–5, highlights B2:B4 and B5, and pairs `=SUM(B2:B4)` with an observable total change from $25 to $28.

Sync/deletion and backup recovery, heading-and-step structure, export choices, specific comments, meeting controls, message inspection and access/encryption comparisons each change their own visible model. App examples pair code with output, provide match/no-match search, and build a prompt locally from chosen requirements. No model claims to change real device settings, account access or a message, and no practice prompt is sent to an AI service.

### Flip cards and knowledge checks

Flip cards are real buttons with `aria-expanded`; the hidden face has its own accessibility state. Card fronts use a cool blue reading surface; answers use navy. Knowledge-check buttons identify the selected answer with `aria-pressed`; text feedback supports retrying. Preserve readable answer text and keyboard activation.

### Video

Video uses the available width, a dark resting background, native controls, selectable WebVTT captions and an adjacent transcript link. Playback pauses when its slide is left. The learner chooses when to play or advance.

Implementation sources: `assets/course.css`, `assets/workshop.css`, `assets/workshop.js`, `scripts/dl2/workshops.py` and `scripts/dl2/build-pages.py`. Captured examples are in `review/redesign/`; this documentation records implementation and direction, not a completed accessibility, CI or finish-review certification.

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
- **Don't** infer a platform redesign or approved comp from this course-scoped record.
- **Don't** substitute repeated title-and-list panels for the approved task-first composition.
