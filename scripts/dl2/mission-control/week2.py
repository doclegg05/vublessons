"""Mission Control Week 2: ask an AI search tool well, check it, keep it, share it.

Shared source of truth for facts and vocabulary: docs/digital-literacy-2/week-02-ai-search-spec.md.
Minutes are what this lab room is expected to need (Week 1 ran at about half its plan),
not a clock for learners. No break and no timers, per Britt's standing rule.
"""
from html import escape as e


def mission(title, app, start, finish, tell, show, do, question, choices, answer, why, lab, practice, rounds=()):
    return dict(title=title, app=app, start=start, finish=finish, tell=tell, show=show, do=do, question=question,
                choices=choices, answer=answer, why=why, lab=lab, practice=practice, rounds=list(rounds))


def rnd(title, app, steps, early, notes, paper='', tasks=(), key=()):
    """One extra hands-on round: a Do slide, matching worksheet tasks and answer-key lines."""
    return dict(title=title, app=app, steps=list(steps), early=early, notes=notes, paper=paper, tasks=list(tasks), key=list(key))


def table(head, rows):
    """Small printable table for worksheet material. Cells are escaped."""
    th = ''.join(f'<th scope="col">{e(h)}</th>' for h in head)
    body = ''.join('<tr>' + ''.join(f'<td>{e(c)}</td>' for c in row) + '</tr>' for row in rows)
    return f'<div class="table-scroll" tabindex="0" role="region" aria-label="Practice material"><table><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>'


A_ROUNDS = [
    rnd('Rescue the weak question', 'Browser · Google',
        ['Take three weak questions: help, computer class, library.',
         'Rewrite each with a service, a place and one detail that matters.',
         'Ask your best rewrite. Compare its answer with the weak one.'],
        'Done early? Ask the same question two different ways. Note what changed.',
        'Learners rewrite, then ask the best version on their own screen. Look for a service, a place and one detail (free, evening, near a bus line). A good rewrite sounds like a question to a person. Ask two or three learners to read theirs aloud.',
        tasks=['Rewrite each weak question with a service, a place and one detail: (a) help (b) computer class (c) library. Ask your best rewrite and write one way its answer beat the weak one.'],
        key=['Each rewrite names a service, a place and one detail, for example: Where can I take a free beginner computer class near Beckley, WV, in the evening? The answer to the rewrite is more local and more specific than the answer to the weak version.']),
    rnd('Catch the error', 'Worksheet · fictional answer and page',
        ['Read the fictional AI answer on your worksheet.',
         'Check each claim against the fictional library page.',
         'Mark each claim: confirmed, wrong, or not on the page.'],
        'Done early? Write the one question you would ask the library by phone.',
        'Everything here is fictional. The AI answer is wrong on the town (Beckley, Ohio), the hours (9 p.m. against 8 p.m.), and "free for everyone" is not on the page. Use it to show why the summary is a lead. Ask who they would trust and why.',
        paper='<h3>Fictional AI answer</h3><blockquote>The Beckley Community Library offers free computer classes for everyone in Beckley, Ohio. It is open until 9 p.m. on weekdays, and you can walk in without signing up.</blockquote><h3>Fictional library page, updated this spring</h3><blockquote>Beckley Community Library, Beckley, West Virginia. Learning desk hours: weekdays until 8 p.m. Computer classes are free for library card holders. Sign up at the learning desk.</blockquote>'
              + table(['Claim from the AI answer', 'Confirmed, wrong, or not on the page?', 'What the page says'],
                      [['Free computer classes', '', ''], ['Beckley, Ohio', '', ''], ['Open until 9 p.m.', '', ''], ['Walk in without signing up', '', '']]),
        tasks=['Check each claim in the table against the fictional library page. Then write which source you would believe, and the next step before you travel.'],
        key=['Free computer classes: partly right, but the page says free for library card holders. Beckley, Ohio: wrong, the page says West Virginia. Open until 9 p.m.: wrong, the page says 8 p.m. Walk in without signing up: wrong, the page says sign up at the learning desk. Believe the library page, then phone the library to confirm hours before travelling.']),
    rnd('Safe to ask?', 'Browser · Google',
        ['Read six things someone might type into a question.',
         'Sort each one: fine to ask, or keep it out of a question.',
         'Rewrite one unsafe question so it works without private details.'],
        'Done early? Write a safe question about a benefit or clinic near you.',
        'Private details typed into a question may be stored by the company that runs the tool. Fine: place names, service types, general questions. Keep out: Social Security, bank or card numbers, passwords, claim numbers, health details. A password reset question never needs the password. No veteran or benefits framing is required: use it only if it is the natural example.',
        paper=table(['Someone might type', 'Fine to ask, or keep out?'],
                    [['What time does the Beckley library open?', ''], ['My Social Security number is [my number]. Can you check my benefits?', ''],
                     ['Here is my bank card number. Is this store trustworthy?', ''], ['My diagnosis is... Which clinics near Beckley have evening hours?', ''],
                     ['How do I reset a forgotten email password?', ''], ['My claim number is 12345. Why is it late?', '']]),
        tasks=['Sort the six questions in the table. Then rewrite one unsafe question so it works without private details.'],
        key=['Fine to ask: library hours; how to reset a forgotten password (no password typed). Keep out: Social Security number; bank card number; claim number; the diagnosis in the clinic question (ask Which clinics near Beckley have evening hours? instead). A safe rewrite removes the number or the health detail and keeps the need.']),
]

B_ROUNDS = [
    rnd('Needed, not needed, risky', 'Worksheet · fictional request form',
        ['Read the eight fields on a fictional computer-help request form.',
         'Sort each field: needed, ask why first, or do not give.',
         'Explain one choice to a partner.'],
        'Done early? Write what you would say to a volunteer who asks for a field you marked do not give.',
        'There is no single right answer for every form, but a request for computer help does not need a Social Security number, bank account or mother\'s maiden name. Date of birth is "ask why first". Praise a learner who says they would phone the organization instead of typing it.',
        paper=table(['Field on the form', 'Needed, ask why first, or do not give?'],
                    [['Name', ''], ['Preferred way to contact you', ''], ['Topic you want help with', ''], ['Days you are free', ''],
                     ['Date of birth', ''], ['Social Security number', ''], ['Mother\'s maiden name', ''], ['Bank account number', '']]),
        tasks=['Sort the eight fields in the table, then write one question you would ask before giving a field you were unsure about.'],
        key=['Needed: name, preferred contact, topic, days free. Ask why first: date of birth. Do not give: Social Security number, mother\'s maiden name, bank account number. A good question: Why do you need this, and how long do you keep it?']),
    rnd('Read before you send', 'Browser · fictional privacy note',
        ['Read the short privacy note on your worksheet.',
         'Answer four questions: who collects it, why, how long, who sees it.',
         'Decide whether you would send the form, and why.'],
        'Done early? Rewrite the note\'s last sentence so it is clearer for a first-time reader.',
        'The note is fictional. Teach the habit: before typing, find who is asking, why, how long they keep it and who sees it. A form that asks for a card number to get a free class is a warning sign, not a service. No sign that a form looks official proves it is safe.',
        paper='<h3>Fictional privacy note</h3><blockquote>Beckley Community Library uses your answers to schedule computer help. Requests are kept for 90 days and are seen only by the learning desk volunteer coordinator. We do not sell your information.</blockquote>'
              + table(['Question', 'Your answer'], [['Who collects it?', ''], ['Why do they want it?', ''], ['How long do they keep it?', ''], ['Who sees it?', '']]),
        tasks=['Answer the four questions in the table about the fictional privacy note. Say whether you would send the form, and what would change your mind.'],
        key=['Who: Beckley Community Library. Why: to schedule computer help. How long: 90 days. Who sees it: the learning desk volunteer coordinator. Sending is reasonable for a help request. It would change if the form asked for a card number or a Social Security number.']),
]

C_ROUNDS = [
    rnd('Rename the mess', 'File Explorer · Downloads',
        ['Read ten messy file names from a Downloads folder.',
         'Write a clear new name for each: subject, then what it is, then a version or date.',
         'Choose one of three folders for each file.'],
        'Done early? Create the three folders in Documents and move your renamed practice files into them.',
        'The names are on paper so the room needs no extra files. Good names say what it is and which version: library-hours-screenshot-oct.png. Folders: Community resources, Household, Photos. Any clear scheme works if a stranger could find the file.',
        paper=table(['Messy name', 'Clear new name', 'Folder'],
                    [['final-final-new.docx', '', ''], ['IMG_2231.jpg', '', ''], ['Document1.docx', '', ''], ['scan0004.pdf', '', ''], ['letter to landlord FINAL.docx', '', ''],
                     ['New Text Document.txt', '', ''], ['library-hours-screenshot.png', '', ''], ['budget.xlsx', '', ''], ['untitled.pptx', '', ''], ['resume copy (3).docx', '', '']]),
        tasks=['Give each of the ten files a clear new name and a folder: Community resources, Household or Photos.'],
        key=['Any scheme where the name says what the file is and which version it is, for example library-help-v1.docx or landlord-letter-oct.docx. Folders are consistent: library and handout files in Community resources, budget and landlord letter in Household, camera and screenshot files in Photos.']),
    rnd('Find it fast', 'File Explorer · Documents',
        ['Open Documents. Click the search box and type part of a file name.',
         'Click the Date modified heading to sort. Find the file you changed last.',
         'Right-click Community resources and choose Pin to Quick access.'],
        'Done early? Rename your ZIP file so a stranger would know what it holds.',
        'File Explorer shows a search box at the top right. The Date modified heading appears in Details view. Pin to Quick access lives in the right-click menu (Show more options may be needed). If the lab image differs, demonstrate on the projector first.',
        tasks=['In File Explorer, search Documents for part of your file name, sort by Date modified, and pin Community resources to Quick access. Write one way each saves time.'],
        key=['Search finds a file from part of its name without opening every folder. Sorting by Date modified brings the newest file to the top. Pinning keeps the folder one click away in the left pane.']),
    rnd('Which tool fixes it?', 'Windows · File Explorer',
        ['Read four problems: deleted file, wrong wording, five files to email, dead computer.',
         'Choose the tool for each: Recycle Bin, version history, ZIP, or backup.',
         'Say why a ZIP does not fix the others.'],
        'Done early? Write a fifth problem and the tool that fixes it.',
        'Match the problem to the tool. A ZIP packages files; it is not a backup and not encryption. Version history needs a cloud service. A backup is a separate copy kept somewhere else.',
        paper=table(['Problem', 'Tool: Recycle Bin, version history, ZIP, or backup?'],
                    [['I deleted the whole file yesterday.', ''], ['The file is here, but a paragraph was replaced.', ''], ['I need to email five files in one attachment.', ''], ['My computer will not start and the file is only on it.', '']]),
        tasks=['Choose the tool for each of the four problems in the table. Then say why a ZIP file helps with only one of them.'],
        key=['Deleted file: Recycle Bin. Replaced paragraph: version history, if the service keeps it. Five files in one attachment: ZIP. Computer will not start: a backup, a separate copy. A ZIP only packages files for transfer; it does not recover deletions, undo edits or replace a backup.']),
]

D_ROUNDS = [
    rnd('Role cards', 'Shared file · fictional',
        ['Read six sharing situations.',
         'Choose the least access that does the job: Viewer, Commenter, Editor, or no sharing.',
         'Say what could go wrong if you chose Editor by habit.'],
        'Done early? Write a sharing situation of your own and the role it needs.',
        'The aim is least access that does the job. Anyone with the link means anyone who gets the link, including after it is forwarded. Choose named people when the file matters. A stranger asking for edit access is a no.',
        paper=table(['Situation', 'Viewer, Commenter, Editor, or no sharing?'],
                    [['A neighbor wants to read your finished handout.', ''], ['A friend will proofread the wording.', ''], ['A co-leader will rewrite steps with you.', ''],
                     ['Thirty class members need the final copy.', ''], ['Someone you do not know asks to edit it.', ''], ['Your landlord should see a letter but not change it.', '']]),
        tasks=['Choose the least access for each of the six situations in the table, and explain one choice.'],
        key=['Neighbor: Viewer. Friend proofreading: Commenter. Co-leader: Editor. Thirty class members: Viewer, to named people or a view-only link. Stranger asking to edit: no sharing. Landlord: Viewer, or send a PDF copy.']),
    rnd('Delete it. Then what?', 'Windows · File Explorer · fictional cloud folder',
        ['Read three delete situations.',
         'Say what sync does, what a backup does, and what version history does.',
         'Choose the best protection for each.'],
        'Done early? Explain sync and backup to a partner as if to a neighbor.',
        'Sync copies a deletion to every connected place. A backup is a separate copy. Version history may bring back earlier wording, for a limited time and only in some services. Online recycle bins keep deleted files for a limited time. Do not test with a real important file.',
        paper=table(['Situation', 'What happens, and what protects you?'],
                    [['You delete a file from your laptop folder that syncs to the cloud.', ''], ['A partner replaces the whole handout with the wrong text.', ''], ['Your laptop is lost and the file is only on it.', '']]),
        tasks=['For each situation in the table, say what happens and which protection helps: online recycle bin, version history, or a backup.'],
        key=['Delete from synced folder: the deletion syncs; look in the online recycle bin, which keeps files for a limited time. Wrong text from a partner: version history, if the service keeps it. Lost laptop with the only copy: only a separate backup helps, because a file that was never synced or backed up cannot be recovered.']),
]

CAPSTONE = dict(
    title='Community resource folder',
    app='Browser · File Explorer · Word',
    brief='Pick a different service than before: a food pantry, a bus route, tax help or a clinic. Use everything from today.',
    steps=['Ask a question. Check one source. Write the five-field source note.',
           'Save the note in Documents as a clearly named file in Community resources.',
           'ZIP the folder. Write who gets which access if you shared it.'],
    peer='Swap your note only, with no browser history. Can your partner find the source page and your detail?',
    early='Done early? Add a second source and mark which one you trust more.',
    notes_brief='Capstone. Learners choose a new service so they transfer the skills instead of repeating the demo. They need a question, a checked source, the five-field note, a clearly named file in Community resources, and a ZIP. No new account. Use fictional personal details if any are needed.',
    notes_peer='Partners swap the note only. If the partner cannot find the page and the detail from the note, the note is missing something: title, organization, full URL, date checked or the detail. Fix it together. Record how each pair did on the roster as Independent, With prompt or Needs practice.',
    tasks=['Ask a question about a new community service. Check one source with the five source questions. Write the five-field source note.',
           'Save the note as a clearly named file in Community resources, ZIP the folder, and write who would get which access if you shared it.',
           'Swap the note only with a partner. Write whether your partner found the page and the detail, and what your note was missing.'],
    key=['A new service, not the earlier example. A question with a service, a place and one detail; one source from the organization\'s own page; all five fields (title, organization, full URL, date checked, specific detail).',
         'A clearly named file in Documents › Community resources; a ZIP of the folder; Viewer for a reader, Commenter for a reviewer, Editor only for a co-writer.',
         'The partner finds the page and the detail from the note alone. If not, the note lacked a field, usually the full URL or the specific detail, and the learner adds it.'],
    outcome='Independent: the partner finds the page and detail from the note alone. With prompt: needed one hint. Needs practice: a field or the file name was missing.')


WEEK2 = dict(
    title='Find it. Check it. Keep it.', photo='library',
    warm='A neighbor in Beckley needs computer help. What would you check before sending them across town?',
    apply='Choose one local service. Save a source trail and explain what you still need to confirm.',
    minutes=[8, 5, 22, 16, 22, 18, 14, 8, 7], nobreak=True, capstone=CAPSTONE,
    missions=[
        mission('Ask well, then check it', 'Browser · Google', 'A broad question: computer help', 'A checked answer and a source trail',
                ['Ask in full sentences: what you need, where, what matters.',
                 'An AI answer is a lead from many pages. It can sound sure and be wrong.',
                 'Open the source: who published it, when, does it fit?'],
                [('Ask', 'Free computer help, Beckley, evenings', 'Say what you need, where you are and what matters, as you would to a librarian. A follow-up narrows the answer. You do not have to start over.'),
                 ('Read', 'AI answer: open until 9 p.m.', 'Treat the answer as a lead. It is a quick summary of many pages and can be wrong, old or about another town. Look for the links beside or beneath it.'),
                 ('Check', 'Library page: open until 8 p.m.', 'Open the organization\'s own page and check who published it and when. When the answer and the page disagree, trust the page, then phone to confirm before you travel.')],
                ['Ask a full-sentence question with a service, a town and one detail.',
                 'Ask one follow-up. Open one source link beneath the answer.',
                 'Find one detail the page confirms and one it does not.'],
                'The AI answer says the library opens at 9. Its own page says 8. What next?',
                ['Go at 9 because the answer is newer', 'Trust the library page and phone to confirm', 'Ask the AI again until it agrees'], 1,
                'The library\'s own page outranks a summary. Hours change, so phone before you go.',
                [0, 1, 2, 3], 6, A_ROUNDS),
        mission('Complete a form carefully', 'Practice form', 'A request with missing information', 'A clear practice confirmation',
                ['Read required fields before typing.', 'Give only the information needed.', 'Read the confirmation; keep a reference.'],
                [('Inspect', 'Computer-help request · fictional', 'A name and topic are required. A Social Security number is not needed.'),
                 ('Try', 'Submit with the topic blank', 'A required-field message means the request is not complete.'),
                 ('Confirm', 'Practice complete: no request was sent', 'This local exercise cannot book a real appointment. Real forms need their own confirmation.')],
                ['Open the practice form; use fictional details.', 'Try a blank required field, then correct it.', 'Read the confirmation and explain its limit.'],
                'The practice page says “No request was sent.” What happened?', ['An appointment is booked', 'Only the practice is complete', 'Your instructor received it'], 1,
                'This is an account-free simulation. It practices validation and reading a confirmation, not delivery.', [4], 10, B_ROUNDS),
        mission('Organize and recover a file', 'File Explorer', 'A file lost among downloads', 'A named file you can reopen',
                ['Use a clear folder and file name.', 'ZIP packages files; extract before editing.', 'Deleted file? Recycle Bin. Wrong edit? History.'],
                [('Save', 'Documents / Community resources / library-help-v1.docx', 'Save a named file, close it, and reopen it from the folder.'),
                 ('Package', 'Community resources.zip → Extract All', 'Compression is not encryption or a separate backup. Edit the extracted copy.'),
                 ('Recover', 'Deleted file → Recycle Bin → Restore', 'For a bad edit in a cloud file, inspect version history; alert collaborators first.')],
                ['Save and reopen a clearly named practice file.', 'ZIP a copy and extract it into a new folder.', 'Delete the spare file, then restore it.'],
                'The file exists, but a paragraph was replaced. Where first?', ['Recycle Bin', 'Make another ZIP', 'Version history, if available'], 2,
                'Recycle Bin recovers deleted files. Version history can recover earlier content of a cloud file.', [5, 7], 18, C_ROUNDS),
        mission('Share only the access needed', 'Shared file', 'One file; three different jobs', 'Reader, reviewer and coauthor roles',
                ['Viewer reads; commenter suggests; editor changes.', 'Check the account, owner and named recipients.', 'Sync copies deletions; keep a separate backup.'],
                [('Decide', 'Reader: Viewer · Reviewer: Commenter', 'If commenting is unavailable, agree on feedback another way; do not grant editing by habit.'),
                 ('Review', 'Coauthor: Editor · Anyone link: Off', 'Keep one shared copy and verify the intended person can open it.'),
                 ('Protect', 'Read-only ≠ encryption ≠ backup', 'Read-only limits changes. Sync can spread deletion. A separate backup supports recovery.')],
                ['Assign access to a reader, reviewer and writer.', 'State who owns the central copy.', 'Explain sync versus a separate backup.'],
                'A neighbor only needs to read the handout. Which access?', ['Editor', 'Viewer', 'Public editable link'], 1,
                'Viewer meets the task with less ability to change the shared copy. It does not encrypt it.', [6, 7], 15, D_ROUNDS),
    ])
