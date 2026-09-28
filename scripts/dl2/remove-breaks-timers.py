"""One-off edit (2026-09-28): Britt teaches DL2 with no class break and no countdown timer,
and every Week 1 unit slide names the app (and file) learners work in.

Run from the repo root: python3 scripts/dl2/remove-breaks-timers.py
Safe to re-run: each step checks for its own finished state.
"""
import html
import json
import re
from pathlib import Path

ROOT = Path('courses/digital-literacy-2')
W1 = ROOT / 'weeks/week-01'
BREAK_MIN = 10
APPS = {
    'A': 'Windows Settings',
    'B': 'Windows Quick Settings <span class="file">speaker icon on the taskbar</span>',
    'C': 'Microsoft Word <span class="file">Community Supper Flyer.docx</span>',
    'D': 'Microsoft Outlook <span class="file">Calendar</span>',
    'E': 'Microsoft Word <span class="file">new blank document</span>',
}
WEEK5_ROSTER = ' Finish any challenge ratings on the roster.'


def drop_break(agenda, week):
    """Return a new agenda without the Break row; Apply and close keeps the 120 minutes."""
    kept = [list(row) for row in agenda if row[1] != 'Break']
    if len(kept) == len(agenda):
        return kept
    kept[-1][0] += BREAK_MIN
    if week == 5:
        check = next(r for r in kept if r[1].startswith('Individual check'))
        check[2] += WEEK5_ROSTER
    return kept


def plan_rows(agenda):
    rows, t = [], 0
    for minutes, phase, action in agenda:
        rows.append(f'<tr><td>{t}–{t+minutes} ({minutes} min)</td><td>{html.escape(phase)}</td>'
                    f'<td>{html.escape(action)}</td></tr>')
        t += minutes
    assert t == 120, t
    return ''.join(rows)


def fix_curriculum_and_plans():
    src = Path('scripts/dl2/curriculum.json')
    cur = json.loads(src.read_text())
    weeks = [dict(w, agenda=drop_break(w['agenda'], n)) for n, w in enumerate(cur['weeks'], 1)]
    src.write_text(json.dumps(dict(cur, weeks=weeks), indent=2) + '\n')
    for n, w in enumerate(weeks, 1):
        page = ROOT / f'weeks/week-{n:02}/lesson-plan.html'
        s = page.read_text()
        s = re.sub(r'<tr><td>0–.*?(?=</tbody></table>)', lambda m: plan_rows(w['agenda']), s, count=1, flags=re.S)
        page.write_text(s)


def shift(clock):
    """5:35..6:20 moves 10 minutes earlier; earlier times, 6:25 and 6:30 stay."""
    h, m = map(int, clock.split(':'))
    total = h * 60 + m
    if 5 * 60 + 35 <= total <= 6 * 60 + 20:
        total -= BREAK_MIN
    return f'{total // 60}:{total % 60:02}'


def label_units(s):
    def add(m):
        sec = m.group(0)
        if 'class="app"' in sec:
            return sec
        unit = m.group(1)
        return re.sub(r'(<div class="hud">.*?)(</div>)',
                      lambda h: f'{h.group(1)}<span class="app">{APPS[unit]}</span>{h.group(2)}', sec, count=1)
    return re.sub(r'<section class="slide"[^>]*data-unit="([A-E])".*?</section>', add, s, flags=re.S)


def fix_deck():
    p = W1 / 'presentation.html'
    s = p.read_text()
    had_break = '<!-- 13 · Break' in s  # the time shift and renumbering run once, with the break removal
    s = re.sub(r'  <!-- 13 · Break.*?</section>\n\n', '', s, flags=re.S)
    s = s.replace(' Break starts at 5:25.', ' Unit C starts at 5:25.')
    s = s.replace(' with one ten-minute break', '')
    # Times in notes and comments only; "4:30 PM" style event times are lesson content.
    if had_break:
        s = re.sub(r'(<aside class="notes">.*?</aside>|<!--.*?-->)',
                   lambda m: re.sub(r'\b[4-6]:[0-5]\d\b(?! ?PM)', lambda t: shift(t.group(0)), m.group(0)),
                   s, flags=re.S)
        s = re.sub(r'<!-- (1[4-9]|2\d) · ', lambda m: f'<!-- {int(m.group(1)) - 1} · ', s)
    s = re.sub(r'<div class="timer"><b>[\d:]+</b><small>TIME LEFT</small></div>', '', s)
    s = re.sub(r' data-minutes="\d+"', '', s)
    s = s.replace(' Press T to start the 12-minute timer; the flyer', ' The flyer')
    s = s.replace(' Press T to start the 10-minute timer, then walk the room.', ' Walk the room.')
    s = re.sub(r' Press T to start the \d+-minute timer\.', '', s)
    s = s.replace('Before time is up, have each person', 'Before moving on, have each person')
    s = s.replace('Before time is up, everyone clicks', 'Before moving on, everyone clicks')
    s = s.replace('In the last two minutes partners swap', 'To finish, partners swap')
    s = re.sub(r'<script>\n/\* The big \.timer.*?</script>\n', '', s, flags=re.S)
    p.write_text(label_units(s))


RUN_ROWS = [  # time, slides, segment, you do, learners do
    ('4:30', '1–2', 'Welcome + pre-test', 'Welcome learners by name; launch the pre-test.', None),
    ('4:50', '3–4', None, None, None),
    ('4:58', '5–8', None, 'Tell, show the demo, walk the room during Mission A, review.', None),
    ('5:13', '9–12', None, 'Tell, show the demo, walk the room during Mission B, review.', None),
    ('5:25', '13–16', None, 'Tell, show the demo, walk the room during Mission C, review.', None),
    ('5:40', '17–20', None, 'Tell, show the demo, walk the room during Mission D, review.', None),
    ('5:55', '21–25', None, 'Tell (undo + help request), show the demo, walk the room during Mission E, review.', None),
    ('6:10', '26–27', None, 'Prompt Take it home; let anyone finish a mission; congratulate; collect worksheets.', None),
]


def fix_run_sheet():
    p = W1 / 'run-sheet.html'
    s = p.read_text()
    s = re.sub(r'<tr><td>5:25</td><td>13</td><td>Break</td>.*?</tr>\n?', '', s)
    rows = re.findall(r'<tr><td>\d:\d\d</td>.*?</tr>', s)
    assert len(rows) == len(RUN_ROWS), len(rows)
    for old, (t, sl, _seg, you, _lr) in zip(rows, RUN_ROWS):
        cells = re.findall(r'<td>(.*?)</td>', old)
        cells[0], cells[1] = t, sl
        if you:
            cells[3] = html.escape(you, quote=False)
        s = s.replace(old, '<tr>' + ''.join(f'<td>{c}</td>' for c in cells) + '</tr>', 1)
    s = s.replace(' · T timer', '')
    p.write_text(s)


def fix_worksheet():
    p = W1 / 'worksheet.html'
    p.write_text(re.sub(r'(<span class="do">DO</span>)<span>\d+ min</span>', r'\1', p.read_text()))


if __name__ == '__main__':
    fix_curriculum_and_plans()
    fix_deck()
    fix_run_sheet()
    fix_worksheet()
    print('done')
