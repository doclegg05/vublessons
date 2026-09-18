"""Parallel original classroom questions; not certification exam items."""
import json
from pathlib import Path
pairs=[]
def q(domain,week,objective,pre,post,why):
 # Each variant: question, correct answer, two plausible distractors.
 pairs.append(dict(domain=domain,week=week,objective=objective,pre=pre,post=post,why=why))
q('Technology Basics',1,'1.1',
 ['A webpage is difficult to read, but other apps look fine. Which adjustment best fits?','Increase browser zoom','Change the default printer','Rename the Downloads folder'],
 ['The text on a service website is too small. What should you try first?','Use the browser’s zoom control','Buy more online storage','Change the email signature'],
 'Browser zoom changes webpage size. Choose the control that matches the problem.')
q('Technology Basics',1,'1.2',
 ['A partner needs your availability, but not appointment details. Which calendar share fits?','Free/busy availability','All private event notes','Your account password'],
 ['A volunteer scheduler only needs to know when you are unavailable. What should you share?','Free/busy information','Every event description','Your recovery codes'],
 'Free/busy can support scheduling without disclosing event details. Verify the service’s options.')
q('Technology Basics',1,'1.3',
 ['Autocorrect changes a person’s name in your message. What should you do?','Review and correct the name before sending','Assume the suggestion is always correct','Disable every security setting'],
 ['Autocomplete suggests the wrong email address. What is the best response?','Check and choose the intended address','Send it because the app suggested it','Share your password with both people'],
 'Automation can save time but needs review, especially for names, addresses and meaning.')
q('Technology Basics',1,'1.5',
 ['Before printing 20 copies, what is the most useful check?','Confirm the printer and preview one test page','Select every available printer','Change the computer’s wallpaper'],
 ['A handout is going to a shared lab printer. What should you verify first?','Printer destination, preview and a test page','The number of browser bookmarks','Whether the email inbox is empty'],
 'Verify the destination and output before sending a large print job.')
q('Digital Citizenship',4,'2.1',
 ['You manage personal and volunteer accounts. What is a sensible practice?','Check the active account and use separate credentials','Reuse one password everywhere','Post every message from whichever account opens'],
 ['Before posting in a professional group, what should you check?','The active identity, audience and account credentials','Only the screen brightness','Whether your personal posts are entertaining'],
 'Check the identity and audience. Keep credentials distinct and use appropriate account protections.')
q('Digital Citizenship',4,'2.2',
 ['A nonurgent work message is ready late at night. What should guide when you send it?','Recipient expectations, urgency and working hours','How many emojis are in it','The size of your monitor'],
 ['You need feedback next week. What is a considerate communication choice?','State the deadline and respect expected working hours','Demand an immediate reply at any hour','Send the same message every five minutes'],
 'Timing and a clear response expectation help the recipient respond appropriately.')
q('Digital Citizenship',4,'2.2',
 ['Which wording best respects different levels of experience?','Here are the steps; tell me where more detail would help.','Everyone your age struggles with this.','This is obvious, so do not ask questions.'],
 ['A new teammate does not know an abbreviation. What should you do?','Explain it plainly without making assumptions','Assume their age explains the problem','Exclude them from the task'],
 'Inclusive communication explains context and avoids assumptions about age, culture or ability.')
q('Digital Citizenship',1,'2.3',
 ['An app feature has changed. What is a useful learning response?','Check official help for your version and try the steps','Assume all old instructions still apply','Give up without identifying the task'],
 ['You cannot find a command in an updated app. What is the best next step?','Use current official help and describe the exact task','Download the first unfamiliar fix offered','Share your password in a public forum'],
 'Version-specific help and a precise question support independent learning.')
q('Information Management',2,'3.1',
 ['You need a nearby library computer class. Which search is most useful?','Library computer class plus your town','Interesting things','Every website'],
 ['You need local public-library opening hours. Which query best fits?','Library name, town and opening hours','Libraries everywhere','Good places'],
 'Search terms should identify the service and location needed for the task.')
q('Information Management',2,'3.2',
 ['A post claims a community service is available everywhere. How should you check it?','Verify with the responsible organization','Trust it because it is first in search','Count how many colors the page uses'],
 ['A directory promises a local service without naming a source. What is the best check?','Confirm availability through the provider’s official contact','Assume a polished design proves the claim','Share the claim before checking'],
 'Responsible sources and corroborating evidence matter more than ranking or appearance.')
q('Information Management',2,'3.2',
 ['An accurate page describes a service in another state. Why might it be unsuitable?','It may not be relevant to your local need','Accurate pages are never useful','Every government page applies everywhere'],
 ['A reliable article explains an old program that no longer operates locally. What is the problem?','It may be outdated or irrelevant to this task','Its accuracy proves current availability','A readable font guarantees relevance'],
 'Accuracy, currency and relevance are separate questions.')
q('Information Management',2,'3.3',
 ['Before submitting an online form, what should you check?','Who collects the data, required fields and the confirmation','Only its background color','Whether you can enter extra private details'],
 ['A service-request form asks for information unrelated to the request. What should you do?','Check the purpose and collector before providing it','Fill every field with real private information','Assume all forms have the same rules'],
 'Understand the collection purpose, provide only needed information, and check the result.')
q('Content Creation',3,'4.1',
 ['Which feature creates a document structure useful to readers and assistive technology?','Heading styles','Random blank lines','Making every line bold'],
 ['How should you mark a document’s main sections?','Apply appropriate heading styles','Add only larger spaces','Turn the entire document into an image'],
 'Real heading styles provide structure; visual bolding alone does not.')
q('Content Creation',3,'4.1',
 ['B2, B3 and B4 contain costs. Which formula totals all three?','=SUM(B2:B4)','=B2+B4','=SUM(A1:A2)'],
 ['C2, C3 and C4 contain quantities. Which formula totals that range?','=SUM(C2:C4)','=C2+C4','=SUM(B1:B2)'],
 'A colon marks an inclusive cell range. Verify the formula by changing one input.')
q('Content Creation',3,'4.3',
 ['You find an image online for a handout. What should you do before reusing it?','Check permission or license and provide required credit','Assume search results are free to reuse','Remove the creator’s name'],
 ['You want to adapt someone else’s diagram. What is the right first step?','Check allowed uses and attribution conditions','Use it without credit if it is small','Assume a screenshot avoids all restrictions'],
 'Find the actual reuse permission and follow its conditions.')
q('Content Creation',3,'4.4',
 ['A partner needs to revise your paragraphs. Which format best fits?','An editable document with appropriate access','Only a photograph of the page','An audio recording with no text'],
 ['A coauthor must change wording in your handout. What should you provide?','The editable file with suitable permissions','Only a locked screenshot','A filename without the file'],
 'Choose the format and access that support the recipient’s task. PDF is often useful for finished layout.')
q('Communication',4,'5.1',
 ['Which email subject best supports a clear request?','Question about computer-help session location','Hi','Important stuff'],
 ['Which subject best helps a recipient act on a schedule question?','Please confirm the resource workshop start time','Message','Read this now!!!'],
 'A specific subject tells the recipient what the message concerns.')
q('Communication',4,'5.1',
 ['What does Bcc do in an email?','Hides Bcc recipient addresses from other recipients','Encrypts all message content','Verifies every recipient’s identity'],
 ['You use Bcc for an announcement. What protection does it provide?','Conceals that recipient list from other recipients','Guarantees the message cannot be forwarded','Makes an attachment malware-free'],
 'Bcc hides recipient addresses; it does not encrypt content or prevent forwarding.')
q('Communication',4,'5.2',
 ['Before starting a free app trial, what should you inspect?','Renewal price, timing and cancellation terms','Only the download button','Only how many icons appear'],
 ['A streaming offer starts at no charge. What should you check before accepting?','Whether it renews, the price and how to cancel','Whether its logo is familiar','Whether it plays an animation'],
 'Free trials can become recurring subscriptions. Review the terms and total cost.')
q('Communication',4,'5.2',
 ['A free game offers an in-app upgrade. What should you remember?','The upgrade may charge money even though the app was free','Everything inside a free app is always free','Payment screens never need review'],
 ['A downloaded app offers extra features for purchase. What is a sensible step?','Review the charge and purchase controls before authorizing','Approve automatically because downloading was free','Share a payment password with the group'],
 'In-app purchases are separate transactions; check terms, controls and receipts.')
q('Collaboration',4,'6.1',
 ['Two people edit a shared document together at the same time. What is this?','Synchronous collaboration','A private backup','Offline archiving'],
 ['A team coauthors a file during a live call. Which description fits?','Synchronous collaboration','Asynchronous-only feedback','File compression'],
 'Synchronous collaboration happens at the same time; asynchronous work happens at different times.')
q('Collaboration',4,'6.1',
 ['A reviewer should suggest wording but not directly rewrite the file. Which access fits when supported?','Commenter','Public editor for everyone','No access at all'],
 ['A partner only needs to leave feedback on your draft. Which permission is appropriate when available?','Commenter access','Unrestricted editing by anyone with the link','Your account password'],
 'Commenter access fits feedback without granting direct editing rights.')
q('Collaboration',4,'6.1',
 ['Which feedback is most useful?','Add a contact number after the steps so readers can find help.','Bad work.','Change everything somehow.'],
 ['Which comment best helps improve a shared handout?','Define this abbreviation so a new reader can follow the instructions.','I do not like it.','You never do this right.'],
 'Useful feedback names a specific change and explains the benefit.')
q('Collaboration',4,'6.2',
 ['Before recording a class video meeting, what should you do?','Ask permission and follow the group’s rules','Record secretly','Assume joining is always recording consent'],
 ['You want to save a webinar discussion that includes participants. What should guide your decision?','Organizer rules and appropriate recording permission','Whether the record button is easy to find','Only how much storage you have'],
 'Meeting etiquette includes checking recording permissions and respecting participants.')
q('Safety and Security',5,'7.1',
 ['What is an example of universal design?','Controls usable by keyboard as well as mouse','Instructions available only through color','Very small fixed-size text'],
 ['Which feature helps people use technology in different situations?','Captions and flexible input methods','A mouse-only form','Audio-only directions without text'],
 'Universal design increases usability across needs and situations.')
q('Safety and Security',5,'7.2',
 ['An online contact uses a false identity to build trust. What is this commonly called?','Catfishing','File versioning','Autocomplete'],
 ['Someone invents a personal profile to manipulate a relationship. Which term fits?','Catfishing','Cloud syncing','Compression'],
 'Catfishing uses a false identity to build trust or manipulate someone. Pause and verify independently.')
q('Safety and Security',5,'7.3',
 ['You find an unknown USB drive in the lab. What should you do?','Give it to authorized staff without plugging it in','Open it to find the owner','Copy it to every computer'],
 ['A stranger offers a USB drive with a useful app. What is the safest class response?','Do not connect it; consult authorized support','Run it immediately','Disable protections to open it'],
 'Untrusted portable media can carry harmful software. Follow approved device procedures.')
q('Safety and Security',5,'7.3',
 ['What is the purpose of encryption?','Make data unreadable without the appropriate key','Make every website honest','Reduce all files to half their size'],
 ['An encrypted device is lost while powered off. What does encryption help protect?','The readability of stored data without its key','The truth of all messages ever received','The ability to cancel every subscription'],
 'Encryption protects data readability. It does not replace other account, device or trust checks.')
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
print('Authored',len(pairs),'parallel pairs; 4 questions per domain')
