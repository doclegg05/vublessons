"""Build reusable HyperFrames sources, matched caption tracks and media provenance."""
import json,html,shutil,textwrap,sys,importlib.util,re
visual_only='--visual-only' in sys.argv
args=[a for a in sys.argv[1:] if a!='--visual-only']
from pathlib import Path
spec=importlib.util.spec_from_file_location("video_scenes",Path(__file__).with_name("video-scenes.py"));visuals=importlib.util.module_from_spec(spec);spec.loader.exec_module(visuals)
from pathlib import Path
root=Path('video/digital-literacy-2');public=Path('courses/digital-literacy-2/media');public.mkdir(exist_ok=True)
esc=lambda s:html.escape(str(s),quote=True)
def stamp(sec,sep='.'):
 ms=round(sec*1000);h,ms=divmod(ms,3600000);m,ms=divmod(ms,60000);s,ms=divmod(ms,1000);return f'{h:02}:{m:02}:{s:02}{sep}{ms:03}'

# Caption cue grouping: break at phrase boundaries (sentence ends first, then
# clause punctuation) instead of a flat word-count/length budget, so cues read
# as phrases rather than arbitrary slices. Thresholds mirror check-captions.py.
# A chunk's reading rate is judged against how much time is actually available
# to display it: its own words plus any silent gap before the next word (or
# the beat's end), the same "extend into the following silence" fix a reading
# of the cues suggested for the fast passages a flat word/char budget cuts.
FUNCTION_WORDS={'a','an','the','to','of','and','or','but','for','with','in','on','at','by','from','as','that','which','who'}
LINE_WIDTH=42;MAX_CUE_DURATION=7.0;MIN_CUE_DURATION=0.7;MAX_CPS=20.0;MAX_CPS_SHORT=22.0;SHORT_CUE_SECONDS=1.5
# A small buffer on the reading-rate and minimum-duration targets absorbs
# millisecond rounding when timestamps are stamped, so a cue computed right
# at the limit does not read a hair over (or under) it once written out.
CPS_BUFFER=0.7;DURATION_BUFFER=0.05
def bare_word(w:str)->str:
 return re.sub(r'^[^A-Za-z0-9]+|[^A-Za-z0-9]+$','',w).lower()
def boundary_strength(w:str)->int:
 last=w[-1:]
 if last in '.!?':return 3
 if last in ';:':return 2
 if last in ',':return 1
 if last in '\u2014\u2013' and len(w)>1:return 2
 return 0
def wrap_split(text:str,width:int=LINE_WIDTH):
 """Best two-line split point for text (word index to break before), or None
 if no split keeps both lines within width. Prefers a break at punctuation
 nearest the middle and never leaves a single short word on line 2."""
 words=text.split(' ');n=len(words)
 def seg(a:int,b:int)->str:return ' '.join(words[a:b])
 best=None
 for i in range(1,n):
  l1,l2=seg(0,i),seg(i,n)
  if len(l1)>width or len(l2)>width:continue
  score=-boundary_strength(words[i-1])*100
  if n-i==1 and n>2 and len(words[-1])<=5:score+=80
  score+=abs(len(l1)-len(l2))
  if best is None or score<best[0]:best=(score,i)
 return best[1] if best else None
def fits_two_lines(text:str,width:int=LINE_WIDTH)->bool:
 return len(text)<=width or wrap_split(text,width) is not None
def required_duration(text_len:int)->float:
 floor=MIN_CUE_DURATION+DURATION_BUFFER
 d=max(floor,text_len/(MAX_CPS_SHORT-CPS_BUFFER))
 if d>=SHORT_CUE_SECONDS:d=max(floor,text_len/(MAX_CPS-CPS_BUFFER))
 return d
def extension_cap(words:list,hi:int,audio_duration:float)->float:
 return words[hi+1]['start'] if hi+1<len(words) else audio_duration
def cue_fits(words:list,lo:int,hi:int,audio_duration:float)->bool:
 text=' '.join(x['word'] for x in words[lo:hi+1])
 if not fits_two_lines(text):return False
 cs=words[lo]['start'];cap=min(extension_cap(words,hi,audio_duration),cs+MAX_CUE_DURATION)
 return required_duration(len(text))<=max(cap-cs,0.001)
def ends_dangling(w:str)->bool:
 """A bare function word is a dangling mid-clause cut; one with its own
 sentence-final punctuation (an English phrasal verb or a sentence that
 trails off on a pronoun, e.g. 'act on.' or 'responsible for.') is a
 complete sentence, not a dangling cut."""
 return w[-1:] not in '.!?' and bare_word(w) in FUNCTION_WORDS
def avoid_function_word_end(words:list,lo:int,hi:int,k:int)->int:
 i=k
 while i<hi and ends_dangling(words[i]['word']):i+=1
 if i<hi and not ends_dangling(words[i]['word']):return i
 i=k
 while i>lo and ends_dangling(words[i]['word']):i-=1
 return i
def timing_deficit(words:list,lo:int,hi:int,audio_duration:float)->float:
 """How far short a span falls of its required duration, after allowing for
 extending its end into any silence before the next word (or the beat's
 end); 0 when cue_fits would accept it. Unlike a raw reading-rate check,
 this credits a span with time it can actually borrow, so a piece next to a
 real pause is not penalized the same as one buried mid-sentence."""
 text_len=len(' '.join(x['word'] for x in words[lo:hi+1]))
 cs=words[lo]['start'];cap=min(extension_cap(words,hi,audio_duration),cs+MAX_CUE_DURATION)
 return max(0.0,required_duration(text_len)-max(cap-cs,0.001))
def choose_split(words:list,lo:int,hi:int,audio_duration:float)->int:
 """Clearing the timing deficit comes first; a clause-punctuation boundary
 is the tiebreaker among splits that are equally good (or equally clean) on
 timing. A sentence spoken at a locally uneven pace can otherwise get cut
 right at its fastest stretch, isolating it instead of diluting it with a
 slower neighbor, and restricting the search to punctuation alone can miss
 the one word gap that actually clears the deficit."""
 best=min(range(lo,hi),key=lambda k:(max(timing_deficit(words,lo,k,audio_duration),timing_deficit(words,k+1,hi,audio_duration)),-boundary_strength(words[k]['word'])))
 return avoid_function_word_end(words,lo,hi,best)
def split_span(words:list,lo:int,hi:int,audio_duration:float)->list:
 """Split for line/length fit (readability) first, preferring a clause
 boundary. A chunk that already fits on two lines but still has a timing
 deficit is only split further when some split point actually lowers the
 worst-case deficit on both halves: a fast burst of words usually has the
 same or a worse deficit in isolation than kept with a neighbor (splitting
 loses whatever extension room the whole span had), so splitting on rate
 alone with no improvement in sight just fragments the cue without fixing
 anything. Any deficit that survives this is left for merge_short_chunks to
 extend into silence or absorb into a neighbor."""
 text=' '.join(x['word'] for x in words[lo:hi+1])
 if hi<=lo:return[(lo,hi)]
 if fits_two_lines(text):
  deficit=timing_deficit(words,lo,hi,audio_duration)
  if deficit<=0:return[(lo,hi)]
  k=choose_split(words,lo,hi,audio_duration)
  if lo<=k<hi and max(timing_deficit(words,lo,k,audio_duration),timing_deficit(words,k+1,hi,audio_duration))>=deficit:return[(lo,hi)]
 else:
  k=choose_split(words,lo,hi,audio_duration)
 if k<lo or k>=hi:k=max(lo,min(hi-1,lo+(hi-lo)//2))
 return split_span(words,lo,k,audio_duration)+split_span(words,k+1,hi,audio_duration)
def dangling_sentence_start(words:list,lo:int,hi:int)->bool:
 """True if a sentence ends strictly inside [lo,hi) leaving fewer than 5
 words of the following sentence in the same span (mirrors check-captions.py's
 rule, so a merge is only allowed to fully absorb a short next sentence, not
 leave a stray fragment of it dangling)."""
 for i in range(lo,hi):
  if boundary_strength(words[i]['word'])==3 and 0<hi-i<5:return True
 return False
def merge_short_chunks(words:list,chunks:list,audio_duration:float)->list:
 chunks=list(chunks);changed=True
 while changed:
  changed=False
  for idx in range(len(chunks)):
   lo,hi=chunks[idx]
   if cue_fits(words,lo,hi,audio_duration) and (hi-lo+1)>=2:continue
   if idx+1<len(chunks):
    nlo,nhi=chunks[idx+1]
    if not dangling_sentence_start(words,lo,nhi) and cue_fits(words,lo,nhi,audio_duration):
     chunks[idx:idx+2]=[(lo,nhi)];changed=True;break
   if idx-1>=0:
    plo,phi=chunks[idx-1]
    if not dangling_sentence_start(words,plo,hi) and cue_fits(words,plo,hi,audio_duration):
     chunks[idx-1:idx+1]=[(plo,hi)];changed=True;break
  if changed:continue
 return chunks
def better_boundary(words:list,lo:int,mid:int,hi:int,audio_duration:float)->int:
 """Nudge the split point between two adjacent chunks if that reduces the
 worse of their two timing deficits, without breaking the line-fit,
 function-word or dangling-sentence rules. A split chosen for one chunk's
 own best interest can still leave its neighbor with slack to spare;
 shifting a word or two across the boundary can clear a small deficit that
 a whole-chunk merge cannot, because the pair's combined text may no
 longer fit on two lines."""
 best_mid=mid;best_score=max(timing_deficit(words,lo,mid,audio_duration),timing_deficit(words,mid+1,hi,audio_duration))
 for cand in range(lo,hi):
  if cand==mid:continue
  left=' '.join(x['word'] for x in words[lo:cand+1]);right=' '.join(x['word'] for x in words[cand+1:hi+1])
  if not fits_two_lines(left) or not fits_two_lines(right):continue
  if ends_dangling(words[cand]['word']):continue
  if dangling_sentence_start(words,lo,cand) or dangling_sentence_start(words,cand+1,hi):continue
  score=max(timing_deficit(words,lo,cand,audio_duration),timing_deficit(words,cand+1,hi,audio_duration))
  if score<best_score:best_score=score;best_mid=cand
 return best_mid
def rebalance_chunks(words:list,chunks:list,audio_duration:float)->list:
 chunks=list(chunks);changed=True
 while changed:
  changed=False
  for i in range(len(chunks)-1):
   lo,mid=chunks[i];mid2,hi=chunks[i+1]
   if mid+1!=mid2:continue
   new_mid=better_boundary(words,lo,mid,hi,audio_duration)
   if new_mid!=mid:chunks[i]=(lo,new_mid);chunks[i+1]=(new_mid+1,hi);changed=True
 return chunks
def group_cues(words:list,audio_duration:float)->list:
 n=len(words)
 if n==0:return[]
 sentence_ends=[i for i in range(n) if boundary_strength(words[i]['word'])==3]
 if not sentence_ends or sentence_ends[-1]!=n-1:sentence_ends=sentence_ends+[n-1]
 chunks=[];lo=0
 for end in sentence_ends:
  chunks+=split_span(words,lo,end,audio_duration);lo=end+1
 chunks=rebalance_chunks(words,chunks,audio_duration)
 chunks=merge_short_chunks(words,chunks,audio_duration)
 return rebalance_chunks(words,chunks,audio_duration)
def cue_timing(words:list,lo:int,hi:int,audio_duration:float)->tuple:
 text=' '.join(x['word'] for x in words[lo:hi+1])
 cs=words[lo]['start'];natural_end=max(words[hi]['end'],cs+.3)
 cap=min(extension_cap(words,hi,audio_duration),cs+MAX_CUE_DURATION,audio_duration)
 end=min(cap,max(natural_end,cs+required_duration(len(text))))
 return cs,end,text
def wrap_cue(text:str,width:int=LINE_WIDTH)->str:
 if len(text)<=width:return text
 i=wrap_split(text,width)
 if i is None:return textwrap.fill(text,width=width,break_long_words=False,break_on_hyphens=False)
 words=text.split(' ');return ' '.join(words[:i])+'\n'+' '.join(words[i:])
for week in sorted(root.glob(args[0] if args else 'week-*')):
 if not (week/'narration/beats.json').exists():continue
 beats=json.loads((week/'narration/beats.json').read_text());n=int(week.name[-2:]);assets=week/'assets';assets.mkdir(exist_ok=True)
 (assets/'gsap.min.js').write_text('\n'.join(line.rstrip() for line in (root/'production/node_modules/gsap/dist/gsap.min.js').read_text().splitlines()).rstrip()+'\n')
 for name in ['source-sans-3-latin-400-normal.woff2','source-sans-3-latin-700-normal.woff2']:shutil.copy(Path('assets/fonts')/name,assets/name)
 shutil.copy('assets/vub-seal-white.png',assets/'vub-seal.png')
 if n==1:shutil.copy(root/'generated-screen-share/workstation.mp4',assets/'workstation-intro.mp4')
 for photo in sorted({visuals.chapter_plan(n,i)['photo'] for i in range(len(beats))} - {None}):
  source=Path('courses/digital-literacy-2/assets/photos')/f'{photo}.webp'
  if not source.exists():raise FileNotFoundError(f'Required approved photograph missing: {source}')
  shutil.copy(source,assets/source.name)
 (week/'compositions/frames').mkdir(parents=True,exist_ok=True);(week/'captions').mkdir(exist_ok=True)
 clips=[];audio=[];cues=[];start=0;story=[];screen_actions=[]
 for i,b in enumerate(beats):
  if 'audioDuration' not in b:raise RuntimeError('Wait for final audio generation')
  duration=b['window'];b['start']=round(start+b.get('leadIn',0.01),3);cid=f'w{n}-scene-{i+1}';labels=b['labels'];labelhtml=''.join(f'<div class="point" id="{cid}-point-{j}"><span class="point-number">{j+1}</span><span>{esc(t)}</span></div>' for j,t in enumerate(labels))
  word_times=json.loads((week/f'narration/{b["id"]}.words.json').read_text())['words']
  sub=visuals.scene(n,i,b,word_times)
  if (n,i) in visuals.screens.SELECTED:
   screen_actions.append(dict(chapter=i+1,title=b['title'],startSeconds=round(start,3),durationSeconds=duration,actions=visuals.screens.timed_actions(n,i,b,word_times)))
  (week/f'compositions/frames/scene-{i+1}.html').write_text(sub)
  clips.append(f'<div class="clip" id="host-{cid}" data-composition-id="{cid}" data-composition-src="compositions/frames/scene-{i+1}.html" data-start="{start:.3f}" data-duration="{duration}" data-track-index="0" style="position:absolute;inset:0"></div>')
  audio.append(f'<audio class="clip" id="aud-{b["id"]}" src="narration/{b["id"]}.wav" data-start="{start+b.get('leadIn',0.01):.3f}" data-duration="{b["audioDuration"]:.5f}" data-track-index="1"></audio>')
  aligned=json.loads((week/f'narration/{b["id"]}.words.json').read_text())['words']
  for lo,hi in group_cues(aligned,b['audioDuration']):
   cs_rel,ce_rel,text=cue_timing(aligned,lo,hi,b['audioDuration']);lead=b.get('leadIn',0.01)
   cs=start+lead+cs_rel;ce=min(start+lead+b['audioDuration'],start+lead+ce_rel);cues.append((cs,ce,text))
  plan=visuals.chapter_plan(n,i)
  story.append(f'## Frame {i+1} — {b["title"]}\n\n- src: compositions/frames/scene-{i+1}.html\n- duration: {duration}s\n- status: animated\n- transition_in: cut\n- scene: {plan['kind']} / {plan['layout']}\n- photo: {plan['photo'] or 'none: full-stage authored demonstration'}\n- worked states: {'; '.join(plan['steps'])}\n- voiceover: "{b["text"]}"\n- blueprint: compose\n\nScene 1 (0–{duration}s): {'Full-screen task simulation with word-aligned cursor, clicks, typed inputs, and verified outcomes; see screen-share-actions.json.' if plan['layout']=='screen-share' else 'Authored fictional demonstration with chapter-specific evidence captions. When present, a landscape scenario photograph or the generated week-1 workstation clip establishes context before the diagram.'} Britt audio, chapter windows and existing caption files are retained in visual-only mode.\n')
  start+=duration
 if not visual_only:(week/'narration/beats.json').write_text(json.dumps(beats,indent=2)+'\n')
 title=json.loads((root/'videos.json').read_text())[n-1]['title']
 (week/'index.html').write_text(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=1280,height=720"><title>{esc(title)}</title><script src="assets/gsap.min.js"></script><style>@font-face{{font-family:VUB;src:url('assets/source-sans-3-latin-400-normal.woff2')}}@font-face{{font-family:VUB;src:url('assets/source-sans-3-latin-700-normal.woff2');font-weight:700}}*{{box-sizing:border-box}}body{{margin:0;font-family:VUB,'Segoe UI',sans-serif}}#root{{position:relative;width:100%;height:100%;overflow:hidden}}</style></head><body><div id="root" data-composition-id="main" data-start="0" data-duration="{start:.3f}" data-width="1280" data-height="720">{''.join(clips)}{''.join(audio)}</div><script>window.__timelines=window.__timelines||{{}};window.__timelines.main=gsap.timeline({{paused:true}});</script></body></html>''')
 (week/'hyperframes.json').write_text((root/'production/hyperframes.json').read_text())
 (week/'STORYBOARD.md').write_text(f'---\nformat: 1280x720\nmode: autonomous\nduration: {start:.3f}s\nmessage: {title}\naudience: adult veteran learners\n---\n\n'+''.join(story))
 (week/'screen-share-actions.json').write_text(json.dumps(screen_actions,indent=2)+'\n')
 if not visual_only:(public/f'week-{n:02}-chapters.json').write_text(json.dumps([dict(title=b['title'],startSeconds=b['start']) for b in beats],indent=2)+'\n')
 if not visual_only:(week/'SCRIPT.md').write_text('\n\n'.join(f'## {b["title"]}\n{b["text"]}' for b in beats))
 srt='\n\n'.join(f'{i+1}\n{stamp(a,",")} --> {stamp(b,",")}\n'+wrap_cue(t) for i,(a,b,t) in enumerate(cues))+'\n'
 vtt='WEBVTT\n\n'+'\n\n'.join(f'{stamp(a)} --> {stamp(b)}\n'+wrap_cue(t) for a,b,t in cues)+'\n'
 if not visual_only:
  (week/'captions/narration.srt').write_text(srt);(public/f'week-{n:02}.vtt').write_text(vtt)
 # Native bottom captions rise above visible playback controls and can obscure
 # the task result. Use the reserved title band during screen demonstrations.
 # Preserve every existing cue's words and timestamps in visual-only builds.
 caption_path=public/f'week-{n:02}.vtt'
 def cue_placement(match):
  hh,mm,ss=match[1].split(':');cue_start=int(hh)*3600+int(mm)*60+float(ss)
  is_demo=any(s['startSeconds']<=cue_start<s['startSeconds']+s['durationSeconds'] for s in screen_actions)
  return match[1]+' --> '+match[2]+(' line:0 position:50% align:center size:95%' if is_demo else '')
 caption_path.write_text(re.sub(r'(?m)^(\d{2}:\d{2}:\d{2}\.\d{3}) --> (\d{2}:\d{2}:\d{2}\.\d{3})[^\n]*',cue_placement,caption_path.read_text()))
 print(week.name,round(start,2),'seconds',len(cues),'aligned captions')
