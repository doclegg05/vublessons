"""Original task diagrams. No product screenshots or external assets."""
from html import escape as e
from week2 import WEEK2
from week3 import WEEK3
def rows(items,active=0):
 return '<div class="visual-rows">'+''.join(f'<div class="visual-row {"visual-active" if i==active else ""}"><span>{e(a)}</span><b>{e(b)}</b></div>' for i,(a,b) in enumerate(items))+'</div>'
def visual(n,letter,step):
 if n==2 and letter=='A':
  # Text comes from the mission's own Show steps in week2.py, so the picture cannot drift from the lesson again.
  asked,answer,page=[value for _,value,_ in WEEK2['missions'][0]['show']]
  return rows([('Question',asked),('AI answer',answer if step>0 else 'Comes next'),('Library page',page if step>1 else 'Not opened yet')],step)
 if n==2 and letter=='B': return rows([('Name *','Alex · fictional'),('Topic *','[missing]' if step==1 else 'Computer help'),('Status','No request sent' if step==2 else 'Practice only')],step)
 if n==2 and letter=='C': return rows([('Documents','Community resources'),('File','library-help-v1.docx'),('Action',['Save → reopen','ZIP → extract','Recycle Bin → restore'][step])],step)
 if n==2 and letter=='D':return rows([('Reader','Viewer'),('Reviewer','Commenter'),('Coauthor','Editor')],step)
 if n==3:
  # Week 3 pictures read the mission's own Show steps from week3.py, so a slide cannot show one value and say another.
  show=WEEK3['missions'][ord(letter)-65]['show']
  if letter=='C':return '<div class="visual-photo '+('cropped' if step>0 else '')+'"><img src="/courses/digital-literacy-2/assets/practice-photo.jpg" alt="Two people reviewing a handout in the approved practice image"></div><div class="visual-caption">'+e(show[step][1])+'</div>'
  # Later steps stay hidden, as in Week 2's Mission A demo, so the picture never answers a prediction early.
  return rows([(label,value if j<=step else 'Comes next') for j,(label,value,_) in enumerate(show)],step)
 if n==4 and letter=='A':return rows([('To','Alex · needs to act'),('Cc','Sam · kept informed'),('Bcc','Volunteer addresses hidden')],step)
 if n==4 and letter=='B':return rows([('Comment','Add the desk location after Step 2.'),('Owner reply','Added, so visitors can find it.'),('Status','Resolved' if step==2 else 'Open for review')],step)
 if n==4 and letter=='C':return rows([('Microphone','Muted' if step!=1 else 'Unmuted to speak'),('Hand','Raised' if step==1 else 'Lowered'),('Captions','Available')],step)
 if n==4 and letter=='D':return rows([('Offer A · $5/month','3 months $15 · year $60'),('Offer B · yearly','$48 paid now'),('Before payment','Renewal + cancel + refund')],step)
 if n==5 and letter=='A':return rows([('Readable','Text size and position'),('Accessible','Captions and keyboard'),('Comfortable','Change position; quiet alerts')],step)
 if n==5 and letter=='B':return rows([('From','account-check.example'),('Subject','Act now to keep benefits'),('Request','Enter password')],step)
 if n==5 and letter=='C':return rows([('Camera permission','Only when needed'),('Encryption','Key required to read'),('Screen lock','Windows + L')],step)
 if n==5 and letter=='D':return rows([('Search + handout','Refine; real heading; numbered steps'),('Four costs','12 + 8 + 5 + 4 = 29'),('Recover + feedback','Undo; identify missing details')],step)
 if n==6 and letter=='A':return rows([('learning','2 resources expected'),('LIBRARY','1 resource expected'),('zzz','No matching resources expected')],step)
 if n==6 and letter=='B':return '<div class="visual-diff"><span>Requested addition</span><code>+ r.category</code><span>Unrequested removal</span><code>− .toLowerCase()</code><span>Prediction: capital-letter search fails</span></div>'
 if n==6 and letter=='C':return rows([('Version 2 · LIBRARY','Expected 1 / actual 0'),('Repair','Restore .toLowerCase()'),('Version 3 · Learning','Expected 2 / actual 2')],step)
 return rows([('Browser','Public page and interface'),('Server','Private key; access checks'),('Owner','Updates; cost; backup; support')],step)
