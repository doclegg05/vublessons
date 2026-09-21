"""Parallel, lesson-based classroom scenarios; not certification exam items."""
import json
from pathlib import Path
pairs=[]
def q(domain,week,objective,pre,post,why):
 # Each variant: scenario and decision, correct answer, two task-related distractors.
 pairs.append(dict(domain=domain,week=week,objective=objective,pre=pre,post=post,why=why))
q('Technology Basics',1,'1.1',
 ['At your local library, the text on a computer-help webpage is too small. Text in your other apps is comfortable to read. Which change best fits this problem?',
  'Increase the browser zoom for the webpage.', 'Increase display scaling for the whole computer.', 'Increase screen brightness without changing text size.'],
 ['You are reading a community workshop page at home. Its words are too small, but your email app and desktop labels are readable. What should you try first?',
  'Enlarge the webpage with browser zoom.', 'Enlarge every app with display scaling.', 'Increase screen brightness while leaving text size unchanged.'],
 'Browser zoom changes the size of webpage content. Display scaling affects the wider desktop, and brightness changes light output. Start with the control that matches the problem, then check the result.')
q('Technology Basics',1,'1.2',
 ['A library volunteer is arranging a practice session with you. They need to see when you are busy, but you want to keep appointment names and locations private. Which calendar setting best fits?',
  'Share free/busy availability only.', 'Share event titles and locations with the volunteer.', 'Publish the full calendar for anyone with the link.'],
 ['A community group is choosing a meeting time. The organizer needs your available times, not the details of your personal appointments. Which calendar information should you share?',
  'Free/busy times without appointment details.', 'Full event descriptions with the organizer.', 'All calendar details through a public link.'],
 'Free/busy sharing answers the scheduling question without exposing appointment details. Check the actual sharing settings and what the other person can see; sharing a whole calendar may reveal more than the task needs.')
q('Technology Basics',1,'1.3',
 ['While you draft a message about a library visit, autocorrect replaces your neighbor’s last name with a different word. The changed word is spelled correctly. What should you do before sending?',
  'Restore the intended name and reread the message.', 'Keep the change because the spelling checker accepts it.', 'Rely on the recipient to work out which name you meant.'],
 ['You begin typing a volunteer’s email address, and autocomplete selects another person with a similar name. The message is meant for only one volunteer. What should you do before sending?',
  'Check the full address and select the intended person.', 'Accept the suggestion because you have emailed that person before.', 'Send to both suggested addresses to reach the right person.'],
 'Autocorrect and autocomplete offer suggestions, not guarantees. Check names, full addresses and meaning yourself. A correctly spelled word or familiar contact can still be wrong for this message.')
q('Technology Basics',1,'1.5',
 ['You need 20 copies of a one-page computer-help handout. The lab has two printers, and the print dialog shows the one used yesterday. What should you do before printing the full set?',
  'Confirm the printer, inspect the preview and print one test copy.', 'Send 20 copies to the printer already selected in the dialog.', 'Send one copy to each printer, then use whichever finishes first.'],
 ['You need 15 copies of a library workshop flyer. You have changed the page layout since its last printout. Which step best avoids wasting paper?',
  'Check the destination and preview, then inspect one printed copy.', 'Print all 15 because the earlier layout printed correctly.', 'Send the job twice so a spare set will be ready.'],
 'The selected printer may be left over from another task, and a layout change can alter the output. Confirm the destination and preview, then inspect one test copy before sending the remaining copies.')
q('Digital Citizenship',4,'2.1',
 ['You use a personal account and a separate volunteer account. Before posting a library event notice, you notice your personal account is active. The notice should come from the volunteer account. What should you do?',
  'Switch accounts and check the posting identity and audience.', 'Post from the personal account and sign the volunteer group’s name.', 'Keep the personal account active and change only its profile photo.'],
 ['You are ready to answer a community group question in your volunteer role. Your browser has opened your personal profile instead. What is the best next step?',
  'Select the volunteer profile and confirm who will see the reply.', 'Reply from the personal profile because the same person owns both.', 'Copy the volunteer profile picture onto the personal reply.'],
 'The active account determines the identity attached to a post. A signature or profile picture does not switch accounts. Confirm both your role and the intended audience before posting.')
q('Digital Citizenship',4,'2.2',
 ['It is late at night, and you finish a nonurgent request for a library volunteer. You need a reply by Friday, and the group normally handles messages during daytime hours. Which approach is most considerate?',
  'Send during expected hours and state that a reply is needed by Friday.', 'Mark the message urgent so it gets attention tonight.', 'Ask for an immediate reply without mentioning the Friday deadline.'],
 ['On Sunday evening, you finish a handout for a team that reviews work on weekdays. Feedback is needed by Thursday. Which message plan gives a clear, reasonable expectation?',
  'Send during the team’s usual hours and ask for feedback by Thursday.', 'Send repeated reminders tonight until someone responds.', 'Request a reply as soon as possible without stating the deadline.'],
 'Match message timing to urgency and the group’s expectations. A specific deadline tells the recipient when to act. For a nonurgent task, an urgent label or repeated reminders creates needless pressure.')
q('Digital Citizenship',4,'2.2',
 ['During a library practice session, a partner asks what an abbreviation in your instructions means. You do not know their past computer experience. Which response best helps them continue?',
  'Explain the term in plain language and ask whether an example would help.', 'Repeat the abbreviation more slowly without explaining it.', 'Take over the task because their question shows they cannot do it.'],
 ['A new volunteer asks you to explain a term in a shared handout. They have not used this program before. Which response respects their experience and supports learning?',
  'Define the term and connect it to the task they are trying to do.', 'Tell them to memorize the term before asking more questions.', 'Assume their age explains the question and complete the task for them.'],
 'Explain the unfamiliar term and connect it to the task. One question does not tell you someone’s overall ability. Plain language and an offer of help support learning without making assumptions.')
q('Digital Citizenship',1,'2.3',
 ['You want to change an app’s download folder, but its menus changed after an update. An older printed guide shows a button you cannot find. What is the most useful next step?',
  'Use official help for the current version and search for changing the download folder.', 'Keep looking only for the old button shown in the printed guide.', 'Install an unfamiliar repair tool that promises to restore all old menus.'],
 ['You need to change a reminder in an updated calendar app. A saved tutorial shows a menu that is no longer there. How should you look for instructions that fit?',
  'Check current official help for the app and the reminder task.', 'Follow the old tutorial’s button positions even when the labels differ.', 'Choose the oldest tutorial because it has collected the most views.'],
 'Current official help is a good starting point when menus change. Identify the app version and the task, rather than relying only on old button positions. When asking for help, describe what you tried and what happened.')
q('Information Management',2,'3.1',
 ['You want an in-person computer-help session at a public library near Beckley, West Virginia. Which search gives the search engine the clearest description of your need?',
  'Beckley WV public library computer help sessions', 'computer help anywhere online', 'West Virginia community activities'],
 ['You want an in-person computer class at a public library near Elkins, West Virginia. Which search is the best starting point for this task?',
  'Elkins WV public library computer classes', 'computer classes around the world', 'West Virginia places to visit'],
 'Useful search terms name the service, place and setting you need. These searches are starting points, not proof that a class exists. Confirm current details with the library before making plans.')
q('Information Management',2,'3.2',
 ['A shared post says every library in your county offers free laptop loans. It gives no source or date. You want to borrow a laptop from your local library. What is the best way to check the claim?',
  'Contact that library through its official website or known phone number.', 'Treat the number of shares as proof that the offer is available.', 'Rely on another directory that repeats the same unsourced claim.'],
 ['An online directory says a nearby community center offers free computer repairs. It does not say where that information came from. What should you do before relying on the offer?',
  'Confirm the service through the center’s official contact information.', 'Assume the listing is verified because it is the first search result.', 'Use the directory’s professional appearance as evidence that the offer is current.'],
 'Verify a service with the organization responsible for providing it. Search position, appearance and repeated claims do not establish current availability. Check the details that matter for your visit.')
q('Information Management',2,'3.2',
 ['You need computer help you can attend locally in West Virginia. You find a current, accurate library page, but the class is in another state and is in person only. Why does this page not meet your need?',
  'The information can be accurate but not relevant to your location.', 'Any page about a library must apply to your local library too.', 'A current page is enough to show that the class is available nearby.'],
 ['You need a local workshop you can attend in person. A reliable community-center page lists a class in another state with no online option. What is missing for your task?',
  'A class relevant to the place where you can attend.', 'Proof that all information on the page must be false.', 'A more recent date, which would make the distant class local.'],
 'Accuracy and relevance are different checks. A trustworthy page can describe a real class that does not fit your location or attendance needs. Use the source that answers your actual question.')
q('Information Management',2,'3.3',
 ['In the fictional library practice form, you need to request computer help. The form has required fields and several optional fields. What should you check before entering information?',
  'Who receives it, why it is needed and which fields the request requires.', 'How to fill every optional field, even when it adds unrelated details.', 'Whether entering extra private details will move the request ahead of others.'],
 ['A fictional community-center form lets you request a workshop place. Some fields are optional and do not seem related to booking. What is the best approach before completing the form?',
  'Check the collector and purpose, then provide only information needed for the task.', 'Treat every visible field as required and supply as much detail as possible.', 'Assume a form with the center’s name can request any personal information.'],
 'Check who collects the information, the purpose and the required fields. Optional does not mean necessary. In class, use fictional details; review the completed request and read its confirmation.')
q('Content Creation',3,'4.1',
 ['You are making a library handout with sections called Getting started, Practice steps and Where to get help. Readers should be able to navigate its sections, including with a screen reader. How should you mark the section titles?',
  'Apply the document’s appropriate heading styles.', 'Make the titles bold but leave them as ordinary paragraphs.', 'Insert extra blank lines above each title without using headings.'],
 ['Your community workshop guide has three main sections. You want clear structure that assistive technology can recognize, not just titles that look different. What should you use?',
  'Built-in heading styles at the appropriate level.', 'Larger font sizes on ordinary paragraphs only.', 'Pictures of the section titles instead of text headings.'],
 'Heading styles give section titles structural meaning, which helps navigation and assistive technology. Bold, font size and spacing can change appearance without creating that structure.')
q('Content Creation',3,'4.1',
 ['Your practice budget lists paper at $12 in B2, folders at $8 in B3 and pens at $5 in B4. You want a total that updates if any cost changes. Which formula belongs in the total cell?',
  '=SUM(B2:B4)', '=B2+B4', '=25'],
 ['Your practice supply list has 6 notebooks in C2, 4 folders in C3 and 3 pens in C4. You want the total quantity to update if any entry changes. Which formula should you use?',
  '=SUM(C2:C4)', '=C2+C4', '=13'],
 'The colon includes every cell in the range, including the middle row. Adding only the first and last cells misses an item. A fixed number can look correct now but will not update when an input changes. Test the formula by changing one input.')
q('Content Creation',3,'4.3',
 ['You find a photograph through an image search and want to add it to a community handout. The search preview does not show reuse terms. What should you do before using it?',
  'Open the source, check allowed uses and follow any required credit conditions.', 'Use it with the creator’s name because credit alone always grants permission.', 'Use it without checking because the handout will be given away free.'],
 ['You want to adapt a diagram from a website for a library workshop handout. You have not checked its license or permission terms. What should you do first?',
  'Check whether adapting it is allowed and what attribution is required.', 'Change the colors and assume it is now entirely your own work.', 'Use a screenshot because that avoids the need to check reuse terms.'],
 'Find the actual license or permission and follow its conditions, including whether changes are allowed and what credit is needed. Credit, a screenshot or free distribution does not by itself establish permission. Use an approved alternative if permission is unclear.')
q('Content Creation',3,'4.4',
 ['A partner needs to rewrite two paragraphs in your workshop handout. You want them to edit the wording directly. Which file and access best support that task?',
  'An editable document with permission for the partner to edit.', 'A picture of the page that lets the partner see the wording.', 'An editable document shared with view-only permission.'],
 ['A coauthor must correct the wording in your community resource guide before it is finished. Which sharing choice lets them make those changes directly?',
  'Share the editable file with suitable editing access.', 'Send only a screenshot of the current guide.', 'Share the editable file with reading access only.'],
 'Direct revision needs both an editable format and permission to edit. A screenshot shows the content but does not provide editable paragraphs. A view-only link also prevents the intended task; a checked PDF can be useful later for finished distribution.')
q('Communication',4,'5.1',
 ['You are emailing the library to ask which room will host its computer-help session. Which subject line best tells the recipient what you need?',
  'Please confirm the room for the computer-help session', 'A question about something at the library', 'Computer-help session room confirmed'],
 ['You are emailing a community organizer to ask when the resource workshop starts. Which subject line most clearly describes your request?',
  'Please confirm the resource workshop start time', 'Information about a community activity', 'Resource workshop start time confirmed'],
 'A useful subject names the topic and the action needed. A vague subject hides the request, while saying something is confirmed incorrectly suggests the question is already settled. Put the needed context in the message as well.')
q('Communication',4,'5.1',
 ['You are sending a workshop announcement to people who do not need to see one another’s email addresses. Which choice hides that recipient list from the other recipients?',
  'Place those addresses in Bcc.', 'Place those addresses in Cc.', 'Place all those addresses in To.'],
 ['You are emailing a library event reminder to several volunteers. They should receive the message without seeing the full list of other recipients’ addresses. Which field fits?',
  'Bcc for the addresses that should be hidden.', 'Cc for the addresses that should be hidden.', 'To for every address in the list.'],
 'Bcc hides those recipient addresses from other recipients; To and Cc normally show them. Bcc does not encrypt the message, stop forwarding or make an attachment safe.')
q('Communication',4,'5.2',
 ['A fictional design app offers a seven-day free trial for making a community flyer. You only need it for one project. What should you check before starting the trial?',
  'Whether it renews, what it will cost and how and when to cancel.', 'Only whether the first seven days are free.', 'Only whether deleting the app removes it from the computer.'],
 ['A fictional video service offers a free month, and you only want to try one lesson. What information do you need before accepting the offer?',
  'Renewal timing, the later price and cancellation terms.', 'Only the price shown for the first month.', 'Only whether you can remove the app icon afterward.'],
 'Look beyond the introductory price to renewal and cancellation terms. Removing an app is not the same as following the service’s cancellation process. The class uses fictional offers and does not require a real purchase.')
q('Communication',4,'5.2',
 ['You downloaded a fictional photo app for free. A new button offers extra templates for a one-time $4 charge. What should you do before choosing that upgrade?',
  'Review the separate purchase and its terms before deciding whether to authorize it.', 'Assume the templates are free because the app cost nothing to download.', 'Approve the purchase first and check what it costs afterward.'],
 ['A fictional free app offers an optional tool for a one-time $3 charge. You are reviewing the offer in class. What should happen before anyone authorizes that upgrade?',
  'Review the separate charge and purchase terms before deciding.', 'Accept it as free because downloading the app cost nothing.', 'Approve it now and review the cost after trying the tool.'],
 'The download price and the price of an extra feature are separate. Read the purchase details before authorizing anything; do not assume when or whether a charge applies. No real payment is needed for the practice.')
q('Collaboration',4,'6.1',
 ['Two library volunteers open the same shared handout during a live call. Both edit it while discussing their changes. Which description fits the way they are working?',
  'Synchronous collaboration: working together at the same time.', 'Asynchronous collaboration: leaving work for someone to review later.', 'Independent copies: each person edits a separate file.'],
 ['A community team meets online and edits one shared workshop outline together during the meeting. What type of collaboration is this?',
  'Synchronous work because people are collaborating at the same time.', 'Asynchronous work because the file is stored online.', 'Separate-copy work because each person has a different computer.'],
 'Synchronous means working together at the same time. Asynchronous work happens at different times, such as leaving comments for tomorrow. Online storage and separate computers do not determine which timing pattern the team uses.')
q('Collaboration',4,'6.1',
 ['Your library handout needs a partner’s feedback. They should leave comments, but you will make the wording changes. The sharing tool offers Viewer, Commenter and Editor. Which access best fits?',
  'Commenter for the named partner.', 'Viewer for the named partner.', 'Editor for anyone with the link.'],
 ['You want a volunteer to point out unclear steps in a draft. They should add feedback without directly changing the document. The tool supports comments. Which permission should you give?',
  'Commenter access to that volunteer.', 'View-only access to that volunteer.', 'Editing access to anyone who receives the link.'],
 'Commenter access supports feedback without direct rewriting. Viewer access does not provide the requested commenting ability in this scenario, and a public editing link gives more access than the task requires.')
q('Collaboration',4,'6.1',
 ['A partner’s computer-help handout says “contact us” but gives no phone number or other contact method. Which comment best explains a useful revision?',
  'Add a contact method after the steps so readers know how to get help.', 'Make the handout better before we share it.', 'Change the title color; that should solve the missing contact information.'],
 ['A workshop guide uses an abbreviation without explaining it. New readers may not know what it means. Which comment would best help the author revise the guide?',
  'Spell out the abbreviation the first time so new readers can follow the steps.', 'Improve this section because it needs more work.', 'Make the abbreviation bold so an explanation is no longer needed.'],
 'Useful feedback identifies the specific problem, suggests a change and explains how readers benefit. Vague criticism leaves the author guessing. A cosmetic change does not supply missing information.')
q('Collaboration',4,'6.2',
 ['You want to record an online volunteer meeting so an absent partner can review it. Participants will be visible and speaking. What should happen before you start recording?',
  'Check the organizer’s rules and obtain the appropriate recording permission.', 'Assume joining the meeting means everyone agreed to be recorded.', 'Start recording because the meeting software offers a Record button.'],
 ['You would like to save a video discussion from a library workshop for later study. The recording would include other participants. What should guide your next step?',
  'Follow the organizer’s recording rules and confirm the needed permission.', 'Treat an invitation to attend as automatic permission to record.', 'Record first because you intend to keep the file for your own use.'],
 'The presence of a Record button or an invitation does not establish recording permission. Check the organizer’s rules and the appropriate permissions before recording participants. A helpful purpose does not replace that check.')
q('Safety and Security',5,'7.1',
 ['One learner uses a keyboard instead of a mouse. Another needs captions to follow spoken directions. Which version of a library learning page supports both needs?',
  'A page with keyboard-operated controls and captioned videos.', 'A page with captions but controls that require a mouse.', 'A page with keyboard controls but spoken directions available only as audio.'],
 ['A volunteer cannot comfortably use a mouse, and another studies with the sound off. Which workshop page would let both people complete the task?',
  'One with keyboard access and accurate captions for spoken content.', 'One with keyboard access but no text alternative to spoken content.', 'One with captions but buttons that work only with a mouse.'],
 'Flexible input and captions address different needs. Providing both lets more people complete the same task in different situations. Supporting one need does not remove the other barrier.')
q('Safety and Security',5,'7.2',
 ['In a fictional online group, a new contact quickly becomes friendly, claims to be a local volunteer and asks for private information. You have not verified their identity. What is the best response?',
  'Pause the request and verify their identity through a separate trusted route.', 'Trust the request because the profile includes local photos.', 'Ask the same contact to promise the profile is real, then send the information.'],
 ['In a fictional community forum, someone you have never met builds a friendly relationship and asks you to keep a request for private information secret. Their identity is unverified. What should you do?',
  'Withhold the information and check their identity independently.', 'Rely on the friendly conversation as proof of who they are.', 'Accept a second profile sent by the same person as independent proof.'],
 'A false identity used to build trust is called catfishing. This scenario does not prove the person is an impostor, but friendliness and local photos do not verify identity. Pause and check through a separate trusted route before sharing private information.')
q('Safety and Security',5,'7.3',
 ['You find an unknown USB drive beside a computer in the library lab. You would like to return it to its owner. What is the safest next step?',
  'Give it to the instructor or authorized staff without connecting it.', 'Plug it into a lab computer to look for the owner’s name.', 'Try it on your own laptop so the shared lab computer is not affected.'],
 ['An unfamiliar person leaves a USB drive labeled “useful workshop files” at the community computer lab. Staff have not approved it. What should you do?',
  'Keep it disconnected and ask authorized staff what to do.', 'Open it briefly because the label describes useful material.', 'Use a different lab computer to test whether the files open.'],
 'An unknown drive can carry harmful software. Its label and appearance do not prove it is safe, and switching computers does not remove the risk. Let authorized staff handle it without connecting it yourself.')
q('Safety and Security',5,'7.3',
 ['A practice file can still be read even after you mark it read-only. You want to protect its readable contents if someone gets a copy without the needed key. Which feature addresses that goal?',
  'Encryption of the file’s contents.', 'Read-only settings that restrict editing.', 'A ZIP archive created without encryption.'],
 ['You are protecting a stored practice document. Preventing edits is not enough; someone without the key should be unable to read its contents. Which protection matches that need?',
  'Encrypting the stored data.', 'Renaming the document to make it less obvious.', 'Compressing it into an unencrypted ZIP file.'],
 'Encryption protects readable data by requiring the appropriate key or authorized access. Read-only settings restrict changes, renaming changes a label, and an ordinary ZIP is not automatically encrypted. An unlocked account or device still needs protection.')
variants={}
for kind in ['pre','post']:
 items=[]
 for i,p in enumerate(pairs):
  question,correct,*wrong=p[kind]
  choices=[correct,*wrong]; offset=(i+(1 if kind=='post' else 0))%3
  choices=choices[offset:]+choices[:offset]
  items.append(dict(id=f'{kind}-{i+1:02}',pair=i+1,domain=p['domain'],week=p['week'],objective=p['objective'],question=question,options=choices,answer=choices.index(correct),why=p['why']))
 variants[kind]=items
Path('courses/digital-literacy-2/assets/questions.json').write_text(json.dumps(variants,indent=2)+'\n')
print('Authored',len(pairs),'parallel scenario pairs; 4 questions per domain')
