"""Original, fictional desktop walkthroughs synchronized to Britt's word alignment.

These are authored screen simulations, not recordings of a commercial product.
Each state shows a real task transition; all cues must resolve in the narration.
"""
import html
import json
import re

E = lambda value: html.escape(str(value), quote=True)
NAVY, INK, GOLD, PAPER, LINE = '#1B365D', '#18334d', '#E6C65C', '#F5F7FA', '#bacbd5'
SELECTED = {(1, 1), (1, 6), (2, 5), (2, 6), (3, 1), (3, 4),
            (4, 3), (4, 5), (5, 3), (5, 6), (6, 5), (6, 6)}


def box(x, y, w, h, fill=PAPER, stroke=None, radius=8):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}"' + (f' stroke="{stroke}" stroke-width="2"' if stroke else '') + '/>'


def txt(value, x, y, size=28, fill=INK, weight=400):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" font-weight="{weight}">{E(value)}</text>'


def lines(values, x, y, size=28, gap=38, fill=INK):
    return ''.join(txt(v, x, y + j * gap, size, fill) for j, v in enumerate(values))


def button(value, x, y, w=180, active=False):
    return box(x, y, w, 48, GOLD if active else NAVY) + txt(value, x+16, y+33, 27, INK if active else PAPER, 700)


def field(label, value, x, y, w=480, focus=False, typing=False):
    value_text=txt(value, x+16, y+46)
    if typing:value_text=value_text.replace('<text ', '<text data-type="true" ',1)
    return txt(label, x, y, 26) + box(x, y+12, w, 51, '#fff', NAVY if focus else LINE) + value_text


def chrome(title, address='Practice workspace • fictional data'):
    return box(0, 0, 1200, 500, '#e5edf2', NAVY, 14) + box(0, 0, 1200, 52, NAVY, radius=0) + txt(title, 24, 36, 28, PAPER, 700) + txt('−  □  ×', 1084, 35, 27, PAPER) + box(18, 65, 1164, 48, '#fff', LINE) + txt(address, 40, 98, 27) + txt('⋮', 1146, 100, 30)


def zoom(stage):
    s = chrome('VUB Practice Browser', 'library.example • Computer help')
    big = stage in (3, 4)
    s += box(30, 132, 1140, 348, '#fff')
    s += txt('Mountain County Library', 64, 184, 32 if big else 29, weight=700)
    s += txt('Find computer help near you', 64, 238, 31 if big else 28)
    s += field('Search the library', 'computer help', 64, 282, 630, stage == 4)
    s += button('Find help', 64, 371, 215, stage == 4)
    s += txt('Zoom: ' + ('110%' if big else '100%'), 843, 451, 29, weight=700)
    if stage in (1, 2, 3):
        s += box(790, 109, 390, 241, '#fff', NAVY)
        s += lines(['New tab', 'Bookmarks'], 817, 151)
        s += txt('Zoom', 817, 260) + txt('−', 921, 260, 36)
        s += txt('110%' if stage == 3 else '100%', 969, 258, 27)
        s += button('+', 1090, 226, 64, stage in (2, 3))
        s += txt('Print…', 817, 323)
    if stage == 5:
        s += box(668, 363, 453, 61, '#d3e9df') + txt('Ctrl + 0   →   restored to 100%', 687, 403, 28)
    return s


def calendar(stage):
    s = chrome('Practice Calendar', 'Training account • Calendar')
    if stage in (0, 5, 6, 8):
        s += button('+ New event', 34, 130, 205, stage == 0)
        s += button('Day', 787, 130, 104, stage in (0,8)) + button('Week', 901, 130, 120, stage == 5) + button('Month', 1031, 130, 134, stage == 6)
        if stage in (0,8):
            s += box(36, 195, 1129, 278, '#fff', LINE) + txt('Tuesday, October 13 • Day view', 59, 235, 30, weight=700)
            for j, time in enumerate(['1:00 PM', '2:00 PM', '3:00 PM']):
                s += txt(time, 62, 302+j*67, 28) + f'<path d="M219 {279+j*67}H1140" stroke="{LINE}" stroke-width="2"/>'
            if stage==8:s += box(235, 346, 887, 65, '#c5dfdc', NAVY) + txt('Library practice • 2:00–3:00 PM • Room A', 254, 387, 29)
        if stage == 5:
            for j, day in enumerate(['Mon 12', 'Tue 13', 'Wed 14', 'Thu 15', 'Fri 16']):
                x = 36+j*229
                s += box(x, 195, 220, 276, '#fff', LINE) + txt(day, x+18, 231, 28, weight=700)
            s += box(272, 273, 204, 143, '#c5dfdc', NAVY) + lines(['Library', 'practice', '2:00–3:00'], 285, 310, 27, 34)
        if stage == 6:
            s += month_grid()
        return s
    s += box(190, 126, 820, 357, '#fff', NAVY)
    s += field('Event title', 'Library practice', 220, 157, 740, stage == 1, stage == 1)
    s += field('Day / start / end', 'Tuesday • 2:00 PM – 3:00 PM' if stage >= 2 else '', 220, 245, 740, stage == 2)
    s += field('Location', 'Room A' if stage >= 3 else '', 220, 330, 360, stage == 3, stage == 3)
    s += field('Reminder', '30 minutes before' if stage >= 4 else 'None', 607, 330, 353, stage == 4)
    s += button('Save' if stage != 7 else 'Details verified', 732, 418, 229, stage >= 4)
    if stage == 7: s += txt('Time zone: Eastern', 220, 451, 27)
    return s


# October with Monday first: 28-30 September lead in, 1 November trails.
MONTH_DAYS = [28, 29, 30] + list(range(1, 32)) + [1]
EVENT_DAY = 13


def month_grid():
    s = txt('October', 270, 166, 30, weight=700)
    for j, day in enumerate(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']):
        s += txt(day, 46+j*161, 222, 26, weight=700)
    event = ''
    for k, day in enumerate(MONTH_DAYS):
        x, y = 36+(k % 7)*161, 232+(k // 7)*51
        in_month = 3 <= k < 34
        if in_month and day == EVENT_DAY:
            # Drawn last so neighbouring cell borders do not cover its outline.
            event = box(x, y, 161, 51, '#c5dfdc', NAVY, 0) + txt(day, x+10, y+35, 26, weight=700) + txt('Library', x+50, y+35, 26, weight=700)
            continue
        s += box(x, y, 161, 51, '#fff' if in_month else '#e5edf2', LINE, 0)
        s += txt(day, x+10, y+35, 26, INK if in_month else '#5A6A7A')
    return s + event


def files(stage):
    s = chrome('Practice Files', 'This computer  ›  Documents' + ('  ›  Community resources' if stage in (2,3,4,6) else ''))
    s += box(24, 131, 214, 349, NAVY) + lines(['Documents', 'Downloads', 'Cloud drive', 'Recycle bin'], 43, 175, 27, 67, PAPER)
    s += button('+ New folder', 264, 133, 210, stage == 1)
    if stage!=4:s += txt('Name', 279, 225, 28, weight=700) + txt('Location', 829, 225, 28, weight=700)
    if stage == 0: s += txt('Your practice files will appear here.', 280, 307)
    if stage == 1:
        s += field('Folder name', 'Community resources', 286, 286, 620, True) + button('Create', 918, 298, 190, True)
    if stage == 5:
        s += box(267,250,890,67,'#c5dfdc',NAVY) + txt('▣  Community resources',285,293,29)
        s += txt('Folder created • open it before saving your file',285,366,28)
    if stage == 2:
        s += box(272,249,875,213,'#fff',NAVY) + field('Save file as', 'library-help-draft.txt',295,282,818,True,True)
        s += button('Save',925,387,188,True)
    if stage in (6, 3):
        s += box(267, 250, 890, 67, '#c5dfdc', NAVY) + txt('▤  library-help-draft.txt', 285, 293, 29) + txt('This computer', 829, 293, 27)
        if stage==6:s += txt('Saved locally • not yet on another device', 285, 366, 28)
    if stage == 3:
        s += box(374, 337, 748, 116, '#fff', NAVY) + lines(['Check the account and sync status first.', 'Local save ≠ available everywhere'], 395, 380, 28)
    if stage == 4:
        s += box(345, 205, 791, 253, '#fff', NAVY) + box(345, 205, 791, 47, NAVY, radius=0)
        s += txt('library-help-draft.txt', 365, 238, 28, PAPER, 700)
        s += lines(['Community resources', 'Library computer-help notes', 'Opened from: Documents / Community resources'], 367, 306, 28, 56)
    return s


def sharing(stage):
    s = chrome('Practice Handout', 'Training account • Community resources / library-help-draft')
    s += box(27, 133, 573, 348, '#fff') + lines(['Computer help', '1. Choose a practice task.', '2. Visit the learning desk.', '3. Ask how to repeat it at home.'], 57, 187, 29, 58)
    s += box(625, 130, 553, 352, '#fff', NAVY) + txt('Share with a partner', 650, 177, 32, weight=700)
    s += field('Recipient', 'partner@example.invalid', 650, 214, 494, stage == 3)
    if stage < 4:
        s += txt('Access', 650, 321, 27)
        for j, label in enumerate(['Viewer', 'Commenter', 'Editor']):
            s += button(label, 647+j*172, 340, 162, (stage == 0 and j == 0) or (stage in (1, 3) and j == 1) or (stage == 2 and j == 2))
        s += button('Save access', 898, 417, 247, stage == 3)
    else:
        s += box(648, 305, 500, 144, '#d3e9df') + lines(['Partner view', 'Comment available', 'Direct editing unavailable'], 671, 344, 28, 40)
    return s


def document(stage):
    s = chrome('Practice Writer', 'computer-help-handout • working copy')
    s += box(25, 128, 1150, 57, '#c8d9e5') + button('Heading 1' if stage >= 3 else 'Normal text ▾', 40, 133, 235, stage == 2)
    s += txt('B    I    U', 306, 170, 28, weight=700) + txt('1.  List', 462, 170, 28)
    s += box(304, 201, 863, 275, '#fff', LINE) + box(26, 201, 260, 275, '#fff', LINE)
    if stage!=2:s += txt('Navigation', 47, 240, 29, weight=700)
    if stage >= 3: s += txt('Computer help', 48, 290, 27)
    elif stage!=2: s += lines(['No headings', 'yet'], 48, 296, 27)
    if stage in (1, 2): s += box(333, 219, 455, 58, '#b9d8f1')
    s += txt('Computer help', 337, 260, 37 if stage >= 3 else 29, weight=700 if stage >= 3 else 400)
    s += lines(['1. Choose a task.', '2. Visit the learning desk.', '3. Ask how to repeat it at home.'], 337, 316, 29, 47)
    if stage >= 4: s += txt('Read the computer-help guide', 337, 459, 28, '#174876')
    if stage == 2:
        s += box(40, 184, 247, 188, '#fff', NAVY) + txt('Normal text', 57, 225, 28) + txt('Heading 2',57,335,28)
        s += box(42, 242, 243, 51, GOLD) + txt('Heading 1', 57, 278, 28, weight=700)
    return s


def sheet(stage):
    s = chrome('Practice Sheets', 'community-supplies • Supplies worksheet')
    s += box(29, 130, 1141, 53, '#fff', LINE) + txt('B5' if stage < 4 or stage >= 5 else 'B2', 44, 166, 28, weight=700)
    formula=txt('=SUM(B2:B4)' if stage in (1, 2, 3, 5, 6) else ('15' if stage == 4 else ''), 208, 166, 30)
    if stage==1:formula=formula.replace('<text ', '<text data-type="true" ',1)
    s += txt('fx', 148, 166, 28) + formula
    x, y, cw, rh = 210, 193, 365, 48
    for j, name in enumerate(['A', 'B']):
        s += box(x+j*cw, y, cw, rh, '#c8d9e5', LINE, 0) + txt(name, x+170+j*cw, y+35, 29, weight=700)
    rows = [('Item', 'Cost ($)'), ('Paper', '15' if stage >= 4 else '12'), ('Folders', '8'), ('Pens', '5'), ('Total', ('28' if stage >= 4 else '25') if stage >= 2 else '')]
    for j, (left, right) in enumerate(rows):
        yy=y+(j+1)*rh
        s += txt(j+1, 157, yy+35, 27)
        for k, value in enumerate([left, right]):
            selected=(k==1 and ((j==4 and stage!=4) or (j==1 and stage==4)))
            s += box(x+k*cw, yy, cw, rh, '#d3e9df' if selected else '#fff', NAVY if selected else LINE, 0)
            s += txt(value, x+k*cw+24, yy+35, 29, weight=700 if j in (0, 4) else 400)
    s += txt('Supplies', 38, 466, 28, weight=700)
    if stage == 3:
        s += box(945, 263, 222, 134, GOLD) + lines(['Predict:', '12 → 15', 'Total = ?'], 961, 300, 28, 39)
    if stage >= 5:
        s += box(945, 263, 222, 134, '#d3e9df') + lines(['Checked:', '15 + 8 + 5', '= 28'], 961, 300, 28, 39)
    return s


def email(stage):
    s = chrome('Practice Mail', 'Training account • Draft only — nothing is sent')
    s += box(27, 133, 1145, 347, '#fff', LINE)
    trimmed = stage >= 4
    cc = 'organizer@example.invalid' + ('' if trimmed else ', class-list@example.invalid')
    bcc = 'volunteers@example.invalid' if 2 <= stage < 4 else ''
    rows=[('To', 'partner@example.invalid'), ('Cc', cc), ('Bcc', bcc)]
    for j, (name, value) in enumerate(rows):
        yy=172+j*56
        s += txt(name, 53, yy, 28, weight=700) + txt(value, 162, yy, 28)
        s += f'<path d="M46 {yy+14}H1144" stroke="{LINE}" stroke-width="2"/>'
    s += txt('Subject', 53, 342, 27, weight=700) + txt('Review the computer-help handout', 189, 342, 28)
    if stage == 5:
        s += box(45, 409, 648, 38, '#fbeec2')
        s += lines(['Please comment on the contact section', 'by Thursday at 3 PM, before Friday’s session.'], 53, 397, 28, 38)
    else:
        s += lines(['Please comment on the contact section', 'before our next practice session.'], 53, 397, 28, 38)
    if stage == 3:
        s += box(640, 352, 508, 120, GOLD) + lines(['If the partner clicks Reply all,', 'it reaches you, the organizer and', 'the class list, but not Bcc.'], 656, 384, 26, 34)
    if stage == 5:
        s += box(758, 408, 390, 58, '#d3e9df') + txt('Saved as a practice draft', 774, 446, 27)
    return s


def feedback(stage):
    s = chrome('Practice Writer', 'Shared handout • Reviewer view' if stage < 3 else 'Shared handout • Author view')
    s += box(29, 131, 644, 351, '#fff', LINE) + txt('Computer help', 56, 182, 35, weight=700)
    s += lines(['1. Choose a task.', '2. Visit the learning desk.', '3. Ask how to repeat it at home.'], 56, 243, 29, 54)
    if stage >= 3: s += box(49, 390, 600, 61, '#d3e9df') + txt('Help desk: 304-555-0142', 64, 431, 29)
    s += box(696, 132, 477, 350, '#fff', NAVY) + txt('Comment on selected steps', 719, 179, 28, weight=700)
    s += lines(['This is confusing.'] if stage == 0 else ['Add the contact number', 'after the steps so readers', 'can find help.'], 719, 238, 28, 42)
    if stage in (1, 2): s += button('Add comment', 903, 407, 244, stage == 2)
    if stage >= 3:
        s += txt('Author: Added — thank you.', 719, 376, 28)
        s += button('Resolved ✓' if stage == 5 else 'Resolve', 928, 410, 220, stage >= 4)
    return s


def trusted(stage):
    s = chrome('VUB Practice Browser', 'mail.example • Suspicious message' if stage < 2 else ('New tab' if stage == 2 else 'mountain-community.example • Known bookmark'))
    if stage < 2:
        s += box(32, 134, 1137, 345, '#fff') + txt('Urgent: your service will stop', 62, 189, 37, '#8d253c', 700)
        s += lines(['Follow this link now to keep your service.', 'Call the number in this message for reassurance.'], 62, 259, 29, 61)
        s += button('Act now', 66, 379, 195)
        if stage == 1:
            s += box(499, 357, 625, 93, GOLD) + lines(['Leave the message alone.', 'Use a separate, trusted route.'], 522, 392, 28)
    elif stage == 2:
        s += txt('Bookmarks', 48, 176, 34, weight=700) + button('Community desk — saved bookmark', 50, 221, 591, True)
    else:
        s += box(31, 134, 1137, 346, '#fff') + txt('Mountain Community Desk', 62, 190, 37, weight=700)
        s += txt('Fictional practice organization', 62, 240, 28)
        s += button('Contact us', 64, 283, 217, stage == 3)
        if stage >= 4:
            s += box(349, 273, 781, 177, '#d3e9df') + lines(['Contact found on the known website', '304-555-0142 • Fictional practice number', 'Ask: Does the claimed issue exist?'], 370, 315, 28, 48)
    return s


def permissions(stage):
    meeting = stage < 3
    s = chrome('Practice Browser Permissions', 'meeting.example • Join practice meeting' if meeting else 'reading.example • Plain text article')
    s += box(31, 134, 1137, 345, '#fff')
    s += txt('Practice meeting' if meeting else 'Community reading page', 62, 185, 37, weight=700)
    if meeting:
        s += box(68, 220, 442, 227, '#c8d9e5') + txt('Camera preview', 165, 339, 32)
    else: s += lines(['Read the library handout.', 'No call. No recording.', 'Camera is unrelated.'], 65, 250, 30, 64)
    s += box(559, 204, 582, 252, '#fff', NAVY)
    if stage in (2, 5):
        s += txt('Site permissions', 582, 253, 32, weight=700)
        s += lines(['Camera: ' + ('Allowed' if stage == 2 else 'Blocked'), 'Microphone: ' + ('Allowed' if stage == 2 else 'Blocked')], 584, 315, 29, 51)
        s += txt('Review access when the task ends.', 582, 426, 27)
    else:
        s += lines(['Allow this site to use your', 'camera and microphone?'], 582, 254, 30, 45)
        s += button('Block', 585, 358, 204, stage == 4) + button('Allow', 832, 358, 277, stage == 1)
    return s


# Mirrors courses/digital-literacy-2/activities/resource-finder.html: the same
# heading, search label and placeholder, filter, Reset button, records and
# status messages, filtered the same way (name + description, any case).
RESOURCES = (
    ('Community library', 'Learning', 'Fictional one-to-one help with browser and file tasks.'),
    ('Community Makers Group', 'Community', 'Fictional peer group for trying small projects together.'),
    ('Practice Workbook Workshop', 'Learning', 'Fictional guided practice with tables, formulas and charts.'),
)
FOCUS = '#a65a00'


def outlined(x, y, w, h, focus):
    stroke, width = (FOCUS, 4) if focus else (NAVY, 2)
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="#fff" stroke="{stroke}" stroke-width="{width}"/>'


def matching(query, category):
    wanted = query.strip().lower()
    return [r for r in RESOURCES if category in ('All categories', r[1]) and wanted in f'{r[0]} {r[2]}'.lower()]


def resource_app(query='', category='All categories', focus=None):
    s = box(30, 128, 1140, 356, PAPER) + txt('Community resource finder', 56, 166, 34, NAVY, 700)
    s += txt('Search fictional resources', 56, 204, 26, weight=700) + outlined(56, 214, 560, 50, focus == 'search')
    value = txt(query, 72, 249) if query else txt('Try library', 72, 249, 28, '#5A6A7A')
    s += value.replace('<text ', '<text data-type="true" ', 1) if focus == 'search' and query else value
    s += txt('Category', 646, 204, 26, weight=700) + outlined(646, 214, 270, 50, focus == 'category') + txt(category + ' ▾', 660, 249, 27)
    s += button('Reset filters', 944, 215, 200)
    found = matching(query, category)
    status = f'{len(found)} fictional resource{"" if len(found) == 1 else "s"} found.' if found else 'No matching resources. Try a different word or reset the filters.'
    s += txt(status, 56, 306, 27, weight=700)
    if len(found) == 1:
        name, kind, about = found[0]
        s += f'<path d="M56 324H1144" stroke="{LINE}" stroke-width="2"/>' + txt(name, 56, 366, 31, NAVY, 700) + txt(f'{kind} · {about}', 56, 410, 27)
    for j, (name, kind, _) in enumerate(found if len(found) > 1 else []):
        yy = 324 + j * 54
        s += f'<path d="M56 {yy}H1144" stroke="{LINE}" stroke-width="2"/>' + txt(name, 56, yy+38, 29, NAVY, 700) + txt(kind, 700, yy+38, 27)
    return s


def local_app(stage):
    if stage >= 3:
        return chrome('VUB Practice Browser', 'Local file: resource-finder-v1.html') + resource_app()
    s = chrome('Practice Text Editor', 'Working copy • local file')
    s += box(28, 133, 1146, 347, '#fff')
    if stage==0:s += lines(['<title>Fictional community resource finder</title>', '<h1>Community resource finder</h1>', '<label for="search">Search fictional resources</label>', '<input id="search" type="search" placeholder="Try library">', '<button id="reset" type="button">Reset filters</button>'], 58, 183, 27, 58)
    if stage in (1, 2):
        s += box(288, 190, 852, 262, '#fff', NAVY) + txt('Save a working version', 313, 237, 33, weight=700)
        s += field('File name', 'resource-finder-v1.html', 314, 279, 785, True, stage==1)
        s += txt('File type: All files • UTF-8', 314, 404, 27) + button('Save', 910, 372, 189, stage == 2)
    return s


def app_checks(stage):
    query=['', 'library', 'zzz', '', 'LIBRARY', 'LIBRARY', 'LIBRARY', 'LIBRARY'][stage]
    cat='Learning' if stage in (5, 7) else ('Community' if stage == 6 else 'All categories')
    return chrome('VUB Practice Browser', 'Local file: resource-finder-v1.html • Test the saved file') + resource_app(query, cat, 'category' if stage in (5, 6) else 'search')


# Each phrase is looked up in the actual aligned narration; no estimated timing.
# Tuple: cue phrase, UI state, cursor x/y, short demonstration caption.
PLANS = {
 (1, 1): (zoom, [
  ('',0,660,308,'Start at 100% • change only the webpage'),
  ('Open the browser menu',1,1155,87,'Open the browser menu'),
  ('find Zoom',2,1120,248,'Find Zoom • choose one step'),
  ('increase it one step',3,1120,248,'110% • the page is larger'),
  ('Then check the important part',4,166,395,'Check the search field and button'),
  ('restore it before continuing',5,1020,439,'Ctrl + 0 • restore the original zoom')]),
 (1, 6): (calendar, [
  ('',0,140,154,'Create a fictional appointment'),
  ('create Library practice',1,137,154,'New event • enter a useful title'),
  ('from two to three',2,550,284,'Library practice • 2:00–3:00 PM'),
  ('Room A as the location',3,393,373,'Add Room A • check day and time zone'),
  ('Add a reminder',4,776,373,'Reminder: 30 minutes before'),
  ('Day view',8,850,442,'Save • check the event in Day view'),
  ('week view',5,960,153,'Save • find the same event in Week view'),
  ('month view',6,1096,153,'Change the view • keep the same event'),
  ('Reopening it confirms',7,269,346,'Reopen • verify the saved details')]),
 (2, 5): (files, [
  ('',0,360,158,'Give the practice handout a recognizable home'),
  ('Create a practice folder',1,371,157,'New folder → Community resources'),
  ('use a descriptive file name',5,1000,323,'Create the folder • open Community resources'),
  ('library help draft',2,600,324,'Name the file library-help-draft.txt'),
  ('A file saved on this computer',6,1000,409,'Save into Community resources'),
  ('check the account',3,130,300,'Before switching devices, check account and sync'),
  ('Reopen the file',4,490,281,'Open the saved file from its intended location')]),
 (2, 6): (sharing, [
  ('',0,730,364,'Reviewer task: suggest without rewriting'),
  ('Commenter access',1,902,364,'Choose Commenter for suggestions'),
  ('Editor access',2,1070,364,'Editor can change the content directly'),
  ('inspect the recipient carefully',3,900,258,'Check recipient • save Commenter access'),
  ('have the partner verify',4,1011,441,'Verify from the partner’s view')]),
 (3, 1): (document, [
  ('',0,558,251,'Start with meaningful document structure'),
  ('Use a real heading style',1,554,250,'Select the title text'),
  ('for the title',2,160,157,'Open Styles → choose Heading 1'),
  ('section headings',3,222,284,'The title now appears in Navigation'),
  ('Use link text',4,588,450,'Name the destination in the link text')]),
 (3, 4): (sheet, [
  ('',0,764,455,'Select B5 • keep the total outside the input range'),
  ('enter equals SUM',1,467,160,'Enter =SUM(B2:B4)'),
  ('twenty five dollars',2,771,455,'Check the expected total: $25'),
  ('Now change paper',3,769,324,'Predict the new total before the change'),
  ('from twelve to fifteen',4,769,324,'Change B2 from 12 to 15'),
  ('twenty eight',5,769,455,'The formula recalculates: $28'),
  ('inspect the formula and range',6,414,158,'Check =SUM(B2:B4) if the result is wrong')]),
 (4, 3): (email, [
  ('',0,438,165,'Inspect every recipient before sending'),
  ('Cc sends a visible copy',1,472,220,'Cc is visible to the recipients'),
  ('Bcc hides those recipients',2,468,274,'Bcc hides addresses • it is not confidentiality'),
  ('Reply all can send',3,1105,372,'Reply all: check the entire recipient list'),
  ('Remove unnecessary recipients',4,700,220,'Remove the class list and the Bcc list'),
  ('reasonable response window',5,712,424,'Add a reasonable response window • draft only')]),
 (4, 5): (feedback, [
  ('',0,914,234,'Review the steps in one shared handout'),
  ('Add the contact number',1,915,272,'Suggest a location, change, and reason'),
  ('identifies a location',2,1006,429,'Add the specific comment'),
  ('After making the edit',3,356,426,'Author adds the fictional help number'),
  ('acknowledge the feedback',4,946,378,'Acknowledge the change and check it'),
  ('Resolve a comment only',5,1021,434,'Resolve after the request has been addressed')]),
 (5, 3): (trusted, [
  ('',0,1049,173,'Do not follow the message’s link'),
  ('Open the organization',1,1145,87,'Leave the suspicious message'),
  ('use a saved bookmark',2,442,245,'Open a bookmark you already trust'),
  ('find its contact details independently',3,175,305,'Use Contact on the known website'),
  ('Ask whether the claimed issue exists',4,722,403,'Verify the claim through the independent contact')]),
 (5, 6): (permissions, [
  ('',0,812,253,'Which site is asking, and why?'),
  ('Grant access only',1,966,384,'Trusted meeting + camera task → Allow'),
  ('request fits that task',2,771,309,'Check the permission that was granted'),
  ('Deny an unrelated request',4,680,384,'A text page does not need the camera → Block'),
  ('review the setting later',5,762,310,'Review permissions • blocked here')]),
 (6, 5): (local_app, [
  ('',0,760,420,'Start from the supplied local HTML file'),
  ('Save the file',1,650,324,'Save a distinct working version'),
  ('with its HTML extension',2,1003,396,'Keep .html • not .html.txt'),
  ('open it in the browser',3,981,397,'Open the file in a browser'),
  ('Confirm that the heading',4,550,173,'Check heading, search, category, and results')]),
 (6, 6): (app_checks, [
  ('',0,560,240,'Test the actual saved app'),
  ('Type library',1,560,240,'library → Community library'),
  ('Then enter an unmatched term',2,560,240,'zzz → No matching resources'),
  ('Clear the field',3,560,240,'Clear the search before the next check'),
  ('try LIBRARY in uppercase',4,560,240,'LIBRARY → the same result'),
  ('combine the search with a category filter',5,790,240,'Learning + LIBRARY → match'),
  ('both conditions apply',6,790,240,'Community + LIBRARY → no match')])
}


def normalized_tokens(value):
    # Hyphens and apostrophes may be separate words in the alignment.
    return re.findall(r'[a-z0-9]+', value.lower())


def timed_actions(n, i, beat, words):
    tokens=[]
    for word in words:
        tokens.extend((t, word['start']) for t in normalized_tokens(word['word']))
    haystack=[t[0] for t in tokens]
    actions=[]
    for phrase, state, x, y, label in PLANS[n, i][1]:
        if not phrase: at=0.0
        else:
            needle=normalized_tokens(phrase)
            matches=[j for j in range(len(haystack)-len(needle)+1) if haystack[j:j+len(needle)] == needle]
            if not matches: raise ValueError(f'Week {n}, chapter {i+1}: narration cue not found: {phrase!r}')
            at=round(tokens[matches[0]][1]+beat.get('leadIn',.01),3)
        actions.append(dict(at=at, phrase=phrase, state=state, x=x, y=y, label=label))
    assert all(a['at'] < b['at'] for a,b in zip(actions,actions[1:])), (n,i,'out of order')
    assert actions[-1]['at'] < beat['audioDuration'], (n,i,'outside narration')
    return actions


def scene(n, i, beat, words):
    cid=f'w{n}-scene-{i+1}'
    render=PLANS[n,i][0]
    actions=timed_actions(n,i,beat,words)
    layers=[]; events=[]
    for j,action in enumerate(actions):
        sid=f'{cid}-state-{j}'
        artwork=render(action['state'])
        # Short, deterministic typing sequences retain exact narration timing.
        for k,match in enumerate(list(re.finditer(r'<text data-type="true" ([^>]+)>(.*?)</text>',artwork))):
            tid=f'{sid}-typing-{k}'
            full=html.unescape(match[2])
            artwork=artwork.replace(match[0],f'<text id="{tid}" {match[1]}>{E(full)}</text>',1)
            next_at=actions[j+1]['at'] if j+1<len(actions) else beat['window']
            span=min(.65,max(.1,(next_at-action['at'])*.55))
            if j and full:
                for count in range(len(full)+1):
                    events.append(f'tl.set("#{tid}",{{textContent:{json.dumps(full[:count])}}},{action["at"]+span*count/len(full):.4f});')
        layers.append(f'<svg class="screen-state" id="{sid}" viewBox="0 0 1200 500" role="img" aria-label="{E(action["label"])}" style="opacity:{1 if j==0 else 0}">{artwork}</svg>')
        if j:
            at=action['at']
            # Move before the spoken action; the click and state change coincide.
            travel=min(.65,max(.12,(at-actions[j-1]['at'])/2))
            # A new performance can bring two clicks closer together. Finish
            # this pulse before the next one so reverse seeking stays stable.
            next_click=actions[j+1]['at'] if j+1<len(actions) else beat['window']
            pulse_duration=.55 if next_click-at>=.55 else max(.001,next_click-at-.02)
            pulse='.55' if pulse_duration==.55 else f'{pulse_duration:.3f}'
            events += [f'tl.to("#{cid} .pointer",{{x:{action["x"]},y:{action["y"]},duration:{travel},ease:"power2.inOut"}},{max(0,at-travel)});',
                       f'tl.set("#{cid}-state-{j-1}",{{opacity:0}},{at});',
                       f'tl.set("#{sid}",{{opacity:1}},{at});',
                       f'tl.set("#{cid} .action-label",{{textContent:{json.dumps(action["label"])}}},{at});',
                       f'tl.set("#{cid} .step-number",{{textContent:"{j+1:02} / {len(actions):02}"}},{at});',
                       f'tl.fromTo("#{cid} .click-ring",{{opacity:1,scale:.6}},{{opacity:0,scale:1.45,duration:{pulse},immediateRender:false}},{at});']
    first=actions[0]
    events.insert(0,f'tl.set("#{cid} .pointer",{{x:{first["x"]},y:{first["y"]}}},0);')
    return f'''<template><div id="{cid}" data-composition-id="{cid}" data-start="0" data-duration="{beat['window']}" data-width="1280" data-height="720" data-screen-share="true" style="position:relative;width:100%;height:100%;overflow:hidden">
<style>
@font-face{{font-family:VUB;src:url('assets/source-sans-3-latin-400-normal.woff2')}}
@font-face{{font-family:VUB;src:url('assets/source-sans-3-latin-700-normal.woff2');font-weight:700}}
#{cid}{{background:#102c4b;font-family:VUB,'Segoe UI',sans-serif;color:#F5F7FA}}
#{cid} .share-heading{{position:absolute;left:40px;top:23px;margin:0;font-size:34px;line-height:1.2;font-weight:700}}
#{cid} .share-label{{position:absolute;left:42px;top:66px;font-size:26px;color:#E6C65C}}
#{cid} .screen-state{{position:absolute;left:40px;top:104px;width:1200px;height:500px}}
#{cid} .pointer{{position:absolute;left:40px;top:104px;width:35px;height:45px;z-index:5}}
#{cid} .click-ring{{position:absolute;left:-19px;top:-19px;width:44px;height:44px;border:4px solid #8d253c;border-radius:50%;opacity:0;transform-origin:50% 50%}}
#{cid} .action-label{{position:absolute;left:40px;top:615px;margin:0;font-size:30px;line-height:1.2;max-width:1060px}}
#{cid} .step-number{{position:absolute;right:41px;top:617px;font-size:28px;color:#E6C65C}}
#{cid} .simulation-label{{position:absolute;left:40px;bottom:12px;font-size:26px;color:#e5edf2}}
</style>
<h1 class="share-heading">{E(beat['title'])}</h1><div class="share-label">VUB LEARNING  /  FOLLOW THE SCREEN</div>
{''.join(layers)}
<div class="pointer"><div class="click-ring"></div><svg width="35" height="45" viewBox="0 0 35 45"><path d="M3 2 L3 33 L12 25 L20 42 L27 38 L19 23 L32 23 Z" fill="#E6C65C" stroke="#102c4b" stroke-width="3"/></svg></div>
<p class="action-label">{E(first['label'])}</p><div class="step-number">01 / {len(actions):02}</div>
<div class="simulation-label">Screen simulation • fictional practice data • menus vary by application</div>
<script>const tl=gsap.timeline({{paused:true}});{''.join(events)}window.__timelines["{cid}"]=tl;</script>
</div></template>'''
