"""Topic-specific illustrated teaching scenes. All examples are fictional and local."""
import html
E=lambda s:html.escape(str(s),quote=True)
# Each choice changes the worked example; explanatory prose remains in the source slide.
# label, artifact headline, artifact content, teaching consequence
SCENES={
(1,8):('browser','Choose a browser default',[
 ('Home page','Start with your task','Library resources → browser home','Choose the page you actually use. A default can be changed again.'),
 ('Downloads','Know where the file went','Downloads / resource-guide.pdf','Choose a folder you can find, then check one downloaded file.'),
 ('Permissions','Match access to the task','Text resource page → camera blocked','A text-only page does not need your camera. Review site permissions.')]),
(1,9):('computer','Follow the work through a computer',[
 ('Processor','Carry out instructions','Instruction → processing → result','The processor performs the requested operations.'),('Memory','Hold current work','Open document + current task','Memory supports work in progress; it is not a substitute for saving.'),('Storage','Keep a saved copy','resource-guide.docx → saved file','Storage keeps files. Check where your work is saved.'),('Connection','Check the capability','Device → matching port → supported feature','A matching shape does not prove the cable supports every feature.')]),
(1,11):('printer','Choose for the print job',[
 ('Laser','Toner-based printing','Document → toner → printed page','Compare the running cost and task, not just the purchase price.'),('Inkjet','Liquid-ink printing','Document → ink → printed page','Check the type of output you need and the cost of replacement ink.'),('Default','Which printer is selected?','Print destination: Training room','Default means the app initially selects it. Check before sending.')]),
(1,13):('calendar','Build a usable event',[
 ('When','Library visit','Monday · 10:00–11:00','Include the day and both start and end times.'),('Where','Library visit','Community library · learning desk','A useful location tells you where to go.'),('Reminder','Library visit','Reminder: 30 minutes before','Choose a reminder you will notice. Check time zones for another region.')]),
(1,16):('automation','Inspect the automatic result',[
 ('Autocorrect','A change was made','Typed wording → changed wording','Check names and meaning before keeping the correction.'),('Autocomplete','A suggestion is offered','Typed beginning → suggested ending','You decide whether the suggestion matches what you meant.'),('Rule','A repeated action','Matching mail → chosen folder','Test a rule with one item and check that it went to the right place.')]),
(1,17):('network','Follow a cloud save',[
 ('This device','Your work begins here','Laptop → network → provider','Check which account is signed in before saving.'),('Provider','A computer elsewhere','Provider stores the saved file','The service uses computers reached through a network.'),('Other device','Open the saved version','Provider → network → second device','Check connection and save status before assuming the latest work is there.')]),
(1,19):('support','Make a useful help request',[
 ('Task','What are you trying to do?','I want to print one page.','Name the goal before describing the problem.'),('Tried','What happened already?','I selected the training-room printer.','Explain what you tried so the next person can help with the next step.'),('Error','What did the app say?','Message: printer unavailable','Record the exact message and app version. Use official help.')]),
(2,3):('search','Build a search with a purpose',[
 ('Too broad','help','Many different kinds of help','Start with the service you need.'),('Specific service','public library computer help','Service: computer help · provider: library','Add the place to make the result useful locally.'),('Add your place','public library computer help [your town]','Service + provider + location','Replace the bracketed place with your town and inspect the results.')]),
(2,4):('search','Narrow a search deliberately',[
 ('Exact phrase','“computer help”','Only this phrase','Quotation marks can narrow a phrase. They can also hide useful alternatives.'),('Domain','site:example.org computer help','One domain','A domain filter narrows where you search; it does not prove a claim.'),('Date','Recent results','A narrower time window','Use a date filter when recency matters, then verify the page itself.')]),
(2,7):('source','Separate correct from useful',[
 ('Correct, wrong place','Library hours in another state','Accurate location · irrelevant to this task','A true fact may not answer your local question.'),('Recent, unverified','New service announcement','Recent date · claim still needs checking','A new date is not proof. Verify evidence and purpose.'),('Useful evidence','Official local service page','Right place · current details · contact','Confirm that the source answers the question you actually have.')]),
(2,8):('document','Leave a trail another person can follow',[
 ('Identify','Computer-help service','Organization: Community Library','Record the title and organization.'),('Locate','Where you found it','URL: example.org/help · access date: [today]','Record the URL and when you accessed it.'),('Separate','Source words versus your words','Quotation: exact words / Summary: your explanation','Mark a quotation clearly and record the specific detail you used.')]),
(2,9):('form','Pause before filling a form',[
 ('Collector','Who receives this?','Community learning team','Identify the collector and purpose before entering information.'),('Required','What does the task need?','Help topic: required / extra detail: optional','Only provide the information needed for the task.'),('Review','What will be submitted?','Topic: finding a file · method: desk visit','Review your choices and read the confirmation. Use fictional data here.')]),
(2,11):('files','Make the filename do useful work',[
 ('Unclear','final-final-new.docx','What is it? Which version?','This name makes the next person guess.'),('Clear','library-resource-v1.docx','Subject: library resource · version: 1','A subject and version make the file easier to identify.'),('Organized','Resources / library-resource-v1.docx','Related files → one folder','Combine a clear name with a folder you can find.')]),
(2,12):('network','A shared link is a doorway',[
 ('Shared copy','One common file','Owner → shared storage → collaborators','Agree which shared location holds the current copy.'),('Access','Who can enter?','Named people + assigned permissions','The service, account or organization controls access.'),('Ownership','Who controls the file?','Shared link ≠ transfer of ownership','Receiving a link does not make someone the owner.')]),
(2,16):('lock','Choose the protection you mean',[
 ('Read-only','Can read; cannot edit','Readable content · changes restricted','Read-only limits changes. It does not hide the content.'),('Encryption','A key is needed to read','Protected content → key → readable content','Encryption protects readable content with a key.'),('Password type','Open or edit?','Password to open / password to edit','Inspect what the chosen password setting actually protects.')]),
(2,17):('archive','Pack, then unpack',[
 ('Pack','resources.zip','handout.docx + budget.csv → ZIP','An archive bundles files and may reduce their size.'),('Extract','Resources folder','ZIP → handout.docx + budget.csv','Extract the files before editing them.'),('Protect?','ZIP is not a security promise','Bundled ≠ encrypted','A ZIP file is not automatically encrypted; media may already be compressed.')]),
(3,4):('keyboard','Choose the shortcut by its job',[
 ('Copy','Ctrl / Command + C','Selected text → clipboard','Select only the content you want to copy.'),('Paste','Ctrl / Command + V','Clipboard → insertion point','Place the cursor before pasting.'),('Undo','Ctrl / Command + Z','Last change → previous state','Use undo to reverse an unwanted edit.'),('Save','Ctrl / Command + S','Current work → saved file','Check the filename and destination.')]),
(3,5):('document','Compare a vague and useful paragraph',[
 ('Vague','Help is available','Contact someone for more information.','The reader still does not know what to do.'),('Useful','Computer help at the learning desk','Bring one computer question to the learning desk.','State the service, who it helps and the next action. Read it aloud.')]),
(3,6):('revision','The owner decides what stays',[
 ('Propose','Suggested wording','“Contact us” → “Visit the learning desk”','Track Changes or Suggesting makes the edit a proposal.'),('Accept','Keep the proposed wording','Visit the learning desk','The reviewer accepts the change into the document.'),('Reject','Keep the original wording','Contact us','The reviewer can reject it; a comment can explain the reason.')]),
(3,7):('document','Make the handout usable in more ways',[
 ('Heading','Structure, not just bold','Heading style → a navigable section','Real heading styles communicate document structure.'),('Link','Name the destination','Read the computer-help guide','Meaningful link text explains where a link goes.'),('Image','Describe useful information','Alt text: what the reader needs from this image','Describe informative images and avoid color-only instructions.')]),
(3,8):('cells','Read a cell address',[
 ('Column','B is the cost column','A: Item / B: Cost ($)','A column groups one category; label its unit.'),('Row','2 is the Paper row','Row 2: Paper / 12','A row can represent one item.'),('Cell','B2 is 12','Column B + Row 2 → B2','Keep numeric values as numbers so formulas can calculate.')]),
(3,12):('storyboard','Build a three-slide message',[
 ('The need','I need computer help','Why the audience should care','Lead with the problem the audience recognizes.'),('The steps','Choose a task. Visit the desk.','What the audience can do','Make the action sequence clear.'),('Get help','Bring your question','Where the audience goes next','Use a consistent theme and readable contrast across all three.')]),
(3,16):('license','Search visibility is not permission',[
 ('Find','An image in search','Visible online','Finding an image does not establish reuse rights.'),('Check','License and conditions','Allowed use + required conditions','Check whether the license fits your intended use.'),('Credit','Give the required attribution','Creator · title · source · license','Preserve the credit and meet the license conditions.')]),
(3,18):('export','Test the exported file itself',[
 ('Open','resource-guide.pdf','Open the separate exported file','Do not judge the export only by the editor view.'),('Inspect','Content and layout','Headings · page breaks · links · images','Look for missing content and broken reading order.'),('Locate','Right name, right folder','Resources / resource-guide.pdf','Verify the filename and destination before sharing.')]),
(4,3):('identity','Check the identity attached to your action',[
 ('Account','Who am I signed in as?','Training account → class activity','Use the account appropriate to the role.'),('Tone','Who will read this?','Clear request → respectful wording','Match tone to the audience and purpose.'),('Protection','Separate your credentials','Password manager + multifactor authentication','Use separate credentials and available account protections.')]),
(4,5):('email','Inspect the recipient fields',[
 ('To','Main recipient','To: Alex','Name the person who needs to act.'),('Cc','Visible information copy','To: Alex / Cc: Sam','Cc recipients are visible to the other recipients.'),('Bcc','Hidden recipient list','To: Alex / Bcc: Pat','Bcc hides that recipient list from others. It does not encrypt the message.')]),
(4,6):('calendar','Give the message a useful time',[
 ('Deadline','State when an answer helps','Please reply before our next practice session.','A clear response time helps the recipient plan.'),('Working hours','Check the recipient’s context','Send now / schedule for working hours','Consider urgency and working hours.'),('Scheduled send','Review before scheduling','Recipient + wording + scheduled time','Scheduling does not correct an unclear message. Verify the settings.')]),
(4,7):('conversation','Remove the guesswork from a message',[
 ('Name','Use the person’s preference','Preferred name and form of address','Ask or use the preference already provided.'),('Abbreviation','Explain the first use','Multifactor authentication (MFA)','Do not assume everyone knows an abbreviation.'),('Invitation','Make room for different needs','Which way of reviewing this works for you?','Avoid assumptions about age, ability or technology experience.')]),
(4,8):('community','Participate without taking over',[
 ('Read','Learn the group’s rules','Guidelines → topic → contribution','Understand the expectations before posting.'),('Disagree','Address the idea','I see a different option because…','Keep disagreement respectful and specific.'),('Share','Ask before using another person’s story','Permission first → share only what was agreed','Someone else’s image or experience is not yours to publish automatically.')]),
(4,9):('source','Turn a directory lead into verified details',[
 ('Lead','A directory entry','Possible service → needs confirmation','Treat the entry as a starting point.'),('Confirm','Use the official contact','Eligibility · availability · hours','Ask the organization directly or check its official website.'),('Use','Make the next step practical','Who to contact + when + requirements','Details can change, so confirm what matters to the task.')]),
(4,10):('roles','Give each person a clear job',[
 ('Owner','Coordinates the shared file','Sets access and what “finished” means','Agree where the common copy lives.'),('Writer','Drafts the content','Makes the planned edits','Work on the agreed copy to avoid competing versions.'),('Reviewer','Checks the result','Specific feedback → writer response','Give the next person a clear action.')]),
(4,13):('revision','Close the feedback loop',[
 ('Read','Understand the comment','Ask if the request is unclear','Do not resolve feedback before understanding it.'),('Respond','Make or decline the change','Change + reason / decline + reason','Explain the decision so the reviewer understands.'),('Resolve','Mark the discussion handled','Resolved comment · version history retained','Use version history if a useful edit is lost.')]),
(4,16):('receipt','Identify what you are getting',[
 ('Good','A product','A physical keyboard','Goods are products.'),('Service','Work or access','Computer support session','Services provide work or access.'),('Subscription','Ongoing access','Renews until canceled under its terms','Streaming delivers media over a connection; check any renewal terms.')]),
(4,17):('receipt','Inspect a fictional checkout',[
 ('Seller','Who receives the payment?','Seller: Practice Learning Store','A familiar logo alone does not verify the seller.'),('Total','What is authorized?','Item $10 + delivery $2 = total $12','Check the full total and any recurring terms.'),('Terms','What happens next?','Delivery + refund information','Read the conditions before authorizing a real payment. This example cannot pay.')]),
(4,18):('receipt','Look beyond “free download”',[
 ('Download','Installation costs $0','Optional features may cost money','A free download does not make every feature free.'),('Extras','Three fictional $2 extras','3 × $2 = $6','Small purchases can accumulate.'),('Controls','Review purchase settings','Purchase controls + receipts','Use the settings and records to understand spending. Do not buy during practice.')]),
(5,3):('workstation','Adjust the setup to the person',[
 ('Screen','Read without leaning in','Screen placement + comfortable text','Adjust the display to your needs.'),('Input','Support a comfortable position','Keyboard and pointing device within reach','Adjust input devices and posture.'),('Break','Pause the task','Take a break and change position','Ask for help with persistent discomfort.')]),
(5,4):('accessibility','One feature, several useful situations',[
 ('Captions','Read the speech','Video → accurate text','Captions help in quiet rooms and when speech is hard to hear.'),('Keyboard','Reach every control','Tab → focus → activate','Keyboard access helps people who cannot use a mouse.'),('Readable controls','Understand the next action','Clear label + visible state','Flexible input and readable controls make tools usable in more situations.')]),
(5,5):('attention','Choose what gets your attention',[
 ('Alerts','Which interruptions matter?','Keep needed alerts / reduce distractions','Adjust notifications to support the current task.'),('FOMO','Fear of missing out','A feeling of pressure to keep checking','Notice the pressure rather than letting it decide the next action.'),('Stopping point','Choose when to finish','Complete one task → step away','Set a stopping point that works for you.')]),
(5,6):('identity','Trust needs independent evidence',[
 ('Profile','A convincing identity','Name + photo + story','An online identity can be invented.'),('Pressure','Money, secrecy or personal information','Urgent request → pause','Pressure is a reason to stop and verify.'),('Verify','Use another trusted route','Known contact → independent confirmation','Do not let the supplied story be its own proof.')]),
(5,7):('community','Choose a response that reduces harm',[
 ('Pause','Do not escalate','Stop before replying','A rapid public reply can make a conflict worse.'),('Record','Keep evidence when safe','Record the relevant message','Preserve useful evidence without increasing your risk.'),('Support','Report, block or seek help','Platform tools + trusted support','Use the available tools and seek support when needed.')]),
(5,11):('lock','Check which action needs a password',[
 ('Open','Password needed to read','Closed file → password → content','A password-to-open setting controls access to readable content.'),('Edit','Password needed to change','Readable file → editing restricted','A password-to-edit setting can protect a different action.'),('Recovery','Plan for access later','Recovery method stored separately','Check recovery and do not store the password beside the protected file.')]),
(5,12):('device','An unknown drive is not a mystery to solve',[
 ('Found','An unfamiliar USB drive','Unknown device → unknown contents','Portable storage may contain malicious software.'),('Pause','Do not plug it in','Keep it disconnected','Do not connect it just to identify the owner.'),('Procedure','Use the lab’s process','Approved device / staff guidance','Follow the organization’s procedure for unknown media.')]),
(6,3):('network','Compare three kinds of digital product',[
 ('Website','Presents pages','Visitor → information','A website can primarily present content.'),('Web app','Responds to a task','Input → behavior → result','A web app supports interactive tasks.'),('SaaS','An ongoing software service','Users + service + maintenance','A real service may need accounts, shared storage, support and ongoing maintenance.')]),
(6,4):('build','Direct the work, then judge it',[
 ('Describe','State the desired result','Find a fictional community resource','Explain the task in ordinary language.'),('Generate','AI produces proposed code','Prompt → proposed implementation','The output needs inspection, not automatic trust.'),('Test','Compare behavior with the goal','Expected result ↔ observed result','You remain responsible for the delivered result.')]),
(6,8):('code','Ask for an explanation you can check',[
 ('Data','Where are the records?','Fictional resources → JavaScript array','Locate the data in the actual file.'),('Files','What does each part do?','HTML / CSS / JavaScript','Compare the explanation with the code and behavior.'),('Checks','How would I test this?','Search + keyboard + no results','Run the checks yourself; an explanation is a claim.')]),
(6,10):('code','Make a small local edit',[
 ('Copy','Preserve the starting file','resource-finder-v1.html → working copy','Keep an unchanged version before editing.'),('Edit','Change the heading and one record','Plain-text editor → saved HTML','Use the worksheet’s exact edit steps.'),('Open','Try your changed file','Browser → inspect → test','No AI account is needed to edit and run the supplied file.')]),
(6,11):('revision','Keep a route back',[
 ('Save','Keep version 1','v1 → small proposed change','Start from a saved working version.'),('Compare','Inspect the difference','What changed? What stayed?','Check that the revision matches the request.'),('Retest','Run the same requirements','Pass → keep / fail → restore v1','Restore the working copy if the change breaks a requirement.')]),
(6,12):('focus','Make the revision measurable',[
 ('Problem','Keyboard focus is hard to see','The filter works with a mouse','Name the specific observed problem.'),('Request','Add a visible focus outline','Tab → clearly outlined control','Specify a behavior you can test.'),('Preserve','Keep existing search behavior','Same fictional data + same search','Name what must continue to work, then retest it.')]),
(6,13):('storage','Locate the data before making promises',[
 ('Page array','Ships with the page','HTML / JavaScript → bundled records','Anyone who receives the page can inspect bundled data.'),('Browser storage','Belongs to this browser','This browser → local saved state','It can be cleared and does not provide shared cross-device records.'),('Database','Shared service behind access rules','Authorized devices → shared data','A shared database needs access controls.')]),
(6,14):('code','Assume browser code is visible',[
 ('Inspect','A visitor can inspect the files','HTML + JavaScript + bundled data','Do not treat shipped code as a hiding place.'),('Exclude','Keep secrets out','No private keys, passwords or records','Never include private secrets in this browser prototype.'),('Practice','Use fictional data','Community Library / Learning Desk','Fictional examples let you test without collecting personal data.')]),
(6,15):('lock','A sign-in picture is not a security boundary',[
 ('Screen','A login-looking form','Username + password fields','The appearance of a form does not protect data.'),('Rules','Authorize access at the server','Identity → access check → allowed data','Real accounts require tested server-side authorization.'),('Prototype','Explain the limitation','Local demonstration only','Do not claim the prototype safely manages real accounts.')]),
(6,18):('bug','Describe a bug someone can reproduce',[
 ('Steps','Search for LIBRARY','Open app → type LIBRARY','List the actions that produce the problem.'),('Expected','Find Community Library','Expected: matching resource','State the intended behavior clearly.'),('Actual','No matching result','Observed: empty result','Ask for a focused fix; repeat this test and a previously passing test.')]),
(6,19):('network','Separate local practice from a launch',[
 ('Local','Runs on your computer','Saved HTML → your browser','A local file is not automatically a hosted service.'),('Hosted','Reachable online','Hosting → visitors','Hosting changes who can reach the work.'),('Maintain','Assign real responsibilities','Rights · access · data · costs · backups','Review ownership and maintenance before a real launch.')]),
}

def icon(kind):
 paths={
 'search':'<circle cx="27" cy="26" r="17"/><path d="m40 39 17 17"/>',
 'network':'<rect x="3" y="22" width="18" height="22" rx="2"/><rect x="43" y="22" width="18" height="22" rx="2"/><path d="M21 33h22m-17-6 6 6-6 6"/>',
 'lock':'<rect x="12" y="27" width="40" height="31" rx="4"/><path d="M21 27V17a11 11 0 0 1 22 0v10m-11 12v8"/>',
 'email':'<rect x="5" y="12" width="54" height="40" rx="3"/><path d="m6 15 26 20 26-20"/>',
 'calendar':'<rect x="7" y="12" width="50" height="45" rx="3"/><path d="M7 25h50M20 5v14M44 5v14M19 36h8m10 0h8M19 46h8"/>',
 'keyboard':'<rect x="3" y="16" width="58" height="32" rx="3"/><path d="M11 25h5m6 0h5m6 0h5m6 0h8M11 34h5m6 0h5m6 0h5m6 0h8M20 42h24"/>',
 'document':'<path d="M13 5h27l12 12v42H13zM40 5v14h12M22 29h21M22 39h21M22 49h14"/>',
 'computer':'<rect x="5" y="6" width="54" height="37" rx="3"/><path d="M32 43v13M18 57h28M13 15h21m-21 9h36m-36 9h25"/>',
 'chart':'<path d="M6 6v51h53M16 45V28h9v17m9 0V13h9v32m9 0V35h8v10"/>',
 'files':'<path d="M5 15h21l6 8h27v33H5zM11 15V8h28l7 8"/>',
 'conversation':'<path d="M5 7h43v31H24L11 49V38H5zM48 20h11v34H42l-8 7v-7H24V38"/>',
 }
 alias={'browser':'computer','printer':'document','automation':'network','support':'conversation','source':'search','form':'document','archive':'files','revision':'document','cells':'chart','storyboard':'document','license':'document','export':'files','identity':'computer','community':'conversation','roles':'network','receipt':'document','workstation':'computer','accessibility':'keyboard','attention':'calendar','device':'computer','build':'network','code':'computer','focus':'keyboard','storage':'files','bug':'search'}
 return '<svg class="scene-icon" viewBox="0 0 64 64" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">'+paths.get(alias.get(kind,kind),paths['document'])+'</svg>'

def artifact(kind,text,index):
 if kind=='cells':
  rows=[('1','Item','Cost ($)'),('2','Paper','12'),('3','Folders','8'),('4','Pens','5')]
  return '<table class="cell-map"><caption>Fictional supply workbook</caption><thead><tr><th></th><th scope="col">A</th><th scope="col">B</th></tr></thead><tbody>'+''.join('<tr>'+''.join(f'<{ "th" if c==0 else "td"} class="{ "cell-selected" if (index==0 and c==2) or (index==1 and r==1) or (index==2 and r==1 and c==2) else ""}">{E(value)}</{ "th" if c==0 else "td"}>' for c,value in enumerate(row))+'</tr>' for r,row in enumerate(rows))+'</tbody></table><div class="artifact-caption">'+E(text)+'</div>'
 if kind=='email':
  fields=[('To','Alex'),('Cc','Sam' if index==1 else '—'),('Bcc','Pat' if index==2 else '—')]
  return '<dl class="recipient-fields">'+''.join(f'<div class="{ "field-selected" if i==index else ""}"><dt>{label}</dt><dd>{value}</dd></div>' for i,(label,value) in enumerate(fields))+'</dl>'
 if '→' in text:
  return '<div class="flow-map">'+'<span class="flow-connector" aria-hidden="true">→</span>'.join('<span class="flow-node">'+E(part.strip())+'</span>' for part in text.split('→'))+'</div>'
 if kind=='search':return '<div class="search-example">'+icon('search')+'<span>'+E(text)+'</span></div>'
 return E(text)

def concept(n,i):
 if (n,i) not in SCENES:return ''
 kind,title,choices=SCENES[n,i]
 buttons=''.join(f'<button type="button" data-scene-choice="{j}" aria-pressed="{str(j==0).lower()}">{E(x[0])}</button>' for j,x in enumerate(choices))
 panels=''.join(f'<div class="scene-state" data-scene-state="{j}" {"hidden" if j else ""}><div class="scene-artifact">{icon(kind)}<h4>{E(x[1])}</h4><div class="artifact-content">{artifact(kind,x[2],j)}</div></div><p class="scene-consequence">{E(x[3])}</p></div>' for j,x in enumerate(choices))
 image={1:'workstation',2:'research',3:'creation',4:'collaboration',5:'security',6:'building'}[n]
 return f'<div class="topic-scene scene-{kind}" data-topic-scene><h3>{E(title)}</h3><div class="scene-choices" role="group" aria-label="Explore this example">{buttons}</div><div class="scene-body"><img class="scene-illustration" src="/courses/digital-literacy-2/assets/illustrations/slide-{image}.webp" alt="" width="1536" height="1024" loading="lazy"><div class="scene-stage" aria-live="polite">{panels}</div></div><span class="scene-label">Illustrative example · select a choice to explore</span></div>'

def chart():
 return '''<div class="topic-scene chart-lab" data-chart-lab><h3>Which supply costs the most?</h3><div class="scene-choices"><button type="button" data-chart="cost" aria-pressed="true">Compare costs</button><button type="button" data-chart="sorted" aria-pressed="false">Lowest cost first</button><button type="button" data-chart="changed" aria-pressed="false">Paper becomes $15</button></div><figure><figcaption>Fictional supply costs ($)</figcaption><div class="bar-chart" role="img" aria-label="Paper 12 dollars, Folders 8 dollars, Pens 5 dollars"><div class="bar-row" data-item="Paper"><strong>Paper</strong><div class="bar-track"><span style="width:80%"></span></div><b>$12</b></div><div class="bar-row" data-item="Folders"><strong>Folders</strong><div class="bar-track"><span style="width:53.33%"></span></div><b>$8</b></div><div class="bar-row" data-item="Pens"><strong>Pens</strong><div class="bar-track"><span style="width:33.33%"></span></div><b>$5</b></div></div></figure><p data-chart-insight role="status">Paper costs the most: $12. Compare bar lengths from the same zero baseline.</p><table class="chart-data"><caption>The same information as a data table</caption><thead><tr><th scope="col">Item</th><th scope="col">Cost ($)</th></tr></thead><tbody><tr><th scope="row">Paper</th><td data-chart-paper>12</td></tr><tr><th scope="row">Folders</th><td>8</td></tr><tr><th scope="row">Pens</th><td>5</td></tr></tbody></table></div>'''

def crop():
 return '''<div class="topic-scene crop-lab" data-crop-lab><h3>Same original. Different edits.</h3><div class="scene-choices"><button type="button" data-crop="original" aria-pressed="true">Original</button><button type="button" data-crop="crop" aria-pressed="false">Crop the edges</button><button type="button" data-crop="resize" aria-pressed="false">Resize proportionally</button></div><div class="image-edit-stage"><div class="image-edit-frame"><img src="/courses/digital-literacy-2/assets/community-resource.svg" alt="Original practice artwork: community resource information" width="900" height="500"></div></div><p data-crop-note role="status">The original stays available. Save an edited copy under a different name.</p></div>'''

def trim():
 return '''<div class="topic-scene trim-lab" data-trim-lab><h3>Edit a fictional 20-second clip</h3><div class="scene-choices"><button type="button" data-trim="original" aria-pressed="true">Original clip</button><button type="button" data-trim="trim" aria-pressed="false">Trim the start and end</button><button type="button" data-trim="split" aria-pressed="false">Remove a middle section</button></div><div class="clip-track" aria-label="Original clip: start, explanation, pause, final step, end"><span data-clip="edge">Start<br>0–3s</span><span>Explain<br>3–9s</span><span data-clip="middle">Pause<br>9–12s</span><span>Next step<br>12–17s</span><span data-clip="edge">End<br>17–20s</span></div><p data-trim-note role="status">Original duration: 20 seconds. Choose an edit and compare what remains.</p><div class="caption-strip">Caption check: “Choose one task. Ask at the learning desk.”</div><p>After editing, check speech volume, caption timing and the exported result.</p></div>'''

def feature(n,i):
 return {(3,11):chart,(3,13):crop,(3,14):trim}.get((n,i),lambda:concept(n,i))()

def supporting(s,n):
 """Illustrated discussion, activity and reflection surfaces without duplicated lesson copy."""
 kind=s['kind'];image={1:'workstation',2:'research',3:'creation',4:'collaboration',5:'security',6:'building'}[n]
 if kind in ['discussion','lab','summary','complete','assessment']:
  return f'<div class="slide-topic-art"><img src="/courses/digital-literacy-2/assets/illustrations/slide-{image}.webp" alt="" width="1536" height="1024" loading="lazy"></div>'
 return ''
