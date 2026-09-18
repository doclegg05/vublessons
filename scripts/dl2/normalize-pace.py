"""Match Sandra's 135–145 wpm house band with pitch-preserving time stretch."""
import json,re,subprocess,hashlib
from pathlib import Path
import soundfile as sf
for folder in sorted(Path('video/digital-literacy-2').glob('week-*/narration')):
 beats=json.loads((folder/'beats.json').read_text());state=json.loads((folder/'take-state.json').read_text())
 for b in beats:
  wav=folder/(b['id']+'.wav');raw=folder/(b['id']+'.raw.wav')
  text=re.sub(r"[^\w'\s]",' ',b['text'].replace('’',"'"));count=len(text.split());seconds=sf.info(str(wav)).duration;wpm=count/seconds*60
  if wpm<135 or wpm>145:
   if not raw.exists():wav.rename(raw)
   seconds=sf.info(str(raw)).duration;factor=count*60/140/seconds
   subprocess.run(['ffmpeg','-v','error','-y','-i',str(raw),'-af',f'atempo={1/factor:.8f}',str(wav)],check=True)
   words=folder/(b['id']+'.words.json')
   if words.exists():words.unlink()
   state[b['id']]['paceAdjustment']='ffmpeg atempo, target 140 wpm'
  seconds=sf.info(str(wav)).duration;b['window']=round(seconds+1.25,3);b['audioDuration']=seconds
  mp3=folder/(b['id']+'.mp3');subprocess.run(['ffmpeg','-v','error','-y','-i',str(wav),'-codec:a','libmp3lame','-b:a','128k',str(mp3)],check=True)
  state[b['id']]['sha256']=hashlib.sha256(mp3.read_bytes()).hexdigest()
 (folder/'beats.json').write_text(json.dumps(beats,indent=2)+'\n');(folder/'take-state.json').write_text(json.dumps(state,indent=2)+'\n')
