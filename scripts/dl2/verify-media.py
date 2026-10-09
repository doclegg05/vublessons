"""Validate final delivery MP4s, caption coverage, and write the build allowlist.

  python3 scripts/dl2/verify-media.py --profile brad-refresh            # all six weeks
  python3 scripts/dl2/verify-media.py --profile brad-refresh --week 3   # one week; the others keep their verified entries
"""
import argparse,hashlib,json,re,subprocess
from pathlib import Path
parser=argparse.ArgumentParser()
parser.add_argument('--profile',choices=['expressive','brad-refresh'],default='expressive')
parser.add_argument('--week',type=int,action='append',help='verify only this week (repeatable); other weeks keep their manifest entries')
args=parser.parse_args()
profile_dir=Path('video/digital-literacy-2')/('elevenlabs-brad-v3-refresh' if args.profile=='brad-refresh' else 'elevenlabs-britt-v3-expressive')
profile=json.loads((profile_dir/'profile.json').read_text())
public=Path('courses/digital-literacy-2/media');videos=[];reports=[]
old_videos={v['path']:v for v in json.loads((public/'manifest.json').read_text())['videos']}
old_reports={r['week']:r for r in json.loads(Path('docs/digital-literacy-2/media-verification.json').read_text())}
def script_texts(n):
 # The reviewed teaching source (teaching-scripts/week-NN.txt) is the approved wording for each chapter.
 blocks=Path(f'video/digital-literacy-2/teaching-scripts/week-{n:02}.txt').read_text().strip().split('\n\n')
 return [hashlib.sha256(b.split('\n',1)[1].strip().encode()).hexdigest() for b in blocks]
def run(args):return subprocess.run(args,capture_output=True,text=True,check=True)
def seconds(t):
 h,m,s=t.split(':');return int(h)*3600+int(m)*60+float(s)
for n in range(1,7):
 p=public/f'week-{n:02}.mp4';source=Path(f'video/digital-literacy-2/week-{n:02}')
 if args.week and n not in args.week:
  videos.append(old_videos[str(p)]);reports.append(old_reports[n]);print(f'Week {n}: kept its earlier verified entry',flush=True);continue
 probe=json.loads(run(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(p)]).stdout)
 v=next(s for s in probe['streams'] if s['codec_type']=='video');a=next(s for s in probe['streams'] if s['codec_type']=='audio');duration=float(probe['format']['duration'])
 assert (v['codec_name'],v['width'],v['height'],v['r_frame_rate'])==('h264',1280,720,'24/1');assert a['codec_name']=='aac'
 states=json.loads((source/'narration/take-state.json').read_text())
 assert len(states)==10 and all(t['engine']=='ElevenLabs' and t['model']=='eleven_v3' and t['voice']==profile['voice'] and t.get('cleanup')=='ElevenLabs Voice Isolator' and not t['draft'] for t in states.values())
 if args.profile=='brad-refresh':
  assert all(t.get('performanceProfile')=='brad-refresh' for t in states.values())
 beats=json.loads((source/'narration/beats.json').read_text())
 chapters=json.loads((public/f'week-{n:02}-chapters.json').read_text())
 assert len(chapters)==len(beats)==10
 assert all(c['title']==b['title'] and abs(c['startSeconds']-b['start'])<.001 for c,b in zip(chapters,beats))
 expected=sum(b['window'] for b in beats);assert abs(duration-expected)<.1
 for beat in beats:
  alignment=json.loads((source/f"narration/{beat['id']}.words.json").read_text())
  assert alignment['textSha256']==hashlib.sha256(beat['text'].encode()).hexdigest()
  assert alignment['wavSha256']==hashlib.sha256((source/f"narration/{beat['id']}.wav").read_bytes()).hexdigest()
  assert alignment['matchRatio']>=.87
  assert abs(beat['window']-beat['audioDuration']-beat['leadIn']-beat['visualHold'])<.002
  assert 'paceAdjustment' not in states[beat['id']], 'V3 delivery must not be time-stretched'
  if states[beat['id']].get('performanceProfile') in ('expressive','brad-refresh'):
   receipt_dir=profile_dir/f'week-{n:02}'/beat['id']
   receipt=json.loads((receipt_dir/'receipt.json').read_text())
   assert receipt['voice']==states[beat['id']]['voice']==profile['voice']
   if args.profile=='brad-refresh':
    assert states[beat['id']]['performanceProfile']=='brad-refresh'
    assert receipt['textSha256']==script_texts(n)[int(beat['id'][-2:])-1], 'Narration must match the reviewed teaching script'
    assert receipt['originalSha256']==hashlib.sha256((receipt_dir/'original.mp3').read_bytes()).hexdigest()
    assert receipt['sourceSha256']==hashlib.sha256((receipt_dir/'isolated.mp3').read_bytes()).hexdigest()
   assert receipt['textSha256']==alignment['textSha256']
   assert receipt['sourceSha256']==states[beat['id']]['sha256']==hashlib.sha256((source/f"narration/{beat['id']}.mp3").read_bytes()).hexdigest()
   assert receipt['promptSha256']==hashlib.sha256((receipt_dir/'prompt.txt').read_bytes()).hexdigest()
   prompt=re.sub(r'\[[^]]+\]','',(receipt_dir/'prompt.txt').read_text())
   assert ' '.join(prompt.split())==' '.join(beat['text'].split()), 'Performance direction must not alter the lesson'

 # Decode every delivered frame/sample, not just container metadata.
 decoded=run(['ffmpeg','-v','error','-i',str(p),'-f','null','-']);assert not decoded.stderr.strip(),decoded.stderr
 audio=run(['ffmpeg','-hide_banner','-i',str(p),'-af','volumedetect','-vn','-f','null','-']).stderr
 mean=float(re.search(r'mean_volume: ([-\d.]+)',audio)[1]);peak=float(re.search(r'max_volume: ([-\d.]+)',audio)[1]);assert -30<mean<-10 and -6<peak<0
 loudness_log=run(['ffmpeg','-hide_banner','-nostats','-i',str(p),'-af','loudnorm=I=-18:TP=-1.5:LRA=11:print_format=json','-vn','-f','null','-']).stderr
 loudness=json.JSONDecoder().raw_decode(loudness_log[loudness_log.rfind('{'):])[0]
 integrated=float(loudness['input_i']);true_peak=float(loudness['input_tp'])
 assert abs(integrated+18)<=.5 and true_peak<=-1, 'Recheck final loudness normalization'
 black=run(['ffmpeg','-hide_banner','-i',str(p),'-vf','blackdetect=d=0.1:pix_th=0.05','-an','-f','null','-']).stderr;assert 'black_start:' not in black
 raw=p.read_bytes();assert len(raw)<=20*1024*1024, 'Video exceeds deployment budget'
 assert raw.index(b'moov')<raw.index(b'mdat'),'Use faststart for browser delivery'
 captions=(public/f'week-{n:02}.vtt').read_text();ranges=re.findall(r'(\d{2}:\d{2}:\d{2}\.\d{3}) --> (\d{2}:\d{2}:\d{2}\.\d{3})',captions);assert len(ranges)>=20
 prior=0
 for start,end in ranges:
  lo,hi=seconds(start),seconds(end);assert lo>=prior-.001 and hi>lo and hi<=duration;prior=hi
 # Captions must reproduce the authored narration, in order.
 body=re.sub(r'(?m)^\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}[^\n]*','',captions.replace('WEBVTT',''))
 assert ' '.join(body.split())==' '.join(' '.join(b['text'] for b in beats).split())
 check=json.loads(Path(f'docs/digital-literacy-2/video-check-{n:02}.json').read_text());assert check['ok'] and check['contrast']['checked']>0
 videos.append(dict(path=str(p),sha256=hashlib.sha256(raw).hexdigest(),durationSeconds=duration,bytes=len(raw),captions=f'courses/digital-literacy-2/media/week-{n:02}.vtt'))
 reports.append(dict(week=n,durationSeconds=duration,fullDecode='pass',blackFrames='none',meanVolumeDb=mean,peakVolumeDb=peak,integratedLufs=integrated,truePeakDbtp=true_peak,captionCues=len(ranges),fastStart=True,hyperframesStrict='pass'))
 print(f'Week {n}: delivery decode, picture, audio, captions and strict source checks PASS',flush=True)
renderer_versions={json.loads(Path(f'docs/digital-literacy-2/video-check-{n:02}.json').read_text())['_meta']['version'] for n in range(1,7)}
assert len(renderer_versions)==1, 'All delivered videos must use the same verified renderer version'
manifest=dict(formatVersion=1,voiceEngine=f"ElevenLabs eleven_v3, {profile['voiceName']} ({profile['voice']}); Voice Isolator cleanup; directed delivery, no time stretch; chaptered teaching",renderer=f'HyperFrames {next(iter(renderer_versions))}, local GSAP 3.14.2',videos=videos)
(public/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');Path('docs/digital-literacy-2/media-verification.json').write_text(json.dumps(reports,indent=2)+'\n')
