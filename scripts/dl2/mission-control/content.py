"""Mission Control weeks 2–6. Authored teaching sequence, not assessment data."""
def mission(title,app,start,finish,tell,show,do,question,choices,answer,why,lab,practice):
 return dict(title=title,app=app,start=start,finish=finish,tell=tell,show=show,do=do,question=question,choices=choices,answer=answer,why=why,lab=lab,practice=practice)
from week2 import WEEK2
from week3 import WEEK3
from week4 import WEEK4
WEEKS={
2:WEEK2,
3:WEEK3,
4:WEEK4,
5:dict(title='Protect your work. Show your skills.',photo='safety',warm='Name one safety habit you already use away from a computer. How could it help online?',apply='Use your results to choose one strength and one specific task to practice next.',minutes=[8,5,12,18,8,14,26,22,7],missions=[
mission('Make your station comfortable','Workstation / browser','A hard-to-read or distracting screen','One useful adjustment you can reverse',
 ['Adjust distance, position and readable text.','Captions and keyboard access help many people.','Quiet unneeded alerts; plan a stopping point.'],
 [('Adjust','Screen near eye level · keyboard within reach','Try a comfortable position and text size. Move regularly; seek help for persistent discomfort.'),('Access','Captions on · visible keyboard focus','These help in noise or without a mouse, not only for a diagnosed disability.'),('Focus','Essential alerts only · planned break','Fear of missing out can keep us checking. Use Do not disturb deliberately and restore shared settings.')],
 ['Change one setting and describe the benefit.','Try captions and keyboard navigation.','Restore the shared workstation settings.'],
 'Which design helps a learner who cannot use a mouse?', ['Color-only instructions','Keyboard access with visible focus','Smaller controls'],1,'Keyboard access and a visible focus indicator show where the next action will occur.',[0,1],3),
mission('Pause and verify independently','Message inspection','An urgent “benefits” message','A trusted contact found another way',
 ['Pressure, secrecy and unusual requests are clues.','Do not use the suspicious message’s contact.','Already shared a password? Act on the real site.'],
 [('Inspect','“Act now” · account-check.example · password request','The example is fictional. A familiar logo or stolen military photo does not prove identity.'),('Verify','Known bookmark or number on a trusted letter','Do not use the message’s link or phone number. Verify money requests, including from online friends.'),('Respond','Change an exposed password; enable MFA','Tell the instructor. For harmful posts, avoid escalation; preserve evidence if safe, report/block and seek support.')],
 ['Inspect sender, subject and destination safely.','Write warning signs and an independent check.','Explain a response to catfishing or harmful posts.'],
 'A new online friend requests secret gift-card payments. Next?', ['Send a small payment','Keep the request secret','Pause, send nothing and verify'],2,'Pressure for money and secrecy calls for an independent check. A profile photo is not proof of identity.',[2,3],8),
mission('Protect access and recovery','Security settings','A signed-in device and unneeded permissions','A lock habit and clear protection choices',
 ['Keep supported software updated.','Allow camera or microphone only when needed.','Encryption, read-only and backup do different jobs.'],
 [('Inspect','Browser → Site permissions → Camera','Review what remains allowed after a call. Do not change lab-wide settings without the instructor.'),('Protect','Read-only: limits edits · Encryption: unreadable without key','Use a supported device and updates. Give unknown USB drives to staff; do not plug them in.'),('Lock','Windows + L before stepping away','Encryption does not protect an open signed-in session from someone at the keyboard. Keep recovery keys safely.')],
 ['Inspect permissions and update status.','Identify password-to-open versus read-only.','Explain locking, encryption and separate backup.'],
 'Which makes file contents unreadable without the key?', ['Read-only','Encryption','ZIP compression'],1,'Encryption protects readable data. Read-only restricts edits and ZIP packages files; neither replaces encryption.',[4,5],11),
mission('Show what you can do','Five-task skills challenge','The course quick card and fresh practice files','Five observed skills; a separate post-test',
 ['Work independently; the quick card is allowed.','Show search, structure, SUM, recovery and feedback.','This observation is separate from your test score.'],
 [('Prepare','Fresh supplies.csv · blank Word document','Refine a local search; create a real heading, three numbered steps and a bold warning.'),('Demonstrate','Add Tape $4 → =SUM(B2:B5) → $29','Use the fresh $12/$8/$5 file. Recover deleted warning text with Undo while the file is still open.'),('Explain','Notice missing time/date/place in the flyer','Name two missing details and a courteous fix. Instructor records Independent / With prompt / Needs practice.')],
 ['Complete the five tasks on the worksheet.','Leave your work visible for the instructor.','Then take the 20-question post-test individually.'],
 'You needed a spoken prompt during the skills challenge. Rating?', ['Independent','With prompt','Add points to the post-test'],1,'Record the support used honestly. The observation and the scored post-test remain separate.',[6,7],15)
]),
6:dict(title='Guide an agent. Test its work.',photo='app-planning',warm='When you ask someone to repair something, how do you describe success? Apply that same care to an AI agent.',apply='Explain the bug, the repair and one responsibility you would keep if this app served real people.',minutes=[8,5,22,20,8,23,19,8,7],missions=[
mission('Specify the change','AI-agent specification','Version 1 searches names and descriptions','A precise category-search request',
 ['Name the user, task and expected behavior.','Say what must stay the same.','Write checks before asking for a change.'],
 [('Baseline','Version 1: LIBRARY works; learning finds none','Read the existing behavior before requesting a feature. All resource data is fictional.'),('Specify','Search categories too; keep mixed-case search','Preserve no-match feedback, keyboard access and narrow layouts. Change only this file.'),('Predict','learning → 2 · LIBRARY → 1 · zzz → 0','No sign-in, real personal data, secret keys or outside code. A prepared example works without an AI account.')],
 ['Open version 1 and run the three searches.','Write a request with limits and checks.','Predict results before viewing version 2.'],
 'Which request gives an agent a testable target?', ['Improve everything','Add category search; preserve case-insensitivity','Make it impressive'],1,'A bounded feature with checks lets you compare the change against the request.',[0,1],7),
mission('Review the proposed change','Change review','The agent returns version 2','Asked-for changes separated from regressions',
 ['HTML gives structure; CSS appearance; JS behavior.','Inspect the changed lines before trusting them.','An unrequested change deserves a test.'],
 [('Requested','name + category + description','Adding category to the searched fields meets the request. The search hint also changes.'),('Unexpected','Before: trim().toLowerCase() · After: trim()','The agent removed case normalization from the typed query. Do not assume this is harmless.'),('Predict','LIBRARY may no longer match lowercase text','Mark requested and unrequested changes. Ask for an explanation, then test the prediction.')],
 ['Open the local before/after code comparison.','Mark the category addition as requested.','Flag the missing toLowerCase and predict a failure.'],
 'The agent removed case normalization. What should you do?', ['Ignore it because the page looks right','Delete the whole app','Test mixed-case input'],2,'The visual layout can remain correct while the search behavior regresses.',[2],10),
mission('Test, report, repair, retest','Three-version test lab','A plausible app with a planted defect','A repair supported by repeatable evidence',
 ['Record expected and actual results.','Report steps, input and observed failure.','Retest the failure and previously passing checks.'],
 [('Test','Version 2: learning → 2; LIBRARY → 0','Try library, learning, zzz and mixed case; also test Tab and a narrow window.'),('Report','Expected 1 library; actual no matches for LIBRARY','Ask the agent to restore case-insensitive input without removing category search.'),('Retest','Version 3: LIBRARY → 1; Learning → 2; zzz → 0','Repeat keyboard and narrow-screen checks too. Fixing one bug can break something else.')],
 ['Record version 2 expected versus actual results.','Write a reproducible bug report and repair request.','Run the same checks on version 3.'],
 'The repaired app finds LIBRARY. Are you finished testing?', ['Yes; the one bug is fixed','No; repeat earlier passing checks too','Only change the colors'],1,'Retest category search, no matches, keyboard and narrow layout so the repair does not hide a new regression.',[3,4,5],17),
mission('Know what “ready” means','Web app / SaaS','A local prototype on your computer','A clear boundary and an operating owner',
 ['A local demo is not a secure hosted service.','Real sign-in and permissions need server checks.','Name the owner, costs, backups and support.'],
 [('Separate','Browser: public UI · Server: private secrets','Do not put secret API keys in browser code. A mock sign-in form is not authentication.'),('Operate','Hosting + recurring cost + access + recovery','SaaS means software provided as a service. Someone must maintain it and support users.'),('Decide','Keep this practice local with fictional data','A hosted app needs tested permissions, data handling and recovery before real use. Do not publish in this lab.')],
 ['Draw the browser/server boundary.','Name an owner and a recovery responsibility.','Use the separate 8-point extension rubric.'],
 'Where does a private API key belong in a deployed app?', ['Public HTML','A screenshot in the help page','Protected server-side configuration'],2,'Private keys must stay out of downloaded browser code. Access checks also belong on the server.',[6,7],13)
])}
