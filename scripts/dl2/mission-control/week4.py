"""Mission Control Week 4: a clear request, one shared copy, a meeting, and a check before paying.

Spec: docs/digital-literacy-2/week-04-spec.md. One fictional cast everywhere (deck, worksheet, video):
you wrote the computer-help handout; Sam reviews it; Pat organizes the Saturday session and owns the
shared copy; Alex runs the session; 20 volunteers get the notice. Feedback example everywhere: in step 2,
add where the learning desk is (Room A, first floor). Offer pair everywhere: A is free for 30 days, then
$6 a month; B is $60 a year, paid now. No capstone, no break, no timers (Britt, 2026-10-08). Rounds avoid
the wording of test items 13 to 17.
"""
from lessonkit import mission, quote, rnd, table

A_ROUNDS = [
    rnd('Make it actionable', 'Worksheet · three vague emails',
        ['Read three vague emails on your worksheet.',
         'Rewrite each: what to do, which file, and by when.',
         'Read one to a partner. Can they say what to do?'],
        'Done early? Write a subject line that states the request by itself.',
        'Each rewrite needs an action, the file or topic, and a time. A partner who can say what to do and by when is '
        'the test. Everything is fictional; nothing is sent.',
        paper=table(['Vague email', 'Your rewrite'],
                    [['FYI, see attached.', ''], ['Can you look at this sometime?', ''],
                     ['Need this ASAP!!', '']]),
        tasks=['Rewrite each vague email in the table so it says what to do, which file, and by when.'],
        key=['Each rewrite names an action, the file and a time, for example: Please check the dates on the attached '
             'Saturday sign-up sheet and reply by Wednesday at noon. A partner can say what to do and by when.']),
    rnd('Say it so anyone can follow', 'Worksheet · four short messages',
        ['Read four short messages on your worksheet.',
         'Circle abbreviations and anything that assumes who people are.',
         'Rewrite two so anyone could follow them.'],
        'Done early? Your draft is ready at 6:40 a.m. Pick a better time to send it, and say why.',
        'Look for unexplained abbreviations (BYOD, RSVP, EOD) and assumptions about age, skill or background. A good '
        'rewrite spells things out and offers help to everyone. Schedule send lets a draft written early arrive at a '
        'reasonable hour.',
        paper=table(['Message', 'Problem', 'Rewrite'],
                    [['Mtg moved to Rm B. BYOD.', '', ''], ['RSVP by EOD pls.', '', ''],
                     ['You probably are not a computer person, so skip step 3.', '', ''],
                     ['Bring your grandkids to set up your phone.', '', '']]),
        tasks=['Mark the problem in each message in the table, then rewrite two so anyone could follow them.'],
        key=['Problems: BYOD, RSVP and EOD are unexplained abbreviations; two messages assume what someone can do or who '
             'is in their life. Rewrites spell out the request and offer help to everyone, for example: The meeting moved '
             'to Room B. Please bring your own laptop if you have one; we have spares.']),
]

B_ROUNDS = [
    rnd('Vague to useful', 'Worksheet · six comments',
        ['Read six comments on a fictional handout.',
         'Sort them: useful or vague.',
         'Rewrite two vague ones with a place, a change and a reason.'],
        'Done early? Write a polite reply that declines one suggestion and gives a reason.',
        'A useful comment names where, what to change, and why. Comments judge the work, never the person. A writer may '
        'decline a suggestion with a reason; the comment is resolved only after that reply.',
        paper=table(['Comment', 'Useful or vague?'],
                    [['This is confusing.', ''], ['In step 2, say which floor the desk is on.', ''],
                     ['Fix it.', ''], ['The title could name the library, so readers know where.', ''],
                     ['I would never write it this way.', ''], ['Make it better.', '']]),
        tasks=['Mark each comment in the table useful or vague, then rewrite two vague comments with a place, a change and '
               'a reason.'],
        key=['Useful: the step 2 floor comment and the title comment. Vague: This is confusing, Fix it, Make it better, and '
             'I would never write it this way (it judges the writer). A rewrite names a place, a change and a reason, for '
             'example: In step 1, list two example tasks so a first-time visitor knows what to ask for.']),
    rnd('Live or later?', 'Worksheet · four schedules',
        ['Read four ways a team could work on the handout.',
         'Choose: together now, or comments for later.',
         'Name the access each person needs: viewer, commenter or editor.'],
        'Done early? Say what the team should write down so everyone knows the final decision.',
        'Together now (synchronous) suits a short task when everyone is free at once. Comments for later '
        '(asynchronous) suit people on different schedules. Give the least access that does the job.',
        paper=table(['Team situation', 'Now or later?', 'Access for each person'],
                    [['All three are free Tuesday at 10 for twenty minutes.', '', ''],
                     ['Sam works nights; Pat works days.', '', ''],
                     ['Alex only needs to read the final version.', '', ''],
                     ['Pat must approve the wording before Friday.', '', '']]),
        tasks=['For each team situation in the table, choose together now or comments for later, and name each person\'s '
               'access.'],
        key=['Tuesday at 10: together now. Night and day shifts: comments for later. Alex reads only: viewer. Pat '
             'approves: Pat is the owner with editor access; others comment. Write the final decision in the shared copy.']),
]

C_ROUNDS = [
    rnd('Hear and be heard', 'Windows Settings · Sound',
        ['Open Start → Settings → System → Sound.',
         'Under Input, choose the headset. Select Start test and speak.',
         'Stop the test. Set the input back if you changed it.'],
        'Done early? Open Sound Recorder, record one sentence, and play it back.',
        'Check the headset before a meeting, not during it. On shared lab computers, set the input back afterwards. If '
        'a station has no headset microphone, the learner explains the steps instead; record it as simulated.',
        tasks=['Test the headset microphone in Settings › System › Sound, then set the input back. Write what you saw '
               'move when you spoke.'],
        key=['The input meter moves while the learner speaks into the headset. The input device is set back afterwards. '
             'With no microphone, the learner names the steps and the evidence is recorded as simulated.']),
    rnd('Meeting or webinar?', 'Worksheet · four online events',
        ['Read four online events on your worksheet.',
         'For each, say how you would ask a question.',
         'Say who you would ask before recording.'],
        'Done early? Name one thing you would do if your sound failed partway through.',
        'In a small meeting people usually unmute or raise a hand. In a webinar the host controls speaking, so '
        'questions go in Q&A or chat. Recording needs the host\'s and the group\'s agreement. Backup plans: rejoin, '
        'use chat, or read the shared notes afterwards.',
        paper=table(['Online event', 'How to ask a question', 'Who to ask before recording'],
                    [['A four-person planning call with Pat', '', ''], ['A library webinar with 200 viewers', '', ''],
                     ['A support group with shared stories', '', ''], ['A training call where the host says use chat', '', '']]),
        tasks=['For each online event in the table, say how you would ask a question and who you would ask before recording.'],
        key=['Planning call: unmute or raise a hand; ask everyone. Webinar: Q&A or chat; the host. Support group: raise a '
             'hand or follow the host; ask the host and every member, and do not record personal stories without '
             'agreement. Training call: chat, as the host asked; the host.']),
    rnd('Is the post right?', 'Worksheet · fictional post and pantry page',
        ['Read the fictional community post and the pantry\'s own page.',
         'Mark each claim: confirmed, wrong, or not on the page.',
         'Write your next step before you go.'],
        'Done early? Write a kind reply to the post that points people to the pantry\'s page.',
        'This mirrors Week 2: a post is a lead, not a source. The post is wrong on the day (Saturday against Friday) '
        'and on the ID rule, and the free coffee is not on the page. Next step: phone the pantry or use its own page.',
        paper=quote('Fictional community post', 'The Hillside food pantry is open Saturday 9 to 11, and you do not need '
                    'any ID. They have free coffee too!')
              + quote('Fictional pantry page, updated this month', 'Hillside Food Pantry. Open Fridays 4 to 6 p.m. Please '
                      'bring a photo ID or a piece of mail with your address.')
              + table(['Claim from the post', 'Confirmed, wrong, or not on the page?'],
                      [['Open Saturday 9 to 11', ''], ['No ID needed', ''], ['Free coffee', '']]),
        tasks=['Check each claim in the table against the pantry\'s own page, then write your next step.'],
        key=['Open Saturday 9 to 11: wrong; the page says Fridays 4 to 6 p.m. No ID needed: wrong; bring a photo ID or a '
             'piece of mail. Free coffee: not on the page. Next step: trust the pantry\'s page and phone to confirm.']),
]

D_ROUNDS = [
    rnd('First-year cost', 'Worksheet · two offers, with Calculator',
        ['Use the two offers on your worksheet.',
         'Work out the cost for 3 months and for 12 months.',
         'Write the last day to cancel the free month.'],
        'Done early? After how many paid months does Offer A cost more than Offer B?',
        'Offer A: free for 30 days, then $6 a month. Three months: 2 paid months, $12. Twelve months: 11 paid months, '
        '$66. Offer B: $60 either way. A trial started October 19 ends November 18, so cancel by November 17. A costs '
        'more than B after 10 paid months.',
        paper=table(['Offer', 'Price', '3 months', '12 months'],
                    [['A', 'Free for 30 days, then $6 a month until you cancel', '', ''],
                     ['B', '$60 a year, paid now, renews every year', '', '']]),
        tasks=['Work out what each offer in the table costs for 3 months and for 12 months, and write the last day to '
               'cancel a free month that started October 19.'],
        key=['A: $12 for 3 months (2 paid months) and $66 for 12 months (11 paid months). B: $60 for either. The free '
             'month runs October 19 to November 18, so cancel by November 17.']),
    rnd('What is missing?', 'Worksheet · fictional sign-up screen',
        ['Read the fictional sign-up screen.',
         'Find the seller, the price now, the later price and the renewal.',
         'Name what is missing and what you would do.'],
        'Done early? Write the question you would send the seller.',
        'The screen hides how to cancel. Without it, do not start the trial: find the cancellation steps on the '
        'seller\'s help page first, or skip it.',
        paper=quote('Fictional sign-up screen', 'StreamSmart Plus. Watch free for 30 days! Then $6 a month. Renews '
                    'automatically each month. Sold by StreamSmart Media LLC. Start watching.'),
        tasks=['Find the seller, the price now, the later price and the renewal on the sign-up screen, then name what is '
               'missing and what you would do.'],
        key=['Seller: StreamSmart Media LLC. Price now: free. Later: $6 a month. Renewal: automatic, monthly. Missing: '
             'how to cancel. Do not sign up until you find the cancellation steps; deleting the app would not cancel it.']),
    rnd('Inspect a checkout', 'Practice page · fictional checkout',
        ['Choose Seller, then Total, then Terms, then Method.',
         'Write what each one tells you.',
         'Say which payment you would use and why.'],
        'Done early? Name one way to stop surprise purchases on your phone.',
        'The checkout is a simulation and cannot take payment. A credit card offers dispute rights. Money sent through '
        'a person-to-person app (Zelle in a bank app, Venmo, Cash App) is hard to get back, so use it only with people '
        'you know. On a phone, require a password for every purchase in the app store settings.',
        tasks=['On the Mission 4D practice page, check the seller, total, terms and method, then write which payment you '
               'would use and why.'],
        key=['Seller: Practice Learning Store. Total: $12, including $2 delivery. Terms: read before paying. Method: a '
             'credit card, or a digital wallet that uses one, because a wrong charge can be disputed.'],
        practice=17),
]

WEEK4 = dict(
    title='Work together without confusion.', photo='collaboration',
    warm='When has a message made your next step easy? What information did it include?',
    apply='Choose a real upcoming conversation. Write who needs to do what, by when, through which channel.',
    minutes=[30, 5, 20, 18, 18, 14, 8, 7], nobreak=True, practice_pages=True, video_pauses=True,
    plan_note='<p>Week 4 uses one fictional cast throughout: you wrote the handout, Sam reviews it, Pat organizes the '
              'Saturday session and owns the shared copy, Alex runs the session, and 20 volunteers get the notice. '
              'Learners have no email, meeting or cloud account, so emails are worksheet drafts, comments happen in a '
              'local Word file by swapping seats, and the meeting and checkout are practice pages; record that evidence '
              'as simulated. The video stops at pause cards; at each one, pause and let learners do the worksheet task '
              'the card names. If the room is slow, skip in this order: every Done early line, Round 3 of Mission 4A, '
              'Round 3 of Mission 4B, then Round 2 of Mission 4C. Keep the Review slides and the individual check.</p>',
    missions=[
        mission('Send a clear request', 'Worksheet · email drafts', 'A vague message with too many recipients',
                'The right request, account and audience',
                ['Pick the channel for the urgency and the reader.', 'Name the request, the file and the reply time.',
                 'To acts; Cc stays informed; Bcc hides addresses.'],
                [('Compose', 'Subject: Please review the handout by Thursday',
                  'Greet Sam, name the task and the reply-by time, then close courteously. Check which account it comes from.'),
                 ('Address', 'Review: To Sam · Cc Pat',
                  'Sam must act, so Sam goes in To. Pat should know, so Pat goes in Cc. Leave out the volunteers.'),
                 ('Notice', 'Notice: To Alex · Cc Pat · Bcc volunteers',
                  'Bcc hides the volunteers\' addresses from one another. It does not stop forwarding.')],
                ['Draft the review request to Sam; nothing is sent.', 'Address the volunteer notice: To, Cc and Bcc.',
                 'Rewrite one unclear message for any reader.'],
                'Pat uses Reply all on the volunteer notice. Who gets it?',
                ['You and Alex', 'Everyone, including the volunteers', 'Only the volunteers'], 0,
                'Reply all reaches the sender and the visible To and Cc names. Bcc names never receive it.',
                [0, 1, 2, 3], None, A_ROUNDS),
        mission('Improve one shared copy', 'Word · How to get computer help', 'Two versions and vague feedback',
                'One owner, one copy, a resolved comment',
                ['Agree on the owner, the writer and the reviewer.', 'A useful comment names the place, change and reason.',
                 'Reply, decide, then resolve the comment.'],
                [('Agree', 'Owner: Pat · Writer: you · Reviewer: Sam',
                  'One shared copy in one agreed place. Work together now, or leave comments for later.'),
                 ('Comment', 'In step 2, add where the desk is: Room A, first floor.',
                  'The reason: a first-time visitor needs to find it. A comment suggests; it does not replace text.'),
                 ('Resolve', 'Reply → change or decline → Resolve',
                  'Resolve only after you reply. A resolved comment is hidden, not deleted.')],
                ['Choose roles and one shared place with a partner.', 'Add one specific comment on their handout.',
                 'Reply with a decision, then resolve it.'],
                'Which comment helps the owner revise?', ['This is confusing.', 'Make it better.',
                                                          'In step 2, add where the desk is.'], 2,
                'A useful comment names the place and the change. Saying why helps the writer decide.',
                [4, 5], None, B_ROUNDS),
        mission('Join with care', 'Practice meeting · headset', 'A noisy call or an unfamiliar group',
                'Clear participation and respectful boundaries',
                ['Test your sound; mute when not speaking.', 'Use captions, raise hand and the host\'s rules.',
                 'Ask before recording or sharing a story.'],
                [('Prepare', 'Headset input tested · captions on',
                  'A meeting allows discussion. In a webinar the host controls who speaks; use Q&A or chat.'),
                 ('Take part', 'Unmute → speak → mute',
                  'Raise your hand when the host asks for it. Ask before you record anyone.'),
                 ('Check', 'A community post is a lead, not a fact',
                  'Read the group\'s rules. Confirm hours or eligibility with the organization itself.')],
                ['Practice unmute, raise hand, lower hand and mute.', 'Test your headset in Windows Sound settings.',
                 'Name one community claim you would check yourself.'],
                'You want to record a group\'s personal stories. What comes first?',
                ['Start recording quietly', 'Ask permission', 'Share them on social media'], 1,
                'Ask before recording or sharing. Respect the group\'s rules and each person\'s choice.',
                [6], 14, C_ROUNDS),
        mission('Check before paying', 'Calculator · worksheet offers', 'Two fictional streaming offers',
                'A decision based on total cost and renewal',
                ['Check the seller, the total, the renewal and how to cancel.', 'A credit card lets you dispute a wrong charge.',
                 'Deleting an app does not cancel a subscription.'],
                [('Compare', 'A: free 30 days, then $6 a month · B: $60 a year',
                  'A costs $12 for 3 months and $66 for 12. B costs $60 up front, even if you stop early.'),
                 ('Inspect', 'Renewal date · how to cancel · refunds',
                  'A free trial turns into a charge. Write the last day to cancel before you start.'),
                 ('Decide', 'Pay with a card you can dispute',
                  'Person-to-person apps are for people you know. Require a password for purchases on your phone.')],
                ['Work out both offers for 3 and 12 months.', 'Write two questions to ask before a trial.',
                 'Choose a payment method and explain why.'],
                'You delete a streaming app. What happens to its subscription?',
                ['It is cancelled automatically', 'Check and cancel with the provider', 'You get an automatic refund'], 1,
                'Deleting an app usually does not stop billing. Cancel through the provider and keep the confirmation.',
                [7], None, D_ROUNDS),
    ])
