"""Schematic Microsoft 365, Windows 10 and Microsoft Edge screens for the DL2 deck.

These are original teaching diagrams, not screenshots: HTML/CSS only (no images, logos,
web fonts or JS). Each public function returns one string:

    <div class="ui ui-NAME" role="img" aria-label="...">...</div>

Styles live in courses/digital-literacy-2/os/ui-drawings.css. Every size there is in cqw of
the 16:9 .deck, so a drawing scales with the projector. Rules the markup keeps:

- div/span only. The deck forces font sizes on p/li/td/th/h1/h2 with !important and styles
  kbd/b/em/small inside some slide parts, so none of those tags appear in a drawing.
- A thing to click is ringed (.u-t, a gold ring with dark edges) AND carries a numbered
  badge (.u-bd), so the meaning never rests on colour alone. Its label uses .u-big
  (at least 1.6cqw, bold). No text anywhere is smaller than 1.15cqw.
- Ribbon tab rows and ribbon bands always fit the column: targets always show, and other
  tabs / groups / buttons are left out (least useful first) when space is short.
"""
import re
from html import escape

__all__ = [
    'app_badge', 'start_search', 'office_start', 'ribbon', 'word_styles', 'word_numbering',
    'word_page', 'word_navpane', 'file_menu', 'save_as_dialog', 'savetype_list', 'pdf_view',
    'excel_grid', 'ppt_window', 'ppt_themes', 'ppt_insert_pictures', 'insert_picture_dialog',
    'ppt_crop', 'designer_pane', 'edge_page_download', 'explorer_resource_pack', 'vub_course_path',
]

APPS = {
    'word': {'name': 'Word', 'doc': 'Document1', 'blank': 'Blank document'},
    'excel': {'name': 'Excel', 'doc': 'Book1', 'blank': 'Blank workbook'},
    'powerpoint': {'name': 'PowerPoint', 'doc': 'Presentation1', 'blank': 'Blank presentation'},
}
_LETTERS = {'word': 'W', 'excel': 'X', 'powerpoint': 'P', 'edge': 'e', 'explorer': 'F', 'mail': 'M', 'settings': 'S', 'outlook': 'O'}

TABS = {
    'word': ['File', 'Home', 'Insert', 'Draw', 'Design', 'Layout', 'References', 'Mailings',
             'Review', 'View', 'Help'],
    'excel': ['File', 'Home', 'Insert', 'Draw', 'Page Layout', 'Formulas', 'Data', 'Review',
              'View', 'Help'],
    'powerpoint': ['File', 'Home', 'Insert', 'Draw', 'Design', 'Transitions', 'Animations',
                   'Slide Show', 'Review', 'View', 'Help'],
}

SAVE_TYPES = ['Word Document (*.docx)', 'Word Macro-Enabled Document (*.docm)',
              'Word 97-2003 Document (*.doc)', 'Word Template (*.dotx)', 'PDF (*.pdf)',
              'XPS Document (*.xps)', 'Web Page (*.htm;*.html)', 'Rich Text Format (*.rtf)',
              'Plain Text (*.txt)']


# ---------------------------------------------------------------- small helpers

def _e(s):
    return escape(str(s), quote=True)


def _tw(text, size, bold=False):
    """Rough rendered width in cqw; generous so wide fallback fonts still fit."""
    return len(str(text)) * size * (0.64 if bold else 0.58)


def _marks(targets):
    """targets -> {key: (number, badge_position_or_None)}; an entry may be (key, pos)."""
    out = {}
    for i, t in enumerate(targets or (), 1):
        key, pos = (t[0], t[1]) if isinstance(t, (tuple, list)) else (t, None)
        out[key] = (i, pos)
    return out


def _get(marks, key, default='tr'):
    n, pos = marks.get(key, (0, None))
    return n, (pos or default)


def _bd(n, pos='tr'):
    return f'<span class="u-bd u-p-{pos}">{n}</span>' if n else ''


def _t(n):
    return ' u-t' if n else ''


def _lab(text, n):
    return f'<span class="u-big">{_e(text)}</span>' if n else _e(text)


def _join(items):
    items = [i for i in items if i]
    if len(items) <= 1:
        return ''.join(items)
    if len(items) == 2:
        return f'{items[0]} and {items[1]}'
    return ', '.join(items[:-1]) + ', and ' + items[-1]


def _said(pairs):
    """[('the Save button', 1), ...] -> ' The Save button is marked 1, and ...'"""
    s = _join([f'{what} is marked {n}' for what, n in sorted(pairs, key=lambda p: p[1])])
    return f' {s[0].upper()}{s[1:]}.' if s else ''


def _root(name, label, inner):
    return f'<div class="ui ui-{name}" role="img" aria-label="{_e(label)}">{inner}</div>'


def _wc():
    return ('<span class="u-wc"><span class="u-min"></span><span class="u-max"></span>'
            '<span class="u-x"></span></span>')


def _title(text, icon=''):
    return f'<div class="u-tb">{icon}<span class="u-tt">{_e(text)}</span>{_wc()}</div>'


def _win(kind, inner, app=''):
    return f'<div class="u-w u-{kind}{" u-" + app if app else ""}">{inner}</div>'


def _dd():
    return '<span class="u-dd"></span>'


# ---------------------------------------------------------------- ribbon pieces

def _tabrow(app, active, marks, extra=(), budget=38.5):
    """Tab row in real order that always fits the column.

    Active and targeted tabs always show. When space is short, other tabs are left out:
    Draw and Help first, then the tabs farthest from a shown target (longest first), and
    File/Home last. Tab badges sit above each tab, offset right, so neighbours never collide.
    """
    tabs = TABS[app] + list(extra)
    idx = {t: i for i, t in enumerate(tabs)}

    def wid(t):
        n, pos = _get(marks, t, 'ta')
        if n:
            return _tw(t, 1.6, True) + 1.1 + 1.2 + .2 + (3.4 if pos in ('r', 'l') else 0)
        return _tw(t, 1.15, t == active) + .9 + .2

    must = [t for t in tabs if t == active or t in marks]
    mi = [idx[t] for t in must] or [0]
    keep = list(tabs)

    def score(t):
        if t in ('Draw', 'Help'):
            return (0, 0, 0)
        if t in ('File', 'Home'):
            return (2, 0, 0)
        return (1, -min(abs(idx[t] - m) for m in mi), -len(t))

    for t in sorted((t for t in tabs if t not in must), key=score):
        if sum(wid(k) for k in keep) <= budget:
            break
        keep.remove(t)
    out, lane = [], ''
    for t in keep:
        n, pos = _get(marks, t, 'ta')
        lane = ' u-tabs-mk' if n and pos == 'ta' else lane
        cls = ('u-tab' + (' u-on' if t == active else '') + (' u-ctx' if t in extra else '') + _t(n))
        out.append(f'<span class="{cls}">{_lab(t, n)}{_bd(n, pos)}</span>')
    return f'<div class="u-tabs{lane}">{"".join(out)}</div>'


_GLYPHS = (('picture', 'pic'), ('album', 'pic'), ('crop', 'crop'), ('table', 'tbl'),
           ('slide', 'sld'), ('shape', 'shp'), ('icons', 'shp'), ('correction', 'adj'),
           ('color', 'clr'), ('zoom', 'zm'), ('100%', 'zm'), ('screenshot', 'scr'))


def _glyph(label):
    low = label.lower()
    for key, g in _GLYPHS:
        if key in low:
            return f'<span class="u-g u-g-{g}"></span>'
    return '<span class="u-g"></span>'


def _is_small(label):
    return label[:4] in ('[x] ', '[ ] ') or label.startswith('~')


def _txt(label):
    if label[:4] in ('[x] ', '[ ] '):
        return label[4:]
    return label[1:] if label.startswith('~') else label


def _small(label, marks):
    text = _txt(label)
    box = ''
    if label[:4] in ('[x] ', '[ ] '):
        box = f'<span class="u-cb{" u-on" if label[1] == "x" else ""}"></span>'
    n, pos = _get(marks, text, 'r')
    cls = 'u-chk' + ('' if box else ' u-fld') + _t(n)
    return f'<span class="{cls}">{box}<span>{_lab(text, n)}</span>{_bd(n, pos)}</span>'


def _bigbtn(label, marks, pressed=(), menus=None):
    n, pos = _get(marks, label, 'tr2')
    down = ' u-down' if label in pressed else ''
    menu = (menus or {}).get(label, '')
    return (f'<span class="u-btn{down}{_t(n)}">{_glyph(label)}<span class="u-bl">{_lab(label, n)}'
            f'</span>{_bd(n, pos)}{menu}</span>')


def _iw(label, marks):
    """Estimated width (cqw) of one ribbon item, including a target's ring margin."""
    text = _txt(label)
    n, pos = _get(marks, text, 'r' if _is_small(label) else 'tr2')
    w = _tw(text, 1.6, True) if n else _tw(text, 1.2 if _is_small(label) else 1.15)
    if _is_small(label):
        return w + 2.6 + (1.2 if n else 0) + (3.4 if n and pos == 'r' else 0)
    return max(2.6, w) + .9 + (1.2 if n else 0)


def _gw(name, items, marks):
    w, stack, count = 0.0, 0.0, 0
    for it in items:
        if _is_small(it):
            stack = max(stack, _iw(it, marks))
            continue
        if stack:
            w, stack, count = w + stack, 0.0, count + 1
        w, count = w + _iw(it, marks), count + 1
    if stack:
        w, count = w + stack, count + 1
    w += .45 * max(0, count - 1)
    return max(w, _tw(name, 1.15) + .4) + 1.6


def _group(name, items, marks, pressed=(), menus=None, raw=None):
    if raw is None:
        parts, stack = [], []
        for it in items:
            if _is_small(it):
                stack.append(_small(it, marks))
                continue
            if stack:
                parts.append('<span class="u-stk">' + ''.join(stack) + '</span>')
                stack = []
            parts.append(_bigbtn(it, marks, pressed, menus))
        if stack:
            parts.append('<span class="u-stk">' + ''.join(stack) + '</span>')
        raw = ''.join(parts)
    return f'<span class="u-grp"><span class="u-gi">{raw}</span><span class="u-gn">{_e(name)}</span></span>'


def _band(groups, marks, pressed=(), menus=None, budget=38.5):
    """Ribbon band that always fits the column. Groups holding a target always show.
    When space is short: groups without a target go first (farthest from a target first),
    then buttons without a target inside target groups (farthest, then longest, first)."""
    names = [g for g, _ in groups]
    keep = [list(its) for _, its in groups]
    hit = [i for i, its in enumerate(keep) if any(_txt(it) in marks for it in its)]
    alive = [True] * len(groups)

    def total():
        return sum(_gw(names[i], keep[i], marks) for i in range(len(groups)) if alive[i])

    def dist(i):
        return min(abs(i - j) for j in hit) if hit else len(groups) - i

    for i in sorted((i for i in range(len(groups)) if i not in hit), key=lambda i: (-dist(i), i)):
        if total() <= budget:
            break
        alive[i] = False
    if total() > budget:
        cands = []
        for i in hit:
            ti = [k for k, it in enumerate(keep[i]) if _txt(it) in marks]
            cands += [(-min(abs(k - t) for t in ti), -len(_txt(it)), i, it)
                      for k, it in enumerate(keep[i]) if _txt(it) not in marks]
        for _, _, i, it in sorted(cands):
            if total() <= budget:
                break
            keep[i].remove(it)
    html = ''.join(_group(names[i], keep[i], marks, pressed, menus)
                   for i in range(len(groups)) if alive[i])
    return f'<div class="u-rb">{html}</div>'


def _doc_stub(app):
    return f'<div class="u-doc u-doc-{app}"><span class="u-stub"></span></div>'


def _what(app, key, extra=()):
    return f'the {key} tab' if key in TABS[app] or key in extra else f'the {key} button'


def ribbon(app, active_tab, groups, targets=(), *, extra_tabs=(), pressed=(), menus=None,
           below=None, name='ribbon', label=None):
    """App window top: title bar, tab row (real order), and a ribbon band of `groups`.

    groups: [(group_name, [button labels])]. A label written '[x] Name' / '[ ] Name' is a
    checkbox and '~Text' a small stacked item; both stack in a column like Office.
    targets: labels (tab names or button labels, without the '[x] '/'~' prefix) to ring and
    number in list order; an entry may be (label, badge_pos) with badge_pos one of
    tr tl br bl r l t b ir.
    """
    a = APPS[app]
    marks = _marks(targets)
    inner = (_title(f'{a["doc"]} - {a["name"]}') + _tabrow(app, active_tab, marks, extra_tabs)
             + _band(groups, marks, pressed, menus))
    inner += _doc_stub(app) if below is None else below
    if label is None:
        names = [g for g, _ in groups]
        label = (f'Drawing: {a["name"]} window with the {active_tab} tab open. The ribbon shows the '
                 f'{_join(names)} group{"s" if len(names) > 1 else ""}.'
                 + _said([(_what(app, k, extra_tabs), n) for k, (n, _) in marks.items()]))
    return _root(name, label, _win('app', inner, app))


def _cap(app, text):
    return (f'<div class="u-cap">{app_badge(app)}<span class="u-capt">{_e(text)}</span>'
            '<span class="u-zoomed"><span class="u-lens"></span>Zoomed in</span></div>')


# ---------------------------------------------------------------- 0. app badge

def app_badge(app, size='sm'):
    """Rounded square with a white letter: word W, excel X, powerpoint P, edge e, explorer F."""
    key = app if app in _LETTERS else 'word'
    size = 'lg' if size == 'lg' else 'sm'
    return (f'<span class="app-badge app-badge-{key} app-badge-{size}" aria-hidden="true">'
            f'{_LETTERS[key]}</span>')


# ---------------------------------------------------------------- 1. Windows search

def start_search(app='word'):
    name = APPS[app]['name']
    left = ('<div class="u-sl"><div class="u-sh">Best match</div>'
            f'<div class="u-res u-t">{app_badge(app)}<span class="u-rt"><span class="u-big">{_e(name)}</span>'
            f'<span class="u-sub">App</span></span>{_bd(3, "ir")}</div>'
            '<div class="u-sh">Search the web</div>'
            f'<div class="u-res2"><span class="u-mag"></span><span>{_e(name)} - See web results</span></div></div>')
    right = (f'<div class="u-sr">{app_badge(app, "lg")}<span class="u-pn">{_e(name)}</span>'
             '<span class="u-sub">App</span><span class="u-open"><span class="u-sq"></span>Open</span></div>')
    bar = ('<div class="u-task"><span class="u-start u-t"><span class="u-win4"><span></span><span></span>'
           f'<span></span><span></span></span>{_bd(1, "tr")}</span>'
           '<span class="u-sbox"><span class="u-mag u-magw"></span>'
           f'<span class="u-typed u-t"><span class="u-big">{_e(name)}</span><span class="u-caret"></span>'
           f'{_bd(2, "r")}</span></span><span class="u-tbi"></span><span class="u-tbi"></span></div>')
    label = (f'Drawing: Windows search. The Start button is marked 1, the typed word {name} is marked 2, '
             f'and the {name} app result under Best match is marked 3.')
    return _root('start-search', label, _win('win10', f'<div class="u-sp">{left}{right}</div>{bar}'))


# ---------------------------------------------------------------- 2. Office start screen

def office_start(app='word'):
    a = APPS[app]
    side = (f'<div class="u-os-side"><span class="u-os-nm">{_e(a["name"])}</span>'
            + ''.join(f'<span class="u-os-i{" u-on" if i == 0 else ""}"><span class="u-os-g u-os-g{i}"></span>'
                      f'{_e(t)}</span>' for i, t in enumerate(('Home', 'New', 'Open'))) + '</div>')
    th = f'<span class="u-th u-th-{app}"><span class="u-thi"></span></span>'
    tiles = (f'<span class="u-tile u-t">{th}<span class="u-tl"><span class="u-big">{_e(a["blank"])}</span>'
             f'</span>{_bd(1, "tr")}</span>'
             f'<span class="u-tile u-dim">{th.replace("u-th ", "u-th u-busy ")}<span class="u-tl">Take a tour</span></span>'
             f'<span class="u-tile u-dim">{th.replace("u-th ", "u-th u-busy ")}<span class="u-tl">Welcome to {_e(a["name"])}</span></span>')
    main = f'<div class="u-os-main"><div class="u-os-h">New</div><div class="u-tiles">{tiles}</div></div>'
    inner = _title(a['name']) + f'<div class="u-os">{side}{main}</div>'
    label = (f'Drawing: the {a["name"]} start screen. Home is selected on the left. Under New, the '
             f'{a["blank"]} tile is marked 1. Other tiles are greyed out.')
    return _root('office-start', label, _win('app', inner, app))


# ---------------------------------------------------------------- 4. Word styles

def word_styles(highlight='Heading 1'):
    tiles = []
    for nm, smp, cls in (('Normal', 'AaBbCcDd', 'n'), ('No Spacing', 'AaBbCcDd', 'n'),
                         ('Heading 1', 'AaBbCc', 'h1'), ('Heading 2', 'AaBbCcD', 'h2'),
                         ('Title', 'AaB', 'ti')):
        n = 1 if nm == highlight else 0
        tiles.append(f'<span class="u-sty u-sty-{cls}{_t(n)}"><span class="u-smp">{smp}</span>'
                     f'<span class="u-sn">{_lab(nm, n)}</span>{_bd(n, "tr")}</span>')
    body = ('<div class="u-mb"><div class="u-gal">' + ''.join(tiles)
            + '<span class="u-more"><span></span><span></span><span></span></span></div>'
            '<div class="u-gn u-gnc">Styles</div></div>')
    label = ('Drawing: Word, Home tab, Styles gallery, zoomed in. It shows the styles Normal, No Spacing, '
             f'Heading 1, Heading 2 and Title. The {highlight} style is marked 1.')
    return _root('word-styles', label, _win('zoom', _cap('word', 'Home tab \u203a Styles') + body, 'word'))


# ---------------------------------------------------------------- 5. Word numbering

def word_numbering():
    def ico(kind, marks):
        rows = ''.join(f'<span class="u-lv{i if kind == "mul" else 0}">{m}<span class="u-ln2"></span></span>'
                       for i, m in enumerate(marks))
        return f'<span class="u-ico u-ico-{kind}">{rows}</span>'
    dot = '<span class="u-dot"></span>'
    bul = ico('bul', [dot] * 3)
    num = ico('num', [f'<span class="u-dg">{d}</span>' for d in '123'])
    mul = ico('mul', [f'<span class="u-dg">{d}</span>' for d in ('1', 'a', 'i')])
    row1 = (f'<span class="u-pb">{bul}{_dd()}</span>'
            f'<span class="u-pb u-t">{num}{_dd()}{_bd(1, "tl")}<span class="u-ptr"></span></span>'
            f'<span class="u-pb">{mul}{_dd()}</span>')
    row2 = ''.join(f'<span class="u-ab u-ab-{k}"><span></span><span></span><span></span><span></span></span>'
                   for k in 'lcrj')
    group = (f'<div class="u-para"><div class="u-prow">{row1}</div><div class="u-prow">{row2}</div>'
             '<div class="u-gn u-gnc">Paragraph</div></div>')
    tip = ('<div class="u-tip"><span class="u-big">Numbering</span>'
           '<span class="u-tipd">Create a numbered list.</span></div>')
    label = ('Drawing: Word, Home tab, Paragraph group, zoomed in. It shows the Bullets, Numbering and '
             'Multilevel List buttons and the alignment buttons. The Numbering button is marked 1, '
             'and its tooltip reads Numbering.')
    inner = _cap('word', 'Home tab \u203a Paragraph') + f'<div class="u-mb u-nb">{group}{tip}</div>'
    return _root('word-numbering', label, _win('zoom', inner, 'word'))


# ---------------------------------------------------------------- 6. Word page

def _page_lines(lines, selected, numbered, cursor=True):
    rows, k = [], 0
    for i, (text, style) in enumerate(lines):
        cur = '<span class="u-cur"></span>' if cursor and i == len(lines) - 1 else ''
        style = style if style in ('h1', 'h2', 'body', 'step') else 'body'
        if style == 'step':
            k += 1
            num = f'<span class="u-num">{k}.</span>' if numbered else ''
            cls = 'u-ln u-step' + (' u-hl' if selected else '') + (' u-numd' if numbered else '')
            rows.append(f'<div class="{cls}">{num}<span class="u-lt">{_e(text)}{cur}</span></div>')
        else:
            rows.append(f'<div class="u-ln u-{style}"><span class="u-lt">{_e(text)}{cur}</span></div>')
    return ''.join(rows)


def _page_height(lines, width, scale=1.0):
    size = {'h1': 1.9, 'h2': 1.5, 'body': 1.25, 'step': 1.25}
    lead = {'h1': 1.2, 'h2': 1.25, 'body': 1.4, 'step': 1.45}
    gap = {'h1': .5, 'h2': .75, 'body': 0, 'step': 0}
    h = 0.0
    for text, style in lines:
        st = style if style in size else 'body'
        sz = max(1.15, size[st] * scale)
        per = max(1, int((width - (2.6 if st == 'step' else 0)) / (sz * .58)))
        h += -(-len(text) // per) * sz * lead[st] + gap[st]
    return h


def word_page(lines, selected=False, numbered=False):
    """lines: [(text, 'h1'|'h2'|'body'|'step')]. numbered prefixes steps 1. 2. 3."""
    est = _page_height(lines, 26.0)
    tight = est > 16.0
    show_tabs = (_page_height(lines, 26.0, .82) if tight else est) <= 16.0
    page = (f'<div class="u-doc u-doc-page"><div class="u-page{" u-tight" if tight else ""}">'
            f'{_page_lines(lines, selected, numbered)}</div></div>')
    inner = _title('Document1 - Word') + (_tabrow('word', 'Home', {}) if show_tabs else '') + page
    heads = [t for t, s in lines if s in ('h1', 'h2')]
    steps = [t for t, s in lines if s == 'step']
    label = 'Drawing: a Word page.'
    if heads:
        label += f' Headings: {_join(heads)}.'
    if steps:
        label += (f' The steps are {"a numbered list" if numbered else "plain lines"}'
                  f'{", and they are selected (highlighted)" if selected else ""}: '
                  f'{_join([s.rstrip(".") for s in steps])}')
        label += '' if label.endswith('.') else '.'
    return _root('word-page', label, _win('app', inner, 'word'))


# ---------------------------------------------------------------- 7. Word navigation pane

def word_navpane():
    marks = _marks([('Navigation Pane', 'r')])
    groups = [('Views', ['Read Mode', 'Print Layout', 'Web Layout']),
              ('Show', ['[ ] Ruler', '[ ] Gridlines', '[x] Navigation Pane']),
              ('Zoom', ['Zoom', '100%'])]
    top = _title('Document1 - Word') + _tabrow('word', 'View', marks) + _band(groups, marks)
    nav = ('<div class="u-nav"><div class="u-navh">Navigation<span class="u-x u-xs"></span></div>'
           '<div class="u-navt"><span class="u-on">Headings</span><span>Pages</span><span>Results</span></div>'
           '<div class="u-navl"><span class="u-n1 on">Computer help at the library</span>'
           '<span class="u-n2">Who it helps</span><span class="u-n2">Steps</span></div></div>')
    page = ('<div class="u-doc u-doc-nav"><div class="u-page u-pgmini"><span class="u-bar1"></span>'
            '<span class="u-bar2"></span><span class="u-barl"></span><span class="u-barl"></span>'
            '<span class="u-bar2"></span><span class="u-barl"></span></div></div>')
    label = ('Drawing: Word with the View tab open. In the Show group, the Navigation Pane box is checked '
             'and marked 1. On the left, the Navigation pane lists the headings: Computer help at the '
             'library, then Who it helps and Steps.')
    return _root('word-navpane', label, _win('app', top + f'<div class="u-split">{nav}{page}</div>', 'word'))


# ---------------------------------------------------------------- 8. File (backstage) menu

def file_menu(app='word', step=1):
    a = APPS[app]
    both = step == 'both'
    sa_n = 1 if step == 1 or both else 0
    br_n = 2 if both else (1 if step == 2 else 0)
    chosen = step in (2, 'both')
    items = []
    for it in ('Home', 'New', 'Open', '|', 'Info', 'Save', 'Save As', 'Print', 'Share', 'Export', 'Close'):
        if it == '|':
            items.append('<span class="u-bsep"></span>')
            continue
        n = sa_n if it == 'Save As' else 0
        on = ' u-on' if it == 'Save As' and chosen else ''
        items.append(f'<span class="u-bi{on}{_t(n)}">{_lab(it, n)}{_bd(n, "ir")}</span>')
    side = f'<div class="u-bs"><span class="u-back"><span></span></span>{"".join(items)}</div>'
    if chosen:
        rows = ''
        for nm, g in (('Recent', 'clock'), ('OneDrive', 'cloud'), ('This PC', 'pc'),
                      ('Add a Place', 'plus'), ('Browse', 'fold')):
            n = br_n if nm == 'Browse' else 0
            rows += (f'<span class="u-loc{_t(n)}"><span class="u-li u-li-{g}"></span>{_lab(nm, n)}'
                     f'{_bd(n, "r")}</span>')
        main = f'<div class="u-bm"><div class="u-bh">Save As</div><div class="u-locs">{rows}</div></div>'
    else:
        main = ('<div class="u-bm"><div class="u-bh u-bh-dim">Home</div><div class="u-phs">'
                '<span></span><span></span><span></span></div><div class="u-phl"><span></span><span></span>'
                '<span></span></div></div>')
    inner = f'<div class="u-bk">{side}{main}<span class="u-bt">{_e(a["doc"])} - {_e(a["name"])}</span></div>'
    pairs = []
    if sa_n:
        pairs.append(('Save As in the left column', sa_n))
    if br_n:
        pairs.append(('Browse', br_n))
    label = (f'Drawing: the {a["name"]} File menu. The left column lists Home, New, Open, Info, Save, '
             'Save As, Print, Share, Export and Close.'
             + (' Save As is selected and the right side lists Recent, OneDrive, This PC, Add a Place '
                'and Browse.' if chosen else '') + _said(pairs))
    return _root('file-menu', label, _win('app', inner, app))


# ---------------------------------------------------------------- Windows 10 file dialogs

_NAV = ('Quick access', 'Desktop', 'Downloads', 'Documents', 'Pictures', 'This PC')
_KIND = {'folder': 'File folder', 'word': 'Word Document', 'excel': 'Excel Worksheet',
         'powerpoint': 'PowerPoint Presentation', 'pdf': 'PDF Document', 'image': 'JPG File'}


def _ficon(kind, big=False):
    if big and kind in ('word', 'excel', 'powerpoint'):
        return app_badge(kind)
    if big and kind == 'pdf':
        return '<span class="u-pdfb" aria-hidden="true">PDF</span>'
    return f'<span class="u-fi u-fi-{kind if kind in _KIND else "file"}"></span>'


def _navpane(names, current, marks):
    rows = ''
    for nm in names:
        key = nm.lower().replace(' ', '')
        n, pos = _get(marks, key, 'r')
        g = {'quickaccess': 'star', 'thispc': 'pc'}.get(key, 'folder')
        on = ' u-on' if nm == current else ''
        rows += f'<span class="u-nr{on}{_t(n)}"><span class="u-ni u-ni-{g}"></span>{_lab(nm, n)}{_bd(n, pos)}</span>'
    return f'<div class="u-np">{rows}</div>'


def _addr(location):
    crumbs = ''.join(f'<span class="u-cr">\u203a</span><span>{_e(p)}</span>' for p in location)
    return ('<div class="u-da"><span class="u-arr">\u2190</span><span class="u-arr">\u2192</span>'
            f'<span class="u-arr">\u2191</span><span class="u-path"><span class="u-ni u-ni-pc"></span>{crumbs}</span>'
            '<span class="u-srch"><span class="u-mag"></span>Search</span></div>')


def _toolbar(marks):
    n, pos = _get(marks, 'newfolder', 'r')
    return (f'<div class="u-dt"><span class="u-org">Organize{_dd()}</span>'
            f'<span class="u-nf{_t(n)}">{_lab("New folder", n)}{_bd(n, pos)}</span></div>')


def save_as_dialog(location, items, filename='', savetype='Word Document (*.docx)', targets=(),
                   open_after=None, app='word'):
    """Windows 10 Save As dialog.

    location: breadcrumb list, e.g. ['This PC', 'Documents'].
    items: [(name, kind)], kind in folder|word|excel|powerpoint|pdf.
    targets: ordered keys from documents, newfolder, folder:<name>, filename, savetype,
             openafter, save.
    open_after: None hides the PDF checkbox; True/False shows it checked/unchecked.
    app: 'word' | 'excel' | 'powerpoint' sets the title-bar letter badge (W, X, P).
    """
    marks = _marks(targets)
    current = location[-1] if location and location[-1] in _NAV else None
    nav = _NAV[:-1] if 'documents' in marks or 'openafter' in marks else _NAV  # room for the ring
    rows = ''
    for nm, kind in items:
        n, pos = _get(marks, f'folder:{nm}', 'r')
        rows += (f'<div class="u-fr"><span class="u-fn{_t(n)}">{_ficon(kind)}<span class="u-fnt">{_lab(nm, n)}</span>{_bd(n, pos)}</span>'
                 f'<span class="u-ft">{_e(_KIND.get(kind, "File"))}</span></div>')
    if not items:
        rows = '<div class="u-empty">No items match your search.</div>'
    lst = f'<div class="u-fl"><div class="u-fh"><span>Name</span><span>Type</span></div>{rows}</div>'
    fn_n, _ = _get(marks, 'filename')
    st_n, _ = _get(marks, 'savetype')
    fields = (f'<div class="u-frow"><span class="u-flab">File name:</span><span class="u-in{_t(fn_n)}">'
              f'<span class="u-iv">{_lab(filename, fn_n) if filename else ""}</span>{_bd(fn_n, "in")}</span></div>'
              f'<div class="u-frow"><span class="u-flab">Save as type:</span><span class="u-in u-sel{_t(st_n)}">'
              f'<span class="u-iv">{_lab(savetype, st_n)}</span>{_bd(st_n, "in")}{_dd()}</span></div>')
    oa_n, _ = _get(marks, 'openafter')
    sv_n, _ = _get(marks, 'save')
    if open_after is None:
        left = '<span class="u-hide"><span class="u-up"></span>Hide Folders</span>'
    else:
        left = (f'<span class="u-chk u-oa{_t(oa_n)}"><span class="u-cb{" u-on" if open_after else ""}"></span>'
                f'<span>{_lab("Open file after publishing", oa_n)}</span>{_bd(oa_n, "r")}</span>')
    btns = (f'<div class="u-brow">{left}<span class="u-btns"><span class="u-pbtn u-def{_t(sv_n)}">'
            f'{_lab("Save", sv_n)}{_bd(sv_n, "l")}</span><span class="u-pbtn">Cancel</span></span></div>')
    tall = ' u-short' if oa_n else ''
    inner = (_title('Save As', app_badge(app if app in APPS else 'word')) + _addr(location) + _toolbar(marks)
             + f'<div class="u-db{tall}">{_navpane(nav, current, marks)}{lst}</div>'
             + f'<div class="u-dbot">{fields}{btns}</div>')
    names = {'documents': 'Documents in the left pane', 'newfolder': 'the New folder button',
             'filename': 'the File name box', 'savetype': 'the Save as type list',
             'openafter': 'the Open file after publishing box', 'save': 'the Save button'}
    pairs = [(names.get(k, f'the {k[7:]} folder' if k.startswith('folder:') else k), n)
             for k, (n, _) in marks.items()]
    shown = _join([nm for nm, _ in items]) if items else 'no items'
    label = (f'Drawing: the Windows Save As dialog, open at {" > ".join(location)}. It shows {shown}. '
             f'File name: {filename or "empty"}. Save as type: {savetype}.'
             + ('' if open_after is None else
                f' Open file after publishing is {"checked" if open_after else "not checked"}.')
             + _said(pairs))
    return _root('save-as', label, _win('dlg', inner))


def savetype_list():
    rows = ''
    for st in SAVE_TYPES:
        n = 1 if st == 'PDF (*.pdf)' else 0
        rows += f'<span class="u-opt{" u-pdf" if n else ""}{_t(n)}">{_lab(st, n)}{_bd(n, "ir")}</span>'
    inner = (_title('Save As', app_badge('word'))
             + '<div class="u-dbot u-dbot-open">'
             '<div class="u-frow"><span class="u-flab">File name:</span><span class="u-in">'
             '<span class="u-iv">Computer help handout</span></span></div>'
             '<div class="u-frow"><span class="u-flab">Save as type:</span><span class="u-in u-sel u-open">'
             f'<span class="u-iv">Word Document (*.docx)</span>{_dd()}</span></div>'
             f'<div class="u-frow"><span class="u-flab"></span><span class="u-list">{rows}</span></div></div>')
    label = ('Drawing: the Save as type list in the Save As dialog is open. It lists ' + _join(SAVE_TYPES)
             + '. PDF (*.pdf) is marked 1.')
    return _root('savetype-list', label, _win('dlg', inner))


# ---------------------------------------------------------------- Edge pieces

def _edge(tab, url, page, *, fav='site', url_n=0, url_pos='r', typed=False, dl=False, popup=''):
    tabs = (f'<div class="u-et">{app_badge("edge")}<span class="u-etab"><span class="u-fav u-fav-{fav}"></span>'
            f'<span class="u-ett">{_e(tab)}</span><span class="u-x u-xs"></span></span>'
            f'<span class="u-eplus">+</span>{_wc()}</div>')
    if typed:
        shown = f'<span class="u-big">{_e(url)}</span><span class="u-caret u-caretd"></span>'
    else:
        shown = f'<span class="u-ut">{_e(url)}</span>'
    lock = '<span class="u-lock"></span>' if fav != 'pdf' else '<span class="u-filet">File</span>'
    addr = ('<div class="u-ea"><span class="u-arr">\u2190</span><span class="u-arr">\u2192</span>'
            f'<span class="u-rf"></span><span class="u-url{_t(url_n)}">{lock}{shown}{_bd(url_n, url_pos)}</span>'
            + ('<span class="u-dlb"><span>\u2193</span></span>' if dl else '<span class="u-dots">\u00b7\u00b7\u00b7</span>')
            + '</div>')
    return _win('edge', tabs + addr + f'<div class="u-epage">{page}{popup}</div>', 'edge')


def _art():
    """Abstract practice-photo illustration: two simple figures at a table with a paper."""
    return ('<span class="u-art"><span class="u-wall"></span><span class="u-fig u-f1"></span>'
            '<span class="u-fig u-f2"></span><span class="u-tbl"></span><span class="u-paper"></span></span>')


# ---------------------------------------------------------------- 11. PDF in Edge

def pdf_view():
    lines = [('Computer help at the library', 'h1'), ('Who it helps', 'h2'),
             ('Anyone who wants to practice one computer task.', 'body'), ('Steps', 'h2'),
             ('Choose one task.', 'step'), ('Visit the learning desk.', 'step'),
             ('Ask how to repeat it at home.', 'step')]
    bar = ('<div class="u-pdfbar"><span>1 / 1</span><span class="u-pdfz">\u2212</span><span class="u-pdfz">+</span>'
           '<span class="u-pdfsep"></span><span>Draw</span><span>Highlight</span></div>')
    page = (bar + '<div class="u-doc u-doc-pdf"><div class="u-page u-page-pdf">'
            + _page_lines(lines, False, True, cursor=False) + '</div></div>')
    label = ('Drawing: Microsoft Edge showing the PDF file Computer help handout.pdf. The page shows the '
             'heading Computer help at the library, then Who it helps: Anyone who wants to practice one '
             'computer task. Then Steps: 1. Choose one task. 2. Visit the learning desk. 3. Ask how to '
             'repeat it at home.')
    return _root('pdf-view', label, _edge('Computer help handout.pdf',
                                          'C:/Users/You/Documents/Resource pack/Computer help handout.pdf',
                                          page, fav='pdf'))


# ---------------------------------------------------------------- 12. Excel grid

_NUM = re.compile(r'^[-+]?\$?\d[\d,]*(\.\d+)?%?$')


def excel_grid(cells, active=None, formula=None, targets=()):
    """cells: {'A1': 'Item', 'B2': '12', ...}; active: 'B5'; formula: text for the formula bar.
    targets: ordered keys from 'formula_bar' and cell addresses."""
    marks = _marks(targets)
    cols = 'ABCD'
    acol, arow = (active[0], active[1:]) if active else ('', '')
    grid = ['<span class="u-xc u-xh u-xcorner"></span>']
    grid += [f'<span class="u-xc u-xh{" u-on" if c == acol else ""}">{c}</span>' for c in cols]
    for r in range(1, 7):
        grid.append(f'<span class="u-xc u-xh u-xr{" u-on" if str(r) == arow else ""}">{r}</span>')
        for ci, c in enumerate(cols):
            addr = f'{c}{r}'
            v = str(cells.get(addr, ''))
            isnum = bool(_NUM.match(v))
            nxt = str(cells.get(f'{cols[ci + 1]}{r}', '')) if ci < 3 else 'edge'
            n, pos = _get(marks, addr, 'tr' if ci < 2 else 'tl')
            spill = bool(v) and not isnum and not nxt and _tw(v, 1.6 if n else 1.3, bool(n)) > 8.4
            cls = ('u-xc' + (' u-isnum' if isnum else '') + (' u-spill' if spill else '')
                   + (' u-act' if addr == active else '') + _t(n))
            grid.append(f'<span class="{cls}"><span class="u-xv">{_lab(v, n) if v else ""}</span>{_bd(n, pos)}</span>')
    shown = formula if formula is not None else (cells.get(active, '') if active else '')
    fn, fpos = _get(marks, 'formula_bar', 'ir')
    fx = (f'<div class="u-fx"><span class="u-nbox">{_e(active or "")}{_dd()}</span><span class="u-fxs">'
          f'<span class="u-fxl">fx</span></span><span class="u-fxi{_t(fn)}">{_lab(shown, fn)}{_bd(fn, fpos)}</span></div>')
    sheets = ('<div class="u-sheets"><span class="u-sheet">Sheet1</span>'
              '<span class="u-plus">+</span></div>')
    inner = _title('Book1 - Excel') + fx + f'<div class="u-grid">{"".join(grid)}</div>' + sheets
    filled = [f'{k} {v}' for k, v in sorted(cells.items(), key=lambda kv: (int(kv[0][1:]), kv[0][0]))]
    pairs = [('the formula bar' if k == 'formula_bar' else f'cell {k}', n) for k, (n, _) in marks.items()]
    label = ('Drawing: an Excel sheet with columns A to D and rows 1 to 6. '
             + (f'Cells: {"; ".join(filled)}. ' if filled else 'The cells are empty. ')
             + (f'The active cell is {active}, with a thick green border. ' if active else '')
             + (f'The formula bar shows {shown}.' if shown else '') + _said(pairs))
    return _root('excel-grid', label.strip(), _win('app', inner, 'excel'))


# ---------------------------------------------------------------- PowerPoint pieces

def _photo(state, marks):
    pn, pp = _get(marks, 'photo', 'tl' if state == 'cropped' else 'tr')
    chip = '<span class="u-chip">practice photo</span>'
    if state != 'cropping':
        return (f'<span class="u-photo u-ph-{state}{_t(pn)}"><span class="u-pclip">{_art()}</span>{chip}'
                f'{_bd(pn, pp)}</span>')
    hn, hp = _get(marks, 'handle', 't')
    hs = ''.join(f'<span class="u-hd u-hd-{k}"></span>' for k in ('tl', 'tr', 'bl', 'br', 't', 'b', 'l'))
    hs += f'<span class="u-hd u-hd-r{_t(hn)}">{_bd(hn, hp)}</span>'
    arrows = '<span class="u-drag u-drag-l">\u2192</span><span class="u-drag u-drag-r">\u2190</span>'
    return (f'<span class="u-photo u-ph-cropping{_t(pn)}"><span class="u-pclip">{_art()}'
            f'<span class="u-cf"></span></span>{hs}{arrows}{chip}{_bd(pn, pp)}</span>')


def _slide(title, subtitle, theme, photo, marks):
    """Slide with title + subtitle laid out in a flow column (they can never overlap);
    with photo='cropped' the column sits top-left and the photo on the right."""
    th = ' u-theme' if theme else ''
    parts = ''
    if photo not in ('inserted', 'cropping'):
        boxes = ''
        for key, text, ph, pos in (('title', title, 'Click to add title', 'tl'),
                                   ('subtitle', subtitle, 'Click to add subtitle', 'bl')):
            n, p = _get(marks, key, pos)
            kind = 'u-ph' if text is None else 'u-typedt'
            boxes += (f'<span class="u-box u-box-{key} {kind}{_t(n)}"><span>{_lab(ph if text is None else text, n)}'
                      f'</span>{_bd(n, p)}</span>')
        parts += f'<span class="u-txt{" u-side" if photo == "cropped" else ""}">{boxes}</span>'
    if photo:
        parts += _photo(photo, marks)
    return f'<div class="u-slide{th}">{parts}</div>'


def _thumbs(theme, photo):
    mini = f'<span class="u-mini{" u-theme" if theme else ""}">' + ('<span class="u-minip"></span>' if photo else '') + '</span>'
    return f'<div class="u-thp"><span class="u-thn">1</span>{mini}</div>'


# ---------------------------------------------------------------- 13. PowerPoint window

def ppt_window(title=None, subtitle=None, theme=None, photo=None, targets=()):
    """PowerPoint normal view. photo: None | 'inserted' | 'cropping' | 'cropped'.
    targets: ordered keys from title, subtitle, photo, handle."""
    marks = _marks(targets)
    inner = (_title('Presentation1 - PowerPoint') + _tabrow('powerpoint', 'Home', {})
             + f'<div class="u-pv">{_thumbs(theme, photo)}<div class="u-stage">'
             + _slide(title, subtitle, theme, photo, marks) + '</div></div>')
    desc = 'Drawing: PowerPoint with one slide.'
    if photo not in ('inserted', 'cropping'):
        desc += (f' Title: {title}.' if title is not None else ' The title box says Click to add title.')
        desc += (f' Subtitle: {subtitle}.' if subtitle is not None else ' The subtitle box says Click to add subtitle.')
    if theme:
        desc += ' A dark teal theme with white text is applied.'
    desc += {None: '', 'inserted': ' A practice photo covers most of the slide.',
             'cropping': ' The practice photo is being cropped: black crop handles sit on its edges and '
                         'corners, the parts being cut away are greyed, and arrows show dragging inward.',
             'cropped': ' A smaller, cropped practice photo sits on the right side of the slide.'}.get(photo, '')
    names = {'title': 'the title box', 'subtitle': 'the subtitle box', 'photo': 'the photo',
             'handle': 'the black crop handle on the right edge'}
    desc += _said([(names.get(k, k), n) for k, (n, _) in marks.items()])
    return _root('ppt-window', desc, _win('app', inner, 'powerpoint'))


# ---------------------------------------------------------------- 14. PowerPoint themes

_THEMES = ('Office Theme', 'Navy', 'Teal', 'Cream', 'Charcoal', 'Lavender')


def ppt_themes():
    tiles = ''
    for i, nm in enumerate(_THEMES, 1):
        n = 1 if i == 3 else 0
        tiles += (f'<span class="u-thm u-thm{i}{_t(n)}"><span class="u-aa{" u-big" if n else ""}">Aa</span>'
                  f'<span class="u-pal"><span></span><span></span><span></span><span></span></span>{_bd(n, "tr")}</span>')
    tiles += '<span class="u-more"><span></span><span></span><span></span></span>'
    band = f'<div class="u-rb u-rb-themes">{_group("Themes", [], {}, raw=tiles)}</div>'
    inner = (_cap('powerpoint', 'Design tab \u203a Themes') + _tabrow('powerpoint', 'Design', {}) + band
             + _doc_stub('powerpoint'))
    label = ('Drawing: PowerPoint with the Design tab open. The Themes gallery shows six theme tiles, each '
             'with the letters Aa in different colours. The third tile, dark teal with white letters, is marked 1.')
    return _root('ppt-themes', label, _win('app', inner, 'powerpoint'))


# ---------------------------------------------------------------- 15. Insert > Pictures

def ppt_insert_pictures():
    marks = _marks(['Insert', 'Pictures'])
    menu = ('<span class="u-menu"><span class="u-mi u-t"><span class="u-mg u-mg-pc"></span>'
            f'<span class="u-big">This Device...</span>{_bd(3, "r")}</span>'
            '<span class="u-mi"><span class="u-mg u-mg-stock"></span>Stock Images...</span>'
            '<span class="u-mi"><span class="u-mg u-mg-web"></span>Online Pictures...</span></span>')
    groups = [('Slides', ['New Slide']), ('Tables', ['Table']), ('Images', ['Pictures', 'Screenshot']),
              ('Illustrations', ['Shapes', 'Icons'])]
    inner = (_title('Presentation1 - PowerPoint') + _tabrow('powerpoint', 'Insert', marks)
             + _band(groups, marks, pressed=('Pictures',), menus={'Pictures': menu})
             + '<div class="u-doc u-doc-powerpoint u-doc-tall"><span class="u-stub"></span></div>')
    label = ('Drawing: PowerPoint. The Insert tab is marked 1. The Pictures button is pressed and marked 2. '
             'Its menu is open, listing This Device..., Stock Images... and Online Pictures...; '
             'This Device... is marked 3.')
    return _root('ppt-insert-pictures', label, _win('app', inner, 'powerpoint'))


# ---------------------------------------------------------------- 16. Insert Picture dialog

def insert_picture_dialog():
    marks = _marks([('downloads', 'r')])
    nav = _navpane(('Quick access', 'Desktop', 'Downloads', 'Documents', 'Pictures'), 'Downloads', marks)
    big = (f'<div class="u-fl u-fl-big"><span class="u-bigfile u-t"><span class="u-bthumb"><span class="u-pclip">'
           f'{_art()}</span></span><span class="u-big">practice-photo</span>{_bd(2, "r")}</span></div>')
    bottom = ('<div class="u-dbot"><div class="u-frow"><span class="u-flab">File name:</span>'
              '<span class="u-in"><span class="u-iv">practice-photo</span></span>'
              f'<span class="u-in u-sel u-filt"><span class="u-iv">All Pictures</span>{_dd()}</span></div>'
              '<div class="u-brow"><span></span><span class="u-btns"><span class="u-pbtn u-def u-t">'
              f'<span class="u-big">Insert</span>{_dd()}{_bd(3, "l")}</span><span class="u-pbtn">Cancel</span></span></div></div>')
    inner = (_title('Insert Picture', app_badge('powerpoint')) + _addr(['This PC', 'Downloads']) + _toolbar({})
             + f'<div class="u-db u-db-ins">{nav}{big}</div>' + bottom)
    label = ('Drawing: the Windows Insert Picture dialog. Downloads in the left pane is marked 1. The '
             'practice-photo file is marked 2. The Insert button is marked 3; Cancel is beside it.')
    return _root('insert-picture', label, _win('dlg', inner))


# ---------------------------------------------------------------- 17. Picture Format > Crop

def ppt_crop():
    marks = _marks(['Crop', ('handle', 't')])
    groups = [('Adjust', ['Corrections', 'Color']), ('Size', ['Crop', '~Height 3.2"', '~Width 5.7"'])]
    stage = ('<div class="u-pv u-pv-crop"><div class="u-stage">'
             + _slide(None, None, None, 'cropping', marks) + '</div></div>')
    inner = (_title('Presentation1 - PowerPoint')
             + _tabrow('powerpoint', 'Picture Format', marks, extra=('Picture Format',))
             + _band(groups, marks) + stage)
    label = ('Drawing: PowerPoint with the Picture Format tab open. In the Size group, the Crop button is '
             'marked 1. Below, the slide photo shows black crop handles; the black handle on the right edge, '
             'with an arrow pointing inward, is marked 2. The greyed parts will be cut away.')
    return _root('ppt-crop', label, _win('app', inner, 'powerpoint'))


# ---------------------------------------------------------------- 18. Designer pane

def designer_pane():
    ideas = ''.join(f'<span class="u-idea u-idea{i}"><span class="u-ip"></span><span class="u-ib"></span>'
                    '<span class="u-ib u-ib2"></span></span>' for i in (1, 2, 3))
    pane = ('<div class="u-dz"><div class="u-dzh"><span class="u-dzt">Designer</span>'
            f'<span class="u-dzx u-t"><span class="u-big">\u00d7</span>{_bd(1, "l")}</span></div>'
            f'<div class="u-ideas">{ideas}</div></div>')
    stage = ('<div class="u-pv u-pv-dz"><div class="u-stage">'
             + _slide(None, None, None, 'inserted', {}) + f'</div>{pane}</div>')
    inner = _title('Presentation1 - PowerPoint') + stage
    label = ('Drawing: PowerPoint with the Designer pane open on the right, showing design idea thumbnails. '
             'The close X in the top-right corner of the Designer pane is marked 1.')
    return _root('designer-pane', label, _win('app', inner, 'powerpoint'))


# ---------------------------------------------------------------- 19. Edge download

def edge_page_download():
    page = ('<div class="u-vub"><span class="u-vubm">VUB Learning</span></div><div class="u-wk">'
            '<div class="u-wkh">Week 3 \u00b7 Worksheet</div><div class="u-part">Part 4</div>'
            '<span class="u-gold u-t"><span class="u-big">Download the practice photo</span>'
            f'{_bd(1, "r")}</span></div>')
    popup = ('<div class="u-dlp u-t"><div class="u-dlh">Downloads</div><div class="u-dlr">'
             '<span class="u-dlthumb"><span class="u-pclip">' + _art() + '</span></span>'
             '<span class="u-dlx"><span class="u-dln">practice-photo.jpg</span><span class="u-link">Open file</span>'
             f'</span></div>{_bd(2, "l")}</div>')
    label = ('Drawing: Microsoft Edge on vublessons.com, Week 3 Worksheet page. In Part 4, the gold '
             'Download the practice photo button is marked 1. The Downloads pop-up at the top right lists '
             'practice-photo.jpg with an Open file link, and is marked 2.')
    return _root('edge-download', label, _edge('Week 3 \u00b7 Worksheet',
                                               'vublessons.com/courses/digital-literacy-2/weeks/week-03/worksheet',
                                               page, dl=True, popup=popup))


# ---------------------------------------------------------------- 20. File Explorer

def explorer_resource_pack():
    files = (('Computer help handout', 'word'), ('Computer help handout', 'pdf'),
             ('Supply list', 'excel'), ('Flyer', 'powerpoint'))
    rows = ''.join(f'<div class="u-fr"><span class="u-fn">{_ficon(k, True)}{_e(n)}</span>'
                   f'<span class="u-ft">{_e(_KIND[k])}</span></div>' for n, k in files)
    inner = (_title('Resource pack', app_badge('explorer'))
             + '<div class="u-xtabs"><span class="u-on">File</span><span>Home</span><span>Share</span><span>View</span></div>'
             + _addr(['This PC', 'Documents', 'Resource pack'])
             + f'<div class="u-fl u-fl-x"><div class="u-fh"><span>Name</span><span>Type</span></div>{rows}</div>'
             + '<div class="u-status">4 items</div>')
    label = ('Drawing: File Explorer open at This PC > Documents > Resource pack. It lists four files: '
             'Computer help handout (Word Document), Computer help handout (PDF Document), Supply list '
             '(Excel Worksheet) and Flyer (PowerPoint Presentation).')
    return _root('explorer', label, _win('dlg', inner, 'explorer'))


# ---------------------------------------------------------------- 21. vublessons.com path

def vub_course_path(week=3, week_title='Create something people can use'):
    page = ('<div class="u-vub"><span class="u-vubm">VUB Learning</span></div><div class="u-wk">'
            '<div class="u-card"><span class="u-cardt">Digital Literacy \u2014 Level 2</span>'
            '<span class="u-cards">6 weeks</span>'
            f'<span class="u-navy u-t"><span class="u-big">Open course \u2192</span>{_bd(2, "r")}</span></div>'
            f'<div class="u-week"><span class="u-weekt">Week {week} \u00b7 {_e(week_title)}</span>'
            f'<span class="u-wl"><span class="u-link">Open week {week}</span>'
            f'<span class="u-link u-t"><span class="u-big">Worksheet</span>{_bd(3, "r")}</span></span></div></div>')
    label = ('Drawing: Microsoft Edge. The address bar with vublessons.com typed in is marked 1. The course '
             'card Digital Literacy, Level 2, has an Open course button, marked 2. '
             f'The row Week {week}, {week_title}, has two links, Open week {week} and Worksheet; Worksheet is marked 3.')
    return _root('vub-path', label, _edge('VUB Learning', 'vublessons.com', page, url_n=1, url_pos='ir', typed=True))
