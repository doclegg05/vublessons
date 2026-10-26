"""Week 6 drawings for the guided deck (original HTML/CSS, not screenshots). guided.drawing() looks names up here
after ui and ui_mail. Shared helpers such as app_badge stay in ui.py.

Same rules as ui.py: div/span only, every thing to click is ringed (.u-t) AND numbered (.u-bd), no text below
1.15cqw. Styles are in courses/digital-literacy-2/os/ui-week6.css, loaded only by Week 6.

The Resource finder drawings work out their results with the same rules the three real pages use
(courses/digital-literacy-2/activities/resource-finder*.html), so a drawing can never show a result the page
would not give. tests/content/dl2-week6-guided.spec.js checks the code lines in agent_change against the pages.
"""
import re

from ui import _bd, _e, _edge, _get, _join, _lab, _marks, _root, _said, _t

__all__ = ['finder_page', 'finder_table', 'request_box', 'agent_change', 'edge_worksheet_top', 'edge_course_home', 'edge_post_test',
           'finder_results', 'CODE', 'NONE']

NONE = 'No matching resources. Try a different word or reset the filters.'
_RESOURCES = (
    ('Community library', 'Learning', 'Fictional one-to-one help with browser and file tasks.'),
    ('Community Makers Group', 'Community', 'Fictional peer group for trying small projects together.'),
    ('Practice Workbook Workshop', 'Learning', 'Fictional guided practice with tables, formulas and charts.'),
)
_URL = {1: 'resource-finder', 2: 'resource-finder-agent', 3: 'resource-finder-agent-fixed'}
_TAB = {1: 'Version 1 · Fictional resource finder', 2: 'Version 2 · Fictional resource finder (agent result)',
        3: 'Version 3 · Fictional resource finder (after the repair)'}

# The exact lines the pages differ in (see the three activity pages). Each pair is (before, after).
CODE = {
    'asked': ("(r.name+' '+r.description).toLowerCase().includes(query)", "(r.name+' '+r.category+' '+r.description).toLowerCase().includes(query)"),
    'unasked': ('const query=search.value.trim().toLowerCase();', 'const query=search.value.trim();'),
    'repair': ('const query=search.value.trim();', 'const query=search.value.trim().toLowerCase();'),
}


def finder_results(version, query):
    """The entries a version of the page shows for a typed search, with All categories chosen."""
    typed = query.strip()
    if version == 1:
        return [n for n, c, d in _RESOURCES if typed.lower() in f'{n} {d}'.lower()]
    if version == 2:
        return [n for n, c, d in _RESOURCES if typed in f'{n} {c} {d}'.lower()]
    return [n for n, c, d in _RESOURCES if typed.lower() in f'{n} {c} {d}'.lower()]


def _status(names):
    return f'{len(names)} fictional resource{"" if len(names) == 1 else "s"} found.' if names else NONE


def _found_word(version, query):
    names = finder_results(version, query)
    return f'{len(names)} found' if names else 'none found'


# ---------------------------------------------------------------- the Resource finder page


def finder_page(version=1, query='', targets=(), focus='', zoom=False):
    """The practice Resource finder in Edge. targets: search, category, reset, status, results (ringed and numbered).
    focus: link, search, category or reset gets the page's own 4-pixel focus ring. zoom: the page zoomed in."""
    marks = _marks(targets)

    def box(key, cls, inner, pos='r'):
        n, p = _get(marks, key, pos)
        ring = ' f-focus' if focus == key else ''
        return f'<span class="{cls}{_t(n)}{ring}">{inner}{_bd(n, p)}</span>'
    names = finder_results(version, query)
    typed = f'<span class="f-typed">{_e(query)}</span><span class="u-caret"></span>' if query else '<span class="f-ph">Try library{}</span>'.format(' or learning' if version > 1 else '')
    results = ''.join(
        f'<div class="f-res"><b>{_e(n)}</b><span>{_e(c)}</span></div>' for n, c, d in _RESOURCES if n in names)
    n_res, p_res = _get(marks, 'results', 'r')
    note = {1: '', 2: '<div class="f-ver">Version 2. Changed by an AI coding agent. Review and test it before you trust it.</div>',
            3: '<div class="f-ver">Version 3. The agent repaired the capital-letter search. Retest it before you trust it.</div>'}[version]
    link_cls = ' f-focus' if focus == 'link' else ''
    page = (f'<div class="f-pg{" f-zoom" if zoom else ""}">'
            f'<div class="f-link{link_cls}">Back to the Week 6 lesson</div>'
            '<div class="f-h">Community resource finder</div>'
            '<div class="f-lab">Search fictional resources</div>'
            + box('search', 'f-in', typed, 'ir')
            + '<div class="f-row"><div><div class="f-lab">Category</div>'
            + box('category', 'f-sel', 'All categories ▾', 'r')
            + '</div>' + box('reset', 'f-btn', 'Reset filters', 'r') + '</div>'
            + box('status', 'f-st', _e(_status(names)), 'r')
            + f'<div class="f-results{_t(n_res)}">{results}{_bd(n_res, p_res)}</div>'
            + note
            + ('<span class="f-zchip">Zoom 300%</span>' if zoom else '') + '</div>')
    spoken = {'search': 'the search box', 'category': 'the Category list', 'reset': 'the Reset filters button', 'status': 'the line that says how many were found',
              'results': 'the matching entries'}
    shown = f'The search box holds {query}.' if query else 'The search box is empty.'
    label = (f'Drawing: Microsoft Edge showing the practice Resource finder, version {version}. {shown} {_status(names)} '
             + (f'The entries shown are {_join(names)}.' if names else 'No entries are shown.')
             + (f' The page has a thick focus ring on {focus if focus != "link" else "the Return link"}.' if focus else '')
             + (' The page is zoomed in to 300 percent.' if zoom else '')
             + _said([(spoken[k], n) for k, (n, _) in marks.items() if k in spoken]))
    return _root('finder', label, _edge(_TAB[version], f'vublessons.com/courses/digital-literacy-2/activities/{_URL[version]}', page))


# ---------------------------------------------------------------- the test table on the worksheet

_TABLE_COLS = {1: ['Search', 'What I saw in version 1'], 3: ['Search', 'What I saw in version 2'], 4: ['Search', 'What I saw in version 3']}
_TABLE_VERSION = {1: 1, 3: 2, 4: 3}
_SEARCHES = ('library', 'learning', 'zzz', 'LIBRARY')


def finder_table(part=1, filled=0, targets=()):
    """The worksheet test table in Edge. part (1, 3 or 4) picks the version; filled is how many of the four rows have an entry."""
    marks = _marks(targets)
    cols = _TABLE_COLS[part]
    version = _TABLE_VERSION[part]
    head = ''.join(f'<span class="f-th">{_e(c)}</span>' for c in cols)
    rows = ''
    for i, q in enumerate(_SEARCHES):
        text = _found_word(version, q) if i < filled else ''
        cell = f'<span class="f-td{" f-fill" if text else ""}">{_e(text)}</span>'
        n, pos = _get(marks, q, 'ir')
        rows += f'<div class="f-tr{_t(n)}"><span class="f-td f-q">{_e(q)}</span>{cell}{_bd(n, pos)}</div>'
    page = ('<div class="u-vub"><span class="u-vubm">VUB Learning</span></div><div class="u-wk">'
            f'<div class="u-wkh">Week 6 · Worksheet</div><div class="u-part">Part {part} · My test table</div>'
            f'<div class="f-tbl"><div class="f-tr f-hd">{head}</div>{rows}</div></div>')
    done = 'empty' if not filled else f'filled in for {filled} of the 4 searches'
    label = (f'Drawing: Microsoft Edge on the Week 6 Worksheet page. In Part {part} there is a test table with the columns {_join(cols)}. '
             f'The rows are library, learning, zzz and LIBRARY. The table is {done}.'
             + _said([(f'the {k} row', n) for k, (n, _) in marks.items()]))
    return _root('finder-table', label, _edge('Week 6 · Worksheet', 'vublessons.com/courses/digital-literacy-2/weeks/week-06/worksheet', page))


def request_box(lines=(), targets=()):
    """The Part 2 worksheet with its My request box. lines: what is typed so far. targets: box."""
    marks = _marks(targets)
    n, pos = _get(marks, 'box', 'r')
    typed = ''.join(f'<span class="f-rl">{_e(x)}</span>' for x in lines) or '<span class="f-ph">&nbsp;</span>'
    page = ('<div class="u-vub"><span class="u-vubm">VUB Learning</span></div><div class="u-wk">'
            '<div class="u-wkh">Week 6 · Worksheet</div><div class="u-part">Part 2 · My request</div>'
            f'<div class="f-rbox{_t(n)}">{typed}{_bd(n, pos)}</div></div>')
    label = ('Drawing: Microsoft Edge on the Week 6 Worksheet page. In Part 2 there is a large box named My request. '
             + (f'It holds {len(lines)} typed lines. ' if lines else 'It is empty. ') + _said([('the My request box', n)] if n else []))
    return _root('request-box', label, _edge('Week 6 · Worksheet', 'vublessons.com/courses/digital-literacy-2/weeks/week-06/worksheet', page))


# ---------------------------------------------------------------- what the agent changed


def _code_line(text, sign, mark=''):
    """One code line with a +/- sign. mark is the part of the line that changed; it is boxed."""
    body = _e(text)
    if mark and mark in text:
        body = body.replace(_e(mark), f'\0{_e(mark)}\1', 1)
    body = re.sub(r'(?<=[+.(])', '<wbr>', body).replace('\0', '<span class="f-chg">').replace('\1', '</span>')
    return f'<span class="f-code"><span class="f-sign" aria-hidden="true">{sign}</span><span class="f-ln">{body}</span></span>'


_MARK = {'asked': ('', "r.category+' '+"), 'unasked': ('.toLowerCase()', ''), 'repair': ('', '.toLowerCase()')}
_HEAD = {
    'asked': ('ASKED FOR', 'f-yes', '✓', 'Version 1 to version 2: category is now searched too.', 'before', 'after'),
    'unasked': ('NOT ASKED FOR', 'f-no', '✗', 'Version 1 to version 2: the step that turns capital letters into small letters is gone.', 'before', 'after'),
    'repair': ('THE REPAIR', 'f-fix', '↺', 'Version 2 to version 3: the step is put back.', 'before', 'after'),
}


def agent_change(which='asked'):
    """Before and after of one line the agent changed. which: asked, unasked or repair. Text labels and a sign, never colour alone."""
    word, cls, mark, caption, _, _ = _HEAD[which]
    before, after = CODE[which]
    mb, ma = _MARK[which]
    ver_a, ver_b = ('version 2', 'version 3') if which == 'repair' else ('version 1', 'version 2')
    inner = (f'<div class="f-ch {cls}"><div class="f-chh"><span class="f-tag"><span aria-hidden="true">{mark}</span> {word}</span>'
             f'<span class="f-cap">{_e(caption)}</span></div>'
             f'<div class="f-bl">Before · {ver_a}</div>{_code_line(before, "−", mb)}'
             f'<div class="f-bl">After · {ver_b}</div>{_code_line(after, "+", ma)}</div>')
    label = (f'Drawing: one line of the page, before and after. {word.capitalize()}. {caption} '
             f'Before, in {ver_a}: {before} After, in {ver_b}: {after}')
    return _root('agent-change', label, inner)


# ---------------------------------------------------------------- course home and the post-test


def edge_worksheet_top(targets=('home',)):
    """The top of the worksheet page, with its row of links. targets: home."""
    marks = _marks(targets)
    n, pos = _get(marks, 'home', 'b')
    links = ''.join(f'<span class="f-nl">{_e(t)}</span>' for t in ('Print / Save as PDF', 'Lesson', 'Worksheet'))
    home = f'<span class="f-nl{_t(n)}"><span class="{"u-big" if n else ""}">Course home</span>{_bd(n, pos)}</span>'
    page = f'<div class="u-vub"><span class="u-vubm">VUB Learning</span></div><div class="f-nav">{links}{home}</div><div class="u-wk"><div class="u-wkh">Week 6 · Worksheet</div></div>'
    label = ('Drawing: Microsoft Edge on the Week 6 Worksheet page. A row of links runs along the top: Print or Save as PDF, Lesson, Worksheet and Course home.'
             + _said([('the Course home link', n)] if n else []))
    return _root('worksheet-top', label, _edge('Week 6 · Worksheet', 'vublessons.com/courses/digital-literacy-2/weeks/week-06/worksheet', page))


def edge_course_home(targets=('post',)):
    """The course home page with its Take the post-test button. targets: post."""
    marks = _marks(targets)
    n, pos = _get(marks, 'post', 'r')
    page = ('<div class="u-vub"><span class="u-vubm">VUB Learning</span></div><div class="u-wk"><div class="u-wkh">Digital Literacy · Level 2</div>'
            '<div class="f-hbtns"><span class="f-hb f-hb1">Open the lesson</span>'
            f'<span class="f-hb{_t(n)}"><span class="{"u-big" if n else ""}">Take the post-test</span>{_bd(n, pos)}</span></div></div>')
    label = ('Drawing: Microsoft Edge on the Digital Literacy Level 2 course home page. Two buttons: Open the lesson and Take the post-test.'
             + _said([('the Take the post-test button', n)] if n else []))
    return _root('course-home', label, _edge('Digital Literacy Level 2', 'vublessons.com/courses/digital-literacy-2/index', page))


def edge_post_test(name='', targets=()):
    """The post-test start screen. name: what is typed in the name box. targets: name, start."""
    marks = _marks(targets)
    nn, np_ = _get(marks, 'name', 'r')
    sn, sp = _get(marks, 'start', 'r')
    typed = f'<span class="u-big">{_e(name)}</span><span class="u-caret"></span>' if name else '<span class="f-ph">&nbsp;</span>'
    page = ('<div class="f-pt"><div class="f-pth">Digital Literacy Level 2 · Post-test</div><div class="f-h">Post-test</div>'
            '<div class="f-pl">20 questions · about 20 minutes.</div><div class="f-lab">Your full name</div>'
            f'<span class="f-in{_t(nn)}">{typed}{_bd(nn, np_)}</span>'
            f'<span class="f-go{_t(sn)}"><span class="{"u-big" if sn else ""}">Start the post-test</span>{_bd(sn, sp)}</span></div>')
    label = ('Drawing: the post-test start screen in Microsoft Edge. It says 20 questions, about 20 minutes. It has a Your full name box and a Start the post-test button.'
             + (f' The name box holds {name}.' if name else '') + _said([(w, n) for w, n in (('the name box', nn), ('the Start the post-test button', sn)) if n]))
    return _root('post-test', label, _edge('Post-test', 'vublessons.com/courses/digital-literacy-2/assessments/post-test', page))
