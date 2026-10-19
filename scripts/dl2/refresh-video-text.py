"""Refresh chapter titles and transcript text after a week's narration is rewritten.

  python3 scripts/dl2/refresh-video-text.py week-03

Writes, from video/digital-literacy-2/week-NN/narration/beats.json, cards.json and screen-share-actions.json:
- the chapter menu labels in the week's video-transcript.html and its practice-library template
  (scripts/dl2/mission-control/practice/week-NN.html), with " · Screen demo" on screen-demo chapters;
- the transcript sections, including each pause card's steps, because the card text is not spoken, and the
  screen-demonstration steps for each screen-demo chapter.
Chapter times and media versions are refresh-video-chapters.py's job; run it afterwards, then the
Mission Control build.
"""
import html
import json
import re
import sys
from pathlib import Path

E = lambda s: html.escape(str(s), quote=True)
MENU = re.compile(r'(data-video-seek="[\d.]+"><time datetime="PT[\d.]+S">\d+:\d+</time>)[^<]*(</button>)')


def labels(media: Path, beats: list) -> list:
    screens = {s['chapter'] for s in json.loads((media / 'screen-share-actions.json').read_text())}
    return [b['title'] + (' · Screen demo' if i + 1 in screens else '') for i, b in enumerate(beats)]


GUIDE = ('<details class="screen-demo-guide"><summary>Screen demonstration steps</summary><p>This is an original screen simulation '
         'with fictional practice data. Menus vary by application. Pause or replay each action before trying it yourself.</p><ol>{}</ol></details>')


def sections(beats: list, cards: dict, demos: dict) -> str:
    out = ''
    for i, b in enumerate(beats):
        out += f'<section><h2>{E(b["title"])}</h2><p>{E(b["text"])}</p>'
        if i + 1 in demos:
            # The steps are the text alternative for the screen demonstration.
            out += GUIDE.format(''.join(f'<li>{E(label)}</li>' for label in demos[i + 1]))
        pause = cards.get(b['id'], {}).get('pause')
        if pause:
            out += f'<p><strong>Pause card.</strong> {E(" ".join(pause["try"]))} Worksheet: {E(pause["where"])}.</p>'
        out += '</section>'
    return out


def relabel(page: Path, names: list) -> str:
    source = page.read_text()
    found = MENU.findall(source)
    if len(found) != len(names):
        raise SystemExit(f'{page}: {len(found)} chapter buttons for {len(names)} chapters')
    names_iter = iter(names)
    return MENU.sub(lambda m: m[1] + E(next(names_iter)) + m[2], source)


def main() -> None:
    week = sys.argv[1]
    media = Path('video/digital-literacy-2') / week
    beats = json.loads((media / 'narration/beats.json').read_text())
    cards_path = media / 'cards.json'
    cards = json.loads(cards_path.read_text())['chapters'] if cards_path.exists() else {}
    names = labels(media, beats)
    demos = {s['chapter']: [a['label'] for a in s['actions']] for s in json.loads((media / 'screen-share-actions.json').read_text())}
    template = Path(f'scripts/dl2/mission-control/practice/{week}.html')
    template.write_text(relabel(template, names))
    transcript = Path(f'courses/digital-literacy-2/weeks/{week}/video-transcript.html')
    source = relabel(transcript, names)
    source, count = re.subn(r'(<div id="transcript-content">).*?(</div><div class="actions">)',
                            lambda m: m[1] + sections(beats, cards, demos) + m[2], source, flags=re.S)
    if count != 1:
        raise SystemExit(f'{transcript}: transcript content not found')
    # A week with a glossary (Week 6) shows it above the transcript as "Words in this video".
    glossary = json.loads(Path('scripts/dl2/curriculum.json').read_text())['weeks'][int(week[-2:]) - 1].get('glossary')
    if glossary:
        words = ''.join(f'<dt>{E(term)}</dt><dd>{E(text)}</dd>' for term, text in glossary)
        source, count = re.subn(r'(<section class="video-words"[^>]*><h2[^>]*>Words in this video</h2><dl>).*?(</dl>)',
                                lambda m: m[1] + words + m[2], source, flags=re.S)
        if count != 1:
            raise SystemExit(f'{transcript}: glossary box not found')
    transcript.write_text(source)
    print(f'{week}: {len(names)} chapter labels and transcript sections refreshed')


if __name__ == '__main__':
    main()
