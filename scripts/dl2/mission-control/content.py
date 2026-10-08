"""Mission Control weeks 2–6. Authored teaching sequence, not assessment data."""
def mission(title,app,start,finish,tell,show,do,question,choices,answer,why,lab,practice):
 return dict(title=title,app=app,start=start,finish=finish,tell=tell,show=show,do=do,question=question,choices=choices,answer=answer,why=why,lab=lab,practice=practice)
from week2 import WEEK2
from week3 import WEEK3
from week4 import WEEK4
from week5 import WEEK5
WEEKS={
2:WEEK2,
3:WEEK3,
4:WEEK4,
5:WEEK5,
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
