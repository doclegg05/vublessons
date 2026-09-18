"""Capture every chapter from delivered MP4s for visual inspection (requires Pillow)."""
import json,subprocess,sys
from pathlib import Path
from PIL import Image,ImageDraw
root=Path(__file__).resolve().parents[2]
out=root/'docs/digital-literacy-2/review/video-teaching';out.mkdir(parents=True,exist_ok=True)
for n in map(int,sys.argv[1:] or range(1,7)):
 beats=json.loads((root/f'video/digital-literacy-2/week-{n:02}/narration/beats.json').read_text())
 sheet=Image.new('RGB',(1280,((len(beats)+1)//2)*380),'#102c4b');draw=ImageDraw.Draw(sheet)
 for i,b in enumerate(beats):
  t=b['start']+b['audioDuration']*.7;p=out/f'week-{n:02}-scene-{i+1}.jpg'
  subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',str(root/f'courses/digital-literacy-2/media/week-{n:02}.mp4'),'-frames:v','1','-q:v','2',str(p)],check=True)
  im=Image.open(p);im.thumbnail((640,360));x=(i%2)*640;y=(i//2)*380;sheet.paste(im,(x,y+20));draw.text((x+12,y+3),f'Week {n} / scene {i+1} / {t:.1f}s',fill='white')
 sheet.save(out/f'week-{n:02}-contact.jpg',quality=90)
 print(n,flush=True)
