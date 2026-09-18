# Product: VUB Digital Literacy Level 2

<!-- impeccable:product-schema 1 -->

This course-scoped record describes the built extension under `courses/digital-literacy-2/`. It does not replace platform policy or redefine the other three VUB Learning courses. Facts come from the requested course brief, repository `AGENTS.md`, curriculum, instructor guide and implementation.

## Platform

web

## Users

Adult veterans in Veterans Upward Bound, including older adults, working at individual lab computers with an instructor. Learners need practical digital confidence, time to practice, and clear explanations that respect their existing experience. Instructors need a reusable two-hour plan, demonstration material, practice tasks and answer guidance for each session.

## Product Purpose

Teach IC3 GS6 Level 2 skills in five weekly two-hour sessions, then apply those skills in a sixth two-hour session building and testing a small web app. Success means completing observable tasks, explaining decisions, preserving useful work and identifying a next practice priority.

## Positioning

This is the fourth independent course in VUB Learning and the second rung of its digital-literacy ladder. It combines guided lab work with original classroom assessments and a separate introductory AI-assisted web-app extension. It is not a Certiport examination, certification award or prediction of certification performance. Week 6 distinguishes a local browser prototype from an operated SaaS service.

## Operating Context

Each of the six plans totals 120 minutes, including a break, demonstration and hands-on practice. The sequence is technology basics; information finding and organization; usable content creation; communication and collaboration; safety and skills review; then app building with AI or the supplied manual-editing path.

The syllabus alone carries cohort dates. Presentations, worksheets, answer guides and transcripts remain reusable. Learners can open a weekly lesson, resume slide progress, practice, check understanding and use the accompanying worksheet. Instructors prepare fictional files and may provide a demonstration account for software features that require sign-in. The supplied week 6 HTML app can be edited without an AI account.

## Capabilities and Constraints

- Six presentations, each with two knowledge checks, eight worksheet tasks, an answer guide, a lesson plan, a captioned narrated video and a transcript. The built presentations contain 137 slides altogether.
- Parallel pre/post assessments each contain 28 original questions: four in each of Technology Basics, Digital Citizenship, Information Management, Content Creation, Communication, Collaboration, and Safety and Security. The week 6 project has a separate eight-point rubric.
- Client-side grading produces a total, domain breakdown and explanations for every response. Post-test growth comparison uses an optional learner-entered pre-test score; it is not a verified identity match.
- Browser Print / Save as PDF and standalone HTML results download preserve results. Printable tests and answer keys support paper delivery. Missing question data produces an explicit error and points to the printable option.
- Assessment drafts and results use `sessionStorage` in the learner's tab, with a clear-assessment control. Slide progress uses the shared `VubProgress` localStorage layer. Worksheet answers remain in the open page and are included in printing. There is no backend grading, automatic instructor submission, instructor results dashboard or durable learner-record service.
- The site is static HTML/CSS/JavaScript. It loads shared assets from root-absolute paths and must be served from the site root. No external CDN is required for course delivery. The build includes only the six hash-verified course videos allowed by the media manifest.
- Course exercises use fictional information. No paid account, personal record, API secret, payment collection or live deployment is required for the week 6 task.

## Brand Commitments

Retain VUB Learning's name, existing seal, navy-and-gold identity and established course interaction language. This is an existing-brand extension. Language is concrete, respectful and task-centred; examples connect to useful everyday technology decisions. Pricing, positioning and learner-facing policy remain outside incidental design edits.

## Evidence on Hand

`scripts/dl2/curriculum.json` records the six-week sequence, objectives, agendas, tasks and answers. The course's `instructor-guide.html`, weekly plans and `sources.html` provide teaching and source context. `assets/questions.json` and `assets/assessment.js` define the actual question bank and result behavior. The course has a working fictional resource-finder app, local media, WebVTT captions and transcripts.

`HANDOFF.md` records media provenance: Explain Video Generator was trialled separately; the initial ElevenLabs authorization error was repaired; the six delivered videos now use ElevenLabs Sarah narration and HyperFrames production. The trial is not a required learner dependency. `review/` contains captured views and print proofs; verification reports record their own scope. These artifacts do not establish live deployment or certify accessibility by themselves.

No approved design comp applies to this brand extension. No testimonials, certification claims or production-service capabilities should be invented.

## Product Principles

- Lead with a useful task and give learners immediate practice.
- Respect prior experience and make help available without forcing a single pace.
- Keep assessment categories parallel and aligned with what is taught.
- Explain where work is stored and how learners preserve or clear it.
- Test a prototype's behavior before trusting an AI-generated claim about it.

## Accessibility & Inclusion

The required standard is WCAG 2.1 AA: readable contrast, semantic controls, keyboard access, visible focus and information that does not rely on color alone. Slide body content, including knowledge-check choices, must meet the 24pt/32px floor. Learner pages include the shared text-size control. Slides do not auto-advance; keyboard and pointer controls support deliberate pacing. Flip content exposes its expanded state, reduced-motion styling removes rotation, and video offers captions and text transcripts. Print and account-free practice paths remain part of delivery.
