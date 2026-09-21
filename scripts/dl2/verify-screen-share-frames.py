"""Compare all task states in encoded deliveries with independently sought sources."""
import json, subprocess, re, sys
from pathlib import Path

root=Path(__file__).resolve().parents[2]
review=root/'video/digital-literacy-2/screen-share-review'
source=json.loads((review/'report.json').read_text())
assert not source['errors'], 'Resolve source-state checks before verifying deliveries'
results=[]
for check in source['checks']:
    n=int(check['week'][-2:])
    video=root/f'courses/digital-literacy-2/media/week-{n:02}.mp4'
    target=review/('encoded-'+check['screenshot'])
    subprocess.run(['ffmpeg','-v','error','-y','-ss',str(check['globalSeconds']),'-i',str(video),'-frames:v','1',str(target)],check=True)
    # Compare the UI region, allowing small codec/rasterizer differences.
    # FFmpeg is already required for delivery; no image-library dependency.
    compare=subprocess.run(['ffmpeg','-hide_banner','-i',str(review/check['screenshot']),'-i',str(target),'-lavfi','[0:v]format=yuv444p,crop=1200:500:40:104[a];[1:v]format=yuv444p,crop=1200:500:40:104[b];[a][b]ssim','-f','null','-'],capture_output=True,text=True,check=True)
    score=float(re.search(r'All:([\d.]+)',compare.stderr)[1])
    results.append(dict(week=n,chapter=check['chapter'],action=check['action'],seconds=round(check['globalSeconds'],3),structuralSimilarity=score,passCheck=score>=.95))
failures=[r for r in results if not r['passCheck']]
report=dict(states=len(results),minimumStructuralSimilarity=.95,failures=failures,checks=results)
(root/'docs/digital-literacy-2/screen-share-frame-verification.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(dict(states=len(results),minimumSimilarity=min(r['structuralSimilarity'] for r in results),failures=failures),indent=2))
if failures:sys.exit(1)
