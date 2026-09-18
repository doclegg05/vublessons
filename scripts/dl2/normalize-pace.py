import sys
"""Measure natural V3 delivery and allocate visual holds; never time-stretch speech."""
import json
from pathlib import Path
import soundfile as sf
for folder in sorted(Path('video/digital-literacy-2').glob((sys.argv[1] if len(sys.argv)>1 else 'week-*')+'/narration')):
 beats=json.loads((folder/'beats.json').read_text())
 for i,b in enumerate(beats):
  seconds=sf.info(str(folder/(b['id']+'.wav'))).duration
  # Brief orientation at scene entry, then a longer final reflection hold.
  b['leadIn']=0.45
  b['visualHold']=2.0 if i==len(beats)-1 else 1.1
  b['window']=round(seconds+b['leadIn']+b['visualHold'],3)
  b['audioDuration']=seconds
 (folder/'beats.json').write_text(json.dumps(beats,indent=2)+'\n')
