"""Run from repo root: python3 scripts/dl2/mission-control/build.py.
Owns Week 1 deck from week-01.html plus Weeks 2–6 materials and practice libraries.
Does not write assessments, video/transcript, catalogue or email delivery.
"""
import json,html,re
from pathlib import Path
from content import WEEKS
from visuals import visual
from opening import video_slide, media_url
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
BASE='/courses/digital-literacy-2'
OUT=ROOT/'courses/digital-literacy-2'
OLD=json.loads((ROOT/'scripts/dl2/curriculum.json').read_text())['weeks']
def e(t):return html.escape(str(t),quote=True)
def link(url,label):return f'<a href="{url}">{e(label)}</a>'
def ul(xs):return '<ul>'+''.join(f'<li>{e(x)}</li>' for x in xs)+'</ul>'
def letterhead(n):return f'<header class="letterhead"><div class="lh-bar" aria-hidden="true"></div><img class="lh-seal" src="{BASE}/os/img/vub-seal-360.png" alt="Veterans Upward Bound seal"><div class="lh-org"><div class="lh-state">WEST VIRGINIA</div><div class="lh-name">Veterans Upward Bound</div><div class="lh-trio">A TRIO program funded by the U.S. Department of Education</div></div><dl class="lh-meta"><div><dt>Course</dt><dd>Digital Literacy Level 2</dd></div><div><dt>Week</dt><dd>{n} of 6</dd></div><div><dt>Instructor</dt><dd>Britt Legg</dd></div></dl><div class="lh-rule" aria-hidden="true"></div></header>'
def paper(n,title,body,private=False):
 return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Week {n} · {e(title)} · VUB</title>{'<meta name="robots" content="noindex">' if private else ''}<link rel="stylesheet" href="{BASE}/os/fonts.css"><link rel="stylesheet" href="{BASE}/os/paper.css"><link rel="stylesheet" href="{BASE}/os/mission-paper.css"></head><body class="mission-paper{" run-sheet" if title == "Instructor run sheet" else ""}"><nav class="paper-actions no-print" aria-label="Week resources"><button type="button" data-print>Print / Save as PDF</button>{link('presentation.html#1','Lesson')}{link('worksheet.html','Worksheet')}{link('practice.html','Practice library')}{link(BASE+'/index.html','Course home')}</nav><main class="paper-doc">{letterhead(n)}<h1>Week {n} · {e(title)}</h1>{body}</main><script src="{BASE}/os/mission-paper.js"></script><script src="/shared/text-size.js"></script></body></html>'''
def response(id,label):return f'<label for="{id}">{e(label)}</label><textarea class="worksheet-input" id="{id}" rows="3"></textarea><div class="print-answer"></div>'
def source_text(t):
 t=re.sub(r'[Ss]lide (\d+)',r'practice library exercise \1',t)
 t=t.replace('Print page 1 of your results or save it as a PDF, and write your score out of 20.','Submit your results to Britt, save the complete graded PDF, and write your score out of 20.')
 return t
# Map all eight detailed task rows to the mission where they are taught.
WEEKS[6]['missions'][1]['lab']=[2,3]
WEEKS[6]['missions'][2]['lab']=[4,5,6]
WEEKS[6]['missions'][3]['lab']=[7]
def log_table(prefix):
 checks=[('New category','learning'),('Existing name','library'),('No match','zzz'),('Mixed case','LIBRARY, then Learning'),('Keyboard only','Tab through controls'),('Narrow screen','Zoom to 400%')]
 out='<div class="table-scroll" tabindex="0" role="region" aria-label="App test log"><table><thead><tr><th>Check / input</th><th>Expected</th><th>Actual</th><th>Pass or fail</th></tr></thead><tbody>'
 for i,(label,value) in enumerate(checks):
  out+=f'<tr><th scope="row">{label}<br>{value}</th>'+''.join(f'<td>{response(f"{prefix}-{i}-{j}",f"{name}: {label}")}</td>' for j,name in enumerate(['Expected result','Actual result','Pass or fail']))+'</tr>'
 return out+'</tbody></table></div>'
def app_links():return '<nav class="resource-links" aria-label="Three practice versions">'+''.join(link(BASE+'/activities/resource-finder'+suffix+'.html',label) for suffix,label in [('', 'Open version 1'),('-agent','Open the agent’s version'),('-agent-fixed','Open the repaired version')])+'</nav><p><a href="'+BASE+'/activities/resource-finder.html" download="resource-finder-v1.html">Download editable HTML: version 1</a> · <a href="'+BASE+'/activities/resource-finder-agent.html" download="resource-finder-v2.html">Download editable HTML: version 2</a></p>'
def slide(n,i,title,body,phase='present',stage='',notes='',cls=''):
 return f'<section class="slide {cls}" id="slide-{i}" data-phase="{phase}" data-stage="{stage}" data-scene="deck" aria-labelledby="s{i}"><div class="panel full"><div class="hud"><img src="/assets/vub-seal-white.png" alt=""><span>Week {n}</span><span class="app">Mission Control</span></div><h1 id="s{i}" tabindex="-1">{e(title)}</h1>{body}</div><aside class="notes"><h2>{e(title)}</h2><p>{e(notes)}</p></aside></section>'
for n,w in WEEKS.items():
 target=OUT/f'weeks/week-{n:02}';old=OLD[n-1];slides=[video_slide(n,1)];schedule=[]
 def add(title,body,phase='present',stage='',notes='',cls=''):
  slides.append(slide(n,len(slides)+1,title,body,phase,stage,notes,cls));return len(slides)
 photo=f'{BASE}/assets/photos/{w["photo"]}.webp'
 add(w['title'],f'<div class="mission-hero"><div><p>Digital Literacy Level 2</p><p>Four missions. One useful result.</p><a class="mission-link" href="worksheet.html">Open your mission worksheet</a></div><figure><img src="{photo}" alt="Illustrative West Virginia learning scenario"><figcaption>Fictional people and setting</figcaption></figure></div>','warm-up',notes='Welcome learners by name. This lesson uses fictional examples and existing tools. Open the worksheet before demonstrations. F toggles fullscreen; N shows notes. Arrow keys progress through shows before advancing slides.')
 add('Start with what you know.',f'<p class="mission-prompt">{e(w["warm"])}</p><p>Share one experience. Passing is welcome.</p>','warm-up',notes='3 minutes including the welcome, after the 8-minute opening video. Invite a real example without asking for private account or benefits details. Connect existing experience to today’s task.')
 add('Your four missions.', '<ol class="mission-map">'+''.join(f'<li><b>{chr(65+i)}</b><span>{e(m["title"])}</span></li>' for i,m in enumerate(w['missions']))+'</ol><p>Tell → Show → Do → Review</p>','intro',notes='2 minutes. Preview the task sequence and success evidence. Use prepared examples if software or accounts are unavailable. The break is protected; optional extensions can wait.')
 elapsed=13
 schedule=[(0,8,'Opening video','1'),(8,11,'Welcome and experience','2–3'),(11,13,'Mission overview','4')]
 for k,m in enumerate(w['missions']):
  letter=chr(65+k);mid=f'{n}{letter}';first=len(slides)+1
  add(m['title'], '<ol class="mission-principles">'+''.join(f'<li><span>{i+1}</span>{e(t)}</li>' for i,t in enumerate(m['tell']))+'</ol>',stage='tell',notes=f'Mission {mid}. App: {m["app"]}. Explain why this helps: {m["finish"]}. Connect to the learner’s own household or community task. Ask for a prediction before the show. Full procedural steps and expected evidence are in the worksheet and answer guide.')
  states=''.join(f'<div class="mission-state" data-state="{j}" {"hidden" if j else ""}><div class="demo-artifact artifact-{n}-{letter}"><span class="demo-app">{e(m["app"])} · fictional demonstration</span><strong>{e(heading)}</strong><div data-visual>{visual(n,letter,j)}</div><div class="artifact-path" aria-hidden="true"><span>Observe</span><i>→</i><span>Act</span><i>→</i><span>Check</span></div></div><p class="demo-explanation">{e(explanation)}</p></div>' for j,(heading,value,explanation) in enumerate(m['show']))
  add('Watch: '+m['title'].lower(),f'<div class="mission-demo" data-mission-demo>{states}<div class="mission-demo-controls"><button type="button" data-demo-back>Previous step</button><output aria-live="polite" class="demo-count">Step 1 of 3</output><button type="button" data-demo-next>Next step</button><button type="button" data-demo-reset>Replay</button></div></div>',stage='show',notes=f'App: {m["app"]}. Advance each state deliberately. Read the visible result aloud, then ask why it matters. No automatic advance. Select Next step or use the deck arrow; Replay starts again. This original diagram is a teaching model; the practice library holds the detailed interactive computer simulations.')
  add('Your turn: Mission '+mid,f'<div class="mission-ab"><div><b>Point A</b><p>{e(m["start"])}</p></div><div><b>Point B</b><p>{e(m["finish"])}</p></div></div><ol class="mission-do">'+''.join(f'<li>{e(s)}</li>' for s in m['do'])+f'</ol><div class="mission-actions">{link(f"worksheet.html#m{mid}","Open step-by-step worksheet")}{link(f"practice.html#slide-{m['practice']}","Open interactive practice")}</div>','practice','do',f'App: {m["app"]}. Worksheet {mid}; practice library exercise {m["practice"]}. Let learners act at their seats. Offer the quick card first, then a prompt, then a demonstration. Account-free fallback: use the practice library and write the predicted/observed result. Paper fallback: narrate actions and annotate the model; record that it was simulated. Do not count a paper prediction as an observed software skill.')
  add(m['question'],f'<div class="mission-check" data-answer="{m["answer"]}" data-why="{e(m["why"])}">'+''.join(f'<button type="button" data-choice="{j}"><b>{chr(65+j)}</b> {e(choice)}</button>' for j,choice in enumerate(m['choices']))+'<p class="mission-feedback" role="status">Choose an answer, then explain your reason.</p><button type="button" class="check-reset">Try again</button></div>','evaluate','review',f'Ask everyone to choose before selecting an answer. Correct answer: {m["choices"][m["answer"]]}. {m["why"]} Check the actual Point B evidence, not simply completion of a click. Misconception to address: the other options may look convenient but do not accomplish the stated task.')
  for si in range(first-1,len(slides)):
   slides[si]=slides[si].replace('<span class="app">Mission Control</span>', '<span class="app">'+e(m['app'])+'</span>')
  duration=w['minutes'][2+k+(1 if k>1 else 0)]
  schedule.append((elapsed,elapsed+duration,f'Mission {mid} · {m["title"]}',f'{first}–{len(slides)}'));elapsed+=duration
  if k==1:
   add('Pause. Reset. Come back ready.','<p class="mission-prompt">Take an 8-minute break.</p><p>Save your work. Rest your eyes. Change position.</p><p>When you return, open Mission '+str(n)+'C.</p>','practice',notes='Protected 8-minute break. Do not use it for catch-up instruction. Allow learners to step away. No countdown or automatic advancing; instructor resumes when the group is ready.')
   schedule.append((elapsed,elapsed+8,'Protected break',str(len(slides))));elapsed+=8
 eval_start=len(slides)+1
 if n==5:
  add('Show your progress.',f'<p>Take the 20-question post-test on your own.</p><p>Submit to Britt and save your complete graded PDF.</p><a class="mission-link" href="{BASE}/assessments/post-test.html">Open the post-test</a>','evaluate',notes='22 minutes. Use the existing 20-question post-test, separate from five-task observations. No coaching during the test. Check the submission status and saved PDF. A saved PDF is not proof of online submission. Classroom results do not award certification.')
 else:
  add('Show the evidence.',f'<p class="mission-prompt">{e(w["apply"])}</p><p>Explain one choice. Show one result. Name your next step.</p>','evaluate',notes='Ask each learner for observable evidence using the answer guide. Record independent, prompted or simulated work accurately. Optional extensions wait if core evidence is unfinished. Week 6 uses its separate 8-point extension rubric, not the IC3 test score.')
 schedule.append((elapsed,elapsed+w['minutes'][-2],'Individual check' if n!=5 else 'Individual post-test',str(eval_start)));elapsed+=w['minutes'][-2]
 add('Take one useful thing home.',f'<p class="mission-prompt">{e(w["apply"])}</p><div class="mission-actions">{link("video-transcript.html","Replay a teaching video chapter")}{link("worksheet.html","Keep your completed worksheet")}</div>','apply',notes='Invite one specific transfer task, such as finding a service, saving a handout or checking a suspicious message. Do not require anyone to reveal personal information. Videos are optional replay resources; no additional viewing time is silently added to the 120-minute lesson.')
 add('Mission complete.',f'<p>You practiced. You checked. You can explain your choices.</p><div class="mission-actions">{link(BASE+"/index.html","Return to course home")}{link("practice.html","Practice a skill again")}</div>','apply',notes='Collect evidence, not just self-reported confidence. Celebrate a concrete improvement. Close applications and restore shared settings. Keep support needs separate from assessment results.')
 schedule.append((elapsed,120,'Transfer and close',f'{len(slides)-1}–{len(slides)}'))
 assert elapsed+w['minutes'][-1]==120,(n,elapsed,w['minutes'])
 head=f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Week {n} · {e(w["title"])} · VUB</title><link rel="stylesheet" href="{BASE}/os/fonts.css"><link rel="stylesheet" href="{BASE}/os/deck.css"><link rel="stylesheet" href="{BASE}/os/missions.css"><link rel="stylesheet" href="{BASE}/os/opening.css"></head>'
 nav='<nav class="mission-toolbar" aria-label="Presentation controls">'+link(BASE+'/index.html','Course home')+'<button type="button" data-deck-prev>Back</button><button type="button" data-deck-next>Next</button><button type="button" data-deck-notes aria-expanded="false">Notes (N)</button><button type="button" data-deck-full>Fullscreen (F)</button><label>Mission <select data-mission-jump><option value="0">Start</option>'+''.join(f'<option value="{4+k*4+(1 if k>1 else 0)}">{chr(65+k)} · {e(m["title"])}</option>' for k,m in enumerate(w['missions']))+'</select></label></nav>'
 (target/'presentation.html').write_text(head+f'<body class="dl2-os mission-series"><a class="mission-skip" href="#main">Skip to lesson</a>{nav}<main id="main" tabindex="-1" data-deck-version="opening-v1" class="deck" aria-label="Week {n} presentation">'+''.join(slides)+f'</main><script src="{BASE}/os/deck.js"></script><script src="{BASE}/os/missions.js"></script><script src="/shared/text-size.js"></script></body></html>')
 # Keep existing interactive simulations and their stable exercise numbers available as a companion library.
 practice=(HERE/f'practice/week-{n:02}.html').read_text().replace('</head>',f'<link rel="stylesheet" href="{BASE}/os/mission-practice.css"></head>')
 # Derive media URL versions and chapter times from approved artifacts on every build.
 for suffix in ('mp4','vtt'):
  path=f'courses/digital-literacy-2/media/week-{n:02}.{suffix}'
  practice=re.sub(re.escape('/'+path)+r'(?:\?[^"\s]*)?',lambda _:media_url(path),practice)
 chapter_times=iter(json.loads((OUT/f'media/week-{n:02}-chapters.json').read_text()))
 def chapter_time(match):
  seconds=next(chapter_times)['startSeconds']
  return f'{match[1]}{seconds:.3f}{match[2]}{seconds:.3f}{match[3]}{int(seconds)//60}:{int(seconds)%60:02}{match[4]}'
 practice=re.sub(r'(data-video-seek=")[\d.]+("><time datetime="PT)[\d.]+(S">)\d+:\d+(</time>)',chapter_time,practice)
 practice=practice.replace('<body class="lesson"', '<body class="lesson mission-library"')
 practice=practice.replace('<title>', '<title>Practice library · ',1)
 practice=practice.replace('<div class="deck-toolbar">', '<div class="deck-toolbar">'+link('presentation.html#1','Return to Mission Control'))
 (target/'practice.html').write_text(practice)
 # Aligned paper materials: each detailed task appears under its teaching mission.
 worksheet='<p>Use fictional details. No new account, payment or real message is required. Work in the app when available; otherwise use the practice library or annotate the paper model. Tell your instructor which route you used.</p>'
 if n==6:
  worksheet+=app_links()+'<h2>Before you begin</h2>'+''.join('<h3>'+e(title)+'</h3><ol>'+''.join('<li>'+e(source_text(step))+'</li>' for step in steps)+'</ol>' for title,steps in old['procedures'])
 worksheet+='<div class="namerow"><span>Name</span><span>Workstation</span></div>'
 answer='<p>Assess observable evidence. A spoken prompt is “With prompt”; using the quick card alone can be independent. Mark simulated work separately from hands-on performance. These observations do not change assessment scores.</p>'
 for k,m in enumerate(w['missions']):
  mid=f'{n}{chr(65+k)}';worksheet+=f'<section class="mission" id="m{mid}"><h2>Mission {mid} · {e(m["title"])}</h2><div class="mission-ab"><div><b>Point A</b><p>{e(m["start"])}</p></div><div><b>Point B</b><p>{e(m["finish"])}</p></div></div><p><b>App:</b> {e(m["app"])} · '+link(f'practice.html#slide-{m["practice"]}','Interactive practice')+'</p><ol>'
  answer+=f'<section><h2>Mission {mid} · {e(m["title"])}</h2><ol>'
  for idx in m['lab']:
   worksheet+=f'<li>{e(source_text(old["lab"][idx]))}</li>'
   answer+=f'<li>{e(source_text(old["answers"][idx]).replace('Page 1 printed or saved','Complete PDF saved or printed'))}</li>'
  worksheet+='</ol>'+response('evidence-'+mid,'What you tried, what happened, and how you checked it')+'<p>Route used: app / simulation / paper · Support: independent / with prompt / needs practice</p></section>'
  answer+=f'</ol><p><b>Review:</b> {e(m["why"])}</p></section>'
 if n==3:
  worksheet+='<h2>Resource pack downloads</h2><p>'+link(BASE+'/assets/supplies.csv','Fresh supplies.csv')+' · '+link(BASE+'/assets/practice-photo.jpg','Approved practice photo')+'</p><p>Photo: VUB practice photo, used with permission. Essential: structured handout, tracked decision, recalculating workbook, three simple slides with crop/alt text/credit, checked PDF. Optional: chart, extra slide decoration and advanced video editing. The local trim/split model is the account-free media activity.</p>'
 if n==5:
  c=old['challenge'];worksheet+='<h2>Five-task observation</h2><p>'+e(c['intro'])+'</p><ol>'+''.join('<li><b>'+e(t)+'</b> '+e(materials)+response('challenge-answer-'+str(i),'Evidence for '+t)+'<fieldset><legend>Instructor rating: '+e(t)+'</legend>'+''.join(f'<label><input type="radio" name="challenge-rating-{i}" value="{e(r)}"> {e(r)}</label>' for r in c['ratings'])+'</fieldset>'+'</li>' for i,(t,materials,_) in enumerate(c['tasks']))+'</ol><p>Quick card allowed. Spoken prompt = With prompt. Keep the five observations separate from the 20-question post-test. Save the complete graded PDF and check submission status.</p>'
  answer+='<h2>Five-task observation evidence</h2>'+ul([t+': '+evidence for t,_,evidence in c['tasks']])
 if n==6:
  worksheet+='<h2>Three versions, one controlled experiment</h2>'+app_links()+'<h2>Version 2 app test log</h2>'+log_table('log')+'<h2>Version 3 retest log</h2>'+log_table('retest')
  answer+=app_links()+'<h2>Expected outcomes</h2><p>Version 1: LIBRARY finds one; learning finds none. Version 2: learning finds two, library one, zzz none; LIBRARY and Learning incorrectly find none. Version 3: LIBRARY finds one, Learning and learning two, zzz none. Test keyboard and narrow layout on each.</p>'
  rubric='<h2>Separate extension rubric · 8 points</h2><div class="table-scroll"><table><thead><tr><th>Criterion</th><th>0</th><th>1</th><th>2</th><th>Score</th></tr></thead><tbody>'+''.join('<tr>'+''.join(f'<td>{e(x)}</td>' for x in row)+'<td>__ / 2</td></tr>' for row in old['rubric'])+'</tbody></table></div><p>Total __ / 8. This extension rubric is separate from the pre/post tests.</p>'
  worksheet+=rubric;answer+=rubric
 quick='<h2>Lab quick card: Windows 11</h2><dl class="quick-card">'+''.join(f'<dt>{e(a)}</dt><dd>{e(b)}</dd>' for a,b in old['lab_paths'])+'</dl>'
 worksheet+=quick;answer+='<p>For the exact learner procedures, use the matching worksheet and quick card.</p>'
 (target/'worksheet.html').write_text(paper(n,'Mission worksheet',worksheet))
 (target/'answer-key.html').write_text(paper(n,'Answer and observation guide',answer,True))
 table='<table><thead><tr><th>Elapsed minutes</th><th>Slides</th><th>Teaching segment</th></tr></thead><tbody>'+''.join(f'<tr><td>{a}–{b} ({b-a} min)</td><td>{s}</td><td>{e(t)}</td></tr>' for a,b,t,s in schedule)+'</tbody></table>'
 prep='<p>Before class: print worksheet and answer guide; open the lesson and practice library; check projector, keyboard, sound and printer; provide fresh fictional files. Play the opening video in the first 8 minutes; welcome, prior experience and mission overview share the next 5 minutes. Use later chapter replay only as needed. No learner account or purchase is required.</p>'
 plan='<h2>Objectives</h2>'+ul(old['objectives'])+'<h2>Observable outcomes</h2>'+ul(old['outcomes'])+'<h2>120-minute plan</h2>'+table+prep+'<h2>Teaching rhythm</h2><p>Tell: explain the purpose using prior experience. Show: ask for a prediction and demonstrate one step at a time. Do: learners act at their own seats using the quick card. Review: explain choices and inspect evidence. Use N for slide-specific instructor notes and the answer guide for expected results.</p><h2>Pacing and recovery</h2><p>Protect the 8-minute break. Finish each essential Point B before optional extensions. Offer prepared examples, partner observation and paper annotation when tools are unavailable; record these as simulated work. Use the closing block for consolidation, not a new task.</p>'
 if n==3:plan+='<p>Week 3 is deliberately sequential: 27 minutes Word, 22 Excel, break, 20 PowerPoint, 16 export/media. Use the supplied starter wording and fresh CSV. Charts, extra decoration and advanced video editing are optional. If a learner falls behind, provide the completed prior artifact so the next objective can still be practiced.</p>'
 if n==5:plan+='<p>Mission 5D is a 26-minute observed skills challenge. The following 22 minutes belong to the individual 20-question post-test. Keep observation ratings and test scores separate. Use a paper test if the browser cannot load; keep the complete result as the backup.</p>'
 if n==6:plan+='<p>Use the prepared three-version resource finder by default. No live AI account is needed. Optional instructor-led live generation must use fictional data and show the diff before accepting a change. The extension is spec → prediction → review → test → repair → retest, not a free-form website prompt.</p>'
 plan+=quick+'<h2>Week-specific preparation</h2><p>'+e(old['prep'] if n!=6 else 'Provide Edge, headphones, worksheet, the three prepared app versions and a plain-text editor for the optional hand repair. An instructor-led live AI run is optional; the prepared versions provide the complete account-free route. Rehearse the diff and each acceptance check, test captions and sound, then select Start fresh on this computer.')+'</p>'
 plan+='<h2>Instructor support</h2><p>'+link(f'{BASE}/weeks/week-{n:02}/answer-key.html','Answer and observation guide')+' · '+link('run-sheet.html','Run sheet')+' · '+link('instructor-notes.html','All slide notes')+'</p>'
 (target/'lesson-plan.html').write_text(paper(n,'Lesson plan',plan,True))
 (target/'run-sheet.html').write_text(paper(n,'Instructor run sheet',table+prep+'<p><b>Keys:</b> arrows / Page Up / Page Down · F fullscreen · N notes · B blackout · number + Enter jumps. Use the mission chooser for A–D. The phase buttons jump to the first instance of that teaching phase.</p><p>Core route: four missions, protected break, individual evidence, transfer. Reference the answer guide for success criteria; the worksheet contains the click-by-click quick card.</p>',True))
 notes=''.join(f'<section><h2>Slide {i+1}</h2>'+re.search(r'<aside class="notes">(.*?)</aside>',s).group(1)+'</section>' for i,s in enumerate(slides))
 (target/'instructor-notes.html').write_text(paper(n,'Instructor notes',notes,True))
 print(f'Week {n}: {len(slides)} slides, 4 matched missions, 120 minutes')

(OUT/'weeks/week-01/presentation.html').write_text((HERE/'week-01.html').read_text().replace('<!-- OPENING_MEDIA -->',video_slide(1,2)))
print('Week 1: 28 slides; pre-test, video, existing lesson')
