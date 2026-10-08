"""Make narration takes straight from the ElevenLabs HTTP API, one week at a time.

Replaces the old ElevenLabs MCP step. Takes land where
import-elevenlabs-narration.py --profile brad-refresh expects them:
  $VUB_TAKES_DIR/week-NN/beat-NN/{prompt.txt, generation-settings.json, raw/, clean/}
VUB_TAKES_DIR defaults to ~/Desktop/vub-brad-narration-refresh. Prompts (the script with delivery
tags) come from video/digital-literacy-2/narration-prompts-week-NN.json; Week 2 keeps its
ai-search-prompts-week-02.json.

The key is read from ELEVENLABS_API_KEY in ./.env (gitignored) or the environment. It is never printed.

  python3 scripts/dl2/elevenlabs-takes.py quota
  python3 scripts/dl2/elevenlabs-takes.py stage --week week-03                # back up old takes, write prompt.txt files
  python3 scripts/dl2/elevenlabs-takes.py generate beat-02 --week week-03 --go # spends characters; omit --go for a dry run
"""
import argparse
import json
import os
import shutil
import sys
import urllib.error
import urllib.request
import uuid
from pathlib import Path

API = 'https://api.elevenlabs.io/v1'
ROOT = Path(__file__).resolve().parents[2]
TAKES = Path(os.environ.get('VUB_TAKES_DIR', Path.home() / 'Desktop/vub-brad-narration-refresh'))


def paths(week: str) -> tuple:
    """Prompt file, local take folder and backup folder for one week."""
    media = ROOT / 'video/digital-literacy-2'
    prompts = media / ('ai-search-prompts-week-02.json' if week == 'week-02' else f'narration-prompts-{week}.json')
    local = TAKES / week
    return prompts, local, local / ('_before-ai-search' if week == 'week-02' else '_before-rewrite')
SETTINGS = dict(model='eleven_v3', voice='Dslrhjl3ZpzrctukrQSN', voiceName='Hey Its Brad - Clear Narrator for Documentary',
                speed=0.95, stability=0.5, similarityBoost=0.8, style=0, useSpeakerBoost=False, language='en',
                outputFormat='mp3_44100_128')


def load_key() -> str:
    env = ROOT / '.env'
    if env.exists():
        for line in env.read_text().splitlines():
            if line.startswith('ELEVENLABS_API_KEY='):
                return line.split('=', 1)[1].strip()
    key = os.environ.get('ELEVENLABS_API_KEY', '')
    if not key:
        sys.exit('No ELEVENLABS_API_KEY in .env or the environment.')
    return key


def call(request: urllib.request.Request) -> bytes:
    try:
        with urllib.request.urlopen(request, timeout=300) as response:
            return response.read()
    except urllib.error.HTTPError as err:
        sys.exit(f'ElevenLabs returned HTTP {err.code}: {err.read().decode()[:300]}')


def quota(key: str) -> None:
    data = json.loads(call(urllib.request.Request(f'{API}/user/subscription', headers={'xi-api-key': key})))
    left = data['character_limit'] - data['character_count']
    print(f"tier {data.get('tier')}: {data['character_count']} of {data['character_limit']} characters used, {left} left")


def speak(key: str, text: str, settings: dict) -> bytes:
    body = json.dumps(dict(text=text, model_id=settings['model'], language_code=settings['language'], voice_settings=dict(
        stability=settings['stability'], similarity_boost=settings['similarityBoost'], style=settings['style'],
        use_speaker_boost=settings['useSpeakerBoost'], speed=settings['speed']))).encode()
    url = f"{API}/text-to-speech/{settings['voice']}?output_format={settings['outputFormat']}"
    return call(urllib.request.Request(url, data=body, method='POST', headers={'xi-api-key': key, 'Content-Type': 'application/json'}))


def isolate(key: str, audio: bytes) -> bytes:
    boundary = uuid.uuid4().hex
    head = f'--{boundary}\r\nContent-Disposition: form-data; name="audio"; filename="take.mp3"\r\nContent-Type: audio/mpeg\r\n\r\n'.encode()
    body = head + audio + f'\r\n--{boundary}--\r\n'.encode()
    return call(urllib.request.Request(f'{API}/audio-isolation', data=body, method='POST', headers={
        'xi-api-key': key, 'Content-Type': f'multipart/form-data; boundary={boundary}'}))


def stage(beats: dict, local: Path, backup: Path, names: list, speed: float) -> None:
    """Write prompt files and clear raw/clean takes, for the named beats only (all beats when none are named)."""
    backup.mkdir(parents=True, exist_ok=True)
    for beat, prompt in beats['prompts'].items():
        if names and beat not in names:
            continue
        folder = local / beat
        if folder.exists() and not (backup / beat).exists():
            shutil.copytree(folder, backup / beat)
        for sub in ('raw', 'clean'):
            shutil.rmtree(folder / sub, ignore_errors=True)
            (folder / sub).mkdir(parents=True, exist_ok=True)
        (folder / 'prompt.txt').write_text(prompt)
        (folder / 'generation-settings.json').write_text(json.dumps(dict(SETTINGS, speed=speed), indent=2) + '\n')
        print(f'staged {beat} ({len(prompt)} characters); old take kept in {backup / beat}')


def generate(key: str, beats: dict, names: list, go: bool, local: Path) -> None:
    for beat in names:
        prompt = beats['prompts'][beat]
        if not go:
            print(f'dry run: {beat} would send {len(prompt)} characters, then isolate the voice')
            continue
        folder = local / beat
        # The staged settings file is what the importer records, so generate with exactly those settings.
        raw = speak(key, prompt, json.loads((folder / 'generation-settings.json').read_text()))
        (folder / 'raw' / f'tts_{beat}.mp3').write_bytes(raw)
        (folder / 'clean' / f'iso_tts_{beat}.mp3').write_bytes(isolate(key, raw))
        print(f'{beat}: raw {len(raw)} bytes, isolated take saved under {folder}')


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['quota', 'stage', 'generate'])
    parser.add_argument('beats', nargs='*')
    parser.add_argument('--go', action='store_true')
    parser.add_argument('--week', default='week-02')
    parser.add_argument('--speed', type=float, default=SETTINGS['speed'], help='slower takes for fast chapters, for example 0.85')
    args = parser.parse_args()
    prompts, local, backup = paths(args.week)
    if args.command == 'stage':
        return stage(json.loads(prompts.read_text()), local, backup, args.beats, args.speed)
    key = load_key()
    quota(key) if args.command == 'quota' else generate(key, json.loads(prompts.read_text()), args.beats, args.go, local)


if __name__ == '__main__':
    main()
