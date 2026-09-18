"""Picture-led motion lessons: original artwork + concise, word-timed diagrams."""
import html,json,re
E=lambda s:html.escape(str(s),quote=True)
KINDS={1:['zoom','zoom','sound','privacy','routine'],2:['sync','permission','sync','recovery','permission'],3:['document','document','sheet','export','bundle'],4:['roles','timing','feedback','meeting','message'],5:['phishing','access','encrypt','attention','verify'],6:['app','parts','prompt','app','versions']}
TITLES={1:['Start with one task','Zoom into the task','Follow the sound','Share availability','Choose. Test. Explain.'],2:['Follow your file','Match access to the task','Deletion can travel too','Bring back the right copy','Suggest without rewriting'],3:['Make the next step visible','Structure guides the reader','Make the numbers prove it','Choose what travels','Show your resource pack'],4:['One file. Clear roles.','Together or later?','Show the useful change','Make room for others','Make the next action clear'],5:['Pause the pressure','Match access to purpose','Protect what can be read','Make room for a break','Show your safer next step'],6:['Build one useful thing','Three layers. One app.','Give the build boundaries','Test what actually happens','Keep a way back']}
ART={1:'workstation',2:'research',3:'creation',4:'collaboration',5:'security',6:'building'}
PATHS={
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
  v+=rect(44,114,280,186,'#e1efed')+text('Library visit',64,157,29,'#1b365d')+text('2:00–3:00',64,205,28,'#1b365d')+text('Room A',64,253,28,'#1b365d')
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
  v=rect(20,30,440,330,'#e1efed')+text('Item',50,78,29,'#1b365d')+text('Cost ($)',295,78,29,'#1b365d')
  for j,(name,value) in enumerate([('Paper','12'),('Folders','8'),('Pens','5')]):v+=text(name,50,140+j*63,31,'#1b365d')+text(value,342,140+j*63,34,'#1b365d','paper-cost' if j==0 else '')
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
  v=tile('usb','Unknown drive',10,54,203,208)+f'<path d="M46 90l129 119" stroke="#E6C65C" stroke-width="6"/>'+tile('file','Readable file',273,54,210,208)+arrow(491,155,529,155)+tile('lock','Key required',538,54,210,208,'locked')
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
 return '<svg class="diagram" viewBox="0 0 760 460" role="img" aria-label="'+E(note)+'">'+v+'</svg>',note

CSS='''*{box-sizing:border-box}.canvas-ground{position:absolute;inset:0;background:#102c4b}.photo-window{position:absolute;left:0;top:0;width:400px;height:720px;overflow:hidden}.topic-photo{width:100%;height:100%;object-fit:cover;object-position:48% center}.photo-shade{position:absolute;left:0;bottom:0;width:400px;height:130px;background:#102c4b}.gold-divider{position:absolute;left:395px;top:0;width:5px;height:720px;background:#c9a227}.video-title{position:absolute;left:440px;top:55px;max-width:755px;margin:0;font-size:46px;line-height:1.14;color:white;letter-spacing:-.5px}.graphic-stage{position:absolute;left:440px;top:153px;width:784px;height:460px}.diagram{width:100%;height:100%;overflow:visible}.video-note{position:absolute;left:445px;bottom:53px;font-size:29px;color:#e6c65c;margin:0;max-width:755px;line-height:1.3}.video-brand{position:absolute;left:31px;bottom:37px;display:flex;align-items:center;gap:12px;color:white;font-size:24px;font-weight:700}.video-brand img{width:49px;height:49px}.graphic-stage text{font-family:VUB}.layout-wide .photo-window{width:270px}.layout-wide .gold-divider{left:265px}.layout-wide .photo-shade{width:270px}.layout-wide .video-title{left:312px;max-width:880px}.layout-wide .graphic-stage{left:312px;width:910px;height:466px;top:153px}.layout-wide .video-note{left:320px;max-width:870px}.layout-finale .photo-window{left:850px;width:430px}.layout-finale .gold-divider{left:845px}.layout-finale .photo-shade{left:850px;width:430px}.layout-finale .video-title{left:55px;max-width:740px}.layout-finale .graphic-stage{left:40px;width:780px}.layout-finale .video-note{left:55px;max-width:750px}.layout-finale .video-brand{left:885px}'''
def scene(n,i,b,words):
 kind=KINDS[n][i];cid=f'w{n}-scene-{i+1}';content,note=diagram(kind,i)
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
 elif kind=='sound':
  change('#speaker-output',{'opacity':0},'headset',.35);change('#headphones',{'opacity':1},'headset',.35)
  for j in range(9):move(f'#wave-{j}',{'scaleY':[3,5,7,4,6,8,5,3,6][j],'transformOrigin':'50% 50%'},'play a short test',.55)
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
 elif kind=='sheet':change('#paper-cost',{'textContent':'15'},'paper to fifteen',.6);change('#total',{'textContent':'28'},'paper to fifteen',.6);light('#total','twenty-eight',.73)
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
  if i==3:change('#query',{'textContent':'zzz'},'no results',.3);move('#match',{'opacity':0},'no results',.3);move('#empty',{'opacity':1},'no results',.3);change('#query',{'textContent':'LIBRARY'},'letter cases',.5);move('#empty',{'opacity':0},'letter cases',.5);move('#match',{'opacity':1},'letter cases',.5)
  else:light('#match','readable results',.3)
 elif kind=='parts':
  for j,p in enumerate(['html','css','javascript']):light(f'#layer-{j}',p,.08+j*.25)
 elif kind=='prompt':
  for j,p in enumerate(['user should do','controls','test','fictional data']):move(f'#prompt-{j} rect',{'fill':'#0f655f'},p,.1+j*.2)
 elif kind=='versions':light('#version-1','first version',.1);light('#version-2','improvement',.28);move('#restore',{'rotation':-20,'transformOrigin':'50% 50%'},'keep both versions',.8)
 layout='layout-finale' if i==4 else 'layout-wide' if i in [1,2,3] else 'layout-split'
 css=CSS
 for variant in ["layout-wide","layout-finale"]:
  css=re.sub(r"\."+variant+r" ([^{}]+)\{([^{}]+)\}", lambda m: m[1]+"{"+m[2]+"}" if variant==layout else "", css)
 return f'''<template><div id="{cid}" data-composition-id="{cid}" data-start="0" data-duration="{b['window']}" data-width="1280" data-height="720" style="position:relative;width:100%;height:100%;overflow:hidden"><style>@font-face{{font-family:VUB;src:url('assets/source-sans-3-latin-400-normal.woff2')}}@font-face{{font-family:VUB;src:url('assets/source-sans-3-latin-700-normal.woff2');font-weight:700}}#{cid}{{font-family:VUB}}{css}</style><div class="canvas-ground"></div><div class="photo-window"><img class="topic-photo" src="assets/topic.webp" alt=""></div><div class="photo-shade"></div><div class="gold-divider"></div><h1 class="video-title">{E(TITLES[n][i])}</h1><div class="graphic-stage">{content}</div><p class="video-note">{E(note)}</p><div class="video-brand"><img src="assets/vub-seal.png" alt="">VUB Learning</div><script>const tl=gsap.timeline({{paused:true}});tl.fromTo("#{cid} .topic-photo",{{scale:1}},{{scale:1.07,duration:{b['window']},ease:"none"}},0);tl.fromTo("#{cid} .graphic-stage",{{opacity:1,y:10}},{{opacity:1,y:0,duration:.7,ease:"power2.out"}},0);{''.join(events)}window.__timelines["{cid}"]=tl;</script></div></template>'''
