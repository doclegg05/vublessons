"""Mission Control Week 4, guided build: a request, who sees which addresses, one shared copy, one offer.

Same brief as Week 3 (Britt, 2026-10-12): everyone can go slide by slide and finish every task; the class
works together from the projected deck; the worksheet repeats every step and ends in a My result page.

Scope is the five Week 4 skills the pre/post tests measure (items.js 13-17):
  13 a clear request with a deadline · 15 respectful, inclusive wording · 14 what Bcc does
  16 feedback on one shared copy (comment, reply, resolve) · 17 spot a recurring charge
Cut on purpose (no test item): choosing a channel, joining a meeting, community posts, Cc and Reply all as
practice. The opening video is not played whole: each part plays only its own clip. No break, no timers.

Email is Practice Mail (activities/practice-mail.html): a practice email program on our site. Nobody needs an
account, and every address must end in example.com, so nothing can be delivered anywhere. Word opens without
a sign-in.

2026-10-20 revision (Britt): more detail, one action per step wherever possible, and a final My result page.

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

SUBJECT = 'Reply by Friday noon: please review the handout'
REQUEST = 'Please review the computer-help handout and reply by Friday at noon.'
CHOICE = 'Reply by email, or call 304-555-0142 if you prefer.'
TO = ['desk@example.com']
BCC = ['sam@example.com', 'pat@example.com', 'lee@example.com']
B_GREET = ['Hi guys,']
B_REQUEST = B_GREET + [REQUEST]
B_CHOICE = B_REQUEST + [CHOICE]
B_DRAFT = B_CHOICE + ['Thank you,']
B_FIXED = ['Hi everyone,', REQUEST, CHOICE, 'Thank you,']
HANDOUT = ['Computer help handout', 'Step 1: Choose one task.', 'Step 2: Visit the learning desk.', 'Step 3: Ask how to repeat it at home.']
COMMENT = 'Add the contact number after the steps so readers can find help.'
NUMBER = 'Help desk: 304-555-0142'
WORD_FILE = 'Handout with comments'
WORD_TYPE = 'Word Document (*.docx)'
COURSE_TITLE = 'Communicate and collaborate with care'
MAIL_LINK = 'Open Practice Mail'
OFFER_LINK = 'Open the practice offer'
OFFER_URL = '/courses/digital-literacy-2/activities/free-trial-offer.html'
MAIL_URL = '/courses/digital-literacy-2/activities/practice-mail.html'


def mc(**kw):
    """A Practice Mail New Message drawing with the same subject and body defaults."""
    return ('mail_compose', kw)


GOALS = [
    dict(app='mail', text='Write an email request with a subject that names what you need and when.', short='Write a request with a deadline', item=13),
    dict(app='mail', text='Use words that welcome everyone, and offer a choice instead of guessing.', short='Use words that welcome all', item=15),
    dict(app='mail', text='Put the right people in To and in Bcc, and know what Bcc does and does not do.', short='Know what Bcc does', item=14),
    dict(app='word', text='Give feedback on one shared copy: write a specific comment, reply, then resolve it.', short='Give feedback on one shared copy', item=16),
    dict(app='edge', text='Check an offer for when it ends, what it costs, how often you pay, and how to cancel.', short='Spot a charge that repeats', item=17),
]

OUTCOMES = [
    'Request: in Practice Mail, each learner types a subject with the day and time, a four-line message with a Friday-at-noon deadline and an email-or-phone choice, and changes «guys» to «everyone».',
    'Recipients: each learner puts desk@example.com in To and the three volunteer addresses in Bcc, sends the practice message, and reads the Who sees what box. They can say what Bcc hides and what it does not stop.',
    'Comments: in Word, each learner types the four-line handout, posts the specific comment, adds the Help desk line, replies Added, thank you, resolves the thread, and saves Handout with comments in Documents.',
    'Offer: on the practice page, each learner finds when the free days end (day 8), the price ($12), how often it is charged (each month) and how to cancel (Account › Billing › Cancel plan), and writes all four on the worksheet.',
]

WORDS = [
    ('Subject', 'The line people read first. It says what the message is about.'),
    ('To', 'The person who needs to act on the message.'),
    ('Cc', 'A visible copy for people who only need to know.'),
    ('Bcc', 'A hidden copy. The other people cannot see these addresses.'),
    ('Comment', 'A note beside a document that suggests a change.'),
    ('Reply', 'Your answer, written under someone\'s comment.'),
    ('Resolve', 'Close a comment once it is dealt with. It stays on record.'),
    ('Free trial', 'Free for a short time. After that you may be charged.'),
    ('Recurring charge', 'The same amount taken again and again, such as every month.'),
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
             'the VUB Learning page with course cards.', ('vub_course_path', dict(week=4, week_title=COURSE_TITLE)), app='edge',
             stuck=('Typed it in a search box and got a list of results?', 'Click the long bar at the very top of Edge, press {Ctrl} and {A}, and type it again.'),
             notes='If the browser opens to another page, the address bar is still the long box at the top.'),
        step('Open the course', ['On the [Digital Literacy — Level 2] card, click [Open course].'],
             'a page that lists the weeks of the course.', ('vub_course_path', dict(week=4, week_title=COURSE_TITLE)), app='edge',
             stuck=('Cannot find the card?', 'Roll the mouse wheel toward you to scroll down. The cards are in a row.'),
             notes='Walk the room until every screen shows the course page.'),
        step('Open your Week 4 worksheet', ['Roll the mouse wheel toward you until you see [Week 4].', 'Click [Worksheet] in the Week 4 row.'],
             'a page titled [Week 4 · Worksheet]. Leave it open. You will come back to it.', ('vub_course_path', dict(week=4, week_title=COURSE_TITLE)), app='edge',
             stuck=('Cannot find Week 4?', 'The weeks are in order. Keep rolling the wheel toward you.'),
             notes='The worksheet tab stays open all night. It holds the links to the practice pages and your result page.'),
    ])

# ---------------------------------------------------------------- Part 1: the request (Practice Mail)
P1_MAP = dict(title='Find your way around the message', draw=mc(targets=['to', 'subject', 'body', 'send']),
              items=['[To]: who gets the message.', '[Subject]: the line people read first.', 'The big white box: your message.', '[Send]: sends the message. In Practice Mail nothing really leaves the page.'],
              notes='Point to each part on the projector. Practice Mail is a practice email program: it looks and works like email, but every address must end in example.com, so nothing is delivered anywhere.')

PART1 = dict(
    app='mail', title='Write a request people can act on', goals=[0, 1],
    what='Practice Mail is a practice email program in Edge. Tonight you write a message in it. It never leaves the page.',
    make='an email that asks for a review, with the day and time in the subject.',
    start='An empty Practice Mail inbox.',
    finish='A message with a subject that names the request and the deadline, a message with a day and a time, and words that welcome everyone.',
    open_note='Everyone opens Practice Mail from the worksheet in a moment.',
    worksheet_extra=(f'<p class="g-download"><a class="g-download-button" href="{MAIL_URL}" target="_blank" rel="noopener">{MAIL_LINK}</a> '
                     '<span>It opens in a new tab. Nothing you write is sent outside the page.</span></p>'),
    tell=dict(title='A request someone can act on.',
              points=['Put what you need and when in the [subject]. People read it first.', 'Ask for one thing, with a day and a time.',
                      'Welcome everyone: write [Hi everyone], not [Hi guys]. Offer a choice, like email or a phone call.'],
              notes='Ask: which message in your inbox was easy to answer? Usually it said what and by when. Tonight we write one, and fix a word that leaves people out.'),
    watch=[dict(title='Watch: a message someone can act on', start=85.1, end=130.3, look='a subject and a message that say what to review and when.',
                notes='Plays 1:25 to 2:10 of the Week 4 video and stops on its own. It ends before the part about checking recipients, which is Part 2.')],
    steps=[
        step('Find Part 1 on your worksheet', ['Click the [Week 4 · Worksheet] tab at the top of Edge.', 'Roll the mouse wheel toward you until you see [Part 1].'],
             'the heading [Part 1 of 4] and a gold button named [Open Practice Mail].', ('edge_worksheet_link', dict(week=4, part='Part 1', label=MAIL_LINK)), app='edge',
             stuck=('Cannot find the worksheet tab?', 'Look at the tabs along the top of Edge. The one named Week 4 · Worksheet has the links.'),
             notes='Everyone should be looking at the gold button before you move on.'),
        step('Open Practice Mail', ['Click the gold button [Open Practice Mail].'],
             'a new tab named [Practice Mail] with a [Compose] button at the top left.', ('mail_inbox', dict(targets=[])), app='mail',
             stuck=('Nothing happened?', 'Look at the tabs along the top of Edge. The new tab may be on the right. Click it.'),
             notes='The worksheet stays open in its own tab. Practice Mail opens beside it.', opener=True),
        step('Start a new message', ['Click [Compose] at the top left.'],
             'a box named [New Message].', ('mail_inbox', dict(targets=['compose'])), app='mail',
             stuck=('No box appeared?', 'Click [Compose] again, and wait one second.'),
             notes='Wait until every screen shows the New Message box.'),
        dict(kind='map', **P1_MAP),
        step('Click the Subject line', ['Click the [Subject] line, the line under [To].'],
             'a blinking line in the [Subject] line.', mc(targets=['subject'], cursor='subject'), app='mail',
             stuck=('Cannot tell which line is Subject?', 'It is the line with the word Subject in gray. It is under the To line.'),
             notes='Say it: click first, then type. The blinking line shows where typing goes.'),
        step('Type the subject', [f'Type «{SUBJECT}»'],
             'your subject on the [Subject] line.', mc(subject=SUBJECT, cursor='subject'), app='mail',
             stuck=('Made a typing mistake?', 'Press {Backspace} to erase the letter before the blinking line, then type it again.'),
             notes='The subject carries the request and the deadline: Friday noon. Spelling does not need to be perfect.'),
        step('Check your subject', ['Read your subject. Find the day [Friday] and the time [noon].'],
             'the day [Friday] and the time [noon] in the subject.', mc(subject=SUBJECT, targets=['subject']), app='mail',
             notes='A reader who sees only the subject already knows what to do and by when.'),
        step('Click the message box', ['Click the big white box under the Subject line.'],
             'a blinking line at the top of the big white box.', mc(subject=SUBJECT, targets=['body'], cursor='body'), app='mail',
             stuck=('The blinking line is still in the subject?', 'Click lower, in the middle of the big white box.'),
             notes='This box holds the message itself.'),
        step('Type the greeting', ['Type «Hi guys,» and press {Enter}.'],
             '[Hi guys,] on the first line. The blinking line moves to the second line.', mc(subject=SUBJECT, body=B_GREET, cursor='body'), app='mail',
             stuck=('Cannot find the {Enter} key?', 'It is the large key on the right side of the keyboard, with a bent arrow on it.'),
             notes='This first line says «Hi guys,» on purpose. We fix it in a few steps.'),
        step('Type the request', [f'Type «{REQUEST}»', 'Press {Enter}.'],
             'the request on the second line.', mc(subject=SUBJECT, body=B_REQUEST, cursor='body'), app='mail',
             notes='One request, with a day and a time.'),
        step('Type the choice', [f'Type «{CHOICE}»', 'Press {Enter}.'],
             'the email-or-phone line on the third line.', mc(subject=SUBJECT, body=B_CHOICE, cursor='body'), app='mail',
             notes='Offering two ways to reply is how a message welcomes people with different habits.'),
        step('Type the closing', ['Type «Thank you,» and press {Enter}.', 'Type your first name.'],
             'a closing line and your name at the end of the message.', mc(subject=SUBJECT, body=B_DRAFT, cursor='body'), app='mail',
             notes='Learners type their own first name.'),
        step('Find the word to change', ['Double-click the word [guys] in your first line.'],
             'the word [guys] shaded.', mc(subject=SUBJECT, body=B_DRAFT, mark='guys'), app='mail',
             stuck=('The whole line is shaded?', 'Click once anywhere else in the box, then double-click on the middle of the word guys.'),
             notes='Double-click means two quick clicks in the same spot.'),
        step('Change the word', ['Type «everyone»'],
             'the first line now says [Hi everyone,].', mc(subject=SUBJECT, body=B_FIXED, cursor='body'), app='mail',
             stuck=('The comma disappeared?', 'Click right after «everyone» and type «,» again.'),
             notes='A word like guys leaves some people out. Everyone leaves nobody out.'),
        step('Read it like your reader', ['Read your message from top to bottom.', 'Find the day and the time you need an answer.'],
             '[Friday] and [noon] in the subject and in the message, and [Hi everyone,] on the first line.', mc(subject=SUBJECT, body=B_FIXED, targets=['subject', 'body']), app='mail',
             notes='Could the reader act without asking what you meant? Read a few subjects aloud around the room.'),
    ],
    stuck=[('Cannot find the gold button?', 'Click the [Week 4 · Worksheet] tab, then roll the mouse wheel toward you until you see Part 1.'),
           ('Made a typing mistake?', 'Press {Backspace} to erase the letter before the blinking line.'),
           ('Clicked away from the message box?', 'Click in the box again. Your words are still there.')],
    check=[dict(question='Which subject line is easiest to act on?',
                choices=['Hello from the learning desk', 'Reply by Thu 5 p.m.: bring the sign-in sheet?', 'Sign-in sheet'], answer=1,
                why='It says what you need and when, so the reader can act.'),
           dict(question='Which invitation is the most welcoming?',
                choices=['Bring your husband or wife.', 'Bring a guest if you like.', 'Wives are welcome.'], answer=1,
                why='It does not guess who someone is or who they live with. It offers a choice.')],
)

# ---------------------------------------------------------------- Part 2: To and Bcc (Practice Mail, same message)
FULL = dict(subject=SUBJECT, body=B_FIXED[:3])
PART2 = dict(
    app='mail', still=True, title='Choose who sees which addresses', goals=[2],
    what='The To and Bcc lines decide who gets the message, and who can see whose address.',
    make='the same message with one address in To and three in Bcc.',
    start='A message with a subject and a text, and nobody to send it to.',
    finish='A sent practice message with desk@example.com in To and three volunteers in Bcc, and the Who sees what box read.',
    open_note='We stay in Practice Mail, in the same message. Do not close it.',
    tell=dict(title='To, Cc and Bcc.',
              points=['[To]: the person who needs to act.', '[Cc]: a visible copy for people who only need to know.',
                      '[Bcc]: hides each person\'s address from the others. It does not stop anyone from forwarding the message.'],
              notes='Ask: when is it a problem if 30 people can see each other\'s addresses? Bcc protects addresses. It does not make the message secret.'),
    watch=[dict(title='Watch: who receives it', start=132.0, end=152.0, look='the To, Cc and Bcc lines, and what Bcc hides.',
                notes='Plays 2:12 to 2:32 and stops on its own, before the part about Reply all, which we are not practicing tonight.')],
    steps=[
        step('Click the To line', ['Click the [To] line at the top of the message.'],
             'a blinking line in the [To] line.', mc(targets=['to'], cursor='to', **FULL), app='mail',
             stuck=('Cannot find the To line?', 'It is the first line of the New Message box, at the top.'),
             notes='The message from Part 1 is still open. Anyone who closed it can click [Drafts] and open it.'),
        step('Type the first address', [f'Type «{TO[0]}»', 'Press {Enter}.'],
             'a gray bubble holding [desk@example.com].', mc(to=TO, cursor='to', **FULL), app='mail',
             stuck=('A message says the address is not allowed?', 'Practice Mail only takes made-up addresses that end in «@example.com». Check the spelling and type it again.'),
             notes='This is the organizer\'s own desk address. The volunteers go in Bcc.'),
        step('Find the Bcc link', ['Look at the right end of the [To] line.', 'Find the word [Bcc].'],
             'two small blue words: [Cc] and [Bcc].', mc(to=TO, targets=['bcc_link'], **FULL), app='mail',
             notes='Bcc stays out of the way until you ask for it.'),
        step('Open the Bcc line', ['Click [Bcc].'],
             'a new line named [Bcc] under the [To] line.', mc(to=TO, targets=['bcc_link'], **FULL), app='mail',
             stuck=('Nothing happened?', 'Click right on the word Bcc, not beside it.'),
             notes='The word Bcc disappears from the To line once the Bcc line is open.'),
        step('Click the Bcc line', ['Click in the [Bcc] line.'],
             'a blinking line in the [Bcc] line.', mc(to=TO, show_bcc=True, targets=['bcc'], cursor='bcc', **FULL), app='mail',
             notes='Wait until every screen shows the blinking line in the Bcc line.'),
        step('Add the three volunteers', ['Type the first address below and press {Enter}.', 'Do the same for the other two addresses.'],
             'three gray bubbles on the [Bcc] line.', None, card=BCC, card_head='Type these addresses:', app='mail',
             stuck=('The bubbles did not appear?', 'Press {Enter} right after you type each address.'),
             notes='These three people do not know each other. Bcc keeps their addresses from the others.'),
        step('Check who sees what', ['Look at your [To] line and your [Bcc] line.'],
             'one address in [To] and three in [Bcc].', mc(to=TO, bcc=BCC, show_bcc=True, targets=['to', 'bcc'], **FULL), app='mail',
             notes='Say it before the next step: the three in Bcc will not see each other.'),
        step('Send the practice message', ['Click the blue [Send] button at the bottom left of the message.'],
             'a page that says the message was sent in practice, with a box named [Who sees what].', mc(to=TO, bcc=BCC, show_bcc=True, targets=['send'], **FULL), app='mail',
             stuck=('A message says to add a subject or an address?', 'Fill in what it asks for, then click [Send] again.'),
             notes='Practice Mail sends nothing anywhere. It shows what each person would see.'),
        step('Read who sees what', ['Find the box named [Who sees what].', 'Read the row for [sam@example.com].'],
             'sam sees [To: desk@example.com] only. The other Bcc addresses are hidden.', ('mail_sent', dict(subject=SUBJECT, targets=['who', 'sam'])), app='mail',
             notes='This is the post-test idea: Bcc hides addresses from the other people. It does not stop forwarding.'),
    ],
    stuck=[('Cannot find [Bcc]?', 'Look at the right end of the [To] line. Click in the [To] line first.'),
           ('The address is not allowed?', 'Practice Mail only takes addresses that end in @example.com.'),
           ('Closed the message by mistake?', 'Click [Drafts] on the left, then click your message. Everything you typed is still there.')],
    check=dict(question='You email 12 members of a community group who do not know each other, and you put their addresses in Bcc. What does Bcc do?',
               choices=['Each person cannot see the other addresses', 'Nobody can forward the email', 'Only those 12 people can open the email'], answer=0,
               why='Bcc hides addresses from the other recipients. It does not stop forwarding or protect the message.'),
)

# ---------------------------------------------------------------- Part 3: comments on one shared copy (Word)
P3_MAP = dict(title='Find your way around the Review tab', draw=('word_review', dict(stage='page', tab='Review', targets=['Review', 'New Comment'])),
              items=['The [Review] tab: comments live here.', '[New Comment]: adds a comment to the words you selected.', 'The comment appears in a box on the right of the page.'],
              notes='Point to each part on the projector. Tonight one person plays both roles on one copy. In real life the copy lives in one shared place, and each person comments on that same file.')


def word(upto=4, **kw):
    return ('word_review', dict(upto=upto, **kw))


def save_word():
    return [
        step('Save: open the File menu', ['Click [File] at the top left.'],
             'a menu with [Save As] in the list on the left.', ('file_menu', dict(app='word', step=1)),
             stuck=('Not sure you clicked File?', 'File is the first word in the row of tabs, above the buttons.'),
             notes='Everything turns into a menu when File is clicked.'),
        step('Open the Save As box', ['Click [Save As], then click [Browse].'],
             'a box titled [Save As].', ('file_menu', dict(app='word', step='both')),
             stuck=('No Browse button?', 'Click [This PC], then look for [Browse] beside it.'),
             notes='The same clicks as in Week 3.'),
        step('Choose Documents', ['On the left side of the box, click [Documents].'],
             'the top of the box ends in [Documents].', ('save_as_dialog', dict(location=['This PC', 'Documents'], items=[], savetype=WORD_TYPE, app='word', targets=['documents'])),
             notes='Documents is the folder learners used last week.'),
        step('Name the file', ['Click in the [File name] box. Press {Ctrl} and {A} together to highlight the old name.', f'Type «{WORD_FILE}»'],
             f'«{WORD_FILE}» in the [File name] box.', ('save_as_dialog', dict(location=['This PC', 'Documents'], items=[], filename=WORD_FILE, savetype=WORD_TYPE, app='word', targets=['filename'])),
             stuck=('Typed the name next to the old one?', 'Click in the box again, press {Ctrl} and {A}, and type the name again.'),
             notes='Check a few screens before the next click.'),
        step('Save the file', ['Click [Save].'],
             f'«{WORD_FILE}» at the very top of the Word window.', ('save_as_dialog', dict(location=['This PC', 'Documents'], items=[], filename=WORD_FILE, savetype=WORD_TYPE, app='word', targets=['save'])),
             notes='The window title now reads Handout with comments.'),
    ]


PART3 = dict(
    app='word', title='Give feedback on one shared copy', goals=[3],
    what='Word lets people leave comments on a document without changing it. Comments keep every suggestion in one place.',
    make='a handout with one comment that you answered and resolved.',
    start='A short handout with no comments.',
    finish='A handout where the comment is answered, the number is added and the thread says Resolved, saved in Documents.',
    open_note='Everyone opens Word in a moment. Tonight one person plays both roles: reviewer, then owner.',
    tell=dict(title='One copy. Comments, not copies.',
              points=['Three people with three copies means nobody knows which is final. Keep [one shared copy].',
                      'A good comment says [where], [what] and [why].', 'The owner makes the change, replies, then [resolves] the comment.'],
              notes='Ask: has anyone received three versions of the same file? In real life the shared copy lives in one place everyone can open. Tonight we practice the comment steps on one file.'),
    watch=[dict(title='Watch: why one copy', start=179.8, end=194.6, look='three separate handouts, and the idea of one common copy.',
                notes='Plays 2:59 to 3:15 and stops on its own, before the roles and the live-or-later discussion.'),
           dict(title='Watch: a useful comment', start=227.8, end=261.2, look='a comment that names a place, a change and a reason, then the reply and Resolve.',
                notes='Plays 3:48 to 4:21 and stops on its own, before the partner pause prompt.')],
    steps=[
        dict(kind='map', **P3_MAP),
        step('Type the title', ['Click the white page. Type «Computer help handout» and press {Enter}.'],
             'the title at the top of the page.', word(upto=1, tab='Home'),
             stuck=('Made a typing mistake?', 'Press {Backspace} to erase the letter before the blinking line, then type it again.'),
             notes='Spelling does not need to be perfect. The comment is the point.'),
        step('Type step 1', ['Type «Step 1: Choose one task.» and press {Enter}.'],
             'a second line under the title.', word(upto=2, tab='Home'), notes='One line at a time.'),
        step('Type step 2', ['Type «Step 2: Visit the learning desk.» and press {Enter}.'],
             'a third line.', word(upto=3, tab='Home')),
        step('Type step 3', ['Type «Step 3: Ask how to repeat it at home.» Do not press {Enter}.'],
             'four lines: the title and three steps.', word(upto=4, tab='Home'),
             notes='The handout is done. The next steps play two roles: first the reviewer.'),
        step('Be the reviewer: select a line', ['Point just before the «S» in «Step 3: Ask how to repeat it at home.»', 'Hold the left mouse button down. Drag to the end of that line. Let go.'],
             'the Step 3 line shaded gray: selected.', word(tab='Home', selected=True),
             stuck=('Lost the shading?', 'Click anywhere on the page and try the drag again, slowly.'),
             notes='You practiced dragging in Week 3. Demonstrate it once more, slowly.'),
        step('Open the Review tab', ['Click the [Review] tab at the top of Word.'],
             'new buttons in the ribbon, including [New Comment].', word(tab='Review', selected=True, targets=['Review']),
             stuck=('Cannot find the Review tab?', 'It is in the row of words above the buttons: File, Home, Insert, and so on.'),
             notes='A ribbon is the strip of buttons under the tab names.'),
        step('Click New Comment', ['Click [New Comment].'],
             'a comment box on the right side of the page, with a blinking line.', word(tab='Review', selected=True, targets=['New Comment']),
             stuck=('No [New Comment] button?', 'Click the [Review] tab first.'),
             notes='The comment is tied to the words you selected.'),
        step('Write a specific comment', [f'Type «{COMMENT}»'],
             'your comment in the box on the right.', word(stage='typing', tab='Review', selected=True),
             notes='Point out where, what and why: after the steps, add the contact number, so readers can find help.'),
        step('Post the comment', ['Click [Post comment].'],
             'your comment stays on the right side, with a [Reply] box under it.', word(stage='typing', tab='Review', selected=True, targets=['Post']),
             stuck=('No [Post comment] button?', 'Press {Ctrl} and {Enter} together.'),
             notes='Posting makes the comment visible to the owner.'),
        step('Be the owner: go to the end of step 3', ['Click at the very end of the line «Step 3: Ask how to repeat it at home.»'],
             'a blinking line after the word [home].', word(stage='posted'),
             stuck=('The comment box moved?', 'Click in the page, on the left of the comment box.'),
             notes='From here the same person plays the owner of the handout.'),
        step('Add the number', ['Press {Enter}.', f'Type «{NUMBER}»'],
             'a new line under Step 3 that says [Help desk: 304-555-0142].', word(stage='posted', added=True),
             stuck=('The new line is shaded?', 'Click anywhere else on the page. The shading was the selection.'),
             notes='Use the number on the slide. A comment is a request; the owner decides and makes the change.'),
        step('Click the Reply box', ['Click the [Reply] box under your comment.'],
             'a blinking line in the [Reply] box.', word(stage='posted', added=True, targets=['Reply']),
             notes='The reply tells the reviewer the change is done.'),
        step('Write and post your reply', ['Type «Added, thank you.»', 'Click the small arrow button next to the box.'],
             'your reply under the comment.', word(stage='replied', added=True),
             stuck=('No arrow button?', 'Press {Enter}, or {Ctrl} and {Enter} together.'),
             notes='A short reply is enough.'),
        step('Open the comment menu', ['Click the three dots [···] at the top right of the comment.'],
             'a small menu with [Resolve thread] in it.', word(stage='menu', added=True, targets=['more']),
             stuck=('A [Resolve] button instead of three dots?', 'Click [Resolve]. Your Word shows it that way.'),
             notes='The three dots mean more choices.'),
        step('Resolve the comment', ['Click [Resolve thread].'],
             'the comment turns gray and says [Resolved].', word(stage='menu', added=True, targets=['Resolve']),
             notes='Resolved comments are hidden from view, not deleted. They stay in the file.'),
    ] + save_word(),
    stuck=[('No [New Comment] button?', 'Click the [Review] tab first.'),
           ('Cannot find [Resolve thread]?', 'Click the three dots at the top right of the comment box.'),
           ('A box asks you to sign in?', 'Close it with the [X]. Word works without it tonight.')],
    check=dict(question='You added the number the comment asked for. What next?',
               choices=['Delete the comment', 'Reply "Added", then resolve the comment', 'Leave the comment as it is'], answer=1,
               why='The reply tells the reviewer. Resolving closes the comment.'),
)

# ---------------------------------------------------------------- Part 4: an offer (Edge)
PART4 = dict(
    app='edge', title='Check an offer before you agree', goals=[4],
    what='Microsoft Edge shows web pages. Tonight we read a practice offer. Nothing on it can charge you.',
    make='four facts about a free trial, written down before you would agree.',
    start='A practice offer: Free for 7 days, then $12 each month.',
    finish='Four facts on your worksheet: when the free days end, the price, how often you pay, and how to cancel.',
    open_note='We are back in Edge, on a practice page. Everyone starts from the worksheet tab.',
    worksheet_extra=(f'<p class="g-download"><a class="g-download-button" href="{OFFER_URL}" target="_blank" rel="noopener">{OFFER_LINK}</a> '
                     '<span>It opens in a new tab. It is a practice page: nothing on it can charge you.</span></p>'),
    tell=dict(title='A free trial can become a monthly charge.',
              points=['[Free for 7 days, then $12 each month] means a charge every month until you cancel.',
                      'Before you agree, find four facts: [when it ends], [what it costs], [how often you pay], [how to cancel].', 'A fact is missing? Do not agree yet.'],
              notes='Ask: has a free trial ever turned into a charge? The four facts are the habit. The offer tonight is fictional.'),
    watch=[dict(title='Watch: review an offer', start=361.1, end=386.9, look='the trial, the monthly price, and what to check before you accept.',
                notes='Plays 6:01 to 6:27 and stops on its own, before the video discusses logos and the practice wrap-up.')],
    steps=[
        step('Find Part 4 on your worksheet', ['Click the [Week 4 · Worksheet] tab at the top of Edge.', 'Roll the mouse wheel toward you until you see [Part 4].'],
             'the heading [Part 4] and a gold button named [Open the practice offer].', ('edge_worksheet_link', dict(week=4, part='Part 4', label=OFFER_LINK)), app='edge',
             stuck=('Cannot find the worksheet tab?', 'Look at the tabs along the top of Edge. The one named Week 4 · Worksheet has the link.'),
             notes='Everyone should be looking at the gold button before you move on.', opener=True),
        step('Open the practice offer', ['Click the gold button [Open the practice offer].'],
             'a new tab named [MapleStream · Practice offer].', ('edge_worksheet_link', dict(week=4, part='Part 4', label=OFFER_LINK)), app='edge',
             stuck=('Nothing happened?', 'Look at the tabs along the top of Edge. The new tab may be on the right. Click it.'),
             notes='The offer opens in a new tab, so the worksheet stays open beside it.'),
        step('Read the offer', ['Read the big words at the top of the page.'],
             '[Free for 7 days] and [then $12 each month].', ('edge_offer', dict(targets=['trial', 'price'])), app='edge',
             notes='This is what the offer says first. The next steps find the details.'),
        step('Find when the free days end', ['Find the line in the small print that starts with [Your first charge].'],
             '[Your first charge is on day 8.]', ('edge_offer', dict(targets=['first'])), app='edge',
             stuck=('Cannot find the small print?', 'Roll the mouse wheel toward you to scroll down. The small print is at the bottom.'),
             notes='Day 8 is the first day a charge happens. That is the end of the free trial.'),
        step('Find the price', ['Find the dollar amount near the top of the page.'],
             '[$12 each month].', ('edge_offer', dict(targets=['price'])), app='edge',
             notes='The price is $12.'),
        step('Find how often you pay', ['Find the words that say how often $12 is charged.'],
             '[each month] near the top, and [every month until you cancel] in the small print.', ('edge_offer', dict(targets=['price'])), app='edge',
             notes='This is the recurring charge: the same amount again and again.'),
        step('Find how to cancel', ['Look at the last line of the small print.'],
             '[Account › Billing › Cancel plan].', ('edge_offer', dict(targets=['cancel'])), app='edge',
             stuck=('No cancel line on your screen?', 'Scroll down. It is the third line of the small print.'),
             notes='A real offer that hides this line is a warning sign.'),
        step('Write the four facts', ['Click the [Week 4 · Worksheet] tab. In [Part 4], click the box and write the four facts.'],
             'your four facts in the box: when it ends, the price, how often, how to cancel.', None,
             write='The four facts:', write_head='Your four facts (worksheet, Part 4):', write_rows=4,
             notes='Walk the room. Accept short notes such as: day 8, $12, every month, Account Billing Cancel plan.', app='edge'),
    ],
    stuck=[('The offer did not open?', 'Click the [Week 4 · Worksheet] tab. In [Part 4], click [Open the practice offer] again.'),
           ('Cannot find a fact?', 'Roll the mouse wheel toward you. The small print is at the bottom of the page.')],
    check=dict(question='Free for 7 days, then $12 each month. You do nothing. What happens?',
               choices=['Nothing is ever charged', '$12 is charged every month until you cancel', '$12 is charged once'], answer=1,
               why='A monthly price keeps charging until you cancel.'),
)

PARTS = [PART1, PART2, PART3, PART4]
# Part 3 opens Word first, then the map, then the task steps (the same order as Week 3).
PART3['steps'] = open_app('word', 'blank document') + PART3['steps']

RESULT = dict(
    title='What I made tonight',
    intro='This page is your finished work. Fill in every box. Your instructor looks at it at the end of class.',
    fields=[('My subject line', 1), ('Who I put in To', 1), ('Who I put in Bcc', 1), ('What Bcc does, in my words', 2),
            ('My comment on the handout (where, what, why)', 2), ('My reply to the comment', 1),
            ('The four offer facts: when it ends, the price, how often, how to cancel', 4), ('One habit I will use in my next group message', 2)],
)

WRAP = dict(
    label='MY RESULT',
    steps=[step('Fill in your result page', ['Turn to the last page of your worksheet, [My result].', 'Fill in every box.'],
                'every box on the [My result] page filled in.', None, card=['My subject line', 'Who I put in To and Bcc', 'What Bcc does', 'My comment and my reply', 'The four offer facts', 'One habit for next time'],
                card_head='Boxes to fill in:', app='edge',
                stuck=('Not sure what to write?', 'Look back at the step that made it. Your Practice Mail, your Word handout and your four facts are still on your screen.'),
                notes='Learners copy what they made into their own words. Walk the room and read a few.')],
    show=['your Practice Mail [Who sees what] box', 'your Word handout with the comment marked [Resolved]', 'your [My result] page, every box filled in'],
    home='Before you send your next group message, check three things: a subject with the day and time, words that welcome everyone, and who is in To and who is in Bcc. Bring one real message you want to improve to Week 5.',
    result=RESULT,
)

QUICK = [
    ('Open Practice Mail', 'Worksheet tab › Part 1 › gold button [Open Practice Mail].'),
    ('Write a message', '[Compose] › click [Subject] and type › click the big box and type.'),
    ('Use Bcc', 'At the right end of the [To] line, click [Bcc]. Addresses in Bcc are hidden from the other people.'),
    ('Send in practice', 'Click the blue [Send] button. Read the [Who sees what] box.'),
    ('Add a Word comment', 'Select the words › [Review] tab › [New Comment] › type › [Post comment].'),
    ('Reply and resolve', 'Click the [Reply] box, type, click the arrow. Then [···] › [Resolve thread].'),
    ('Save in Documents', '[File] › [Save As] › [Browse] › [Documents] › click in [File name], press {Ctrl}+{A}, type the name › [Save].'),
    ('Check an offer', 'Find four facts: when the free days end, the price, how often you pay, and how to cancel.'),
]

WEEK4 = dict(
    guided=True, title='Work together without confusion.', photo='collaboration', nobreak=True,
    warm='When has a message made your next step easy? What information did it include?',
    goals=GOALS, outcomes=OUTCOMES, ready=READY, parts=PARTS, wrap=WRAP, apps=APPS, words=WORDS,
    warm_notes='Two or three answers. Listen for a clear subject, a day and a time, and one thing to do. Tonight teaches exactly those.',
    goals_notes='Read each goal aloud. There are five goals in four parts: Part 1 teaches goals 1 and 2, and each later part teaches one. Learners check the goals off on their worksheet at the end of class.',
    video='week-04', minutes=[30, 17, 30, 18], example_app='mail', css=['ui-week4.css'],
    hero='Tonight you write an email, answer a comment and check an offer.',
    goals_foot='These five skills are on your post-test.',
    done='You wrote a clear request, chose who sees which addresses, answered a comment and checked an offer.',
    show_notes='Walk the room with the roster. Mark Independent, With prompt or Needs practice for each of the five. Re-show only the missing step. Read the My result page as the evidence.',
    home_notes='Close all programs. Select Start fresh on this computer. Handout with comments may stay in Documents. Practice Mail forgets everything when the tab closes.',
    ws_note='Tonight you use two practice pages on our site. Every email address is made up and ends in example.com, so nothing is ever delivered. Practice Mail and the practice offer cannot charge you or send anything outside the page.',
    answer_note='The four parts prepare the five Week 4 post-test items (13 to 17). The My result page is the written evidence.',
    plan_scope='Each part opens with a slide naming the program, then why it matters, a short video clip, the steps and one check question. Week 4 teaches only the five skills on the post-test (items 13 to 17): a clear request, welcoming words, Bcc, comments on one shared copy and a charge that repeats. Every step is one or two actions with what you should see. The video chapters on choosing a channel, meetings and community posts are not played. There is no break and no timer. Minutes below are a guide for pacing, not a clock for learners.',
    jump_labels=['Start', 'Before we start', 'Part 1 · Practice Mail: the request', 'Part 2 · Practice Mail: To and Bcc', 'Part 3 · Word: comments', 'Part 4 · Edge: an offer', 'Wrap-up'],
    quick=QUICK,
    prep='Each station: Microsoft Edge, Microsoft Word that opens without a sign-in, and File Explorer. No email account is needed: Practice Mail (activities/practice-mail.html) works in Edge on every computer and accepts only addresses that end in example.com, which is reserved for examples and accepts no mail. Before class, check that Word can save to Documents on This PC (not only OneDrive), and that Practice Mail and the practice offer open from the Week 4 worksheet. Check sound on the projector: play the first Watch slide. Keep a roster for the end-of-class check. Print the worksheet if you can: the My result page is the written evidence. After your own run-through, delete Handout with comments and select Start fresh on this computer at each station.',
)
