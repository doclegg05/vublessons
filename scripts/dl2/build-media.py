"""Build reusable HyperFrames sources, matched caption tracks and media provenance."""
import json,html,shutil,textwrap,sys,importlib.util
from pathlib import Path
spec=importlib.util.spec_from_file_location("video_scenes",Path(__file__).with_name("video-scenes.py"));visuals=importlib.util.module_from_spec(spec);spec.loader.exec_module(visuals)
from pathlib import Path
root=Path('video/digital-literacy-2');public=Path('courses/digital-literacy-2/media');public.mkdir(exist_ok=True)
esc=lambda s:html.escape(str(s),quote=True)
def stamp(sec,sep='.'):
 ms=round(sec*1000);h,ms=divmod(ms,3600000);m,ms=divmod(ms,60000);s,ms=divmod(ms,1000);return f'{h:02}:{m:02}:{s:02}{sep}{ms:03}'
for week in sorted(root.glob(sys.argv[1] if len(sys.argv)>1 else 'week-*')):
 if not (week/'narration/beats.json').exists():continue
 beats=json.loads((week/'narration/beats.json').read_text());n=int(week.name[-2:]);assets=week/'assets';assets.mkdir(exist_ok=True)
 (assets/'gsap.min.js').write_text('\n'.join(line.rstrip() for line in (root/'production/node_modules/gsap/dist/gsap.min.js').read_text().splitlines()).rstrip()+'\n')
 for name in ['source-sans-3-latin-400-normal.woff2','source-sans-3-latin-700-normal.woff2']:shutil.copy(Path('assets/fonts')/name,assets/name)
 shutil.copy('assets/vub-seal-white.png',assets/'vub-seal.png')
 shutil.copy(Path('courses/digital-literacy-2/assets/illustrations')/f'slide-{visuals.ART[n]}.webp',assets/'topic.webp')
 (week/'compositions/frames').mkdir(parents=True,exist_ok=True);(week/'captions').mkdir(exist_ok=True)
 clips=[];audio=[];cues=[];start=0;story=[]
 for i,b in enumerate(beats):
  if 'audioDuration' not in b:raise RuntimeError('Wait for final audio generation')
  duration=b['window'];b['start']=round(start+b.get('leadIn',0.01),3);cid=f'w{n}-scene-{i+1}';labels=b['labels'];labelhtml=''.join(f'<div class="point" id="{cid}-point-{j}"><span class="point-number">{j+1}</span><span>{esc(t)}</span></div>' for j,t in enumerate(labels))
  word_times=json.loads((week/f'narration/{b["id"]}.words.json').read_text())['words']
  sub=visuals.scene(n,i,b,word_times)
  (week/f'compositions/frames/scene-{i+1}.html').write_text(sub)
  clips.append(f'<div class="clip" id="host-{cid}" data-composition-id="{cid}" data-composition-src="compositions/frames/scene-{i+1}.html" data-start="{start:.3f}" data-duration="{duration}" data-track-index="0" style="position:absolute;inset:0"></div>')
  audio.append(f'<audio class="clip" id="aud-{b["id"]}" src="narration/{b["id"]}.wav" data-start="{start+b.get('leadIn',0.01):.3f}" data-duration="{b["audioDuration"]:.5f}" data-track-index="1"></audio>')
  aligned=json.loads((week/f'narration/{b["id"]}.words.json').read_text())['words']
  group=[]
  for j,word in enumerate(aligned):
   group.append(word)
   length=len(' '.join(x['word'] for x in group))
   if ((len(group)>=10 or length>=63) and len(aligned)-j-1>=4) or j==len(aligned)-1:
    text=' '.join(x['word'] for x in group);cs=start+b.get('leadIn',0.01)+group[0]['start'];ce=min(start+b.get('leadIn',0.01)+b['audioDuration'],start+b.get('leadIn',0.01)+max(group[-1]['end'],group[0]['start']+.3));cues.append((cs,ce,text));group=[]
  story.append(f'## Frame {i+1} — {b["title"]}\n\n- src: compositions/frames/scene-{i+1}.html\n- duration: {duration}s\n- status: animated\n- transition_in: cut\n- scene: Picture-led explanation with original topic art, concise visual diagrams and word-timed state changes.\n- voiceover: "{b["text"]}"\n- blueprint: compose\n\nScene 1 (0–{duration}s): Original software demonstration; state changes follow the recognized narration anchors. The original artwork sets context; large diagrams show the change with minimal labels. Keep the bottom band available for optional player captions.\n')
  start+=duration
 (week/'narration/beats.json').write_text(json.dumps(beats,indent=2)+'\n')
 title=json.loads((root/'videos.json').read_text())[n-1]['title']
 (week/'index.html').write_text(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=1280,height=720"><title>{esc(title)}</title><script src="assets/gsap.min.js"></script><style>@font-face{{font-family:VUB;src:url('assets/source-sans-3-latin-400-normal.woff2')}}@font-face{{font-family:VUB;src:url('assets/source-sans-3-latin-700-normal.woff2');font-weight:700}}*{{box-sizing:border-box}}body{{margin:0;font-family:VUB,'Segoe UI',sans-serif}}#root{{position:relative;width:1280px;height:720px;overflow:hidden}}</style></head><body><div id="root" data-composition-id="main" data-start="0" data-duration="{start:.3f}" data-width="1280" data-height="720">{''.join(clips)}{''.join(audio)}</div><script>window.__timelines=window.__timelines||{{}};window.__timelines.main=gsap.timeline({{paused:true}});</script></body></html>''')
 (week/'hyperframes.json').write_text((root/'production/hyperframes.json').read_text())
 (week/'STORYBOARD.md').write_text(f'---\nformat: 1280x720\nmode: autonomous\nduration: {start:.3f}s\nmessage: {title}\naudience: adult veteran learners\n---\n\n'+''.join(story))
 (public/f'week-{n:02}-chapters.json').write_text(json.dumps([dict(title=b['title'],startSeconds=b['start']) for b in beats],indent=2)+'\n')
 (week/'SCRIPT.md').write_text('\n\n'.join(f'## {b["title"]}\n{b["text"]}' for b in beats))
 srt='\n\n'.join(f'{i+1}\n{stamp(a,",")} --> {stamp(b,",")}\n'+textwrap.fill(t,width=42,break_long_words=False,break_on_hyphens=False) for i,(a,b,t) in enumerate(cues))+'\n'
 vtt='WEBVTT\n\n'+'\n\n'.join(f'{stamp(a)} --> {stamp(b)}\n'+textwrap.fill(t,width=42,break_long_words=False,break_on_hyphens=False) for a,b,t in cues)+'\n'
 (week/'captions/narration.srt').write_text(srt);(public/f'week-{n:02}.vtt').write_text(vtt)
 print(week.name,round(start,2),'seconds',len(cues),'aligned captions')
