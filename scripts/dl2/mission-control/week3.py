"""Mission Control Week 3, guided build: one program at a time, one or two clicks per slide.

Britt's brief (2026-10-12): a beginner must be able to go slide by slide and finish every task;
a missing critical step is a failure. The class works together from the projected deck; the
worksheet repeats every step for anyone who falls behind.

Scope is the four Week 3 skills the pre/post tests measure (items.js 9-12):
  9 real heading styles · 12 share a file that looks the same everywhere (PDF)
  10 a SUM total that updates · 11 use a licensed photo properly (crop + credit)
Britt also kept numbered steps in Word and a PowerPoint design theme. Track Changes, the
link and copy/paste/undo practice, the chart, alt text, the three-slide deck and the video
trim/split were cut on purpose. The opening video is not played whole: each part plays only
its own clip, and no clip covers a cut topic. No break and no timers (Britt's standing rule).

Lab: Microsoft 365 desktop apps on Windows 10, not signed in, Microsoft Edge.

Inline markup used in text (rendered by guided.py):
  [Label]   an on-screen name to find and click (bold)
  {Key}     a keyboard key
  «text»    exactly what to type, or text to find on screen
"""

APPS = {
    'word': 'Microsoft Word',
    'excel': 'Microsoft Excel',
    'powerpoint': 'Microsoft PowerPoint',
    'edge': 'Microsoft Edge',
    'explorer': 'File Explorer',
}

# What learners type in Word. Style names drive the drawings of the page.
HANDOUT = [
    ('Computer help at the library', 'h1'),
    ('Who it helps', 'h2'),
    ('Anyone who wants to practice one computer task.', 'body'),
    ('Steps', 'h2'),
    ('Choose one task.', 'step'),
    ('Visit the learning desk.', 'step'),
    ('Ask how to repeat it at home.', 'step'),
]
PLAIN = [(text, 'body') for text, _ in HANDOUT]
SUPPLIES = [('Paper', '12'), ('Folders', '8'), ('Pens', '5')]
CREDIT = 'Photo: VUB practice photo, used with permission.'
FOLDER = 'Resource pack'
FILES = {'word': 'Computer help handout', 'excel': 'Supply list', 'powerpoint': 'Flyer'}

# Learner-facing goals. One per part, each matched to the test item it prepares for.
GOALS = [
    dict(app='word', text='Make headings Word can find, using Heading 1 and Heading 2, not just bold.', short='Make headings Word can find', item=9),
    dict(app='word', text='Save a handout as a PDF, so it looks the same on any computer or printer.', short='Save a PDF that looks the same everywhere', item=12),
    dict(app='excel', text='Add costs with a formula that updates by itself when a cost changes.', short='Add costs with a total that updates', item=10),
    dict(app='powerpoint', text='Use a photo the right way: crop it, and give the credit its permission asks for.', short='Use a photo the right way', item=11),
]

# Instructor outcomes (measurable). Shown in the lesson plan.
OUTCOMES = [
    'Headings: in Word, each learner types the seven handout lines, applies Heading 1 to the title and Heading 2 to Who it helps and Steps, numbers the three steps, and shows all three headings in the Navigation Pane. No heading made with bold alone.',
    'PDF: each learner saves the handout as a PDF in the Resource pack folder, opens it, and says why a neighbor without Word should get the PDF.',
    'Formula: in Excel, each learner types the supply list, enters =SUM(B2:B4) in B5 (25), writes a prediction, changes Paper to 15, sees 28, and saves Supply list as an Excel workbook.',
    'Photo: in PowerPoint, each learner picks a theme, types the title and the credit line, inserts the practice photo, crops it, and saves Flyer; they can say why the credit line is there.',
]


def step(title, actions, see, draw=None, stuck=None, notes='', app=None, card=None, write=None, opener=False):
    """One projected step. actions: 1-2 short instructions. see: what success looks like.
    draw: (function name in ui.py, kwargs) for the drawing. card: lines to type, shown large.
    write: a worksheet prompt the learner answers in writing (gets a text box)."""
    assert 1 <= len(actions) <= 2, title
    return dict(kind='step', title=title, actions=list(actions), see=see, draw=draw, stuck=stuck, notes=notes, app=app, card=card, write=write, opener=opener)


def open_app(app, label):
    name = APPS[app]
    short = name.split()[-1]
    tile = {'word': 'Blank document', 'excel': 'Blank workbook', 'powerpoint': 'Blank Presentation'}[app]
    return [
        step(f'Open {short}', ['Press the {Windows} key on your keyboard. (Or click [Start] at the bottom left.)', f'Type «{short}» and press {{Enter}}.'],
             f'the {short} start screen, with a [{tile}] tile.', ('start_search', dict(app=app)),
             stuck=(f'{short} did not open?', f'Click [Start], scroll the list of apps to [{short}], and click it.'),
             notes=f'Say the keys aloud: Windows key, type {short}, Enter. Wait until every screen shows {short}.'),
        step(f'Start a {label}', [f'Click [{tile}].'],
             label_see(app), ('office_start', dict(app=app)),
             stuck=('Already looking at an empty page?', 'Your computer skips the start screen. Go on to the next step. A sign-in box? Close it with its [X]; no account is needed.'),
             notes=f'Walk the room. Everyone should see an empty {label}.', opener=True),
    ]


def label_see(app):
    return {
        'word': 'a white page with a blinking line at the top. The blinking line is the cursor: where your typing goes.',
        'excel': 'a grid of empty boxes called cells. The cell [A1] has a green border.',
        'powerpoint': 'one white slide with two boxes: [Click to add title] and [Click to add subtitle].',
    }[app]


def save_steps(app, first_time=False):
    """File > Save As > Browse into Documents > Resource pack, the same three moves in every app."""
    name = FILES[app]
    kind = {'word': 'Word document', 'excel': 'Excel workbook', 'powerpoint': 'PowerPoint presentation'}[app]
    stype = {'word': 'Word Document (*.docx)', 'excel': 'Excel Workbook (*.xlsx)', 'powerpoint': 'PowerPoint Presentation (*.pptx)'}[app]
    out = [step('Save: open the Save As box', ['Click [File] at the top left.', 'Click [Save As], then click [Browse].'],
                'a box titled [Save As].', ('file_menu', dict(app=app, step='both')),
                stuck=('Not sure you clicked File?', 'File is the first word in the row of tabs, above the buttons. Everything turns into a menu when you click it.'),
                notes='The Save As box is the one place every program saves the same way. Point to the title of the box on the projector.')]
    if first_time:
        out += [
            step('Make your Resource pack folder', ['On the left side of the box, click [Documents].', 'Click [New folder] near the top. Type «Resource pack» and press {Enter}.'],
                 'a new folder named [Resource pack].', ('save_as_dialog', dict(location=['This PC', 'Documents'], items=[('Resource pack', 'folder')], savetype=stype, app=app, targets=['documents', 'newfolder'])),
                 stuck=('The new folder is called New folder?', 'Right-click it, choose [Rename], type «Resource pack» and press {Enter}.'),
                 notes='Every file tonight goes in this folder. If someone already has a Resource pack folder from an earlier class, they open that one instead.'),
            step('Open the folder', ['Double-click [Resource pack].'],
                 'the top of the box ends in [Resource pack]. The folder is empty.', ('save_as_dialog', dict(location=['This PC', 'Documents', 'Resource pack'], items=[], savetype=stype, app=app, targets=[])),
                 notes='Double-click means two quick clicks. If it does not open, try again a little faster.'),
        ]
    else:
        out += [step('Open your Resource pack folder', ['On the left side of the box, click [Documents].', 'Double-click [Resource pack].'],
                     'the top of the box ends in [Resource pack].', ('save_as_dialog', dict(location=['This PC', 'Documents'], items=[('Resource pack', 'folder')], savetype=stype, app=app, targets=['documents', 'folder:Resource pack'])),
                     stuck=('The folder looks empty?', f'That is normal. This box only shows {kind}s, and you have not saved one here yet.'),
                     notes='This is the folder from Part 1.')]
    out += [step('Name it and save', ['Click in the [File name] box. Press {Ctrl} and {A} together to highlight the old name.', f'Type «{name}». Click [Save].'],
                 f'«{name}» at the very top of the window.', ('save_as_dialog', dict(location=['This PC', 'Documents', 'Resource pack'], items=[], filename=name, savetype=stype, app=app, targets=['filename', 'save'])),
                 stuck=('Typed the name next to the old one?', 'Click in the box again, press {Ctrl} and {A}, and type the name again.'),
                 notes=f'Check a few screens: the window title should read {name}.')]
    return out


READY = dict(
    title='Open this worksheet on your computer', app='edge',
    what='It has every step from tonight, a box to check for each one, and the practice photo for Part 4. If you have a printed copy, open it on screen too.',
    steps=[
        step('Open the course website', ['Click [Microsoft Edge] on the taskbar at the bottom.', 'Click the address bar at the top. Type «vublessons.com», press {Enter}.'],
             'the VUB Learning page with course cards.', ('vub_course_path', {}),
             stuck=('No Edge on the taskbar?', 'Press the {Windows} key, type «Edge» and press {Enter}.'), app='edge',
             notes='If the lab browser opens to another page, the address bar is still the long box at the top.'),
        step('Open your Week 3 worksheet', ['On the [Digital Literacy — Level 2] card, click [Open course].', 'Scroll down to [Week 3]. Click [Worksheet].'],
             'a page titled [Week 3 · Worksheet]. Leave it open for Part 4.', ('vub_course_path', {}),
             stuck=('Cannot find Week 3?', 'Roll the mouse wheel toward you to scroll down. The weeks are in order.'), app='edge',
             notes='Learners may also have a printed copy. The page still needs to be open for the photo download in Part 4.'),
    ])

PARTS = [
    dict(
        app='word', title='Make a handout with real headings', goal=0,
        what='Word makes documents: letters, flyers and handouts.',
        make='a one-page computer-help handout with real headings and numbered steps.',
        start='Seven plain lines of text, all the same size.',
        finish='A handout whose three headings show in the Navigation Pane, saved in Resource pack.',
        tell=dict(title='Bold is not a heading.',
                  points=['A heading is the title of a section.', 'Bold text only [looks] like a heading. Word cannot find it.',
                          'A heading style, like [Heading 1], tells Word: this is a title. Word then lists it in the [Navigation Pane].'],
                  notes='Ask: when you skim a long letter from the VA, what helps you find your place? Headings. Word can only list headings it knows about.'),
        watch=[dict(title='Watch: make a real heading', start=43.0, end=71.8, look='the title turning into Heading 1, then showing in the Navigation Pane.',
                    notes='Plays 0:43 to 1:12 of the Week 3 video and stops on its own. It ends before the part about links, which we are not doing tonight.')],
        map=dict(title='Find your way around Word', draw=('ribbon', dict(app='word', active_tab='Home', groups=[('Clipboard', ['Paste']), ('Font', ['Bold', 'Italic']), ('Paragraph', ['Bullets', 'Numbering']), ('Styles', ['Normal', 'Heading 1', 'Heading 2'])], targets=['File', 'Home', 'Numbering', 'Heading 1', 'View'])),
                 items=['[File]: save your work.', '[Home] tab: most buttons.', '[Numbering]: makes 1, 2, 3.', '[Styles] box: [Heading 1], [Heading 2].', '[View] tab: Navigation Pane.'],
                 notes='Point to each part on the projector, then ask learners to point to it on their own screen.'),
        steps=[
            step('Type the handout', ['Type the seven lines below. Press {Enter} at the end of each line.'],
                 'seven lines, all the same size and color.', None, card=[t for t, _ in HANDOUT],
                 stuck=('Made a typing mistake?', 'Press {Backspace} to erase the letter before the blinking line, then type it again.'),
                 notes='Read the lines aloud slowly. Spelling does not need to be perfect; the headings are the point.'),
            step('Make the title a Heading 1', ['Click anywhere in the first line, «Computer help at the library».', 'On the [Home] tab, in the [Styles] box, click [Heading 1].'],
                 'the line gets bigger and turns dark blue.', ('word_styles', dict(highlight='Heading 1')),
                 stuck=('Cannot see [Heading 1]?', 'Make the window full size: double-click the very top edge of the window. Or click the small arrow at the right of the [Styles] box.'),
                 notes='This is the key move of Part 1. Check screens before moving on.'),
            step('Make two section headings', ['Click in the line «Who it helps». Click [Heading 2].', 'Click in the line «Steps». Click [Heading 2].'],
                 'both lines turn dark blue. They are a little smaller than the title.', ('word_styles', dict(highlight='Heading 2')),
                 stuck=('Cannot see Heading 2?', 'It is next to [Heading 1] in the [Styles] box on the [Home] tab.'),
                 notes='Heading 2 sits under Heading 1, like a chapter inside a book.'),
            step('Select the three steps', ['Point just before the «C» in «Choose one task.»', 'Hold the left mouse button down. Drag to the end of «home.» Let go.'],
                 'the three step lines shaded gray: selected.', ('word_page', dict(lines=HANDOUT, selected=True)),
                 stuck=('Lost the shading?', 'Click anywhere on the page and try the drag again, slowly.'),
                 notes='Dragging is the hardest move tonight. Demonstrate it twice on the projector, slowly.'),
            step('Number the steps', ['On the [Home] tab, click [Numbering]: the button with 1, 2, 3 on it.'],
                 '«1.», «2.» and «3.» in front of the three steps.', ('word_numbering', {}),
                 stuck=('Got dots instead of numbers?', 'Click [Numbering], the button with numbers. It is next to the button with dots.'),
                 notes='Point out the difference between the dots button and the numbers button.'),
            step('Check your headings', ['Click the [View] tab.', 'Click the box next to [Navigation Pane] so it has a check mark.'],
                 'a panel on the left that lists «Computer help at the library», «Who it helps» and «Steps».', ('word_navpane', {}),
                 stuck=('A heading is missing from the list?', 'Click in that line, click the [Home] tab, and click [Heading 1] or [Heading 2].'),
                 notes='This is the proof the post-test asks about: real headings show in the Navigation Pane; bold text does not.'),
        ] + save_steps('word', first_time=True),
        stuck=[('A box asks you to sign in?', 'Close it with the [X]. You do not need an account tonight.'),
               ('Made a typing mistake?', 'Press {Backspace} to erase the letter before the blinking line.'),
               ('A heading is missing from the Navigation Pane?', 'Click in that line, then click [Heading 1] or [Heading 2] on the [Home] tab.')],
        check=dict(question='Bold text looks like a heading. What proves it is a real heading?',
                   choices=['It is bigger than the other lines', 'It is blue', 'It shows in the Navigation Pane'], answer=2,
                   why='A heading style tells Word the line is a title, so Word lists it in the Navigation Pane. Size and color alone do not.'),
    ),
    dict(
        app='word', still=True, title='Save your handout as a PDF', goal=1,
        what='A PDF is a copy of your document that looks the same on every computer and printer, even one without Word.',
        make='a PDF of your handout, ready to email or print.',
        start='A handout saved as a Word document.',
        finish='A PDF of the handout in Resource pack that looks the same as in Word.',
        tell=dict(title='Word document or PDF?',
                  points=['[Word document]: for you. Keep changing it.', '[PDF]: for other people. It looks the same on any computer or printer, even without Word.',
                          'Keep both. Change the Word document, then make a new PDF.'],
                  notes='Ask: who might get this handout? A neighbor with a phone, the library printer, a family member without Word. They all get the PDF.'),
        watch=[dict(title='Watch: why a PDF', start=354.0, end=362.8, look='the PDF keeping the finished look for reading and printing.',
                    notes='A short clip, 5:54 to 6:03. It stops before the part about CSV files, which we are not doing tonight.')],
        steps=[
            step('Open the Save As box again', ['Click [File] at the top left.', 'Click [Save As], then click [Browse].'],
                 'the [Save As] box. It opens in your [Resource pack] folder.', ('file_menu', dict(app='word', step='both')),
                 stuck=('The box is not in Resource pack?', 'Click [Documents] on the left, then double-click [Resource pack].'),
                 notes='Same three clicks as before.'),
            step('Choose PDF', ['Click the [Save as type] box, just under [File name].', 'In the list, click [PDF (*.pdf)].'],
                 '[Save as type] now says [PDF (*.pdf)].', ('savetype_list', {}),
                 stuck=('The list closed before you clicked PDF?', 'Click the [Save as type] box again. The list opens again.'),
                 notes='The list is long. PDF is about halfway down.'),
            step('Save the PDF', ['Check that [Open file after publishing] has a check mark. If not, click its box.', 'Click [Save].'],
                 'your handout opens as a PDF in Microsoft Edge.', ('save_as_dialog', dict(location=['This PC', 'Documents', 'Resource pack'], items=[], filename='Computer help handout', savetype='PDF (*.pdf)', open_after=True, app='word', targets=['openafter', 'save'])),
                 stuck=('Nothing opened?', 'The PDF is still saved. You will see it in Resource pack at the end of class.'),
                 notes='The PDF keeps the same name as the Word document. The two are different files.'),
            step('Check your PDF', ['Look at the PDF. Find the three blue headings and the numbers 1, 2 and 3.'],
                 'the same headings and numbers you made in Word.', ('pdf_view', {}), app='edge',
                 stuck=('The headings are not blue?', 'Go back to Word, fix the headings, and save the PDF again.'),
                 notes='Leave the PDF open; there is no need to close it. The next part starts a new program.'),
        ],
        stuck=[('The Save As box is not in Resource pack?', 'Click [Documents] on the left, then double-click [Resource pack].'),
               ('Cannot find PDF in the list?', 'Click the [Save as type] box. PDF is about halfway down the list.')],
        check=dict(question='You email your handout as a PDF. What will your neighbor see?',
                   choices=['A blank page without Word', 'Your same headings and layout', 'Plain text, no headings'], answer=1,
                   why='A PDF keeps your layout on any computer, even one without Word.'),
    ),
    dict(
        app='excel', title='Add costs with a total that updates', goal=2,
        what='Excel works with numbers in a grid of boxes called cells.',
        make='a supply list with a total that updates by itself.',
        start='Three supply costs on paper: Paper $12, Folders $8, Pens $5.',
        finish='A supply list whose total changes on its own when a cost changes, saved in Resource pack.',
        tell=dict(title='Every cell has an address.',
                  points=['Columns have letters: A, B, C. Rows have numbers: 1, 2, 3.', '[B5] means column B, row 5.',
                          'A formula starts with «=». Excel works out the answer, and works it out again when a number changes.'],
                  notes='Connect to a household budget: change one bill and the total should change too, without adding it up again by hand.'),
        watch=[dict(title='Watch: a formula that adds', start=130.5, end=195.6, look='the formula =SUM(B2:B4) adding the three costs.',
                    notes='Plays 2:10 to 3:15 and stops on its own, before the narrator changes the paper cost. Learners predict that answer themselves later.')],
        map=dict(title='Find your way around Excel', draw=('excel_grid', dict(cells={}, active='A1', formula='', targets=['formula_bar', 'A1'])),
                 items=['The [formula bar]: shows what is really in a cell.', 'A [cell]: the box where a column and a row meet. This one is [A1].', '[File] is at the top left, the same as in Word.'],
                 notes='Point to column letters across the top and row numbers down the side.'),
        steps=[
            step('Type the labels', ['Click cell [A1]. Type «Item» and press {Tab}.', 'Type «Cost in dollars» and press {Enter}.'],
                 '«Item» in A1 and «Cost in dollars» in B1.', ('excel_grid', dict(cells={'A1': 'Item', 'B1': 'Cost in dollars'}, active='A2', formula='')),
                 stuck=('Typed in the wrong cell?', 'Click that cell and press {Delete}. Then click the right cell and type again.'),
                 notes='Tab moves right. Enter goes down to the start of the next row.'),
            step('Type the supplies', ['In [A2] type «Paper», press {Tab}, type «12», press {Enter}.', 'Do the same for «Folders» and «8», then «Pens» and «5».'],
                 'Paper 12, Folders 8 and Pens 5 in rows 2, 3 and 4.', ('excel_grid', dict(cells={'A1': 'Item', 'B1': 'Cost in dollars', 'A2': 'Paper', 'B2': '12', 'A3': 'Folders', 'B3': '8', 'A4': 'Pens', 'B4': '5'}, active='A5', formula='')),
                 stuck=('A number went in the wrong row?', 'Click it, type the right number, and press {Enter}. The new number replaces the old one.'),
                 notes='Type numbers without a dollar sign; the column label already says dollars.'),
            step('Add the total', ['Click [A5]. Type «Total» and press {Tab}.', 'In [B5], type «=SUM(B2:B4)» and press {Enter}.'],
                 '[B5] shows 25.', ('excel_grid', dict(cells={'A1': 'Item', 'B1': 'Cost in dollars', 'A2': 'Paper', 'B2': '12', 'A3': 'Folders', 'B3': '8', 'A4': 'Pens', 'B4': '5', 'A5': 'Total', 'B5': '25'}, active='B5', formula='=SUM(B2:B4)', targets=['B5'])),
                 stuck=('B5 shows the letters you typed?', 'Click [B5] and type it again. It must start with «=». The «:» means "through": B2 through B4.'),
                 notes='Say each key: equals, S U M, open bracket, B 2, colon, B 4, close bracket, Enter.'),
            step('Look at the formula', ['Click cell [B5].', 'Look at the long box above the column letters: the [formula bar].'],
                 'the cell shows 25. The formula bar shows «=SUM(B2:B4)».', ('excel_grid', dict(cells={'A1': 'Item', 'B1': 'Cost in dollars', 'A2': 'Paper', 'B2': '12', 'A3': 'Folders', 'B3': '8', 'A4': 'Pens', 'B4': '5', 'A5': 'Total', 'B5': '25'}, active='B5', formula='=SUM(B2:B4)', targets=['formula_bar'])),
                 notes='The cell shows the answer. The formula bar shows the formula behind it.'),
            step('Predict', ['Paper is going up from 12 to 15. Before you change anything, guess: what will [B5] show? Say it out loud or write it down.'],
                 'your guess, ready to check.', None, write='If paper costs 15, B5 will show:',
                 notes='Do not give the answer. Wait until everyone has written a number.'),
            step('Change one cost', ['Click cell [B2]. Type «15» and press {Enter}.'],
                 '[B5] changes to 28 by itself. Was your guess right?', ('excel_grid', dict(cells={'A1': 'Item', 'B1': 'Cost in dollars', 'A2': 'Paper', 'B2': '15', 'A3': 'Folders', 'B3': '8', 'A4': 'Pens', 'B4': '5', 'A5': 'Total', 'B5': '28'}, active='B3', formula='8', targets=['B5'])),
                 stuck=('B5 still shows 25?', 'Click [B5] and look at the formula bar. If it shows 25, not the formula, type «=SUM(B2:B4)» in B5 again.'),
                 notes='This is the post-test skill: the formula refers to the cells, so the total updates. A typed 25 would not.'),
        ] + save_steps('excel'),
        stuck=[('B5 shows the letters you typed?', 'It must start with «=». Click [B5] and type «=SUM(B2:B4)» again.'),
               ('Typed in the wrong cell?', 'Click that cell and press {Delete}, then type in the right cell.')],
        check=dict(question='B5 has =SUM(B2:B4) and shows 28. You change Pens from 5 to 7. What will B5 show?',
                   choices=['28, because the total stays the same', '30', '35'], answer=1,
                   why='The formula adds the cells again: 15 + 8 + 7 = 30.'),
    ),
    dict(
        app='powerpoint', title='Use a photo the right way', goal=3,
        what='PowerPoint makes slides for talks, and one-page flyers.',
        make='a one-slide flyer with a photo you have permission to use.',
        start='A practice photo, with permission to use and crop it if you give credit.',
        finish='A flyer with a theme, a title, the credit line and the cropped photo, saved in Resource pack.',
        tell=dict(title='Use photos the right way.',
                  points=['Finding a photo online does not mean you may use it.', 'Our practice photo\'s permission says: you may use it and crop it if you give credit.',
                          'Cropping trims the edges on your slide. The photo file itself does not change.'],
                  notes='Credit line learners will type: ' + CREDIT),
        watch=[dict(title='Watch: permission and credit', start=379.3, end=395.4, look='why a photo from a search still needs permission and credit.',
                    notes='Plays 6:19 to 6:35 and stops on its own.'),
               dict(title='Watch: crop or resize', start=280.3, end=306.2, look='the difference between cropping and making a picture smaller.',
                    notes='Plays 4:40 to 5:06 and stops before the part about alt text, which we are not doing tonight.')],
        map=dict(title='Find your way around PowerPoint', draw=('ribbon', dict(app='powerpoint', active_tab='Home', groups=[('Slides', ['New Slide', 'Layout']), ('Font', ['Bold', 'Italic']), ('Paragraph', ['Bullets'])], targets=['File', 'Insert', 'Design'])),
                 items=['[File]: where you save.', '[Insert] tab: add a picture.', '[Design] tab: choose a theme.'],
                 notes='The tabs are in the same row as in Word. Design and Insert are the two we need.'),
        steps=[
            step('Download the practice photo', ['Click [Microsoft Edge] on the taskbar. Click the [Week 3 · Worksheet] tab.', 'Scroll to [Part 4]. Click [Download the practice photo].'],
                 '«practice-photo.jpg» at the top right.', ('edge_page_download', {}), app='edge',
                 stuck=('The photo opened on its own page instead?', 'Right-click the photo, choose [Save image as], then click [Save]. Two Edge windows? Point at Edge on the taskbar and click the one named Week 3 · Worksheet.'),
                 notes='The photo goes to the Downloads folder. Insert Picture finds it there.'),
            step('Pick a theme', ['Click the [Design] tab.', 'Click any theme you like in the [Themes] row.'],
                 'your slide changes color and style.', ('ppt_themes', {}),
                 stuck=('A [Designer] panel opened on the right?', 'Click the [X] at the top of that panel to close it.'),
                 notes='Any theme is fine. If a Designer panel opens, close it.'),
            step('Type the title', ['Click [Click to add title].', 'Type «Need computer help?»'],
                 'your title on the slide.', ('ppt_window', dict(theme='theme', targets=['title'])),
                 notes='Clicking the box makes the words Click to add title disappear.'),
            step('Type the photo credit', ['Click [Click to add subtitle].', f'Type «{CREDIT}»'],
                 'the credit line under the title.', ('ppt_window', dict(title='Need computer help?', theme='theme', targets=['subtitle'])),
                 notes='This credit line is what the photo\'s permission asks for.'),
            step('Insert the photo', ['Click the [Insert] tab.', 'Click [Pictures], then click [This Device].'],
                 'a box titled [Insert Picture].', ('ppt_insert_pictures', {}),
                 notes='Pictures is near the left of the Insert tab.'),
            step('Choose the photo', ['On the left side of the box, click [Downloads].', 'Click [practice-photo], then click [Insert].'],
                 'the photo on your slide. If a [Designer] panel opens on the right, click the [X] at the top of that panel.', ('insert_picture_dialog', {}),
                 stuck=('No practice-photo in Downloads?', 'Go back to Edge and click [Download the practice photo] again.'),
                 notes='The photo will cover the words for a moment. The next two steps fix that.'),
            step('Crop the photo', ['Click the photo. Click the [Picture Format] tab, then [Crop].', 'Drag a black mark on one side inward. Press {Esc}.'],
                 'that edge trimmed away.', ('ppt_crop', {}),
                 stuck=('A small menu opened under [Crop]?', 'Click [Crop] at the top of that menu. (No [Picture Format] tab? Click the photo once first.)'),
                 notes='Cropping trims the slide view only. The file in Downloads is unchanged; that is the post-test idea.'),
            step('Make it fit', ['Drag a corner circle of the photo inward to shrink it.', 'Drag the middle of the photo off your words.'],
                 'the title, the credit line and the photo, all in view.', ('ppt_window', dict(title='Need computer help?', subtitle=CREDIT, theme='theme', photo='cropped')),
                 stuck=('The photo got squashed?', 'Drag a corner circle, not a side. Corners keep the shape.'),
                 notes='Corners keep the proportions. Side handles stretch the photo.'),
        ] + save_steps('powerpoint'),
        stuck=[('A [Designer] panel opened on the right?', 'Click the [X] at the top of that panel to close it.'),
               ('No Picture Format tab?', 'Click once on the photo. The tab appears only while the photo is selected.'),
               ('No practice-photo in Downloads?', 'In Edge, click [Download the practice photo] again.')],
        check=dict(question='Why does the flyer have a photo credit line?',
                   choices=['To fill empty space', 'PowerPoint needs a caption', 'The photo\'s permission asks for it'], answer=2,
                   why='The photo\'s permission says: use it if you give credit.'),
    ),
]
# Order inside a part: any Edge step that must come first (the photo download), then open the
# program, then the "find your way around" map, then the task steps.
for _part in PARTS:
    if _part.get('still'):
        continue
    label = {'word': 'blank document', 'excel': 'blank workbook', 'powerpoint': 'blank presentation'}[_part['app']]
    lead = [s for s in _part['steps'] if s.get('app') == 'edge']
    rest = [s for s in _part['steps'] if s.get('app') != 'edge']
    _part['steps'] = lead + open_app(_part['app'], label) + [dict(kind='map', **_part['map'])] + rest


WRAP = dict(
    files=step('Check your Resource pack', ['Click [File Explorer] (the yellow folder) on the taskbar.', 'Click [Documents], then double-click [Resource pack].'],
               'four files: the handout (Word and PDF), [Supply list] and [Flyer].', ('explorer_resource_pack', {}), app='explorer',
               stuck=('A file is missing?', 'Open that program again with the {Windows} key, then use [File] › [Save As] › [Browse] into Resource pack.'),
               notes='This is the evidence check. Walk the room with the roster.'),
    show=['the Navigation Pane in Word listing your three headings', 'your PDF', '[B5] showing 28 and the formula bar showing «=SUM(B2:B4)»', 'your flyer with the credit line'],
    home='Make one real handout with a heading and numbered steps, or a short list of costs with a SUM total. Bring one thing you noticed to Week 4.',
)

WEEK3 = dict(
    guided=True, title='Make a useful resource pack.', photo='resource-pack', nobreak=True,
    warm='Think of a flyer or handout that was easy to follow. What made it easy?',
    goals=GOALS, outcomes=OUTCOMES, ready=READY, parts=PARTS, wrap=WRAP, apps=APPS, credit=CREDIT,
    prep='Each station: Microsoft Word, Excel and PowerPoint that open without a sign-in, Microsoft Edge, and File Explorer on the taskbar. Before class, check that Word can save to Documents on This PC (not only OneDrive), that Edge can download the practice photo from the Week 3 worksheet, and that no old Resource pack folder is left in Documents. Check sound on the projector: play the first Watch slide. Keep a roster for the end-of-class check. After your own run-through, delete your Resource pack folder and the downloaded photo, then select Start fresh on this computer at each station.',
)
