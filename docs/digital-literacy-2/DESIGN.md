---
name: VUB Digital Literacy Level 2
description: An extension of the VUB course system for readable lessons and practical lab work.
colors:
  primary: "#1b365d"
  primary-hover: "#2c4a7c"
  gold: "#c9a227"
  active-gold: "#e5ca74"
  practice-teal: "#0f655f"
  practice-surface: "#e1efed"
  selected-surface: "#dcece9"
  sidebar: "#102c4b"
  sidebar-hover: "#25476b"
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
    fontSize: "clamp(2rem,3.2vw,3rem)"
    fontWeight: 700
    lineHeight: 1.2
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
  navigation: "5px"
  field: "6px"
  control: "8px"
  panel: "12px"
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
    padding: "clamp(1.3rem,3vw,3rem)"
  practice-note:
    backgroundColor: "{colors.practice-surface}"
    rounded: "{rounded.control}"
    padding: "1rem 1.4rem"
  slide-navigation-current:
    backgroundColor: "{colors.active-gold}"
    textColor: "{colors.sidebar}"
    rounded: "{rounded.navigation}"
    padding: ".65rem"
---

# Design System: VUB Digital Literacy Level 2

## Overview

**Creative North Star: "The VUB guided lab"**

This name describes the incumbent course extension rather than a newly approved visual identity. The surface serves learners reading and operating software in an instructor-led computer lab. A light lesson canvas carries substantial readable text; persistent dark navigation gives the lesson a stable location; teal surfaces identify practice and explanation.

The governing visual authority is the existing VUB brand and the implemented course CSS, not a separate approved comp. This record applies to Digital Literacy Level 2 only. It does not replace platform-wide design authority or impose this course's layout on other courses.

**Key Characteristics:**

- VUB navy with a narrow gold brand line and gold current-slide treatment.
- White reading panels beside a dark, independently scrollable desktop sidebar.
- Familiar Segoe UI typography with an enlarged classroom slide-body scale.
- Teal practice surfaces, explicit feedback and learner-controlled interactions.

## Colors

The palette combines an established navy-and-gold frame with quiet reading surfaces and teal practice areas.

### Primary

- **VUB Navy:** headings, primary actions, header and revealed flip-card answers.
- **VUB Navy Hover:** a visible state change for primary controls.

### Secondary

- **Brand Gold:** the thin brand line beneath the header.
- **Active Gold:** the current slide in the dark sidebar; bold text and `aria-current` also identify this state.
- **Practice Teal:** step numbers, progress and selected-answer borders.
- **Practice Surface / Selected Surface:** hands-on notes, card fronts and selected answers.

### Neutral

- **Sidebar Navy:** the lesson navigation, code blocks and media background.
- **Canvas / Paper:** page background and white reading panels.
- **Ink / Muted:** main text and supporting metadata.
- **Divider / Cool Surface:** separators, table headings and secondary hover states.

**The Visible State Rule.** Pair color with text, shape, weight or semantic state; answer feedback explicitly says “Correct” or “Try again.”

## Typography

The Segoe UI stack applies to interface, lesson and document content. It preserves the established lab-computer character and readable line shapes. This is an Operate/Read use of a system face, not a new display-font identity.

Page titles use a fluid scale; lesson titles are slightly tighter. Base reading content uses generous leading, while slide body text uses a larger classroom scale and a shorter line height. Paragraphs and list items have a maximum measure of 72 characters. Sidebar labels are a compact navigation role, separate from instructional body content.

**The Classroom Body Rule.** Instructional slide body content and knowledge-check answer choices retain the 24pt/32px minimum as the shared text-size control enlarges them. Compact navigation, video captions and document metadata are distinct roles; their smaller values must not be reused for lesson explanations.

Printed presentations retain large lesson type. Printable worksheets, instructor material and assessment results use document sizing, with headings above a 12pt body. This print distinction is intentional; it is not a mobile-slide reduction.

## Layout

Course and document pages use a centred container capped at 1120px. The landing introduction pairs a text column and a six-week route map; weekly resources are separated by rows rather than arranged as interchangeable dashboard tiles.

Desktop lessons use a 300px sidebar and a flexible main region. At 1000px and below, the sidebar narrows to 250px. It stays sticky with its own vertical scrolling so the active slide and resource links remain reachable. The lesson toolbar, progress indicator, white lesson panel and previous/next navigation establish a consistent reading sequence.

At 760px and below, the page becomes one column. A semantic menu button reveals navigation in the normal flow with a capped scrollable height; cards stack and control groups wrap. Body text keeps its classroom minimum. The desktop panel's 520px minimum height is removed on small screens.

## Elevation & Depth

Tonal separation and borders provide most structure. Lesson panels alone use a restrained ambient shadow (`0 8px 28px #102c4b0e`). Cards and inputs rely on borders rather than floating depth. Flip cards use perspective only to expose an answer; reduced-motion mode switches visible faces without rotation. Nothing advances automatically.

## Shapes

Controls use gently rounded corners, fields slightly tighter corners, and larger lesson/flip panels broader corners. The repeated border language uses 2px controls and panels, with 1px document/table separators. Keep the course's soft rectangular forms and readable content alignment.

## Components

### Buttons

Solid navy marks primary actions; white with navy border marks secondary actions. Controls have a 48px minimum height, clear hover treatment and a subtle 1px pressed displacement. Visible focus uses a 4px warm-brown outline with a 4px offset; the dark header and sidebar use a pale-gold outline. Disabled navigation is visibly dimmed and actually disabled.

### Fields and assessments

Inputs have white backgrounds, strong borders, explicit labels and a shared type stack. Assessment choices are native radios within fieldsets and legends. Validation focuses the first missing answer; results move focus to their heading. Results use a score, domain table and separated answer explanations. Print removes interaction controls and preserves readable results.

### Navigation

Current slide links use the active-gold surface and heavier text. The sidebar includes weekly resources as links; its scroll region is independent of the lesson. Previous/next controls, slide counter and progress bar remain consistent. Arrow keys, Page Up/Down, Home and End navigate when focus is outside interactive controls, leaving field editing and native control behavior intact.

### Lesson panels and practice notes

White panels carry one slide at a time. Teal notes mark contextual practice; numbered steps and explicit instructions explain what to do. Full-page print shows all slides and both sides of flip content.

### Flip cards and knowledge checks

Flip cards are real buttons with `aria-expanded`; the hidden face has its own accessibility state. Card fronts use the practice surface, answers use navy. Knowledge-check buttons identify the selected answer with `aria-pressed`; text feedback supports retrying. Preserve readable answer text and keyboard activation.

### Video

Video uses the available width, a dark resting background, native controls, selectable WebVTT captions and an adjacent transcript link. Playback pauses when its slide is left. The learner chooses when to play or advance.

## Do's and Don'ts

### Do:

- **Do** keep this system scoped to the Level 2 course extension.
- **Do** preserve the classroom body floor when adding new interactive content.
- **Do** pair state color with words or semantic state.
- **Do** maintain the same task and controls through desktop, mobile, reduced-motion and print modes.
- **Do** retain VUB identity assets and the shared text-size control.

### Don't:

- **Don't** add CDN dependencies or assume external fonts are available.
- **Don't** turn compact navigation typography into lesson body typography.
- **Don't** use animation as the only way to reveal an answer.
- **Don't** infer a platform redesign or approved comp from this course-scoped record.
