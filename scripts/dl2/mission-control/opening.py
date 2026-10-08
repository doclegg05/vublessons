"""Shared video opening; approved media stays owned by the media pipeline."""
import hashlib, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
BASE='/courses/digital-literacy-2'
def media_url(path):
 return '/'+path+'?v='+hashlib.sha256((ROOT/path).read_bytes()).hexdigest()[:12]
def video_slide(n, i, note='', minutes=8, pauses=False):
 item=json.loads((ROOT/'courses/digital-literacy-2/media/manifest.json').read_text())['videos'][n-1]
 poster=BASE+'/assets/photos/'+['workstation','library','resource-pack','collaboration','safety','app-planning'][n-1]+'.webp'
 seconds=round(item['durationSeconds']); duration=f'{seconds//60}:{seconds%60:02}'
 return f'''<section class="slide opening-video" id="slide-{i}" data-scene="deck" data-opening="video" aria-labelledby="video-title">
 <div class="panel full"><div class="hud"><img src="/assets/vub-seal-white.png" alt=""> WEEK {n} · WATCH &amp; CONNECT · {duration}</div>
 <h1 id="video-title" tabindex="-1">See it. Then try it.</h1>
 <div class="opening-media"><video controls playsinline preload="metadata" tabindex="0" aria-label="Week {n} teaching video" poster="{poster}"><source src="{media_url(item['path'])}" type="video/mp4"><track kind="captions" src="{media_url(item['captions'])}" srclang="en" label="English" default>Your browser cannot play this video. Open the transcript below.</video>
 <div class="opening-guide"><p>Play when ready.<br>{'Pause at each card.' if pauses else 'Pause to discuss.'}</p><a href="video-transcript.html" target="_blank" rel="noopener">Transcript &amp; chapters<br><span>(opens a new tab)</span></a><button type="button" data-opening-next>Continue to lesson →</button></div></div></div>
 <aside class="notes"><h2>Opening video · Week {n}</h2><p>{f'Allow about {minutes} minutes for this {duration} video and its pauses. Ask learners to open the worksheet first. Press Play; it never starts automatically. The video stops at pause cards: each card holds 10 seconds of silence and names the worksheet tasks to do. Press Pause, let learners work, then press Play when most are done.' if pauses else f'Allow {minutes} minutes for this {duration} video. Press Play; it never starts automatically. Captions are on by default. Pause for a question when useful, then resume.'} Use the transcript link for chapter replay in a separate tab. Leaving this slide pauses playback. With the video focused, its native controls own the keyboard; Tab to Continue to lesson for deck navigation.</p>{('<p>'+note+'</p>') if note else ''}</aside></section>'''
