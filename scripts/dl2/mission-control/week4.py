"""Mission Control Week 4, guided build: a request, who sees which addresses, one shared copy, one offer.

Same brief as Week 3 (Britt, 2026-10-12): a beginner must be able to go slide by slide and finish every
task; the class works together from the projected deck; the worksheet repeats every step.

Scope is the five Week 4 skills the pre/post tests measure (items.js 13-17):
  13 a clear request with a deadline · 15 respectful, inclusive wording · 14 what Bcc does
  16 feedback on one shared copy (comment, reply, resolve) · 17 spot a recurring charge
Cut on purpose (no test item): choosing a channel, joining a meeting, community posts, Cc and Reply all
as practice. Part 2 of the old deck ("Join with care") is gone. The opening video is not played whole:
each part plays only its own clip. No break and no timers (Britt's standing rule).

Lab: Microsoft Edge with a Gmail account, Microsoft 365 Word on Windows 10 (not signed in).
Nothing is sent: every address ends in example.com and the lesson says never to click Send.

Inline markup in text (rendered by guided.py): [Label] on-screen name · {Key} keyboard key · «text» exact text.
"""
from week3 import open_app, step

APPS = {
    'gmail': 'Gmail (in Microsoft Edge)',
    'word': 'Microsoft Word',
    'edge': 'Microsoft Edge',
    'excel': 'Microsoft Excel',
    'powerpoint': 'Microsoft PowerPoint',
    'explorer': 'File Explorer',
}

SUBJECT = 'Reply by Friday noon: please review the handout'
TO = ['desk@example.com']
BCC = ['sam@example.com', 'pat@example.com', 'lee@example.com']
BODY_DRAFT = ['Hi guys,', 'Please review the computer-help handout and reply by Friday at noon.', 'Reply by email, or call 304-555-0142 if you prefer.', 'Thank you,']
BODY_FIXED = ['Hi everyone,'] + BODY_DRAFT[1:]
HANDOUT = ['Computer help handout', 'Step 1: Choose one task.', 'Step 2: Visit the learning desk.', 'Step 3: Ask how to repeat it at home.']
COMMENT = 'Add the contact number after the steps so readers can find help.'
NUMBER = 'Help desk: 304-555-0142'
WORD_FILE = 'Handout with comments'
WORD_TYPE = 'Word Document (*.docx)'
COURSE_TITLE = 'Communicate and collaborate with care'

GOALS = [
    dict(app='gmail', text='Write an email request with a subject that names what you need and when.', short='Write a request with a deadline', item=13),
    dict(app='gmail', text='Use words that welcome everyone, and offer a choice instead of guessing.', short='Use words that welcome all', item=15),
    dict(app='gmail', text='Put the right people in To and in Bcc, and know what Bcc does and does not do.', short='Know what Bcc does', item=14),
    dict(app='word', text='Give feedback on one shared copy: write a specific comment, reply, then resolve it.', short='Give feedback on one shared copy', item=16),
    dict(app='edge', text='Check an offer for when it ends, what it costs, how often you pay, and how to cancel.', short='Spot a charge that repeats', item=17),
]

OUTCOMES = [
    'Request: in Gmail, each learner writes a subject with the day and time, types the four-line message with a Friday-at-noon deadline and a phone-or-email choice, and changes «guys» to «everyone». Nothing is sent.',
    'Recipients: each learner puts desk@example.com in To and the three volunteer addresses in Bcc, does not click Send, closes the draft, finds it in Drafts, and can say what Bcc hides and what it does not stop.',
    'Comments: in Word, each learner types the four-line handout, posts the specific comment, adds the Help desk line, replies Added, thank you, resolves the thread, and saves Handout with comments in Documents.',
    'Offer: on the practice page, each learner finds when the free days end (day 8), the price ($12), how often it is charged (each month) and how to cancel (Account › Billing › Cancel plan), and writes all four on the worksheet.',
]


def gmail_compose_draw(**kw):
    return ('gmail_compose', kw)


READY = dict(
    title='Open this worksheet on your computer', app='edge',
    what='It has every step from tonight, a box to check for each one, and a link to the practice offer for Part 4. If you have a printed copy, open it on screen too.',
    steps=[
        step('Open the course website', ['Click [Microsoft Edge] on the taskbar at the bottom.', 'Click the address bar at the top. Type «vublessons.com», press {Enter}.'],
             'the VUB Learning page with course cards.', ('vub_course_path', dict(week=4, week_title=COURSE_TITLE)),
             stuck=('No Edge on the taskbar?', 'Press the {Windows} key, type «Edge» and press {Enter}.'), app='edge',
             notes='If the lab browser opens to another page, the address bar is still the long box at the top.'),
        step('Open your Week 4 worksheet', ['On the [Digital Literacy — Level 2] card, click [Open course].', 'Scroll down to [Week 4]. Click [Worksheet].'],
             'a page titled [Week 4 · Worksheet]. Leave it open: you need it in Part 4.', ('vub_course_path', dict(week=4, week_title=COURSE_TITLE)),
             stuck=('Cannot find Week 4?', 'Roll the mouse wheel toward you to scroll down. The weeks are in order.'), app='edge',
             notes='Learners may also have a printed copy. The worksheet tab stays open for the practice offer link in Part 4.'),
    ])

# ---------------------------------------------------------------- Part 1: the request (Gmail)
P1_MAP = dict(title='Find your way around the message', draw=('gmail_compose', dict(targets=['to', 'subject', 'body', 'send'])),
              items=['[To]: who gets the message.', '[Subject]: the line people read first.', 'The big white box: your message.', '[Send]: do not click it tonight. Nothing leaves your computer until you do.'],
              notes='Point to each part on the projector. Say it twice: tonight we only write drafts, and nobody clicks Send. Every address ends in example.com, which cannot receive mail.')

PART1 = dict(
    app='gmail', title='Write a request people can act on', goals=[0, 1],
    what='Gmail is email you read and write in your web browser. Tonight you write a message but never send it.',
    make='a draft email that asks for a review, with the day and time in the subject.',
    start='An empty Gmail inbox.',
    finish='A draft with a subject that names the request and the deadline, a message with a day and time, and words that welcome everyone.',
    open_note='Everyone opens Gmail in a new Edge tab. Anyone who cannot sign in is the first thing to help.',
    tell=dict(title='A request someone can act on.',
              points=['Put what you need and when in the [subject]. People read it first.', 'Ask for one thing, with a day and a time.',
                      'Welcome everyone: write [Hi everyone], not [Hi guys]. Offer a choice, like email or a phone call.'],
              notes='Ask: which message in your inbox was easy to answer? Usually it said what and by when. Tonight we write one, and fix a word that leaves people out.'),
    watch=[dict(title='Watch: a message someone can act on', start=85.1, end=130.3, look='a subject and a message that say what to review and when.',
                notes='Plays 1:25 to 2:10 of the Week 4 video and stops on its own. It ends before the part about checking recipients, which is Part 2.')],
    steps=[
        step('Open Gmail', ['In Edge, click the [+] next to the tabs to open a new tab.', 'Type «mail.google.com» and press {Enter}.'],
             'your Gmail inbox, with a [Compose] button at the top left.', ('gmail_inbox', dict(targets=[])),
             stuck=('A sign-in page?', 'Sign in with your Gmail address and password, the way you do in Computer Skills. Ask your instructor if you cannot.'), app='gmail',
             notes='Check that every screen reaches an inbox before going on. Help anyone who cannot sign in now.'),
        step('Start a new message', ['Click [Compose] at the top left.'],
             'a small window titled [New Message] at the bottom right.', ('gmail_inbox', dict(targets=['compose'])),
             stuck=('No Compose button?', 'Make the Edge window full size: double-click the very top edge of the window.'),
             notes='Tonight is drafts only. Say it now: nobody clicks Send.', opener=True),
        dict(kind='map', **P1_MAP),
        step('Type the subject', ['Click in the [Subject] box.', f'Type «{SUBJECT}»'],
             'your subject at the top of the message.', ('gmail_compose', dict(subject=SUBJECT, cursor='subject', targets=['subject'])),
             stuck=('Typed it in the wrong box?', 'Click in the [Subject] box, press {Ctrl} and {A}, and type the subject again.'),
             notes='The subject carries the request and the deadline: Friday noon.'),
        step('Type the message', ['Click the big white box. Type the lines on the right. Press {Enter} after each.', 'Then type your first name.'],
             'four lines and your name in the box.', None, card=BODY_DRAFT,
             stuck=('Made a typing mistake?', 'Press {Backspace} to erase the letter before the blinking line, then type it again.'),
             notes='The first line says «Hi guys,» on purpose. We fix it in the next step. Read the lines aloud slowly.'),
        step('Make the words welcome everyone', ['Double-click the word [guys] in your first line. It turns shaded.', 'Type «everyone»'],
             'the first line now says «Hi everyone,».', ('gmail_compose', dict(subject=SUBJECT, body=BODY_FIXED, cursor='body', targets=['body'])),
             stuck=('The comma disappeared?', 'Click right after «everyone» and type «,» again.'),
             notes='A word like guys leaves some people out. Everyone leaves nobody out. The phone line is the other fix: it offers a choice.'),
        step('Read it like your reader', ['Look at the subject and the message. Find the day and the time you need an answer.'],
             'the day [Friday] and the time [noon] in the subject and in the message.', ('gmail_compose', dict(subject=SUBJECT, body=BODY_FIXED, targets=['subject', 'body'])),
             notes='Could the reader act without asking what you meant? Walk the room and read a few subjects aloud.'),
    ],
    stuck=[('A sign-in page?', 'Sign in with your Gmail address and password. Ask your instructor if you cannot.'),
           ('Clicked [Send] by mistake?', 'Nothing is delivered: every address ends in example.com. Tell your instructor.'),
           ('Made a typing mistake?', 'Press {Backspace} to erase the letter before the blinking line.')],
    check=[dict(question='Which subject line is easiest to act on?',
                choices=['Hello from the learning desk', 'Reply by Thu 5 p.m.: bring the sign-in sheet?', 'Sign-in sheet'], answer=1,
                why='It says what you need and when, so the reader can act.'),
           dict(question='Which invitation is the most welcoming?',
                choices=['Bring your husband or wife.', 'Bring a guest if you like.', 'Wives are welcome.'], answer=1,
                why='It does not guess who someone is or who they live with. It offers a choice.')],
)

# ---------------------------------------------------------------- Part 2: To and Bcc (Gmail, same draft)
FULL = dict(subject=SUBJECT, body=BODY_FIXED[:3])
PART2 = dict(
    app='gmail', still=True, title='Choose who sees which addresses', goals=[2],
    what='The To and Bcc lines decide who gets the message, and who can see whose address.',
    make='the same draft with one address in To and three in Bcc.',
    start='A draft with a subject and a message, and nobody to send it to.',
    finish='A draft with desk@example.com in To and three volunteers in Bcc, saved in Drafts. You never click Send.',
    open_note='We stay in Gmail, in the same message. Do not close it.',
    tell=dict(title='To, Cc and Bcc.',
              points=['[To]: the person who needs to act.', '[Cc]: a visible copy for people who only need to know.',
                      '[Bcc]: hides each person\'s address from the others. It does not stop anyone from forwarding the message.'],
              notes='Ask: when is it a problem if 30 people can see each other\'s addresses? Bcc protects addresses. It does not make the message secret.'),
    watch=[dict(title='Watch: who receives it', start=132.0, end=152.0, look='the To, Cc and Bcc lines, and what Bcc hides.',
                notes='Plays 2:12 to 2:32 and stops on its own, before the part about Reply all, which we are not practicing tonight.')],
    steps=[
        step('Add who answers', ['Click the top line of the message, the one marked [To] or [Recipients].', f'Type «{TO[0]}» and press {{Enter}}.'],
             'the address in a gray bubble on the [To] line.', ('gmail_compose', dict(to=TO, cursor='to', targets=['to'], **FULL)),
             stuck=('Gmail shows a list of names under the box?', 'Keep typing the whole address and press {Enter}. Ignore the list.'),
             notes='This is the organizer\'s own desk address. The volunteers go in Bcc.'),
        step('Open the Bcc line', ['At the right end of the [To] line, click [Bcc].'],
             'a new line marked [Bcc] under [To].', ('gmail_compose', dict(to=TO, targets=['bcc_link'], **FULL)),
             stuck=('Cannot find [Bcc]?', 'Look at the right end of the [To] line. [Cc] and [Bcc] are two small words. Click in the [To] line first.'),
             notes='Bcc stays out of the way until you ask for it.'),
        step('Add the volunteers', ['Click in the [Bcc] line.', 'Type each address below. Press {Enter} after each one.'],
             'three gray bubbles on the [Bcc] line.', None, card=BCC,
             stuck=('The bubbles did not appear?', 'Press {Enter} or {Tab} right after you type each address.'),
             notes='These three people do not know each other. Bcc keeps their addresses from the others.'),
        step('Check who sees what', ['Look at your [To] line and your [Bcc] line.'],
             'one address in [To] and three in [Bcc]. Each volunteer sees only the [To] address, not the other volunteers.',
             ('gmail_compose', dict(to=TO, bcc=BCC, show_bcc=True, targets=['to', 'bcc'], **FULL)),
             notes='Say it: the three in Bcc cannot see each other. They can still forward the message.'),
        step('Close the draft', ['Do not click [Send]. Click the [X] at the top right of the message window.'],
             'the message window closes. Gmail keeps your message as a draft.', ('gmail_compose', dict(to=TO, bcc=BCC, show_bcc=True, targets=['close'], **FULL)),
             stuck=('Asked whether to save or discard?', 'Choose to save it. Gmail keeps a draft automatically.'),
             notes='Closing with the X is safe. Gmail saves drafts by itself.'),
        step('Find your draft', ['Click [Drafts] in the list on the left.'],
             f'one draft with the subject [{SUBJECT}].', ('gmail_drafts', dict(subject=SUBJECT, targets=['drafts'])),
             stuck=('No Drafts folder in the list?', 'Click [More] in the list on the left, then [Drafts].'),
             notes='Leave the draft in place. Your instructor checks it at the end of class.'),
    ],
    stuck=[('Cannot find [Bcc]?', 'Look at the right end of the [To] line. Click in the [To] line first.'),
           ('A name list appears as you type?', 'Keep typing the whole address and press {Enter}.'),
           ('Clicked [Send] by mistake?', 'Nothing is delivered: every address ends in example.com. Tell your instructor.')],
    check=dict(question='You email 12 members of a community group who do not know each other, and you put their addresses in Bcc. What does Bcc do?',
               choices=['Each person cannot see the other addresses', 'Nobody can forward the email', 'Only those 12 people can open the email'], answer=0,
               why='Bcc hides addresses from the other recipients. It does not stop forwarding or protect the message.'),
)

# ---------------------------------------------------------------- Part 3: comments on one shared copy (Word)
P3_MAP = dict(title='Find your way around the Review tab', draw=('word_review', dict(stage='page', tab='Review', targets=['Review', 'New Comment'])),
              items=['The [Review] tab: comments live here.', '[New Comment]: adds a comment to the words you selected.', 'The comment appears in a box on the right of the page.'],
              notes='Point to each part on the projector. Tonight one person plays both roles on one copy. In real life the copy lives in one shared place, and each person comments on that same file.')


def save_word():
    return [
        step('Save: open the Save As box', ['Click [File] at the top left.', 'Click [Save As], then click [Browse].'],
             'a box titled [Save As].', ('file_menu', dict(app='word', step='both')),
             stuck=('Not sure you clicked File?', 'File is the first word in the row of tabs, above the buttons.'),
             notes='The same three clicks as in Week 3.'),
        step('Choose Documents', ['On the left side of the box, click [Documents].'],
             'the top of the box ends in [Documents].', ('save_as_dialog', dict(location=['This PC', 'Documents'], items=[], savetype=WORD_TYPE, app='word', targets=['documents'])),
             notes='Documents is the folder learners used last week.'),
        step('Name it and save', ['Click in the [File name] box. Press {Ctrl} and {A} together to highlight the old name.', f'Type «{WORD_FILE}». Click [Save].'],
             f'«{WORD_FILE}» at the very top of the window.', ('save_as_dialog', dict(location=['This PC', 'Documents'], items=[], filename=WORD_FILE, savetype=WORD_TYPE, app='word', targets=['filename', 'save'])),
             stuck=('Typed the name next to the old one?', 'Click in the box again, press {Ctrl} and {A}, and type the name again.'),
             notes='Check a few screens: the window title should read Handout with comments.'),
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
        step('Type the handout', ['Click the page. Type the four lines below. Press {Enter} at the end of each line.'],
             'four lines, all the same size.', None, card=HANDOUT,
             stuck=('Made a typing mistake?', 'Press {Backspace} to erase the letter before the blinking line, then type it again.'),
             notes='Spelling does not need to be perfect. The comment is the point.'),
        step('Be the reviewer: select a line', ['Point just before the «S» in «Step 3: Ask how to repeat it at home.»', 'Hold the left mouse button down. Drag to the end of that line. Let go.'],
             'the Step 3 line shaded gray: selected.', ('word_review', dict(stage='page', tab='Home', selected=True)),
             stuck=('Lost the shading?', 'Click anywhere on the page and try the drag again, slowly.'),
             notes='You practiced dragging in Week 3. Demonstrate it once more, slowly.'),
        step('Add a comment', ['Click the [Review] tab.', 'Click [New Comment].'],
             'a comment box on the right side of the page, with a blinking line.', ('word_review', dict(stage='page', tab='Review', selected=True, targets=['Review', 'New Comment'])),
             stuck=('No [New Comment] button?', 'Click the [Review] tab first. It is in the row of tabs above the buttons.'),
             notes='The comment is tied to the words you selected.'),
        step('Write a specific comment', [f'Type «{COMMENT}»', 'Click [Post comment].'],
             'your comment in a box on the right.', ('word_review', dict(stage='typing', selected=True, targets=['Post'])),
             stuck=('No [Post comment] button?', 'Press {Ctrl} and {Enter} together.'),
             notes='Point out where, what and why: after the steps, add the contact number, so readers can find help.'),
        step('Be the owner: make the change', ['Click at the end of the line «Step 3: Ask how to repeat it at home.» Press {Enter}.', f'Type «{NUMBER}»'],
             'a new line under Step 3 that says «Help desk: 304-555-0142».', ('word_review', dict(stage='posted', added=True)),
             stuck=('The new line is shaded or crossed out?', 'Click anywhere else on the page. The shading was the selection.'),
             notes='Use the number on the slide. A comment is a request; the owner decides and makes the change.'),
        step('Reply to the comment', ['Click the [Reply] box under your comment.', 'Type «Added, thank you.» Click the small arrow button.'],
             'your reply under the comment.', ('word_review', dict(stage='posted', added=True, targets=['Reply'])),
             stuck=('No arrow button?', 'Press {Enter}, or {Ctrl} and {Enter} together.'),
             notes='The reply tells the reviewer the change is done.'),
        step('Resolve the comment', ['Click the three dots [···] at the top right of the comment.', 'Click [Resolve thread].'],
             'the comment turns gray and says [Resolved].', ('word_review', dict(stage='menu', added=True, targets=['more', 'Resolve'])),
             stuck=('A [Resolve] button instead of three dots?', 'Click [Resolve]. Your Word shows it that way.'),
             notes='Resolved comments are hidden from view, not deleted. They stay in the file.'),
    ] + save_word(),
    stuck=[('No [New Comment] button?', 'Click the [Review] tab first.'),
           ('Cannot find [Resolve thread]?', 'Click the three dots at the top right of the comment box.'),
           ('A box asks you to sign in?', 'Close it with the [X]. You do not need an account tonight.')],
    check=dict(question='You added the number the comment asked for. What next?',
               choices=['Delete the comment', 'Reply "Added", then resolve the comment', 'Leave the comment as it is'], answer=1,
               why='The reply tells the reviewer. Resolving closes the comment.'),
)

# ---------------------------------------------------------------- Part 4: an offer (Edge)
OFFER_LINK = '/courses/digital-literacy-2/activities/free-trial-offer.html'
PART4 = dict(
    app='edge', title='Check an offer before you agree', goals=[4],
    what='Microsoft Edge shows web pages. Tonight we read a practice offer. Nothing on it can charge you.',
    make='four facts about a free trial, written down before you would agree.',
    start='A practice offer: Free for 7 days, then $12 each month.',
    finish='Four facts on your worksheet: when the free days end, the price, how often you pay, and how to cancel.',
    open_note='We are back in Edge, on a practice page. Everyone starts from the worksheet tab.',
    worksheet_extra=(f'<p class="g-download"><a class="g-download-button" href="{OFFER_LINK}" target="_blank" rel="noopener">Open the practice offer</a> '
                     '<span>It opens in a new tab. It is a practice page: nothing on it can charge you.</span></p>'),
    tell=dict(title='A free trial can become a monthly charge.',
              points=['[Free for 7 days, then $12 each month] means a charge every month until you cancel.',
                      'Before you agree, find four facts: [when it ends], [what it costs], [how often you pay], [how to cancel].', 'A fact is missing? Do not agree yet.'],
              notes='Ask: has a free trial ever turned into a charge? The four facts are the habit. The offer tonight is fictional.'),
    watch=[dict(title='Watch: review an offer', start=361.1, end=386.9, look='the trial, the monthly price, and what to check before you accept.',
                notes='Plays 6:01 to 6:27 and stops on its own, before the video discusses logos and the practice wrap-up.')],
    steps=[
        step('Open the practice offer', ['In Edge, click the [Week 4 · Worksheet] tab. Scroll to [Part 4].', 'Click [Open the practice offer].'],
             'a new tab named [MapleStream · Practice offer].', ('edge_worksheet_link', dict(week=4, part='Part 4', label='Open the practice offer')), app='edge',
             stuck=('Cannot find the worksheet tab?', 'Click the tabs at the top of Edge. The one named Week 4 · Worksheet has the link.'),
             notes='The offer opens in a new tab, so the worksheet stays open beside it.', opener=True),
        step('Find when the free days end', ['Read the big words at the top of the page.', 'Find the line in the small print that says when the first charge happens.'],
             '[Free for 7 days] and [Your first charge is on day 8.]', ('edge_offer', dict(targets=['trial', 'first'])), app='edge',
             stuck=('Cannot find the small print?', 'Roll the mouse wheel toward you to scroll down. The small print is at the bottom.'),
             notes='Day 8 is the first day a charge happens. That is the end of the free trial.'),
        step('Find the price and how often', ['Find the dollar amount near the top.', 'Find the words that say how often it is charged.'],
             '[$12 each month]. The small print says it repeats every month until you cancel.', ('edge_offer', dict(targets=['price'])), app='edge',
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
_p3 = PART3['steps']
PART3['steps'] = open_app('word', 'blank document') + [_p3[0]] + _p3[1:]

WRAP = dict(
    label='GMAIL', show_first=True,
    steps=[step('Delete your practice draft', ['In Gmail, click [Drafts] and click your draft to open it.', 'Click the trash can at the bottom right of the message.'],
                'your draft is gone from the [Drafts] list.', ('gmail_compose', dict(to=TO, bcc=BCC, show_bcc=True, targets=['trash'], **FULL)), app='gmail',
                stuck=('No trash can on the draft?', 'Click the three dots at the bottom right, then [Discard draft].'),
                notes='Do this after your instructor has checked the draft. A discarded draft leaves nothing in the learner\'s account.')],
    show=['your draft in Gmail: the day and time in the subject, one address in To and three in Bcc', 'your Word handout with the comment answered and marked [Resolved]',
          'your four offer facts, written on the worksheet'],
    home='Before you send your next group message, check three things: a subject with the day and time, words that welcome everyone, and who is in To and who is in Bcc. Bring one real message you want to improve to Week 5.',
)

QUICK = [
    ('Open Gmail', 'Click the [+] for a new tab › type «mail.google.com» › {Enter}.'),
    ('Write a draft', '[Compose] › click [Subject] › type the message. Never click [Send] in class.'),
    ('Use Bcc', 'At the right end of the [To] line, click [Bcc]. Addresses in Bcc are hidden from the other people.'),
    ('Close and find a draft', 'Click the [X] at the top right of the message. Open [Drafts] on the left.'),
    ('Add a Word comment', 'Select the words › [Review] tab › [New Comment] › type › [Post comment].'),
    ('Reply and resolve', 'Click the [Reply] box, type, click the arrow. Then [···] › [Resolve thread].'),
    ('Save in Documents', '[File] › [Save As] › [Browse] › [Documents] › click in [File name], press {Ctrl}+{A}, type the name › [Save].'),
    ('Check an offer', 'Find four facts: when the free days end, the price, how often you pay, and how to cancel.'),
]

WEEK4 = dict(
    guided=True, title='Work together without confusion.', photo='collaboration', nobreak=True,
    warm='When has a message made your next step easy? What information did it include?',
    goals=GOALS, outcomes=OUTCOMES, ready=READY, parts=PARTS, wrap=WRAP, apps=APPS,
    video='week-04', minutes=[28, 15, 32, 20], example_app='gmail', css=['ui-week4.css'],
    hero='Tonight you write an email, answer a comment and check an offer.',
    goals_foot='These five skills are on your post-test.',
    done='You wrote a clear request, chose who sees which addresses, answered a comment and checked an offer.',
    show_notes='Walk the room with the roster. Mark Independent, With prompt or Needs practice for each of the five. Re-show only the missing step. Check the draft before anyone deletes it.',
    home_notes='Learners delete the practice draft, then close all programs. Select Start fresh on this computer. Handout with comments may stay in Documents.',
    ws_note='Tonight you use your own Gmail account to write a draft. You send nothing: never click Send. Every email address is made up and ends in example.com, so nothing could be delivered. The offer page is a practice page.',
    answer_note='The four parts prepare the five Week 4 post-test items (13 to 17).',
    plan_scope='Each part opens with a slide naming the program, then why it matters, a short video clip, the steps and one check question. Week 4 teaches only the five skills on the post-test (items 13 to 17): a clear request, welcoming words, Bcc, comments on one shared copy and a charge that repeats. The video chapters on choosing a channel, meetings and community posts are not played. There is no break and no timer. Minutes below are a guide for pacing, not a clock for learners.',
    jump_labels=['Start', 'Before we start', 'Part 1 · Gmail: the request', 'Part 2 · Gmail: To and Bcc', 'Part 3 · Word: comments', 'Part 4 · Edge: an offer', 'Wrap-up'],
    quick=QUICK,
    prep='Each station: Microsoft Edge signed in to a Gmail account (learners use their own from Computer Skills, or a class account), Microsoft Word that opens without a sign-in, and File Explorer. Before class, confirm every learner can sign in to Gmail, that Word can save to Documents on This PC (not only OneDrive), that the practice offer opens from the Week 4 worksheet, and that no old practice drafts are left. All addresses end in example.com, which is reserved for examples and does not accept mail, so a message sent by mistake only bounces back. Check sound on the projector: play the first Watch slide. Keep a roster for the end-of-class check. After your own run-through, discard your practice draft, delete Handout with comments, and select Start fresh on this computer at each station.',
)
