"""Fail when any DL2 video composition sets text below the 24px floor at 720p.

Scans, relative to the current directory:
  video/digital-literacy-2/week-0*/compositions/frames/*.html
  video/digital-literacy-2/week-0*/index.html
for CSS `font-size:NNpx` (style blocks and style attributes) and SVG
`font-size="NN"` attributes. Every occurrence under the floor is listed with
its file, how many times it occurs, and the text it applies to where that can
be found. Screen-share demos (data-screen-share="true", emitted by
screen-share-scenes.py) are tagged apart from diagram scenes (video-scenes.py).

Usage:
  python3 scripts/dl2/check-text-floor.py [--floor 24] [--screen-share-only]
Exit status 1 when anything is below the floor, 0 otherwise.
"""
import argparse
import html
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path('video/digital-literacy-2')
SVG_SIZE = re.compile(r'<([a-zA-Z][\w:-]*)\b[^>]*?\sfont-size="([\d.]+)(?:px)?"[^>]*>')
STYLE_BLOCK = re.compile(r'<style[^>]*>(.*?)</style>', re.S)
CSS_RULE = re.compile(r'([^{}]+)\{([^{}]*)\}')
CSS_SIZE = re.compile(r'font-size\s*:\s*([\d.]+)px')
INLINE_STYLE = re.compile(r'<([a-zA-Z][\w:-]*)\b[^>]*?\sstyle="([^"]*font-size[^"]*)"[^>]*>')
TAGS = re.compile(r'<[^>]+>')


def clip(value, limit=70):
    value = re.sub(r'\s+', ' ', html.unescape(TAGS.sub(' ', value))).strip()
    return value if len(value) <= limit else value[:limit - 1] + '…'


def text_after(markup, pos):
    """Text of the element that starts at pos, up to its first closing tag."""
    end = markup.find('</', pos)
    return clip(markup[pos:end if end != -1 else pos + 300])


def selector_text(markup, selector):
    """Text of the first element a simple .class or #id selector names."""
    last = selector.strip().split()[-1] if selector.strip() else ''
    match = re.search(r'([.#])([\w-]+)$', last)
    if not match:
        return ''
    attr = 'class' if match[1] == '.' else 'id'
    pattern = rf'<[^>]*\s{attr}="(?:[^"]*\s)?{re.escape(match[2])}(?:\s[^"]*)?"[^>]*>'
    element = re.search(pattern, markup)
    return text_after(markup, element.end()) if element else ''


def scan(markup, floor):
    """Yield (kind, size, context) for every font size under the floor."""
    for match in SVG_SIZE.finditer(markup):
        size = float(match[2])
        if size < floor:
            yield 'svg', size, f'<{match[1]}> "{text_after(markup, match.end())}"'
    for block in STYLE_BLOCK.finditer(markup):
        for rule in CSS_RULE.finditer(block[1]):
            for size in CSS_SIZE.findall(rule[2]):
                if float(size) < floor:
                    selector = rule[1].strip()
                    shown = selector_text(markup, selector.split(',')[-1])
                    yield 'css', float(size), f'{selector} "{shown}"'
    for match in INLINE_STYLE.finditer(markup):
        for size in CSS_SIZE.findall(match[2]):
            if float(size) < floor:
                yield 'css-inline', float(size), f'<{match[1]}> "{text_after(markup, match.end())}"'


def files():
    return sorted(ROOT.glob('week-0*/compositions/frames/*.html')) + sorted(ROOT.glob('week-0*/index.html'))


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--floor', type=float, default=24.0, help='minimum font size in px (default 24)')
    parser.add_argument('--screen-share-only', action='store_true', help='only scan screen-share demo scenes')
    args = parser.parse_args()
    targets = files()
    if not targets:
        print(f'check-text-floor: no compositions found under {ROOT.resolve()}', file=sys.stderr)
        return 2
    findings = Counter()
    scanned = 0
    for path in targets:
        markup = path.read_text(encoding='utf-8')
        source = 'screen-share' if 'data-screen-share="true"' in markup else 'diagram'
        if args.screen_share_only and source != 'screen-share':
            continue
        scanned += 1
        for kind, size, context in scan(markup, args.floor):
            findings[(str(path), source, kind, size, context)] += 1
    for (path, source, kind, size, context), count in sorted(findings.items()):
        print(f'{path}  [{source}] {kind} {size:g}px x{count}  {context}')
    total = sum(findings.values())
    verdict = 'FAIL' if total else 'PASS'
    print(f'{verdict}: {total} font-size occurrence(s) under {args.floor:g}px in {len({k[0] for k in findings})} of {scanned} file(s)')
    return 1 if total else 0


if __name__ == '__main__':
    sys.exit(main())
