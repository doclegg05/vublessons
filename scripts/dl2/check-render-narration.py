"""Transcribe a delivered DL2 MP4 and check each chapter's narration against its script.

The take checks hear the staged MP3s; this hears the file learners get. Every
chapter must match its script, sit inside its own audio clip, and leave the
pause and topic cards silent. A word counts as narration when it overlaps a
clip, because whisper stretches a chapter's last word into the silent card
after it (Weeks 4 and 5, "now." at the end of chapter 3). Sound-alikes ("two lowercase") lower the ratio
and need a human read of the differences, not a retake.
Run with the faster-whisper venv: video/digital-literacy-2/.venv/bin/python.
small.en is the default: on the whole Week 6 file base.en mistimed and dropped
words that a 9-second slice showed were there. Slice any flag before a retake.
"""
import argparse
import difflib
import json
import re
from pathlib import Path
from faster_whisper import WhisperModel

ROOT = Path(__file__).resolve().parents[2]
MIN_MATCH = 0.9
EDGE = 0.5
norm = lambda text: re.sub(r'[^a-z0-9]', '', text.lower())


def clips(week: str) -> dict[str, tuple[float, float]]:
  html = (ROOT / f'video/digital-literacy-2/{week}/index.html').read_text()
  found = re.findall(r'id="aud-(beat-\d+)"[^>]*data-start="([\d.]+)" data-duration="([\d.]+)"', html)
  return {beat: (float(start), float(start) + float(length)) for beat, start, length in found}


def transcribe(video: Path, model_name: str) -> list:
  model = WhisperModel(model_name, device='cpu', compute_type='int8', cpu_threads=4)
  segments, _ = model.transcribe(str(video), language='en', beam_size=5,
                                 word_timestamps=True, condition_on_previous_text=False)
  return [w for s in segments for w in s.words if norm(w.word)]


def chapter_report(beat: dict, words: list, spans: list[tuple[str, str]], span: dict[int, str | None]) -> dict:
  expected = [w for w, b in spans if b == beat['id']]
  heard = [words[i] for i in range(len(words)) if span.get(i) == beat['id']]
  match = difflib.SequenceMatcher(None, [norm(w) for w in expected], [norm(w.word) for w in heard], autojunk=False)
  ratio = sum(size for _, _, size in match.get_matching_blocks()) / len(expected)
  changes = [dict(expected=' '.join(expected[a:b]), recognized=' '.join(w.word.strip() for w in heard[c:d]))
             for op, a, b, c, d in match.get_opcodes() if op != 'equal']
  return dict(chapter=beat['id'], words=len(expected), matchRatio=round(ratio, 4),
              heardFrom=round(heard[0].start, 2) if heard else None,
              heardTo=round(heard[-1].end, 2) if heard else None, differences=changes)


def main() -> None:
  parser = argparse.ArgumentParser()
  parser.add_argument('--week', type=int, required=True)
  parser.add_argument('--model', default='small.en', choices=['base.en', 'small.en'])
  parser.add_argument('--out', type=Path, required=True)
  args = parser.parse_args()
  week = f'week-{args.week:02}'
  beats = json.loads((ROOT / f'video/digital-literacy-2/{week}/narration/beats.json').read_text())
  windows = clips(week)
  words = transcribe(ROOT / f'courses/digital-literacy-2/media/{week}.mp4', args.model)
  inside = lambda w: next((b for b, (s, e) in windows.items() if w.start <= e + EDGE and w.end >= s - EDGE), None)
  span = {i: inside(w) for i, w in enumerate(words)}
  spans = [(w, b['id']) for b in beats for w in b['text'].split()]
  chapters = [chapter_report(b, words, spans, span) for b in beats]
  stray = [dict(at=round(w.start, 2), word=w.word.strip()) for i, w in enumerate(words) if span[i] is None]
  report = dict(week=week, model=args.model, chapters=chapters, wordsOutsideNarration=stray)
  args.out.write_text(json.dumps(report, indent=2) + '\n')
  for c in chapters:
    print(c['chapter'], c['matchRatio'], c['heardFrom'], c['heardTo'], flush=True)
  print('words outside narration clips:', len(stray))
  low = [c['chapter'] for c in chapters if c['matchRatio'] < MIN_MATCH]
  if low or stray or len(windows) != len(beats):
    raise SystemExit(f'Review needed: low match {low}, {len(stray)} stray words, {len(windows)}/{len(beats)} clips')


if __name__ == '__main__':
  main()
