"""Mission Control Week 5: comfort and access, a scam checked another way, protected devices, then the skills
challenge and the post-test.

Spec: docs/digital-literacy-2/week-05-spec.md. One fictional scam message everywhere (deck, worksheet, video,
practice page): "Act now: account will close" from support@account-check.example, asking you to verify your
password. Two-step verification, not MFA, as in test items 19 and 20. No capstone: the five-task skills challenge
is the week's transfer task (Britt, 2026-10-08). No break, no timers. Windows 10 home Extended Security Updates
run through October 12, 2027 (Microsoft's consumer ESU page, checked 2026-10-08). Rounds avoid the wording of
test items 18 to 20.
"""
from lessonkit import mission, quote, rnd, table

A_ROUNDS = [
    rnd('Color is not the only clue', 'Worksheet · fictional volunteer schedule',
        ['Read the schedule. Its status is shown by shading only.',
         'Mark each place where shading is the only clue.',
         'Add a word to each status, such as Open or Full.'],
        'Done early? Name one fix for someone who cannot use a mouse.',
        'Color or shading alone leaves out people who see color differently, people using a black-and-white printer, '
        'and anyone in poor light. A word or symbol beside the color fixes it. Keyboard access with a visible outline '
        'helps someone who cannot use a mouse.',
        paper='<p>Key: dark shading means full; light shading means one spot left; no shading means open.</p>'
              + table(['Shift', 'Day', 'Status', 'Your fix'],
                      [['Set up chairs', 'Saturday 9 a.m.', '▓▓▓ dark', ''], ['Help desk', 'Saturday 10 a.m.', '░░░ light', ''],
                       ['Clean up', 'Saturday noon', '(no shading)', ''], ['Phone reminders', 'Friday 4 p.m.', '▓▓▓ dark', '']]),
        tasks=['Add a word to each status in the table so the schedule works without shading, and name one fix for someone '
               'who cannot use a mouse.'],
        key=['Set up chairs: Full. Help desk: One spot left. Clean up: Open. Phone reminders: Full. A fix for someone '
             'who cannot use a mouse: every control works with the Tab key and shows a visible outline.']),
    rnd('Bigger, then back', 'Windows · Magnifier · Edge',
        ['Press Windows and plus to zoom in. Press Windows and Esc to close.',
         'In Edge, press Ctrl and plus twice. Then press Ctrl and 0.',
         'Write which one enlarged everything and which one page.'],
        'Done early? Open Settings › Accessibility › Text size and look, without applying.',
        'Magnifier enlarges the whole screen; browser zoom enlarges one website. Both undo cleanly, which matters on a '
        'shared computer. Text size in Settings changes every app, so learners only look at it here.',
        tasks=['Try Magnifier and browser zoom, put both back, and write which one enlarged everything and which one '
               'enlarged a single page.'],
        key=['Magnifier (Windows and plus) enlarges everything on the screen; Windows and Esc closes it. Ctrl and plus in '
             'Edge enlarges only that website; Ctrl and 0 puts it back.']),
]

B_ROUNDS = [
    rnd('Four messages', 'Worksheet · four fictional messages',
        ['Read four fictional messages on your worksheet.',
         'Circle the pressure, and the contact each one gives you.',
         'Write the safer route for each.'],
        'Done early? Write one polite sentence to end the phone call.',
        'Common scams this year: unpaid-toll texts, pop-ups with a support phone number, a "grandchild" in trouble '
        'asking for gift cards. Microsoft error messages never include a phone number. Scam texts can be forwarded to '
        '7726. The library notice gives no link and no pressure, so it is probably fine; check it on the library site '
        'you saved.',
        paper=table(['Message', 'Pressure or odd request', 'Safer route'],
                    [['Text: Unpaid toll of $3.95. Pay today at toll-pay.example or face a fine.', '', ''],
                     ['Pop-up: Your computer is infected! Call Microsoft Support at 1-800-555-0199 now.', '', ''],
                     ['Phone call: Grandpa, it is me. I am in trouble. Send gift cards and do not tell Mom.', '', ''],
                     ['Email from your library: Your hold is ready. Pick it up by Friday at the front desk.', '', '']]),
        tasks=['For each message in the table, circle the pressure or odd request and write a safer route.'],
        key=['Toll text: pressure and a strange link; use the toll agency\'s own site or app you already know, and forward '
             'the text to 7726. Pop-up: a phone number in an error message is a scam; close the browser and ask staff. '
             'Grandchild call: secrecy and gift cards; hang up and call family on a number you know. Library email: no '
             'pressure and no link; check your account on the library site you saved.']),
    rnd('Never read back a code', 'Worksheet · fictional text message',
        ['Read the fictional text message.',
         'Mark what you can verify and what you cannot.',
         'Write what you would do instead of replying.'],
        'Done early? Write what to do if someone already read the code back.',
        'A one-time code proves you are you. Anyone who asks you to read it back is trying to get into your account. '
        'A real bank will not ask. Call the number on the back of your card.',
        paper=quote('Fictional text message', 'Mountain Bank alert: we stopped a suspicious charge. To cancel it, reply '
                    'with the 6-digit code we just sent you.'),
        tasks=['Mark what you can and cannot verify in the text message, then write what you would do instead of replying.'],
        key=['Nothing in the text can be verified: the sender, the charge and the story. A bank never asks you to read back '
             'a code. Do not reply; call the number on your card. If the code was shared, call the bank now and change '
             'the password.']),
]

C_ROUNDS = [
    rnd('A password you will never use', 'Worksheet · four sample passwords',
        ['Rank four sample passwords from weakest to strongest.',
         'Make up a four-word passphrase for a fictional account.',
         'Name a second check: an app code, a text code, or a passkey.'],
        'Done early? Tell a partner why using one password everywhere is risky.',
        'Use a passkey when a site offers one. Otherwise use a long, unique passphrase and turn on two-step '
        'verification; a browser password manager can remember it. Never write a real password on the worksheet.',
        paper=table(['Sample password', 'Rank 1 to 4 (1 is weakest)'],
                    [['Beckley1', ''], ['password123', ''], ['maple-river-lantern-cocoa', ''], ['Tr0ub4dor!', '']]),
        tasks=['Rank the sample passwords in the table, make up a four-word passphrase for a fictional account, and name '
               'a second check.'],
        key=['Weakest to strongest: password123, Beckley1, Tr0ub4dor!, maple-river-lantern-cocoa. A good passphrase is '
             'four unrelated words, used for one account only. Second check: a code from an app or a text, or a passkey.']),
    rnd('Which protection fits?', 'Worksheet · five situations',
        ['Read five situations on your worksheet.',
         'Choose: sign out, password to open, read-only, device encryption, or backup.',
         'Say why for one of them.'],
        'Done early? Say where a recovery key is kept, without writing one down.',
        'Each protection does one job. On a shared lab login, sign out rather than lock. Device encryption protects '
        'a lost computer that is turned off; its recovery key is in the Microsoft account. Read-only limits edits but '
        'anyone can still read the file.',
        paper=table(['Situation', 'Best protection'],
                    [['You are leaving a library computer.', ''], ['Your laptop could be lost on the bus.', ''],
                     ['Others may read the flyer but should not change it.', ''],
                     ['A private letter must be unreadable without a password.', ''],
                     ['Your laptop might stop working one day.', '']]),
        tasks=['Choose the best protection for each situation in the table and explain one choice.'],
        key=['Library computer: sign out. Lost laptop: device encryption (recovery key kept in the Microsoft account). '
             'Flyer: read-only. Private letter: password to open, which encrypts it. Laptop might stop: a backup copy '
             'somewhere else.']),
]

WEEK5 = dict(
    title='Protect your work. Show your skills.', photo='safety',
    warm='Name one safety habit you already use away from a computer. How could it help online?',
    apply='Use your results to choose one strength and one specific task to practice next.',
    minutes=[26, 4, 12, 12, 11, 26, 22, 7], nobreak=True, practice_pages=True, video_pauses=True,
    downloads='<h2>Practice workbook data</h2><p><a href="/courses/digital-literacy-2/assets/supplies.csv">Fresh supplies.csv</a> for row 3 of the skills challenge.</p>',
    plan_note='<p>Week 5 is the last GS6 week: three short missions, then the 26-minute observed skills challenge and '
              'the 22-minute post-test. The video stops at pause cards for Missions 5A to 5C; at each one, pause and let '
              'learners do the worksheet task the card names. Its last chapter explains the challenge and the post-test. '
              'If the room is slow, skip every Done early line, then Round 3 of Mission 5A, then Round 3 of Mission 5C. '
              'Protect the challenge and the post-test time.</p>',
    missions=[
        mission('Make your station comfortable', 'Windows · Settings · Magnifier', 'A hard-to-read or distracting screen',
                'One useful adjustment you can reverse',
                ['Adjust text, position and zoom; then put it back.', 'Captions, keyboard access, and words beside colors.',
                 'Quiet unneeded alerts; plan a stopping point.'],
                [('Adjust', 'Magnifier: Windows + plus · Windows + Esc',
                  'Screen about an arm\'s length away, top near eye level. Try one change you can undo.'),
                 ('Access', 'Captions on · Tab moves a visible outline',
                  'These help many people, not only people with a disability. Color alone should never carry the message.'),
                 ('Restore', 'Settings back · Do not disturb for focus',
                  'Put shared settings back. Quiet alerts deliberately, and plan a stopping point.')],
                ['Change one thing so you can read without leaning in.', 'Mute this week\'s video, read the captions, press Tab.',
                 'Put the shared settings back.'],
                'Which design helps a learner who cannot use a mouse?', ['Color-only instructions',
                                                                          'Keyboard access with visible focus', 'Smaller controls'], 1,
                'Keyboard access and a visible focus outline show where the next action will happen.', [0, 1], None, A_ROUNDS),
        mission('Pause and verify independently', 'Practice page · fictional inbox', 'An urgent account message',
                'A trusted contact found another way',
                ['Pressure, secrecy and odd requests are clues.', 'Check another way, never with the message\'s contact.',
                 'Already typed a password? Change it on the real site.'],
                [('Inspect', 'Act now: account will close',
                  'Clues: pressure, an odd sender (account-check.example) and a password request.'),
                 ('Verify', 'Your bookmark, or the number on your card',
                  'Never use the message\'s own link or phone number.'),
                 ('Respond', 'Typed it? Change it on the real site',
                  'Turn on two-step verification, then tell the instructor.')],
                ['Inspect the subject, sender and link on the practice page.', 'Write two warning signs and your safer check.',
                 'Name a safe next step for three tricky situations.'],
                'A new online friend asks for gift cards and says keep it secret. Next?',
                ['Send a small amount', 'Keep the request secret', 'Pause, send nothing and verify'], 2,
                'Pressure for money and secrecy call for an independent check. A profile photo is not proof of identity.',
                [2, 3], 8, B_ROUNDS),
        mission('Protect access and recovery', 'Edge · Windows Settings · Word', 'A signed-in device and unneeded permissions',
                'A lock habit and clear protection choices',
                ['Keep supported software updated.', 'Allow the camera or microphone only when needed.',
                 'Encryption, read-only and backup do different jobs.'],
                [('Inspect', 'Edge → Settings → permissions → Camera',
                  'Look without changing anything. A permission can stay on after a call ends.'),
                 ('Protect', 'Password to open encrypts · read-only limits edits',
                  'Updates close security holes. A passkey, or a long unique passphrase with two-step verification, protects an account.'),
                 ('Lock', 'Windows + L, or sign out on a shared login',
                  'Encryption protects a lost computer that is turned off. It does not protect an open, signed-in session.')],
                ['Choose on each practice-page card before you flip it.', 'Look at Camera permissions and Windows Update.',
                 'In Word, find which protection encrypts a file.'],
                'Which makes file contents unreadable without the key?', ['Read-only', 'Encryption', 'ZIP compression'], 1,
                'Encryption protects readable data. Read-only restricts edits and ZIP packages files; neither replaces it.',
                [4, 5], 9, C_ROUNDS),
        mission('Show what you can do', 'Word · Excel · Edge · skills challenge', 'The course quick card and fresh practice files',
                'Five observed skills; a separate post-test',
                ['Work on your own; the quick card is allowed.', 'Show search, structure, SUM, recovery and feedback.',
                 'This observation is separate from your test score.'],
                [('Prepare', 'Fresh supplies.csv · blank Word document',
                  'Ask a full question that names the place, then open its own page. Build a heading, numbered steps and a bold warning.'),
                 ('Demonstrate', 'Add Tape $4 → =SUM(B2:B5) → $29',
                  'Use the fresh 12, 8, 5 file. Bring back deleted text with Undo while the file is still open.'),
                 ('Explain', 'The flyer gives no a.m. or p.m., no date, no room',
                  'Name two missing details and a polite fix. The instructor rates Independent, With prompt or Needs practice.')],
                ['Complete the five tasks on the worksheet.', 'Leave your work on screen for the instructor.',
                 'Then take the 20-question post-test on your own.'],
                'You needed a spoken prompt during the skills challenge. Rating?',
                ['Independent', 'With prompt', 'Add points to the post-test'], 1,
                'Record the support used honestly. The observation and the scored post-test stay separate.', [6, 7], None),
    ])
