"""Mission Control Week 6: direct an AI coding agent, review its change, test it, and learn what stands between
a page on your computer and a real service.

Spec: docs/digital-literacy-2/week-06-spec.md. The three prepared versions in activities/ are the evidence
(version 2 keeps its planted defect: the search line lost .toLowerCase(), so LIBRARY and Learning find
nothing). Learners need no AI account; the instructor's live agent run is optional. Mission D teaches the six
roadblocks between a local page and a service: address (domain name), home (hosting), memory (back end and
database), front door (sign-in), secret keys, and a caretaker (cost and upkeep). No capstone, no break,
no timers (Britt, 2026-10-08).
"""
from lessonkit import mission, quote, rnd, table

V1 = ('Open version 1', '/courses/digital-literacy-2/activities/resource-finder.html')
V2 = ('Open the agent\u2019s version', '/courses/digital-literacy-2/activities/resource-finder-agent.html')
V3 = ('Open the repaired version', '/courses/digital-literacy-2/activities/resource-finder-agent-fixed.html')

A_ROUNDS = [
    rnd('Baseline first', 'Edge · version 1',
        ['Search library, LIBRARY, learning, community, then zzz.',
         'Write how many resources each search finds.',
         'Circle the search the change must fix.'],
        'Done early? Find one word from a description that finds exactly one resource.',
        'Version 1 finds 1, 1, 0, 2 and 0. Learning finds nothing because version 1 searches names and descriptions, not '
        'categories. That is the change the spec asks for. Capital letters already match, so LIBRARY must keep finding 1.',
        tasks=['Search version 1 for library, LIBRARY, learning, community and zzz. Write each count and circle the search '
               'the change must fix.'],
        key=['library 1, LIBRARY 1, learning 0, community 2, zzz 0. The change must fix learning, which should find the two '
             'Learning resources.'], links=(V1,)),
    rnd('Rescue the vague request', 'Worksheet · three vague requests',
        ['Read three vague requests for the agent.',
         'Say what is missing from each.',
         'Rewrite one as one change plus two things to keep.'],
        'Done early? Add a last line asking the agent to show its plan first.',
        'Vague requests invite the agent to guess, and guesses touch things you did not ask about. A useful request '
        'names one change, who it helps, what must stay the same, and how you will check it.',
        paper=table(['Vague request', 'What is missing?'],
                    [['Make it better.', ''], ['Fix the search.', ''], ['Add categories and make it look modern.', '']]),
        tasks=['Say what is missing from each request in the table, then rewrite one as one change plus two things that must '
               'stay the same.'],
        key=['Make it better: no change named. Fix the search: no problem described and nothing to keep. Add categories and '
             'make it look modern: two changes, and modern invites redesign. A good rewrite: let the search box find '
             'resources by category; keep capital letters matching and keep the no-match message.']),
    rnd('Can a stranger run it?', 'Worksheet · six candidate checks',
        ['Read six candidate checks.',
         'Mark each: a stranger could run it, or not.',
         'Rewrite two so anyone could run them.'],
        'Done early? Write one check for something that already works and must not break.',
        'A good check says what to type or press and what to expect: I type learning, I expect 2 resources. "It works" '
        'and "looks good" cannot be run by someone else.',
        paper=table(['Candidate check', 'Runnable or not?'],
                    [['It works.', ''], ['I type learning, I expect 2 resources.', ''], ['The search looks good.', ''],
                     ['I type zzz, I expect No matching resources.', ''], ['Categories are better now.', ''],
                     ['I press Tab, I expect a thick outline on the search box.', '']]),
        tasks=['Mark each check in the table runnable or not, then rewrite two so anyone could run them.'],
        key=['Runnable: learning expects 2; zzz expects the no-match message; Tab expects a thick outline. Not runnable: It '
             'works; The search looks good; Categories are better now. Rewrites name an input and an expected result.']),
]

B_ROUNDS = [
    rnd('Count it yourself', 'Edge · Ctrl+U on version 2',
        ['Open the agent\u2019s version. Press Ctrl and U to see its code.',
         'Press Ctrl and F and type toLowerCase. Count the matches.',
         'Do the same on version 1. Which line changed?'],
        'Done early? Find the line that adds category to the search.',
        'Version 2 has one toLowerCase and version 1 has two. The missing one is on the line that reads the search box, '
        'so capital letters stop matching. Ctrl and U shows the code but cannot change it.',
        tasks=['Count toLowerCase in versions 1 and 2 with Ctrl and U, then Ctrl and F, and write which line changed.'],
        key=['Version 1: 2 matches. Version 2: 1 match. The search line lost .toLowerCase(), so the typed search is no longer '
             'turned to small letters.'], links=(V2, V1)),
    rnd('Scope creep', 'Worksheet · a new fictional change',
        ['Read the fictional request and the agent\u2019s four changes.',
         'Mark each change: asked for, or not asked for.',
         'Decide: approve, or send it back with a reason.'],
        'Done early? Write the sentence you would send back to the agent.',
        'Only the bold count was asked for. A renamed button is unrequested but small; a removed no-match message breaks '
        'something that worked; a new outside script adds code from somewhere else. Send it back.',
        paper=quote('Fictional request', 'Show the number of matching resources in bold. Change nothing else.')
              + table(['Agent\u2019s change', 'Asked for or not?'],
                      [['The count is now bold.', ''], ['The Reset button now says Clear.', ''],
                       ['The no-match message was removed.', ''], ['A script from an outside website was added.', '']]),
        tasks=['Mark each of the agent\u2019s changes in the table asked for or not, then decide whether to approve it.'],
        key=['Asked for: the bold count. Not asked for: the renamed button, the removed no-match message (a regression) and '
             'the outside script (code from somewhere else). Send it back: keep only the bold count.']),
    rnd('Approve this plan?', 'Worksheet · two fictional plans',
        ['Read two plans an agent might show before it starts.',
         'Choose the plan you would approve.',
         'Say what is wrong with the other one.'],
        'Done early? Answer an agent that says Done. All checks pass. What do you do?',
        'A good plan names one file, the one rule it will change and the checks. A plan that rewrites the page or adds '
        'sign-in goes far beyond the request. "All checks pass" from the agent is a claim; run the checks yourself.',
        paper=table(['Plan', 'Approve?'],
                    [['Plan 1: change one line in resource-finder.html so the search also looks at the category. Then run '
                      'learning, LIBRARY and zzz.', ''],
                     ['Plan 2: rewrite the whole page with a new design, add a sign-in screen, and save searches.', '']]),
        tasks=['Choose the plan you would approve and say what is wrong with the other one.'],
        key=['Approve Plan 1: one file, one rule, and checks. Plan 2 rewrites everything and adds sign-in nobody asked for. '
             'If an agent says all checks pass, run them yourself.']),
]

C_ROUNDS = [
    rnd('Hunt the capitals', 'Edge · version 2',
        ['Predict, then search version 2 for Library, Community and Practice.',
         'Write what each finds.',
         'State the rule you discovered.'],
        'Done early? Choose Category Learning and search library. What is found?',
        'In version 2 every search with a capital letter finds nothing, because the typed text is no longer turned to '
        'small letters. With Category Learning and library, Community library is found: the filter still works.',
        tasks=['Search version 2 for Library, Community and Practice, write what each finds, and state the rule.'],
        key=['Library, Community and Practice all find nothing in version 2. Rule: any capital letter breaks the search. '
             'Category Learning with library finds Community library.'], links=(V2,)),
    rnd('Report it so it can be fixed', 'Worksheet · three weak bug reports',
        ['Read three weak bug reports.',
         'Say what each is missing: steps, expected, actual, or what to keep.',
         'Rewrite one completely.'],
        'Done early? Add one line telling the agent what must not change.',
        'A useful report lets a stranger see the bug: the steps, what you expected, what happened, and what must stay the '
        'same. "It is broken" gives nothing to act on.',
        paper=table(['Bug report', 'What is missing?'],
                    [['It is broken.', ''], ['Search does not work sometimes.', ''],
                     ['I typed LIBRARY and got nothing.', '']]),
        tasks=['Say what each bug report in the table is missing, then rewrite one with steps, expected, actual and what to '
               'keep.'],
        key=['It is broken: everything. Search does not work sometimes: the steps and the input. I typed LIBRARY and got '
             'nothing: the expected result and what to keep. A full report: open version 2, type LIBRARY; expected '
             'Community library, as in version 1; actual: no matches; keep the category search.']),
    rnd('Retest plus one', 'Edge · version 3',
        ['Open the repaired version. Repeat the check that failed.',
         'Repeat two checks that passed before.',
         'Add one new check: Community.'],
        'Done early? Try the optional hand repair on your worksheet.',
        'Version 3 finds LIBRARY (1), learning and Learning (2), zzz (0) and Community (2). A repair is only accepted when '
        'the failed check passes and nothing that worked before broke.',
        tasks=['On version 3, repeat the failed check, two checks that passed before, and Community. Write each result.'],
        key=['LIBRARY 1, Learning 2, learning 2, zzz no matches, Community 2. Accept the repair: the failed check passes and '
             'nothing that worked before broke.'], links=(V3,)),
]

D_ROUNDS = [
    rnd('Local or hosted?', 'Edge · version 1, downloaded and online',
        ['Download version 1 from your worksheet and open the file.',
         'Compare its address with the course copy\u2019s address.',
         'Who else could open each one?'],
        'Done early? Say why the Text size button does not appear in the downloaded copy.',
        'The downloaded copy opens from file:///C:/Users/... and only this computer can see it. The course copy is hosted '
        'on vublessons.com, so anyone with the address can open it. The downloaded copy cannot load the course\'s shared '
        'files, which is why the Text size button disappears.',
        tasks=['Open the downloaded version 1 and the course copy, compare their addresses, and say who else could open each.'],
        key=['The downloaded copy starts with file:/// and only this computer can open it. The course copy is hosted at '
             'vublessons.com and anyone with the address can open it.'], links=(V1,)),
    rnd('What can a visitor see?', 'Edge · Ctrl+U on version 2',
        ['Open the agent\u2019s version and press Ctrl and U.',
         'Find the list of resources and the matching rule.',
         'Would a secret key pasted here be safe?'],
        'Done early? Say where a secret key should live instead.',
        'Everything in the page\'s code is visible to every visitor, including data and rules. A secret key pasted there '
        'could be copied and used, and the owner would pay the bill. Secret keys belong on the server.',
        tasks=['Find the resource list and the matching rule with Ctrl and U, and say whether a secret key in the page would '
               'be safe.'],
        key=['The resource list and the matching rule are both visible. A secret key in the page would be visible too, so '
             'anyone could copy it. It belongs on the server, never in the page.'], links=(V2,)),
    rnd('Roadblock cards', 'Worksheet · six things that go wrong',
        ['Read six things that can go wrong with a real website.',
         'Name the roadblock each one belongs to.',
         'Say who would have to fix it.'],
        'Done early? Pick the roadblock you think costs the most, and say why.',
        'Address: a domain name is rented each year. Home: hosting costs money and must be paid. Memory: saving for many '
        'people needs a back end and a database. Front door: sign-in must be checked on the server. Keys: secret keys stay '
        'on the server. Caretaker: someone updates, backs up, helps users and reviews every agent change.',
        paper=table(['What went wrong', 'Roadblock', 'Who fixes it?'],
                    [['Nobody renewed the web address, and the site vanished.', '', ''],
                     ['The hosting bill was not paid.', '', ''],
                     ['Saved favorites only exist in one person\'s browser.', '', ''],
                     ['The sign-in box is a picture; nothing checks the password.', '', ''],
                     ['A secret key was pasted into the page code.', '', ''],
                     ['An agent changed the site and nobody reviewed it.', '', '']]),
        tasks=['Name the roadblock and who fixes it for each problem in the table.'],
        key=['Address (domain name): the owner renews it. Home (hosting): the owner pays. Memory (back end and database): a '
             'developer builds shared storage. Front door (sign-in): the server must check it. Keys: move the key to the '
             'server and replace it. Caretaker: someone must review every change before it goes live.']),
]

WEEK6 = dict(
    title='Guide an agent. Test its work.', photo='app-planning',
    warm='When you ask someone to repair something, how do you describe success? Apply that same care to an AI agent.',
    apply='Explain the bug, the repair and one responsibility you would keep if this app served real people.',
    minutes=[30, 5, 18, 20, 18, 15, 7, 7], nobreak=True, practice_pages=True, video_pauses=True,
    plan_note='<p>Week 6 is the extension week. Learners need no AI account: the three prepared versions of the resource '
              'finder are the evidence, and version 2 keeps its planted defect. An instructor-led live agent run is '
              'optional. The video stops at pause cards; at each one, pause and let learners do the worksheet task the '
              'card names. Mission 6D teaches the six roadblocks between a page on your computer and a real service. If '
              'the room is slow, skip every Done early line, then Round 4 of Mission 6A, then Round 4 of Mission 6B. Keep '
              'the retest and the rubric.</p>',
    missions=[
        mission('Specify the change', 'Edge · version 1 · worksheet spec', 'Version 1 searches names and descriptions',
                'A precise category-search request',
                ['Name the user, the task and the expected result.', 'Say what must stay the same.',
                 'Write checks before you ask for a change.'],
                [('Baseline', 'Version 1: library 1 · LIBRARY 1 · learning 0',
                  'Read what already works before asking for anything. All resources are fictional.'),
                 ('Specify', 'Search categories too; keep capital letters matching',
                  'One change, who it helps, and what must stay the same. Ask for a plan first.'),
                 ('Predict', 'learning → 2 · LIBRARY → 1 · zzz → 0',
                  'Write the checks before the agent runs. No sign-in, real data, secret keys or outside code.')],
                ['Search version 1 and write what it finds.', 'Write a spec with one change and two things to keep.',
                 'Write three checks a partner could run.'],
                'Which request gives an agent a testable target?',
                ['Improve everything', 'Search categories too; keep capitals matching', 'Make it impressive'], 1,
                'One bounded change with checks lets you compare the result against the request.', [0, 1], 7, A_ROUNDS),
        mission('Review the proposed change', 'Mission 6B practice page · the diff', 'The agent returns version 2',
                'Asked-for changes separated from regressions',
                ['A diff shows each removed and added line.', 'Read the changed lines before you trust them.',
                 'An unrequested change needs a test.'],
                [('Requested', '+ r.category in the search',
                  'Adding category to the searched fields meets the request. The hint text also changed.'),
                 ('Unexpected', '− .toLowerCase() on the search line',
                  'The agent removed the step that ignores capital letters. Do not assume it is harmless.'),
                 ('Predict', 'LIBRARY may now find nothing',
                  'Mark requested and unrequested changes, then test your prediction.')],
                ['Predict the change, then compare with the agent\u2019s plan.', 'Read the diff on the practice page.',
                 'Mark each changed line asked for or not.'],
                'The agent removed the step that ignores capital letters. What should you do?',
                ['Ignore it, because the page looks right', 'Delete the whole app', 'Test a search with capitals'], 2,
                'A page can look right while its search breaks. Test the prediction.', [2, 3], 10, B_ROUNDS),
        mission('Test, report, repair, retest', 'Edge · versions 2 and 3', 'A plausible app with a planted defect',
                'A repair backed by repeatable evidence',
                ['Record what you expected and what happened.', 'Report the steps, the input and the failure.',
                 'Retest the failure and the checks that passed.'],
                [('Test', 'Version 2: learning 2 · LIBRARY 0',
                  'Run the happy path, no match, mixed case, keyboard and a narrow window.'),
                 ('Report', 'Expected 1 for LIBRARY; got no matches',
                  'Ask the agent to make capital letters match again and keep the category search.'),
                 ('Retest', 'Version 3: LIBRARY 1 · Learning 2 · zzz 0',
                  'Repeat the earlier checks too. Fixing one bug can break something else.')],
                ['Run the five checks on version 2.', 'Write a repair request a stranger could follow.',
                 'Retest on version 3 and decide.'],
                'The repaired app finds LIBRARY. Are you finished testing?',
                ['Yes, the one bug is fixed', 'No, repeat the checks that passed before', 'Only change the colors'], 1,
                'Retest the earlier checks too, so the repair does not hide a new break.', [4, 5, 6], None, C_ROUNDS,
                links=(V2, V3)),
        mission('Know what \u201cready\u201d means', 'Worksheet · the six roadblocks', 'A page on your computer',
                'A clear picture of what a real service needs',
                ['A page on your computer is not a service.', 'Sign-in, saved data and keys need a server.',
                 'Someone must pay, update and support it.'],
                [('Address', 'Domain name · hosting',
                  'Miss the renewal and the site vanishes. Once hosted, anyone with the address can open it.'),
                 ('Server', 'Back end: data · sign-in · keys',
                  'A page cannot remember for everyone or check a password. Secret keys never go in page code.'),
                 ('Caretaker', 'Pay · update · back up · review',
                  'Someone pays, fixes, helps users and reviews every agent change before it goes live.')],
                ['Plan the finder as a real service, roadblock by roadblock.', 'Name an owner for each roadblock.',
                 'Score your work with the 8-point rubric.'],
                'Where does a secret API key belong in a real app?',
                ['In the page\u2019s HTML', 'In a screenshot in the help page', 'On the server, out of the page code'], 2,
                'Anyone can read a page\u2019s code with Ctrl and U. Secret keys and sign-in checks belong on the server.',
                [7], None, D_ROUNDS),
    ])
