---
format: 1280x720
mode: autonomous
duration: 558.720s
message: Direct an agent, then check its work
audience: adult veteran learners
---

## Frame 1 — Direct an agent, then check its work

- src: compositions/frames/scene-1.html
- duration: 42.093s
- status: animated
- transition_in: cut
- scene: app / scenario
- photo: app-planning
- worked states: Agent|Reads, plans, edits, checks; You|Ask clearly, review every change; Today|One change to a fictional finder
- voiceover: "An AI coding agent is a program that reads the files of an app, plans a change, edits the code, and can run checks, all from a request written in plain English. That sounds like magic, but it is closer to hiring a fast helper who has never met you. It does exactly what it understood, which is not always what you meant. Today you will direct one. Our app is a small, fictional community resource finder. You will ask for one change, read what the agent changed, test it, and report a problem. Then we look at what it would take to turn this page into a real service."
- blueprint: compose

Scene 1 (0–42.093s): Authored fictional demonstration with chapter-specific evidence captions. When present, a landscape scenario photograph or the generated week-1 workstation clip establishes context before the diagram. Narration audio, chapter windows and existing caption files are retained in visual-only mode.
## Frame 2 — Start from what already works

- src: compositions/frames/scene-2.html
- duration: 61.621s
- status: animated
- transition_in: cut
- scene: baseline / demonstration
- photo: none: full-stage authored demonstration
- worked states: library|1 found; LIBRARY|1 found: capitals ignored; learning|Nothing: categories not searched
- voiceover: "Before you ask for any change, find out what works now. Open version 1 of the resource finder and try a few searches. Library finds one resource. LIBRARY in capital letters also finds one, because the page ignores capital letters. But learning finds nothing, even though two resources are about learning. Version 1 only searches names and descriptions, not categories. That is the one thing we want changed. Writing down what works today also tells you what must not break tomorrow. Search version 1 for library, LIBRARY, learning, community, and zzz, and write down each result. Pause the video now."
- blueprint: compose
- cards: divider · pause

Scene 1 (0–61.621s): Authored fictional demonstration with chapter-specific evidence captions. When present, a landscape scenario photograph or the generated week-1 workstation clip establishes context before the diagram. Narration audio, chapter windows and existing caption files are retained in visual-only mode.
## Frame 3 — Write a spec the agent can follow

- src: compositions/frames/scene-3.html
- duration: 57.901s
- status: animated
- transition_in: cut
- scene: spec / demonstration
- photo: none: full-stage authored demonstration
- worked states: Change|Search categories too; Keep|Capitals match; no-match message; Checks|learning → 2 · LIBRARY → 1
- voiceover: "A spec is a careful request. It names one change, who it helps, and what must stay the same. Ours says: let the search also find resources by category, for visitors who know the kind of help but not the name. Keep capital letters matching, and keep the message that appears when nothing matches. Then add acceptance checks, tests anyone can run. I type learning, I expect two resources. I type LIBRARY, I expect one. Never put real names, passwords, or secret keys in a request. Write your spec and three checks a partner could run. Pause the video now."
- blueprint: compose
- cards: pause

Scene 1 (0–57.901s): Authored fictional demonstration with chapter-specific evidence captions. When present, a landscape scenario photograph or the generated week-1 workstation clip establishes context before the diagram. Narration audio, chapter windows and existing caption files are retained in visual-only mode.
## Frame 4 — Ask for a plan, then predict

- src: compositions/frames/scene-4.html
- duration: 52.983s
- status: animated
- transition_in: cut
- scene: plan / demonstration
- photo: none: full-stage authored demonstration
- worked states: Plan|One file, one rule, checks; Freedom|You choose; you still review; Predict|Part · lines · what could break
- voiceover: "A good agent can show its plan before it touches anything. Ask for that. Some agents can also work on their own for a while, and you choose how much freedom to give. Either way, you review every change before you accept it. Read the plan and make a prediction. Which part of the page will change? About how many lines? What could break? Predicting first makes you a sharper reviewer, because you know what to look for. Write your prediction: the part that will change, about how many lines, and one thing that could break. Pause the video now."
- blueprint: compose
- cards: divider · pause

Scene 1 (0–52.983s): Authored fictional demonstration with chapter-specific evidence captions. When present, a landscape scenario photograph or the generated week-1 workstation clip establishes context before the diagram. Narration audio, chapter windows and existing caption files are retained in visual-only mode.
## Frame 5 — Read the diff before you trust it

- src: compositions/frames/scene-5.html
- duration: 68.048s
- status: animated
- transition_in: cut
- scene: diff / screen-share
- photo: none: full-stage authored demonstration
- worked states: A diff: minus removed, plus added; Asked for: category added to the search; Not asked for: toLowerCase removed; Ctrl+U shows the code • Ctrl+F: 1 match in version 2; Version 1 has 2 matches; version 2 has 1
- voiceover: "A diff shows exactly what changed. A line with a minus sign was removed, and a line with a plus sign was added. Here, one added line puts the category into the search. That is what we asked for. But look closer. Another line lost three words written together in the code: to lower case. That is the step that ignores capital letters. Nobody asked for that. You can check it yourself. Press Control and U to see the page's code, then Control and F to search it for to lower case. Version 1 has two matches, and version 2 has one. Open the Mission 6B practice page, and mark each changed line as asked for or not. Pause the video now."
- blueprint: compose
- cards: pause

Scene 1 (0–68.048s): Full-screen task simulation with word-aligned cursor, clicks, typed inputs, and verified outcomes; see screen-share-actions.json. Narration audio, chapter windows and existing caption files are retained in visual-only mode.
## Frame 6 — Test the agent's version

- src: compositions/frames/scene-6.html
- duration: 59.3s
- status: animated
- transition_in: cut
- scene: app / screen-share
- photo: none: full-stage authored demonstration
- worked states: Test the agent's version 2; Happy path: learning → 2 found; library → 1 found; zzz → the no-match message; LIBRARY → nothing found: a regression; Tab: a clear outline on each control
- voiceover: "Now test the agent's version, called version 2. Start with the happy path, the normal use you expect to work. Type learning, and two resources appear. Type library, and one appears. Type zzz, and the no-match message shows. Then try capital letters. Type LIBRARY, and nothing is found. Version 1 found it. Something that used to work and broke after a change is called a regression. Keep going, because one failure does not end a test. Check that Tab moves a clear outline through the controls, and that the page still works in a narrow window. Run the five checks in your test log. Pause the video now."
- blueprint: compose
- cards: divider · pause

Scene 1 (0–59.3s): Full-screen task simulation with word-aligned cursor, clicks, typed inputs, and verified outcomes; see screen-share-actions.json. Narration audio, chapter windows and existing caption files are retained in visual-only mode.
## Frame 7 — Report it so it can be fixed

- src: compositions/frames/scene-7.html
- duration: 56.693s
- status: animated
- transition_in: cut
- scene: report / demonstration
- photo: none: full-stage authored demonstration
- worked states: Steps|Open version 2; type LIBRARY; Expected|1 resource, as version 1; Keep|The new category search
- voiceover: "A bug report is a request a stranger could follow. Give the steps: open version 2 and type LIBRARY. Give what you expected: one resource, as version 1 found. Give what actually happened: no matches. Then say what must stay the same: keep the new category search. That last part matters, because a careless fix can undo the work you wanted. Saying it is broken gives the agent nothing to act on. A clear report usually gets a small, careful repair. Write a repair request with the steps, what you expected, what happened, and what to keep. Pause the video now."
- blueprint: compose
- cards: pause

Scene 1 (0–56.693s): Authored fictional demonstration with chapter-specific evidence captions. When present, a landscape scenario photograph or the generated week-1 workstation clip establishes context before the diagram. Narration audio, chapter windows and existing caption files are retained in visual-only mode.
## Frame 8 — Retest the repair

- src: compositions/frames/scene-8.html
- duration: 55.509s
- status: animated
- transition_in: cut
- scene: retest / demonstration
- photo: none: full-stage authored demonstration
- worked states: Failed check|LIBRARY → 1 again; Passed before|learning 2 · zzz no match; Decide|Accept only if nothing broke
- voiceover: "The agent sends back version 3. Do not trust it until you retest. First repeat the check that failed. Type LIBRARY, and one resource appears again. Then repeat checks that passed before, because fixing one thing can break another. Learning still finds two, and zzz still shows the no-match message. Only when the failed check passes and nothing else broke do you accept the repair. This loop is the whole job: ask clearly, read the change, test it, report it, and retest. Run your checks on version 3 and decide whether to accept the repair. Pause the video now."
- blueprint: compose
- cards: pause

Scene 1 (0–55.509s): Authored fictional demonstration with chapter-specific evidence captions. When present, a landscape scenario photograph or the generated week-1 workstation clip establishes context before the diagram. Narration audio, chapter windows and existing caption files are retained in visual-only mode.
## Frame 9 — What stands between a page and a service

- src: compositions/frames/scene-9.html
- duration: 58.579s
- status: animated
- transition_in: cut
- scene: roadblocks / demonstration
- photo: none: full-stage authored demonstration
- worked states: Address|Domain name, rented yearly; Server|Back end · sign-in · secret keys; Caretaker|Pays, updates, reviews
- voiceover: "Our finder is one page with fictional data. A real service needs much more. It needs an address, a domain name you rent every year. It needs a home: hosting is a computer that keeps the site running, so anyone with the address can use it. To save favorites for many people, it needs a back end, the part on a server that stores data. Sign-in must be checked on that server, never by a picture of a sign-in box. A secret API key, the code that lets your app use a paid service, stays on the server too. Plan the finder as a real service, one roadblock at a time. Pause the video now."
- blueprint: compose
- cards: divider · pause

Scene 1 (0–58.579s): Authored fictional demonstration with chapter-specific evidence captions. When present, a landscape scenario photograph or the generated week-1 workstation clip establishes context before the diagram. Narration audio, chapter windows and existing caption files are retained in visual-only mode.
## Frame 10 — Direct it, check it, own it

- src: compositions/frames/scene-10.html
- duration: 45.993s
- status: animated
- transition_in: cut
- scene: evidence / scenario
- photo: app-planning
- worked states: Loop|Ask · read · test · report · retest; Owner|Someone keeps it running; Limit|An agent cannot take responsibility
- voiceover: "Here is what you practiced. You started from what worked, wrote one clear request with checks, predicted the change, read the diff, tested, reported a regression, and retested the repair. That loop works whether the helper is an AI agent or a person. And someone must still own the result. A real service needs a caretaker who pays the bills, keeps it updated, backs up the data, helps users, and reviews every change before it goes live. An agent can write code quickly. It cannot take responsibility. That part stays with the people who run the service."
- blueprint: compose
- cards: divider

Scene 1 (0–45.993s): Authored fictional demonstration with chapter-specific evidence captions. When present, a landscape scenario photograph or the generated week-1 workstation clip establishes context before the diagram. Narration audio, chapter windows and existing caption files are retained in visual-only mode.
