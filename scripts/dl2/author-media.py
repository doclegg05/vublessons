"""Build ten-chapter adult-learning scripts from the reviewed teaching source."""
import json
from pathlib import Path
root=Path('video/digital-literacy-2')
videos=[]
for n,p in enumerate(sorted((root/'teaching-scripts').glob('week-*.txt')),1):
 beats=[]
 for i,block in enumerate(p.read_text().strip().split('\n\n')):
  header,text=block.split('\n',1);title,visual,variant=header.split('|')
  beats.append(dict(id=f'beat-{i+1:02}',title=title,visual=visual,variant=int(variant),labels=[],text=text.strip(),window=60))
 assert len(beats)==10
 folder=root/f'week-{n:02}'/'narration';folder.mkdir(exist_ok=True)
 (folder/'beats.json').write_text(json.dumps(beats,indent=2)+'\n')
 for b in beats:(folder/(b['id']+'.txt')).write_text(b['text'])
 videos.append(dict(week=n,title=beats[0]['title']))
(root/'videos.json').write_text(json.dumps(videos,indent=2)+'\n')
print('Authored six teaching videos, ten chapters each.')
