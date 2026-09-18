"""Build reusable HyperFrames sources, matched caption tracks and media provenance."""
import json,html,shutil,textwrap,sys
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
 (week/'compositions/frames').mkdir(parents=True,exist_ok=True);(week/'captions').mkdir(exist_ok=True)
 clips=[];audio=[];cues=[];start=0;story=[]
 for i,b in enumerate(beats):
  if 'audioDuration' not in b:raise RuntimeError('Wait for final audio generation')
  duration=b['window'];b['start']=round(start+0.01,3);cid=f'w{n}-scene-{i+1}';labels=b['labels'];labelhtml=''.join(f'<div class="point" id="{cid}-point-{j}"><span class="point-number">{j+1}</span><span>{esc(t)}</span></div>' for j,t in enumerate(labels))
  # Intent: timed emphasis on a compact set of choices, with persistent scene progress.
  tweens=''.join(f'tl.fromTo("#{cid}-point-{j}",{{opacity:1,x:12}},{{opacity:1,x:0,duration:0.8,ease:"power2.out"}},{round(1+j*(duration-3)/max(1,len(labels)),3)});' for j in range(len(labels)))
  sub=f'''<template>
<div id="{cid}" data-composition-id="{cid}" data-start="0" data-duration="{duration}" data-width="1280" data-height="720" style="position:relative;width:1280px;height:720px;overflow:hidden">
<style>
#{cid} *{{box-sizing:border-box}}#{cid} .ground{{position:absolute;inset:0;background:#f5f7fa}}#{cid} .left{{position:absolute;left:0;top:0;width:520px;height:720px;background:#1b365d;color:white;padding:56px 44px}}#{cid} .seal{{width:64px;height:64px;object-fit:contain}}#{cid} .brand{{font-size:24px;font-weight:700;margin:18px 0 42px}}#{cid} h1{{font-size:50px;line-height:1.16;margin:0;font-weight:700;max-width:425px}}#{cid} .right{{position:absolute;left:555px;top:120px;width:665px;display:flex;flex-direction:column;gap:22px}}#{cid} .point{{display:flex;gap:20px;align-items:center;font-size:37px;line-height:1.35;color:#16243a;padding:18px 12px;border-bottom:2px solid #b5c9c5;min-height:100px}}#{cid} .point-number{{display:flex;flex:none;align-items:center;justify-content:center;width:52px;height:52px;background:#0f655f;color:white;border-radius:50%;font-size:28px;font-weight:700}}#{cid} .rail{{position:absolute;left:565px;right:70px;bottom:60px;height:7px;background:#cad8d6}}#{cid} .fill{{width:100%;height:7px;background:#0f655f;transform-origin:left center}}#{cid} .footer{{position:absolute;left:44px;bottom:44px;color:#f0d57c;font-size:22px}}#{cid} .scene-count{{position:absolute;right:70px;top:52px;color:#46566d;font-size:22px}}
</style>
<div class="ground"></div><div class="left"><img class="seal" src="assets/vub-seal.png" alt=""><div class="brand">VUB Learning · Level 2</div><h1>{esc(b['title'])}</h1><div class="footer">Week {n} · Try it. Check it. Explain it.</div></div><div class="scene-count">{i+1} / {len(beats)}</div><div class="right">{labelhtml}</div><div class="rail"><div class="fill" id="{cid}-fill"></div></div>
<script>
window.__timelines=window.__timelines||{{}};const tl=gsap.timeline({{paused:true}});{tweens}tl.fromTo("#{cid}-fill",{{scaleX:0}},{{scaleX:1,duration:{duration},ease:"none"}},0);window.__timelines["{cid}"]=tl;
</script></div></template>'''
  (week/f'compositions/frames/scene-{i+1}.html').write_text(sub)
  clips.append(f'<div class="clip" id="host-{cid}" data-composition-id="{cid}" data-composition-src="compositions/frames/scene-{i+1}.html" data-start="{start:.3f}" data-duration="{duration}" data-track-index="0" style="position:absolute;inset:0"></div>')
  audio.append(f'<audio class="clip" id="aud-{b["id"]}" src="narration/{b["id"]}.wav" data-start="{start+0.01:.3f}" data-duration="{b["audioDuration"]:.5f}" data-track-index="1"></audio>')
  aligned=json.loads((week/f'narration/{b["id"]}.words.json').read_text())['words']
  group=[]
  for j,word in enumerate(aligned):
   group.append(word)
   length=len(' '.join(x['word'] for x in group))
   if ((len(group)>=10 or length>=63) and len(aligned)-j-1>=4) or j==len(aligned)-1:
    text=' '.join(x['word'] for x in group);cs=start+0.01+group[0]['start'];ce=min(start+0.01+b['audioDuration'],start+0.01+max(group[-1]['end'],group[0]['start']+.3));cues.append((cs,ce,text));group=[]
  story.append(f'## Frame {i+1} — {b["title"]}\n\n- src: compositions/frames/scene-{i+1}.html\n- duration: {duration}s\n- status: animated\n- transition_in: cut\n- scene: Show the decision labels in their narrated order.\n- voiceover: "{b["text"]}"\n- blueprint: compose\n\nScene 1 (0–{duration}s): VUB title panel and ordered labels; each label receives emphasis as the explanation develops. The bottom rail shows the scene’s playback progress. Keep the bottom band available for optional player captions.\n')
  start+=duration
 (week/'narration/beats.json').write_text(json.dumps(beats,indent=2)+'\n')
 title=json.loads((root/'videos.json').read_text())[n-1]['title']
 (week/'index.html').write_text(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=1280,height=720"><title>{esc(title)}</title><script src="assets/gsap.min.js"></script><style>@font-face{{font-family:VUB;src:url('assets/source-sans-3-latin-400-normal.woff2')}}@font-face{{font-family:VUB;src:url('assets/source-sans-3-latin-700-normal.woff2');font-weight:700}}*{{box-sizing:border-box}}body{{margin:0;font-family:VUB,'Segoe UI',sans-serif}}#root{{position:relative;width:1280px;height:720px;overflow:hidden}}</style></head><body><div id="root" data-composition-id="main" data-start="0" data-duration="{start:.3f}" data-width="1280" data-height="720">{''.join(clips)}{''.join(audio)}</div><script>window.__timelines=window.__timelines||{{}};window.__timelines.main=gsap.timeline({{paused:true}});</script></body></html>''')
 (week/'hyperframes.json').write_text((root/'production/hyperframes.json').read_text())
 (week/'STORYBOARD.md').write_text(f'---\nformat: 1280x720\nmode: autonomous\nduration: {start:.3f}s\nmessage: {title}\naudience: adult veteran learners\n---\n\n'+''.join(story))
 (week/'SCRIPT.md').write_text('\n\n'.join(f'## {b["title"]}\n{b["text"]}' for b in beats))
 srt='\n\n'.join(f'{i+1}\n{stamp(a,",")} --> {stamp(b,",")}\n'+textwrap.fill(t,width=42) for i,(a,b,t) in enumerate(cues))+'\n'
 vtt='WEBVTT\n\n'+'\n\n'.join(f'{stamp(a)} --> {stamp(b)}\n'+textwrap.fill(t,width=42) for a,b,t in cues)+'\n'
 (week/'captions/narration.srt').write_text(srt);(public/f'week-{n:02}.vtt').write_text(vtt)
 print(week.name,round(start,2),'seconds',len(cues),'aligned captions')
