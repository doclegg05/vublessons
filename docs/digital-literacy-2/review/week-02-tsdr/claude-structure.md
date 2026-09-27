# Week 2 structure and content review (Tell, Show, Do, Review + WIPPEA + adult learning) — Claude

Scope: Digital Literacy Level 2, week 2 "Find, judge, and organize information", class Monday 2026-10-05. Reviewed read-only against `vublessons` `main` at 9270815 (includes the week 1 Tell, Show, Do, Review change). No repo file was changed.

Conventions:
- Slide numbers are as learners see them (slide 1 = title, 23 slides; checked on the live deck).
- Lesson-plan minutes come from `weeks/week-02/lesson-plan.html` (generated from `scripts/dl2/author-content.py` week 2 `agenda`).
- Video times are m:ss in `media/week-02.mp4` (7:12). Chapter starts: ch1 0:00, ch2 0:44, ch3 1:24, ch4 2:09, ch5 2:47, ch6 3:31, ch7 4:14, ch8 5:06, ch9 5:49, ch10 6:31.
- Pause points were re-measured from `narration/beat-NN.words.json` plus the beat start: 1:16.6 (ch2, 0.00 s gap), 3:29.1 (ch5, ch6 starts 1.7 s later), 5:01.8 (ch7, answer 0.90 s later), 6:34.8 (ch10, 0.42 s gap). One more instruction ends at 5:47.6 (ch8, ch9 starts 1.5 s later).
- 56 frames were extracted (48 full frames and 8 caption strips): chapter starts and middles, all 12 screen-share actions (ch6 and ch7), and the ch9 caption changes. Each was inspected. They are in `scratchpad/video-eval/w2frames-claude/`.
- Live checks (read-only): the week 2 deck on vublessons.com (practice-form validation message), a Bing results page and a Google results page for "public library computer help" (filter controls and AI summaries).

## Verdict

**Monday 2026-10-05 is teachable. Week 2 is not yet a Tell, Show, Do, Review lesson.** The search half is close to a cycle. The files half is a lecture that cannot fit its time, followed by a lab that mostly asks learners to explain. The technical content is correct. No task is impossible.

**Strengths**
- A real, respectful problem: help a neighbor find computer help, then keep a usable record (slide 2; ch1).
- Good low-risk practice: the practice form (slide 10), the sync simulation (slide 13) and the permission simulator (slide 15) all work without accounts and say "nothing is sent".
- Two strong screen demonstrations: ch6 (new folder → name → save → reopen) and ch7 (Viewer, Commenter, Editor → save → partner view).
- The source-evaluation content is sound and current: "Do not count votes between websites; identify which source is in a position to know" (ch3).
- Week 3 opens with "Review last week's source trail and folder choices", which is the follow-up WIPPEA wants.

**Problems**
- **Big blocks, not cycles.**
  - 60–80 "Files demonstration" must cover 10 slides (9–18) and "Play the cloud-file explainer", a 7:12 video. After the video that leaves about 1.3 minutes per slide.
  - The video plays at 60–80. Chapters 2–4 show search and source checks 30–50 minutes after learners already did them at 30–50. The plan's label "cloud-file explainer" hides this.
  - Both knowledge checks wait until 110–120. Slide 19 (sources) comes 60+ minutes after the source work.
- **Warm-up ignores Level 1.** DL1 week 2 taught smart searching, ads versus real results and keeping sources. DL1 week 3 taught file naming, saving and 3-2-1 backup. Week 2 re-teaches all of these without mentioning it.
- **The files half is mostly Tell.** Task 8 asks learners to explain version history, the Recycle Bin, backup, ZIP and read-only in writing. Yet making a ZIP, extracting it and restoring a file from the Recycle Bin can all be done on a lab PC with no account.
- **No real click paths.** No slide, plan or video shows the real Edge search filters, File Explorer, Save As, ZIP, the Recycle Bin, Word's Protect Document menu or a real Share box.
- **Practice is shared.** The plan template says "Pair a driver and coach, then switch", so each learner does about half the tasks.
- **Evaluation is thin.** Ten minutes to "justify a source and a permission" for every learner plus two knowledge checks. Slide 19 has a throwaway option ("Count the page's colors").

**Correctness:** 0 High, 4 Medium, 9 Low. The Medium items:
- The plan's prep promises "instructor-provided fictional accounts" that do not exist, and names apps the week does not use.
- The one practice file has four different names across slides, simulations and video, in a lesson about naming files.
- The slides never mention the AI summary that now sits at the top of Google and Bing results.
- Version history only works for files in OneDrive, SharePoint or Google Docs. The slides do not say so, and the lab has no such account.

**For Monday:** use the revised running order below: six short cycles, each chapter played as the Show for its own slide, every learner doing each task at their own seat. Make tasks 6 and 8 hands-on in File Explorer (folder, ZIP, Recycle Bin). Run sharing and version history on slides 15 and 18, marked simulated. Use one file name: library-help-v1.docx.

## WIPPEA map

| Stage | Where it happens | Rating | Evidence | What to change |
|:--|:--|:--|:--|:--|
| **W — Warm-up** | 0–10 "Reconnect: Ask learners to demonstrate last week's check-one-change routine." | **Adequate** | <ul><li>Good follow-up of week 1, which set a home task to share "at the start of week 2".</li><li>Nothing recalls Level 1: DL1 week 2 "Define a search need and judge relevant vs. irrelevant results", "Collect and retain source references"; DL1 week 3 "Apply file naming & organization conventions", "Save and back up work (the 3-2-1 idea)" (`digital-literacy-1/weeks/week-02` and `week-03/syllabus.html`).</li><li>Nothing points toward today's topic.</li></ul> | <ul><li>Pairs share the week 1 home task (3 min).</li><li>Two recall questions: "What made a search clear in Level 1?" and "Where did you save your Level 1 document, and what did you call it?"</li></ul> |
| **I — Introduction** | Slides 1–2; ch1 (0:00–0:44) not scheduled | **Adequate** | <ul><li>Objectives are shown in writing with the Source / Folder / Access organiser.</li><li>Slide 2 and ch1 link the lesson to a neighbor's real need.</li><li>The three objectives are not measurable, and they hide five separate skills (forms, compression, read-only, sync, recovery).</li></ul> | <ul><li>State five plain goals and ABCD outcomes.</li><li>Play ch1 (44 s) as the bridge; learners write task 1.</li></ul> |
| **P — Presentation** | 10–30 "Search demonstration" (slides 3–8); 60–80 "Files demonstration" (slides 9–18 and the whole video) | **Adequate** content, **Weak** pacing | <ul><li>Many modes: 14 slides have simulations, scenes or flip cards; captions and a transcript.</li><li>60–80 holds 10 slides plus a 7:12 video.</li><li>Undefined at first use: domain and site: (slide 4), retention (slide 12), key (slide 16), coauthor (task 7), validation message (task 5).</li><li>No planned check of understanding in either block.</li><li>Slides 21–23 are named in no phase.</li></ul> | <ul><li>One skill group per cycle; play each chapter with its slide.</li><li>End each cycle with a Review.</li></ul> |
| **P — Practice** | 30–50 "Research lab" (tasks 1–4); 80–110 "Files lab" (tasks 5–8) | **Weak** | <ul><li>No instructor modelling in the real browser or File Explorer is planned.</li><li>Tasks 1–4 follow the search Tell within 20 minutes: the best-placed practice in the week.</li><li>Task 5 is 20–50 minutes after slides 9–10.</li><li>Task 6 names no app, location or file ("Create a folder and clear filename"). The prep says fictional files will be supplied; none exist (IR review).</li><li>Task 8 is explain-only, in two long written answers.</li><li>"Pair a driver and coach, then switch" (plan template).</li></ul> | <ul><li>Every learner does each task at their own seat right after its Show.</li><li>Tasks 6 and 8 become real File Explorer work: folder, save, reopen, ZIP, extract, Recycle Bin.</li></ul> |
| **E — Evaluation** | 110–120: "Ask each learner to justify a source and a permission. Use the knowledge checks." Slides 19–20; answer guide; pre/post 3.1, 3.2, 3.3 | **Weak** | <ul><li>Two knowledge checks cover sources (3.2) and read-only (4.2.4 / 7.4.2). Nothing in class checks forms, folders, compression or recovery.</li><li>Slide 19 options: "Trust the first result", "Count the page's colors", "Verify it with the responsible organization". The middle one is not a believable mistake.</li><li>About 50 seconds per learner for 12 learners, after the two checks.</li><li>The pre/post tests have no item for 4.2 or 7.4 (AS-10), so file work is judged only by the worksheet.</li></ul> | <ul><li>Slide 19 after cycle B; slide 20 after cycle E.</li><li>A final 3-item individual check with a roster.</li></ul> |
| **A — Application** | Slides 21–23; ch10 "For your next independent task, reuse this sequence…"; week 3 "Retrieve: Review last week's source trail and folder choices." | **Adequate** | <ul><li>Good transfer language in ch10; week 3 follows up.</li><li>No home task. Nothing asks learners to use the routine on their own device or for their own need.</li></ul> | Home task: "Search for one service you need, write the five-field source note, and keep it in a named folder or on paper. Bring it to week 3." |

**Overall flow.** The order is W → P (search, 20) → Practice (search, 20) → break → P (files and the whole video, 20) → Practice (files, 30) → E (10). A is not scheduled.
- The search half is nearly one cycle, but its Show (ch2–4) plays at 60–80, after the Do. The Review (slide 19) is at 110–120.
- The files half presents eight skills (forms, naming, storage, sync, sharing, protection, compression, recovery) before any practice, and checks one of them.
- The video belongs chapter by chapter inside each cycle as the Show, not as one block labelled "cloud-file explainer".

## Tell, Show, Do, Review by skill

| Skill | Tell (where) | Show (where) | Do (where; minutes available) | Review (where) | Missing or weak steps |
|:--|:--|:--|:--|:--|:--|
| Search keywords | Slide 3; ch2 0:44–1:24 | Slide 3 simulation (help → service → your town); ch2 diagram | Task 2 at 30–50 (about 5 min) | Answer guide 2; pre/post 3.1 | ch2 plays at 60–80, after the Do. ch2's search box shows "computer help + library + town" (frames 0:50–1:06). No live search. |
| Filters (quotes, site:, date) | Slide 4 | Slide 4 scene ("site:example.org computer help") | Task 2 "one refinement or filter" | Answer guide 2 | No real filter shown. Where the date filter lives (Google: Tools › Any time) is never said. example.org returns nothing useful. |
| Judge a source (accuracy, perspective, bias, credibility, relevance) | Slides 5, 7; ch3 1:24–2:09 | Slide 5 simulation; slide 6 flip cards; slide 7 scene; ch3 two cards ("Directory lead" vs "Responsible source") | Task 4 at 30–50 | Slide 19 at 110–120; pre/post 3.2 (two each) | Review 60+ minutes late. The AI summary at the top of real results is never mentioned. |
| Source trail | Slide 8; ch4 2:09–2:47 | Slide 8 scene; ch4 "My source record" (five fields, frames 2:15–2:40) | Task 3 at 30–50 | Answer guide 3 | Copying the web address is never shown. ch4 is the fastest chapter (181 wpm, VM-02). |
| Online forms | Slide 9; ch5 2:47–3:31 | Slide 10 practice form; ch5 "Practice request" card (matches slide 10's options) | Task 5 at 80–110 | Answer guide 5; pre/post 3.3 | The Do is 20–50 min after the Tell. "Record a validation message" never says how to see one. |
| Folders and file names | Slide 11; ch6 3:31–4:14 | **ch6 screen demo** (7 steps: New folder → Community resources → library-help-draft.txt → Save → "Saved locally • not yet on another device" → reopen). Simulated "Practice Files" window, not File Explorer. | Task 6 at 80–110 (no app, location or file named) | Answer guide 6 | No live File Explorer. Four names for the one file (see Content correctness, row 2). |
| Central storage and ownership | Slide 12; ch6 narration | Slide 12 scene | Task 6 part 2 (describe) | Answer guide 6 | Tell only, which is enough for 3.3.2 and 4.2.3 ("explain"). "Retention" undefined. |
| Sharing roles | Slide 15; ch7 4:14–5:06 | Slide 15 simulator and preview; **ch7 screen demo** (Viewer / Commenter / Editor → Save access → "Comment available · Direct editing unavailable") | Task 7 at 80–110 (simulator) | 110–120 "justify a permission" | ch7 plays 20–50 min before the Do. Its prompt (5:01.8) is answered 0.90 s later. |
| Read-only, encryption, passwords | Slide 16; ch7 4:47 (narration only) | Slide 16 scene | Task 8 (explain) | Slide 20 at 110–120 | No Show of Word's File › Info › Protect Document. GS6 4.2.5 "Implement password protection" is explained only. |
| Sync versus backup | Slide 13; ch8 5:06–5:49 | Slide 13 simulation (delete travels to both; restore from backup); ch8 diagram | Task 8 (explain) | Answer guide 8 | Adequate: the simulation is a good account-free Show and Do. ch8's arrow runs one way only. |
| Compression (ZIP) | Slide 17; ch9 6:09–6:29 | Slide 17 scene; ch9 diagram | Task 8 ("Explain why ZIP … do not prove encryption") | Answer guide 8 | No Show or Do, although Send to › Compressed (zipped) folder and Extract All need no account. |
| Recovery (Recycle Bin, version history) | Slide 18; ch9 5:49–6:09 | Slide 18 scene (trash preview, version history, recovery result) | Task 8 (explain) | Answer guide 8 | Restoring from the Recycle Bin is account-free but never shown or done. Version history needs a cloud account and is not labelled simulated. |

**Week 2 runs as two lecture-then-lab blocks.** Search is taught and practised within 40 minutes, which is better than week 1. The files half is not:
- Eight skills are told in one 20-minute block, together with the whole video.
- The two best Shows (ch6, ch7) play 20–50 minutes before their Do.
- Compression and recovery have Tell only, and the Do is a written explanation.
- Everything is checked together in the last 10 minutes.

For older learners this means holding eight procedures for up to 50 minutes before trying them. It also means mistakes surface only in the lab, when the instructor can no longer re-model for the whole room.

## Objectives

GS6 Level 2 groups claimed: 3.1, 3.2, 3.3, 4.2, 4.3.1, 7.4.

**1. "Refine a search and justify a source choice."**
- **ABCD rewrite:** In Edge on a lab workstation, given a local service need, each learner:
  - writes a search naming the service, provider and place, and applies one refinement (quotation marks, site: or a date range), saying what it changed;
  - records the five source fields for one result (title, organization, web address, date checked, detail used);
  - answers the five source questions for it and names one detail to confirm with the responsible organization.

  Degree: all five fields present; each judgment tied to something on the page.
- **Taught:** slides 3–8; video ch2–4. **Practised:** tasks 1–4. **Evaluated:** slide 19; pre/post 3.1 and 3.2.
- **Status:** Met in content, but the Show and Review are out of order. "Justify" is not defined by a checklist.

**2. "Complete a fictional online form and check its confirmation."**
- **ABCD rewrite:** Using the practice form on slide 10 with fictional details, each learner submits once with a required choice missing, reads the message, completes the form, and explains that the confirmation does not mean a real request was sent.
- **Taught:** slides 9–10; ch5. **Practised:** task 5. **Evaluated:** answer guide; pre/post 3.3.
- **Status:** Met, once the task says how to see the validation message.

**3. "Organize files, set access and explain a recovery path."**
- This objective bundles five GS6 sub-objectives: 4.2.1 organize, 4.2.2 compress, 4.2.4 read-only, 4.2.6 versions, 7.4 file security. Three of them are hidden inside "set access" and "recovery".
- **ABCD rewrite (split in two):**
  - **Files:** in File Explorer on a lab workstation, each learner makes a folder named Community resources, saves a Word file in it as library-help-v1.docx, reopens it from that folder, compresses the folder to a ZIP file, extracts it and opens the extracted copy. Degree: all steps done; nothing saved elsewhere by mistake.
  - **Access and recovery:** using the permission practice on slide 15 (simulated), each learner picks Viewer, Commenter or Editor for a reader, a reviewer and a co-writer with the least access each needs. They restore a deleted practice file from the Recycle Bin and say when version history is the right tool instead. They say what read-only does and does not do. Degree: all correct with no more than one prompt.
- **Taught:** slides 11–18; ch6–9. **Practised:** tasks 6–8, with task 8 explain-only. **Evaluated:** slide 20 only.
- **Status:** Partly met. Organizing, compression and recovery have no in-class performance check.

**Coverage notes.**
- 4.2.5 "Implement password protection" is explained only. A projector-only Show of Word's Encrypt with Password on a fictional file is the account-free minimum.
- 4.3.1 (rights in sharing intellectual property) is touched only by slide 8's "Separate a direct quotation from your own summary".
- 4.2 and 7.4 have no pre/post item (AS-10, confirmed).

**Backward design.** The "Evidence to collect" list copies the worksheet. It was not designed first. Two of the week's biggest skill groups (organizing and recovery) have no in-class check.

## Adult learning principles

| Principle | Rating | Evidence | Improvement |
|:--|:--|:--|:--|
| 1. Need to know | Adequate | <ul><li>Strong in the search half: "Imagine a neighbor asks where they can get help using a computer" (ch1); slide 2.</li><li>The files half is subject-centred. Slides 12, 13 and 17 say what sync, central storage and ZIP are, not why a learner would care.</li></ul> | Open each files cycle with a one-line problem: "You saved it, but where?"; "Twelve photos to send to a relative"; "A relative should read your notes, not change them"; "You deleted the wrong file". |
| 2. Self-concept | Adequate | <ul><li>Fictional data, local simulations and "nothing is sent" labels respect learners and remove fear.</li><li>"Count the page's colors" (slide 19) talks down to capable adults.</li><li>Driver/coach switching means half the time each learner watches.</li></ul> | Believable wrong answers; each learner drives their own workstation. |
| 3. Experience | **Weak** | <ul><li>ch1 invites learners to start from a library or veterans' organization they know: good.</li><li>DL1 already taught smart search, ads versus results, keeping sources, file naming and backup. Week 2 never says so.</li></ul> | Warm-up recall of DL1; before each Show ask "What do you do now?" (for example, "Where do your downloaded files go?"). |
| 4. Readiness | Adequate | <ul><li>Finding local help, keeping a record, and not losing files are needs these learners have now.</li><li>Sharing and version history assume an account; many learners have Gmail (Google Drive) or Outlook.com (OneDrive) at home, but the lesson never names them.</li></ul> | Name the real services: "If you have Gmail, this is Google Drive's Share box." Home task on the learner's own device. |
| 5. Orientation (problem-centred) | Adequate | <ul><li>Search, sources and forms are task-framed.</li><li>Titles such as "Compression packages files" and "Central storage needs clear access" are subject-centred.</li></ul> | Frame cycles D–F as problems (see principle 1). |
| 6. Motivation | Adequate | <ul><li>A clear routine (Source, Folder, Access) and "Mark practiced" buttons (slide 5).</li><li>Success in the files half is delayed to the last 40 minutes and is mostly written.</li></ul> | A visible "I did it" after every cycle: a folder that reopens, a ZIP that extracts, a file back from the Recycle Bin. |

## Content correctness

| # | Where | What it says | What is correct (source) | Severity |
|:--|:--|:--|:--|:--|
| 1 | Lesson plan "Prepare the room" (shared `PREP` text in `build-pages.py`) | "…a word processor and spreadsheet app. Use instructor-provided fictional accounts or a modeled demonstration for cloud tasks. Test the local video and printer destination…" | <ul><li>No fictional accounts exist (CP-02, confirmed). Week 2 uses no spreadsheet or printer.</li><li>It does not name Edge, File Explorer or Word, where learners save, or that sharing and version history need an account.</li><li>OneDrive and Google Drive sharing both need a signed-in account ([Microsoft](https://support.microsoft.com/en-us/onedrive/share-files-and-folders-in-microsoft-onedrive); [Google](https://support.google.com/drive/answer/2494822?hl=en&co=GENIE.Platform%3DDesktop)).</li></ul> | Medium |
| 2 | Slides 11–12, 13, 18; video ch6–7; transcript | One practice handout, four names: `library-resource-v1.docx` (slides 11–12), `Resource guide.docx` (slide 13 simulation, also hard-coded in `assets/workshop.js` line 42), `resource-guide.docx` (slide 18), `library-help-draft.txt` (ch6 3:41, ch7 path "Community resources / library-help-draft"). A fifth, `computer-help-notes.txt`, sits unused in `video-scenes.py`. | Slide 11 teaches "a clear subject and version". The materials should use one name so learners can follow the file through the lesson. Use `library-help-v1.docx` in slides, simulations and worksheet now; change the video at the next render. | Medium |
| 3 | Slides 5–7; ch3 | Results are modelled as title, address and snippet. "Search-result snippets may be incomplete" (ch3). | <ul><li>In 2026 Google and Bing put an AI answer above the links. For "public library computer help" Google showed an AI Overview with a library's address and phone number (checked live, 2026-09-26).</li><li>Google: "AI responses may include mistakes" and advises checking important information in more than one place ([Google](https://support.google.com/websearch/answer/14901683)).</li><li>Learners should be told the summary is not the source: open the organization's own page.</li></ul> | Medium |
| 4 | Slides 13, 18; task 8; answer 8 | "Version history may recover earlier content." "Wrong content? Inspect version history." | <ul><li>Correct, but "Version history in Microsoft 365 only works for files stored in OneDrive or SharePoint in Microsoft 365" ([Microsoft](https://support.microsoft.com/en-us/office/view-previous-versions-of-office-files-5c1e076f-a9c9-41b8-8ace-f77b9642e2c2)). OneDrive keeps versions 30 days ([Microsoft](https://support.microsoft.com/en-us/office/restore-a-previous-version-of-a-file-stored-in-onedrive-159cad6d-d76e-4981-88ef-de6e96c93893)). Google Docs has its own ([Google](https://support.google.com/docs/answer/190843)).</li><li>Windows' own File History must be set up first, to an external drive or network location ([Microsoft](https://support.microsoft.com/en-us/windows/recover-lost-or-deleted-files-7bf065bf-f1ea-0a78-c1cf-7dcf51cc8bfc)).</li><li>A Word file saved only on a lab PC has no version history. Say so, and mark the slide 18 practice simulated.</li></ul> | Medium |
| 5 | Video ch2 (0:44–1:24); slide 3 | Search box shows "computer help + library + town"; narration "Computer help library plus your town". At 0:58 the box shows the refined search while the label still says "Broad · Computer help"; at 1:06 the box shows "computer help + town" while the label says "Refine…" (frames). | Plus signs are not needed: Bing: "By default, all searches are AND searches" ([Microsoft](https://support.microsoft.com/en-us/bing/advanced-search-options)); Google's operators are quotes, site: and minus ([Google](https://support.google.com/websearch/answer/2466433)). Novices copy what they see. Confirms VM-13. | Low |
| 6 | Slide 4 and its scene | "A site: filter narrows a domain…"; example "site:example.org computer help". | Correct operator ([Google](https://support.google.com/websearch/answer/2466433); Bing: works for "web domains, top level domains", no space after the colon, [Microsoft](https://support.microsoft.com/en-us/bing/advanced-search-keywords)). But "domain" is undefined, and example.org is a reserved example domain with no real pages. Use `site:gov`. | Low |
| 7 | Worksheet task 5; answer 5 | "Record a validation message and the confirmation." | The message is the browser's own: "Please select an item in the list." It appears only if the learner submits with a choice blank (checked live in the deck). The task never says to do that. The confirmation reads "Practice complete: …; No request was sent." (`lesson.js` line 49). | Low |
| 8 | Slide 12 scene vs slide 15 and simulator | Slide 12: "Owner: Alex — controls access; Partner: Sam — commenter". Slide 15: "Alex needs to suggest wording" (Alex is now the recipient). | Keep one cast: you are the owner, Alex is the reviewer. | Low |
| 9 | Video ch8 (5:06–5:49) | Arrow runs device → cloud only (frames 5:10, 5:18). Narration: "a change can travel between a device and an online service." | OneDrive: "If you add, change, or delete a file or folder in your OneDrive folder, the file or folder is added, changed, or deleted on the OneDrive website and vice versa" ([Microsoft](https://support.microsoft.com/en-us/onedrive/sync-your-computer-s-files-and-folders-with-onedrive)). Slide 13 draws both directions; the video should too. | Low |
| 10 | Answer guide task 7 | "…named recipients and least useful access." | Wording error (IR-18). Use "the least access each task needs". | Low |
| 11 | Worksheet task 7 | "Choose permissions for a reader, a reviewer and a coauthor." | "Coauthor" is not defined until week 4 (CP-11). Use "someone who writes it with you". | Low |
| 12 | Lesson plan 60–80 | "Play the cloud-file explainer." | Chapters 1–5 cover search, sources, the source trail and forms (CP-23, confirmed). | Low |
| 13 | Video ch6 → ch7 | ch6 saves the file to "This computer" ("Saved locally • not yet on another device", 3:44). ch7 opens it at "Training account • Community resources / library-help-draft" (4:14). | No step moves the file to a cloud account. Say "Once the file is in a cloud drive…" in the plan, or add one state at the next render. | Low |

**Totals:** High 0, Medium 4 (rows 1–4), Low 9 (rows 5–13).

**Verified as correct**
- **Search operators (slide 4):** quotation marks for an exact phrase; `site:` for one site or domain; filters can hide useful pages ([Google](https://support.google.com/websearch/answer/2466433); [Bing options](https://support.microsoft.com/en-us/bing/advanced-search-options); [Bing keywords](https://support.microsoft.com/en-us/bing/advanced-search-keywords)).
- **Date filter:** Google desktop: "Below the search box, click Tools", then pick the filter ([Google](https://support.google.com/websearch/answer/142143?hl=en&co=GENIE.Platform%3DDesktop)); the live control reads "Any time" (checked 2026-09-26). Bing also has an "Any time" filter (Past 24 hours to Past year), but it was hidden in the layout checked, so the quick card uses Google's.
- **Edge searches with Bing by default** ([Microsoft](https://support.microsoft.com/en-us/microsoft-edge/change-your-default-search-engine-in-microsoft-edge-cccaf51c-a4df-a43e-8036-d4d2c527a791)).
- **Source evaluation (slides 5–7; ch3):** who published it, evidence, purpose, currency, fit, and confirming with the responsible organization. The pre/post 3.2 items agree.
- **Source trail (slide 8; ch4):** the five fields match between slide 8, ch4 (frames 2:15–2:40) and task 3.
- **Practice form (slide 10; ch5):** required fields, review, and "No request was sent". ch5's card uses the same options as slide 10.
- **Central storage and ownership (slide 12):** "an editor can't change the owner" ([Google](https://support.google.com/drive/answer/2494822?hl=en&co=GENIE.Platform%3DDesktop)).
- **Sync carries deletions (slide 13; ch8):** OneDrive sync statement above. The OneDrive recycle bin keeps items 30 days (personal) or 93 days (work or school) ([Microsoft](https://support.microsoft.com/en-us/onedrive/restore-deleted-files-or-folders-in-onedrive)).
- **Roles (slide 15; ch7):** Google Drive has Viewer, Commenter, Editor. OneDrive has Can view and Can edit, plus Can review for Word documents, so "a commenter suggests, where supported" is accurate ([Microsoft](https://support.microsoft.com/en-us/onedrive/share-files-and-folders-in-microsoft-onedrive)).
- **Read-only (slide 16; slide 20; ch7):** "the document can be read or copied but not modified" ([Microsoft](https://support.microsoft.com/en-us/word/make-a-document-read-only-in-word)). Encrypt with Password and "Word won't be able to recover it" ([Microsoft](https://support.microsoft.com/en-us/word/protect-a-word-document-with-a-password)). Passwords to open and to modify are separate options (same page).
- **ZIP (slide 17; ch9):** Send to › Compressed (zipped) folder; Extract All ([Microsoft](https://support.microsoft.com/en-us/windows/zip-and-unzip-files-8d28fa72-f2f9-712f-67df-f80cf89fd4e5)). A ZIP is not encryption or a backup.
- **Recycle Bin (slide 18; ch9):** "open the Recycle Bin, select the files or folders you want to recover, right-click them, and select Restore" ([Microsoft](https://support.microsoft.com/en-us/onedrive/restore-deleted-files-or-folders-in-onedrive)). Shift + Delete skips it ([Microsoft](https://support.microsoft.com/en-us/windows/keyboard-shortcuts-in-windows-dcc61a57-8ff0-cffe-9796-cb9706c75eec)).
- **Knowledge checks:** the keys for slides 19 and 20 are correct.

## Does the content make sense for this audience?

**Undefined terms at first use**
- "domain" and "site: filter" (slide 4).
- "retention" (slide 12).
- "key" (slide 16: "Encryption protects readable content with a key").
- "validation message" (task 5).
- "coauthor" (task 7).
- "perspective" and "bias" (task 4 uses the GS6 words; slide 5 uses "What perspective or interest shapes it?", which is clearer). "Sync" and "free/busy"-style terms are well defined.

**Logic leaps**
- The slide order interleaves topics: slide 13 (sync) → 14 (video) → 15 (sharing) → 16 (protection) → 17 (ZIP) → 18 (recovery). Sync and recovery belong together; the new order teaches 13 with 17–18.
- ch7 jumps to read-only and encryption (4:47) in the middle of sharing, with no visual.
- ch9 moves from recovery to ZIP with one sentence ("Compression is a separate tool").

**Missing steps**
- No real click path anywhere for: using the date filter; copying a web address; File Explorer New › Folder; Word Save As into a folder; renaming; making and extracting a ZIP; restoring from the Recycle Bin; Word's Protect Document menu; a real Share box; OneDrive or Google Docs version history.
- The video's screens are simplified simulations ("Practice Files", "Practice Handout"); learners will not see the same buttons in File Explorer or OneDrive.

**Tasks unclear or unreliable as written**

| Task | Problem |
|:--|:--|
| Task 2 | "one refinement or filter" does not say where the filters are. |
| Task 4 | Five GS6 judgments plus "one check still needed" is a lot of typing for 5 minutes. |
| Task 5 | The validation message appears only if the learner leaves a choice blank; the task does not say so. |
| Task 6 | No app, location or file named; "organize a fictional folder" has no fictional files (IR review). |
| Task 8 | Two long written explanations and no hands-on step, though ZIP and the Recycle Bin need no account. |

**Pacing is unrealistic in two places**
- 60–80: 10 slides (7 with simulations) and a 7:12 video in 20 minutes.
- 110–120: two knowledge checks plus an individual justification from every learner.
- 30–50 (4 tasks in 20 minutes) and 80–110 (4 tasks in 30 minutes) are workable.

**Earlier findings re-checked**

| Earlier finding | Status | Evidence |
|:--|:--|:--|
| CP-23: video label and filename mismatch | **Confirmed, and wider** | Four names in learner materials, a fifth unused (row 2). |
| CP-19: "Files demonstration" overloaded | **Confirmed** | 10 slides plus 7:12 video in 20 minutes. |
| CP-02: week 2 tasks 6–7 need accounts | **Partly refuted** | Task 6 is local File Explorer work; task 7 works in the slide 15 simulator. Only a real Share box and version history need an account. |
| IR: "fictional files for the week 2 folder lab are not supplied" | **Confirmed**, but not needed | Learners can make their own file from tasks 1 and 3. |
| IR-18: "least useful access" | **Confirmed** | Answer guide 7. |
| CP-08 / AS-11: throwaway distractor | **Confirmed** | Slide 19 "Count the page's colors". Slide 20's options are real misconceptions. |
| CP-11: jargon | **Confirmed** | domain, retention, key, coauthor. |
| CP-03: no click paths | **Confirmed** | See "Missing steps". |
| VM-01: prompts give no thinking time | **Confirmed** | 1:16.6 (0.00 s), 3:29.1 (1.7 s to ch6), 5:01.8 (answer in 0.90 s), 6:34.8 (0.42 s). |
| VM-02: ch4 pace | **Confirmed** | 181 wpm, the fastest chapter in week 2. |
| VM-13: ch2 "+" and label lag | **Confirmed** | Frames 0:50, 0:58, 1:06. |
| AS-10: 4.2 and 7.4 untested | **Confirmed** | Pre/post week 2 items are 3.1, 3.2, 3.3 only. |
| AX-01: flip-card text hidden from screen readers | **Still present** | `build-pages.py` flip markup unchanged; affects slide 6. |

**New in this review**
- AI summaries at the top of results are not addressed (row 3).
- Version history needs a cloud account and is not labelled simulated (row 4).
- ZIP, extract and Recycle Bin restore are account-free Dos the week does not use.
- Warm-up ignores DL1 week 2 and week 3.
- Slide 12 and slide 15 swap Alex's role.
- ch8's sync arrow runs one way; ch6 → ch7 moves the file to a cloud account without a step.
- `workshops.py` `MAP[2][18]='sync'` never renders, because `photo_scenes.special(2,18)` takes precedence. Harmless, but confusing for the next editor.

## Video structure

**Sequence.** Ten chapters (38–52 seconds each) follow the slides' order: framing (ch1) → search (ch2) → judge (ch3) → source trail (ch4) → form (ch5) → folders (ch6) → sharing and read-only (ch7) → sync (ch8) → recovery and ZIP (ch9) → evidence recap (ch10). Opening and closing on the neighbor scenario (same photo, 0:00 and 6:31) gives a clear frame. Captions are in a separate VTT track.

**Model → prompt → answer, chapter by chapter**

| Chapter | Model | Prompt and answer | Rating |
|:--|:--|:--|:--|
| ch6 (3:31–4:14) | **Strong.** Seven-step screen demo: New folder → "Community resources" → Create → Save file as "library-help-draft.txt" → "Saved locally • not yet on another device" → "check account and sync" → "Opened from: Documents / Community resources" (frames 3:32–4:12). | No prompt. | Strong, but a simulated explorer; pair with live File Explorer. |
| ch7 (4:14–5:06) | **Strong.** Five-step screen demo: Viewer → Commenter → Editor → "Check recipient • save Commenter access" → "Partner view · Comment available · Direct editing unavailable" (frames 4:16–5:00). | "Pause and choose a role…" ends 5:01.8; "Viewer is the appropriate starting point" 0.90 s later. | Strong model; the instructor must pause by 5:02. |
| ch2 (0:44–1:24) | Diagram with a search box and three result cards. | Prompt ends 1:16.6 with 0.00 s gap. | Weak: "+" in the box and labels one step behind the box (VM-13). |
| ch3 (1:24–2:09) | Two cards: "Directory lead · Publisher: not named · Updated 2019" versus "Responsible source · Publisher: the library · Updated this month". | "Compare two pages that disagree" — an instruction with no pause. | Good Tell; the cards are the clearest source comparison in the week. |
| ch4 (2:09–2:47) | "My source record" card with all five fields. | None. | Good content, fastest narration (181 wpm). |
| ch5 (2:47–3:31) | Practice request card matching slide 10. | Prompt ends 3:29.1; ch6 starts 1.7 s later. | Good; pause by 3:29. |
| ch8 (5:06–5:49) | Diagram: file deleted on both sides; backup stays. | "…explain which protection would help…" ends 5:47.6; ch9 starts 1.5 s later. | Good idea; one-way arrow. Optional pause at 5:47. |
| ch9 (5:49–6:31) | Recovery tiles, then a ZIP flow (Approved copies → ZIP archive → Extracted files). Labels follow the narration (checked at 5:50–6:24). | None. | Tell only; four ideas in 41 s. Needs the live demo. |
| ch1, ch10 | Photo and routine diagram. ch10 lists the whole task after its prompt. | ch10 prompt ends 6:34.8; 35 s of task instructions follow. | Good. Pause at 6:35 to predict, then play on to compare. |

**Coverage gaps.** No chapter shows a real search filter, the AI summary above results, File Explorer, Save As, making or extracting a ZIP, the Recycle Bin, Word's Protect Document menu, a real Share box or real version history.

**Where it should play.** Play it chapter by chapter as the Show inside each cycle, from slide 14's chapter list, as in the restructure below. Stop at 1:17, 3:29, 5:02 and 6:35, and optionally at 5:47. The current plan plays it once at 60–80, after search was already practised. Slide 14 becomes the chapter menu, and the whole video is assigned as home review.

## Recommended restructure

This is a 120-minute running order of six short Tell, Show, Do, Review cycles inside the WIPPEA stages. It uses the current slides, chapters and tasks; tasks 6–8 are rewritten to be hands-on. "Live" means the instructor demonstrates on the projector in the lab's real Edge, File Explorer or Word. Chapters play from slide 14; use the sidebar to jump.

| Minutes | WIPPEA | Tell, Show, Do, Review cycle | Slides | Video | Worksheet / check | Notes |
|:--|:--|:--|:--|:--|:--|:--|
| 0–7 | W | Reconnect and goals | 1 | — | — | Logins. Pairs share the week 1 home task. Ask: "What made a search clear in Level 1?" and "Where did you save your Level 1 file, and what did you call it?" Read the five goals aloud. |
| 7–10 | I | **Tell:** the neighbor's question | 2 | ch1 0:00–0:44 | Task 1 | Learners pick their own service or use library computer help. |
| 10–22 | P → P → E | **Cycle A, search.** Tell: slides 3–4 (no plus signs; quotation marks; site:gov; date filter). Show: ch2 (pause at 1:17: learners say a search aloud), then live in Edge: "help" → "public library computer help" plus a town → one refinement; Tools › Any time on google.com. Do: task 2, every learner. Review: partner reads the refined search and says what changed. | 3, 4 | ch2 0:44–1:24 | Task 2 | Instructor scans for plus signs and searches too narrow to find anything. |
| 22–38 | P → P → E | **Cycle B, judge and record a source.** Tell: slides 5 and 7 (the AI summary is not the source). Show: ch3 and ch4, then live: open a library's own page, find who runs it and when it was updated, copy the address (Ctrl + L, Ctrl + C). Do: tasks 3 and 4, every learner, with slide 8 as the checklist. Review: slide 19; partner checks the five fields. | 5, 7, 8, 19 (6 optional) | ch3 1:24–2:09; ch4 2:09–2:47 | Tasks 3, 4 | Fullest cycle. If long, make task 4 oral and skip slide 6. |
| 38–46 | P → P → E | **Cycle C, online form.** Tell: slide 9. Show: ch5 (pause at 3:29), then submit slide 10 with a blank choice to show "Please select an item in the list." Do: task 5, every learner. Review: "Did anyone receive a request?" (No.) | 9, 10 | ch5 2:47–3:31 | Task 5 | — |
| 46–56 | — | Break | — | — | — | Screen-free. |
| 56–70 | P → P → E | **Cycle D, folders and names.** Tell: slides 11–12. Show: ch6, then live: Windows logo key + E › Documents › New › Folder "Community resources"; Word › File › Save As › Browse into it as library-help-v1.docx; close and reopen. Do: task 6, every learner. Review: partner reopens the file from the folder. | 11, 12 | ch6 3:31–4:14 | Task 6 | Say the video's name (library-help-draft) and why ours adds v1. |
| 70–84 | P → P → E | **Cycle E, sharing and protection.** Tell: slides 15–16. Show: ch7 (pause at 5:02, before the answer), then on the projector only: a real Share box from your own account with a fictional file, if you have one; Word › File › Info › Protect Document (point to Always Open Read-Only and Encrypt with Password; do not set them). Do: task 7 on slide 15, marked simulated, every learner. Review: slide 20; "Who owns the file after you share it?" | 15, 16, 20 | ch7 4:14–5:06 | Task 7 | Account-free path is the slide 15 simulator. |
| 84–102 | P → P → E | **Cycle F, sync, ZIP and recovery.** Tell: slides 13, 17, 18. Show: ch8 (optional pause at 5:47) and the slide 13 delete; ch9; then live: right-click the folder › Show more options › Send to › Compressed (zipped) folder; Extract All; delete a file and restore it from the Recycle Bin. Version history: slide 18 (simulated). Do: task 8, every learner. Review: partner asks "missing file or wrong wording?" and the learner names the tool. | 13, 17, 18 | ch8 5:06–5:49; ch9 5:49–6:31 | Task 8 | Windows 10 lab PCs show Send to on the first menu. |
| 102–112 | E | **Individual check.** Play ch10, pause at 6:35 ("What should the folder hold?"), play on to compare. Each learner shows you: (1) the five-field source note; (2) the file reopened from Community resources; (3) a file restored from the Recycle Bin, and names the role for a reviewer. Mark Independent / With prompt / Needs practice on a roster. | — | ch10 6:31–7:12 | Roster | Re-model only the missing step. |
| 112–120 | A | Transfer and close | 21, 22, 23 | — | Print or save the worksheet | Home task (see Objectives). Delete the practice folder and ZIP from Documents, then select Start fresh on this computer. |

Timing check: 7 + 3 + 12 + 16 + 8 + 10 + 14 + 14 + 18 + 10 + 8 = 120 minutes.

**Moved or optional**
- The two labs (30–50, 80–110) dissolve into cycles A–F.
- Slide 14 becomes the chapter launcher, not a block.
- Slide 6 (flip cards): optional in cycle B.
- Slide 21 changes role: from "Lab" to "do each task in its cycle".

**Tight spots:** cycle B (16 min) and cycle F (18 min). If running long, make task 4 oral in B, and in F skip the slide 13 simulation because ch8 shows the same thing.

## Top 10 changes, ranked

| # | Change | Where | Why (Tell/Show/Do/Review, WIPPEA or andragogy) | Effort | Source file to edit |
|:--|:--|:--|:--|:--|:--|
| 1 | Replace the 7-row agenda with six cycles (restructure above). Name slides, chapters with pause times, worksheet tasks and "every learner" in each. Drop "Play the cloud-file explainer". | Lesson plan agenda | Each skill gets its own Tell → Show → Do → Review; the Show comes before the Do; fixes the impossible 60–80 block | Medium | `scripts/dl2/author-content.py` week 2 `agenda` (line 39) |
| 2 | Make tasks 6 and 8 hands-on and account-free: folder, Save As, reopen; ZIP, Extract All; delete and restore from the Recycle Bin. Keep sharing and version history on slides 15 and 18, marked simulated. | Worksheet 6–8; answer guide | The Do must repeat the Show; GS6 4.2.1, 4.2.2, 4.2.6 get real practice | Small | `author-content.py` week 2 `lab` and `answers` |
| 3 | Use one file name, library-help-v1.docx, in slides 11–12, the slide 13 simulation, slide 18 and the worksheet. Change the video at the next render. | Slides 11–13, 18; `workshop.js` | Correctness row 2; the lesson about naming files must name its own file one way | Small | `author-content.py`; `photo_scenes.py` (2,11), (2,12), special (2,18); `workshops.py` sync; `assets/workshop.js` line 42 |
| 4 | Add a Windows 11 lab quick card (14 rows): address-bar search, quotation marks, site:, date filter, Ctrl + F, copy an address, New › Folder, Save As, rename, ZIP, Extract All, Recycle Bin, Word protection (instructor), Share and version history (instructor, needs an account). | Lesson plan and worksheet | The Show must be the same task as the Do; CP-03 | Small | `author-content.py` week 2 `lab_paths` |
| 5 | Rewrite goals as five plain objectives and five ABCD outcomes; split "organize files, set access and explain a recovery path" into Files and Access and recovery. | Slide 1; plan outcomes | WIPPEA Introduction and Evaluation; backward design | Small | `author-content.py` week 2 `objectives`, `outcomes` |
| 6 | Move slide 19 into cycle B and slide 20 into cycle E. Replace "Count the page's colors" with believable wrong answers ("top search result", "several websites repeat it"). Add a 3-item individual check with a roster. | Slides 19–20; 102–112 | Review checks each learner; respectful tone | Small | `author-content.py` slide 19 `options`, `why` |
| 7 | Add two Tell sentences: an AI summary at the top of results is not the source; version history needs a service such as OneDrive or Google Docs. | Slides 7, 13, 18 | Correctness rows 3–4 | Small | `author-content.py` slide bodies |
| 8 | Warm-up that uses week 1's home task and DL1 (smart search, file naming, backup). Add a home task. | 0–10; 112–120 | WIPPEA Warm-up and Application; the experience principle | Small | `author-content.py` week 2 agenda |
| 9 | Define terms and fix wording: domain and site:gov (slide 4, scenes), retention (slide 12), key (slide 16), "someone who writes it with you" (task 7), "least access each task needs" (answer 7), one cast for Alex (slide 12 scene), no plus signs (slide 3). | Slides 3, 4, 12, 16; tasks 5, 7 | Audience fit; correctness rows 5–11 | Small | `author-content.py`; `scenes.py` (2,4); `photo_scenes.py` (2,4), (2,12) |
| 10 | Week-specific prep; "every learner at their own seat" in the shared plan and worksheet text; video fixes at the next render (no "+", labels in sync, one filename, two-way sync arrow, silent holds after prompts, ch4 pace). | Plan prep and facilitation; video | Practice belongs to each learner; Show quality and think time | Small (text) / medium–large (render) | `author-content.py` week 2 `prep`; `build-pages.py` line 102 and worksheet intro; `video-scenes.py` lines 27–31, 161–165, 406–408; `screen-share-scenes.py` ch6–7 |

## Gemini claims checked

**Video review (`week-02-video-gemini-3.1-pro-preview.md`)**

| Claim | Verdict | Evidence |
|:--|:--|:--|
| Practice prompts give no time and spoil answers (1:13, 4:57) | **Agree**, with corrected times | Word timings: prompt ends 1:16.6 with 0.00 s gap; 5:01.8 with the answer 0.90 s later (Gemini said 2 s). |
| Form prompt at 3:24 has 0 s | **Agree** | Ends 3:29.1; ch6 starts 1.7 s later. |
| Prompt at 5:41 has 0 s | **Agree** | Instruction ends 5:47.6; ch9 starts 1.5 s later. Added as an optional pause. |
| 6:30 prompt is at the end of the video, so time is enough | **Disagree** | It ends 6:34.8 and 35 s of task instructions follow 0.42 s later. Pause at 6:35. |
| 5:06–6:30 packs five concepts into 84 s | **Agree** | ch8–9 cover sync, backup, version history, recycle bin and ZIP. The restructure pairs them with a live demo and a real Do. |
| ch4 source record is dense | **Agree** | Five fields in 38 s at 181 wpm (VM-02). |
| "Encryption" undefined at 4:47; tell the class to ignore it | **Partly agree** | It is said at 4:47.5 with no visual. But slide 16 defines it, slide 20 checks it and GS6 7.4 requires it. Teach it with slide 16 in cycle E instead of ignoring it. "Key" is the undefined word. |
| Audio–visual alignment is good (3:35, 4:28, 5:20) | **Agree** for ch6–8 | Frames 3:35, 3:39, 4:23, 4:28 and 5:18 match the narration. |
| (Not noted) ch2 search box | **Gemini missed it** | The box shows "computer help + library + town"; at 0:58 and 1:06 the labels lag the box (VM-13). |
| Abstract diagrams will not transfer to real software | **Agree** | ch6 and ch7 use "Practice Files" and "Practice Handout" windows. Pair each with a live Show. |
| Captions not burned in | **Correct** | Captions are the `week-02.vtt` track. |
| Legibility 5/5 | **Agree it is readable** | Not scored by pixel size. |
| Narrator doesn't read "+ New folder" (3:35) | **Agree, Low** | The on-screen label "New folder → Community resources" carries it. |

**Structure review (`week-02-structure-gemini-3.1-pro-preview.md`)**

| Claim | Verdict | Evidence |
|:--|:--|:--|
| Warm-up "Strong" | **Disagree: Adequate** | It reviews week 1 but not the DL1 search, source and file skills that week 2 builds on. |
| Presentation, Practice and Evaluation Weak; Application Adequate | **Agree** | See WIPPEA map. |
| Break the lesson into five cycles | **Agree in principle** | This review uses six: forms get their own short cycle, and sharing is kept apart from recovery. |
| Restructure starts with "0–25 Pre-test (Required evaluation)" | **Disagree** | Week 2 has no pre-test; the pre-test is week 1 slide 3. It would cost 25 minutes of teaching. |
| Search Show is "Video 0:44" | **Disagree** | The current plan plays the video only at 60–80, after the search lab. |
| Content "highly accurate and up-to-date" for Windows 11, Edge, Chrome | **Disagree** | The week gives no Windows, Edge or Chrome steps to be accurate about. It also missed the AI-summary gap and that version history needs a cloud account. |
| Filenames differ (three names) | **Agree, and wider** | Four names in learner materials, a fifth in the video generator. |
| Define "domain" | **Agree** | Also retention, key, coauthor, validation message. |
| Task 8 is too much writing; make it verbal | **Partly agree** | Make it hands-on (ZIP, extract, Recycle Bin) with short answers, not only verbal. |
| Self-concept Weak; Experience Strong | **Partly disagree** | Self-concept is Adequate (fictional, local practice); Experience is Weak because DL1 is ignored. |
| (Not noted) slide 19 distractor | **Gemini missed it** | "Count the page's colors". |
| Connect week 1's routine to week 2; instructor checks every Do | **Agree** | Both are in the restructure. |
