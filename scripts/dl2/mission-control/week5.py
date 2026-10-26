"""Mission Control Week 5, guided build: meaning without color, a safe new account, a message that rushes you.

Same brief as Weeks 3 and 4 (Britt): everyone can go slide by slide and finish every task; the class works together
from the projected deck; the worksheet repeats every step and ends in a My result page.

Scope is the three Week 5 skills the pre/post tests measure (items.js 18-20), and nothing else:
  18 don't rely on color alone · 19 secure a new account · 20 check a suspicious contact a safer way
Cut on purpose (Britt, 2026-10-23): comfort and workstation setup, camera and microphone permissions, encryption and
read-only, unknown USB drives, catfishing and harmful posts, the five-task skills challenge, and the post-test (it now
happens in Week 6, so Week 5 has no post-test slide). Each part plays only its own clip of the Week 5 video; the
passwords part has no clip because the video does not cover passwords. No break, no timers.

Excel is the real Excel. The sign-up page is a practice page (activities/practice-signup.html) and the suspicious
message is in Practice Mail (activities/practice-mail.html?inbox=week-5). Both make no network calls, take only
example.com addresses, and store nothing a learner types.

Inline markup in text (rendered by guided.py): [Label] on-screen name · {Key} keyboard key · «text» exact text.
"""
from week3 import open_app, step

APPS = {
    'mail': 'Practice Mail',
    'word': 'Microsoft Word',
    'edge': 'Microsoft Edge',
    'excel': 'Microsoft Excel',
    'powerpoint': 'Microsoft PowerPoint',
    'explorer': 'File Explorer',
}

COURSE_TITLE = 'Keep your accounts and messages safe'  # the catalog title (courses.json) for the course path drawing
SIGNUP_LINK = 'Open the practice sign-up page'
MAIL_LINK = 'Open Practice Mail'
SIGNUP_URL = '/courses/digital-literacy-2/activities/practice-signup.html'
MAIL_URL = '/courses/digital-literacy-2/activities/practice-mail.html?inbox=week-5#inbox=week-5'
PASSPHRASE = 'kettle orbit meadow quilt'
SHORT_PASSWORD = 'Maple9'
EMAIL = 'learner@example.com'
CODE = '482913'
SHEET_FILE = 'Sign-in sheet'
SHEET_TYPE = 'Excel Workbook (*.xlsx)'
REAL_NUMBER = '304-555-0188'
MESSAGE_NUMBER = '304-555-0199'
LINK_DEST = 'maple-valley-confirm.example.net/login'

# The sign-in sheet, built up one step at a time.
HEAD = {'A1': 'Name', 'B1': 'Done?'}
NAMES = {'A2': 'Ana', 'A3': 'Ben', 'A4': 'Cal', 'A5': 'Dee'}
BASE = {**HEAD, **NAMES}
WORDS_IN = {'B2': 'Complete', 'B3': 'Complete', 'B4': 'Not yet', 'B5': 'Not yet'}
GREEN = {'B2': 'green', 'B3': 'green'}
RED = {'B4': 'red', 'B5': 'red'}
BOTH = {**GREEN, **RED}


def sheet(cells=None, **kw):
    return ('excel_signin', dict(cells=cells if cells is not None else BASE, **kw))


GOALS = [
    dict(app='excel', text='Make a sheet that still makes sense without color: add words next to the color, and know that charts need labels or patterns too.', short='Show meaning without color alone', item=18),
    dict(app='edge', text='Secure a new account with a long password used nowhere else, and turn on two-step verification.', short='Secure a new account', item=19),
    dict(app='mail', text='Check a suspicious message or caller a safer way: spot the pressure, read where a link really goes, and verify through a route you already trust.', short='Check a suspicious message a safer way', item=20),
]

OUTCOMES = [
    'Color: in Excel, each learner types a sign-in sheet with four fictional names, colors the Done cells green and red with Fill Color, adds the words Complete and Not yet so the sheet makes sense without color, and saves Sign-in sheet in Documents. They can say that a chart needs labels or patterns for the same reason.',
    'Account: on the practice sign-up page, each learner enters a made-up example.com email, sees a short password refused, enters the long practice passphrase, sees it accepted with the reminder to use it nowhere else, chooses a text code, types the code from the drawn phone, and reads Two-step verification is on.',
    'Message: in Practice Mail, each learner opens the Week 5 message, finds the pressure words, points at the link without clicking and reads where it really goes, compares the message’s phone number with the number on the letter, reports the message, and writes a safer route on the worksheet.',
]

WORDS = [
    ('Tab', 'One of the page names along the top of Edge. Click a tab to switch pages.'),
    ('Address bar', 'The long box at the top of Edge where you type a website name.'),
    ('Cell', 'One box in an Excel sheet, where a column and a row meet.'),
    ('Fill Color', 'The Excel button that paints the inside of a cell.'),
    ('Chart', 'A picture of numbers, such as bars or lines.'),
    ('Password', 'The secret word or words that open an account.'),
    ('Passphrase', 'A long password made of several words in a row.'),
    ('Two-step verification', 'A second lock. After your password, the site sends a code to your phone. Only your phone gets it.'),
    ('Pressure words', 'Words that rush you, such as act now or stops today.'),
    ('Link', 'Words you can click to go to another page. The words shown can differ from where the link really goes.'),
    ('Trusted route', 'A way to reach a company that you already had before the message came: a letter, a card or a saved bookmark.'),
    ('Report', 'Tell your email program that a message looks like a trick.'),
]

READY = dict(
    title='Open this worksheet on your computer', app='edge',
    what='It has every step from tonight, a box to check for each one, links to the practice pages, and a My result page at the end. If you have a printed copy, open it on screen too.',
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
             'the VUB Learning page with course cards.', ('vub_course_path', dict(week=5, week_title=COURSE_TITLE)), app='edge',
             stuck=('Typed it in a search box and got a list of results?', 'Click the long bar at the very top of Edge, press {Ctrl} and {A}, and type it again.'),
             notes='If the browser opens to another page, the address bar is still the long box at the top.'),
        step('Open the course', ['On the [Digital Literacy — Level 2] card, click [Open course].'],
             'a page that lists the weeks of the course.', ('vub_course_path', dict(week=5, week_title=COURSE_TITLE)), app='edge',
             stuck=('Cannot find the card?', 'Roll the mouse wheel toward you to scroll down. The cards are in a row.'),
             notes='Walk the room until every screen shows the course page.'),
        step('Open your Week 5 worksheet', ['Roll the mouse wheel toward you until you see [Week 5].', 'Click [Worksheet] in the Week 5 row.'],
             'a page titled [Week 5 · Worksheet]. Leave it open. You will come back to it.', ('vub_course_path', dict(week=5, week_title=COURSE_TITLE)), app='edge',
             stuck=('Cannot find Week 5?', 'The weeks are in order. Keep rolling the wheel toward you.'),
             notes='The worksheet tab stays open all night. It holds the links to the practice pages and your result page.'),
    ])


# ---------------------------------------------------------------- Part 1: meaning without color (Excel)
def save_excel():
    return [
        step('Save: open the File menu', ['Click [File] at the top left.'],
             'a menu with [Save As] in the list on the left.', ('file_menu', dict(app='excel', step=1)),
             stuck=('Not sure you clicked File?', 'File is the first word in the row of tabs, above the buttons.'),
             notes='Everything turns into a menu when File is clicked.'),
        step('Open the Save As box', ['Click [Save As], then click [Browse].'],
             'a box titled [Save As].', ('file_menu', dict(app='excel', step='both')),
             stuck=('No Browse button?', 'Click [This PC], then look for [Browse] beside it.'),
             notes='The same clicks as in Weeks 3 and 4.'),
        step('Choose Documents', ['On the left side of the box, click [Documents].'],
             'the top of the box ends in [Documents].', ('save_as_dialog', dict(location=['This PC', 'Documents'], items=[], savetype=SHEET_TYPE, app='excel', targets=['documents'])),
             notes='Documents is the folder learners used in earlier weeks.'),
        step('Name the file', ['Click in the [File name] box. Press {Ctrl} and {A} together to shade the old name.', f'Type «{SHEET_FILE}»'],
             f'«{SHEET_FILE}» in the [File name] box.', ('save_as_dialog', dict(location=['This PC', 'Documents'], items=[], filename=SHEET_FILE, savetype=SHEET_TYPE, app='excel', targets=['filename'])),
             stuck=('Typed the name next to the old one?', 'Click in the box again, press {Ctrl} and {A}, and type the name again.'),
             notes='Check a few screens before the next click.'),
        step('Save the file', ['Click [Save].'],
             f'«{SHEET_FILE}» at the very top of the Excel window.', ('save_as_dialog', dict(location=['This PC', 'Documents'], items=[], filename=SHEET_FILE, savetype=SHEET_TYPE, app='excel', targets=['save'])),
             notes='The window title now reads Sign-in sheet.'),
    ]


P1_MAP = dict(title='Find your way around Excel', draw=sheet({}, tab='Home', targets=['Home', 'Fill Color']),
              items=['The [Home] tab: the buttons we need are here.', '[Fill Color]: paints the inside of a cell.', 'A [cell]: one box in the sheet, where a column and a row meet.'],
              notes='Point to each part on the projector. The cells are the boxes below the ribbon. Fill Color is the paint-bucket button; its small arrow opens the list of colors.')

PART1 = dict(
    app='excel', title='Make a sheet that makes sense without color', goals=[0],
    what='Excel works with lists in a grid of boxes called cells. Tonight you color some cells, then make sure the sheet still works without the colors.',
    make='a sign-in sheet with green and red cells and the words Complete and Not yet.',
    start='A blank workbook and a list of four fictional names.',
    finish='A sign-in sheet where the words, not only the colors, say who is done, saved in Documents.',
    open_note='Everyone opens Excel in a moment.',
    tell=dict(title='Do not let color do all the work.',
              points=['Some people cannot tell [red] from [green]. A black-and-white printer shows both as gray.',
                      'Add [words] next to the color, such as [Complete] and [Not yet]. Now the sheet works for everyone.',
                      'The same goes for charts: add [labels] or [patterns] to the bars, so the meaning does not depend on color alone.'],
              notes='Ask: has anyone had trouble reading something because of its colors? About one man in twelve cannot tell red from green. A printed copy loses color too. Tonight we color a sheet, then fix it. The same fix works on charts.'),
    watch=[dict(title='Watch: instructions that do not rely on color', start=65.68, end=78.88, look='the idea that meaning should not depend on color alone.',
                notes='Plays 1:06 to 1:19 of the Week 5 video and stops on its own. It ends before the Pause and choose prompt.')],
    steps=[
        dict(kind='map', **P1_MAP),
        step('Type the headings', ['Click cell [A1]. Type «Name» and press {Tab}.', 'Type «Done?» and press {Enter}.'],
             '«Name» in A1 and «Done?» in B1.', sheet(HEAD, active='A2'),
             stuck=('Typed in the wrong cell?', 'Click that cell and press {Delete}. Then click the right cell and type again.'),
             notes='Tab moves right. Enter goes down to the start of the next row.'),
        step('Type the four names', ['Type each name below in column A. Press {Enter} after each one.'],
             'four names under «Name»: Ana, Ben, Cal and Dee.', None, card=['Ana', 'Ben', 'Cal', 'Dee'], card_head='Type these names:',
             stuck=('A name went in the wrong row?', 'Click it, type the right name, and press {Enter}. The new name replaces the old one.'),
             notes='These are made-up names. Ana and Ben will be done; Cal and Dee will not.'),
        step('Check your sheet', ['Look at your sheet. Find the heading row and four names.'],
             'a heading row and four names, with nothing in column B yet.', sheet(BASE, active='A6', targets=['A1', 'A5']),
             notes='Everyone should have the same sheet before the colors start.'),
        step('Select the two done cells', ['Click cell [B2]. Hold the left mouse button down and drag to [B3]. Let go.'],
             'a green border around [B2] and [B3], beside Ana and Ben. [B2] stays white.', sheet(BASE, selected=['B2', 'B3'], active='B2', targets=['B2', 'B3']),
             stuck=('Lost the shading?', 'Click anywhere else and try the drag again, slowly.'),
             notes='Ana and Ben are done, so their cells will be green. Dragging was practiced in Weeks 3 and 4.'),
        step('Open the Fill Color list', ['On the [Home] tab, click the small arrow next to [Fill Color].'],
             'a list of colors under the button. The big block at the top is [Theme Colors]. Below it is one row named [Standard Colors].', sheet(BASE, selected=['B2', 'B3'], tab='Home', targets=['Fill Color'], pick='green'),
             stuck=('Painted the cells yellow right away?', 'You clicked the bucket, not the arrow. Press {Ctrl} and {Z}, then click the small arrow beside the bucket.'),
             notes='The bucket paints the last color used. The small arrow beside it opens the list.'),
        step('Choose green', ['Look at the single row under [Standard Colors], below the big block. Click its green square: the sixth from the left.'],
             '[B2] and [B3] turn green.', sheet(BASE, fills=GREEN, selected=['B2', 'B3'], active='B2', targets=['B2', 'B3']),
             stuck=('Picked the wrong color?', 'Press {Ctrl} and {Z}, then open the list and choose the sixth square in the [Standard Colors] row, not the big block above it.'),
             notes='Green is the sixth square, between light green and light blue. Name the color aloud as you click it.'),
        step('Select the two not-done cells', ['Click cell [B4]. Hold the left mouse button down and drag to [B5]. Let go.'],
             'a green border around [B4] and [B5], beside Cal and Dee. [B4] stays white.', sheet(BASE, fills=GREEN, selected=['B4', 'B5'], active='B4', targets=['B4', 'B5']),
             notes='Cal and Dee are not done yet, so their cells will be red.'),
        step('Open the Fill Color list again', ['Click the small arrow next to [Fill Color].'],
             'the list of colors.', sheet(BASE, fills=GREEN, selected=['B4', 'B5'], tab='Home', targets=['Fill Color'], pick='red'),
             notes='Same list as before.'),
        step('Choose red', ['In the single [Standard Colors] row, click the red square: the second from the left.'],
             '[B4] and [B5] turn red.', sheet(BASE, fills=BOTH, selected=['B4', 'B5'], active='B4', targets=['B4', 'B5']),
             stuck=('The cells are dark red?', 'You picked the first square. Press {Ctrl} and {Z}, then choose the second.'),
             notes='Red is the second square. Dark red is the first.'),
        step('Look at your colors', ['Click any empty cell, such as [D1]. Look at the [Done?] column.'],
             'two green cells and two red cells. No words yet.', sheet(BASE, fills=BOTH, active='D1'),
             notes='Ask: if you could not tell red from green, could you tell who is done? No. The words come next.'),
        step('Add the words', ['Click cell [B2]. Type each word below. Press {Enter} after each one.'],
             'a word in each colored cell. The colors stay.', None, card=['Complete', 'Complete', 'Not yet', 'Not yet'], card_head='Type these words:',
             stuck=('The color disappeared?', 'Typing does not remove it. If it did, press {Ctrl} and {Z} and start the step again.'),
             notes='Typing in a colored cell keeps the color. B2 and B3 get Complete; B4 and B5 get Not yet.'),
        step('Read the sheet without color', ['Read down the [Done?] column. Ignore the colors.'],
             'Ana Complete, Ben Complete, Cal Not yet, Dee Not yet. The words say it all.', sheet(BASE | WORDS_IN, fills=BOTH, active='D1'),
             notes='This is the post-test idea: the words carry the meaning, so the sheet works for someone who cannot tell the colors apart. The same idea fixes a chart: label the bars or give each a pattern.'),
    ] + save_excel(),
    stuck=[('Cannot find the arrow next to Fill Color?', 'It is a tiny triangle right beside the paint bucket on the [Home] tab.'),
           ('Painted the wrong cells?', 'Press {Ctrl} and {Z} to undo, then select the right cells and try again.'),
           ('A box asks you to sign in?', 'Close it with the [X]. You do not need an account tonight.')],
    check=dict(question='A chart shows two stores as blue and orange bars. In gray they look alike. What fixes it?',
               choices=['Make the chart bigger', 'Label each bar, or give one store stripes', 'Pick two brighter colors'], answer=1,
               why='Labels or patterns carry the meaning when color cannot.'),
)

# ---------------------------------------------------------------- Part 2: a new account (practice sign-up page in Edge)
SU = 'edge_signup'


def su(**kw):
    return (SU, kw)


PART2 = dict(
    app='edge', title='Secure a new account', goals=[1],
    what='Microsoft Edge shows web pages. Tonight we use a practice sign-up page for a made-up reading club. Nothing you type there is saved or sent.',
    make='a practice account with a long password and two-step verification turned on.',
    start='A practice sign-up page with an empty email box and an empty password box.',
    finish='A page that says Two-step verification is on.',
    open_note='We stay in Edge. Everyone opens the practice page from the worksheet.',
    worksheet_extra=(f'<p class="g-download"><a class="g-download-button" href="{SIGNUP_URL}" target="_blank" rel="noopener">{SIGNUP_LINK}</a> '
                     '<span>It opens in a new tab. It is a practice page: nothing you type is saved or sent.</span></p>'
                     f'<p><b>Practice passphrase:</b> <span class="typed">{PASSPHRASE}</span><br><b>For this practice page only. Never use it for a real account.</b></p>'),
    tell=dict(title='Two locks are better than one.',
              points=['A [long] password is stronger than a short one. Four words in a row is long and easy to remember.',
                      'Use it on [one site only]. If one site loses your password, a reused one opens your other accounts too.',
                      '[Two-step verification] is a second lock: after your password, the site sends a code to your phone.'],
              notes='Ask: how many sites could one reused password open? The practice passphrase is for this page only. Real passphrases are never shown on a slide, shared or written on the result page.'),
    watch=[],
    steps=[
        step('Find Part 2 on your worksheet', ['Click the [Week 5 · Worksheet] tab at the top of Edge.', 'Roll the mouse wheel toward you until you see [Part 2].'],
             'the heading [Part 2 of 3] and a gold button named [Open the practice sign-up page].', ('edge_worksheet_link', dict(week=5, part='Part 2', label=SIGNUP_LINK)), app='edge',
             stuck=('Cannot find the worksheet tab?', 'Look at the tabs along the top of Edge. The one named Week 5 · Worksheet has the links.'),
             notes='Everyone should be looking at the gold button before you move on.'),
        step('Open the practice sign-up page', ['Click the gold button [Open the practice sign-up page].'],
             'a new tab named [Riverbend Reading Club · Practice sign-up].', su(stage='form', targets=[]), app='edge',
             stuck=('Nothing happened?', 'Look at the tabs along the top of Edge. The new tab may be on the right. Click it.'),
             notes='The worksheet stays open in its own tab. The sign-up page opens beside it.', opener=True),
        dict(kind='map', title='Find your way around the page', draw=su(stage='form', targets=['email', 'password', 'create']),
             items=['[Email]: your made-up email goes here.', '[Password]: the page checks it when you click the button.', '[Create account]: asks the page to check both.'],
             notes='Point to each part on the projector. The page shows the password as you type, so you can check it. Real sites show dots.'),
        step('Click the Email box', ['Click the [Email] box.'],
             'a blinking line in the [Email] box.', su(stage='form', targets=['email']), app='edge',
             notes='Wait until every screen shows the blinking line.'),
        step('Type a made-up email', [f'Type «{EMAIL}»'],
             f'«{EMAIL}» in the [Email] box.', su(stage='form', email=EMAIL, targets=['email']), app='edge',
             stuck=('A message says the email is not allowed?', 'The practice page only takes made-up emails that end in «@example.com». Check the spelling and type it again.'),
             notes='example.com is reserved for examples. Nothing can be delivered there.'),
        step('Click the Password box', ['Click the [Password] box.'],
             'a blinking line in the [Password] box.', su(stage='form', email=EMAIL, targets=['password']), app='edge',
             notes='Wait until every screen shows the blinking line in the Password box.'),
        step('Type a short password', [f'Type «{SHORT_PASSWORD}»'],
             f'«{SHORT_PASSWORD}» in the [Password] box.', su(stage='form', email=EMAIL, password=SHORT_PASSWORD, targets=['password']), app='edge',
             notes='A short password on purpose. We want to see the page say no.'),
        step('Click Create account', ['Click [Create account].'],
             'a red message under the button. The page says no.', su(stage='form', email=EMAIL, password=SHORT_PASSWORD, message='That password is too short. It has 6 characters. Use at least 12: four words in a row works well.', bad=True, targets=['create']), app='edge',
             stuck=('Nothing happened?', 'Click right on the words [Create account].'),
             notes='The page refuses a short password and says why.'),
        step('Read the reason', ['Read the red message under the button.'],
             'the words «too short» and a number of characters.', su(stage='form', email=EMAIL, password=SHORT_PASSWORD, message='That password is too short. It has 6 characters. Use at least 12: four words in a row works well.', bad=True), app='edge',
             notes='Length matters most. Six characters is easy to guess. Four words in a row is long and easy to remember.'),
        step('Shade the short password', ['Click in the [Password] box. Press {Ctrl} and {A} together to shade it.'],
             'the short password shaded.', su(stage='form', email=EMAIL, password=SHORT_PASSWORD, targets=['password']), app='edge',
             stuck=('Nothing is shaded?', 'Click inside the Password box first, then press {Ctrl} and {A} again.'),
             notes='Typing over shaded words replaces them.'),
        step('Type the practice passphrase', ['Type the practice passphrase below.', 'It is for this practice page only. Never use it for a real account.'],
             'four words with spaces between them in the [Password] box.', None, card=[PASSPHRASE], card_head='Type this practice passphrase:', app='edge',
             stuck=('Made a typing mistake?', 'Press {Ctrl} and {A}, then type the four words again.'),
             notes='The passphrase is printed on the slide and the worksheet so everyone matches. Say it clearly: it is for practice only. A real passphrase is never shown or shared.'),
        step('Click Create account again', ['Click [Create account].'],
             'a new heading, [Turn on two-step verification]. A green note says the password was accepted.', su(stage='two_step', targets=[]), app='edge',
             stuck=('The red message is back?', 'Check that the passphrase has four words with a space between each one, then click [Create account] again.'),
             notes='The page accepts a long password.'),
        step('Read the reminder', ['Read the green note at the top.'],
             'the words «this one site only».', su(stage='two_step', targets=[]), app='edge',
             notes='A password reused on two sites can open both. This is the second half of the post-test idea: long, and used nowhere else.'),
        step('Choose a text code', ['Click [Text me a code].'],
             'a page named [Check your phone], with a drawing of a phone.', su(stage='two_step', targets=['text_code']), app='edge',
             stuck=('Clicked Skip for now?', 'Click [Text me a code]. Skipping leaves only one lock.'),
             notes='Real sites send the code to your own phone. Our page draws a phone, so every screen matches the slide.'),
        step('Find the code on the phone', ['Look at the drawing of the phone. Find the six-digit code.'],
             f'the code [{CODE}] on the phone.', su(stage='code', targets=['phone']), app='edge',
             notes='A real code arrives on your phone and lasts a few minutes. Never read a code to a caller or type it into a page you reached from a message.'),
        step('Type the code', ['Click the [Code] box.', f'Type «{CODE}»'],
             f'«{CODE}» in the [Code] box.', su(stage='code', code=CODE, targets=['code']), app='edge',
             stuck=('A message says the code does not match?', f'Look at the phone again. The code is {CODE}. Type it again.'),
             notes='Six digits, no spaces.'),
        step('Click Verify', ['Click [Verify].'],
             'a green box that says [Two-step verification is on].', su(stage='code', code=CODE, targets=['verify']), app='edge',
             notes='Two locks now: a long password used nowhere else, and a code from the phone.'),
        step('Read what you turned on', ['Read the green box.'],
             '[Two-step verification is on].', su(stage='done', targets=[]), app='edge',
             notes='Leave the tab open. You will not need it again, and it keeps nothing.'),
    ],
    stuck=[('Cannot find the gold button?', 'Click the [Week 5 · Worksheet] tab, then roll the mouse wheel toward you until you see Part 2.'),
           ('The page says the email is not allowed?', 'Practice pages only take emails that end in @example.com.'),
           ('The page keeps saying the password is too short?', 'It needs 12 or more characters. Type the four practice words with a space between each.')],
    check=[dict(question='A friend uses her long email password for her new bank login. What is wrong with that?',
                choices=['Nothing. It is long, so it is safe', 'One lost password opens both accounts', 'Banks do not allow long passwords'], answer=1,
                why='One lost password can open every account that shares it.'),
           dict(question='What does two-step verification add to your password?',
                choices=['A second lock: a code sent to your phone', 'A longer password made by the site', 'A way to log in without a password'], answer=0,
                why='After the password, the site asks for a code that only your phone receives.')],
)

# ---------------------------------------------------------------- Part 3: a suspicious message (Practice Mail)
P3_MAP = dict(title='Find your way around the message', draw=('mail5_message', dict(targets=['from', 'link', 'phone', 'report'])),
              items=['[From]: who the message says it is from.', 'The blue [link]: words you can click.', 'The [phone number] in the message.', '[Report this message]: warns your email program.'],
              notes='Point to each part on the projector. This is a made-up message. Practice Mail never sends or receives anything real, and the link will not open.')

LETTER_HTML = (
    '<div style="border:2px solid #333;padding:.6em 1em;margin:.8em 0;max-width:30em"><p style="margin:0"><b>A letter you already have</b></p>'
    '<p style="margin:.3em 0 0"><b>Maple Valley Health Plan</b> · Member letter<br>Questions? Call Member Services: <b>' + REAL_NUMBER + '</b><br>Website: maplevalleyhealth.example.com</p></div>')

PART3 = dict(
    app='mail', title='Check a message that rushes you', goals=[2],
    what='Practice Mail is a practice email program in Edge. Tonight it holds one made-up message that tries to rush you.',
    make='a list of the warning signs in the message, and a safer way to check it.',
    start='A message that says your coverage stops today.',
    finish='A reported message, and your worksheet showing the pressure words, where the link really goes, and a safer route.',
    open_note='Everyone opens Practice Mail from the worksheet in a moment. We never click the link.',
    worksheet_extra=(f'<p class="g-download"><a class="g-download-button" href="{MAIL_URL}" target="_blank" rel="noopener">{MAIL_LINK}</a> '
                     '<span>It opens in a new tab. The message is made up. Nothing is sent outside the page.</span></p>' + LETTER_HTML),
    tell=dict(title='Pressure is a warning sign.',
              points=['Words like [act now] and [stops today] try to make you hurry. Hurrying is how people get tricked.',
                      'A [link] can say one thing and go somewhere else. Point at it, without clicking, and read the real address.',
                      'Check through a [route you already trust]: a number on a letter or card you already have, or a website you saved. Never the message’s own link or number.'],
              notes='Ask: has anyone had a message or call that said hurry? Pressure is the clue, not proof. The same habit works for a phone call: hang up, then call the number you already trust.'),
    watch=[dict(title='Watch: recognize the pressure', start=89.069, end=132.0, look='the urgent words, and why urgency is a reason to slow down.',
                notes='Plays 1:29 to 2:12 of the Week 5 video and stops on its own.'),
           dict(title='Watch: check a safer way', start=133.413, end=165.9, look='checking through a website or number you found yourself, not the message’s own.',
                notes='Plays 2:13 to 2:46 and stops on its own, before the Pause and choose prompt.')],
    steps=[
        step('Find Part 3 on your worksheet', ['Click the [Week 5 · Worksheet] tab at the top of Edge.', 'Roll the mouse wheel toward you until you see [Part 3].'],
             'the heading [Part 3 of 3] and a gold button named [Open Practice Mail].', ('edge_worksheet_link', dict(week=5, part='Part 3', label=MAIL_LINK)), app='edge',
             stuck=('Cannot find the worksheet tab?', 'Look at the tabs along the top of Edge. The one named Week 5 · Worksheet has the links.'),
             notes='Everyone should be looking at the gold button before you move on. Just under it is a box named A letter you already have: it stands for a real letter at home.'),
        step('Open Practice Mail', ['Click the gold button [Open Practice Mail].'],
             'a new tab named [Practice Mail] with one message in the Inbox.', ('mail5_inbox', dict(targets=[])), app='mail',
             stuck=('Nothing happened?', 'Look at the tabs along the top of Edge. The new tab may be on the right. Click it.'),
             notes='The worksheet stays open in its own tab. Practice Mail opens beside it.', opener=True),
        step('Open the message', ['Click the message from [Maple Valley Health Plan].'],
             'the message open, with a [From] line and a [Subject] line.', ('mail5_inbox', dict(targets=['row'])), app='mail',
             stuck=('Nothing happened?', 'Click right on the words Maple Valley Health Plan.'),
             notes='Wait until every screen shows the open message.'),
        dict(kind='map', **P3_MAP),
        step('Find the rush words in the subject', ['Read the [Subject] line. Find [ACT NOW] and [stops today].'],
             'two rush phrases in the subject.', ('mail5_message', dict(targets=['act', 'today'])), app='mail',
             notes='Capital letters and a deadline: both are pressure.'),
        step('Find the rush words in the message', ['Read the message. Find [act now], [stops today] and [within 1 hour].'],
             'three rush phrases in the message.', ('mail5_message', dict(targets=['today2', 'act2', 'hour'])), app='mail',
             stuck=('Cannot find them?', 'They are in the first two lines under the Subject: act now and stops today in the first, within 1 hour in the second.'),
             notes='A real company gives you time and a way to ask questions. Pressure is the clue. It is not proof by itself.'),
        step('Read the From line', ['Read the [From] line.'],
             'the name «Maple Valley Health Plan». Anyone can type that name, so it proves nothing by itself.', ('mail5_message', dict(targets=['from'])), app='mail',
             notes='Anyone can type a name that looks right. Do not trust it by itself. The next checks matter more.'),
        step('Point at the link', ['Move the mouse pointer onto the blue link. Do not click it.'],
             'a line at the bottom left of Edge that shows the real address.', ('mail5_message', dict(targets=['link'], status=True)), app='mail',
             stuck=('Nothing shows at the bottom left?', 'Hold the pointer still on the blue words for a second. Practice Mail also shows the address under the link.'),
             notes='Edge shows where a link really goes at the bottom left of the window. Practice Mail also writes it under the link. Never click to find out.'),
        step('Read where it really goes', ['Read the address at the bottom left of Edge.'],
             f'«{LINK_DEST}». It is not «maplevalleyhealth.example.com».', ('mail5_message', dict(targets=[], status=True)), app='mail',
             notes='The words on the link said one site. The real address is another. Anyone can write one thing and link to another.'),
        step('Find the phone number in the message', ['Find the phone number near the bottom of the message.'],
             f'«{MESSAGE_NUMBER}».', ('mail5_message', dict(targets=['phone'])), app='mail',
             notes='We will compare it with a number you already trust.'),
        step('Find the number on your letter', ['Click the [Week 5 · Worksheet] tab. Find the box named [A letter you already have].'],
             f'«{REAL_NUMBER}» under Member Services.', ('phone_compare', dict(targets=[])), app='edge',
             stuck=('Cannot find the letter?', 'It is just under the gold button in Part 3 of the worksheet.'),
             notes='The letter stands for a real one you already have. A number you had before the message came is a trusted route.'),
        step('Compare the numbers', ['Look at the last four digits of both numbers.'],
             f'«{MESSAGE_NUMBER}» is not «{REAL_NUMBER}». The numbers are different.', ('phone_compare', dict(targets=['message', 'letter'])), app='edge',
             notes='Different numbers mean the message did not come from the company on your letter.'),
        step('Report the message', ['Click the [Practice Mail] tab. Click [Report this message].'],
             'the button changes to [Reported].', ('mail5_message', dict(targets=['report'], reported=True)), app='mail',
             stuck=('Cannot find the button?', 'It is at the bottom of the message.'),
             notes='Reporting tells your email program to treat messages like this with care. In real life, do not reply and do not click.'),
        step('Write your safer route', ['Click the [Week 5 · Worksheet] tab. In [Part 3], click the box and write what you would do instead.'],
             'a sentence in the box that uses the number on your letter.', None,
             write='Instead of using the message, I would:', write_head='Your safer route (worksheet, Part 3):', write_rows=3, app='edge',
             notes='Accept any trusted route: call the number on the letter, or open the plan’s website from a saved bookmark. Never the message’s link or number.'),
    ],
    stuck=[('Cannot find the gold button?', 'Click the [Week 5 · Worksheet] tab, then roll the mouse wheel toward you until you see Part 3.'),
           ('Clicked the link by mistake?', 'Nothing happened. Practice Mail shows a warning and stays on the page. In real life, close the page and tell someone.'),
           ('Cannot see the address at the bottom left?', 'Hold the pointer still on the blue words for a second. Practice Mail also writes it under the link.')],
    check=[dict(question='An email says: pay in 30 minutes or lose power. What is the safest first move?',
                choices=['Click the button in the email', 'Do not click. Call the number on your paper bill', 'Reply and ask if it is real'], answer=1,
                why='A number you already had is a trusted route. The email is not.'),
           dict(question='A caller wants the code just texted to you, right now. What do you do?',
                       choices=['Read him the code', 'Hang up. Call the number on your bill', 'Ask him to call from another number'], answer=1,
                       why='Asking for a code is a warning sign. Use the number on your bill.')],
)

PARTS = [PART1, PART2, PART3]
# Part 1 opens Excel first, then the map, then the task steps (the same order as Week 3).
PART1['steps'] = open_app('excel', 'blank workbook') + PART1['steps']

RESULT = dict(
    title='What I made tonight',
    intro='This page is your finished work. Fill in every box. Do not write your passphrase here. Your instructor looks at this page at the end of class.',
    fields=[('The words I added so my sign-in sheet does not need color', 1),
            ('My rule for a password: how long it is, and where I use it', 2),
            ('Two-step verification: is it on? What did the page say?', 1),
            ('The pressure words I found in the message', 1),
            ('Where the link in the message really went', 1),
            ('My trusted route for checking a message or a caller', 2),
            ('One habit I will use', 2)],
)

WRAP = dict(
    label='MY RESULT',
    steps=[step('Fill in your result page', ['Turn to the last page of your worksheet, [My result].', 'Fill in every box.'],
                'every box on the [My result] page filled in.', None, card=['Words I added to my sheet', 'My rule for a password', 'Two-step verification', 'Pressure words', 'Where the link went', 'My trusted route', 'One habit'],
                card_head='Boxes to fill in:', app='edge',
                stuck=('Not sure what to write?', 'Look back at the step that made it. Your Excel sheet, the sign-up page tab and the Practice Mail message are still open.'),
                notes='Learners write the rule for a passphrase, never the passphrase itself. Walk the room and read a few.')],
    show=['your Excel sign-in sheet with the words [Complete] and [Not yet]', 'the practice sign-up page saying [Two-step verification is on]', 'your reported Practice Mail message', 'your [My result] page, every box filled in'],
    home='Pick one account that matters, such as your email. Give it a long password you use nowhere else, and turn on two-step verification. Next time a message or caller rushes you, stop and check through a number or website you already trust.',
    result=RESULT,
)

QUICK = [
    ('Color a cell', 'Select the cells › [Home] tab › small arrow next to [Fill Color] › click a color.'),
    ('Do not rely on color', 'Add words next to the color, such as Complete and Not yet. On a chart, add labels or patterns.'),
    ('Save in Documents', '[File] › [Save As] › [Browse] › [Documents] › click in [File name], press {Ctrl}+{A}, type the name › [Save].'),
    ('A strong password', 'Long (four words in a row) and used on one site only.'),
    ('Two-step verification', 'After your password, the site sends a code to your phone. Type it. Never read it to a caller.'),
    ('Spot the pressure', 'Words like act now, stops today, within 1 hour. Slow down.'),
    ('Check a link', 'Point at it without clicking. Read the address at the bottom left of Edge.'),
    ('Check a safer way', 'Use a number or website you already had: a letter, a card or a saved bookmark. Not the message’s.'),
]

WEEK5 = dict(
    guided=True, title='Keep your accounts and messages safe.', photo='safety', nobreak=True,
    warm='When has a message or a call made you stop and wonder, is this real? What made you wonder?',
    goals=GOALS, outcomes=OUTCOMES, ready=READY, parts=PARTS, wrap=WRAP, apps=APPS, words=WORDS,
    warm_notes='Two or three answers. Listen for hurry, a strange sender or a request that did not fit. Tonight teaches how to check, and how to set up an account that is hard to break into.',
    goals_notes='Read each goal aloud. There are three goals in three parts: each part teaches one. Learners check the goals off on their worksheet at the end of class. The post-test is next week.',
    video='week-05', minutes=[32, 30, 33], example_app='excel', css=['ui-week4.css', 'ui-week5.css'],
    hero='Tonight you fix a sheet, secure an account and check a message.',
    goals_foot='These three skills are on your post-test.',
    done='You made a sheet that works without color, secured a practice account and checked a message the safer way.',
    show_notes='Walk the room with the roster. Mark Independent, With prompt or Needs practice for each of the three. Re-show only the missing step. Read the My result page as the evidence, and check that nobody wrote a passphrase on it.',
    home_notes='Close all programs. Select Start fresh on this computer. Sign-in sheet may stay in Documents. The practice pages keep nothing when the tab closes.',
    ws_note='Tonight you use two practice pages on our site. Every email address is made up and ends in example.com, so nothing is ever delivered. The practice sign-up page and Practice Mail cannot send anything outside the page. The practice passphrase is for the practice page only: never use it for a real account.',
    answer_note='The three parts prepare the three Week 5 post-test items (18 to 20). The My result page is the written evidence.',
    plan_scope='Each part opens with a slide naming the program, then why it matters, short video clips where the video covers the topic, the steps and check questions. Week 5 teaches only the three skills on the post-test (items 18 to 20): meaning without color, securing a new account, and checking a suspicious contact a safer way. Every step is one or two actions with what you should see. The video chapters on comfort and workstation setup, camera and microphone permissions, encryption, unknown USB drives and harmful posts are not played. The skills challenge is cut and the post-test is in Week 6. There is no break and no timer. Minutes below are a guide for pacing, not a clock for learners.',
    jump_labels=['Start', 'Before we start', 'Part 1 · Excel: color alone', 'Part 2 · Edge: a new account', 'Part 3 · Practice Mail: a rushed message', 'Wrap-up'],
    quick=QUICK,
    prep='Each station: Microsoft Edge and Microsoft Excel that opens without a sign-in. No email or other account is needed: the practice sign-up page (activities/practice-signup.html) and Practice Mail (activities/practice-mail.html?inbox=week-5) work in Edge on every computer, accept only addresses that end in example.com, and keep nothing a learner types. Before class, check that Excel can save to Documents on This PC (not only OneDrive), and that both practice pages open from the Week 5 worksheet. Check sound on the projector: play the first Watch slide. Print the worksheet if you can: the letter in Part 3 is meant to be on paper, and the My result page is the written evidence. After your own run-through, delete Sign-in sheet and select Start fresh on this computer at each station.',
)
