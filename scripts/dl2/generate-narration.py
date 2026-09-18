"""Generate local final narration with Kokoro; keep deterministic source/provenance."""
import json,hashlib,subprocess,sys,shutil
from pathlib import Path
import soundfile as sf
from kokoro_onnx import Kokoro
cache=Path.home()/'.cache/hyperframes/tts'
k=Kokoro(str(cache/'models/kokoro-v1.0.onnx'),str(cache/'voices/voices-v1.0.bin'))
for p in sorted(Path('video/digital-literacy-2').glob('week-*/narration')):
 beats=json.loads((p/'beats.json').read_text());state={}
 previous=json.loads((p/'take-state.json').read_text()) if (p/'take-state.json').exists() else {}
 for b in beats:
  wav=p/(b['id']+'.wav');mp3=p/(b['id']+'.mp3')
  textHash=hashlib.sha256(b['text'].encode()).hexdigest()
  if not wav.exists() or previous.get(b['id'],{}).get('textSha256')!=textHash or previous.get(b['id'],{}).get('engine')!='kokoro-onnx 0.6.1':
   samples,rate=k.create(b['text'],voice='af_heart',speed=.88,lang='en-us');sf.write(str(wav),samples,rate);shutil.copy(wav,p/(b['id']+'.raw.wav'))
  seconds=sf.info(str(wav)).duration;b['window']=round(seconds+1.25,3);b['audioDuration']=seconds
  subprocess.run(['ffmpeg','-v','error','-y','-i',str(wav),'-codec:a','libmp3lame','-b:a','128k',str(mp3)],check=True)
  state[b['id']]=dict(engine='kokoro-onnx 0.6.1',voice='af_heart',speed=.88,draft=False,textSha256=textHash,sha256=hashlib.sha256(mp3.read_bytes()).hexdigest())
  print(p.parent.name,b['id'],round(seconds,2),'seconds',flush=True)
 (p/'beats.json').write_text(json.dumps(beats,indent=2)+'\n');(p/'take-state.json').write_text(json.dumps(state,indent=2)+'\n')
