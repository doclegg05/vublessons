"""Import locally saved ElevenLabs MCP takes; never request or read API credentials.

Generate one MP3 per elevenlabs-britt/week-NN/beat-NN directory using the
parameters below and the matching beats.json text. Existing receipt hashes bind
those local source files to the script and prevent accidental stale reuse.
"""
import hashlib
import json
import shutil
import subprocess
from pathlib import Path

import soundfile as sf

ROOT = Path('video/digital-literacy-2')
PARAMETERS = dict(model='eleven_multilingual_v2', voice='iKrofGyA12WC0e6AhZ8B',
                  voiceName='Britt - Mild Appalachian Male Voice', speed=0.95,
                  stability=0.5, similarityBoost=0.8, style=0.1,
                  useSpeakerBoost=True, language='en', outputFormat='mp3_44100_128')


def digest(data):
  return hashlib.sha256(data).hexdigest()


# Validate the complete source batch before replacing any working narration.
jobs = []
for folder in sorted(ROOT.glob('week-*/narration')):
  beats = json.loads((folder / 'beats.json').read_text())
  for beat in beats:
    source_dir = ROOT / 'elevenlabs-britt' / folder.parent.name / beat['id']
    files = list(source_dir.glob('*.mp3'))
    if len(files) != 1:
      raise RuntimeError(f'{source_dir}: expected exactly one generated source MP3')
    source = files[0]
    receipt = dict(provider='ElevenLabs MCP', **PARAMETERS,
                   textSha256=digest(beat['text'].encode()),
                   sourceSha256=digest(source.read_bytes()), sourceFile=source.name)
    receipt_path = source_dir / 'receipt.json'
    if receipt_path.exists() and json.loads(receipt_path.read_text()) != receipt:
      raise RuntimeError(f'{source_dir}: receipt mismatch; generate a new matching take')
    jobs.append((folder, beat, source, receipt_path, receipt))

for folder, beat, source, receipt_path, receipt in jobs:
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
  state[beat['id']] = dict(engine='ElevenLabs', **PARAMETERS, draft=False,
                           textSha256=receipt['textSha256'],
                           sourceSha256=receipt['sourceSha256'],
                           sha256=digest(mp3.read_bytes()))
  state_path.write_text(json.dumps(state, indent=2) + '\n')
  print(folder.parent.name, beat['id'], round(duration, 2), 'seconds', flush=True)
