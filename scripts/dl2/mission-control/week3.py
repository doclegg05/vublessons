"""Mission Control Week 3: a resource pack in Word, Excel and PowerPoint, exported and checked.

Spec: docs/digital-literacy-2/week-03-spec.md. The video teaches each mission and stops at pause cards
that send learners to the worksheet tasks named here, so the video block is about 30 minutes of class.
No capstone, no break and no timers (Britt, 2026-10-08). Supply order everywhere: Paper 12, Folders 8,
Pens 5, the order in assets/supplies.csv and the video. Round numbers avoid the pre/post test values
(28 to 31 and 40 to 44 in items 10).
"""
from lessonkit import mission, quote, rnd, table

A_ROUNDS = [
    rnd('Bold is not a heading', 'Word · resource-handout.docx',
        ['Type a new line: Where to find us. Make it bold.',
         'Open View → Navigation Pane. Is the line listed?',
         'Apply Heading 2. Then run Review → Check Accessibility.'],
        'Done early? Choose References → Table of Contents. Add a heading, then select Update Table.',
        'Bold changes how a line looks, not what it is, so the Navigation Pane leaves it out until it gets Heading 2. '
        'Check Accessibility works without an account and flags missing headings, missing alt text and link text that '
        'does not name its destination. The Table of Contents extra is built from the same heading styles.',
        tasks=['Add the bold line Where to find us and check the Navigation Pane. Apply Heading 2, then run Review › Check '
               'Accessibility. Write what changed in the Navigation Pane and what the checker reported.'],
        key=['The bold line is missing from the Navigation Pane until Heading 2 is applied; then it is listed. Check '
             'Accessibility reports no heading problems, or names a finding the learner fixes, such as missing alt text.']),
    rnd('Check the AI draft', 'Worksheet · fictional AI-drafted handout',
        ['Read the fictional AI draft and the fictional library page.',
         'Mark four problems in the draft.',
         'Rewrite the link line and the last step.'],
        'Done early? Write the follow-up question you would ask the AI to fix the draft.',
        'This connects to Week 2: an AI answer is a lead, not a source. The four problems are the click here link text, '
        'the hours (the draft says 9 p.m., the library page says 8 p.m.), the steps in the wrong order, and no next '
        'action at the end. Everything here is fictional.',
        paper=quote('Fictional AI-drafted handout',
                    'Computer Help at the Library. Ask how to repeat it at home. Choose one task you want to learn. '
                    'Visit the learning desk, open until 9 p.m. on weekdays. For more information, click here.')
              + quote('Fictional library page, updated this spring',
                      'Beckley Community Library learning desk: weekdays until 8 p.m. Free computer help for library '
                      'card holders. Read the computer-help guide at the desk or online.')
              + table(['Problem in the draft', 'How to fix it'], [['', ''], ['', ''], ['', ''], ['', '']]),
        tasks=['Mark four problems in the fictional AI draft, using the library page to check the facts. Then rewrite the '
               'link line and add a clear next action.'],
        key=['The link says click here instead of naming its destination. The hours say 9 p.m., but the library page says '
             '8 p.m. The steps are out of order: choose a task, visit the desk, then ask how to repeat it. The draft ends '
             'with no next action. A good rewrite uses Read the computer-help guide as the link text and ends with a step '
             'such as Visit the learning desk on a weekday before 8 p.m.']),
]

B_ROUNDS = [
    rnd('Typed total versus formula', 'Excel · supplies.xlsx',
        ['Click C5 and type 28, the total as a plain number.',
         'Write what B5 and C5 will show if paper becomes 20.',
         'Change paper to 20. Which total is wrong now?'],
        'Done early? Click B5 and press F2. The colored box shows the cells the formula adds.',
        'B5 recalculates to 33. C5 still says 28 because nobody retyped it, which is the most common mistake in a '
        'household budget. F2 shows the formula and outlines its range. Ask learners to set paper back to 15 before '
        'Round 3.',
        tasks=['Type 28 in C5 as a plain number. Predict B5 and C5 for paper at 20, change paper to 20 and compare. Then '
               'set paper back to 15.'],
        key=['B5 shows 33 because the formula adds the cells. C5 still shows 28 because a typed number never updates. '
             'With paper back at 15, B5 shows 28 again.']),
    rnd('Add a row', 'Excel · supplies.xlsx',
        ['Right-click the row 5 number and choose Insert.',
         'Type Envelopes in A5 and 6 in B5. Predict the total.',
         'Click the total. Does the formula bar include B5?'],
        'Done early? Select the four costs and press Alt and = for AutoSum. Compare its formula with yours.',
        'The total moves down to B6. Excel may or may not stretch the range to take in the new row, and that is the '
        'lesson: read the range. With paper at 15 the total should be =SUM(B2:B5), showing 34. If it shows 28, edit '
        'the range to B2:B5.',
        tasks=['Insert a row above Total and add Envelopes at $6. Predict the new total, then read the formula bar and fix '
               'the range if it skips the new row.'],
        key=['The total is now in B6 and reads =SUM(B2:B5), showing 34 (15 + 8 + 5 + 6). If the range still ended at B4, '
             'the learner changed it to B2:B5.']),
    rnd('CSV keeps values only', 'Excel · File Explorer',
        ['File → Save As. Choose CSV and name it supplies-copy.',
         'Close Excel. Open supplies-copy.csv from Resource pack.',
         'Click the total. What does the formula bar show?'],
        'Done early? Open supplies.xlsx, choose Insert → Recommended Charts, and title the chart Supply costs in dollars.',
        'CSV is plain rows of values. It keeps the numbers but drops formulas, formatting and charts, and Excel warns '
        'about possible data loss when you save. Keep supplies.xlsx as the working file. The chart is optional; check '
        'that its title names the units.',
        tasks=['Save a copy as CSV named supplies-copy, reopen it and click the total. Write what the formula bar shows and '
               'which file you would keep working in.'],
        key=['The formula bar shows a plain number, such as 28 or 34, not =SUM. The CSV kept the values and lost the '
             'formula, so keep working in supplies.xlsx.']),
]

C_ROUNDS = [
    rnd('Alt text that helps', 'Worksheet · four alt-text drafts',
        ['Read four alt-text drafts for the practice photo.',
         'Pick the best. Label the rest: vague, too long, or starts with image of.',
         'Update your own alt text in PowerPoint.'],
        'Done early? Add a plain shape, open View Alt Text and tick Mark as decorative.',
        'Good alt text is one sentence about what matters in the picture. Screen readers already say it is an image, '
        'so image of wastes the listener\'s time. PowerPoint may suggest a description; check it the way Week 2 '
        'checked an AI answer before keeping it.',
        paper=table(['Draft alt text', 'Best, vague, too long, or starts with image of?'],
                    [['Image of two people.', ''], ['A photo.', ''],
                     ['Two people review a computer-help handout at a library table.', ''],
                     ['This picture shows a bright room with a wooden table, two chairs, a window, a blue folder, a printed '
                      'page, a man in a gray shirt and a woman with glasses, and both of them are looking down at the page.', '']]),
        tasks=['Label each draft in the table, then write the alt text you will use for your own photo.'],
        key=['Best: Two people review a computer-help handout at a library table. Starts with image of: Image of two '
             'people. Vague: A photo. Too long: the description of the whole room. The learner\'s own alt text is one '
             'sentence about what matters in the photo.']),
    rnd('Crop is not delete', 'PowerPoint · resource-slides.pptx',
        ['Select the photo. Choose Picture Format → Crop and drag the handles back out.',
         'Watch the hidden edges return. Crop again and press Esc.',
         'Choose Compress Pictures. Tick Delete cropped areas of pictures. Select OK.'],
        'Done early? Choose Crop → Aspect Ratio → 1:1 and compare the frame.',
        'A crop hides the edges but PowerPoint keeps them in the file, so the crop can be undone. Compress Pictures with '
        'Delete cropped areas removes them. That matters before sharing a photo with something private near the edge. '
        'The original photo file on disk never changes.',
        tasks=['Drag the crop handles back out and watch the hidden edges return. Crop again, then use Compress Pictures › '
               'Delete cropped areas of pictures. Write why this matters before you share a photo.'],
        key=['The cropped edges come back when the handles are dragged out, so a crop alone does not remove them. After '
             'Compress Pictures with Delete cropped areas of pictures they are gone from the presentation. It matters when '
             'something private sits near the edge of a photo.']),
    rnd('Use, credit, ask or skip?', 'Worksheet · five picture situations',
        ['Read five picture situations on your worksheet.',
         'Choose for each: use it, use it with a credit, ask first, or do not use it.',
         'Write one credit line.'],
        'Done early? Tell a partner why finding a picture in search results is not permission to use it.',
        'Your own photo of a public sign: use it. The VUB practice photo: use it with the credit given. A search result '
        'with no license shown: do not use it. A photo whose license allows reuse with credit: use it with a credit. '
        'A neighbor\'s photo: ask first.',
        paper=table(['Picture', 'Use, use with credit, ask first, or do not use?'],
                    [['A photo you took of the library sign', ''], ['The VUB practice photo from this lesson', ''],
                     ['A picture from search results with no license shown', ''],
                     ['A photo whose license allows reuse if you credit the photographer', ''],
                     ['A photo a neighbor took at a community supper', '']]),
        tasks=['Choose use, use with credit, ask first, or do not use for each picture in the table, then write one credit line.'],
        key=['Your photo of the sign: use it. VUB practice photo: use with credit. Search result with no license: do not '
             'use it. Licensed with credit: use with credit, for example Photo: J. Smith, used under its license. '
             'Neighbor\'s photo: ask first.']),
]

D_ROUNDS = [
    rnd('Check before you export', 'Word · resource-handout.docx',
        ['Choose Review → Check Accessibility.',
         'Fix one finding, or note that there were none.',
         'Save the PDF again and open it from File Explorer.'],
        'Done early? Run Check Accessibility on your slides in PowerPoint too.',
        'The checker runs without an account. Common findings are missing alt text, a skipped heading level and link '
        'text that does not name its destination. Learners replace the old PDF when Word asks.',
        tasks=['Run Review › Check Accessibility and fix one finding, or note that there were none. Save the PDF again and '
               'open it from File Explorer.'],
        key=['The learner names a finding and its fix, or reports none, replaces the PDF and opens the new copy from '
             'Resource pack.']),
    rnd('Which format for whom?', 'Worksheet · six people',
        ['Read what six people need to do with your files.',
         'Choose DOCX, XLSX, PPTX, PDF or CSV for each.',
         'Say what the wrong format would lose.'],
        'Done early? In PowerPoint, save the slides as a PDF too: File → Save As → PDF.',
        'Reader only: PDF. Editing partner: DOCX. Treasurer: XLSX. Presenter: PPTX. A sign-up tool that needs plain '
        'rows: CSV. Printing at the library: PDF, so the layout does not move. A PDF is hard to edit, and CSV drops '
        'formulas.',
        paper=table(['Person', 'Format', 'What the wrong format would lose'],
                    [['A neighbor who only reads the handout', '', ''], ['A partner who will edit the handout', '', ''],
                     ['A treasurer who updates the costs', '', ''], ['A volunteer who presents the slides', '', ''],
                     ['A sign-up tool that needs plain rows of data', '', ''],
                     ['Someone who prints the handout at the library', '', '']]),
        tasks=['Choose a format for each person in the table and write what the wrong format would lose.'],
        key=['Neighbor: PDF. Editing partner: DOCX. Treasurer: XLSX, because CSV would lose the formula. Presenter: PPTX. '
             'Sign-up tool: CSV. Printing: PDF, so the layout does not shift.']),
    rnd('Trim and split a clip', 'Practice page · fictional 20-second clip',
        ['Choose Trim the start and end. Note what is left.',
         'Choose Remove a middle section. Note what is left.',
         'Which parts carry the explanation?'],
        'Done early? Would the caption line still match?',
        'The video editor in Windows, Clipchamp, needs a Microsoft account, so this is a simulation. Trim removes 3 '
        'seconds at each end and leaves 14 seconds. Removing the middle pause leaves 17 seconds. Explain and Next step '
        'carry the speech, so they stay.',
        tasks=['On the Mission 3D practice page, trim the start and end, then remove the middle section. Write how long each '
               'edit leaves and which parts you kept.'],
        key=['Trimming removes Start (0 to 3 s) and End (17 to 20 s) and leaves 14 seconds. Removing the middle pause (9 to '
             '12 s) leaves 17 seconds. Explain and Next step stay because they carry the speech.'],
        practice=14),
]

WEEK3 = dict(
    title='Make a useful resource pack.', photo='resource-pack',
    warm='Think of instructions that helped you learn a new task. What made them easy to follow?',
    apply='Open the saved PDF as a neighbor would. Check its steps, link and layout; choose one improvement.',
    minutes=[30, 5, 20, 20, 16, 14, 8, 7], nobreak=True, practice_pages=True, video_pauses=True,
    plan_note='<p>Week 3 runs Word, Excel, PowerPoint, then export, in that order, with no break and no timer. The video '
              'stops at pause cards. At each card, pause and let learners do the worksheet task the card names, then play '
              'on. That makes the video block about 30 minutes, and learners reach each mission with its first tasks '
              'done: at each Your turn slide, check the work, then move to the rounds. If the room is slow, skip in this '
              'order: every Done early line, Round 4 of Mission 3B (CSV keeps values only), Round 4 of Mission 3C (Use, '
              'credit, ask or skip?), then Round 3 of Mission 3D. Keep the Review slides and the individual check. If a '
              'learner falls behind, give them the finished file from the earlier mission so they can still practice the '
              'next one.</p>',
    missions=[
        mission('Structure, then suggest', 'Word · resource-handout.docx', 'A wall of plain text',
                'A clear handout with a reviewed edit',
                ['Use real heading styles and numbered steps.', 'Name the link destination; press Ctrl+K.',
                 'Track Changes lets the owner decide.'],
                [('Structure', 'Heading 1: Computer help at the library',
                  'Home → Styles → Heading 1, then Numbering for the steps. View → Navigation Pane lists the heading.'),
                 ('Link', 'Read the computer-help guide',
                  'Select words that name the destination and press Ctrl+K. Ctrl+C copies, Ctrl+V pastes, Ctrl+Z undoes.'),
                 ('Review', 'Visit the learning desk → Ask at the learning desk',
                  'Turn on Review → Track Changes before editing. The owner chooses Accept or Reject.')],
                ['Type the handout, then apply heading styles.', 'Add the link; try copy, paste and undo.',
                 'Trade seats; track one edit; accept or reject.'],
                'Bold text looks like a heading. What proves its structure?',
                ['A larger font', 'Its blue color', 'It appears in the Navigation Pane'], 2,
                'A real heading style carries structure. Bold alone does not tell Word or a screen reader it is a heading.',
                [0, 1, 2, 3], None, A_ROUNDS),
        mission('Make the total recalculate', 'Excel · supplies.xlsx', 'Paper $12 + folders $8 + pens $5',
                'A tested formula, saved as .xlsx',
                ['Rows hold items; columns have labels and units.', 'In B5, enter =SUM(B2:B4).',
                 'Predict, change one cost, then check.'],
                [('Enter', '=SUM(B2:B4) → $25', 'Start with =. The colon means B2 through B4, including B3. Press Enter.'),
                 ('Predict', 'Paper $12 → $15: total?', 'Write your prediction before you edit. It should be $28.'),
                 ('Test', '15 + 8 + 5 = $28',
                  'If it stays $25, read the formula bar. Save as Excel Workbook; CSV keeps values only.')],
                ['Open supplies.csv; enter the SUM formula in B5.', 'Write a prediction, then change paper to 15.',
                 'Save as supplies.xlsx, an Excel Workbook.'],
                'Which formula includes all three cost cells?', ['=SUM(B2,B4)', '=SUM(B2:B4)', 'SUM(B2:B4)'], 1,
                'The colon includes the full range and = starts the formula. The comma here leaves out B3.',
                [4, 5], None, B_ROUNDS),
        mission('Show the message clearly', 'PowerPoint · resource-slides.pptx', 'An audience who needs computer help',
                'Three matching slides and a useful photo',
                ['Need → steps → where to get help.', 'Crop trims the frame; resize changes the size.',
                 'Add alt text and a permission credit.'],
                [('Arrange', 'Need computer help? · Steps · Where to get help',
                  'One theme on all three slides. Keep the same steps as your Word handout.'),
                 ('Crop', 'Keep the two people and the handout in view',
                  'Picture Format → Crop trims the edges. The cut edges stay in the file until you compress the picture.'),
                 ('Describe', 'Two people review a computer-help handout',
                  'Right-click → View Alt Text. Check any suggested description, then add the credit line.')],
                ['Make three matching slides from the starter text.', 'Insert the practice photo; crop and describe it.',
                 'Add the credit and save resource-slides.pptx.'],
                'What does cropping a picture change?', ['Its outer visible edges', 'The original file on disk',
                                                          'The meaning of its license'], 0,
                'Cropping changes the visible frame on the slide. Keep the original photo and check its reuse permission.',
                [6, 7], None, C_ROUNDS),
        mission('Export, then inspect', 'Word · resource-handout.pdf', 'A finished editable handout',
                'A separately opened and checked PDF',
                ['PDF for reading; editable files for changes.', 'CSV keeps values, not formulas or formatting.',
                 'Trim the ends; split to remove a middle section.'],
                [('Choose', 'Reader → PDF · Editor → DOCX',
                  'Keep the editable original. A picture in search results is not permission to reuse it.'),
                 ('Export', 'Save As → PDF → open it from the folder',
                  'Check the headings, steps and link in the PDF itself. That file is what the reader gets.'),
                 ('Edit media', 'Start · Explain · Pause · Next step · End',
                  'Trim removes the ends. Split, then remove the pause in the middle. Recheck speech and captions.')],
                ['Save the handout as PDF and reopen it.', 'Check its headings, numbered steps and link.',
                 'Choose a format for three different people.'],
                'What confirms your export is usable?', ['Word still looks correct', 'The PDF file exists',
                                                          'Open the PDF and check it'], 2,
                'A PDF is a separate file. Reopen that file and inspect what the reader will receive.',
                [8], None, D_ROUNDS),
    ])
