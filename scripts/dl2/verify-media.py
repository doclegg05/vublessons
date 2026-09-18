"""Validate final delivery MP4s, caption coverage, and write the build allowlist."""
import hashlib,json,re,subprocess
from pathlib import Path
public=Path('courses/digital-literacy-2/media');videos=[];reports=[]
def run(args):return subprocess.run(args,capture_output=True,text=True,check=True)
def seconds(t):
 h,m,s=t.split(':');return int(h)*3600+int(m)*60+float(s)
for n in range(1,7):
 p=public/f'week-{n:02}.mp4';source=Path(f'video/digital-literacy-2/week-{n:02}')
 probe=json.loads(run(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(p)]).stdout)
 v=next(s for s in probe['streams'] if s['codec_type']=='video');a=next(s for s in probe['streams'] if s['codec_type']=='audio');duration=float(probe['format']['duration'])
 assert (v['codec_name'],v['width'],v['height'],v['r_frame_rate'])==('h264',1280,720,'24/1');assert a['codec_name']=='aac'
 states=json.loads((source/'narration/take-state.json').read_text())
 assert len(states)==5 and all(t['engine']=='ElevenLabs' and t['model']=='eleven_v3' and t['voice']=='iKrofGyA12WC0e6AhZ8B' and not t['draft'] for t in states.values())
 beats=json.loads((source/'narration/beats.json').read_text());expected=sum(b['window'] for b in beats);assert abs(duration-expected)<.1
 for beat in beats:
  alignment=json.loads((source/f"narration/{beat['id']}.words.json").read_text())
  assert alignment['textSha256']==hashlib.sha256(beat['text'].encode()).hexdigest()
  assert alignment['wavSha256']==hashlib.sha256((source/f"narration/{beat['id']}.wav").read_bytes()).hexdigest()
  assert alignment['matchRatio']>=.87
  assert abs(beat['window']-beat['audioDuration']-beat['leadIn']-beat['visualHold'])<.002
  assert 'paceAdjustment' not in states[beat['id']], 'V3 delivery must not be time-stretched'

 # Decode every delivered frame/sample, not just container metadata.
 decoded=run(['ffmpeg','-v','error','-i',str(p),'-f','null','-']);assert not decoded.stderr.strip(),decoded.stderr
 audio=run(['ffmpeg','-hide_banner','-i',str(p),'-af','volumedetect','-vn','-f','null','-']).stderr
 mean=float(re.search(r'mean_volume: ([-\d.]+)',audio)[1]);peak=float(re.search(r'max_volume: ([-\d.]+)',audio)[1]);assert -30<mean<-10 and -6<peak<0
 black=run(['ffmpeg','-hide_banner','-i',str(p),'-vf','blackdetect=d=0.1:pix_th=0.05','-an','-f','null','-']).stderr;assert 'black_start:' not in black
 raw=p.read_bytes();assert raw.index(b'moov')<raw.index(b'mdat'),'Use faststart for browser delivery'
 captions=(public/f'week-{n:02}.vtt').read_text();ranges=re.findall(r'(\d{2}:\d{2}:\d{2}\.\d{3}) --> (\d{2}:\d{2}:\d{2}\.\d{3})',captions);assert len(ranges)>=20
 prior=0
 for start,end in ranges:
  lo,hi=seconds(start),seconds(end);assert lo>=prior-.001 and hi>lo and hi<=duration;prior=hi
 # Captions must reproduce the authored narration, in order.
 body=re.sub(r'\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}','',captions.replace('WEBVTT',''))
 assert ' '.join(body.split())==' '.join(' '.join(b['text'] for b in beats).split())
 check=json.loads(Path(f'docs/digital-literacy-2/video-check-{n:02}.json').read_text());assert check['ok'] and check['contrast']['checked']>0
 videos.append(dict(path=str(p),sha256=hashlib.sha256(raw).hexdigest(),durationSeconds=duration,bytes=len(raw),captions=f'courses/digital-literacy-2/media/week-{n:02}.vtt'))
 reports.append(dict(week=n,durationSeconds=duration,fullDecode='pass',blackFrames='none',meanVolumeDb=mean,peakVolumeDb=peak,captionCues=len(ranges),fastStart=True,hyperframesStrict='pass'))
 print(f'Week {n}: delivery decode, picture, audio, captions and strict source checks PASS',flush=True)
manifest=dict(formatVersion=1,voiceEngine='ElevenLabs eleven_v3, Britt (iKrofGyA12WC0e6AhZ8B); natural delivery, no time stretch; timed visual holds',renderer='HyperFrames 0.8.48, local GSAP 3.14.2',videos=videos)
(public/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');Path('docs/digital-literacy-2/media-verification.json').write_text(json.dumps(reports,indent=2)+'\n')
