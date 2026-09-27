"""Render the reusable course and its print materials from one curriculum source."""
import json,html,base64
from workshops import for_slide,workshop
import learning
import scenes as slide_scenes
import photo_scenes
from pathlib import Path
ROOT=Path('courses/digital-literacy-2'); BASE='/courses/digital-literacy-2'
C=json.loads(Path('scripts/dl2/curriculum.json').read_text()); W=C['weeks']; Q=json.loads((ROOT/'assets/questions.json').read_text())
def e(t): return html.escape(str(t),quote=True)
def link(path,label,cls=''):return f'<a class="{cls}" href="{BASE}/{path}">{e(label)}</a>'
def ul(items):return '<ul>'+''.join('<li>'+e(x)+'</li>' for x in items)+'</ul>'
def challenge_table(c):
 rows=''
 for k,(task,materials,_) in enumerate(c['tasks']):
  rating=''.join(f'<label><input type="radio" name="challenge-rating-{k}" value="{e(r)}"> {e(r)}</label>' for r in c['ratings'])
  rows+=f'<tr><td>{e(task)}</td><td>{e(materials)}</td><td><label class="visually-hidden" for="challenge-answer-{k}">What you did for task {k+1}</label><textarea class="worksheet-input" id="challenge-answer-{k}"></textarea><div class="print-answer"></div></td><td><fieldset class="rating"><legend class="visually-hidden">Instructor rating for task {k+1}</legend>{rating}</fieldset></td></tr>'
 return f'<p>{e(c["intro"])}</p><div class="table-scroll"><table class="challenge"><thead><tr><th>Task</th><th>Materials</th><th>What you did</th><th>Instructor rating</th></tr></thead><tbody>{rows}</tbody></table></div>'
def challenge_key(c):return '<p>Evidence to look for on each row:</p><ol>'+''.join(f'<li><strong>{e(task)}.</strong> {e(evidence)}</li>' for task,_,evidence in c['tasks'])+'</ol>'
def page(title,body,cls='doc',week=None,script='lesson.js',instructor=False):
 if script=='assessment.js':
  seal=base64.b64encode(Path('assets/vub-seal-white.png').read_bytes()).decode()
  body+=f'<template id="report-brand"><img class="report-seal" src="data:image/png;base64,{seal}" alt="WV Veterans Upward Bound seal"></template>'
 if cls!='lesson':body=learning.frame(body,instructor)
 return f'''<!doctype html>
<html lang="en"{' class="deck-page"' if cls=="lesson" else ''}><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="{e(title)} — practical VUB Digital Literacy Level 2 learning.">{'<meta name="robots" content="noindex">' if instructor else ''}<title>{e(title)} | VUB Learning</title><link rel="stylesheet" href="/shared/brand.css">{f'<link rel="stylesheet" href="{BASE}/assets/workshop.css"><link rel="stylesheet" href="{BASE}/assets/slide-scenes.css"><link rel="stylesheet" href="{BASE}/assets/deck.css">' if cls=="lesson" else f'<link rel="stylesheet" href="{BASE}/assets/course.css"><link rel="stylesheet" href="{BASE}/assets/workshop.css"><link rel="stylesheet" href="{BASE}/assets/learning-app.css">'}{('<style id="result-report-style">'+(ROOT/'assets/results-report.css').read_text()+'</style>') if script=='assessment.js' else ''}</head>
<body class="{cls}{' deck' if cls=='lesson' else ''}" {f'data-week="{week}"' if week else ''}>
{learning.CONTRACT}
{'' if cls=='lesson' else '<a class="skip" href="#main">Skip to content</a><header class="topbar"><a class="brand" href="/"><img src="/assets/vub-seal-white.png" alt=""><span>VUB Learning</span></a><span class="course-name">Digital Literacy · Level 2</span>'+link('index.html','Course home')+'</header><div class="brand-line"></div>'}
{body}
{'' if cls=='lesson' else '<footer class="footer">WV Veterans Upward Bound · Build technology confidence through practice.</footer>'}
<script src="/shared/progress.js"></script><script src="/shared/text-size.js"></script><script src="{BASE}/assets/{script}"></script><script src="{BASE}/assets/workshop.js"></script><script src="{BASE}/assets/learning-app.js"></script>{f'<script src="{BASE}/assets/slide-scenes.js"></script>' if cls=="lesson" else ""}</body></html>'''
def chapters(n,video_id):
 p=Path(f'video/digital-literacy-2/week-{n:02}/narration/beats.json')
 if not p.exists():return ''
 beats=json.loads(p.read_text())
 if not all('start' in b for b in beats):return ''
 demo_path=p.parent.parent/'screen-share-actions.json'
 demo_chapters={s['chapter'] for s in json.loads(demo_path.read_text())} if demo_path.exists() else set()
 items=''.join(f'<li><button type="button" data-video-seek="{b["start"]:.3f}"><time datetime="PT{b["start"]:.3f}S">{int(b["start"])//60}:{int(b["start"])%60:02}</time>{e(b["title"])}{(" · Screen demo" if i+1 in demo_chapters else "")}</button></li>' for i,b in enumerate(beats))
 return f'<details class="video-chapters"><summary>Choose a chapter or replay a skill</summary><nav aria-label="Video chapters" data-video-chapters="{video_id}"><p>Selecting a chapter pauses the video at that point. Use Play when you are ready.</p><ol>{items}</ol></nav></details>'
def write(path,text):p=ROOT/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text)
def doc(title,body,instructor=False):return page(title,f'<main class="page doc" id="main"><h1>{e(title)}</h1><div class="actions"><button type="button" data-print>Print / Save as PDF</button>{link("index.html","Course home","button secondary")}</div>{body}</main>',instructor=instructor)
PREP='Provide a workstation and headphones for each learner, this lesson and worksheet, a word processor and spreadsheet app. Use instructor-provided fictional accounts or a modeled demonstration for cloud tasks. Test the local video and printer destination before class. No paid service, real purchase or new learner account is required.'
def lab_card(rows,os='Windows 11'):
 if not rows:return ''
 body=''.join(f'<tr><td>{e(task)}</td><td>{e(steps)}</td></tr>' for task,steps in rows)
 note=' Windows 11 differences are in brackets.' if os!='Windows 11' else ''
 return f'<h2>Lab quick card: {e(os)}</h2><p>Click-by-click steps for this week’s tasks in {e(os)} with Microsoft Edge.{note} If your screen looks different, ask your instructor.</p><div class="table-scroll" role="region" tabindex="0" aria-label="Lab quick card"><table class="lab-card"><thead><tr><th scope="col">To do this</th><th scope="col">Steps</th></tr></thead><tbody>{body}</tbody></table></div>'
def run_sheet(w):
 units=[x for x in w['runsheet'] if x['kind']=='unit']
 body=f'<p class="run-intro">{e(w["summary"])} Every unit runs the same way: pose the problem, Tell, Show it live on the projector, every learner does it at their own seat, Review, then the next unit. Print this sheet; one unit fits one page. Minutes count from the start of class.</p>'
 body+='<h2>Today’s objectives</h2><ol class="run-objectives">'+''.join(f'<li><strong>{e(u["letter"])}. {e(u["objective"])}</strong> <span class="run-tested">{e(", ".join(u["tested"]))}</span></li>' for u in units)+'</ol>'
 body+='<p class="run-legend">Tested by: “post 1” is post-test item 1; “pre 1” is pre-test item 1; “IC3 1.4” is an objective group the tests leave out.</p>'
 t=0
 for x in w['runsheet']:
  span=f'minute {t}–{t+x["minutes"]} · {x["minutes"]} min';t+=x['minutes']
  if x['kind']=='block':
   body+=f'<section class="run-block"><h2>{e(x["phase"])} <span class="run-time">{span}</span></h2><p class="run-say"><strong>Say:</strong> {e(x["say"])}</p><ol>'+''.join(f'<li>{e(st)}</li>' for st in x['steps'])+'</ol>'+(f'<p class="run-slides">Slides {e(", ".join(str(k) for k in x["slides"]))}</p>' if x['slides'] else '')+'</section>'
  else:
   body+=f'<section class="run-unit"><h2>Cycle {e(x["letter"])}: {e(x["name"])} <span class="run-time">{span}</span></h2><p class="run-objective"><strong>Objective:</strong> {e(x["objective"])} <span class="run-tested">{e(", ".join(x["tested"]))}</span></p>'
   body+=f'<p class="run-say"><strong>Pose the problem:</strong> {e(x["problem"])}</p>'
   body+='<h3>Tell</h3><ul>'+''.join(f'<li>{e(l)}</li>' for l in x['tell'])+'</ul>'
   body+='<h3>Show <span class="run-note">(you, on the projector)</span></h3><ol>'+''.join(f'<li>{e(l)}</li>' for l in x['show'])+'</ol>'
   body+=f'<h3>Do <span class="run-note">(every learner, own seat)</span></h3><p>{e(x["do"])}</p>'
   body+='<h3>Review</h3><ul>'+''.join(f'<li>{e(l)}</li>' for l in x['review'])+'</ul>'
   body+=f'<p class="run-slides">Slides: {e(" → ".join(x["slides"]))}</p></section>'
 assert t==120
 return body
def typed(key,label):return f'<label class="visually-hidden" for="{key}">{e(label)}</label><textarea class="worksheet-input" id="{key}"></textarea><div class="print-answer"></div>'
# Week 6: the three practice pages (version 2 is the agent's result with one planted defect; see HANDOFF.md).
FINDER='activities/resource-finder'
def practice_versions():
 download=lambda path,name,which:f'<a class="button secondary" href="{BASE}/{path}" download="{name}">Download editable HTML<span class="visually-hidden"> of {which}</span></a>'
 groups=[('Version 1, before the agent',link(FINDER+'.html','Open version 1','button')+download(FINDER+'.html','resource-finder-v1.html','version 1')),
  ('Version 2, the agent’s result',link(FINDER+'-agent.html','Open the agent’s version','button')+download(FINDER+'-agent.html','resource-finder-v2.html','version 2')),
  ('Version 3, after the repair',link(FINDER+'-agent-fixed.html','Open the repaired version','button'))]
 return '<h2 class="no-print">The three practice pages</h2>'+''.join(f'<div class="actions" role="group" aria-label="{e(label)}">{buttons}</div>' for label,buttons in groups)
APP_TESTS=[('Happy path, new','type learning'),('Happy path, still works','type library'),('No match','type zzz'),('Mixed case','type LIBRARY, then Learning'),('Keyboard only','Tab through every control'),('Narrow screen','zoom to 400%')]
RETESTS=[('The check that failed','repeat it on version 3'),('Passed before: learning','type learning'),('Passed before: zzz','type zzz')]
def test_log(key,title,intro,rows):
 cols=[('Expected','Expected result'),('Actual','Actual result'),('Pass or fail','Pass or fail')]
 body=''.join(f'<tr><th scope="row">{e(check)}</th><td>{e(todo)}</td>'+''.join(f'<td>{typed(f"{key}-{r}-{c}",f"{label}: {check}")}</td>' for c,(_,label) in enumerate(cols))+'</tr>' for r,(check,todo) in enumerate(rows))
 head=''.join(f'<th scope="col">{e(x)}</th>' for x in ['Check','What to do']+[c for c,_ in cols])
 return f'<h2>{e(title)}</h2><p>{e(intro)}</p><div class="table-scroll" role="region" tabindex="0" aria-label="{e(title)}"><table class="test-log"><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>'
def rubric_table(rows):
 body=''.join(f'<tr><th scope="row">{e(c)}</th><td>{e(a)}</td><td>{e(b)}</td><td>{e(d)}</td><td>____</td></tr>' for c,a,b,d in rows)
 return f'<h2>Extension rubric</h2><p>Score each row 0, 1 or 2 using the descriptions. This {2*len(rows)}-point extension score is separate from the 28-point GS6 classroom assessment.</p><div class="table-scroll" role="region" tabindex="0" aria-label="Extension rubric"><table class="rubric"><thead><tr>'+''.join(f'<th scope="col">{x}</th>' for x in ['Criterion','0','1','2','Score'])+f'</tr></thead><tbody>{body}</tbody></table></div><p><strong>Total __ / {2*len(rows)}</strong></p>'
def glossary(words):
 if not words:return ''
 return '<section class="video-words" aria-labelledby="video-words-title"><h2 id="video-words-title">Words in this video</h2><dl>'+''.join(f'<dt>{e(t)}</dt><dd>{e(d)}</dd>' for t,d in words)+'</dl></section>'
def resources(n,instructor=False):
 p=f'weeks/week-{n:02}'
 staff=([(p+'/run-sheet.html','Instructor run sheet')] if W[n-1].get('runsheet') else [])+[(p+'/lesson-plan.html','Instructor lesson plan'),(p+'/answer-key.html','Worksheet answer guide')] if instructor else []
 return ''.join(link(x,y) for x,y in [(p+'/worksheet.html','Worksheet')]+staff+[(p+'/video-transcript.html','Video and transcript'),('syllabus.html','Syllabus'),('assessments/pre-test.html','Pre-test'),('assessments/post-test.html','Post-test')])
def exercise(s,n,i):
 k=s['kind']; prefix=f'w{n}s{i}'
 if k=='steps': return '<ol class="step-list interactive-steps">'+''.join('<li><button type="button" data-step-done aria-pressed="false"><span>'+e(x)+'</span><span class="step-state">Mark practiced</span></button></li>' for x in s['items'])+'</ol>'
 if k=='flip':return '<div class="flip-grid">'+''.join(f'<button class="flip" type="button" aria-expanded="false" aria-label="{e(a)}: reveal explanation"><span class="flip-inner"><span class="flip-front" aria-hidden="false">{e(a)}<span class="flip-hint">Select to reveal</span></span><span class="flip-back" aria-hidden="true">{e(b)}<span class="flip-hint">Select to turn back</span></span></span></button>' for a,b in s['cards'])+'</div>'
 if k=='check':return f'<div class="check-options" data-explanation="{e(s["why"])}">'+''.join(f'<button type="button" aria-pressed="false" data-correct="{str(j==s["answer"]).lower()}"><span class="kc-letter" aria-hidden="true">{"ABC"[j]}</span>{e(o)}</button>' for j,o in enumerate(s['options']))+'</div><p class="feedback" role="status"></p>'
 if k=='video':return f'<video poster="{(photo_scenes.PHOTO_ROOT+photo_scenes.PHOTOS[n][1]+".webp") if n!=5 else BASE+"/media/week-05-poster.webp"}" id="lesson-video" tabindex="0" controls preload="metadata" playsinline aria-label="Week {n} explainer"><source src="{BASE}/media/week-{n:02}.mp4" type="video/mp4"><track kind="captions" src="{BASE}/media/week-{n:02}.vtt" srclang="en" label="English" default></video><p class="video-caption">Captions are available in the player. {link(f"weeks/week-{n:02}/video-transcript.html","Read the full transcript")}.</p>'+chapters(n,"lesson-video")
 if k=='lab':return link(f'weeks/week-{n:02}/worksheet.html','Open the activity worksheet','button')
 if k=='assessment':return link(f'assessments/{s["href"]}-test.html','Open the '+s['href']+'-test','button')
 if k=='form':return '<form id="practice-form" class="exercise"><label for="practice-topic">Help topic (required)</label><select id="practice-topic" name="topic" required><option value="">Choose a topic</option><option>Finding a file</option><option>Using a calendar</option></select><label for="practice-method">Practice contact method (required)</label><select id="practice-method" name="method" required><option value="">Choose a method</option><option>Fictional email reply</option><option>Ask at the desk</option></select><div class="actions"><button type="submit">Review practice request</button><button type="reset" class="secondary">Reset practice form</button></div><p id="form-result" class="sim-status" role="status"></p></form>'
 if k=='permissions':return '<div class="exercise"><label for="permission">Alex needs to suggest wording. Choose access:</label><select id="permission"><option value="">Choose permission</option><option value="viewer">Viewer</option><option value="commenter">Commenter</option><option value="editor">Editor</option></select><p id="permission-result" class="sim-status" role="status">This simulation changes no real file access.</p></div>'
 if k=='spreadsheet':return '<div class="interactive-calc"><label for="paper-cost">Paper cost ($)</label><input id="paper-cost" type="number" min="0" step="1" value="12"><output id="budget-total" for="paper-cost" aria-live="polite">Total: $25.00</output></div><p class="small">Folders: $8 · Pens: $5. In a spreadsheet, enter the formula yourself.</p>'+link('assets/supplies.csv','Download the practice CSV','button secondary')
 if k=='starter':return '<div class="actions">'+link('activities/resource-finder.html','Open starter app','button')+f'<a class="button secondary" href="{BASE}/activities/resource-finder.html" download="resource-finder-v1.html">Download editable HTML</a></div>'
 return ''
# ── Deck templates: the same slide language as the Level 1 and Computer Skills decks ────────────────
import re as _re
ICONS={
 'zoom':'<circle cx="26" cy="26" r="15"/><path d="m37 37 15 15M20 26h12M26 20v12"/>',
 'sound':'<path d="M8 24h11l14-11v38L19 40H8zM42 22a12 12 0 0 1 0 20M49 15a21 21 0 0 1 0 34"/>',
 'print':'<path d="M18 22V8h28v14M14 22h36a4 4 0 0 1 4 4v18H10V26a4 4 0 0 1 4-4zM18 36h28v18H18z"/>',
 'calendar':'<rect x="8" y="12" width="48" height="44" rx="4"/><path d="M8 26h48M20 6v12M44 6v12M18 38h8m10 0h8M18 48h8"/>',
 'help':'<circle cx="32" cy="32" r="26"/><path d="M24 25a8 8 0 1 1 11 7c-2 1-3 3-3 5v2M32 47v1"/>',
 'undo':'<path d="M20 22h20a14 14 0 0 1 0 28H24M20 22l10-10M20 22l10 10"/>',
 'settings':'<circle cx="32" cy="32" r="9"/><path d="M32 4v8M32 52v8M4 32h8M52 32h8M12 12l6 6M46 46l6 6M12 52l6-6M46 18l6-6"/>',
 'screen':'<rect x="6" y="10" width="52" height="34" rx="3"/><path d="M32 44v12M20 56h24"/>',
 'file':'<path d="M14 6h24l12 12v40H14zM38 6v12h12M22 30h20M22 40h20M22 50h12"/>',
 'folder':'<path d="M6 18h20l6 7h26v29H6zM6 18v-8h18l6 7"/>',
 'message':'<rect x="6" y="12" width="52" height="40" rx="4"/><path d="m8 16 24 19 24-19"/>',
 'person':'<circle cx="32" cy="18" r="11"/><path d="M10 58v-9a22 22 0 0 1 44 0v9"/>',
 'people':'<circle cx="22" cy="20" r="9"/><circle cx="44" cy="24" r="7"/><path d="M4 56v-6a18 18 0 0 1 36 0v6M40 56v-5a14 14 0 0 1 20 0v5"/>',
 'check':'<circle cx="32" cy="32" r="26"/><path d="m18 33 9 9 19-20"/>',
 'cloud':'<path d="M17 50a13 13 0 0 1-2-26 18 18 0 0 1 35-2 14 14 0 0 1 1 28z"/>',
 'lock':'<rect x="12" y="28" width="40" height="30" rx="4"/><path d="M20 28V18a12 12 0 0 1 24 0v10M32 40v8"/>',
 'shield':'<path d="M32 4 54 14v16c0 15-11 25-22 30C21 55 10 45 10 30V14zM22 32l8 8 14-16"/>',
 'search':'<circle cx="27" cy="27" r="18"/><path d="m40 40 18 18"/>',
 'star':'<path d="m32 6 8 17 18 2-13 13 3 18-16-9-16 9 3-18L6 25l18-2z"/>',
 'link':'<path d="M26 38a10 10 0 0 0 14 0l10-10a10 10 0 0 0-14-14l-4 4M38 26a10 10 0 0 0-14 0L14 36a10 10 0 0 0 14 14l4-4"/>',
 'chart':'<path d="M8 56h48M14 48V30M28 48V18M42 48V26M56 48V12"/>',
 'photo':'<rect x="6" y="12" width="52" height="40" rx="3"/><circle cx="22" cy="26" r="5"/><path d="m6 46 16-14 12 10 8-7 16 15"/>',
 'video':'<rect x="6" y="14" width="38" height="36" rx="3"/><path d="m44 26 14-8v28l-14-8z"/>',
 'money':'<circle cx="32" cy="32" r="26"/><path d="M32 16v32M40 24c0-4-4-6-8-6s-8 2-8 6 4 6 8 6 8 2 8 6-4 6-8 6-8-2-8-6"/>',
 'keyboard':'<rect x="4" y="18" width="56" height="30" rx="3"/><path d="M12 28h4m6 0h4m6 0h4m6 0h4m6 0h4M12 38h4m6 0h20m6 0h4"/>',
 'usb':'<rect x="20" y="24" width="24" height="34" rx="3"/><path d="M26 24V8h12v16M30 12v8M34 12v8"/>',
 'wifi':'<path d="M6 24a38 38 0 0 1 52 0M14 34a26 26 0 0 1 36 0M22 44a14 14 0 0 1 20 0"/><circle cx="32" cy="52" r="3"/>',
 'lightbulb':'<path d="M22 44a16 16 0 1 1 20 0v6H22zM26 58h12"/>',
 'hand':'<path d="M16 34V16a4 4 0 0 1 8 0v14V9a4 4 0 0 1 8 0v20V8a4 4 0 0 1 8 0v22V14a4 4 0 0 1 8 0v26c0 12-6 18-18 18-6 0-11-4-15-9L6 40a5 5 0 0 1 7-7l6 7"/>',
 'app':'<rect x="8" y="8" width="48" height="48" rx="6"/><path d="M8 20h48M16 14h4M24 14h4"/>',
 'spark':'<path d="M32 6v12M32 46v12M6 32h12M46 32h12M14 14l8 8M42 42l8 8M14 50l8-8M42 22l8-8"/>',
}
KEY_ICONS=[(r'zoom|magnif|text size|readable|larger|bigger|display scal',r'zoom'),(r'sound|speaker|headset|headphone|volume|mute|audio',r'sound'),(r'print|printer|preview|toner|ink',r'print'),(r'calendar|appointment|event|reminder|week view|schedule',r'calendar'),(r'help|support|ask |request',r'help'),(r'undo|autocorrect|automatic|autocomplete|rule',r'undo'),(r'setting|scale|adjust|brightness|contrast',r'settings'),(r'password|encrypt|lock|secure|private|permission',r'lock'),(r'phish|scam|safe|verify|protect|catfish|trust',r'shield'),(r'search|find|filter|result',r'search'),(r'cloud|sync|online|account|service',r'cloud'),(r'email|message|send|recipient|subject|bcc|reply',r'message'),(r'partner|neighbor|reviewer|people|team|meeting|collaborat|share',r'people'),(r'folder|zip|save|file name|recycle',r'folder'),(r'file|document|handout|pdf|word|draft|version',r'file'),(r'chart|spreadsheet|formula|sum|total|cell',r'chart'),(r'photo|image|crop|picture',r'photo'),(r'video|clip|trim|caption',r'video'),(r'purchase|subscription|pay|price|cost|\$|money|trial',r'money'),(r'keyboard|shortcut|tab key|ctrl',r'keyboard'),(r'usb|drive|cable|hdmi|ethernet|port|connect',r'usb'),(r'network|wi-?fi|internet',r'wifi'),(r'app|website|browser|page|html|agent|spec|code',r'app'),(r'check|test|confirm|inspect|review|evidence',r'check')]
def icon(kind,cls='key-point-icon'):
 return f'<span class="{cls}" aria-hidden="true"><svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round">{ICONS.get(kind,ICONS["spark"])}</svg></span>'
def pick_icon(text,used):
 t=text.lower()
 for pat,k in KEY_ICONS:
  if _re.search(pat,t) and k not in used:return k
 for pat,k in KEY_ICONS:
  if _re.search(pat,t):return k
 return 'spark'
def sentences(body):
 parts=[x.strip() for x in _re.split(r'(?<=[.!?])\s+(?=[A-Z“"(])',body) if x.strip()]
 return parts or [body]
def key_points(body,kind_hint=''):
 """The teaching sentences as icon cards, the way the Level 1 decks present ideas."""
 items=sentences(body);used=[];out=''
 for t in items:
  k=pick_icon(t+' '+kind_hint,used);used.append(k)
  out+=f'<div class="key-point">{icon(k)}<div class="key-point-text">{e(t)}</div></div>'
 cols=' cols-3' if len(items)==3 else ' cols-2' if len(items)>=4 else ''
 return f'<div class="key-points{cols}">{out}</div>'
def header(s,i,sub=True):
 return f'<div class="slide-header"><h2 id="title-{i+1}" tabindex="-1">{e(s["title"])}</h2>'+(f'<p class="slide-subtitle">{e(s["body"])}</p>' if sub else '')+'</div>'
def two(left,right,wide=False):return f'<div class="two-column{" wide-right" if wide else ""}">{left}{right}</div>'
def chapters_for(w,slides):
 """Sidebar groups. Week 1 groups by teaching unit; other weeks by start, lesson and wrap-up."""
 titles=[s['title'] for s in slides];groups=[]
 units=[x for x in w.get('runsheet',[]) if x['kind']=='unit']
 if units:
  first=titles.index(units[0]['slides'][0]);groups.append(('Start here',list(range(first))))
  for u in units:groups.append((f'{u["letter"]} · {u["name"]}',[titles.index(t) for t in u['slides']]))
  last=max(groups[-1][1]);groups.append(('Wrap-up',list(range(last+1,len(slides)))))
  return groups
 wrap=len(slides)
 while wrap>1 and slides[wrap-1]['kind'] in ('lab','video','summary','complete','assessment'):wrap-=1
 first=0
 while first<wrap and slides[first]['kind'] in ('objectives','discussion','assessment'):first+=1
 return [('Start here',list(range(first))),('Lesson',list(range(first,wrap))),('Wrap-up',list(range(wrap,len(slides))))]
for w in W:
 n=w['n']; folder=f'weeks/week-{n:02}'
 slides=[dict(title=f'Week {n}: '+w['title'],body=w['summary'],kind='objectives')]+w['slides']+[dict(title='You completed this lesson',body='Name one thing you can now do and one next practice step. Revisit any slide when you need it.',kind='complete')]
 nav=''.join(f'<div class="chapter" role="group" aria-labelledby="ch-{n}-{g}"><div class="chapter-title" id="ch-{n}-{g}">{e(label)}</div><div class="chapter-slides">'+''.join(f'<button class="slide-link" type="button" data-slide="{i}" aria-current="false">{e(slides[i]["title"])}</button>' for i in idx)+'</div></div>' for g,(label,idx) in enumerate(chapters_for(w,slides)))
 sections=''
 for i,s in enumerate(slides):
  k=s['kind'];extra=''
  demo=photo_scenes.special(n,i+1) or for_slide(n,i+1) or slide_scenes.feature(n,i+1)
  photo=photo_scenes.photo(n,i+1,True) if (n,i+1)!=(5,3) else ''
  if k=='objectives':
   extra='title-slide'
   content=f'<div class="title-grid"><div class="title-copy"><img class="seal" src="/assets/vub-seal-white.png" alt=""><h2 id="title-{i+1}" tabindex="-1">{e(s["title"])}</h2><p class="slide-subtitle">{e(s["body"])}</p><p class="course-info">Week {n} of 6 · VUB Digital Literacy — Level 2</p></div><div class="title-panel"><h3>Today you will be able to</h3><ol>'+''.join(f'<li>{e(o)}</li>' for o in w['objectives'])+'</ol></div></div>'
  elif k=='complete':
   extra='completion-slide'
   cta=('<div class="actions">'+link(f'weeks/week-{n+1:02}/presentation.html','Continue to next week','button')+'</div>') if n<6 else '<div class="actions">'+link('index.html','Return to your course','button')+'</div>'
   content=f'<div class="completion-badge" aria-hidden="true"><img src="/assets/vub-seal-white.png" alt=""></div><h2 id="title-{i+1}" tabindex="-1">{e(s["title"])}</h2><p>{e(s["body"])}</p>{cta}'
  elif k=='summary':
   extra='summary-slide'
   content=header(s,i)+photo_scenes.evidence_board(n)
  elif k=='discussion':
   content=header(s,i,False)+two(photo,key_points(s['body'],'partner'),True)
  elif k=='assessment':
   content=header(s,i)+two(f'<div class="demo-box"><h3>{"Before we begin" if s["href"]=="pre" else "Show what you know"}</h3><p>28 questions · about 25 minutes · no time limit</p><div class="actions" style="justify-content:center">'+link(f'assessments/{s["href"]}-test.html','Open the '+s['href']+'-test','button')+'</div></div>',key_points('Complete your own assessment. Use the feedback to choose what to practice. Print or save your results.','check'))
  elif k=='steps':
   short=len(s['items'])<=3 and max(len(x) for x in s['items'])<=44
   content=header(s,i)+'<ol class="step-list interactive-steps'+(' cols-3' if short else '')+'">'+''.join('<li><button type="button" data-step-done aria-pressed="false"><span>'+e(x)+'</span><span class="step-state">Mark practiced</span></button></li>' for x in s['items'])+'</ol>'
   # One panel beside the steps: the illustrated record if there is one, else the practice window.
   content+=photo_scenes.supplement(n,i+1) or demo or ''
  elif k=='flip':
   content=header(s,i)+exercise(s,n,i)+(demo or '')
  elif k=='check':
   content=header(s,i,False)+f'<div class="knowledge-check"><p class="kc-question">{e(s["body"])}</p></div>'+exercise(s,n,i)+(photo_scenes.supplement(n,i+1) or demo or '')
  elif k=='video':
   content=header(s,i)+two('<div>'+exercise(s,n,i).replace('<details class="video-chapters">','<details class="video-chapters" open>').split('<details')[0]+'</div>','<div class="column"><details'+exercise(s,n,i).split('<details')[1].replace('class="video-chapters"','class="video-chapters" open',1)+'</div>',True)
  elif k=='lab':
   content=header(s,i)+two(f'<div class="demo-box"><h3>Your worksheet</h3><p>Work at your own seat. A partner checks your result.</p><div class="actions" style="justify-content:center">'+exercise(s,n,i)+'</div></div>',photo_scenes.evidence_board(n))
  elif k=='try':
   content=header(s,i,False)+f'<div class="handout-prompt">{icon("hand","handout-prompt-icon")}<div class="handout-prompt-text">{e(s["body"])}</div></div>'+(demo or key_points(s['body']))
  elif k in ('form','permissions','spreadsheet','starter','prompt'):
   content=header(s,i)+(two(f'<div class="column">{exercise(s,n,i)}</div>',demo) if demo and exercise(s,n,i) else (demo or f'<div class="column">{exercise(s,n,i)}</div>' or key_points(s['body'])))
  else:  # teach
   if demo and photo:content=header(s,i)+two(photo,demo,True)
   elif demo:content=header(s,i)+demo
   elif photo:content=header(s,i,False)+two(photo,key_points(s['body'],s['title']),True)
   else:content=header(s,i,False)+key_points(s['body'],s['title'])
  # One picture per slide: the illustrated side panel joins only slides that have no practice window or example.
  if k not in ('objectives','complete','try','steps','check') and not demo:content+=photo_scenes.supplement(n,i+1)
  sections+=f'<section class="slide slide-kind-{k} {extra} {"has-workshop" if demo else ""}" id="slide-{i+1}" aria-labelledby="title-{i+1}"><div class="slide-body">{content}</div></section>'
 body=f'<a class="skip" href="#main">Skip to content</a><aside class="sidebar" id="lesson-sidebar" aria-label="Lesson navigation"><a class="logo" href="{BASE}/index.html"><img src="/assets/vub-seal-white.png" alt=""><h2>VUB Digital Literacy</h2><p>Level 2 · IC3 GS6 Aligned</p></a><div class="week-indicator"><span class="week-num">Week {n}</span><span class="week-title">{e(w["title"])}</span></div><nav aria-label="Slides">{nav}</nav><nav class="resources" aria-label="Week resources">{resources(n)}</nav><div class="progress-section"><progress id="lesson-progress" value="1" max="{len(slides)}" aria-label="Lesson progress"></progress><p class="progress-text" id="progress-text"></p></div></aside><main class="main-content" id="main"><div class="ics-toolbar"><button type="button" class="menu-toggle" aria-expanded="false" aria-controls="lesson-sidebar">Show lesson navigation</button><a href="{BASE}/index.html">Digital Literacy Level 2 home</a><div class="toolbar-right"><div data-text-dock></div><button type="button" id="restart">Start over</button><button type="button" id="present" aria-keyshortcuts="P">Present (P)</button></div></div><div class="slides-container">{sections}</div><div class="nav-footer"><button type="button" class="nav-btn" id="previous">← Previous</button><span id="slide-counter" role="status"></span><button type="button" class="nav-btn" id="next">Next →</button><button type="button" class="nav-btn" id="present-exit" aria-keyshortcuts="Escape">Exit (Esc)</button></div></main>'
 write(folder+'/presentation.html',page(w['title'],body,'lesson',n))
 worksheet='<p>'+e(w['summary'])+'</p><p>Name or learner code: ____________________</p><p>Use fictional information. Work at your own workstation; a partner can check your result. Record what you actually observed. Type below or print a blank copy. Typed worksheet responses stay on this page only; print before closing.</p>'
 if n==6:worksheet+=practice_versions()+''.join(f'<h2>{e(t)}</h2><ol class="procedure">'+''.join('<li>'+e(x)+'</li>' for x in steps)+'</ol>' for t,steps in w['procedures'])
 for i,prompt in enumerate(w['lab']):worksheet+=f'<section class="question"><h2>{i+1}. {e(prompt)}</h2>'+(challenge_table(w['challenge']) if w.get('challenge',{}).get('item')==i else f'<label class="visually-hidden" for="answer-{i}">Response to activity {i+1}</label><textarea class="worksheet-input" id="answer-{i}"></textarea><div class="print-answer"></div>')+'</section>'
 if n==5:worksheet+='<div class="actions">'+link('assets/supplies.csv','Practice workbook data (fresh supplies.csv)','button secondary')+'</div>'
 if n==3:worksheet+='<div class="actions">'+link('assets/supplies.csv','Practice workbook data','button secondary')+link('assets/practice-photo.jpg','Practice photo (JPG)','button secondary')+'</div>'
 if n==6:worksheet+=test_log('log','App test log','Open the agent’s version (resource-finder-agent.html). For each check, write what you expect before you try it, then what actually happened, then pass or fail.',APP_TESTS)+test_log('retest','Retest after the repair','Open the repaired version (resource-finder-agent-fixed.html). Repeat the check that failed, then two checks that passed before.',RETESTS)
 if w.get('rubric'):worksheet+=rubric_table(w['rubric'])
 worksheet+=lab_card(w.get('lab_paths'),w.get('lab_os','Windows 11'))
 write(folder+'/worksheet.html',doc(f'Week {n} activity worksheet',worksheet))
 key='<p>Instructor guide. Accept equivalent evidence-based answers. These activities evaluate demonstrated skills, not speed.</p>'+''.join(f'<section class="question"><h2>{i+1}. {e(w["lab"][i])}</h2><p class="answer-model">{e(a)}</p>'+(challenge_key(w['challenge']) if w.get('challenge',{}).get('item')==i else '')+'</section>' for i,a in enumerate(w['answers']))
 if w.get('rubric'):key+=rubric_table(w['rubric'])
 write(folder+'/answer-key.html',doc(f'Week {n} worksheet answer guide',key,True))
 plan=f'<p>{e(w["summary"])}</p><h2>Learning outcomes</h2>{ul(w.get("outcomes",w["objectives"]))}<h2>Prepare the room</h2><p>{e(w.get("prep",PREP))}</p><p>For unavailable features, use the course simulation or role play and label the evidence as simulated.{" For week 6, the instructor runs an AI coding agent on the projector; learners need no account or AI access. Supply a plain-text editor for the optional hand repair." if n==6 else ""}</p><h2>Two-hour teaching plan</h2><table><thead><tr><th>Minutes from start</th><th>Phase</th><th>Instructor and learner actions</th></tr></thead><tbody>'
 time=0
 for minutes,phase,action in w['agenda']:
  plan+=f'<tr><td>{time}–{time+minutes} ({minutes} min)</td><td>{e(phase)}</td><td>{e(action)}</td></tr>';time+=minutes
 assert time==120
 video_use=('<h2>Using the video</h2><p>This week the instructor demonstrates every task live. The video repeats each task for home viewing; point learners to its chapters at the close. It pauses on a “Your turn” card after each practice prompt.</p>' if w.get('runsheet') else '<h2>Using the chaptered video</h2><p>Play each chapter inside its cycle, as the Show, from the video slide. Pause at the times named in the plan; the narration does not stop by itself. Ask learners to predict before a demonstration and explain the evidence afterward. Replay only the chapter needed for a refresher.</p>')
 plan+='</tbody></table>'+(f'<p><strong>Teach from the printed <a href="{BASE}/{folder}/run-sheet.html">run sheet</a></strong>: one page per unit with what to say, the exact clicks to show, the learner task and the review check.</p>' if w.get('runsheet') else '')+lab_card(w.get('lab_paths'),w.get('lab_os','Windows 11'))+video_use+'<h2>Facilitation and access</h2><p>Demonstrate slowly, then let learners try. Offer keyboard and mouse paths, captions and the written transcript. Print large copies if needed. Every learner works at their own workstation; a partner coaches but does not take over. Provide extra practice time without requiring learners to disclose a disability.</p><h2>Evidence to collect</h2>'+ul(w['lab'])+'<h2>Feedback and differentiation</h2><p>Ask the learner to explain a choice and demonstrate the result. Mark Independent, With prompt, or Needs practice. Re-model only the missing step. For faster learners, ask them to test an edge case or explain an alternative; do not add unrelated tasks.</p><h2>Materials and answers</h2><nav>'+resources(n,True)+'</nav><h2>Alignment</h2><p>GS6 Level 2 objective groups: '+e(', '.join(w['refs']))+'. The final week is a VUB extension.</p>'
 write(folder+'/lesson-plan.html',doc(f'Week {n} lesson plan: '+w['title'],plan,True))
 if w.get('runsheet'):write(folder+'/run-sheet.html',doc(f'Week {n} run sheet: '+w['title'],run_sheet(w),True))
 # Transcript is populated from final narration beats by the media builder.
 transcript=f'<p>{e(w["summary"])}</p><video {("poster="+chr(34)+photo_scenes.PHOTO_ROOT+photo_scenes.PHOTOS[n][1]+".webp"+chr(34)) if n!=5 else ""} id="transcript-video" tabindex="0" controls preload="metadata" aria-label="Week {n} explainer"><source src="{BASE}/media/week-{n:02}.mp4" type="video/mp4"><track kind="captions" src="{BASE}/media/week-{n:02}.vtt" srclang="en" label="English" default></video>'+chapters(n,"transcript-video")+glossary(w.get('glossary'))+'<div id="transcript-content">'
 beats=Path(f'video/digital-literacy-2/week-{n:02}/narration/beats.json')
 if beats.exists():
  demo_path=beats.parent.parent/'screen-share-actions.json'
  demos={s['chapter']:s for s in json.loads(demo_path.read_text())} if demo_path.exists() else {}
  for i,b in enumerate(json.loads(beats.read_text())):
   demo=demos.get(i+1)
   guide=('<details class="screen-demo-guide"><summary>Screen demonstration steps</summary><p>This is an original screen simulation with fictional practice data. Menus vary by application. Pause or replay each action before trying it yourself.</p><ol>'+''.join('<li>'+e(a['label'])+'</li>' for a in demo['actions'])+'</ol></details>') if demo else ''
   transcript+=f'<section><h2>{e(b["title"])}</h2><p>{e(b["text"])}</p>{guide}</section>'
 transcript+='</div><div class="actions">'+link(folder+'/presentation.html','Return to lesson','button')+'</div>'
 write(folder+'/video-transcript.html',doc(f'Week {n} explainer and transcript',transcript))
write('index.html',page(C['title'],learning.home(W,link),'course-home'))
dates=['September 28','October 5','October 12','October 19','October 26','November 2']
syll='<p><strong>WV Veterans Upward Bound · IC3 Digital Literacy GS6 Level 2 + AI Agent and SaaS Basics</strong></p><p><strong>Mondays, September 28–November 2, 2026 · 4:30–6:30 p.m. Eastern Time</strong><br>Six meetings · 12 contact hours · Computer lab instruction</p><p>For veterans who can use a mouse and keyboard, open a browser and manage basic files. Level 1 or equivalent experience is recommended. Ask the instructor for a refresher when needed.</p><h2>What you will be able to do</h2>'+ul([x for w in W for x in w['objectives']])+'<h2>Cohort schedule</h2><table><thead><tr><th>Meeting</th><th>Focus</th><th>Evidence of learning</th></tr></thead><tbody>'
for w,date in zip(W,dates):syll+=f'<tr><td>Week {w["n"]}<br>{date}, 2026<br>4:30–6:30 p.m.</td><td>{e(w["title"])}</td><td>{e(w["summary"])}'+(' Pre-test.' if w['n']==1 else ' Post-test and skills challenge.' if w['n']==5 else ' Spec, change review and test log.' if w['n']==6 else '')+'</td></tr>'
syll+='</tbody></table><p>The October 12 meeting is included as scheduled. Confirm building access with the program before that meeting.</p><h2>How we will learn</h2><p>Each meeting combines demonstration, a short captioned explainer, guided practice, a break, partner work and a check for understanding. Use fictional examples throughout. In the final week the instructor demonstrates an AI coding agent; learners write the request, review the change and test it, with no account or AI access of their own.</p><h2>Learning checks</h2><p>The pre-test occurs before instruction in week 1. The parallel post-test follows the GS6 lessons in week 5. Each has 28 questions, four per domain, and produces printable graded results. The week 6 prototype uses a separate 8-point rubric. Scores guide practice; they are not certification results.</p><h2>Materials and access</h2><p>Bring your willingness to practice. A workstation, browser, headphones, word processor, spreadsheet app and plain-text editor support the activities. Captions, transcripts, keyboard navigation, text sizing and print copies are available. No real purchases, private records or paid AI account are needed.</p><h2>Between meetings</h2><p>Optional: repeat one class task with fictional data and note where you need help. Save your worksheets and assessment results before leaving a shared computer.</p>'
write('syllabus.html',doc('Digital Literacy Level 2 syllabus',syll))
index='<p>All six lesson plans and the syllabus derive from the same curriculum source. Each plan totals 120 minutes. Dates appear only on the cohort syllabus.</p><h2>Before the course</h2><p>To teach from the projector, open the week’s slides and press P (or select Present on a projector). Slides fill the screen; a slide too tall for it shows its words first, then each visual, as you press Next. Press Esc to stop. Test playback, captions, print preview, software access and the lab printer. Provide fictional files and a demonstration account if collaboration features require sign-in. Rehearse the week 6 agent demo and open the three practice pages (versions 1, 2 and 3). Keep learner responses out of public repositories.</p><div class="overview-links">'+''.join(link(f'weeks/week-{w["n"]:02}/lesson-plan.html',f'Week {w["n"]}: {w["title"]}')+(link(f'weeks/week-{w["n"]:02}/run-sheet.html',f'Week {w["n"]} run sheet (print this)') if w.get('runsheet') else '') for w in W)+'</div><h2>Assessment kit</h2><div class="overview-links">'+''.join(link(f'assessments/{k}-test{suffix}.html',f'{k.title()}-test {label}') for k in ['pre','post'] for suffix,label in [('', 'browser assessment'),('-printable','paper copy'),('-answer-key','answer key')])+'</div><h2>Practical scoring</h2><p>Record task performance as Independent, With prompt or Needs practice. Use the worksheet answer guides for expected evidence. Keep practical observations separate from the 28-point knowledge score. Use the final worksheet’s 8-point app rubric for the extension.</p><h2>Local data and clearing</h2><p>Slide progress is stored in the browser. Assessment drafts and results stay in the current browser tab’s session storage until cleared or the tab session ends. They are not sent to an instructor automatically. Have learners print or download their results, then select Clear my assessment on shared computers. Before the first learner arrives and at the end of each session, select Start fresh on this computer on the course home to clear saved lessons and test answers.</p>'+link('sources.html','Research and objective alignment')
write('instructor-guide.html',doc('Instructor guide and lesson plans',index,True))
sources='<p>This is original VUB teaching material informed by the GS6 Level 2 framework. It uses no certification exam questions or copyrighted software screenshots. The additional week on guiding an AI coding agent is explicitly outside the GS6 Level 2 assessment score.</p><h2>Primary references</h2><ul><li><a href="https://certiport.pearsonvue.com/Certifications/IC3/Digital-Literacy-Certification/Certify/IC3-Global-Standard-6">Certiport: IC3 Global Standard 6</a> and its Level 2 objective-domain download.</li><li><a href="https://certiport.ccilearning.com/wp-content/uploads/2022/10/IC3_GS6_All_Levels_Exam_Domains.pdf">Certiport-authored objective domains, hosted by CCI Learning</a>, Level 2 pages 4–6. Used for the objective map; this is the accessible reference copy.</li><li><a href="https://support.microsoft.com/en-us/onedrive/restore-a-previous-version-of-a-file-stored-in-onedrive">Microsoft: restore previous OneDrive file versions</a>.</li><li><a href="https://consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams">FTC: recognize and avoid phishing</a>.</li><li><a href="https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API/Using_the_Web_Storage_API">MDN: browser storage</a>.</li></ul><h2>Teaching coverage</h2><p>Objective numbers below identify the framework groups taught. Lessons, simulations and worksheets provide practice across these groups; the 28-question classroom test samples each of the seven domains equally and is not a full certification readiness prediction.</p><table><thead><tr><th>Week</th><th>Objective groups</th><th>Practice evidence</th></tr></thead><tbody>'+''.join(f'<tr><td>{w["n"]}: {e(w["title"])}</td><td>{e(", ".join(w["refs"]))}</td><td>{e(w["summary"])}</td></tr>' for w in W)+'</tbody></table><h2>Assessment blueprint</h2><table><thead><tr><th>Domain</th><th>Pre / post items</th><th>Teaching week</th></tr></thead><tbody>'+''.join(f'<tr><td>{e(d)}</td><td>4 / 4</td><td>{", ".join(str(x) for x in sorted(set(q["week"] for q in Q["pre"] if q["domain"]==d)))}</td></tr>' for d in dict.fromkeys(q['domain'] for q in Q['pre']))+'</tbody></table><p>The worksheet answer guides include performance evidence for objectives beyond the quiz sample. Re-check vendor instructions when menus change; learning goals and lesson dates remain reusable.</p>'
sources+='<h2>Adult learning and deeper video lessons</h2><p>The chaptered videos connect skills to learner-chosen household and community tasks, model decisions, invite predictions, provide practice with feedback, and ask learners to transfer the routine. Accessibility and learner-controlled replay support different needs without assuming ability from age.</p><ul><li><a href="https://www.cdc.gov/training-development/php/about/develop-training-captivating-and-motivating-adult-learners.html">CDC: engaging adult learners</a>.</li><li><a href="https://www.w3.org/WAI/older-users/">W3C: older users and web accessibility</a>.</li><li><a href="https://support.microsoft.com/en-us/accessibility/word/make-your-word-documents-accessible-to-people-with-disabilities">Microsoft: accessible documents</a>.</li><li><a href="https://support.microsoft.com/en-us/excel/functions/sum-function">Microsoft: SUM and cell ranges</a>.</li><li><a href="https://support.google.com/drive/answer/2494822?hl=en">Google: file-sharing roles</a>.</li><li><a href="https://www.nist.gov/itl/smallbusinesscyber/guidance-topic/phishing">NIST: phishing guidance</a>.</li><li><a href="https://developer.mozilla.org/en-US/docs/Learn_web_development">MDN: learning web development</a>.</li></ul>'
write('sources.html',doc('Sources and curriculum alignment',sources))
for kind,questions in Q.items():
 title=kind.title()+'-test'
 version=3 if kind=='post' else 2
 write(f'assessments/{kind}-test.html',page(title,learning.assessment(kind,link),'assessment',script='assessment.js'))
 paper=f'<p>Assessment version {version} · Fictional practice scenarios</p><p>Name or learner code: ____________________</p><p>Read each situation and choose the one answer that best fits the task. Each correct answer earns one point. Total: 28. This is a classroom assessment, not a certification exam.</p>'
 key=f'<p>Assessment version {version}</p><p>One point per correct answer. Domain totals: four points each. Total: 28. Accept only the keyed choice for the knowledge score; use worksheet rubrics for demonstrated skills.</p>'
 for i,q in enumerate(questions):
  paper+=f'<section class="question"><h2>{i+1}. {e(q["question"])}</h2><ol type="A">'+''.join('<li>☐ '+e(o)+'</li>' for o in q['options'])+'</ol></section>'
  key+=f'<section class="question"><h2>{i+1}. {e(q["question"])}</h2><p><strong>{"ABC"[q["answer"]]}. {e(q["options"][q["answer"]])}</strong></p><p>{e(q["why"])}</p><p>Domain: {e(q["domain"])} · objective {e(q["objective"])} · week {q["week"]}</p></section>'
 write(f'assessments/{kind}-test-printable.html',doc(title+' printable assessment',paper))
 write(f'assessments/{kind}-test-answer-key.html',doc(title+' answer key',key,True))
# Catalog is the platform discovery source of truth.
p=Path('courses.json'); catalog=json.loads(p.read_text());catalog['courses']=[c for c in catalog['courses'] if c['id']!='digital-literacy-2']
catalog['courses'].append(dict(id='digital-literacy-2',title=C['title'],subtitle='Six practical weeks: IC3 GS6 Level 2, plus guiding an AI agent to build and test a web app.',type='weeks',progressKey='dl2',category='Digital Literacy',emphasis='Create, collaborate, build',path='courses/digital-literacy-2/',entry='courses/digital-literacy-2/index.html',preTest='courses/digital-literacy-2/assessments/pre-test.html',postTest='courses/digital-literacy-2/assessments/post-test.html',lessons=[dict(n=w['n'],title=w['title'],topic=w['summary'],path=f'courses/digital-literacy-2/weeks/week-{w["n"]:02}/presentation.html',statusKey=f'dl2:w{w["n"]}') for w in W]))
serialized=json.dumps(catalog,indent=2,ensure_ascii=False)
# Keep the catalog's existing compact lesson-row convention.
import re
serialized=re.sub(r'        \{\n          "n"[\s\S]*?\n        \}',lambda m:'        { '+', '.join(json.dumps(k)+': '+json.dumps(v) for k,v in json.loads(m.group()).items())+' }',serialized)
p.write_text(serialized+'\n')
print('Built',len(list(ROOT.rglob('*.html'))),'course pages')
