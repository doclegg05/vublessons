"""Refresh video chapter times and cache versions in existing learner pages.

The broad page generator also writes lessons and assessments. A narration-only
revision must preserve those classroom releases outside chapter times and media
URL versions. Captions and chapter titles remain bound to build-media.py.
"""
import hashlib
import json
import re
from pathlib import Path

root = Path('courses/digital-literacy-2/weeks')
pattern = re.compile(r'(data-video-seek=")[\d.]+("><time datetime="PT)[\d.]+(S">)\d+:\d+(</time>)')
for number in range(1, 7):
  week = f'week-{number:02}'
  beats = json.loads(Path(f'video/digital-literacy-2/{week}/narration/beats.json').read_text())
  updated = 0
  for page in sorted((root / week).glob('*.html')):
    source = page.read_text()
    # Week 1's current Mission Control presentation has no embedded video.
    # Its archived presentation still has a working player and chapter menu.
    if 'data-video-seek=' not in source:
      continue
    assert len(pattern.findall(source)) == len(beats), page
    iterator = iter(beats)
    def replace(match):
      seconds = next(iterator)['start']
      return f'{match[1]}{seconds:.3f}{match[2]}{seconds:.3f}{match[3]}{int(seconds)//60}:{int(seconds)%60:02}{match[4]}'
    source = pattern.sub(replace, source)
    # The media cache lasts a day. Version audio and captions independently so
    # a returning learner cannot combine old speech with new chapter timings.
    for suffix in ('mp4', 'vtt'):
      asset = Path(f'courses/digital-literacy-2/media/{week}.{suffix}')
      version = hashlib.sha256(asset.read_bytes()).hexdigest()[:12]
      media_pattern = re.escape('/' + str(asset)) + r'(?:\?[^"\s]*)?(?=")'
      source, count = re.subn(media_pattern, '/' + str(asset) + '?v=' + version, source)
      assert count == 1, f'{page}: expected one {suffix} reference'
    page.write_text(source)
    updated += 1
    print(page)
  assert updated == 2, f'{week}: expected one presentation and one transcript menu'
