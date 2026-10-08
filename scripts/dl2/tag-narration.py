"""Write a week's ElevenLabs prompt file: the narration text with delivery tags inserted.

  python3 scripts/dl2/tag-narration.py week-03

Reads video/digital-literacy-2/week-NN/narration/beats.json (the authored words) and
video/digital-literacy-2/week-NN/delivery.json (tag before phrase). Writes
video/digital-literacy-2/narration-prompts-week-NN.json for elevenlabs-takes.py.
Fails if a phrase is missing or ambiguous, or if the tagged prompt would speak different words.
"""
import json
import re
import sys
from pathlib import Path

MEDIA = Path('video/digital-literacy-2')


def tagged(text: str, plan: list) -> str:
    start = ' '.join(tag for phrase, tag in plan if not phrase)
    out = text
    for phrase, tag in plan:
        if not phrase:
            continue
        if out.count(phrase) != 1:
            raise SystemExit(f'{phrase!r} appears {out.count(phrase)} times; it must appear once')
        out = out.replace(phrase, f'{tag} {phrase}')
    out = f'{start} {out}' if start else out
    if ' '.join(re.sub(r'\[[^]]+\]', '', out).split()) != ' '.join(text.split()):
        raise SystemExit('Delivery tags changed the spoken words')
    return out


def main() -> None:
    week = sys.argv[1]
    beats = json.loads((MEDIA / week / 'narration/beats.json').read_text())
    plan = json.loads((MEDIA / week / 'delivery.json').read_text())
    prompts = {b['id']: tagged(b['text'], plan.get(b['id'], [])) for b in beats}
    doc = dict(voice='Dslrhjl3ZpzrctukrQSN', voiceName='Hey Its Brad - Clear Narrator for Documentary',
               prompts=prompts, texts={b['id']: b['text'] for b in beats})
    (MEDIA / f'narration-prompts-{week}.json').write_text(json.dumps(doc, indent=2) + '\n')
    print(f'{week}: {sum(len(p) for p in prompts.values())} characters in {len(prompts)} prompts')


if __name__ == '__main__':
    main()
