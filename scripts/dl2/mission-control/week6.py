"""Mission Control Week 6, guided build: test a practice page, guide an AI agent's change, retest, then review the course and take the post-test.

Same brief as Weeks 3 and 4 (Britt, 2026-10-23): the whole class goes slide by slide in Microsoft Edge, nobody needs an
AI account (the agent's work is pre-built as three versions of one practice page), and nobody works alone until the
post-test itself, which is a test.

  Part 1  Version 1 as it is: write checks, search together, write each result in a test table
  Part 2  The request: type a given request, then predict the new results
  Part 3  Version 2, the agent's change: one change was asked for, one was not; search, then write a bug report
  Part 4  Version 3, the repair: rerun every check, Tab through the controls, zoom in; why a practice app is not a real service
  Then    wrap-up evidence (My result page), a course review of weeks 1 to 5 (20 questions, one per post-test item,
          each a new scenario), and the post-test.

Cut on purpose: the website / web app / SaaS lecture, the HTML / CSS / JavaScript lecture, where data lives, secrets in
browser code as its own lesson, downloading editable HTML and hand repair in a text editor, and the 8-point extension
rubric (the My result page replaces it). Week 6 has no post-test item of its own: its goals are practice only.

The three pages are courses/digital-literacy-2/activities/resource-finder.html (version 1), -agent.html (version 2) and
-agent-fixed.html (version 3). Real results: library finds 1; learning finds none in version 1 and 2 in versions 2 and 3;
zzz finds none; LIBRARY finds 1 in versions 1 and 3 and none in version 2.

Inline markup in text (rendered by guided.py): [Label] on-screen name · {Key} keyboard key · «text» exact text.
"""
from week3 import step

APPS = {
    'edge': 'Microsoft Edge',
    'word': 'Microsoft Word',
    'excel': 'Microsoft Excel',
    'powerpoint': 'Microsoft PowerPoint',
    'explorer': 'File Explorer',
    'mail': 'Practice Mail',
    'settings': 'Windows Settings',
    'outlook': 'Outlook Calendar',
}

COURSE_TITLE = 'Guide an AI agent to improve a web app'
ACT = '/courses/digital-literacy-2/activities'
NONE = 'No matching resources. Try a different word or reset the filters.'
REQUEST = ['Please change only this file.', 'Let people search the category too.', 'Keep searches working in any letter case.', 'Keep the message for no matches.']
REPAIR = ['LIBRARY finds nothing, but library finds Community library.', 'Make both find the same entry.', 'Keep the category search.', 'Change only this file.']
SEARCHES = ('library', 'learning', 'zzz', 'LIBRARY')

GOALS = [
    dict(app='edge', text='Write checks first, then test a web page with them and write down what you really saw.', short='Test a page with written checks', item=None),
    dict(app='edge', text='Write a request for an AI agent that says what to change and what must stay the same.', short='Write a request an AI agent can follow', item=None),
    dict(app='edge', text='Find a change nobody asked for, and report it as a bug with steps, what you typed, what you expected and what happened.', short='Report a change nobody asked for', item=None),
    dict(app='edge', text='Retest a repair: run the new check and the checks that passed before.', short='Retest a repair, not just the fix', item=None),
]

OUTCOMES = [
    'Checks: in Edge, each learner opens version 1, searches library, learning, zzz and LIBRARY, and writes what they saw on the test table (1 found, none found, none found, 1 found).',
    'Request: each learner types the four-line request on the worksheet and writes a guess for each of the four searches in the new version.',
    'Bug report: each learner opens version 2, sees learning find 2 and LIBRARY find none, and writes a bug report with the steps, what they typed, what they expected and what happened.',
    'Retest: each learner opens version 3, reruns all four searches (1, 2, none, 1), tabs through the controls, zooms in, and fills in the My result page.',
]

WORDS = [
    ('Tab', 'One of the page names along the top of Edge. Click a tab to switch pages.'),
    ('Address bar', 'The long box at the top of Edge where you type a website name.'),
    ('Check', 'A test you can run: type this, and you expect to see that.'),
    ('AI agent', 'A program that changes a file for you when you ask it to.'),
    ('Request', 'The words you give an AI agent. It says what to change and what must stay the same.'),
    ('Version', 'One saved copy of the page. Version 2 is the agent’s change. Version 3 is the repair.'),
    ('Bug', 'Something that does not work the way it should.'),
    ('Bug report', 'A short note that lets someone else see the bug: the steps, what you typed, what you expected, what happened.'),
    ('Retest', 'Run the checks again after a change, the old ones as well as the new one.'),
    ('Focus ring', 'The thick outline that shows which control the keyboard is on.'),
]


def table(pid, head):
    """The worksheet test table: one typed box per search, kept when printed."""
    rows = ''.join(
        f'<tr><th scope="row">{q}</th><td><label class="visually-hidden" for="{pid}-{i}">{head}, search {q}</label>'
        f'<textarea class="worksheet-input" id="{pid}-{i}" rows="2"></textarea><span class="print-answer"></span></td></tr>'
        for i, q in enumerate(SEARCHES))
    return (f'<div class="table-scroll" tabindex="0" role="region" aria-label="{head}"><table class="g-testtable"><thead><tr><th scope="col">Search for</th>'
            f'<th scope="col">{head}</th></tr></thead><tbody>{rows}</tbody></table></div>')


def open_button(file, label, note):
    return (f'<p class="g-download"><a class="g-download-button" href="{ACT}/{file}" target="_blank" rel="noopener">{label}</a> <span>{note}</span></p>')


def fd(version, query='', **kw):
    return ('finder_page', dict(version=version, query=query, **kw))


def tb(part, filled, key):
    return ('finder_table', dict(part=part, filled=filled, targets=[key]))


# ---------------------------------------------------------------- Before we start (Edge)
READY = dict(
    title='Open this worksheet on your computer', app='edge',
    what='It has every step from tonight, a box to check for each one, links to the practice pages, a test table, and a My result page at the end. If you have a printed copy, open it on screen too.',
    steps=[
        step('Find the taskbar', ['Look at the bottom of your screen. The long dark bar there is the [taskbar].'],
             'the taskbar, with a round [Edge] icon on it.', ('taskbar', dict(targets=[])), app='edge',
             stuck=('Cannot see the taskbar?', 'Move the mouse pointer to the very bottom of the screen. The bar appears.'),
             notes='Point to the taskbar on the projector. Every screen should show the same bar along the bottom.'),
        step('Open Microsoft Edge', ['Click the round blue-green [Edge] icon on the taskbar.'],
             'a window with a long address bar at the top. This is [Microsoft Edge].', ('taskbar', dict(targets=['edge'])), app='edge',
             stuck=('No Edge icon on the taskbar?', 'Press the {Windows} key, type «Edge» and press {Enter}.'),
             notes='Wait until every screen shows the Edge window.'),
        step('Go to the course website', ['Click the long address bar at the top of Edge.', 'Type «vublessons.com» and press {Enter}.'],
             'the VUB Learning page with course cards.', ('vub_course_path', dict(week=6, week_title=COURSE_TITLE)), app='edge',
             stuck=('Typed it in a search box and got a list of results?', 'Click the long bar at the very top of Edge, press {Ctrl} and {A}, and type it again.'),
             notes='If the browser opens to another page, the address bar is still the long box at the top.'),
        step('Open the course', ['On the [Digital Literacy — Level 2] card, click [Open course].'],
             'a page that lists the weeks of the course.', ('vub_course_path', dict(week=6, week_title=COURSE_TITLE)), app='edge',
             stuck=('Cannot find the card?', 'Roll the mouse wheel toward you to scroll down. The cards are in a row.'),
             notes='Walk the room until every screen shows the course page.'),
        step('Open your Week 6 worksheet', ['Roll the mouse wheel toward you until you see [Week 6].', 'Click [Worksheet] in the Week 6 row.'],
             'a page titled [Week 6 · Worksheet]. Leave it open. You will come back to it.', ('vub_course_path', dict(week=6, week_title=COURSE_TITLE)), app='edge',
             stuck=('Cannot find Week 6?', 'The weeks are in order. Keep rolling the wheel toward you.'),
             notes='The worksheet tab stays open all night. It holds the links to the three versions of the page, your test tables and your result page.'),
    ])


# ---------------------------------------------------------------- Part 1: version 1 (Edge)
P1_MAP = dict(title='Find your way around the page', draw=fd(1, targets=['search', 'category', 'reset', 'status']),
              items=['[Search fictional resources]: type here.', '[Category]: one kind of entry, or all.', '[Reset filters]: clears everything.', 'The line below says how many were found.'],
              notes='Point to each part on the projector. Every entry on this page is made up. The page sends nothing anywhere and has no sign-in.')


def pair(tag, query, part, filled, find, first=False):
    """Search once, then write the result in the test table. Two steps, so the class moves together."""
    click = ['Click the [Search fictional resources] box.'] if first else ['Click the finder tab, then click [Reset filters].']
    out = []
    if first:
        out.append(step('Click the search box', click, 'a blinking line in the search box.', fd(part[0], targets=['search']), app='edge',
                        stuck=('Cannot find the search box?', 'It is the long white box under the words Search fictional resources.'),
                        notes='Click first, then type. The blinking line shows where typing goes.'))
        acts = [f'Type «{query}»']
    else:
        acts = click + [f'Type «{query}»']
    out.append(step(f'Search for {query}', acts, find, fd(part[0], query, targets=part[1]), app='edge',
                    stuck=('The old word is still there?', 'Click [Reset filters] first. It clears the box and puts the blinking line back in it.'),
                    notes=part[2]))
    out.append(step(f'Write the {query} result', ['Click the [Week 6 · Worksheet] tab.', f'In your test table, write what you saw on the [{query}] row.'],
                    f'your note on the [{query}] row, for example «{part[3]}».', tb(part[4], filled, query), app='edge',
                    stuck=('Cannot find the test table?', 'Roll the mouse wheel toward you. The table is near the top of the part.'),
                    notes='Short notes are fine: 1 found, none found. Walk the room and read a few.'))
    return out


def p1(query, filled, find, note, first=False, targets=('status',)):
    return pair('v1', query, (1, list(targets), note, 'none found' if 'No matching' in find else '1 found', 1), filled, find, first)


PART1 = dict(
    app='edge', title='Test the page before you change it', goals=[0],
    what='Microsoft Edge shows web pages. Tonight we use one practice page, a made-up list of community resources with a search box. It runs on your computer. Nothing you type leaves the page.',
    make='a test table with what version 1 really did for four searches.',
    start='A practice page you have not tested yet.',
    finish='A test table with a note on each of the four rows: library, learning, zzz and LIBRARY.',
    open_note='Everyone opens the practice page from the worksheet in a moment. No AI account is needed tonight.',
    worksheet_extra=(open_button('resource-finder.html', 'Open version 1', 'It opens in a new tab. Nothing you type is sent anywhere.')
                     + '<p><b>My test table.</b> Write what you see after each search. Short notes are fine.</p>' + table('t1', 'What I saw in version 1')),
    tell=dict(title='Write the checks. Then test.',
              points=['A [check] says what to type and what you expect to see.', 'Write your checks before you ask for any change. Then you can tell if a change helped or hurt.',
                      'What you see on the screen is the evidence. A confident answer from an AI is not.'],
              notes='Ask: how do you check that a repair worked, like a fixed faucet? You turn it on. A check is the same idea. Tonight the checks are four searches.'),
    watch=[dict(title='Watch: write checks before asking for code', start=131.95, end=168.19, look='checks that a stranger could carry out without guessing.',
                notes='Plays 2:12 to 2:48 and stops on its own. It ends before the video asks learners to pause and write three checks of their own.')],
    steps=[
        step('Find Part 1 on your worksheet', ['Click the [Week 6 · Worksheet] tab at the top of Edge.', 'Roll the mouse wheel toward you until you see [Part 1].'],
             'the heading [Part 1 of 4], a gold button named [Open version 1], and a table named [My test table].', ('edge_worksheet_link', dict(week=6, part='Part 1', label='Open version 1')), app='edge',
             stuck=('Cannot find the worksheet tab?', 'Look at the tabs along the top of Edge. The one named Week 6 · Worksheet has the links.'),
             notes='Everyone should be looking at the gold button before you move on.'),
        step('Open version 1', ['Click the gold button [Open version 1].'],
             'a new tab named [Fictional community resource finder] with a search box. This is the finder tab.', fd(1, targets=['search']), app='edge',
             stuck=('Nothing happened?', 'Look at the tabs along the top of Edge. The new tab may be on the right. Click it.'),
             notes='The worksheet stays open in its own tab. The finder opens beside it. Call this tab the finder tab all night.', opener=True),
        dict(kind='map', **P1_MAP),
        step('Read the list', ['Look at the entries under the search box.'],
             'three entries and the line [3 fictional resources found.]', fd(1, targets=['results', 'status']), app='edge',
             notes='With nothing typed, the page shows every entry.'),
    ] + p1('library', 1, 'one entry, [Community library], and the line [1 fictional resource found.]', 'Version 1 searches the name and the description of each entry.', first=True, targets=('results',))
      + p1('learning', 2, 'the line [No matching resources. Try a different word or reset the filters.]', 'Learning is a category. Version 1 does not search categories, so it finds nothing. This is what we will ask to change.')
      + p1('zzz', 3, 'the same line, [No matching resources. Try a different word or reset the filters.]', 'A good page says clearly when nothing matches. It does not look broken.')
      + p1('LIBRARY', 4, 'one entry, [Community library], and the line [1 fictional resource found.]', 'Capital letters work in version 1. Remember this: it matters in Part 3.', targets=('results',)),
    stuck=[('Cannot find the gold button?', 'Click the [Week 6 · Worksheet] tab, then roll the mouse wheel toward you until you see Part 1.'),
           ('The result looks different?', 'Click [Reset filters], then type the word again.'),
           ('Closed the finder tab by mistake?', 'Click the [Week 6 · Worksheet] tab and click [Open version 1] again.')],
    check=dict(question='Which check can a partner run without guessing?',
               choices=['The page should feel friendly', 'Type zzz. The page says no entries match.', 'The search should be good'], answer=1,
               why='It says what to type and what you expect to see.'),
)

# ---------------------------------------------------------------- Part 2: the request
PART2 = dict(
    app='edge', still=True, title='Ask for one change, with limits', goals=[1],
    what='An AI agent can change a page for you. It does better when you say what to change and what must stay the same.',
    make='a four-line request, and a guess for each of the four searches.',
    start='Version 1, tested. The page cannot search categories.',
    finish='A request in the My request box, and a written guess for library, learning, zzz and LIBRARY.',
    open_note='We stay in Edge. The AI agent’s work is already prepared, so nobody needs an AI account.',
    tell=dict(title='One change. Say what must stay the same.',
              points=['Ask for [one change]. A big wish like [make it better] cannot be tested.', 'Say what must [stay the same]. Without that, the agent may change things you did not ask for.',
                      'Say where it may work: [change only this file].'],
              notes='Ask: if you asked a contractor to fix one door, what would you say about the rest of the house? The same care applies to an AI agent.'),
    watch=[dict(title='Watch: give the AI a bounded, useful request', start=180.94, end=226.91, look='a request that names the task, the limits and the checks.',
                notes='Plays 3:01 to 3:47 and stops on its own. It includes the video’s one-line reminder not to put passwords into a prompt.')],
    steps=[
        step('Find Part 2 on your worksheet', ['Click the [Week 6 · Worksheet] tab at the top of Edge.', 'Roll the mouse wheel toward you until you see [Part 2].'],
             'the heading [Part 2 of 4] and a large box named [My request].', ('request_box', dict(targets=['box'])), app='edge',
             stuck=('Cannot find Part 2?', 'Roll the mouse wheel toward you. Part 2 comes after the Part 1 test table.'),
             notes='Everyone should see the My request box before you move on.'),
        step('Read the request', ['Read the four lines on the slide.'],
             'four short lines: one change, a limit on where, and two things that must stay the same.', None, card=REQUEST, card_head='The request:', app='edge',
             notes='Point out each line. Line 1 says where. Line 2 is the one change. Lines 3 and 4 are what must stay the same.'),
        step('Type the request', ['Click the [My request] box on your worksheet.', 'Type the four lines. Press {Enter} after each line.'],
             'your four lines in the [My request] box.', None, card=REQUEST, card_head='Type these lines:', write='My request:', write_rows=5, app='edge',
             stuck=('Made a typing mistake?', 'Press {Backspace} to erase the letter before the blinking line, then type it again.'),
             notes='Learners type the same four lines. Spelling does not need to be perfect.'),
    ] + [
        step(f'Guess: {q}', [f'Write what you think will happen when you search for [{q}] in the new version.'],
             'your guess in the box. There are no wrong guesses yet.', None,
             write=f'Search «{q}» in the new version. I expect to see:', write_head='Your guess (worksheet, Part 2):', write_rows=2, app='edge',
             notes=f'Take a few guesses aloud before moving on. In the pre-built version 2, {note}')
        for q, note in zip(SEARCHES, ['library finds 1 entry.', 'learning finds 2 entries.', 'zzz finds none.', 'LIBRARY finds none: the agent dropped a step. Do not say so yet.'])
    ],
    stuck=[('Cannot find the My request box?', 'Click the [Week 6 · Worksheet] tab, then roll the mouse wheel toward you until you see Part 2.'),
           ('Made a typing mistake?', 'Press {Backspace} to erase the letter before the blinking line.'),
           ('Not sure what to guess?', 'Say it simply: found one, found two, or found nothing.')],
    check=dict(question='Which line of the request keeps the page from losing something it already does?',
               choices=['Make the page better.', 'Keep searches working in any letter case.', 'Add anything you like.'], answer=1,
               why='It names a behavior that must stay the same, and you can test it.'),
)

# ---------------------------------------------------------------- Part 3: version 2
def bug(title, head, prompt, see):
    return step(title, ['Write it in your bug report.'], see, None, write=prompt, write_head=head, write_rows=2, app='edge',
                notes='Walk the room. A good report lets someone else see the same thing.')


PART3 = dict(
    app='edge', still=True, title='Check the agent’s change', goals=[2],
    what='The agent has made its change. It is saved as version 2. A change can fix what you asked for and break something else.',
    make='a bug report about one thing that stopped working.',
    start='Your guesses from Part 2, and version 2 of the page.',
    finish='A test table for version 2 and a bug report with four parts: steps, what you typed, what you expected, what happened.',
    open_note='We stay in Edge. Version 2 opens in a new tab.',
    worksheet_extra=(open_button('resource-finder-agent.html', 'Open version 2', 'It opens in a new tab. It is the agent’s change.')
                     + '<p><b>My test table.</b> Write what you see after each search in version 2.</p>' + table('t3', 'What I saw in version 2')),
    tell=dict(title='A change can break what used to work.',
              points=['Check the change you [asked for]. Then check what [used to work].', 'The page can look the same and still behave differently.',
                      'A bug report gives the [steps], what you [typed], what you [expected] and what [happened].'],
              notes='Ask: has an update ever changed something you did not ask it to change? The page looked fine, and the harm was in what it did.'),
    watch=[dict(title='Watch: test the happy path and the missing result', start=276.83, end=321.63, look='a search that works, a search that finds nothing, and the same word in capital letters.',
                notes='Plays 4:37 to 5:22 and stops on its own. It ends before the keyboard and narrow-window checks, which we do in Part 4.')],
    steps=[
        step('Find Part 3 on your worksheet', ['Click the [Week 6 · Worksheet] tab at the top of Edge.', 'Roll the mouse wheel toward you until you see [Part 3].'],
             'the heading [Part 3 of 4], a gold button named [Open version 2], and a table named [My test table].', ('edge_worksheet_link', dict(week=6, part='Part 3', label='Open version 2')), app='edge',
             stuck=('Cannot find Part 3?', 'Roll the mouse wheel toward you. Part 3 comes after Part 2.'),
             notes='Everyone should be looking at the gold button before you move on.'),
        step('Open version 2', ['Click the gold button [Open version 2].'],
             'a new tab whose name ends in [version 2 (agent result)].', fd(2, targets=['search']), app='edge',
             stuck=('Nothing happened?', 'Look at the tabs along the top of Edge. The new tab may be on the right. Click it.'),
             notes='Version 2 is the pre-built result of the request. Call this tab the finder tab now.', opener=True),
        step('See the change you asked for', ['Look at the two lines on the slide.'],
             'the words [r.category] added to the After line. The agent did what you asked: category is now searched.', ('agent_change', dict(which='asked')), app='edge',
             notes='These lines come from the real pages. Nobody has to read code. Point to the added word, category, and the plus sign.'),
        step('See the change nobody asked for', ['Look at the two lines on the slide.'],
             'the part that turns capital letters into small letters is missing from the After line. Nobody asked for this.', ('agent_change', dict(which='unasked')), app='edge',
             notes='The agent also removed a step. Ask: what do you predict will happen with capital letters? Take a few guesses before testing.'),
        step('Click the search box', ['Click the [Search fictional resources] box.'],
             'a blinking line in the search box.', fd(2, targets=['search']), app='edge',
             stuck=('Cannot find the search box?', 'It is the long white box under the words Search fictional resources.'),
             notes='Click first, then type.'),
    ] + [
        s for q, filled, find, note, tg in [
            ('library', 1, 'one entry, [Community library], and the line [1 fictional resource found.]', 'The happy path: the search that worked before still works.', ('results',)),
            ('learning', 2, 'two entries, [Community library] and [Practice Workbook Workshop]. The new search works.', 'This is the change you asked for. Learning is a category, and now it is searched.', ('results',)),
            ('zzz', 3, 'the line [No matching resources. Try a different word or reset the filters.]', 'The no-match message still works.', ('status',)),
            ('LIBRARY', 4, 'the line [No matching resources. Try a different word or reset the filters.] Version 1 found an entry here.', 'The bug. Version 1 found Community library for LIBRARY. Version 2 finds nothing. Ask who predicted it.', ('status',)),
        ] for s in pair('v2', q, (2, list(tg), note, 'none found' if 'No matching' in find else ('2 found' if q == 'learning' else '1 found'), 3), filled, find, False)
    ] + [
        bug('Bug report: the steps', 'Your bug report (worksheet, Part 3):', 'Bug report, the steps I took:', 'your steps, for example: opened version 2 and typed in the search box.'),
        bug('Bug report: what you typed', 'Your bug report (worksheet, Part 3):', 'Bug report, what I typed:', 'the exact word you typed, in capital letters.'),
        bug('Bug report: what you expected', 'Your bug report (worksheet, Part 3):', 'Bug report, what I expected:', 'what version 1 did with the same word.'),
        bug('Bug report: what happened', 'Your bug report (worksheet, Part 3):', 'Bug report, what happened:', 'the message you saw instead.'),
    ],
    stuck=[('Cannot find the gold button?', 'Click the [Week 6 · Worksheet] tab, then roll the mouse wheel toward you until you see Part 3.'),
           ('Opened version 1 by mistake?', 'The tab name ends in version 2 (agent result) for the agent’s change. Click that tab, or click [Open version 2] again.'),
           ('Not sure what to write in the report?', 'Four short answers: what I did, what I typed, what I expected, what happened.')],
    check=dict(question='The agent added category search, and the page looks the same. What next?',
               choices=['Trust it, because the page looks the same', 'Test the old searches too, not only the new one', 'Delete the page'], answer=1,
               why='A page can look the same and behave differently. Run the old checks as well as the new one.'),
)

# ---------------------------------------------------------------- Part 4: version 3
def tab_step(title, acts, see, focus):
    return step(title, acts, see, fd(3, 'LIBRARY', focus=focus), app='edge',
                stuck=('The ring is hard to find?', 'Look for the thick outline around one control. It moves each time you press {Tab}.'),
                notes='Do not press {Enter} on the first stop: it is a link that leaves this page. The thick outline shows which control the keyboard is on.')


PART4 = dict(
    app='edge', still=True, title='Retest the repair', goals=[3],
    what='The agent has repaired the page. It is saved as version 3. Tonight’s last job is to test it as carefully as the others.',
    make='a test table for version 3, and two quick checks: the keyboard and a zoomed-in window.',
    start='A bug report about version 2.',
    finish='A test table for version 3 with all four rows, and a pass on the keyboard and zoom checks.',
    open_note='We stay in Edge. Version 3 opens in a new tab.',
    worksheet_extra=(open_button('resource-finder-agent-fixed.html', 'Open version 3', 'It opens in a new tab. It is the repair.')
                     + '<p><b>My test table.</b> Write what you see after each search in version 3.</p>' + table('t4', 'What I saw in version 3')),
    tell=dict(title='Ask for one repair. Then retest everything.',
              points=['A repair request names the [problem], what you [expected], and what must [stay the same].', 'Run the check that failed. Then run the checks that [passed before].',
                      'Try the [keyboard] and a [zoomed-in] window too. They are checks, like the searches.'],
              notes='Ask: when a mechanic fixes one thing, what else do you check on the drive home? Fixing one bug can break something else.'),
    watch=[dict(title='Watch: request one repair and retest what worked', start=364.77, end=400.62, look='a repair request, then a check that failed and a check that passed before.',
                notes='Plays 6:05 to 6:41 and stops on its own. It ends before the video asks learners to make their own improvement.')],
    closing=dict(title='A practice page is not a real service.',
                 points=['This page runs on one computer with made-up entries. A real service has real sign-ins, private data or payments, and needs much more care.',
                         'A picture of a sign-in box is [not security]. It protects nothing.'],
                 notes='Keep it short. Tonight’s page has no account, no private information and no payments. A real service with those needs people with the right skills to build and test it.'),
    steps=[
        step('Read the repair request', ['Read the four lines on the slide.'],
             'a request that names the problem, what you expected, and what must stay the same.', None, card=REPAIR, card_head='The repair request:', app='edge',
             notes='Point out the four parts: the problem, the expected result, what to keep, and the limit.'),
        step('See the repair', ['Look at the two lines on the slide.'],
             'the small-letters step back in the After line.', ('agent_change', dict(which='repair')), app='edge',
             notes='This is the real one-line difference between version 2 and version 3.'),
        step('Find Part 4 on your worksheet', ['Click the [Week 6 · Worksheet] tab at the top of Edge.', 'Roll the mouse wheel toward you until you see [Part 4].'],
             'the heading [Part 4 of 4], a gold button named [Open version 3], and a table named [My test table].', ('edge_worksheet_link', dict(week=6, part='Part 4', label='Open version 3')), app='edge',
             stuck=('Cannot find Part 4?', 'Roll the mouse wheel toward you. Part 4 comes after Part 3.'),
             notes='Everyone should be looking at the gold button before you move on.'),
        step('Open version 3', ['Click the gold button [Open version 3].'],
             'a new tab whose name ends in [version 3 (after the repair)].', fd(3, targets=['search']), app='edge',
             stuck=('Nothing happened?', 'Look at the tabs along the top of Edge. The new tab may be on the right. Click it.'),
             notes='Call this tab the finder tab now.', opener=True),
        step('Click the search box', ['Click the [Search fictional resources] box.'],
             'a blinking line in the search box.', fd(3, targets=['search']), app='edge',
             stuck=('Cannot find the search box?', 'It is the long white box under the words Search fictional resources.'),
             notes='Click first, then type.'),
    ] + [
        s for q, filled, find, note, tg in [
            ('library', 1, 'one entry, [Community library], and the line [1 fictional resource found.]', 'A check that passed before. It still passes.', ('results',)),
            ('learning', 2, 'two entries, [Community library] and [Practice Workbook Workshop].', 'The new feature survived the repair.', ('results',)),
            ('zzz', 3, 'the line [No matching resources. Try a different word or reset the filters.]', 'The no-match message survived too.', ('status',)),
            ('LIBRARY', 4, 'one entry, [Community library]. The bug is fixed.', 'The check that failed now passes.', ('results',)),
        ] for s in pair('v3', q, (3, list(tg), note, 'none found' if 'No matching' in find else ('2 found' if q == 'learning' else '1 found'), 4), filled, find, False)
    ] + [
        tab_step('Press Tab: first stop', ['Click a blank space on the page. Press {Tab} once.'], 'a thick outline around the link at the top of the page.', 'link'),
        tab_step('Press Tab: second stop', ['Press {Tab} again.'], 'the thick outline around the search box.', 'search'),
        tab_step('Press Tab: third stop', ['Press {Tab} again.'], 'the thick outline around the [Category] list.', 'category'),
        tab_step('Press Tab: fourth stop', ['Press {Tab} again.'], 'the thick outline around the [Reset filters] button.', 'reset'),
        step('Zoom in', ['Hold {Ctrl} and press {+} again and again, until the number next to the address bar reads 300%.'],
             'the page much larger. Words wrap, and nothing is cut off.', fd(3, 'LIBRARY', zoom=True), app='edge',
             stuck=('Cannot find the plus key?', 'It is the {+} key near the top right of the main keyboard. You may need to hold {Shift}.'),
             notes='A narrow window is the same test as a small screen. Nothing important should be cut off, and the page should not need sideways scrolling.'),
        step('Put the zoom back', ['Hold {Ctrl} and press {0}.'],
             'the page back at its normal size.', fd(3, 'LIBRARY'), app='edge',
             stuck=('The page is still big?', 'Press {Ctrl} and {0} again. That is the zero key, not the letter O.'),
             notes='Make sure every screen is back to normal before the next part.'),
    ],
    stuck=[('Cannot find the gold button?', 'Click the [Week 6 · Worksheet] tab, then roll the mouse wheel toward you until you see Part 4.'),
           ('Pressed {Enter} on the first stop?', 'It leaves this page. Click the Back arrow at the top left of Edge, then go on.'),
           ('The page stays big after you zoom?', 'Press {Ctrl} and {0} to go back to the normal size.')],
    check=dict(question='The repaired page finds LIBRARY. What else do you test?',
               choices=['Nothing; one bug is fixed', 'The searches that already worked', 'Only the colors'], answer=1,
               why='Fixing one thing can break another, so run the old checks again too.'),
)

PARTS = [PART1, PART2, PART3, PART4]

RESULT = dict(
    title='What I made tonight',
    intro='This page is your finished work. Fill in every box. Your instructor looks at it at the end of class.',
    fields=[('My test table: what version 1 showed for library, learning, zzz and LIBRARY', 3), ('My bug report: the steps, what I typed, what I expected, what happened', 4),
            ('My retest: what version 3 showed for each search, and what the keyboard and zoom checks showed', 3), ('One habit I will use when a program or an AI changes something for me', 2)],
)

WRAP = dict(
    label='MY RESULT',
    steps=[step('Fill in your result page', ['Turn to the last page of your worksheet, [My result].', 'Fill in every box.'],
                'every box on the [My result] page filled in.', None, card=['My test table', 'My bug report', 'My retest', 'One habit for next time'],
                card_head='Boxes to fill in:', app='edge',
                stuck=('Not sure what to write?', 'Look back at your test tables and your bug report on the worksheet. Copy what you wrote into your own words.'),
                notes='Learners copy what they found into their own words. Walk the room and read a few.')],
    show=['your [test table] for version 1', 'your [bug report] for version 2', 'your [My result] page, every box filled in'],
    home='Before you accept any change a program or an AI makes for you, run the checks that passed before the change, as well as the new one.',
    result=RESULT,
)

# ---------------------------------------------------------------- Course review (weeks 1 to 5)
SKILLS = {1: 'Make text bigger in every app', 2: 'Fix a page that spills onto a second sheet', 3: 'Fix a repeating calendar event', 4: 'Write a help request that can be answered',
          5: 'Narrow a web search', 6: 'Judge whether a source fits', 7: 'Act on a wrong confirmation', 8: 'Share with the right permissions', 9: 'Use real heading styles',
          10: 'Check that a SUM total updates', 11: 'Use a licensed photo properly', 12: 'Share a file that looks the same everywhere', 13: 'Write a clear request with a deadline',
          14: 'Know what Bcc does', 15: 'Use respectful, inclusive wording', 16: 'Give and answer feedback on one shared copy', 17: 'Spot a recurring charge',
          18: "Don't rely on color alone", 19: 'Secure a new account', 20: 'Check a suspicious contact a safer way'}


def q(item, app, question, correct, wrong, pos, why):
    """A review question: three choices, the right one at position pos (0 to 2)."""
    assert len(wrong) == 2 and 0 <= pos <= 2
    choices = list(wrong)
    choices.insert(pos, correct)
    return dict(n=item, item=item, skill=SKILLS[item], app=app, question=question, choices=choices, answer=pos, why=why)


REVIEW_WEEKS = [
    dict(week=1, app='settings', heading='Make the computer fit you', title='Week 1: make the computer fit you.',
         points=['In [Windows Settings], the Display page makes text larger in every program.',
                 'In [Microsoft Word], narrow the margins when a line spills. In [Outlook Calendar], fix the whole series.',
                 'A good help request names the program, what you tried and the exact message.'],
         notes='Two minutes. Ask what the class made in Week 1: readable text, a clean printed page, a weekly event and a clear help request. Then the four questions, one at a time.',
         questions=[
             q(1, 'settings', 'Menus, the clock and file names are too small to read. Which Windows Settings page fixes all of them?',
               'Display: pick a larger Scale', ['Personalization: pick a new background', 'Sound: raise the volume'], 0, 'Scale on the Display page resizes text and other items in every program.'),
             q(2, 'word', 'One line of your flyer spills onto page 2. What do you try first?',
               'Narrow margins, then look at the preview', ['Print both and throw one away', 'Cut words until it fits'], 1,
               'Narrow margins make room. The preview then shows it fits.'),
             q(3, 'outlook', 'Your weekly Thursday class moves to Wednesdays for good. What do you change?',
               'Change the whole series, then look at next week', ['Move just this one event', 'Add a Wednesday event and keep Thursday'], 2,
               'The series fixes every week. Next week shows it worked.'),
             q(4, 'word', 'You are writing a help request about a problem in Word. Which detail should you leave out?',
               'Your password', ['The exact message on the screen', 'What you already tried'], 1, 'Helpers never need your password. The other details help them find the cause.'),
         ]),
    dict(week=2, app='edge', heading='Find it, check it, keep it', title='Week 2: find it, check it, keep it.',
         points=['In [Microsoft Edge], ask a full question with a place and a detail, then check the source.',
                 'On a practice form, read the confirmation and fix a wrong detail its way. In [File Explorer], use clear names.',
                 'Share a file with the least access the job needs: Viewer, Commenter or Editor.'],
         notes='Two minutes. Ask what the class made in Week 2: a checked answer with a source note, a clearly named file, and sharing roles. Then the four questions.',
         questions=[
             q(5, 'edge', 'You want a weekend farmers market in Lewisburg, WV that takes SNAP. Which question works best?',
               'Which Lewisburg, WV markets open weekends and take SNAP?', ['markets', 'food, then scroll for a while'], 2, 'A place and details narrow the answer.'),
             q(6, 'edge', 'A page about heating help shows no date and no author. What should that make you do?',
               'Check it against a source that names its owner and date', ['Rely on it, since it is neatly laid out', 'Ignore every page like it'], 0, 'A page with no author or date is hard to judge.'),
             q(7, 'edge', 'You signed up for a class, but the confirmation lists the wrong time. What do you do?',
               'Fix it the way the confirmation says, and keep a record', ['Sign up a second time with the right time', 'Just come at the time you wanted'], 2,
               'Use the route the confirmation gives, and keep proof.'),
             q(8, 'edge', 'You gave a friend Editor access to a file, but he only needs to read it. What do you do?',
               'Change his access to Viewer', ['Leave it, since he probably will not change anything', 'Delete the file for everyone'], 1, 'Give people the least access the job needs.'),
         ]),
    dict(week=3, app='word', heading='Make something people can use', title='Week 3: make something people can use.',
         points=['In [Microsoft Word], use real heading styles, and save a PDF so the handout looks the same everywhere.',
                 'In [Microsoft Excel], a SUM formula adds the costs and changes by itself when a cost changes.',
                 'In [Microsoft PowerPoint], crop the photo and type the credit its permission asks for.'],
         notes='Two minutes. Ask what the class made in Week 3: a handout with headings, a PDF, a supply list that adds itself, and a one-slide flyer with a credit. Then the four questions.',
         questions=[
             q(9, 'word', 'You gave your section titles real heading styles in Word. What does the Navigation pane show?',
               'Every heading, so you can click one to jump to it', ['Every comment in the file', 'Every picture in the file'], 0, 'The Navigation pane is built from heading styles.'),
             q(10, 'excel', 'Why type =SUM(B2:B4) in Excel instead of typing the total yourself?',
               'The total changes by itself when a cost changes', ['It prints in a larger font', 'It makes the numbers bold'], 2, 'A formula recalculates. A typed number stays the same.'),
             q(11, 'powerpoint', 'A photo’s permission says to name the photographer. Which line on the slide does that?',
               'Photo: Dana Ruiz, used with permission', ['Photo: found online', 'No line is needed if the photo is cropped'], 1, 'The credit names who took it and says the permission was followed.'),
             q(12, 'word', 'How do you turn a Word handout into a PDF?',
               'File, Save As, then choose PDF as the type', ['Insert, then Pictures', 'Review, then New Comment'], 0, 'Saving as a PDF keeps the layout the same on any computer.'),
         ]),
    dict(week=4, app='mail', heading='Work together without confusion', title='Week 4: work together without confusion.',
         points=['In [Practice Mail], put what and when in the subject. Bcc hides addresses, but a message can still be passed on.',
                 'In [Microsoft Word], leave one specific comment on a shared copy. The owner changes it, replies, then resolves.',
                 'In [Microsoft Edge], find when a free trial ends, the price, how often you pay and how to cancel.'],
         notes='Two minutes. Ask what the class made in Week 4: a request with a deadline, a message with To and Bcc, a handout with a resolved comment, and four offer facts. Then the five questions.',
         questions=[
             q(13, 'mail', 'Where should the deadline for a request appear in an email?',
               'In the subject line, and again in the message', ['Only in your signature', 'Nowhere; people will ask'], 1, 'The subject is read first, so the deadline belongs there.'),
             q(14, 'mail', 'You Bcc ten neighbors. One passes your message to a stranger. Did Bcc fail?',
               'No. Bcc never stops a message being passed on', ['Yes, Bcc is meant to block that', 'Yes, the stranger sees the ten addresses'], 2, 'Bcc only hides addresses from the other people who got the message.'),
             q(15, 'mail', 'Which greeting leaves nobody out of a message to a class of adults?',
               'Hi everyone,', ['Hi ladies,', 'Hi boys and girls,'], 0, 'Words that name everyone welcome everyone.'),
             q(16, 'word', 'In Word, what does Resolve do to a comment thread?',
               'Closes it, and keeps it on record', ['Deletes it for good', 'Sends it to the owner by email'], 1, 'Resolved comments are hidden from view, not deleted.'),
             q(17, 'edge', 'A page says "First month $1, then $15 every month." How much do you pay in the third month?',
               '$15', ['$1', '$16'], 2, 'After the first month, the monthly price repeats until you cancel.'),
         ]),
    dict(week=5, app='excel', heading='Protect your work, show your skills', title='Week 5: protect your work, show your skills.',
         points=['In [Microsoft Excel], add words to a sign-in sheet so color is not the only clue.',
                 'On a practice sign-up page in [Microsoft Edge], use a long passphrase for that one site, plus two-step verification.',
                 'In [Practice Mail], check a suspicious message through a number you already trust.'],
         notes='Two minutes. Ask what the class made in Week 5: a sign-in sheet that does not rely on color, a protected practice sign-up, and a checked message. Then the three questions.',
         questions=[
             q(18, 'excel', 'In a four-color pie chart, what helps a reader who cannot tell the colors apart?',
               'Label each slice with its name', ['Use four shades of the same color', 'Make the chart larger'], 0, 'Words carry the meaning when color cannot.'),
             q(19, 'edge', 'On a practice sign-up page in Edge, what does two-step verification add?',
               'A second proof, such as a phone code', ['A longer password made by the site', 'A copy of your password on the page'], 2, 'Someone with your password still needs the second proof.'),
             q(20, 'mail', 'A message claims to be from your electric company. Where do you find a safe number to call?',
               'On your last paper bill', ['In the message itself', 'In a reply from the sender'], 1, 'Use a number you already trust, not one the message gives you.'),
         ]),
]

REVIEW = dict(
    title='Course review', minutes=20, weeks=REVIEW_WEEKS,
    intro='Twenty questions, one for each skill on the post-test. We go through them together. Write your answer letter on the line.',
    answer_note='One question for each post-test item, in item order. Every question is a new scenario, not a post-test question. Ask learners to say why before you reveal the answer.',
)

POST_TEST = dict(
    app='edge', minutes=20, title='Open the post-test',
    what='The post-test is a web page in Edge. We open it together from the course home. Then everyone answers on their own.',
    make='the post-test open on your screen, ready for your first question.',
    open_note='Walk the room as the class opens the page. Do not help with answers once the test starts.',
    steps=[
        step('Go to the course home', ['Click [Course home] at the top of your worksheet page.'],
             'the course home page, with a button named [Take the post-test].', ('edge_worksheet_top', dict(targets=['home'])), app='edge',
             stuck=('Cannot find Course home?', 'Click the [Week 6 · Worksheet] tab. The row of links is at the very top of the page.'),
             notes='Wait until every screen shows the course home page.'),
        step('Open the post-test', ['Click [Take the post-test].'],
             'a page named [Post-test], with a box named [Your full name].', ('edge_course_home', dict(targets=['post'])), app='edge',
             stuck=('Cannot find the button?', 'Roll the mouse wheel toward you. The button is on the course home page.'),
             notes='The post-test opens in the same tab.'),
        step('Click the name box', ['Click the [Your full name] box.'],
             'a blinking line in the name box.', ('edge_post_test', dict(targets=['name'])), app='edge',
             notes='The test is saved under the name you type.'),
        step('Type your name', ['Type your first and last name.'],
             'your name in the box.', ('edge_post_test', dict(name='Your name', targets=['name'])), app='edge',
             stuck=('Made a typing mistake?', 'Press {Backspace} to erase the letter before the blinking line, then type it again.'),
             notes='Each learner types their own full name.'),
        step('Start the post-test', ['Click [Start the post-test].'],
             'the words [Question 1 of 20].', ('edge_post_test', dict(name='Your name', targets=['start'])), app='edge',
             notes='Stop here. The next slide tells everyone how the test works. Nobody answers until you say so.'),
    ],
    alone=dict(title='Now you answer on your own.',
               points=['No help with answers. Choose the answer you think is best. You can go back and change answers before you submit.',
                       'If the page stops working, raise your hand.', 'At question 20, click [Review answers]. Then click [Submit my test].'],
               notes='Read it aloud. Then let the class begin. Walk the room quietly. Help only with a page that stops working, never with an answer. Plan about 20 minutes.'),
    finish=dict(title='When you finish.',
                points=['Click [Submit to instructor]. The page says when it is sent.', 'Click [Download graded PDF]. Save it to Britt’s flash drive, the way the page describes.',
                        'Open the PDF from the drive and check your name and score. Then close it and wait quietly.'],
                notes='A saved PDF is not proof that the answers were sent. Check each learner’s page for the sent message. Collect the flash drive at the end.'),
    worksheet_alone='Answer every question on your own. Raise your hand if the page stops working. When you finish, click Submit to instructor, then Download graded PDF, and save it to Britt’s flash drive.',
    answer_note='Learners open the post-test together, then work alone with no help on answers. Help only if the page stops working. After each learner submits, check that the page shows the sent message, and that the graded PDF is on the flash drive.',
)

QUICK = [
    ('Open a version', 'Worksheet tab › Part 1, 3 or 4 › the gold button.'),
    ('Search again', 'Finder tab › [Reset filters] › type the word.'),
    ('Write a result', 'Worksheet tab › your test table › the row for that word.'),
    ('Tab through', 'Click a blank space, then press {Tab}. The thick outline shows where the keyboard is.'),
    ('Zoom in', 'Hold {Ctrl} and press {+}. Back to normal: {Ctrl} and {0}.'),
    ('Open the post-test', 'Course home link on the worksheet › [Take the post-test] › type your name › [Start the post-test].'),
]

WEEK6 = dict(
    guided=True, title='Guide an agent. Test its work.', photo='app-planning', nobreak=True,
    warm='When someone changes something for you, like a repair or a new schedule, how do you check that it is right?',
    goals=GOALS, outcomes=OUTCOMES, ready=READY, parts=PARTS, wrap=WRAP, apps=APPS, words=WORDS, review=REVIEW, post_test=POST_TEST,
    warm_notes='Two or three answers. Listen for checking the old things as well as the new one. Tonight teaches exactly that, with a practice web page.',
    goals_notes='Read each goal aloud. There are four goals in four parts. Learners check the goals off on their worksheet at the end of the wrap-up. After the wrap-up we review weeks 1 to 5 together, and then everyone takes the post-test.',
    video='week-06', minutes=[16, 10, 17, 12], example_app='edge', css=['ui-week6.css'],
    hero='Tonight: test a page, check an AI agent’s change, review the course, take the post-test.',
    goals_foot='After these four parts: a course review, then the post-test.',
    done='You tested a page, asked for one change, found what the change broke and retested the repair. You finished the course.',
    show_notes='Walk the room with the roster. Mark Independent, With prompt or Needs practice for each of the four goals. Re-show only the missing step. Read the My result page as the evidence.',
    home_notes='Close all programs. Select Start fresh on this computer. Practice pages keep nothing on the computer. Collect the flash drives.',
    ws_note='Tonight you use three versions of one practice page on our site. It has made-up entries, no sign-in, and sends nothing anywhere. No AI account is needed. At the end of class, you take the post-test.',
    answer_note='The four parts have no post-test item of their own. Week 6 practices checking and guiding a change. The My result page is the written evidence. The course review and the post-test come after it.',
    plan_scope='Each part opens with a slide naming the program, then why it matters, a short video clip, the steps and one check question. Everything happens together in Microsoft Edge. The AI agent’s work is pre-built as three versions of one practice page, so nobody needs an AI account. After the wrap-up, the class reviews weeks 1 to 5 (a recap slide and the check questions for each week, 20 in all, one for each post-test skill), then opens the post-test together. The post-test is the only time learners work alone. The video chapters on websites and web apps, how a page is built, where data lives, secret keys, and repairing a file by hand are not played. There is no break and no timer. Minutes below are a guide for pacing, not a clock for learners.',
    jump_labels=['Start', 'Before we start', 'Part 1 · Edge: test version 1', 'Part 2 · Edge: the request', 'Part 3 · Edge: version 2', 'Part 4 · Edge: the repair', 'Wrap-up', 'Course review', 'Post-test'],
    quick=QUICK,
    prep='Each station: Microsoft Edge and the Week 6 worksheet. The three practice pages (resource-finder.html, resource-finder-agent.html and resource-finder-agent-fixed.html) work in Edge on every computer and need no account. Before class, open each from the worksheet and check that LIBRARY finds one entry in versions 1 and 3 and none in version 2. Check sound on the projector: play the first Watch slide. For the post-test, check that the course home opens and that the post-test page opens, and have Britt’s flash drives ready. Keep a roster for the end-of-class check. After your own run-through, select Start fresh on this computer at each station.',
)
