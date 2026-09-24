"""Photographic context and authored teaching surfaces; no external services or records."""
from html import escape as E

PHOTO_ROOT='/courses/digital-literacy-2/assets/photos/'
# Explicit placement prevents a week-wide decorative image from invading a demonstration.
PHOTOS={
 1:{1:'workstation',2:'workstation',11:'workstation',18:'workstation',22:'workstation'},
 2:{1:'library',2:'library',14:'library',21:'library'},
 3:{1:'resource-pack',2:'resource-pack',15:'resource-pack',21:'resource-pack'},
 4:{1:'collaboration',2:'collaboration',8:'collaboration',14:'workstation',15:'collaboration'},
 5:{1:'safety',2:'safety',3:'workstation',8:'safety',9:'usb',12:'usb',14:'safety',20:'safety'},
 6:{1:'app-planning',2:'app-planning',16:'app-planning',22:'collaboration',24:'collaboration'}
}
PURPOSE={1:'Make a familiar task easier',2:'Find useful help in your community',3:'Create something a neighbor can use',4:'Plan together and leave a clear next step',5:'Pause, verify and protect your work',6:'Turn a small local problem into a working app'}
EVIDENCE={
 1:[('Choose','One setting for your task'),('Test','Read, hear or find the result'),('Restore','Keep a way back')],
 2:[('Source','Organization + evidence'),('Folder','A name you can find'),('Access','The right role + recovery')],
 3:[('Handout','A clear next action'),('Workbook','A total that recalculates'),('Export','Open and inspect the saved copy')],
 4:[('Request','Who does what, and when?'),('Review','A specific change + a reason'),('Decision','One agreed shared copy')],
 5:[('Evidence','What can you confirm?'),('Protection','Access that matches the task'),('Practice','Choose one skill to repeat')],
 6:[('Saved app','A working recoverable copy'),('Test log','Expected result ↔ observed result'),('Limitation','Local prototype, fictional data')]
}

def photo(n,i,compact=False):
 name=PHOTOS.get(n,{}).get(i)
 if not name:return ''
 overlay=''
 if name=='safety':
  overlay='<svg class="photo-screen-overlay" viewBox="0 0 1376 768" aria-hidden="true"><polygon points="284,352 365,333 446,543 350,570" fill="#173657"/><g transform="translate(320 410) rotate(-17)"><rect width="61" height="43" rx="3" fill="#e1efed"/><path d="m0 3 30 24L61 3" fill="none" stroke="#173657" stroke-width="3"/><path d="M2 62h59M2 76h41" stroke="#e1efed" stroke-width="5"/></g><polygon points="790,162 1138,188 1112,412 766,373" fill="#e1efed"/><path d="m800 188 326 24" stroke="#173657" stroke-width="18"/><g fill="#173657"><circle cx="831" cy="253" r="12"/><circle cx="826" cy="311" r="12"/></g><g stroke="#173657" stroke-width="8"><path d="m862 254 189 14M857 312l189 14"/></g></svg>'
 return f'<figure class="scenario-photo photo-{name} {"photo-compact" if compact else ""}"><div class="photo-frame"><img src="{PHOTO_ROOT}{name}.webp" width="1376" height="768" alt="" loading="lazy">{overlay}</div><figcaption>Illustrative West Virginia scenario · fictional people and setting</figcaption></figure>'

def sequence(items):
 return '<ol class="evidence-sequence">'+''.join(f'<li><strong>{E(title)}</strong><span>{E(detail)}</span></li>' for title,detail in items)+'</ol>'

def evidence_board(n):
 symbols={1:['screen','calendar','check'],2:['file','folder','person'],3:['file','file','check'],4:['message','file','check'],5:['message','file','check'],6:['screen','check','file']}[n]
 return '<div class="evidence-board">'+''.join('<figure>'+mini_icon(symbol)+'<figcaption><strong>'+E(title)+'</strong><span>'+E(detail)+'</span></figcaption></figure>' for symbol,(title,detail) in zip(symbols,EVIDENCE[n]))+'</div>'

def supporting(s,n,i):
 if s['kind'] in ['summary','complete','lab']:
  return photo(n,i,True)+evidence_board(n)
 if s['kind']=='assessment':return sequence([('Take','Complete your own assessment'),('Review','Use feedback to choose practice'),('Save','Print or save your results')])
 if s['kind']=='discussion':return photo(n,i)+sequence(EVIDENCE[n][:2])
 return ''

def field(label,value,active=False):
 return f'<div class="visual-field {"visual-selected" if active else ""}"><strong>{E(label)}</strong><span>{E(value)}</span></div>'

def panel(title,body):return f'<div class="authored-window"><div class="authored-title">{E(title)}</div><div class="authored-content">{body}</div></div>'
def mini_icon(kind):
 paths={
 'file':'<path d="M12 4h22l10 10v38H12zM34 4v12h10M19 25h18M19 33h18M19 41h12"/>',
 'folder':'<path d="M4 15h19l6 7h23v29H4zM4 15V8h18l7 7h23v7"/>',
 'screen':'<rect x="4" y="6" width="48" height="32" rx="3"/><path d="M28 38v12M16 51h24"/>',
 'message':'<rect x="4" y="9" width="48" height="36" rx="3"/><path d="m4 12 24 19 24-19"/>',
 'person':'<circle cx="28" cy="15" r="10"/><path d="M8 52v-8a20 20 0 0 1 40 0v8"/>',
 'check':'<path d="m9 29 12 12L47 13"/>',
 'cloud':'<path d="M15 44a12 12 0 0 1-2-24 16 16 0 0 1 31 0 12 12 0 0 1-1 24z"/>',
 'calendar':'<rect x="5" y="10" width="46" height="42" rx="3"/><path d="M5 23h46M16 4v13M40 4v13M14 33h7m10 0h10M14 42h7"/>'}
 return '<svg class="teaching-symbol" viewBox="0 0 56 56" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">'+paths.get(kind,paths['file'])+'</svg>'

def visual_record(title,rows,index):
 if 'event' in title:
  return '<div class="event-layout"><div class="calendar-sheet"><strong>Monday</strong><div>1 p.m.</div><div class="calendar-event">Library practice<br>2–3 p.m.<br>Room A</div><div>3 p.m.</div></div><div>'+''.join(field(k,v,j==index) for j,(k,v) in enumerate(rows))+'</div></div>'
 if 'Draft only' in title:
  return '<div class="mail-draft"><div class="recipient-chips"><span>To: Alex</span></div><h4>Review the computer-help handout</h4><p>Please comment on whether the contact section is clear before our next practice session.</p><div class="attachment">'+mini_icon('file')+'computer-help-handout-v1.docx</div>'+field('Reviewing',rows[index][0]+' — '+rows[index][1],True)+'</div>'
 if 'Recipient visibility' in title:
  return '<div class="recipient-board">'+''.join('<div>'+mini_icon('person')+'<strong>'+E(k)+'</strong><span>'+E(v)+'</span></div>' for k,v in rows[:3])+'</div>'+field(*rows[3],True)
 if any(x in title for x in ['Resources /','destination','Saved work','Recovery result','Trash preview','Version history','Preserve the original','Starter files','Open the export']):
  return '<div class="file-browser"><div class="folder-trail">'+mini_icon('folder')+'Resources / practice</div>'+''.join('<div class="file-row '+('visual-selected' if j==index else '')+'">'+mini_icon('file')+'<div><strong>'+E(k)+'</strong><span>'+E(v)+'</span></div></div>' for j,(k,v) in enumerate(rows))+'</div>'
 if 'checkout' in title:
  return '<div class="checkout-receipt"><p>Practice Learning Store</p><div><span>Item</span><strong>$10</strong></div><div><span>Delivery</span><strong>$2</strong></div><div class="receipt-total"><span>Total</span><strong>$12</strong></div>'+field(*rows[index],True)+'<p>No payment is possible in this practice.</p></div>'
 if 'app receipt' in title:
  return '<div class="checkout-receipt"><div><span>Installation</span><strong>$0</strong></div><div><span>Extra 1</span><strong>$2</strong></div><div><span>Extra 2</span><strong>$2</strong></div><div><span>Extra 3</span><strong>$2</strong></div><div class="receipt-total"><span>Extras total</span><strong>$6</strong></div>'+field(*rows[index],True)+'</div>'
 if 'shared file' in title.lower() or 'shared handout' in title.lower():
  return '<div class="shared-file">'+mini_icon('file')+'<strong>One agreed copy</strong></div><div class="role-network">'+''.join('<div class="'+('visual-selected' if j==index else '')+'">'+mini_icon('person')+'<strong>'+E(k)+'</strong><span>'+E(v)+'</span></div>' for j,(k,v) in enumerate(rows))+'</div>'
 if title in ['This device','Provider','Second device','Data boundary','A separate launch decision','Software as a service']:
  return '<div class="boundary-map">'+''.join('<section class="boundary-zone '+('visual-selected' if j==index else '')+'">'+mini_icon('cloud' if j==2 or title=='Provider' else 'screen')+'<h4>'+E(k)+'</h4><p>'+E(v)+'</p></section>' for j,(k,v) in enumerate(rows))+'</div>'
 if 'search' in title.lower():
  return '<div class="fictional-searchbar">'+E(rows[0][1])+'</div>'+''.join('<div class="search-result"><h4>'+E(k)+'</h4><p>'+E(v)+'</p></div>' for k,v in rows[1:])
 if 'source note' in title.lower() or 'service page' in title.lower() or 'service lead' in title.lower() or 'verification note' in title.lower():
  return '<div class="source-page"><h4>Community computer help</h4><div class="source-page-lines" aria-hidden="true"></div>'+''.join(field(k,v,j==index) for j,(k,v) in enumerate(rows))+'</div>'
 return ''.join(field(k,v,j==index) for j,(k,v) in enumerate(rows))

def fields(title,rows,index=0):
 return panel(title,visual_record(title,rows,index))
def document(title,body):return panel('Fictional handout',f'<h4>{E(title)}</h4>'+body)
def flow(items):return sequence([(str(i+1),x) for i,x in enumerate(items)])

def artifact(n,i,j):
 """Return a topic-specific authored artifact for the current user-selected state."""
 if (n,i)==(1,8):
  return [fields('Browser settings',[('Home page','Community learning resources'),('Startup','Open the home page')]),fields('Download destination',[('Folder','Resources'),('Test file','resource-guide.pdf')]),fields('Site permissions',[('Text resource page','Camera blocked'),('Reason','No camera needed to read')])][j]
 if (n,i)==(1,9):
  return [flow(['Instruction: open a file','Processor carries out instructions','File appears in the app']),fields('Current work',[('Memory','Open document and unsaved changes'),('Close app','Unsaved changes can be lost')]),fields('Saved work',[('Storage','resource-guide.docx'),('Close and reopen','Saved file remains')]),fields('Connection check',[('Port shape','Match the connector'),('Capability','Check supported data, video and power')])][j]
 if (n,i)==(1,11):return [flow(['Document','Toner','Printed page']),flow(['Document','Liquid ink','Printed page']),fields('Print destination',[('Selected printer','Training room'),('Before sending','Check the destination')])][j]
 if (n,i)==(1,13):return fields('Library practice · fictional event',[('When','Monday · 2:00–3:00 p.m.'),('Where','Room A'),('Reminder','30 minutes before')],j)
 if (n,i)==(1,16):return [fields('Check the correction',[('Typed name','Maren'),('Autocorrect','Marine — wrong name'),('Recovery','Undo → Maren')],1),fields('Suggestion preview',[('Typed','Please meet at the'),('Suggested','learning desk'),('Your decision','Accept only if this is your meaning')],1),fields('Mail rule test',[('Matches','Subject contains Practice'),('Destination','Practice folder'),('Check','One test message arrived')],2)][j]
 if (n,i)==(1,17):return [fields('This device',[('Account','Training'),('Save status','Saving…')]),fields('Provider',[('Saved file','resource-guide.docx'),('Save status','Saved')]),fields('Second device',[('Connection','Offline'),('Next action','Reconnect and verify the latest copy')])][j]
 if (n,i)==(1,19):return fields('Help request · app version: practice',[('Task','Print one page'),('Already tried','Selected training-room printer'),('Exact message','Printer unavailable')],j)
 if (n,i)==(2,3):return fields('Fictional search results',[('Query',['help','public library computer help','public library computer help [your town]'][j]),('Result focus',['Many unrelated services','Library computer-help services','Local service: confirm place and contact'][j])])
 if (n,i)==(2,4):return [fields('Phrase filter',[('Exact phrase','“computer help”'),('Hidden alternative','Digital skills support'),('Try next','Remove quotes to compare')]),fields('Domain filter',[('Scope','example.org only'),('Still check','Evidence and task fit')]),fields('Date filter',[('Scope','Recent pages only'),('Still check','Details on the source page')])][j]
 if (n,i)==(2,7):return fields('Service lead · fictional',[('Place',['Another state','Your town','Your town'][j]),('Currency',['Current','New announcement','Current details'][j]),('Evidence',['Correct but not local','Needs confirmation','Organization + contact'][j])],j)
 if (n,i)==(2,8):return fields('My source note',[('Title / organization','Computer-help service / Community Library'),('Address / checked','example.org/help / today'),('Words used','Quote: “Computer help” · Summary: help with a task')],j)
 if (n,i)==(2,9):return fields('Practice help request',[('Collector / purpose','Learning team / arrange computer help'),('Required / optional','Help topic / extra detail'),('Review','Finding a file · desk visit · fictional data')],j)
 if (n,i)==(2,11):return fields('Resources / fictional files',[('Name',['final-final-new.docx','library-resource-v1.docx','Resources / library-resource-v1.docx'][j]),('What this tells you',['Unclear subject and version','Subject + version','Folder + subject + version'][j])])
 if (n,i)==(2,12):return fields('One shared file',[('Owner','Alex — controls access'),('Partner','Sam — commenter'),('Common copy','Resources / library-resource-v1.docx')],j)
 if (n,i)==(2,16):return fields('File protection',[('Readable',['Yes','Protected content: key required','Inspect password setting'][j]),('Editable',['No','Only after authorized access','Open and edit are different actions'][j])])
 if (n,i)==(2,17):
  files='<div class="file-objects"><div>'+mini_icon('file')+'<strong>handout.docx</strong></div><div>'+mini_icon('file')+'<strong>budget.csv</strong></div></div>'
  archive='<div class="archive-object">'+mini_icon('folder')+'<strong>resources.zip</strong><span>Packaged files</span></div>'
  return panel('Pack and extract', [files+'<p class="object-arrow">Package ↓</p>'+archive,archive+'<p class="object-arrow">Extract ↓</p>'+files,archive+field('Protection','ZIP alone does not promise encryption. Compressed media may not shrink.',True)][j])
 if (n,i)==(3,4):return fields('Practice editor',[('Keys',['Ctrl / Command + C','Ctrl / Command + V','Ctrl / Command + Z','Ctrl / Command + S'][j]),('Before',['Selected: learning desk','Cursor after: Visit the','Unwanted wording','Unsaved document'][j]),('After',['Clipboard: learning desk','Visit the learning desk','Original wording restored','Resources / handout.docx'][j])],2)
 if (n,i)==(3,5):return document(['Help is available','Computer help at the learning desk'][j],'<p>'+['Contact someone for more information.','Bring one computer question to the learning desk.'][j]+'</p>')
 if (n,i)==(3,6):return document('Review the proposed change',['<p><del>Contact us</del> <ins>Visit the learning desk</ins></p><p>Pending author decision</p>','<p>Visit the learning desk</p><p>Accepted into document</p>','<p>Contact us</p><p>Original retained · proposed edit rejected</p>'][j])
 if (n,i)==(3,7):return [fields('Document outline',[('Heading style','Computer help'),('Navigation entry','Computer help → Steps')]),document('Find help','<p class="meaningful-link">Read the computer-help guide</p><p>Destination is named in the link.</p>'),fields('Image description',[('Informative image','Describe the useful information'),('Decorative image','Empty alternative text'),('Never depend on','Color alone')])][j]
 if (n,i)==(3,12):
  return '<div class="storyboard-previews">'+''.join('<article class="'+('visual-selected' if k==j else '')+'"><span>Slide '+str(k+1)+'</span><h4>'+title+'</h4>'+body+'</article>' for k,(title,body) in enumerate([('Need computer help?', '<img src="'+PHOTO_ROOT+'resource-pack.webp" width="1376" height="768" alt="" loading="lazy">'),('Choose a task', '<ol><li>Bring a question.</li><li>Visit the learning desk.</li></ol>'),('Your next step', '<p>Bring your question to the learning desk.</p>')]))+'</div>'
 if (n,i)==(3,16):return fields('Illustrative license record',[('Find','Visible in search — permission unknown'),('Check','Allowed use and license conditions'),('Credit','Creator · title · source · license')],j)
 if (n,i)==(3,18):return [fields('Open the export',[('File','resource-guide.pdf'),('Application','Separate exported-file preview')]),fields('Inspect actual output',[('Page break','Heading stays with its steps'),('Link','Destination opens correctly'),('Image','Useful content is present')]),fields('Saved destination',[('Folder','Resources'),('Filename','resource-guide.pdf')])][j]
 if (n,i)==(4,3):return fields('Check before posting',[('Active account','Training · fictional profile'),('Tone','Clear request to a partner'),('Protection','Separate credentials + MFA where available')],j)
 if (n,i)==(4,5):return fields('Recipient visibility',[('Main recipient','Alex'),('Visible copy','Sam' if j==1 else 'None'),('Hidden copy','Pat' if j==2 else 'None'),('Alex sees','Alex and Sam' if j==1 else 'Alex; hidden-list addresses are not shown')],j)
 if (n,i)==(4,6):return fields('Message timing',[('Reply by','Before the next practice session'),('Recipient context','Check working hours and urgency'),('Schedule preview','Chosen time + recipient + reviewed wording')],j)
 if (n,i)==(4,7):return document('Make the request understandable','<p>'+['Use the name and form of address the person prefers.','Multifactor authentication (MFA) adds another check when signing in.','Which way of reviewing this works for you?'][j]+'</p>')
 if (n,i)==(4,8):return fields('Fictional community discussion',[('Before posting','Read the purpose and rules'),('Respectful response','I see a different option because…'),('Before sharing a story','Ask permission; share only what was agreed')],j)
 if (n,i)==(4,9):return fields('Service verification note',[('Directory lead','Computer-help session — needs confirmation'),('Official contact','Verify eligibility, availability and hours'),('Usable next step','Record contact method + requirements')],j)
 if (n,i)==(4,10):return fields('One shared handout',[('Owner','Coordinates final decision and access'),('Writer','Edits the agreed copy'),('Reviewer','Comments with location, change and reason')],j)
 if (n,i)==(4,13):return fields('Anchored comment: contact section',[('Read','Add the contact number after the steps.'),('Respond','Added after steps so readers can find help.'),('Resolve','Decision recorded; version history remains available')],j)
 if (n,i)==(4,16):return [panel('Good',field('Physical product','A keyboard')),panel('Service',field('Work provided','Computer support session')),fields('Subscription',[('Access','Ongoing software or media access'),('Renewal','Continues under its terms until canceled')])][j]
 if (n,i)==(4,17):return fields('Practice checkout · cannot pay',[('Seller','Practice Learning Store'),('Total','Item $10 + delivery $2 = $12'),('Terms','Review delivery, refund and recurring charges')],j)
 if (n,i)==(4,18):return fields('Fictional app receipt',[('Download','$0 installation'),('Extras','$2 + $2 + $2 = $6'),('Controls','Review purchase settings and receipts')],j)
 if (n,i)==(5,3):return fields('Adapt the setup to yourself',[('Screen','Readable without leaning in'),('Input','Keyboard and pointer within reach'),('Break','Change position and pause the task')],j)
 if (n,i)==(5,4):return [panel('Captioned media','<div class="caption-strip">Choose one task. Ask at the learning desk.</div>'),panel('Keyboard route',flow(['Tab: Search','Tab: Filter','Enter: select action'])),fields('Readable control',[('Label','Search resources'),('Visible state','No matches — change your search')])][j]
 if (n,i)==(5,5):return fields('Attention settings',[('Notifications',['Needed alerts only','Pressure to keep checking','Task complete: step away'][j]),('Your choice','Keep the controls that support your task')])
 if (n,i)==(5,6):return fields('Fictional identity claim',[('Profile','Name + image + story are claims'),('Request','Urgent money, secrecy or personal details'),('Independent route','Confirm through a known trusted contact')],j)
 if (n,i)==(5,7):return fields('Fictional conversation controls',[('Pause','Do not escalate the exchange'),('Record','Preserve relevant evidence when safe'),('Support','Report · block · trusted support')],j)
 if (n,i)==(5,11):return fields('Choose the protected action',[('Open','A password is required to read'),('Edit','Content may be readable but changes restricted'),('Recovery','Keep recovery method separately')],j)
 if (n,i)==(5,12):return fields('Disconnected device',[('Found','Unfamiliar USB drive'),('Pause','Do not connect it'),('Procedure','Ask authorized lab staff')],j)
 if (n,i)==(6,3):return [fields('Resource website',[('Content','Community library · Learning'),('Purpose','Read information')]),fields('Resource web app',[('Search','library'),('Result','Community library · Learning')]),fields('Software as a service',[('Users','Ongoing hosted service'),('Responsibilities','Access · shared data · support · maintenance')])][j]
 if (n,i)==(6,4):return fields('Direct and inspect the build',[('Task','Find a fictional community resource'),('Proposed code','AI output requires review'),('Observed result','Compare behavior with your acceptance checks')],j)
 if (n,i)==(6,8):return [panel('Bundled fictional data','<pre>name: "Community library"\ncategory: "Learning"</pre>'),fields('Starter files',[('Open','resource-finder-v1.html'),('Inspect','HTML · CSS · JavaScript')]),fields('Test evidence',[('Query','LIBRARY'),('Expected','Community library'),('Observed','Compare with actual result')])][j]
 if (n,i)==(6,10):return [fields('Preserve the original',[('Original','resource-finder-v1.html'),('Working copy','resource-finder-v2.html')]),panel('One heading change','<pre><del>&lt;h1&gt;Find a resource&lt;/h1&gt;</del>\n<ins>&lt;h1&gt;Community resources&lt;/h1&gt;</ins></pre>'),fields('Open and test',[('File','resource-finder-v2.html'),('Heading','Community resources'),('Search','skills finds Community Skills Desk')])][j]
 if (n,i)==(6,11):return fields('One change, recoverable versions',[('Save','Keep resource-finder-v1.html'),('Compare','Only the heading changes in v2'),('Retest','Search still works; restore v1 if needed')],j)
 if (n,i)==(6,12):return panel('Visible keyboard focus',field('Observed problem','Focus is hard to see')+'<button type="button" class="focus-practice">Practice focus: press Tab</button>'+field('Repair requirement','A visible outline; search behavior preserved',j>0))
 if (n,i)==(6,13):return fields('Data boundary',[('Bundled file','Anyone with the file can inspect records'),('One browser','Local storage is not synchronized; can be cleared'),('Shared service','Requires access rules and authorized devices')],j)
 if (n,i)==(6,14):return panel('Safe practice source','<pre>name: "Community library"\ncategory: "Learning"</pre>'+field(['Inspect','Exclude','Practice'][j],['Bundled code and data are visible','No secrets or private records in browser code','Use fictional records only'][j],True))
 if (n,i)==(6,15):return fields('Screen versus security',[('Decorative form','A sign-in picture does not protect data'),('Server boundary','Identity → authorization → allowed data'),('This prototype','No real accounts or passwords collected')],j)
 if (n,i)==(6,18):return fields('Explicitly broken demonstration',[('Steps','Search for LIBRARY'),('Expected','Community library'),('Actual','No match — reproduce and repair the bug')],j)
 if (n,i)==(6,19):return fields('A separate launch decision',[('Local','Saved HTML on your own device'),('Hosted','Visitors can reach published files'),('Maintain','Ownership · rights · costs · access · backups')],j)
 return ''

def steps_demo(title,states):
 controls=''.join(f'<button type="button" data-scene-choice="{i}" aria-pressed="{str(i==0).lower()}">{E(label)}</button>' for i,(label,body) in enumerate(states))
 panels=''.join(f'<div class="scene-state" data-scene-state="{i}" {"hidden" if i else ""}>{body}</div>' for i,(label,body) in enumerate(states))
 return f'<div class="topic-scene authored-demo" data-topic-scene><h3>{E(title)}</h3><div class="scene-choices">{controls}</div><div aria-live="polite">{panels}</div><p class="scene-label">Fictional local simulation · nothing is sent or changed on your device</p></div>'

def special(n,i):
 if (n,i)==(4,4):return steps_demo('Build an actionable email draft',[(label,fields('Draft only · no message is sent',[('To','Alex · practice partner'),('Subject','Review the computer-help handout'),('Request','Please comment on whether the contact section is clear.'),('When','Before our next practice session'),('Attachment','computer-help-handout-v1.docx')],j)) for j,label in enumerate(['Recipient','Subject','Request','Response time','Attachment'])])
 if (n,i)==(2,18):return steps_demo('Choose the right recovery route',[
  ('Missing file',fields('Trash preview',[('File','resource-guide.docx'),('State','Deleted · preview before restoring'),('Before restoring','Confirm this is the file you need')],1)),
  ('Wrong content',fields('Version history',[('Current version','Contact section missing'),('Earlier version','Contact section present'),('Before replacing','Coordinate with collaborators and preview')],1)),
  ('Restore checked copy',fields('Recovery result',[('File','resource-guide.docx'),('Verification','Open and check useful content'),('Shared work','Confirm the restored version with partners')],1))])
 if (n,i)==(1,12):
  states=[]
  checks=['Confirm the training-room printer is the intended destination.','Select page 1 so the test uses only one sheet.','Inspect all page edges; change orientation if useful content is clipped.','Keep copies at 1 for the first test.','Inspect the single printed test before authorizing the remaining pages.']
  for j,(label,value) in enumerate([('Printer','Training room'),('Page range','Page 1 only'),('Layout','Portrait · inspect all edges'),('Copies','1 test copy'),('Test copy','Inspect the printed result')]):
   page='<figure class="print-paper-preview"><svg viewBox="0 0 200 260" aria-hidden="true"><rect x="12" y="5" width="176" height="248" rx="3" fill="white" stroke="#173657" stroke-width="3"/><path d="M33 38h121M33 56h83M33 92h133M33 110h133M33 128h100M33 164h133M33 182h111M33 220h55" fill="none" stroke="#829bb0" stroke-width="7"/><rect x="27" y="25" width="147" height="211" fill="none" stroke="#0f655f" stroke-width="2" stroke-dasharray="6 4"/></svg><figcaption>Page 1 · content inside the print area</figcaption></figure>'
   body=panel('Practice print · no print job is sent','<div class="print-preview-layout">'+page+'<div>'+field(label,value,True)+field('Check this step',checks[j])+'</div></div>')
   states.append((label,body))
  return steps_demo('Inspect the print preview',states)

 return ''

def supplement(n,i):
 """Small explanatory views beside preserved functional course activities."""
 if (n,i)==(1,4):return flow(['Before: text is difficult to read','Change: page zoom to 125%','Check: text and next control are readable','Restore: page zoom to 100%'])
 if (n,i)==(1,5):return fields('Scope of page zoom',[('Browser controls','Stay at their usual size'),('Page content','Text and page controls grow')])
 if (n,i)==(1,6):return fields('Keyboard practice',[('Increase','Ctrl / Command + plus'),('Decrease','Ctrl / Command + minus'),('Reset','Ctrl / Command + zero')])
 if (n,i)==(1,7):return steps_demo('Check the screen too',[(label,panel('Illustrative display comparison',f'<svg class="display-sample display-{mode}" viewBox="0 0 640 180" role="img" aria-label="Illustrative {label} sample: Computer help, choose one task"><rect width="640" height="180" fill="white"/><text x="25" y="65" fill="{"#aaa" if mode=="low" else "#173657"}" font-size="40">Computer help</text><text x="25" y="125" fill="{"#aaa" if mode=="low" else "#173657"}" font-size="36">Choose one useful task.</text></svg>')+field('What to check',hint)) for label,mode,hint in [('Low contrast','low','Faint text is harder to distinguish.'),('Readable contrast','clear','Dark text and a light background separate clearly.'),('Brightness','bright','Adjust your actual screen for the room; this only models the comparison.')]])
 if (n,i)==(1,10):return panel('Connector shape and capability', '<div class="connector-profiles"><figure><svg viewBox="0 0 120 80" aria-hidden="true"><path d="M15 20h90l-10 40H25z"/><path d="M30 30h60v15H30z"/></svg><figcaption>HDMI · display</figcaption></figure><figure><svg viewBox="0 0 120 80" aria-hidden="true"><path d="M30 12h60v48H30zM45 60v10h30V60M39 20v18m9-18v18m9-18v18m9-18v18m9-18v18m9-18v18"/></svg><figcaption>Ethernet · wired network</figcaption></figure><figure><svg viewBox="0 0 120 80" aria-hidden="true"><rect x="15" y="10" width="90" height="24"/><rect x="15" y="48" width="90" height="24" rx="12"/></svg><figcaption>USB-A / USB-C · check supported features</figcaption></figure></div>')
 if (n,i)==(2,5):return steps_demo('Inspect evidence and fit',[
  ('Evidence',fields('Fictional service page',[('Responsible organization','Community Library'),('Evidence','Contact method and service description'),('Still verify','Confirm important details independently')],1)),
  ('Task fit',fields('Does this answer your question?',[('Place','Your community'),('Service','Computer help'),('Next step','Confirm availability and access needs')],0))])
 if (n,i)==(2,6):return fields('Two leads to compare',[('Document','Organization + service description + contact'),('Community post','Personal recommendation + claim'),('Your task','Inspect supporting evidence for both')])
 if (n,i)==(2,15):return steps_demo('Preview what a recipient can do',[(label,fields('Recipient preview · fictional',[('Role',label),('Available action',action),('Ownership','Remains with the owner')])) for label,action in [('Viewer','Read the content'),('Commenter','Read + propose a comment'),('Editor','Read + change content')]])
 if (n,i)==(3,3):return fields('Navigation outline',[('Heading','Computer help'),('Section','Steps'),('Meaning','Structure remains useful beyond visual bold text')])
 if (n,i)==(3,9):return panel('The same values in a worksheet','<table class="budget-evidence"><caption>Fictional supplies · cost in dollars</caption><thead><tr><th scope="col">Cell</th><th scope="col">Item</th><th scope="col">Cost ($)</th></tr></thead><tbody><tr><th scope="row">B2</th><td>Paper</td><td data-budget-paper>12.00</td></tr><tr><th scope="row">B3</th><td>Folders</td><td>8.00</td></tr><tr><th scope="row">B4</th><td>Pens</td><td>5.00</td></tr><tr><th scope="row">B5</th><td>Total</td><td data-budget-sum>25.00</td></tr></tbody></table><p>Formula in B5: <code>=SUM(B2:B4)</code></p>')
 if (n,i)==(3,10):return steps_demo('Compare a typed answer with a formula',[
  ('Typed total',fields('Wrong after paper changes',[('Paper','15'),('Typed total','25 — stale'),('Cause','A typed answer does not recalculate')],1)),
  ('Formula total',fields('Responsive total',[('Paper','15'),('Formula','=SUM(B2:B4)'),('Result','28 — correct after the change')],2))])
 if (n,i)==(3,17):return steps_demo('Look inside the exported result',[
  ('Editable',document('Computer help','<p>Editable heading and steps remain available in a compatible app.</p>')),
  ('PDF',document('Computer help','<ol><li>Choose a task.</li><li>Visit the learning desk.</li></ol><p>Reopen to inspect layout and reading order.</p>')),
  ('CSV',panel('Plain rows and columns','<pre>Item,Cost\nPaper,15\nFolders,8\nPens,5\nTotal,28</pre><p>No workbook formatting or live formula behavior.</p>'))])
 if (n,i)==(4,11):return panel('Same task, different schedules',flow(['Together: writer + reviewer edit now','Later: reviewer comments → writer responds → decision recorded']))
 if (n,i)==(4,14):return steps_demo('Prepare before joining',[
  ('Sound',fields('Practice device selection',[('Speaker','Choose intended output'),('Microphone','Choose intended input'),('Check','Use the actual app’s test controls')],2)),
  ('Captions',panel('Captioned meeting','<div class="caption-strip">Host: Let’s review the next step.</div><p>Turn on available captions when helpful.</p>')),
  ('Backup',fields('If the connection fails',[('Shared record','Read agreed notes afterward'),('Recording','Ask before recording others')]))])

 if (n,i)==(5,9):return photo(n,i,True)
 if (n,i)==(5,13):return fields('Compare the task',[('Video meeting','Camera may support participation'),('Text resource page','Reading does not need a camera')])
 if (n,i)==(5,19):return panel('Fictional practice report · not certification', '<div class="sample-score"><strong>Safety practice · 2 of 4</strong><div class="sample-score-track" aria-hidden="true"><span></span></div></div>'+flow(['Review: recognizing message pressure','Practice: use an independent contact route','Explain: what evidence supports your choice']))
 if (n,i)==(6,6):return fields('Observable acceptance checks',[('Match','library finds Community library'),('Keyboard','Tab reaches controls with a visible outline'),('Empty result','zzz shows a useful no-match message')])
 if (n,i)==(6,9):return fields('Working reference',[('Filename','resource-finder-v1.html'),('Test states','Match · no match · mixed case')])
 if (n,i)==(6,17):return steps_demo('Record evidence for every test',[(label,fields('Test log · compare with the working app',[('Action',action),('Expected',result),('Observed','Try it in the supplied starter; record what actually happens')])) for label,action,result in [('Blank','Clear the search','All matching-category resources'),('No match','Search zzz','Useful empty-result message'),('Mixed case','Search LIBRARY','Community library'),('Category','Combine category with search','Only records satisfying both filters'),('Narrow screen','Resize the starter window','Controls and content remain usable'),('Keyboard','Tab and activate controls','Visible focus and usable actions')]])
 return ''


def comfort_hotspots():
 return '<div class="comfort-hotspots">'+photo(5,3)+'<div class="hotspot-controls"><button type="button" data-scene-choice="0" aria-pressed="true" class="hotspot-screen">1 · Screen</button><button type="button" data-scene-choice="1" aria-pressed="false" class="hotspot-input">2 · Input</button><button type="button" data-scene-choice="2" aria-pressed="false" class="hotspot-break">3 · Break</button></div></div>'
