"""Build a local review gallery after all six replacement videos verify."""
import html
import json
from pathlib import Path

root = Path('video/digital-literacy-2')
profile = json.loads((root / 'elevenlabs-brad-v3-refresh/profile.json').read_text())
manifest = json.loads(Path('courses/digital-literacy-2/media/manifest.json').read_text())
assert profile['voice'] in manifest['voiceEngine'], 'Verify refreshed media before labeling the gallery'
titles = json.loads((root / 'videos.json').read_text())
cards = []
for number, media in enumerate(manifest['videos'], 1):
  week = f'week-{number:02}'
  states = json.loads((root / week / 'narration/take-state.json').read_text())
  assert all(t['voice'] == profile['voice'] for t in states.values())
  seconds = round(media['durationSeconds'])
  title = html.escape(titles[number - 1]['title'])
  base = f'/courses/digital-literacy-2/media/{week}'
  cards.append(f'''<article id="{week}"><p class="eyebrow">Week {number} · {seconds//60}:{seconds%60:02} · 10 chapters</p>
<h2>{title}</h2><video controls preload="none" playsinline aria-label="Week {number}: {title}" poster="/docs/digital-literacy-2/review/video-teaching/{week}-scene-1.jpg">
<source src="{base}.mp4" type="video/mp4"><track kind="captions" src="{base}.vtt" srclang="en" label="English" default></video>
<div class="links"><a href="/courses/digital-literacy-2/weeks/{week}/video-transcript.html">Chapters and transcript</a><a href="{base}.mp4" download>Download MP4</a></div></article>''')
out = Path('docs/digital-literacy-2/review/narration-refresh')
out.mkdir(parents=True, exist_ok=True)
out.joinpath('index.html').write_text('''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>DL2 narration review | VUB Learning</title>
<style>*{box-sizing:border-box}body{margin:0;background:#102c4b;color:#f5f7fa;font:18px/1.6 'Segoe UI',Tahoma,sans-serif}header,main,footer{max-width:1280px;margin:auto;padding:32px}header{padding-top:48px}h1{font-size:clamp(32px,4vw,52px);line-height:1.15;margin:12px 0 20px}h2{font-size:24px;line-height:1.3;margin:8px 0 20px}.tag,.eyebrow{color:#e6c65c;font-weight:700;letter-spacing:.04em}.tag{display:inline-block;border:1px solid #e6c65c;border-radius:999px;padding:4px 14px}.intro{max-width:900px}main{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px;padding-top:0}article{min-width:0;background:#1b365d;border:1px solid #526f90;border-radius:16px;padding:24px}video{display:block;width:100%;aspect-ratio:16/9;background:#0d1b2a;border-radius:8px}.links{display:flex;gap:24px;flex-wrap:wrap;margin-top:20px}a{color:#fff;text-underline-offset:4px}a:focus-visible,video:focus-visible{outline:3px solid #e6c65c;outline-offset:5px}footer{border-top:1px solid #526f90}.skip{position:absolute;left:-9999px}.skip:focus{left:20px;top:10px;background:#1b365d;padding:10px} @media(max-width:760px){main{grid-template-columns:1fr}header,main,footer{padding:20px}article{padding:18px}}</style></head><body><a class="skip" href="#main">Skip to videos</a><header><span class="tag">Draft review · live classroom videos unchanged</span><h1>Digital Literacy Level 2<br>Narration review</h1><p class="intro">All six lessons use <strong>Hey Its Brad — Clear Narrator for Documentary</strong>. Review the warmth, clarity and pace on your classroom speakers. Captions and chapter links follow the new narration; pause for learner practice whenever needed.</p><p>ElevenLabs voice ID: <code>Dslrhjl3ZpzrctukrQSN</code></p></header><main id="main">'''+''.join(cards)+'''</main><footer><p>WV Veterans Upward Bound · Prepared for review. Publication is a separate decision.</p></footer><script>document.querySelectorAll('video').forEach(v=>v.addEventListener('play',()=>document.querySelectorAll('video').forEach(other=>{if(other!==v)other.pause()})));</script><script src="/shared/text-size.js"></script></body></html>''')
print(out / 'index.html')
