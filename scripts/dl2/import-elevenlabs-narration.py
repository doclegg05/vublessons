import argparse
"""Import locally saved ElevenLabs MCP takes; never request or read API credentials.

Generate one raw V3 MP3 and one Voice Isolator MP3 per chapter in the
Desktop vub-deep-narration workspace using the parameters below and prompt.txt. Existing receipt hashes bind
those local source files to the script and prevent accidental stale reuse.
"""
import hashlib
import json
import re
import shutil
import subprocess
from pathlib import Path

import soundfile as sf

ROOT = Path('video/digital-literacy-2')
parser = argparse.ArgumentParser()
parser.add_argument('week', nargs='?', default='week-*')
parser.add_argument('--profile', choices=['deep', 'expressive'], default='deep')
args = parser.parse_args()
LOCAL = Path.home() / f'Desktop/vub-{args.profile}-narration'
PARAMETERS = dict(model='eleven_v3', voice='iKrofGyA12WC0e6AhZ8B',
                  voiceName='Britt - Mild Appalachian Male Voice', speed=0.95,
                  stability=0.5, similarityBoost=0.8, style=0,
                  useSpeakerBoost=False, language='en', outputFormat='mp3_44100_128')
if args.profile == 'expressive':
  PARAMETERS = json.loads((ROOT / 'elevenlabs-britt-v3-expressive/profile.json').read_text())
  checks = {(c['week'], c['chapter']): c for c in json.loads(
    (ROOT / 'elevenlabs-britt-v3-expressive/transcription-checks.json').read_text())}


def digest(data):
  return hashlib.sha256(data).hexdigest()


# Validate the complete source batch before replacing any working narration.
jobs = []
for folder in sorted(ROOT.glob(args.week+'/narration')):
  beats = json.loads((folder / 'beats.json').read_text())
  for beat in beats:
    local = LOCAL / folder.parent.name / beat['id']
    source_dir = ROOT / f'elevenlabs-britt-v3-{args.profile}' / folder.parent.name / beat['id']
    raw_files = list((local / 'raw').glob('*.mp3'))
    clean_files = list((local / 'clean').glob('*.mp3'))
    if len(raw_files) != 1 or len(clean_files) != 1:
      raise RuntimeError(f'{local}: expected one raw and one isolated take')
    source = clean_files[0]
    if args.profile == 'expressive':
      check = checks.get((folder.parent.name, beat['id']), {})
      if (check.get('sha256') != digest(source.read_bytes()) or
          check.get('matchRatio', 0) < .87 or
          not 100 <= check.get('wordsPerMinute', 0) <= 185):
        raise RuntimeError(f'{local}: missing or unsuccessful transcription/pacing preflight')
    prompt = (local / 'prompt.txt').read_text()
    spoken = re.sub(r'\[[^]]+\]', '', prompt)
    if ' '.join(spoken.split()) != ' '.join(beat['text'].split()):
      raise RuntimeError(f'{source_dir}: prompt changes the authored narration')
    parameters = (json.loads((local / 'generation-settings.json').read_text())
                  if args.profile == 'expressive' else PARAMETERS)
    receipt = dict(provider='ElevenLabs MCP', **parameters,
                   cleanup='ElevenLabs Voice Isolator',
                   originalSha256=digest(raw_files[0].read_bytes()),
                   textSha256=digest(beat['text'].encode()),
                   promptSha256=digest((local / 'prompt.txt').read_bytes()),
                   sourceSha256=digest(source.read_bytes()), sourceFile='isolated.mp3')
    receipt_path = source_dir / 'receipt.json'
    if receipt_path.exists() and json.loads(receipt_path.read_text()) != receipt:
      raise RuntimeError(f'{source_dir}: receipt mismatch; generate a new matching take')
    jobs.append((folder, beat, source, receipt_path, receipt, raw_files[0], local))

for folder, beat, source, receipt_path, receipt, original, local in jobs:
  receipt_path.parent.mkdir(parents=True, exist_ok=True)
  shutil.copyfile(original, receipt_path.parent / 'original.mp3')
  shutil.copyfile(source, receipt_path.parent / 'isolated.mp3')
  shutil.copyfile(local / 'prompt.txt', receipt_path.parent / 'prompt.txt')
  raw = folder / (beat['id'] + '.raw.wav')
  wav = folder / (beat['id'] + '.wav')
  # Decode the provider source anew: do not tempo-adjust the old fallback audio.
  subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(source),
                  '-c:a', 'pcm_s16le', str(raw)], check=True)
  shutil.copyfile(raw, wav)
  duration = sf.info(str(wav)).duration
  if duration <= 0:
    raise RuntimeError(f'{source}: empty decoded audio')
  receipt_path.write_text(json.dumps(receipt, indent=2) + '\n')
  state_path = folder / 'take-state.json'
  state = json.loads(state_path.read_text()) if state_path.exists() else {}
  mp3 = folder / (beat['id'] + '.mp3')
  shutil.copyfile(source, mp3)
  state[beat['id']] = dict(engine='ElevenLabs', **{key: receipt[key] for key in PARAMETERS}, draft=False,
                           performanceProfile=args.profile,
                           textSha256=receipt['textSha256'],
                           cleanup=receipt['cleanup'],
                           originalSha256=receipt['originalSha256'],
                           sourceSha256=receipt['sourceSha256'],
                           sha256=digest(mp3.read_bytes()))
  state_path.write_text(json.dumps(state, indent=2) + '\n')
  print(folder.parent.name, beat['id'], round(duration, 2), 'seconds', flush=True)
