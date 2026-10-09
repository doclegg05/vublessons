"""Build ten-chapter adult-learning scripts from the reviewed teaching source.

  python3 scripts/dl2/author-media.py            # every week (resets each beats.json to the script)
  python3 scripts/dl2/author-media.py week-03    # one week; the other weeks' narration is left alone
"""
import json,sys
from pathlib import Path
root=Path('video/digital-literacy-2')
only=sys.argv[1] if len(sys.argv)>1 else None
videos=json.loads((root/'videos.json').read_text()) if only else []
for n,p in enumerate(sorted((root/'teaching-scripts').glob('week-*.txt')),1):
 if only and p.stem!=only:continue
 beats=[]
 for i,block in enumerate(p.read_text().strip().split('\n\n')):
  header,text=block.split('\n',1);title,visual,variant=header.split('|')
  beats.append(dict(id=f'beat-{i+1:02}',title=title,visual=visual,variant=int(variant),labels=[],text=text.strip(),window=60))
 assert len(beats)==10
 folder=root/f'week-{n:02}'/'narration';folder.mkdir(exist_ok=True)
 (folder/'beats.json').write_text(json.dumps(beats,indent=2)+'\n')
 for b in beats:(folder/(b['id']+'.txt')).write_text(b['text'])
 if only:videos[n-1]=dict(week=n,title=beats[0]['title'])
 else:videos.append(dict(week=n,title=beats[0]['title']))
(root/'videos.json').write_text(json.dumps(videos,indent=2)+'\n')
print(f"Authored {only or 'six teaching videos'}, ten chapters each.")
