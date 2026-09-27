# Week 6 structure and content review (Tell, Show, Do, Review + WIPPEA + adult learning)

## Verdict
The lesson is highly ambitious, well-documented, and uses excellent, accessible analogies, but it structurally fails its stated goal and the Tell, Show, Do, Review framework. The instructor's goal is to "teach the basics of agentic engineering a SaaS website," yet the materials explicitly and correctly state (Slides 3, 15, 19) that learners are building a *local prototype*, not a SaaS website. Furthermore, the lesson plan relies on massive 20- to 30-minute blocks of instruction followed by equally long blocks of practice, which will overwhelm learners who only recently mastered basic computer skills. The single most important change is to break the 40-minute "Model / Build" blocks into 10-minute Tell-Show-Do-Review cycles for each specific skill (e.g., writing checks, editing HTML, testing edge cases).

## WIPPEA map
| Stage | Where it happens | How well it meets purpose | Evidence | What to change |
|:--|:--|:--|:--|:--|
| **Warm-up** | Missing from lesson plan | Missing | The lesson plan starts at minute 0 with "Choose the problem." There is no activation of prior knowledge or review of Weeks 1–5. | Add the required 25-minute pre-test at the very beginning to serve as the evaluation of prior weeks and a transition into Week 6. |
| **Introduction** | Lesson plan 0–10m; Slides 1–2 | Strong | Slide 1 clearly lists the three bulleted learning outcomes. Slide 2 connects the task to a familiar, concrete scenario (community resources). | Keep as is, but move it to immediately follow the pre-test. |
| **Presentation** | Lesson plan 10–30m, 60–75m; Slides 3–5, 8, 13–15; Video chapters 1–3, 8 | Weak | The lesson plan groups 20 minutes of modeling into one block. This is too much cognitive load (SaaS concepts, HTML/CSS/JS, prompting, and testing all at once). | Break the presentation into smaller chunks. Teach HTML editing, let them do it. Teach testing, let them do it. |
| **Practice** | Lesson plan 30–50m, 75–105m; Slides 6–7, 9–12, 17–18; Worksheet tasks 1–7 | Adequate | The worksheet provides excellent step-by-step guidance, but the practice happens too long after the initial presentation. | Interleave the worksheet tasks directly after their corresponding video chapters/slides. |
| **Evaluation** | Lesson plan 105–120m; Worksheet task 8; Answer guide rubric | Strong | The rubric directly measures the stated objectives (defines task, builds prototype, tests/records, explains limits). | Ensure the instructor checks individual test logs during the practice phase, not just at the end. |
| **Application** | Slides 19, 23–24 | Adequate | Slide 19 discusses the real-world implications of hosting (costs, maintenance, access). | Ask learners how they might use this "vibe coding" approach for a personal hobby or household list. |

**Overall flow:** The order of concepts is logical, but the pacing and block sizes are wrong. The lesson plan separates the "Test demonstration" (60–75m) from the "Build round one" (30–50m). In software prototyping, you must test immediately after building. The video chapters are excellent but are meant to be shown during the massive demonstration blocks, exacerbating the "long tell/show" problem. 

## Tell, Show, Do, Review by skill
The week currently follows big blocks rather than short cycles. For older veterans transitioning from basic computer skills, a 20-minute demonstration of HTML, CSS, JS, prompting, and file saving will result in forgotten steps by the time they open Notepad.

| Skill | Tell | Show | Do | Review | Missing or weak steps |
|:--|:--|:--|:--|:--|:--|
| **Distinguish App vs SaaS** | Slide 3 | Video 1:31 (Ch 2) | Worksheet Task 8 | Slide 20 (Knowledge check) | Do is delayed until the very end of the class. |
| **Write acceptance checks** | Slide 6 | Video 3:16 (Ch 4) | Worksheet Task 1 | Partner check (Worksheet instructions) | Strong cycle, but needs to happen before any code is discussed. |
| **Write a bounded prompt** | Slide 7 | Video 4:15 (Ch 5) | Worksheet Task 2 | Answer guide rubric | Good, but the lesson mixes "use AI" with "edit the starter manually," which confuses the Do step. |
| **Edit & run local HTML** | Slide 10 | Video 5:17 (Ch 6) | Worksheet Tasks 3 & 4 | Browser refresh check | Show step needs to explicitly demonstrate Windows 11 Notepad file saving to avoid `.txt` errors. |
| **Test edge cases** | Slide 17 | Video 6:35 (Ch 7) | Worksheet Task 6 | Worksheet test log | Seven edge cases is too many for the allotted time; reduce to four. |
| **Request a revision** | Slides 12, 18 | Video 8:44 (Ch 9) | Worksheet Tasks 5 & 7 | Regression test (Task 7) | The Do step is split across tasks 5 and 7, making the cycle disjointed. |

## Objectives
1. **Describe a small app and write a bounded AI prompt.**
   * *ABCD rewrite:* Given a fictional community scenario (Condition), the learner (Audience) will write a bounded AI prompt (Behavior) that includes content, behavior, and privacy boundaries (Degree).
   * *Taught/Evaluated:* Taught on Slide 7 and Video Chapter 5. Practiced in Worksheet Task 2. Evaluated via the Answer Guide rubric.
2. **Explain HTML, CSS, JavaScript and browser storage.**
   * *ABCD rewrite:* Given a working local web app (Condition), the learner (Audience) will verbally explain (Behavior) the roles of HTML, CSS, JS, and local storage with 100% accuracy (Degree).
   * *Taught/Evaluated:* Taught on Slides 5 and 13. Practiced and evaluated in Worksheet Task 8 and the final demonstration.
3. **Test a prototype, revise one behavior and explain what a hosted service still needs.**
   * *ABCD rewrite:* Given a local HTML prototype (Condition), the learner (Audience) will execute and log at least four edge-case tests, perform one revision, and state two missing SaaS requirements (Behavior) without instructor assistance (Degree).
   * *Taught/Evaluated:* Taught on Slides 17–19. Practiced in Worksheet Tasks 6–7. Evaluated via the Answer Guide rubric.

## Adult learning principles
| Principle | How well | Evidence | Suggested improvement |
|:--|:--|:--|:--|
| **1. Need to know** | Strong | Slides 14–15 and 19 clearly explain *why* we use fictional data and *why* a local file isn't a secure SaaS. | None. Excellent context setting. |
| **2. Self-concept** | Adequate | Video Chapter 1 encourages them to think of their own lists, but the starter app forces "Community resources." | Provide two different starter apps (e.g., a hobby list and a resource list) so they have a choice. |
| **3. Experience** | Strong | Video Chapter 1 ties the abstract concept of a database to familiar concepts like contacts and places to visit. | Ask learners to share a time a website's search function frustrated them, tying into the testing phase. |
| **4. Readiness** | Weak | The leap from Level 1 (basic mouse/keyboard) to editing raw HTML tags and JavaScript arrays is massive. | Provide a "word bank" or exact copy-paste snippets in the worksheet so they don't have to type raw syntax. |
| **5. Orientation** | Strong | The entire lesson is built around a single, concrete task: building a resource finder. | None. Highly task-centered. |
| **6. Motivation** | Adequate | Building a working app builds confidence, but syntax errors in Notepad will cause severe frustration. | Emphasize that breaking the code is normal and show exactly how to use the "recoverable copy" (Ctrl+Z or reopening v1). |

## Content correctness
| Where | What it says | What is correct | Severity |
|:--|:--|:--|:--|
| **Instructor Goal** | "...teach the basics of agentic engineering a SaaS website." | The lesson explicitly teaches building a *local HTML prototype*, not a SaaS website (Slide 3, 19). | High. The stated goal contradicts the actual, correct lesson content. |
| **Starter App Code** | `<script src="/shared/text-size.js"></script>` | If a learner opens this local file (`file:///C:/...`), the absolute path `/shared/text-size.js` will look at the root of their C: drive and fail to load. It must be a relative path (e.g., `./shared/...`) or an absolute URL (e.g., `https://...`), or be removed. | High. This will cause a broken script on a local machine. |
| **Starter App Code** | `<a href="/courses/digital-literacy-2/weeks/week-06/presentation.html">` | Same issue. This absolute path will result in a "File not found" error when clicked from a local file. | Medium. |
| **Worksheet (Save instructions)** | "On Windows, set Save as type to All files so Notepad does not add .txt." | In Windows 11, if "Hide extensions for known file types" is enabled in Explorer, saving as `name.html` might still save as `name.html.txt`. The foolproof method is to wrap the filename in quotes: `"resource-finder-v2.html"`. | Medium. Will cause the file to open in Notepad instead of Edge/Chrome. |
| **Worksheet (Mac instructions)** | "On a Mac, open TextEdit..." | The audience is in a standard computer lab with individual workstations (almost universally Windows in U.S. military/veteran basic IT labs). | Low. Correct, but adds visual clutter and cognitive load for Windows users. |
| **Slide 21** | "Where should a private API key go in a browser prototype? [Nowhere in the browser code]" | Correct, but the lesson never actually defines what an "API key" is before asking this question. | Low. Define API key briefly on Slide 14. |

## Does the content make sense for this audience?
* **Undefined terms:** "API key" (Slide 14/21) and "external dependencies" (Slide 7) are used without plain-language definitions. For basic computer skills graduates, these are foreign concepts.
* **Leaps in logic:** The worksheet asks learners to write an AI prompt (Task 2), but then immediately tells them to open a pre-built starter app and edit it manually (Task 3/4). It is confusing whether they are generating an app from scratch using their prompt, or just editing a template. 
* **Pacing:** The lesson plan allocates 120 minutes, but the prompt requires keeping a 25-minute pre-test. This leaves only 95 minutes. Expecting older novices to learn prompting, edit HTML, save file extensions correctly, and run 7 different regression tests in 95 minutes is highly unrealistic.

## Recommended restructure
*Assumes a 120-minute total session, incorporating the required 25-minute pre-test, and breaking the instruction into short TSDR cycles.*

*   **0–25 min: Warm-up & Pre-test**
    *   Administer the 25-minute pre-test (evaluating Weeks 1–5).
*   **25–40 min: Cycle 1 - App vs. SaaS & Acceptance Checks**
    *   *Tell/Show:* Slides 1–4, 6. Video Chapters 1, 2, and 4. Explain the goal and how to write checks.
    *   *Do:* Worksheet Task 1 (Write user, problem, and 3 checks).
    *   *Review:* Partner check.
*   **40–55 min: Cycle 2 - The Starter App & HTML/CSS/JS**
    *   *Tell/Show:* Slides 5, 9, 10. Video Chapters 3 and 6. Show how to open the starter app and explain the 3 layers. Demonstrate saving with quotes `"...html"` in Notepad.
    *   *Do:* Worksheet Tasks 3 & 4 (Save v1, edit the `<h1>` and array manually, save as v2, refresh browser). *Skip the AI generation path to save time and reduce confusion.*
    *   *Review:* Instructor walks the room to ensure everyone sees "Community Skills Desk" in their browser.
*   **55–65 min: Break** (10 minutes away from screens).
*   **65–85 min: Cycle 3 - Testing Edge Cases**
    *   *Tell/Show:* Slides 17. Video Chapters 7 and 8. Demonstrate testing the happy path, empty path, and keyboard focus.
    *   *Do:* Worksheet Task 6 (Test log). *Reduce to 4 tests: Blank, Matching, No match, Keyboard.*
    *   *Review:* Discuss as a class what failed or looked weird.
*   **85–105 min: Cycle 4 - Revising & Data Boundaries**
    *   *Tell/Show:* Slides 11, 12, 18. Video Chapter 9. Show how to make one small change and retest.
    *   *Do:* Worksheet Tasks 5 & 7 (Make one more manual edit or use AI if available, save as v3, run regression test).
    *   *Review:* Verify the previous tests still pass.
*   **105–120 min: Cycle 5 - Security, Limits & Final Demo**
    *   *Tell/Show:* Slides 13–15, 19. Video Chapter 10. Explain why this local file is not a secure SaaS.
    *   *Do:* Worksheet Task 8 (Demonstrate app to partner, explain limits).
    *   *Review:* Instructor uses the Answer Guide rubric to evaluate learners during their paired demos. Slide 24 (Next steps).

## Top 10 changes, ranked
1. **Fix the stated course goal (High effort - conceptual):** Change the instructor's goal from "engineer a SaaS website" to "build and test a local web app prototype." This aligns the goal with the actual (and correct) lesson content.
2. **Restructure into short cycles (Medium effort):** Abandon the 20-minute "Model" and 20-minute "Build" blocks. Use the recommended restructure above to interleave the video chapters, slides, and worksheet tasks every 10–15 minutes.
3. **Add the Pre-test (Small effort):** Insert the required 25-minute pre-test at the beginning of the lesson plan to serve as the WIPPEA Evaluation for prior weeks and Warm-up for Week 6.
4. **Fix Notepad save instructions (Small effort):** Update Worksheet Task 3 and Slide 10 to instruct learners to wrap their filename in quotes (e.g., `"resource-finder-v2.html"`) to guarantee Windows 11 Notepad does not append `.txt`.
5. **Fix broken local paths in Starter App (Small effort):** Remove `<script src="/shared/text-size.js"></script>` and the absolute `<a href="...">` link from the `resource-finder.html` starter file, as these will throw errors when run locally from a `file:///` path.
6. **Clarify the build path (Medium effort):** The worksheet currently mixes "write an AI prompt" with "manually edit the starter app." For this audience, make manual editing of the starter app the primary path. Make the AI generation an optional extension for fast finishers.
7. **Reduce the testing burden (Small effort):** Cut the required edge-case tests in Worksheet Task 6 from seven down to four (e.g., Blank, Match, No Match, Keyboard). Seven is too repetitive and time-consuming for a 120-minute class.
8. **Remove Mac instructions (Small effort):** Delete the TextEdit instructions from the worksheet. The audience is in a standard computer lab (Windows), and extra OS instructions add unnecessary cognitive load.
9. **Define "API Key" (Small effort):** Add a brief, plain-language definition of an API key (e.g., "a secret password for software to talk to other software") to Slide 14 so the knowledge check on Slide 21 makes sense.
10. **Add a visual verification step (Small effort):** Add a note to the worksheet telling learners to look at the icon of their saved file in the Downloads folder. If it looks like a text document instead of the Edge/Chrome logo, they saved it wrong. This provides immediate, low-risk feedback.