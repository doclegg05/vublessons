"""Picture-led motion lessons: original artwork + concise, word-timed diagrams."""
import html,json,re,importlib.util
from pathlib import Path
_screen_spec=importlib.util.spec_from_file_location('screen_share_scenes',Path(__file__).with_name('screen-share-scenes.py'))
screens=importlib.util.module_from_spec(_screen_spec);_screen_spec.loader.exec_module(screens)
E=lambda s:html.escape(str(s),quote=True)
KINDS={1:['zoom','zoom','sound','privacy','routine'],2:['sync','permission','sync','recovery','permission'],3:['document','document','sheet','export','bundle'],4:['roles','timing','feedback','meeting','message'],5:['phishing','access','encrypt','attention','verify'],6:['app','parts','prompt','app','versions']}
TITLES={1:['Start with one task','Zoom into the task','Follow the sound','Share availability','Choose. Test. Explain.'],2:['Follow your file','Match access to the task','Deletion can travel too','Bring back the right copy','Suggest without rewriting'],3:['Make the next step visible','Structure guides the reader','Make the numbers prove it','Choose what travels','Show your resource pack'],4:['One file. Clear roles.','Together or later?','Show the useful change','Make room for others','Make the next action clear'],5:['Pause the pressure','Match access to purpose','Protect what can be read','Make room for a break','Show your safer next step'],6:['Build one useful thing','Three layers. One app.','Give the build boundaries','Test what actually happens','Keep a way back']}
ART={1:'workstation',2:'research',3:'creation',4:'collaboration',5:'security',6:'building'}

# Every chapter has an explicit visual plan; tuple = scene kind, scenario photo,
# and three inspectable states. Photos establish context, never carry UI text.
CHAPTERS = {
1: [
 ('routine','workstation',['Choose|Read a page comfortably','Test|Can I reach the next action?','Restore|Keep the original setting']),
 ('zoom',None,['Before|Page zoom: 100%','Change|Page zoom: 125%','Check|Find help stays reachable']),
 ('scope',None,['Page zoom|Only this webpage grows','Display scaling|Apps and system controls grow','Choose|Make the smallest useful change']),
 ('sound',None,['Destination|Headset selected','App setting|Check the meeting output too','Test|Unmute and play a short sample']),
 ('connections',None,['Processor|Carries out instructions','Memory|Current work on the workbench','Storage|Saved file in the cabinet']),
 ('print',None,['Preview|Destination · range · orientation','Test|Print one page first','Queue|Check before sending it again']),
 ('calendar',None,['Library practice|2:00–3:00 · Room A','Reminder|Check timing and permission','Reopen|Same event in day / week / month']),
 ('privacy',None,['Owner|Library practice · Room A','Partner|Busy · 2:00–3:00','Verify|Inspect the partner view']),
 ('automation',None,['Account|Confirm the active account','Reminder|Check notification permission','Help|Match instructions to your version']),
 ('routine','workstation',['Choose|Read · hear · remember','Explain|Expected result versus actual','Finish|Save · restore · sign out'])],
2: [
 ('search','library',['Task|Find community computer help','Place|Use your West Virginia town','Evidence|Confirm the details independently']),
 ('search',None,['Broad|Computer help','Refine|Computer help + library + town','Adjust|Remove a term if too restrictive']),
 ('source-check',None,['Responsibility|Who published this page?','Fit|Place · date · purpose','Conflict|Check the responsible organization']),
 ('source-trail',None,['Source|Organization · title · address','Checked|Date accessed · verified fact','Separate|Source statement ≠ my interpretation']),
 ('form',None,['Purpose|Who collects this information?','Required|Fictional topic and contact route','Review|Practice only: nothing is sent']),
 ('files',None,['Folder|Practice resources','Rename|computer-help-notes.txt','Reopen|Check location and account']),
 ('permission',None,['Viewer|Read the shared document','Commenter|Suggest without rewriting','Editor|Change the content; test access']),
 ('sync',None,['Sync|A deletion may reach both devices','Backup|Separate earlier recovery copy','Check|Saving status and recovery options']),
 ('recovery',None,['Recover|Trash or earlier version?','Package|Create ZIP from approved copies','Inspect|Extract and open the files']),
 ('evidence','library',['Source note|Fact · address · date checked','Folder|Recognizable name and location','Partner|Right access and recovery choice'])],
3: [
 ('document','resource-pack',['Audience|Community computer-help reader','Purpose|A clear next action','Pack|Handout · workbook · slides']),
 ('document',None,['Heading style|Computer help','Numbered steps|Choose · visit · ask','Useful link|Read the computer-help guide']),
 ('editing',None,['Select|Check exactly what is selected','Preserve|Copy and undo unwanted changes','Review|Comment ≠ tracked suggestion']),
 ('sheet',None,['Column A|Item names','Column B|Cost in dollars','Cell B2|Paper: 12']),
 ('sheet',None,['Formula|=SUM(B2:B4)','Challenge|Paper: 12 → 15','Check|Total: 25 → 28']),
 ('chart',None,['Source|Paper 15 · folders 8 · pens 5','Question|Which supply costs most?','Check|Title and units match the table']),
 ('slide-design',None,['Slide 1|Purpose and useful image','Slide 2|One action at a time','Image edit|Crop removes; resize changes size']),
 ('media-edit',None,['Preserve|Keep the original clip','Edit|Trim ends; split unwanted section','Review|Listen at cuts; recheck captions']),
 ('export',None,['DOCX|Editable document structure','PDF|Inspect the saved page layout','CSV|Inspect values; record image credit']),
 ('bundle','resource-pack',['Reader|Can they find the next action?','Workbook|Does the total respond?','Improve|Fix one observed confusion'])],
4: [
 ('roles','collaboration',['Task|Plan a community help session','Output|One useful handout','People|Owner · writer · reviewer']),
 ('identity-channel',None,['Task|Message, shared file or meeting?','Identity|Training profile is active','Timing|Enough context for a later reply']),
 ('message',None,['Subject|Review the computer-help handout','Request|Comment on the contact section','Timing|Reply before our practice session']),
 ('email-fields',None,['To / Cc|Visible recipient list','Bcc|Other recipients cannot see addresses','Reply all|Inspect who will receive it']),
 ('roles',None,['Before|Three competing file copies','Agree|One shared handout','Coordinate|Roles, access and response time']),
 ('feedback',None,['Vague|Make this better','Specific|Add the contact details here','Resolve|Explain decision after responding']),
 ('meeting',None,['Prepare|Sound test and captions','Participate|Mute or raise hand as needed','Choice|Ask before recording; keep notes']),
 ('community',None,['Read|Community rules and context','Verify|Compare claim with official source','Post|Share only agreed information']),
 ('commerce',None,['Today|Fictional trial offer','Renewal|12 dollars each month','Inspect|Seller · cancellation · full terms']),
 ('evidence','collaboration',['Draft|Clear request and response time','Shared file|Correct access and revised section','Record|Decision and next action'])],
5: [
 ('verify','safety',['Pause|What is being requested?','Inspect|What evidence do I have?','Verify|Choose an independent route']),
 ('comfort','workstation',['Comfort|Screen and input within reach','Access|Captions · large text · keyboard','Control|Choose a helpful adjustment']),
 ('phishing',None,['Claim|Your service will stop','Request|Provide information immediately','Evidence|A convincing logo is not proof']),
 ('trusted-route',None,['Message route|Sender supplies its own evidence','Independent route|Open a known website or bookmark','Confirm|Ask whether the issue exists']),
 ('encrypt',None,['Read-only|Content remains readable','Encryption|Key required to read the data','Limit|Unlocked accounts still need care']),
 ('usb','usb',['Found|Ordinary appearance proves nothing','Pause|Keep the drive disconnected','Procedure|Give it to authorized staff']),
 ('access',None,['Meeting|Camera or microphone may fit task','Text page|Camera access is unrelated','Review|Check app and permission later']),
 ('wellbeing',None,['Identity|A friendly story is not verification','Attention|Choose notifications and breaks','Support|Report · block · trusted help']),
 ('decision',None,['Claim|A code is needed for an appointment','Unverified|Who is actually asking?','Next step|Do not share; check known contact']),
 ('results',None,['Result|A classroom score, not certification','Review|Find a skill to practice','Transfer|Repeat a useful task with less help'])],
6: [
 ('app','app-planning',['Familiar task|Find a community resource','Small scope|One page, search and filter','Safe data|Fictional records only']),
 ('product-types',None,['Website|Information to read','Web app|Input → filtered result','SaaS|Hosted service and ongoing support']),
 ('parts',None,['HTML|Heading, label and search field','CSS|Layout and readable focus','JavaScript|Match records to the search']),
 ('acceptance',None,['Search library|Community library appears','Search zzz|No matching resources','Keyboard|Every control has visible focus']),
 ('prompt',None,['User and task|Find fictional community resources','Controls|Labeled search and category filter','Boundaries|No external dependencies or secrets']),
 ('local-file',None,['Save|resource-finder-v1.html','Open|Check heading, controls and results','No account|Edit heading; save and refresh']),
 ('app',None,['library|Matching resource shown','zzz|Clear no-results message','LIBRARY|Same match; also test category']),
 ('keyboard',None,['Keyboard|Tab through visible controls','Narrow screen|Labels and results remain readable','Data|Bundled file ≠ shared database']),
 ('versions',None,['Report|LIBRARY fails; library succeeds','Repair|Match case without losing filter','Retest|Failed check and a passing check']),
 ('evidence','app-planning',['Demonstrate|Run three acceptance checks','Explain|One part and one revision','Limit|Local prototype ≠ public service'])]
}

def chapter_plan(n,index):
 kind,photo,steps=CHAPTERS[n][index]
 if (n,index) in screens.SELECTED:
  return dict(kind=kind,photo=None,steps=[action[4] for action in screens.PLANS[n,index][1]],layout='screen-share')
 return dict(kind=kind,photo=photo,steps=steps,layout='scenario' if photo else 'demonstration')

def package_panel():
 v=''
 for j,(k,label,sub) in enumerate([('file','Approved copies','Inspect the contents'),('file','ZIP archive','Package, not encrypt'),('file','Extracted files','Open and check each')]):
  v+=tile(k,label,18+j*253,45,217,239)+text(sub,126+j*253,340,25,anchor='middle')
 v+=arrow(239,165,266,165)+arrow(492,165,518,165)
 return '<svg class="diagram" viewBox="0 0 760 460" role="img" aria-label="Package, extract and verify a ZIP">'+v+'</svg>'

def evidence_panel(steps):
 v=''
 for j,entry in enumerate(steps):
  label,value=entry.split('|',1);y=18+j*140
  v+=f'<g id="detail-{j}">'+rect(18,y,724,124,'#173d5c')+rect(18,y,7,124,'#c9a227',radius=0)+text(f'{j+1:02}  {label}',47,y+42,29,'#E6C65C')+text(value,47,y+88,29)+'</g>'
 return '<svg class="diagram" viewBox="0 0 760 460" role="img" aria-label="Worked example">'+v+'</svg>'

PATHS={
'usb':'<rect x=17 y=22 width=30 height=37 rx=6/><path d="M22 22V5h20v17M28 9v7M36 9v7"/>',
'computer':'<rect x="5" y="7" width="54" height="36" rx="3"/><path d="M32 43v13M18 57h28"/>',
'file':'<path d="M14 5h25l12 12v42H14zM39 5v14h12M23 30h19M23 40h19M23 50h12"/>',
'cloud':'<path d="M15 47a13 13 0 0 1-1-26 18 18 0 0 1 35-2 14 14 0 0 1 1 28z"/>',
'headset':'<path d="M9 34v-7a23 23 0 0 1 46 0v7M9 32H4v21h12V32zm46 0h5v21H48V32z"/>',
'speaker':'<path d="M6 23h13L36 8v48L19 41H6zM44 22q11 10 0 20M51 12q20 20 0 40"/>',
'camera':'<rect x="4" y="16" width="39" height="32" rx="4"/><path d="m43 25 16-10v34L43 39z"/>',
'lock':'<rect x="12" y="27" width="40" height="31" rx="4"/><path d="M21 27V17a11 11 0 0 1 22 0v10M32 38v10"/>',
'person':'<circle cx="32" cy="17" r="11"/><path d="M10 58v-9a22 22 0 0 1 44 0v9z"/>',
'check':'<circle cx="32" cy="32" r="27"/><path d="m17 32 10 11 21-23"/>',
'edit':'<path d="m10 44 32-32 12 12-32 32-15 3zM36 18l12 12"/>',
'chat':'<path d="M5 7h54v38H30L13 59V45H5zM16 21h32M16 31h23"/>',
'clock':'<circle cx="32" cy="32" r="27"/><path d="M32 15v18l12 9"/>',
'bin':'<path d="M9 17h46M24 17V7h16v10M15 17l4 42h26l4-42M26 26v22M38 26v22"/>',
'email':'<rect x="5" y="12" width="54" height="40" rx="4"/><path d="m7 15 25 20 25-20"/>',
'search':'<circle cx="27" cy="26" r="19"/><path d="m41 41 17 17"/>',
'key':'<circle cx="19" cy="24" r="13"/><path d="m29 34 23 23 9-9-7-7-7 7M35 40l8-8"/>',
'mic':'<rect x="23" y="4" width="18" height="35" rx="9"/><path d="M14 28v6a18 18 0 0 0 36 0v-6M32 52v9M20 61h24"/>',
'hand':'<path d="M15 34V16a4 4 0 0 1 8 0v15V9a4 4 0 0 1 8 0v22V7a4 4 0 0 1 8 0v24V14a4 4 0 0 1 8 0v29c0 12-6 18-18 18-6 0-11-4-15-9L5 39a5 5 0 0 1 7-7l7 8"/>',
'pause':'<circle cx="32" cy="32" r="27"/><path d="M24 20v24M40 20v24"/>',
'shield':'<path d="M32 4 55 14v17c0 15-12 25-23 30C21 56 9 46 9 31V14zM20 31l9 10 17-21"/>',
'usb':'<rect x="19" y="22" width="26" height="36" rx="4"/><path d="M24 22V4h16v18M29 8v8M35 8v8"/>',
'grid':'<rect x="5" y="7" width="54" height="50" rx="3"/><path d="M5 23h54M5 40h54M23 7v50M42 7v50"/>',
'slides':'<rect x="9" y="8" width="48" height="35" rx="3"/><path d="M4 20v31h42M33 43v14M21 60l12-3 12 3M20 20h25M20 29h17"/>',
'undo':'<path d="M18 22h22a17 17 0 0 1 0 34H18M18 22 30 10M18 22l12 12"/>',
'filter':'<path d="M4 8h56L38 33v23H26V33z"/>',
}
def icon(kind,x,y,size=78,color='#E6C65C',id=''):
 return f'<svg {f"id={id}" if id else ""} x="{x}" y="{y}" width="{size}" height="{size}" viewBox="0 0 64 64" fill="none" stroke="{color}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">{PATHS[kind]}</svg>'
def text(s,x,y,size=32,color='white',id='',anchor='start'):
 return f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" font-weight="700" text-anchor="{anchor}" {f"id={id}" if id else ""}>{E(s)}</text>'
def rect(x,y,w,h,fill='#234b6a',id='',radius=14):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" {f"id={id}" if id else ""}/>'
def arrow(x1,y1,x2,y2,id=''):
 direction=1 if x2>x1 else -1
 return f'<path {f"id={id}" if id else ""} d="M{x1} {y1}H{x2}m{-12*direction} -10 {12*direction} 10 {-12*direction} 10" fill="none" stroke="#E6C65C" stroke-width="4"/>'
def tile(kind,label,x,y,w=210,h=170,id=''):
 return f'<g {f"id={id}" if id else ""}>'+rect(x,y,w,h)+icon(kind,x+(w-68)/2,y+22,68)+text(label,x+w/2,y+h-22,28,anchor='middle')+'</g>'
def paper(x,y,w=190,h=235,id=''):
 return f'<g {f"id={id}" if id else ""}>'+rect(x,y,w,h,'#e1efed')+rect(x+22,y+h*.11,w-44,14,'#1b365d',radius=3)+''.join(rect(x+22,y+h*(.30+j*.13),w-44-(j%2)*35,7,'#72978f',radius=2) for j in range(4))+'</g>'

def diagram(kind,i):
 note='';v=''
 if kind=='zoom':
  v=rect(25,22,710,356,'#e1efed')+rect(25,22,710,47,'#c4d8de')+text('100%',675,55,28,'#1b365d','zoom-value',anchor='end')
  v+='<g id="zoom-content">'+text('Computer help',70,139,34,'#1b365d')+text('Choose one task.',70,192,28,'#1b365d')+rect(70,229,420,12,'#72978f',radius=3)+rect(70,259,345,12,'#72978f',radius=3)+rect(70,305,242,48,'#0f655f')+text('Find help',191,338,28,anchor='middle')+'</g>'
  note='One change. Check the result.'
 elif kind=='sound':
  v=tile('computer','Computer',20,60,210,180)+arrow(246,149,468,149)+tile('speaker','Output',490,60,235,180,'speaker-output')
  v+='<g id="headphones" opacity="0">'+rect(490,60,235,180)+icon('headset',567,83,78)+text('Headset',607,210,28,anchor='middle')+'</g>'
  v+=''.join(rect(190+j*44,343,24,8,'#E6C65C',f'wave-{j}',4) for j in range(9));note='Select. Unmute. Test.'
 elif kind=='privacy':
  v=rect(20,35,330,295)+rect(410,35,330,295)+text('Your calendar',185,83,31,anchor='middle')+text('Partner sees',575,83,31,anchor='middle')
  v+=rect(44,114,280,186,'#e1efed')+text('Library practice',64,157,28,'#1b365d')+text('2:00–3:00',64,205,28,'#1b365d')+text('Room A',64,253,28,'#1b365d')
  v+=rect(434,114,280,186,'#c9a227')+icon('lock',543,126,62,'#1b365d')+text('Busy',574,233,42,'#1b365d',anchor='middle')+text('2:00–3:00',574,279,28,'#1b365d',anchor='middle');note='Availability, without private details.'
 elif kind=='routine':
  v=tile('edit','Choose',18,92,210,220,'choose')+tile('check','Test',274,92,210,220,'test')+tile('undo','Explain / undo',530,92,210,220,'explain')+arrow(233,185,270,185)+arrow(490,185,525,185);note='Save work. Restore lab settings.'
 elif kind=='sync':
  v=tile('computer','This device',20,30,230,170)+tile('cloud','Cloud account',500,30,240,170)+arrow(265,110,490,110)
  v+=icon('file',292,73,65,id='travel-file')+paper(70,237,130,145,'local-copy')+paper(552,237,130,145,'cloud-copy')
  v+='<g id="backup">'+icon('file',343,235,65)+text('Backup',376,330,29,anchor='middle')+text('Separate copy',376,368,25,anchor='middle')+'</g>'
  v+='<g id="deletion" opacity="0">'+icon('bin',86,255,95,'#E6C65C')+icon('bin',568,255,95,'#E6C65C')+'</g>';note='Check saving and the account.' if i==0 else 'Sync ≠ a separate backup.'
 elif kind=='permission':
  v=paper(16,73,180,255)+icon('person',68,91,73,'#0f655f')+arrow(205,205,274,205)
  for j,(k,label) in enumerate([('search','Viewer'),('chat','Commenter'),('edit','Editor')]):
   y=30+j*128;v+=f'<g id="access-{j}">'+rect(292,y,444,110)+icon(k,313,y+21,63)+text(label,410,y+65,34)+'</g>'
  note='Give only the access the task needs.'
 elif kind=='recovery':
  v=tile('bin','Deleted file',20,34,310,180,'trash')+tile('clock','Earlier version',430,34,310,180,'history')+paper(288,257,184,144,'restored')+text('Preview → restore',380,444,32,anchor='middle');note='Coordinate before replacing shared work.'
 elif kind=='document':
  v=rect(65,17,630,396,'#e1efed')+text('Computer help',107,83,37,'#1b365d','doc-title')
  for j,s in enumerate(['Choose a task','Visit the desk','Ask how to repeat']):
   v+=f'<g id="doc-step-{j}">'+rect(105,117+j*77,50,50,'#0f655f')+text(str(j+1),130,152+j*77,28,anchor='middle')+text(s,181,152+j*77,31,'#1b365d')+'</g>'
  note='A clear heading. A useful sequence.'
 elif kind=='sheet':
  v=rect(20,20,440,340,'#e1efed')+text('A',168,62,27,'#1b365d')+text('B',370,62,27,'#1b365d')
  v+=text('1',43,118,27,'#1b365d')+text('Item',89,118,29,'#1b365d')+text('Cost ($)',290,118,29,'#1b365d')
  for j,(name,value) in enumerate([('Paper','12'),('Folders','8'),('Pens','5')]):v+=text(str(j+2),43,181+j*63,27,'#1b365d')+text(name,89,181+j*63,31,'#1b365d')+text(value,370,181+j*63,34,'#1b365d','paper-cost' if j==0 else '')
  v+=rect(490,30,250,330,'#0f655f')+text('Total',615,92,34,anchor='middle')+text('25',615,234,104,'#E6C65C','total',anchor='middle')+text('=SUM(B2:B4)',380,419,38,anchor='middle');note='Change a value. Watch the formula.'
 elif kind=='export':
  for j,(kind2,title) in enumerate([('edit','DOCX'),('file','PDF'),('grid','CSV')]):v+=tile(kind2,title,18+j*253,66,217,248,f'format-{j}')
  note='Revise · preserve layout · move data'
 elif kind=='bundle':
  v=paper(10,66,207,265,'handout')+rect(254,66,220,265,'#0f655f','workbook')+icon('grid',319,106,90)+text('28',364,280,68,'#E6C65C',anchor='middle')
  v+='<g id="slides">'+rect(514,110,182,158,'#72978f')+rect(534,87,182,158,'#c9a227')+rect(554,64,182,158,'#e1efed')+icon('slides',609,95,70,'#1b365d')+'</g>'
  for x,t in [(113,'Handout'),(364,'Workbook'),(634,'Slides')]:v+=text(t,x,388,29,anchor='middle')
  note='Check it with another reader.'
 elif kind=='roles':
  for j,t in enumerate(['Owner','Writer','Reviewer']):v+=tile('person',t,18+j*253,30,217,182,f'role-{j}')
  v+=f'<path d="M126 222v42h506v-42M379 222v86" fill="none" stroke="#E6C65C" stroke-width="4"/>'+rect(234,308,292,110,'#0f655f')+icon('file',258,326,67)+text('One copy',422,374,31,anchor='middle');note='Agree where the shared file lives.'
 elif kind=='timing':
  for j,label in enumerate(['Together','Later']):
   y=45+j*201;v+=text(label,20,y+45,33)+rect(210,y,530,135)
   for k in range(3):v+=icon('person' if j==0 else ['chat','edit','check'][k],244+k*172,y+28,62,id=f'time-{j}-{k}')
  note='Same time—or enough context for later.'
 elif kind=='feedback':
  v=paper(24,30,300,355)+rect(369,50,370,180,'#e1efed')+icon('chat',398,78,65,'#0f655f')+text('Add contact details',397,187,29,'#1b365d')+arrow(390,272,270,272)
  v+='<g id="contact" opacity="0">'+rect(45,284,258,64,'#0f655f')+text('Learning desk',174,325,28,anchor='middle')+'</g>'+icon('check',520,272,94,id='accepted');note='Specific change → useful result.'
 elif kind=='meeting':
  v=tile('person','You',40,30,295,220)+tile('person','Host',425,30,295,220)
  for j,k in enumerate(['headset','mic','hand']):v+=f'<g id="meeting-{j}">'+rect(132+j*185,294,128,123)+icon(k,165+j*185,318,64)+'</g>'
  v+=f'<path id="muted" d="M347 321l64 65" stroke="#E6C65C" stroke-width="6" opacity="0"/>';note='Test sound. Mute. Raise your hand.'
 elif kind=='message':
  v=rect(30,30,700,355,'#e1efed')+icon('email',65,60,75,'#0f655f')
  for j,t in enumerate(['Review the handout','Comment on the contact section','Reply before practice']):v+=f'<g id="message-{j}">'+rect(64,157+j*70,630,53,'#c4d8de')+text(t,85,192+j*70,29,'#1b365d')+'</g>'
  note='Subject · request · response time'
 elif kind=='phishing':
  v=rect(15,43,324,280,'#e1efed')+icon('email',128,72,87,'#1b365d')+text('ACT NOW',177,220,38,'#1b365d',anchor='middle')+rect(84,251,183,45,'#c9a227')+text('Unknown link',177,282,24,'#1b365d',anchor='middle')
  v+=icon('pause',354,136,82)+arrow(448,180,493,180)+tile('shield','Known contact',505,71,239,226,'verified');note='Pause. Verify independently.'
 elif kind=='access':
  v=tile('camera','Video meeting',25,37,320,190,'camera-yes')+tile('file','Text page',415,37,320,190,'camera-no')+icon('check',146,276,95,id='allow')
  v+='<g id="deny">'+icon('camera',529,278,95)+f'<path d="M524 280l100 94" stroke="#E6C65C" stroke-width="6"/>'+'</g>';note='Access must fit the task.'
 elif kind=='encrypt':
  v=tile('file','Read-only',10,54,203,208)+text('Still readable',111,306,26,anchor='middle')+tile('file','Original data',273,54,210,208)+arrow(491,155,529,155)+tile('lock','Key required',538,54,210,208,'locked')
  v+='<g id="cipher">'+rect(287,299,448,91,'#0f655f')+text('7fA2 · 9cD4 · e18B',511,359,34,anchor='middle')+'</g>';note='Encryption protects reading.'
 elif kind=='attention':
  for j in range(3):v+=f'<g id="alert-{j}">'+rect(15,45+j*108,330,82)+icon('chat',34,61+j*108,48)+rect(105,71+j*108,205,12,'#b7d1ce',radius=3)+'</g>'
  v+=tile('pause','Take a break',425,70,315,264,'quiet');note='Choose what gets your attention.'
 elif kind=='verify':
  for j,(k,t) in enumerate([('search','Evidence'),('shield','Verify'),('check','Safer action')]):v+=tile(k,t,18+j*253,90,217,226,f'safe-{j}')
  v+=arrow(239,200,267,200)+arrow(490,200,520,200);note='Explain the decision to a partner.'
 elif kind=='app':
  v=rect(30,22,700,370,'#e1efed')+rect(53,48,474,63,'white')+icon('search',68,62,34,'#0f655f')+text('library',126,92,31,'#1b365d','query')+rect(543,48,162,63,'#c9a227')+text('All',625,91,29,'#1b365d',anchor='middle')
  v+='<g id="match">'+rect(53,142,651,94,'#c4d8de')+icon('file',74,161,53,'#0f655f')+text('Community library',153,201,33,'#1b365d')+'</g>'
  v+='<g id="empty" opacity="0">'+icon('search',338,147,75,'#0f655f')+text('No matching resources',380,285,34,'#1b365d',anchor='middle')+'</g>'
  v+=text('Fictional resources',380,355,26,'#1b365d',anchor='middle');note='Search. Filter. Check the result.'
 elif kind=='parts':
  for j,(k,t) in enumerate([('file','HTML'),('grid','CSS'),('filter','JavaScript')]):v+=tile(k,t,18+j*253,60,217,220,f'layer-{j}')
  v+=text('Structure',126,343,29,anchor='middle')+text('Appearance',379,343,29,anchor='middle')+text('Behavior',632,343,29,anchor='middle');note='A local prototype—not a real account service.'
 elif kind=='prompt':
  for j,(k,t) in enumerate([('search','Task'),('filter','Controls'),('check','Tests'),('lock','Boundaries')]):v+=tile(k,t,20+(j%2)*380,20+(j//2)*212,340,190,f'prompt-{j}')
  note='Fictional data. No private keys.'
 elif kind=='versions':
  v=tile('file','Version 1',15,42,265,234,'version-1')+arrow(293,159,455,159)+tile('edit','Version 2',477,42,265,234,'version-2')
  v+=icon('undo',335,287,89,id='restore')+text('Retest the change',194,406,30,anchor='middle')+text('Retest what worked',574,406,30,anchor='middle');note='Keep both versions and your test log.'
 elif kind=='connections':
  for j,(k,t) in enumerate([('computer','Processing'),('grid','Working memory'),('file','Saved storage')]):v+=tile(k,t,15+j*253,40,222,197,f'concept-{j}')
  v+=icon('computer',40,290,78)+arrow(135,330,288,330)+icon('grid',307,290,78)+arrow(400,330,554,330)+icon('file',580,290,78);note='Active work and saved files serve different jobs.'
 elif kind=='print':
  v=rect(20,26,287,373,'#e1efed')+text('Preview',163,82,31,'#1b365d',anchor='middle')+''.join(rect(45,124+j*49,234-(j%2)*28,8,'#72978f',radius=2) for j in range(5))
  for j,t in enumerate(['1  Destination','2  Page range','3  Test one page']):v+=f'<g id="concept-{j}">'+rect(354,46+j*116,387,95)+text(t,380,104+j*116,30)+'</g>'
  note='Preview → test → print more'
 elif kind=='calendar':
  v=rect(15,20,728,397,'#e1efed')+text('Library practice',48,74,35,'#1b365d')
  for j,t in enumerate(['Day','Week','Month']):v+=f'<g id="concept-{j}">'+rect(45+j*235,109,206,48,'#234b6a')+text(t,148+j*235,143,28,anchor='middle')+'</g>'
  for col in range(7):
   for row in range(3):v+=rect(45+col*94,178+row*65,87,58,'#c4d8de',radius=5)
  v+=rect(233,243,181,58,'#0f655f')+text('2–3 · Room A',324,281,25,anchor='middle');note='Check the day, time, place and reminder.'
 elif kind=='search':
  v=rect(22,27,716,67,'#e1efed')+icon('search',41,40,43,'#0f655f')+text('computer help',105,72,29,'#1b365d','search-query')
  for j,(t,sub) in enumerate([('Official service page','Responsible organization'),('Check the details','Location · date · purpose'),('Record the source','Address · fact · date checked')]):
   v+=f'<g id="concept-{j}">'+rect(22,122+j*101,716,88)+text(t,49,158+j*101,29)+text(sub,49,189+j*101,24,'#E6C65C')+'</g>'
  note='Useful results need evidence and relevance.'
 elif kind=='form':
  v=rect(55,20,649,398,'#e1efed')+text('Practice request',88,74,35,'#1b365d')
  for j,t in enumerate(['Help topic: finding a file','Contact: ask at the desk','Review before submitting']):v+=f'<g id="concept-{j}">'+rect(88,112+j*91,581,70,'#c4d8de')+text(t,109,157+j*91,28,'#1b365d')+'</g>'
  note='Fictional information. No real request is sent.'
 elif kind=='chart':
  v=text('Supply costs ($)',30,45,34)+f'<path d="M173 73v306h540" fill="none" stroke="#b7d1ce" stroke-width="3"/>'
  for j,(t,value,width) in enumerate([('Paper','15',450),('Folders','8',240),('Pens','5',150)]):
   v+=text(t,151,135+j*101,28,anchor='end')+f'<g id="concept-{j}">'+rect(181,89+j*101,width,65,'#0f655f',radius=5)+text(value,202,133+j*101,32,'#E6C65C')+'</g>'
  note='Match the chart to the checked table.'
 elif kind=='media-edit':
  v=text('Keep the useful explanation',380,54,34,anchor='middle')
  for j,(t,w,c) in enumerate([('Start',116,'#234b6a'),('Explain',221,'#0f655f'),('Pause',116,'#234b6a'),('Result',221,'#0f655f')]):
   x=[20,143,371,494][j];v+=rect(x,118,w,126,c)+text(t,x+w/2,192,28,anchor='middle')
  for j,(k,t) in enumerate([('undo','Preserve original'),('edit','Check the edit'),('chat','Retest captions')]):v+=f'<g id="concept-{j}">'+icon(k,75+j*247,291,61)+text(t,133+j*247,397,26,anchor='middle')+'</g>'
  note='Trim ends. Split sections. Check speech and captions.'
 elif kind=='email-fields':
  v=rect(30,29,700,363,'#e1efed')
  for j,(t,sub) in enumerate([('To','Main recipients'),('Cc','Visible copy'),('Bcc','Other recipients cannot see addresses')]):
   v+=f'<g id="concept-{j}">'+text(t,60,92+j*113,35,'#1b365d')+rect(149,51+j*113,550,76,'#c4d8de')+text(sub,171,99+j*113,25,'#1b365d')+'</g>'
  note='Inspect every recipient. Check Reply all.'
 elif kind=='commerce':
  v=tile('clock','Trial today',20,41,300,192,'concept-0')+arrow(336,143,415,143)+tile('file','$12 each month',436,41,304,192,'concept-1')
  v+=f'<g id="concept-2">'+rect(20,283,720,109,'#0f655f')+text('Seller · renewal · cancellation',380,348,34,anchor='middle')+'</g>';note='Fictional offer. No payment is required.'
 elif kind=='source-trail':
  v=rect(22,14,716,425,'#e1efed')+text('My source record',52,61,34,'#1b365d')
  rows=[('Organization','Fictional community library'),('Title / address','Computer help · example.org/help'),('Date accessed','Record the day you checked'),('Verified fact','The source states Room A'),('Interpretation','My conclusion is separate')]
  for j,(label,value) in enumerate(rows):
   y=95+j*67;v+=f'<g id="concept-{j}">'+text(label,52,y,23,'#0f655f')+text(value,52,y+32,28,'#1b365d')+'</g>'
  note='Fictional example · record evidence you can revisit.'
 elif kind=='usb':
  v=tile('usb','Unknown drive',20,64,214,228,'concept-0')+tile('hand','Do not connect',273,64,214,228,'concept-1')+tile('person','Authorized staff',526,64,214,228,'concept-2')
  v+=arrow(240,180,267,180)+arrow(493,180,520,180);note='Appearance does not prove safety.'
 elif kind=='automation':
  v=rect(25,25,710,385,'#e1efed')+text('Practice settings',58,77,35,'#1b365d')
  for j,(k,label,value) in enumerate([('person','Active account','Training profile'),('clock','Reminder','Before Library practice'),('search','Help version','Matches this application')]):
   y=100+j*96;v+=f'<g id="detail-{j}">'+rect(48,y,664,81,'#c4d8de')+icon(k,62,y+14,48,'#0f655f')+text(label,131,y+29,23,'#1b365d')+text(value,131,y+62,29,'#1b365d')+'</g>'
  note='Check the saved setting, not just the request.'
 elif kind=='source-check':
  for j,(label,body) in enumerate([('Directory lead','Possible computer help'),('Responsible source','Confirm place and availability')]):
   x=14+j*385;v+=rect(x,25,350,337,'#e1efed')+rect(x,25,350,53,'#c4d8de')+text(label,x+175,62,29,'#1b365d',anchor='middle')+icon('search' if j==0 else 'person',x+133,107,80,'#0f655f')
   v+=text('Computer help',x+175,240,28,'#1b365d',anchor='middle')+text('Check current details',x+175,287,24,'#1b365d',anchor='middle')
  v+=arrow(290,396,473,396);note='A lead becomes useful after independent confirmation.'
 elif kind=='editing':
  v=rect(18,20,456,391,'#e1efed')+text('Computer help',45,73,34,'#1b365d')+rect(43,106,400,60,'#c9a227')+text('Visit the learning desk',56,145,28,'#1b365d')
  v+=text('Selected passage',48,217,27,'#1b365d')+icon('undo',184,272,90,'#0f655f')+rect(495,70,245,252)+icon('chat',578,94,70)+text('Comment',617,224,29,anchor='middle')+text('Suggest a change',617,275,24,anchor='middle');note='Select carefully. Keep a route back.'
 elif kind=='slide-design':
  for j,label in enumerate(['Purpose','Action','Result']):
   x=18+j*250;v+=rect(x,30,225,170,'#e1efed')+text(label,x+112,72,30,'#1b365d',anchor='middle')+icon(['person','edit','check'][j],x+75,99,69,'#0f655f')
  v+=rect(45,253,280,154,'#72978f')+rect(85,277,196,105,'#0f655f')+text('Crop',185,439,28,anchor='middle')+rect(441,268,234,130,'#72978f')+text('Resize proportionally',558,439,27,anchor='middle');note='One message per slide. Preserve the original image.'
 elif kind=='identity-channel':
  v=rect(22,22,716,83,'#e1efed')+icon('person',42,35,57,'#0f655f')+text('Active profile: Training',128,74,34,'#1b365d')
  for j,(k,t) in enumerate([('email','Message'),('file','Shared file'),('camera','Meeting')]):v+=tile(k,t,18+j*253,147,217,236)
  note='Choose a channel and identity that fit the task.'
 elif kind=='community':
  v=rect(15,30,346,360,'#e1efed')+text('Community draft',40,82,30,'#1b365d')+icon('chat',130,107,91,'#0f655f')+text('Is this detail verified?',188,254,24,'#1b365d',anchor='middle')+text('Permission to share?',188,308,24,'#1b365d',anchor='middle')
  v+=rect(395,30,350,360)+text('Source check',570,82,30,anchor='middle')+icon('search',526,114,84)+text('Official contact',570,258,27,anchor='middle')+text('Hours · requirements',570,313,24,anchor='middle');note='Read the rules. Verify details. Respect privacy.'
 elif kind=='comfort':
  v=icon('computer',271,20,214)+rect(172,254,416,25,'#c9a227')+icon('grid',239,298,74)+icon('hand',411,295,76)
  v+=text('Readable screen',379,247,31,anchor='middle')+text('Input within reach',379,423,31,anchor='middle')+icon('chat',48,95,76)+text('Captions',88,220,24,anchor='middle')+icon('pause',642,95,76)+text('Breaks',679,220,24,anchor='middle');note='Adapt the setup to your task and comfort.'
 elif kind=='wellbeing':
  v=rect(20,20,340,390,'#e1efed')+text('Notifications',190,74,31,'#1b365d',anchor='middle')
  for j in range(3):v+=rect(43,110+j*78,294,57,'#c4d8de')+icon('chat',59,122+j*78,31,'#0f655f')+text('Choose alerts',110,149+j*78,23,'#1b365d')
  v+=rect(408,51,330,328)+text('Interaction options',573,105,29,anchor='middle')
  for j,t in enumerate(['Report','Block','Ask trusted support']):v+=rect(430,137+j*70,286,53,'#0f655f')+text(t,573,172+j*70,25,anchor='middle')
  note='Your attention and wellbeing are part of safety.'
 elif kind=='decision':
  v=rect(20,25,420,367,'#e1efed')+icon('email',50,50,71,'#0f655f')+text('Appointment message',52,159,31,'#1b365d')+text('A private code is requested',52,222,26,'#1b365d')+rect(52,267,350,63,'#c9a227')+text('Pause before sharing',227,309,28,'#1b365d',anchor='middle')
  v+=icon('pause',475,81,100)+icon('search',607,230,100)+arrow(494,229,601,229);note='Evidence → unknowns → independent next step.'
 elif kind=='evidence':
  for j,(k,t) in enumerate([('file','Saved work'),('check','Test evidence'),('chat','Next step')]):v+=tile(k,t,18+j*253,45,217,258)
  v+=arrow(237,167,269,167)+arrow(491,167,522,167)+text('Show the result. Explain why you trust it.',380,396,31,anchor='middle');note='Choose a useful task to repeat independently.'
 elif kind=='product-types':
  for j,(k,label,detail) in enumerate([('file','Website','Read information'),('filter','Web app','Input → result'),('cloud','SaaS','Ongoing service')]):
   v+=tile(k,label,18+j*253,30,217,226)+text(detail,126+j*253,310,25,anchor='middle')
  v+=rect(20,357,720,69,'#0f655f')+text('Accounts · shared data · support · maintenance',380,400,26,anchor='middle');note='Our local prototype is a smaller task.'
 elif kind=='scope':
  for j,label in enumerate(['Page zoom','Display scaling']):
   x=15+j*385;v+=rect(x,32,350,315,'#e1efed')+rect(x,32,350,45,'#c4d8de')+text(label,x+175,65,29,'#1b365d',anchor='middle')
   v+=rect(x+23,102,303,62,'#0f655f')+text('Page content',x+175,143,32,anchor='middle')
   v+=rect(x+23,190,303,105,'#c4d8de')+text('Find help',x+175,253,32,'#1b365d',anchor='middle')
  v+=text('Page only',190,403,32,anchor='middle')+text('Apps + system',575,403,32,anchor='middle');note='Choose the scope that fits the task.'
 elif kind=='files' or kind=='local-file':
  v=rect(20,25,720,379,'#e1efed')+rect(20,25,720,65,'#c4d8de')+text('Practice resources',49,69,33,'#1b365d')
  name='computer-help-notes.txt' if kind=='files' else 'resource-finder-v1.html'
  v+=icon('file',60,123,80,'#0f655f')+text(name,165,172,31,'#1b365d')+arrow(160,234,585,234)+rect(79,272,600,82,'#0f655f')+text('Save → reopen → inspect',379,326,32,anchor='middle');note='Keep a recognizable working copy.'
 elif kind=='trusted-route':
  v=tile('email','Unexpected message',18,32,345,233)+tile('search','Known contact',397,32,345,233)
  v+=text('Unverified request',190,326,29,anchor='middle')+text('Independent check',570,326,29,anchor='middle')+text('Do not use the message’s supplied number',380,411,30,'#E6C65C',anchor='middle');note='Use a route you already trust.'
 elif kind=='results':
  v=rect(30,24,700,378,'#e1efed')+text('My next practice',65,81,36,'#1b365d')
  for j,(name,w) in enumerate([('Settings',430),('Files',310),('Communication',365)]):
   y=119+j*87;v+=text(name,62,y+30,26,'#1b365d')+rect(285,y,w,40,'#0f655f')
  note='Fictional learning report · not certification'
 elif kind=='acceptance':
  v=rect(20,30,720,375,'#e1efed')+text('Check',55,82,30,'#1b365d')+text('Expected result',338,82,30,'#1b365d')
  for j,(a,b) in enumerate([('library','Community library'),('zzz','No matching resources'),('Tab key','Visible focus')]):
   y=130+j*95;v+=rect(40,y-20,680,75,'#c4d8de')+text(a,55,y+27,30,'#1b365d')+text(b,335,y+27,28,'#1b365d')
  note='Expected versus actual: observe the saved app.'
 elif kind=='keyboard':
  v=rect(25,22,710,320,'#e1efed')+rect(53,56,469,65,'#c4d8de','concept-0')+text('Search resources',80,99,30,'#1b365d')+rect(548,56,158,65,'#c9a227','concept-1')+text('All',627,99,29,'#1b365d',anchor='middle')
  v+=rect(53,155,653,95,'#c4d8de','concept-2')+text('Community library',85,214,32,'#1b365d')+rect(200,373,165,57)+text('Tab →',282,412,30,anchor='middle')+text('Visible focus',545,412,30,anchor='middle');v+='<rect id=focus-ring x=50 y=53 width=475 height=71 rx=8 fill=none stroke=#1b365d stroke-width=4 />';note='Keyboard · narrow screen · data location'
 return '<svg class="diagram" viewBox="0 0 760 460" role="img" aria-label="'+E(note)+'">'+v+'</svg>',note

CSS='''*{box-sizing:border-box}.canvas-ground{position:absolute;inset:0;background:#102c4b}.photo-window{position:absolute;left:0;top:0;width:400px;height:720px;overflow:hidden}.topic-photo{width:100%;height:100%;object-fit:cover;object-position:48% center}.photo-shade{position:absolute;left:0;bottom:0;width:400px;height:130px;background:#102c4b}.gold-divider{position:absolute;left:395px;top:0;width:5px;height:720px;background:#c9a227}.video-title{position:absolute;left:440px;top:55px;max-width:755px;margin:0;font-size:46px;line-height:1.14;color:white;letter-spacing:-.5px}.graphic-stage{position:absolute;left:440px;top:153px;width:784px;height:460px}.diagram{width:100%;height:100%;overflow:visible}.video-note{position:absolute;left:445px;bottom:53px;font-size:29px;color:#e6c65c;margin:0;max-width:755px;line-height:1.3}.video-brand{position:absolute;left:31px;bottom:37px;display:flex;align-items:center;gap:12px;color:white;font-size:24px;font-weight:700}.video-brand img{width:49px;height:49px}.graphic-stage text{font-family:VUB}.layout-wide .photo-window{width:270px}.layout-wide .gold-divider{left:265px}.layout-wide .photo-shade{width:270px}.layout-wide .video-title{left:312px;max-width:880px}.layout-wide .graphic-stage{left:312px;width:910px;height:466px;top:153px}.layout-wide .video-note{left:320px;max-width:870px}.layout-finale .photo-window{left:850px;width:430px}.layout-finale .gold-divider{left:845px}.layout-finale .photo-shade{left:850px;width:430px}.layout-finale .video-title{left:55px;max-width:740px}.layout-finale .graphic-stage{left:40px;width:780px}.layout-finale .video-note{left:55px;max-width:750px}.layout-finale .video-brand{left:885px}'''
def scene(n,i,b,words):
 if (n,i) in screens.SELECTED:return screens.scene(n,i,b,words)
 index=i;plan=chapter_plan(n,index);kind=plan['kind'];i=b.get('variant',i);cid=f'w{n}-scene-{index+1}';content,note=diagram(kind,i)
 if not note:raise ValueError(f'No authored diagram for {kind}')
 detail=(package_panel() if n==2 and index==8 else evidence_panel(plan['steps'])).replace('id="detail-', 'id="inspect-')
 content=f'<div class=main-example>{content}</div><div class=detail-example style="opacity:0">{detail}</div>'
 # Scope ids and every animation to the owning frame.
 for old in re.findall(r'id=([a-zA-Z0-9-]+)',content):content=content.replace(f'id={old}',f'id="{cid}-{old}"')
 for old in re.findall(r'id="([^\"]+)"',content):
  if not old.startswith(cid):content=content.replace(f'id="{old}"',f'id="{cid}-{old}"')
 def selector(s):return '#'+cid+' '+('#'+cid+'-'+s[1:] if s.startswith('#') else s)
 def at(phrase,fallback):
  tokens=[re.sub('[^a-z0-9]','',w['word'].lower()) for w in words];needle=[re.sub('[^a-z0-9]','',x.lower()) for x in phrase.split()]
  for j in range(len(tokens)-len(needle)+1):
   if needle and tokens[j:j+len(needle)]==needle:return round(words[j]['start']+b.get('leadIn',0.01),3)
  return round(b['audioDuration']*fallback+b.get('leadIn',0.01),3)
 events=[]
 def change(s,props,phrase='',f=.5):events.append(f'tl.set({json.dumps(selector(s))},{json.dumps(props)},{at(phrase,f)});')
 def move(s,props,phrase='',f=.5):events.append(f'tl.to({json.dumps(selector(s))},{json.dumps(dict(duration=.8,ease="power2.out",**props))},{at(phrase,f)});')
 def light(s,phrase='',f=.5):move(s,{'scale':1.06,'transformOrigin':'50% 50%'},phrase,f)
 if kind=='zoom':
  move('#zoom-content',{'scale':1.14,'transformOrigin':'70px 120px'},'larger' if i else 'one change',.45);change('#zoom-value',{'textContent':'125%'},'larger' if i else 'one change',.45)
  move('#zoom-content',{'scale':1},'restore',.84);change('#zoom-value',{'textContent':'100%'},'restore',.84)
 elif kind=='sound':
  change('#speaker-output',{'opacity':0},'headset',.35);change('#headphones',{'opacity':1},'headset',.35)
  for j in range(9):move(f'#wave-{j}',{'scaleY':[3,5,7,4,6,8,5,3,6][j],'transformOrigin':'50% 50%'},'play a short test',.55)
 elif kind=='search':
  change('#search-query',{'textContent':'computer help + library + town'},'library',.3)
  if index==1:change('#search-query',{'textContent':'computer help + town'},'remove',.72)
 elif kind=='privacy':move('.diagram',{'scale':1.04,'transformOrigin':'70% 45%'},'free or busy',.6)
 elif kind=='routine':
  for s,p,f in [('#choose','one helpful adjustment',.2),('#test','show a partner',.4),('#explain','restore',.6)]:light(s,p,f)
 elif kind=='sync':
  move('#travel-file',{'x':130},'cloud service' if i==0 else 'changes',.2)
  if i==2:
   move('#local-copy',{'opacity':0},'a deletion',.3);move('#cloud-copy',{'opacity':0},'sync alone',.45);move('#deletion',{'opacity':1},'sync alone',.45);light('#backup','a backup',.6)
  else:light('#cloud-copy','check that',.6)
 elif kind=='permission':
  for j,p in enumerate(['a viewer','a commenter','an editor'] if i==1 else ['','','']):
   if i==1:move(f'#access-{j} rect',{'fill':'#0f655f'},p,.25+j*.2)
  if i==4:move('#access-1 rect',{'fill':'#0f655f'},'commenter access',.5)
 elif kind=='recovery':light('#trash','trash',.2);light('#history','version history',.5);light('#restored','preview',.7)
 elif kind=='document':
  for j in range(3):move(f'#doc-step-{j}',{'x':10},'numbered list' if i==1 else 'next action',.28+j*.2)
 elif kind=='sheet' and index==4:change('#paper-cost',{'textContent':'15'},'paper to fifteen',.6);change('#total',{'textContent':'28'},'paper to fifteen',.6);light('#total','twenty-eight',.73)
 elif kind=='export':
  for j,p in enumerate(['editable document','a pdf','a csv']):light(f'#format-{j}',p,.15+j*.24)
 elif kind=='bundle':
  for s,p,f in [('#handout','handout',.2),('#workbook','workbook',.28),('#slides','slides',.36)]:move(s,{'y':-10},p,f)
 elif kind=='roles':
  for j,p in enumerate(['owner','writer','reviewer']):light(f'#role-{j}',p,.15+j*.17)
 elif kind=='timing':
  for j in range(3):move(f'#time-0-{j}',{'y':-9},'synchronous collaboration',.22);move(f'#time-1-{j}',{'x':10},'asynchronous collaboration',.5+j*.08)
 elif kind=='feedback':move('#contact',{'opacity':1},'add the contact number',.25);light('#accepted','accept the idea',.55)
 elif kind=='meeting':light('#meeting-0','test the sound',.15);move('#muted',{'opacity':1},'mute',.35);light('#meeting-2','raise-hand',.5)
 elif kind=='message':
  for j,p in enumerate(['specific subject','clear request','response time']):move(f'#message-{j} rect',{'fill':'#b2d8c9'},p,.2+j*.17)
 elif kind=='phishing':light('#verified','known website',.62)
 elif kind=='access':light('#allow','video meeting',.1);light('#deny','deny',.68)
 elif kind=='encrypt':light('#locked','encryption',.35);move('#cipher',{'y':-9},'unreadable',.45)
 elif kind=='attention':
  for j in range(3):move(f'#alert-{j}',{'x':-100,'opacity':0},'notification limits',.58+j*.04)
  light('#quiet','take breaks',.75)
 elif kind=='verify':
  for j,p in enumerate(['evidence','independent source','action']):light(f'#safe-{j}',p,.2+j*.2)
 elif kind=='app':
  if i==3:change('#query',{'textContent':'zzz'},'unmatched term',.3);move('#match',{'opacity':0},'unmatched term',.3);move('#empty',{'opacity':1},'unmatched term',.3);change('#query',{'textContent':'LIBRARY'},'uppercase',.5);move('#empty',{'opacity':0},'uppercase',.5);move('#match',{'opacity':1},'uppercase',.5)
  else:light('#match','readable results',.3)
 elif kind=='parts':
  for j,p in enumerate(['html','css','javascript']):light(f'#layer-{j}',p,.08+j*.25)
 elif kind=='prompt':
  for j,p in enumerate(['user should do','controls','test','fictional data']):move(f'#prompt-{j} rect',{'fill':'#0f655f'},p,.1+j*.2)
 elif kind=='versions':light('#version-1','first version',.1);light('#version-2','improvement',.28);move('#restore',{'rotation':-20,'transformOrigin':'50% 50%'},'keep both versions',.8)
 if kind=='automation':
  for j in range(3):light(f'#detail-{j}','',.17+j*.25)
 if kind=='keyboard':move('#focus-ring',{'attr':{'x':545,'width':166}},'operate the filter',.4)
 if kind in ['connections','print','calendar','search','form','chart','media-edit','email-fields','commerce','keyboard','usb','source-trail']:
  for j in range(5 if kind=='source-trail' else 3):
   move(f'#concept-{j}',{'scale':1.025,'transformOrigin':'50% 50%'},'',.12+j*(.14 if kind=='source-trail' else .24))
 layout='layout-split'
 # Preserve the instructional diagram; the ZIP handoff is a separate mechanism.
 if n==2 and index==8:
  move('.main-example',{'opacity':0},'zip',.66);move('.detail-example',{'opacity':1},'zip',.66)
 # Small chapter-specific evidence caption changes, without replacing pictures.
 for j,entry in enumerate(plan['steps']):
  change('.video-note',{'textContent':entry.replace('|',' · ')},'',.10+j*.28)
 photo=plan['photo']
 photohtml=f'<div class=photo-window><img class=topic-photo src="assets/{photo}.webp" alt=""></div>' if photo else ''
 if n==1 and index==0:
  photohtml='<div class=photo-window><video id="w1-generated-workstation" class="topic-photo clip" src="assets/workstation-intro.mp4" data-start="0" data-duration="7" data-track-index="0" muted playsinline></video></div>'
 if photo=='safety':
  photohtml='<div class=photo-window><svg class=topic-photo viewBox="0 0 1376 768" role="img" aria-label="Fictional home verification scenario"><image href="assets/safety.webp" width="1376" height="768"/><polygon points="287,355 361,337 440,540 353,566" fill="#e1efed"/><polygon points="805,174 1137,198 1120,407 779,375" fill="#e1efed"/><g transform="translate(319 376) rotate(-18)"><rect width="40" height="32" rx="4" fill="#1b365d"/><path d="M3 4 L20 19 L37 4" fill="none" stroke="#e6c65c" stroke-width="3"/></g><g transform="translate(812 215) rotate(5)"><text fill="#1b365d" font-size="24">Known contact</text><rect y="24" width="260" height="44" rx="5" fill="#c4d8de"/><text x="12" y="53" fill="#1b365d" font-size="21">Community desk</text><text y="107" fill="#1b365d" font-size="21">Verify independently</text></g></svg></div>'
 if photo:
  # Full landscape context first, then an unobstructed authored demonstration.
  events.insert(0,f'tl.set("#{cid} .graphic-stage",{{opacity:0}},0);')
  transition=6.5 if n==1 and index==0 else min(7,b["audioDuration"]*.16)
  events.append(f'tl.to("#{cid} .photo-window",{{opacity:0,duration:.5}},{transition});')
  events.append(f'tl.to("#{cid} .graphic-stage",{{opacity:1,duration:.5}},{transition});')
 css=CSS
 css+=' .graphic-stage{opacity:'+('0' if photo else '1')+'}'
 css+=' .main-example,.detail-example{position:absolute;inset:0}.graphic-stage{top:160px;height:445px}.video-note{bottom:92px;font-size:25px}.video-brand{bottom:20px;font-size:21px}.video-title{font-size:40px;top:34px}.video-brand img{width:36px;height:36px}'
 css+=' .gold-divider{left:40px;top:131px;width:1200px;height:3px}.video-title{left:52px;max-width:1160px;background:#102c4b;padding:5px 12px}.graphic-stage{left:105px;width:1070px;top:156px;height:445px}.video-note{left:105px;max-width:1070px;background:#102c4b;padding:5px 12px}.video-brand{left:52px}.photo-window{width:1280px;height:720px;inset:0}.topic-photo{width:100%;height:100%;object-fit:contain}.topic-photo text{font-family:VUB}.video-brand{background:#102c4b;padding:4px 8px}'
 for variant in ["layout-wide","layout-finale"]:
  css=re.sub(r"\."+variant+r" ([^{}]+)\{([^{}]+)\}", lambda m: m[1]+"{"+m[2]+"}" if variant==layout else "", css)
 return f'''<template><div id="{cid}" data-composition-id="{cid}" data-start="0" data-duration="{b['window']}" data-width="1280" data-height="720" style="position:relative;width:100%;height:100%;overflow:hidden"><style>@font-face{{font-family:VUB;src:url('assets/source-sans-3-latin-400-normal.woff2')}}@font-face{{font-family:VUB;src:url('assets/source-sans-3-latin-700-normal.woff2');font-weight:700}}#{cid}{{font-family:VUB}}{css}</style><div class="canvas-ground"></div>{photohtml}<div class="gold-divider"></div><h1 class="video-title">{E(b["title"])}</h1><div class="graphic-stage">{content}</div><p class="video-note">{E(note)}</p><div class="video-brand"><img src="assets/vub-seal.png" alt="">VUB Learning</div><script>const tl=gsap.timeline({{paused:true}});tl.fromTo("#{cid} .graphic-stage",{{y:10}},{{y:0,duration:.7,ease:"power2.out"}},0);{''.join(events)}window.__timelines["{cid}"]=tl;</script></div></template>'''
