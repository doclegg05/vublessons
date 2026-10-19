"""Week 4 drawings: Practice Mail in Edge, the taskbar, Word comments, the worksheet link and the practice offer page.

Same rules as ui.py: original HTML/CSS diagrams (not screenshots), div/span only, every thing to
click is ringed (.u-t) AND numbered (.u-bd), and no text below 1.15cqw. Styles are in
courses/digital-literacy-2/os/ui-week4.css, loaded only by Week 4. The shared helpers come from ui.py.
Practice Mail itself is courses/digital-literacy-2/activities/practice-mail.html.
"""
from ui import _bd, _e, _edge, _get, _join, _lab, _marks, _root, _said, _t, _tabrow, _title, _win, app_badge, ribbon

__all__ = ['taskbar', 'mail_inbox', 'mail_compose', 'mail_sent', 'word_review', 'edge_worksheet_link', 'edge_offer']

_MAIL_URL = 'vublessons.com/courses/digital-literacy-2/activities/practice-mail'
_ADDR_CAP = 4  # chips shown before "+ more"


def _icon(kind):
    return f'<span class="m-ic m-ic-{kind}"></span>'


# ---------------------------------------------------------------- the taskbar

def taskbar(targets=()):
    """The bottom of the Windows 10 screen: Start, the search box and the Edge icon."""
    marks = _marks(targets)
    en, ep = _get(marks, 'edge', 'tr')
    bar = ('<div class="m-tb"><span class="m-start"><span></span><span></span><span></span><span></span></span>'
           '<span class="m-tsearch"><span class="u-mag"></span>Type here to search</span>'
           f'<span class="m-ticon{_t(en)}">{app_badge("edge")}{_bd(en, ep)}</span><span class="m-ticon">{app_badge("explorer")}</span></div>')
    label = ('Drawing: the bottom of a Windows 10 screen. The taskbar is a long dark bar with the Start button at the left, a search box, '
             'a round Edge icon and a yellow File Explorer folder icon.'
             + _said([('the Edge icon', n) for _, (n, _) in marks.items()]))
    return _root('taskbar', label, f'<div class="m-desk"><span class="m-deskt">Your screen</span></div>{bar}')


# ---------------------------------------------------------------- Practice Mail

def _side(marks, active='Inbox', drafts=0, sent=0):
    """Left column: Compose button and the folder list."""
    cn, cp = _get(marks, 'compose', 'r')
    rows = ''
    for name, count in (('Inbox', 0), ('Drafts', drafts), ('Sent', sent)):
        c = f'<span class="m-cnt">{count}</span>' if count else ''
        rows += f'<span class="m-fold{" m-on" if name == active else ""}">{name}{c}</span>'
    return (f'<div class="m-side"><span class="m-compose{_t(cn)}">{_icon("pen")}<span class="{"u-big" if cn else ""}">Compose</span>'
            f'{_bd(cn, cp)}</span>{rows}</div>')


def _mail(inner, tab='Practice Mail'):
    return _edge(tab, _MAIL_URL, f'<div class="m-gm">{inner}</div>')


def _bar():
    return '<div class="m-top"><span class="m-logo">Practice Mail</span><span class="m-note">fictional \u00b7 nothing is sent</span></div>'


def mail_inbox(targets=('compose',)):
    marks = _marks(targets)
    rows = ''.join(f'<div class="m-row"><span class="m-from">{f}</span><span class="m-subj">{s}</span></div>'
                   for f, s in (('Library newsletter', 'October events at the library'), ('Volunteer desk', 'Thank you for helping last week'),
                                ('Computer class', 'Your Week 4 worksheet')))
    label = ('Drawing: Practice Mail in Microsoft Edge. At the left, a Compose button sits above the folders Inbox, Drafts and Sent. '
             'The Inbox lists three messages.' + _said([('the Compose button', n) for _, (n, _) in marks.items()]))
    return _root('mail-inbox', label, _mail(_bar() + f'<div class="m-cols">{_side(marks)}<div class="m-list">{rows}</div></div>'))


def _chips(addrs):
    shown = ''.join(f'<span class="m-chip">{_e(a)}</span>' for a in addrs[:_ADDR_CAP])
    return shown + (f'<span class="m-chip m-more">+{len(addrs) - _ADDR_CAP}</span>' if len(addrs) > _ADDR_CAP else '')


def _body_line(text, mark):
    t = _e(text)
    return t.replace(_e(mark), f'<span class="m-sel">{_e(mark)}</span>', 1) if mark and mark in text else t


def mail_compose(to=(), bcc=(), show_bcc=False, subject='', body=(), targets=(), cursor='', mark=''):
    """The New Message window. cursor: which field shows the blinking line (to, bcc, subject, body).
    mark: a word in the message to show shaded (selected)."""
    marks = _marks(targets)
    tn, tp = _get(marks, 'to', 'ir')
    ln, lp = _get(marks, 'bcc_link', 'b')
    bn, bp = _get(marks, 'bcc', 'ir')
    sn, sp = _get(marks, 'subject', 'ir')
    yn, yp = _get(marks, 'body', 'ir')
    xn, xp = _get(marks, 'close', 'l')
    vn, vp = _get(marks, 'send', 'tr')
    caret = '<span class="u-caret m-caret"></span>'
    head = (f'<div class="m-head"><span>New Message</span><span class="m-wc"><span class="m-x{_t(xn)}"><span class="u-x"></span>{_bd(xn, xp)}</span></span></div>')
    to_in = _chips(list(to)) if to else ''
    links = ('<span class="m-lnks"><span class="m-lnk">Cc</span>' + ('' if show_bcc else f'<span class="m-lnk{_t(ln)}">{_lab("Bcc", ln)}{_bd(ln, lp)}</span>') + '</span>')
    rows = (f'<div class="m-fld{_t(tn)}"><span class="m-lab">To</span><span class="m-in">{to_in}{caret if cursor == "to" else ""}</span>{links}{_bd(tn, tp)}</div>')
    if show_bcc:
        rows += (f'<div class="m-fld{_t(bn)}"><span class="m-lab">Bcc</span><span class="m-in">{_chips(list(bcc)) if bcc else ""}{caret if cursor == "bcc" else ""}</span>{_bd(bn, bp)}</div>')
    subj = _e(subject) if subject else '<span class="m-ph">Subject</span>'
    rows += f'<div class="m-fld{_t(sn)}"><span class="m-in m-subject">{subj}{caret if cursor == "subject" else ""}</span>{_bd(sn, sp)}</div>'
    lines = ''.join(f'<span class="m-bl">{_body_line(t, mark)}</span>' for t in body)
    rows += f'<div class="m-body{_t(yn)}">{lines}{caret if cursor == "body" else ""}{_bd(yn, yp)}</div>'
    foot = (f'<div class="m-foot"><span class="m-send{_t(vn)}">Send{_bd(vn, vp)}</span>'
            '<span class="m-trash"><span class="m-lid"></span><span class="m-can"></span></span></div>')
    side = '<div class="m-side m-ghost"><span class="m-compose">Compose</span><span class="m-fold">Inbox</span><span class="m-fold">Drafts</span></div>'
    label = 'Drawing: Practice Mail in Microsoft Edge with a New Message box open. '
    label += (f'The To line has {_join(list(to))}. ' if to else 'The To line is empty. ')
    label += (f'The Bcc line has {_join(list(bcc))}. ' if show_bcc and bcc else ('A Bcc line is open and empty. ' if show_bcc else 'The words Cc and Bcc are at the right end of the To line. '))
    label += (f'The subject is {subject}. ' if subject else 'The subject is empty. ')
    label += (f'The message reads: {" ".join(body)} ' if body else 'The message is empty. ')
    label += (f'The word {mark} is shaded. ' if mark else '')
    label += 'A blue Send button is at the bottom left, and a trash can is at the bottom right.'
    names = {'to': 'the To line', 'bcc_link': 'the Bcc link', 'bcc': 'the Bcc line', 'subject': 'the Subject line',
             'body': 'the message box', 'send': 'the Send button', 'close': 'the X at the top right of the message box'}
    label += _said([(names[k], n) for k, (n, _) in marks.items()])
    return _root('mail-compose', label, _mail(f'<div class="m-cols">{side}<div class="m-win{" m-bcc" if show_bcc else ""}">{head}{rows}{foot}</div></div>'))


def mail_sent(subject, to=('desk@example.com',), bcc=('sam@example.com', 'pat@example.com', 'lee@example.com'), targets=('who',)):
    """The Sent view right after Send: the message, then the Who sees what box."""
    marks = _marks(targets)
    wn, wp = _get(marks, 'who', 'tr')
    rn, rp = _get(marks, 'sam', 'r')
    msg = ('<div class="m-msg"><span class="m-ml"><b>To</b>' + _e(', '.join(to)) + '</span><span class="m-ml"><b>Bcc</b>' + _e(', '.join(bcc))
           + f'</span><span class="m-ml"><b>Subject</b>{_e(subject)}</span></div>')
    rows = ''
    for r in to:
        rows += f'<span class="m-wr"><span class="m-wp">{_e(r)}</span><span class="m-ws">To: {_e(", ".join(to))}</span></span>'
    for r in bcc:
        key = r.split('@')[0] == 'sam'
        n = rn if key else 0
        rows += (f'<span class="m-wr{_t(n)}"><span class="m-wp">{_lab(_e(r), n) if n else _e(r)}</span>'
                 f'<span class="m-ws">To: {_e(", ".join(to))} only</span>{_bd(n, rp)}</span>')
    who = f'<div class="m-who{_t(wn)}"><span class="m-wh">Who sees what</span>{rows}{_bd(wn, wp)}</div>'
    label = (f'Drawing: Practice Mail after Send. The message shows To {", ".join(to)}, Bcc {", ".join(bcc)} and the subject {subject}. '
             'Below it, a box called Who sees what lists each person. The person in To sees To: desk@example.com. Each Bcc person sees To: desk@example.com '
             'and a note that the other Bcc addresses are hidden.'
             + _said([('the Who sees what box' if k == 'who' else 'the row for sam@example.com', n) for k, (n, _) in marks.items()]))
    return _root('mail-sent', label, _mail(f'<div class="m-pad"><span class="m-back">\u2190 Back</span>{msg}{who}</div>', tab='Practice Mail'))


# ---------------------------------------------------------------- Word comments

_LINES = ('Computer help handout', 'Step 1: Choose one task.', 'Step 2: Visit the learning desk.', 'Step 3: Ask how to repeat it at home.')
_COMMENT = 'Add the contact number after the steps so readers can find help.'
_NUMBER = 'Help desk: 304-555-0142'


def word_review(stage='page', targets=(), added=False, selected=False, tab='Review', upto=4):
    """Word with the Review (or Home) tab open. stage: page (typed, no comment), new (empty comment box), typing, posted,
    replying, replied, menu (the ... menu open), resolved.
    targets: Review, New Comment, Post, Reply, more, Resolve, Save (keys, ringed and numbered in order)."""
    marks = _marks(targets)
    pn, pp = _get(marks, 'Post', 'l')
    rn, rp = _get(marks, 'Reply', 'l')
    mn, mp = _get(marks, 'more', 'tl')
    on, op = _get(marks, 'Resolve', 'l')
    lines = list(_LINES[:upto]) + ([_NUMBER] if added else [])
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
    label += ('' if upto >= 4 else f'Only the first {upto} line{"s" if upto > 1 else ""} of the handout are typed so far. ')
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
