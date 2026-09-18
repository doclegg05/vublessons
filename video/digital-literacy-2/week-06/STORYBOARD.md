---
format: 1280x720
mode: autonomous
duration: 452.380s
message: Build something small enough to understand
audience: adult veteran learners
---

## Frame 1 — Build something small enough to understand

- src: compositions/frames/scene-1.html
- duration: 44.183s
- status: animated
- transition_in: cut
- scene: Picture-led explanation with original topic art, concise visual diagrams and word-timed state changes.
- voiceover: "Think about a list you already use: contacts, places to visit, or resources for a community activity. We will turn a fictional resource list into a small browser app that helps someone find an entry. Your experience with lists gives you a useful starting point for deciding whether the result makes sense. You do not need to become a professional programmer today. You will practice directing a build, checking what it does, and making one controlled improvement. The first version has one page, a search field, a category filter, and readable results. Keep the records fictional so the work can be shared and tested without exposing anyone's private information."
- blueprint: compose

Scene 1 (0–44.183s): Original software demonstration; state changes follow the recognized narration anchors. The original artwork sets context; large diagrams show the change with minimal labels. Keep the bottom band available for optional player captions.
## Frame 2 — Distinguish a website, an app, and a service

- src: compositions/frames/scene-2.html
- duration: 49.128s
- status: animated
- transition_in: cut
- scene: Picture-led explanation with original topic art, concise visual diagrams and word-timed state changes.
- voiceover: "A website can present information for people to read. A web app responds to input, such as filtering our resource list. Software as a service usually provides an ongoing hosted service and may include accounts, stored data, subscriptions, and operational support. Our one-file practice app is not all of that. It has no real account system, private database, or payment service. This distinction helps you ask for an achievable first version. A convincing sign-in screen does not prove secure authentication exists behind it. Start by describing the useful behavior you can actually test in the browser, then treat hosting, security, and service operations as separate decisions that require more work."
- blueprint: compose

Scene 1 (0–49.128s): Original software demonstration; state changes follow the recognized narration anchors. The original artwork sets context; large diagrams show the change with minimal labels. Keep the bottom band available for optional player captions.
## Frame 3 — Understand the three parts of the page

- src: compositions/frames/scene-3.html
- duration: 42.022s
- status: animated
- transition_in: cut
- scene: Picture-led explanation with original topic art, concise visual diagrams and word-timed state changes.
- voiceover: "HTML describes the content and structure: a heading, a labeled search field, and a list of resources. CSS controls how those parts are arranged and displayed. JavaScript responds to input, such as deciding which records match a search. Think of a familiar form: the questions and fields are its structure, their presentation helps you read them, and the rules determine what happens when you use it. The analogy is a starting point, not a complete description of software. Open the supplied starter in the browser and identify a visible example of each part. Changing a heading is different from changing the rule that filters the list."
- blueprint: compose

Scene 1 (0–42.022s): Original software demonstration; state changes follow the recognized narration anchors. The original artwork sets context; large diagrams show the change with minimal labels. Keep the bottom band available for optional player captions.
## Frame 4 — Write checks before asking for code

- src: compositions/frames/scene-4.html
- duration: 44.507s
- status: animated
- transition_in: cut
- scene: Picture-led explanation with original topic art, concise visual diagrams and word-timed state changes.
- voiceover: "Define success in terms someone else can observe. First, searching for library should show the fictional Community library entry. Second, searching for an unmatched term should show a clear no-results message. Third, the controls should work with the keyboard. Add a check for different letter cases and a narrow screen. These are acceptance checks: statements about behavior that help you decide whether the result is usable. Avoid a requirement such as make it amazing, because it does not explain what to test. Pause and write three checks for a small app idea of your own. Ask a partner whether they could carry out each check without guessing what you meant."
- blueprint: compose

Scene 1 (0–44.507s): Original software demonstration; state changes follow the recognized narration anchors. The original artwork sets context; large diagrams show the change with minimal labels. Keep the bottom band available for optional player captions.
## Frame 5 — Give the AI a bounded, useful request

- src: compositions/frames/scene-5.html
- duration: 47.688s
- status: animated
- transition_in: cut
- scene: Picture-led explanation with original topic art, concise visual diagrams and word-timed state changes.
- voiceover: "A useful prompt describes the user, the task, the controls, the data boundaries, and the checks. For example: build one local HTML page that searches fictional community resources by name and category. Include labeled fields, visible keyboard focus, a no-results message, and no external dependencies. Keep all example records fictional and explain how to run the file. Ask the AI to describe the important parts so you can inspect its work. Do not put passwords or private API keys into the prompt or the browser code. People can inspect code delivered to their browser. A longer prompt is not automatically better; each instruction should clarify behavior or a boundary you can verify."
- blueprint: compose

Scene 1 (0–47.688s): Original software demonstration; state changes follow the recognized narration anchors. The original artwork sets context; large diagrams show the change with minimal labels. Keep the bottom band available for optional player captions.
## Frame 6 — Open a working version before changing it

- src: compositions/frames/scene-6.html
- duration: 44.669s
- status: animated
- transition_in: cut
- scene: Picture-led explanation with original topic art, concise visual diagrams and word-timed state changes.
- voiceover: "Use the instructor-approved tool if one is available, or begin with the supplied starter. Save the file with its HTML extension and open it in the browser. Confirm that the heading, search field, filter, and results appear. Keep this first working version before asking for changes. If no AI account is available, you can still complete the exercise with a plain-text editor: change the heading and one fictional resource, save the file, and refresh the browser. Be careful that the editor has not silently added a text-file extension. The goal is a working result you can explain, not evidence that you used a particular paid service or model."
- blueprint: compose

Scene 1 (0–44.669s): Original software demonstration; state changes follow the recognized narration anchors. The original artwork sets context; large diagrams show the change with minimal labels. Keep the bottom band available for optional player captions.
## Frame 7 — Test the happy path and the missing result

- src: compositions/frames/scene-7.html
- duration: 42.58s
- status: animated
- transition_in: cut
- scene: Picture-led explanation with original topic art, concise visual diagrams and word-timed state changes.
- voiceover: "Type library into the search field and compare the result with your first acceptance check. Then enter an unmatched term such as zzz. The page should explain that there are no matching resources rather than appearing broken or showing an old result. Clear the field and try LIBRARY in uppercase. If the intended behavior is a case-insensitive search, it should find the same record. Next combine the search with a category filter and inspect whether both conditions apply. Record expected and actual results separately. A confident statement from the AI is not test evidence. The evidence is what happened when you carried out a named check on the saved file."
- blueprint: compose

Scene 1 (0–42.58s): Original software demonstration; state changes follow the recognized narration anchors. The original artwork sets context; large diagrams show the change with minimal labels. Keep the bottom band available for optional player captions.
## Frame 8 — Test access, screen size, and data assumptions

- src: compositions/frames/scene-8.html
- duration: 44.089s
- status: animated
- transition_in: cut
- scene: Picture-led explanation with original topic art, concise visual diagrams and word-timed state changes.
- voiceover: "Set the mouse aside and move through the controls with the keyboard. Can you see which control has focus? Can you enter a search and operate the filter? Narrow the browser window and check that labels, results, and buttons remain readable without important content being cut off. Then ask where the data lives. In our starter, fictional records are inside the file. Browser storage, if added later, may remain only in that browser and may be cleared; it is not automatically a shared database or a backup. Test persistence rather than assuming it. Use the course's existing text-size and accessibility habits as standards for the app you build."
- blueprint: compose

Scene 1 (0–44.089s): Original software demonstration; state changes follow the recognized narration anchors. The original artwork sets context; large diagrams show the change with minimal labels. Keep the bottom band available for optional player captions.
## Frame 9 — Request one repair and retest what worked

- src: compositions/frames/scene-9.html
- duration: 44.669s
- status: animated
- transition_in: cut
- scene: Picture-led explanation with original topic art, concise visual diagrams and word-timed state changes.
- voiceover: "Suppose the uppercase search failed. A useful revision request names the observed problem, the expected behavior, and the check: LIBRARY returns no result, but library returns Community library; make both searches match the same entry and preserve the category filter. Save the revised version under a distinct name. Repeat the failed check, then repeat a check that previously passed. This second step can reveal a regression, where fixing one behavior breaks another. If the new version is worse, return to the saved working version. Pause and make one small improvement or repair. Keep a brief test log so a partner can follow what changed and why you trust it."
- blueprint: compose

Scene 1 (0–44.669s): Original software demonstration; state changes follow the recognized narration anchors. The original artwork sets context; large diagrams show the change with minimal labels. Keep the bottom band available for optional player captions.
## Frame 10 — Demonstrate the result and name its limits

- src: compositions/frames/scene-10.html
- duration: 48.845s
- status: animated
- transition_in: cut
- scene: Picture-led explanation with original topic art, concise visual diagrams and word-timed state changes.
- voiceover: "Show a partner the saved app and carry out your three acceptance checks. Explain one part of the page, one change you made, and one limitation that remains. A local fictional prototype can be a successful learning result without being ready to operate a public service. Hosting is a separate choice. A real service handling accounts, private data, or payments needs appropriate security, access controls, support, and testing beyond this exercise. Do not treat a decorative sign-in form as protection. Carry forward the method you practiced: define a small task, give clear instructions, inspect the result, test more than the easiest path, and keep a way back when you revise it."
- blueprint: compose

Scene 1 (0–48.845s): Original software demonstration; state changes follow the recognized narration anchors. The original artwork sets context; large diagrams show the change with minimal labels. Keep the bottom band available for optional player captions.
