"""Transcribe staged narration without modifying the working course audio.

Unprompted recognition is evidence for omissions and spoken directions, not a
subjective listening judgment. Numeric spelling differences need human review.
Use --watch during MCP generation; cached results are tied to the MP3 hash.
"""
import argparse
import difflib
import hashlib
import json
import re
import time
from pathlib import Path
from faster_whisper import WhisperModel

parser = argparse.ArgumentParser()
parser.add_argument('--watch', action='store_true')
args = parser.parse_args()
root = Path('video/digital-literacy-2')
local = Path.home() / 'Desktop/vub-expressive-narration'
model = WhisperModel('base.en', device='cpu', compute_type='int8', cpu_threads=4)
jobs = [(w, b) for w in sorted(root.glob('week-*'))
        for b in json.loads((w / 'narration/beats.json').read_text())]
norm = lambda text: re.sub(r'[^a-z0-9]', '', text.lower())
report = root / 'elevenlabs-britt-v3-expressive/transcription-checks.json'
results = json.loads(report.read_text()) if report.exists() else []
done = {(r['week'], r['chapter']): r for r in results}
deadline = time.monotonic() + 1800
while True:
  for week, beat in jobs:
    key = (week.name, beat['id'])
    files = list((local / week.name / beat['id'] / 'clean').glob('*.mp3'))
    if len(files) != 1 or time.time() - files[0].stat().st_mtime < 3:
      done.pop(key, None)
      continue
    source = files[0]
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    if done.get(key, {}).get('sha256') == digest:
      continue
    segments, info = model.transcribe(str(source), language='en', beam_size=5,
                                    word_timestamps=True, condition_on_previous_text=False)
    words = [w for s in segments for w in s.words]
    expected = beat['text'].split()
    match = difflib.SequenceMatcher(None, [norm(w) for w in expected],
                                  [norm(w.word) for w in words], autojunk=False)
    changes = [dict(expected=' '.join(expected[a:b]), recognized=' '.join(w.word.strip() for w in words[c:d]))
               for op, a, b, c, d in match.get_opcodes() if op != 'equal']
    matched = sum(size for _, _, size in match.get_matching_blocks()) / len(expected)
    done[key] = dict(week=week.name, chapter=beat['id'], sha256=digest,
                    durationSeconds=round(info.duration, 3),
                    wordsPerMinute=round(len(expected) / info.duration * 60, 1),
                    matchRatio=round(matched, 4), differences=changes,
                    recognized=' '.join(w.word.strip() for w in words))
    report.write_text(json.dumps(sorted(done.values(), key=lambda r: (r['week'], r['chapter'])), indent=2) + '\n')
    print(week.name, beat['id'], done[key]['wordsPerMinute'], 'WPM', round(matched, 3), flush=True)
  report.write_text(json.dumps(sorted(done.values(), key=lambda r: (r['week'], r['chapter'])), indent=2) + '\n')
  if len(done) == len(jobs):
    break
  if not args.watch:
    raise RuntimeError(f'Only {len(done)}/{len(jobs)} current sources are available.')
  if time.monotonic() > deadline:
    raise RuntimeError('Generation batch remains incomplete; no working audio replaced.')
  time.sleep(5)
print(f'Checked {len(done)}/{len(jobs)} takes. Review recognition differences before import.', flush=True)
