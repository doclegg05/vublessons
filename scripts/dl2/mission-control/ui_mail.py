"""Week 4 drawings: Gmail in Edge, Word comments, the worksheet link and the practice offer page.

Same rules as ui.py: original HTML/CSS diagrams (not screenshots), div/span only, every thing to
click is ringed (.u-t) AND numbered (.u-bd), and no text below 1.15cqw. Styles are in
courses/digital-literacy-2/os/ui-week4.css, loaded only by Week 4. The shared helpers come from ui.py.
"""
from ui import _bd, _e, _edge, _get, _join, _lab, _marks, _root, _said, _t, _tabrow, _title, _win, ribbon

__all__ = ['gmail_inbox', 'gmail_compose', 'gmail_drafts', 'word_review', 'edge_worksheet_link', 'edge_offer']

_GMAIL_URL = 'mail.google.com'
_ADDR_CAP = 4  # chips shown before "+ more"


def _icon(kind):
    return f'<span class="m-ic m-ic-{kind}"></span>'


def _side(marks, active='Inbox', drafts=0):
    """Gmail left column: Compose button and the folder list."""
    cn, cp = _get(marks, 'compose', 'r')
    dn, dp = _get(marks, 'drafts', 'r')
    rows = ''
    for name in ('Inbox', 'Starred', 'Sent', 'Drafts'):
        n = dn if name == 'Drafts' else 0
        count = f'<span class="m-cnt">{drafts}</span>' if name == 'Drafts' and drafts else ''
        on = ' m-on' if name == active else ''
        rows += f'<span class="m-fold{on}{_t(n)}">{_lab(name, n)}{count}{_bd(n, dp)}</span>'
    return (f'<div class="m-side"><span class="m-compose{_t(cn)}">{_icon("pen")}<span class="{"u-big" if cn else ""}">Compose</span>'
            f'{_bd(cn, cp)}</span>{rows}</div>')


def _gmail(inner, tab='Inbox - Gmail', **kw):
    return _edge(tab, _GMAIL_URL, f'<div class="m-gm">{inner}</div>', **kw)


def _bar():
    return '<div class="m-top"><span class="m-logo">Gmail</span><span class="m-search"><span class="u-mag"></span>Search mail</span></div>'


def gmail_inbox(targets=('compose',)):
    marks = _marks(targets)
    rows = ''.join(f'<div class="m-row"><span class="m-from">{f}</span><span class="m-subj">{s}</span></div>'
                   for f, s in (('Library newsletter', 'October events at the library'), ('Volunteer desk', 'Thank you for helping last week'),
                                ('Computer class', 'Your Week 4 worksheet')))
    label = ('Drawing: Gmail in Microsoft Edge. The address bar shows mail.google.com. At the left, a Compose button sits above the '
             'folders Inbox, Starred, Sent and Drafts. The Inbox lists three messages.'
             + _said([('the Compose button' if k == 'compose' else 'the Drafts folder', n) for k, (n, _) in marks.items()]))
    return _root('gmail-inbox', label, _gmail(_bar() + f'<div class="m-cols">{_side(marks)}<div class="m-list">{rows}</div></div>'))


def _chips(addrs):
    shown = ''.join(f'<span class="m-chip">{_e(a)}</span>' for a in addrs[:_ADDR_CAP])
    return shown + (f'<span class="m-chip m-more">+{len(addrs) - _ADDR_CAP}</span>' if len(addrs) > _ADDR_CAP else '')


def gmail_compose(to=(), bcc=(), show_bcc=False, subject='', body=(), targets=(), cursor=''):
    """The New Message window. cursor: which field shows the blinking line (to, bcc, subject, body)."""
    marks = _marks(targets)
    tn, tp = _get(marks, 'to', 'ir')
    ln, lp = _get(marks, 'bcc_link', 'b')
    bn, bp = _get(marks, 'bcc', 'ir')
    sn, sp = _get(marks, 'subject', 'ir')
    yn, yp = _get(marks, 'body', 'ir')
    xn, xp = _get(marks, 'close', 'l')
    rn, rp = _get(marks, 'trash', 'l')
    vn, vp = _get(marks, 'send', 'tr')
    caret = '<span class="u-caret m-caret"></span>'
    head = (f'<div class="m-head"><span>New Message</span><span class="m-wc"><span class="m-min"></span><span class="m-max"></span>'
            f'<span class="m-x{_t(xn)}"><span class="u-x"></span>{_bd(xn, xp)}</span></span></div>')
    to_in = _chips(list(to)) if to else '<span class="m-ph">Recipients</span>'
    links = (f'<span class="m-lnks"><span class="m-lnk">Cc</span>' + ('' if show_bcc else f'<span class="m-lnk{_t(ln)}">{_lab("Bcc", ln)}{_bd(ln, lp)}</span>') + '</span>')
    rows = (f'<div class="m-fld{_t(tn)}"><span class="m-lab">To</span><span class="m-in">{to_in}{caret if cursor == "to" else ""}</span>{links}{_bd(tn, tp)}</div>')
    if show_bcc:
        bcc_in = _chips(list(bcc)) if bcc else ''
        rows += (f'<div class="m-fld{_t(bn)}"><span class="m-lab">Bcc</span><span class="m-in">{bcc_in}{caret if cursor == "bcc" else ""}</span>{_bd(bn, bp)}</div>')
    subj = _e(subject) if subject else '<span class="m-ph">Subject</span>'
    rows += f'<div class="m-fld{_t(sn)}"><span class="m-in m-subject">{subj}{caret if cursor == "subject" else ""}</span>{_bd(sn, sp)}</div>'
    lines = ''.join(f'<span class="m-bl">{_e(t)}</span>' for t in body)
    rows += f'<div class="m-body{_t(yn)}">{lines}{caret if cursor == "body" else ""}{_bd(yn, yp)}</div>'
    send = (f'<span class="m-send{_t(vn)}">Send{_bd(vn, vp)}</span><span class="m-nope">Do not click</span>' if vn else '<span class="m-send">Send</span>')
    foot = (f'<div class="m-foot">{send}<span class="m-fi">A</span><span class="m-fi m-clip"></span>'
            f'<span class="m-trash{_t(rn)}"><span class="m-lid"></span><span class="m-can"></span>{_bd(rn, rp)}</span></div>')
    side = '<div class="m-side m-ghost"><span class="m-compose">Compose</span><span class="m-fold">Inbox</span><span class="m-fold">Drafts</span></div>'
    label = 'Drawing: Gmail in Microsoft Edge with a New Message window open. '
    label += (f'The To line has {_join(list(to))}. ' if to else 'The To line is empty and says Recipients. ')
    label += (f'The Bcc line has {_join(list(bcc))}. ' if show_bcc and bcc else ('A Bcc line is open and empty. ' if show_bcc else 'The words Cc and Bcc are at the right end of the To line. '))
    label += (f'The subject is {subject}. ' if subject else 'The subject is empty. ')
    label += (f'The message reads: {" ".join(body)} ' if body else 'The message is empty. ')
    label += 'A blue Send button is at the bottom left, and a trash can is at the bottom right.'
    names = {'to': 'the To line', 'bcc_link': 'the Bcc link', 'bcc': 'the Bcc line', 'subject': 'the Subject line',
             'body': 'the message box', 'send': 'the Send button, which you must not click', 'close': 'the X at the top right of the message window', 'trash': 'the trash can'}
    label += _said([(names[k], n) for k, (n, _) in marks.items()])
    return _root('gmail-compose', label, _gmail(f'<div class="m-cols">{side}<div class="m-win{" m-bcc" if show_bcc else ""}">{head}{rows}{foot}</div></div>', tab='Gmail'))


def gmail_drafts(subject, opened=False, targets=('drafts',)):
    """The Drafts folder with one draft; opened=True shows the draft open with its trash can marked."""
    marks = _marks(targets)
    if opened:
        return gmail_compose(to=('desk@example.com',), bcc=('sam@example.com', 'pat@example.com', 'lee@example.com'),
                             show_bcc=True, subject=subject, body=('Hi everyone,',), targets=targets)
    row = (f'<div class="m-row"><span class="m-from m-draft">Draft</span><span class="m-subj">{_e(subject)}</span></div>')
    label = (f'Drawing: Gmail in Microsoft Edge with the Drafts folder open. It lists one draft, with the subject {subject}.'
             + _said([('the Drafts folder', n) for _, (n, _) in marks.items()]))
    return _root('gmail-drafts', label, _gmail(_bar() + f'<div class="m-cols">{_side(marks, "Drafts", 1)}<div class="m-list">{row}</div></div>', tab='Drafts - Gmail'))


# ---------------------------------------------------------------- Word comments

_LINES = ('Computer help handout', 'Step 1: Choose one task.', 'Step 2: Visit the learning desk.', 'Step 3: Ask how to repeat it at home.')
_COMMENT = 'Add the contact number after the steps so readers can find help.'
_NUMBER = 'Help desk: 304-555-0142'


def word_review(stage='page', targets=(), added=False, selected=False, tab='Review'):
    """Word with the Review (or Home) tab open. stage: page (typed, no comment), new (empty comment box), typing, posted,
    replying, replied, menu (the ... menu open), resolved.
    targets: Review, New Comment, Post, Reply, more, Resolve, Save (keys, ringed and numbered in order)."""
    marks = _marks(targets)
    pn, pp = _get(marks, 'Post', 'l')
    rn, rp = _get(marks, 'Reply', 'l')
    mn, mp = _get(marks, 'more', 'tl')
    on, op = _get(marks, 'Resolve', 'l')
    lines = list(_LINES) + ([_NUMBER] if added else [])
    page = ''
    for i, t in enumerate(lines):
        cls = 'r-ln' + (' r-h' if i == 0 else '') + (' r-sel' if selected and i == 3 else '')
        page += f'<span class="{cls}">{_e(t)}</span>'
    card = ''
    if stage != 'page':
        done = stage == 'resolved'
        text = '' if stage == 'new' else _e(_COMMENT)
        typed = stage in ('new', 'typing')
        body = f'<span class="r-ct">{text}{"<span class=u-caret></span>" if typed else ""}</span>'
        post = f'<span class="r-post{_t(pn)}">{_lab("Post comment", pn)}{_bd(pn, pp)}</span>' if typed else ''
        menu = ''
        if stage in ('posted', 'replying', 'replied', 'menu'):
            menu = f'<span class="r-more{_t(mn)}">···{_bd(mn, mp)}</span>'
        if stage == 'menu':
            menu += (f'<span class="r-menu"><span class="r-mi{_t(on)}">{_lab("Resolve thread", on)}{_bd(on, op)}</span>'
                     '<span class="r-mi">Delete thread</span></span>')
        reply = ''
        if stage == 'posted':
            reply = f'<span class="r-reply{_t(rn)}">{_lab("Reply", rn)}{_bd(rn, rp)}</span>'
        elif stage == 'replying':
            reply = '<span class="r-reply r-typing">Added, thank you.<span class="u-caret"></span></span>'
        elif stage in ('replied', 'menu', 'resolved'):
            reply = '<span class="r-rtext"><b>You:</b> Added, thank you.</span>'
        who = 'Reviewer' if typed else 'Author'
        flag = '<span class="r-done">Resolved</span>' if done else ''
        card = f'<div class="r-card{" r-res" if done else ""}"><span class="r-who">{who}</span>{flag}{menu}{body}{post}{reply}</div>'
    on_ribbon = bool({'Review', 'New Comment'} & set(marks))  # only the screens that click the ribbon draw its buttons
    size = ' r-short' if on_ribbon else ' r-tall'
    below = f'<div class="r-split{size}"><div class="r-doc"><div class="r-page">{page}</div></div><div class="r-pane">{card}</div></div>'
    groups = ([('Clipboard', ['Paste']), ('Font', ['Bold', 'Italic']), ('Paragraph', ['Bullets', 'Numbering']), ('Styles', ['Normal', 'Heading 1'])]
              if tab == 'Home' else [('Proofing', ['Spelling']), ('Comments', ['New Comment', 'Delete', 'Previous', 'Next'])])
    label = (f'Drawing: Word with the {tab} tab open. '
             + ('The ribbon has a Comments group with New Comment, Delete, Previous and Next. ' if tab == 'Review' else '')
             + 
             f'The page shows: {" ".join(lines)}. ')
    label += ('The words of Step 3 are highlighted. ' if selected else '')
    label += {'page': 'There are no comments.', 'new': 'A comment box is open on the right with a blinking line and a Post comment button.',
              'typing': f'A comment box on the right holds the text {_COMMENT} and a Post comment button.',
              'posted': f'A comment on the right reads: {_COMMENT} Below it is a Reply box.',
              'replying': 'The comment on the right has a reply being typed: Added, thank you.',
              'replied': 'The comment on the right has your reply: Added, thank you.',
              'menu': 'The three-dot menu on the comment is open, listing Resolve thread and Delete thread.',
              'resolved': 'The comment on the right is grayed out and marked Resolved.'}[stage]
    names = {'Review': 'the Review tab', 'New Comment': 'the New Comment button', 'Post': 'the Post comment button',
             'Reply': 'the Reply box', 'more': 'the three-dot menu on the comment', 'Resolve': 'Resolve thread'}
    label += _said([(names.get(k, k), n) for k, (n, _) in marks.items()])
    # Ring targets live either on the ribbon (Review, New Comment) or in the comment box, never both on one drawing.
    assert not (on_ribbon and set(marks) - {'Review', 'New Comment'}), targets
    if on_ribbon:
        return ribbon('word', tab, groups, [t for t in targets if t in ('Review', 'New Comment')], below=below, name='word-review', label=label)
    inner = _title('Document1 - Word') + _tabrow('word', tab, {}) + below
    return _root('word-review', label, _win('app', inner, 'word'))


# ---------------------------------------------------------------- Edge pages on vublessons.com

def edge_worksheet_link(week=4, part='Part 4', label='Open the practice offer'):
    page = ('<div class="u-vub"><span class="u-vubm">VUB Learning</span></div><div class="u-wk">'
            f'<div class="u-wkh">Week {week} · Worksheet</div><div class="u-part">{_e(part)}</div>'
            f'<span class="u-gold u-t"><span class="u-big">{_e(label)}</span>{_bd(1, "r")}</span></div>')
    text = (f'Drawing: Microsoft Edge on vublessons.com, Week {week} Worksheet page. In {part}, the gold {label} button is marked 1.')
    return _root('edge-worksheet-link', text, _edge(f'Week {week} · Worksheet', f'vublessons.com/courses/digital-literacy-2/weeks/week-0{week}/worksheet', page))


def edge_offer(targets=()):
    """The practice offer page. targets: trial, first, price, cancel (ringed and numbered in order)."""
    marks = _marks(targets)

    def piece(key, text, pos, cls=''):
        n, p = _get(marks, key, pos)
        return f'<span class="o-p {cls}{_t(n)}">{_lab(text, n)}{_bd(n, p)}</span>'
    page = ('<div class="o-bar">Practice offer · fictional · nothing here can charge you</div><div class="o-pg">'
            '<div class="o-brand">MapleStream</div>'
            f'<div class="o-big">{piece("trial", "Free for 7 days", "tr", "o-free")}</div>'
            f'<div class="o-then">then {piece("price", "$12 each month", "tr", "o-price")}</div>'
            '<span class="o-btn">Start free trial</span>'
            '<div class="o-fine">'
            f'{piece("first", "Your first charge is on day 8.", "r", "o-line")}'
            '<span class="o-line">After that, $12 is charged every month until you cancel.</span>'
            f'{piece("cancel", "To cancel: Account › Billing › Cancel plan.", "r", "o-line")}</div></div>')
    names = {'trial': 'the words Free for 7 days', 'first': 'the line Your first charge is on day 8', 'price': 'the price, $12 each month',
             'cancel': 'the line about cancelling'}
    label = ('Drawing: a practice offer page for a fictional service called MapleStream in Microsoft Edge. A banner says it is fictional and nothing '
             'can charge you. The page says Free for 7 days, then $12 each month, with a Start free trial button. The small print says: Your first '
             'charge is on day 8. After that, $12 is charged every month until you cancel. To cancel: Account, Billing, Cancel plan.'
             + _said([(names[k], n) for k, (n, _) in marks.items()]))
    return _root('edge-offer', label, _edge('MapleStream · Practice offer', 'vublessons.com/courses/digital-literacy-2/activities/free-trial-offer', page))
