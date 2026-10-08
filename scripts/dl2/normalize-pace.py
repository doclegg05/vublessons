import sys
"""Measure natural V3 delivery and allocate visual holds; never time-stretch speech.

A week with cards.json (see build-media.py) gets silent time for its cards: a topic divider
plays before the narration starts, and a pause card holds after it so the instructor can stop
the video while the card is on screen (Britt, 2026-10-08: about 10 seconds).
"""
import json
from pathlib import Path
import soundfile as sf
DIVIDER_SECONDS=3.0
PAUSE_HOLD=10.5
for folder in sorted(Path('video/digital-literacy-2').glob((sys.argv[1] if len(sys.argv)>1 else 'week-*')+'/narration')):
 beats=json.loads((folder/'beats.json').read_text())
 cards_path=folder.parent/'cards.json'
 cards=json.loads(cards_path.read_text())['chapters'] if cards_path.exists() else {}
 for i,b in enumerate(beats):
  seconds=sf.info(str(folder/(b['id']+'.wav'))).duration
  card=cards.get(b['id'],{})
  # Brief orientation at scene entry, then a longer final reflection hold.
  b['leadIn']=round(0.45+(DIVIDER_SECONDS if 'divider' in card else 0),3)
  b['visualHold']=PAUSE_HOLD if 'pause' in card else 2.0 if i==len(beats)-1 else 1.1
  b['window']=round(seconds+b['leadIn']+b['visualHold'],3)
  b['audioDuration']=seconds
 (folder/'beats.json').write_text(json.dumps(beats,indent=2)+'\n')
