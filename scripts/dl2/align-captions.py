import sys
"""Align original captions to recognized words in final audio, with a match gate."""
import json,re,difflib,hashlib
from pathlib import Path
from faster_whisper import WhisperModel
model=WhisperModel('base.en',device='cpu',compute_type='int8',cpu_threads=4)
def norm(s):return re.sub(r'[^a-z0-9]','',s.lower())
for folder in sorted(Path('video/digital-literacy-2').glob((sys.argv[1] if len(sys.argv)>1 else 'week-*')+'/narration')):
 beats=json.loads((folder/'beats.json').read_text())
 for beat in beats:
  out=folder/(beat['id']+'.words.json')
  wavHash=hashlib.sha256((folder/(beat['id']+'.wav')).read_bytes()).hexdigest()
  textHash=hashlib.sha256(beat['text'].encode()).hexdigest()
  if out.exists():
   cached=json.loads(out.read_text())
   if cached.get('wavSha256')==wavHash and cached.get('textSha256')==textHash:continue
  segments,_=model.transcribe(str(folder/(beat['id']+'.wav')),word_timestamps=True,language='en',beam_size=5,condition_on_previous_text=False)
  observed=[w for s in segments for w in s.words];script=beat['text'].split()
  match=difflib.SequenceMatcher(None,[norm(x) for x in script],[norm(w.word) for w in observed],autojunk=False)
  aligned={}
  for a,b,size in match.get_matching_blocks():
   for offset in range(size):aligned[a+offset]=(observed[b+offset].start,observed[b+offset].end)
  ratio=len(aligned)/len(script)
  if ratio<.87:
   segments,_=model.transcribe(str(folder/(beat['id']+'.wav')),word_timestamps=True,language='en',beam_size=5,initial_prompt=beat['text'])
   retry=[w for seg in segments for w in seg.words]
   match=difflib.SequenceMatcher(None,[norm(x) for x in script],[norm(w.word) for w in retry],autojunk=False)
   alternative={}
   for a,b,size in match.get_matching_blocks():
    for offset in range(size):alternative[a+offset]=(retry[b+offset].start,retry[b+offset].end)
   if len(alternative)>len(aligned):aligned=alternative
   ratio=len(aligned)/len(script)
  if ratio<.87:raise RuntimeError(f'{folder} {beat["id"]}: alignment too weak: {ratio:.2f}')
  # Fill isolated unrecognized words only between neighboring recognized anchors.
  for i in range(len(script)):
   if i in aligned:continue
   prev=max([j for j in aligned if j<i],default=-1);nxt=min([j for j in aligned if j>i],default=len(script))
   start=aligned[prev][1] if prev>=0 else 0;end=aligned[nxt][0] if nxt<len(script) else beat['audioDuration']
   width=max(0,end-start)/(nxt-prev-1)
   aligned[i]=(start+width*(i-prev-1),start+width*(i-prev))
  words=[dict(word=w,start=round(aligned[i][0],3),end=round(aligned[i][1],3)) for i,w in enumerate(script)]
  out.write_text(json.dumps(dict(source='faster-whisper base.en on final narration wav',wavSha256=wavHash,textSha256=textHash,matchRatio=ratio,words=words),indent=2)+'\n')
  print(folder.parent.name,beat['id'],'matched',round(ratio,3),flush=True)
