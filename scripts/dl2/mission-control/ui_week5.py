"""Week 5 drawings for the guided deck (original HTML/CSS, not screenshots). guided.drawing() looks names up here
after ui and ui_mail. Shared helpers stay in ui.py.

Same rules as ui.py: div/span only, every thing to click is ringed (.u-t) AND numbered (.u-bd), no text below
1.15cqw. Styles are in courses/digital-literacy-2/os/ui-week5.css, loaded only by Week 5. The pages they draw are
activities/practice-signup.html and activities/practice-mail.html?inbox=week-5.
"""
from ui import _bd, _dd, _e, _edge, _get, _join, _lab, _marks, _root, _said, _t, _title, _win, ribbon
from ui_mail import _bar, _side

__all__ = ['excel_signin', 'edge_signup', 'mail5_inbox', 'mail5_message', 'phone_compare']

SIGNUP_URL = 'vublessons.com/courses/digital-literacy-2/activities/practice-signup'
MAIL5_URL = 'vublessons.com/courses/digital-literacy-2/activities/practice-mail?inbox=week-5'
LINK_DEST = 'maple-valley-confirm.example.net/login'
SWATCHES = [('Dark Red', '#c00000'), ('Red', '#ff0000'), ('Orange', '#ffc000'), ('Yellow', '#ffff00'), ('Light Green', '#92d050'),
            ('Green', '#00b050'), ('Light Blue', '#00b0f0'), ('Blue', '#0070c0'), ('Dark Blue', '#002060'), ('Purple', '#7030a0')]
FILL_NAME = {'green': 'green', 'red': 'red'}


# ---------------------------------------------------------------- Excel sign-in sheet

def _palette(pick, number):
    """Fill Color list, open. pick: the colour name that is ringed and numbered."""
    sw = ''
    for name, hexv in SWATCHES:
        hit = name == pick
        sw += (f'<span class="w5-sw{_t(number if hit else 0)}" style="background:{hexv}">{_bd(number, "t") if hit else ""}</span>')
    return (f'<span class="w5-pal"><span class="w5-pt">Standard Colors</span><span class="w5-swrow">{sw}</span>'
            f'<span class="w5-pc">Click the {pick.lower()} square: number {[n for n, _ in SWATCHES].index(pick) + 1} from the left.</span></span>')


def _grid(cells, fills, selected, active, marks, rows):
    cols = 'ABCD'
    sel = set(selected)
    acol, arow = (active[0], active[1:]) if active else ('', '')
    out = ['<span class="u-xc u-xh u-xcorner"></span>']
    out += [f'<span class="u-xc u-xh{" u-on" if c == acol else ""}">{c}</span>' for c in cols]
    for r in range(1, rows + 1):
        out.append(f'<span class="u-xc u-xh u-xr{" u-on" if str(r) == arow else ""}">{r}</span>')
        for ci, c in enumerate(cols):
            addr = f'{c}{r}'
            v = str(cells.get(addr, ''))
            n, pos = _get(marks, addr, 'tr' if ci < 2 else 'tl')
            cls = ('u-xc' + (f' w5-{fills[addr]}' if addr in fills else '') + (' w5-sel' if addr in sel else '')
                   + (' u-act' if addr == active else '') + _t(n))
            out.append(f'<span class="{cls}"><span class="u-xv">{_lab(v, n) if v else ""}</span>{_bd(n, pos)}</span>')
    return f'<div class="u-grid w5-grid">{"".join(out)}</div>'


def excel_signin(cells=None, fills=None, selected=(), active=None, tab=None, targets=(), pick=None):
    """Excel with the sign-in sheet. cells: {'A1': 'Name'}; fills: {'B2': 'green'}; selected: shaded cells.
    tab=None draws the grid with a formula bar; tab='Home' draws the Home ribbon above a short grid, with targets
    from the ribbon (Home, Fill Color) and, when pick is a colour name, its Fill Color list open (swatch marked 2)."""
    cells, fills = dict(cells or {}), dict(fills or {})
    tail = ''
    if fills:
        tail += ' ' + _join([f'cell {k} is filled {FILL_NAME[v]}' for k, v in sorted(fills.items())]).capitalize() + '.'
    body = (f'Cells: {"; ".join(f"{k} {v}" for k, v in sorted(cells.items(), key=lambda kv: (int(kv[0][1:]), kv[0][0])))}. ' if cells else 'The cells are empty. ')
    if selected:
        body += f'Shaded gray (selected): {_join(sorted(selected))}. '
    if tab:
        in_ribbon = [t for t in targets if t in ('Home', 'Fill Color')]
        marks = _marks(targets)
        menus = None
        if pick:
            pick = pick.capitalize()
            swatch_n = 2 if in_ribbon else 1
            menus = {'Fill Color': _palette(pick, swatch_n)}
        grid = _grid(cells, fills, selected, active, {}, 5 if cells else 4)
        label = (f'Drawing: Excel with the Home tab open, showing the Fill Color button in the Font group. {body}'
                 + (f'The Fill Color list is open, with the {pick.lower()} square marked {swatch_n}. ' if pick else '')
                 + _said([('the Home tab' if k == 'Home' else 'the Fill Color button', n) for k, (n, _) in marks.items()]) + tail)
        groups = [('Clipboard', ['Paste']), ('Font', ['Bold', 'Fill Color']), ('Alignment', ['Wrap Text'])]
        return ribbon('excel', 'Home', groups, in_ribbon, menus=menus, below=grid, name='excel-signin', label=label.strip())
    marks = _marks(targets)
    grid = _grid(cells, fills, selected, active, marks, 5)
    shown = cells.get(active, '') if active else ''
    fx = (f'<div class="u-fx"><span class="u-nbox">{_e(active or "")}{_dd()}</span><span class="u-fxs"><span class="u-fxl">fx</span></span>'
          f'<span class="u-fxi">{_e(shown)}</span></div>')
    inner = _title('Book1 - Excel') + fx + grid + '<div class="u-sheets"><span class="u-sheet">Sheet1</span><span class="u-plus">+</span></div>'
    pairs = [(f'cell {k}', n) for k, (n, _) in marks.items()]
    label = ('Drawing: an Excel sheet with columns A to D and rows 1 to 5. ' + body
             + (f'The active cell is {active}, with a thick green border. ' if active else '') + _said(pairs) + tail)
    return _root('excel-signin', label.strip(), _win('app', inner, 'excel'))


# ---------------------------------------------------------------- practice sign-up page in Edge

def edge_signup(stage='form', email='', password='', message='', bad=False, code='', targets=()):
    """The practice sign-up page. stage: form, two_step, code, done. targets: email, password, create, text_code, code, verify."""
    marks = _marks(targets)

    def field(key, lab, value, pos='r'):
        n, p = _get(marks, key, pos)
        return (f'<div class="s-row"><span class="s-lab">{lab}</span><span class="s-in{_t(n)}">{_lab(value, n) if value else ""}'
                f'{"" if value else "<span class=u-caret></span>" if n else ""}{_bd(n, p)}</span></div>')

    def button(key, text, cls='s-btn', pos='tr'):
        n, p = _get(marks, key, pos)
        return f'<span class="{cls}{_t(n)}">{_lab(text, n)}{_bd(n, p)}</span>'

    bar = '<div class="o-bar">Practice sign-up · fictional · nothing here is saved or sent</div>'
    if stage == 'form':
        msg = f'<div class="s-msg{" s-bad" if bad else ""}">{_e(message)}</div>' if message else ''
        page = (bar + '<div class="o-pg"><div class="o-brand">Riverbend Reading Club</div><div class="s-h">Create your account</div>'
                + field('email', 'Email', email) + field('password', 'Password', password)
                + button('create', 'Create account') + msg + '</div>')
        label = ('Drawing: a practice sign-up page for a fictional Riverbend Reading Club in Microsoft Edge. It has an Email box'
                 + (f' holding {email}' if email else ', empty') + ' and a Password box' + (f' holding {password}' if password else ', empty')
                 + ', and a Create account button.' + (f' A message says: {message}' if message else ''))
    elif stage == 'two_step':
        page = (bar + '<div class="o-pg"><div class="s-keep">Password accepted. It is long. Use it on this one site only.</div><div class="s-h">Turn on two-step verification</div>'
                '<div class="s-p">A second lock: the site sends a code to your phone.</div>'
                + f'<div class="s-btns">{button("text_code", "Text me a code")}<span class="s-btn s-plain">Skip for now</span></div></div>')
        label = ('Drawing: the practice sign-up page after the password was accepted. A green note says the password is long and should be used on this one site only. '
                 'The heading is Turn on two-step verification, with two buttons: Text me a code and Skip for now.')
    elif stage == 'code':
        pn, pp = _get(marks, 'phone', 'r')
        phone = ('<div class="s-phone"><span class="s-pbar"></span><div class="s-bub"><span class="s-from">Riverbend Reading Club</span>Your code is'
                 f'<span class="s-num{_t(pn)}">{_lab("482913", pn)}{_bd(pn, pp)}</span>Do not share it.</div></div>')
        page = (bar + '<div class="o-pg s-split"><div class="s-left"><div class="s-h">Check your phone</div>' + field('code', 'Code', code)
                + button('verify', 'Verify') + '</div>' + phone + '</div>')
        label = ('Drawing: the practice sign-up page, Check your phone. At the right is a drawing of a phone with a text message: Your code is 482913. Do not share it. '
                 'At the left are a Code box' + (f' holding {code}' if code else '') + ' and a Verify button.')
    else:
        page = (bar + '<div class="o-pg"><div class="s-done"><div class="s-h s-ok">Two-step verification is on</div>'
                '<div class="s-p">Your practice account has a long password used nowhere else, and a code sent to your phone.</div></div></div>')
        label = 'Drawing: the practice sign-up page. A green box says Two-step verification is on.'
    names = {'email': 'the Email box', 'password': 'the Password box', 'create': 'the Create account button', 'text_code': 'the Text me a code button',
             'code': 'the Code box', 'verify': 'the Verify button', 'phone': 'the six-digit code on the phone'}
    label += _said([(names[k], n) for k, (n, _) in marks.items()])
    return _root('edge-signup', label, _edge('Riverbend Reading Club · Practice sign-up', SIGNUP_URL, page))


# ---------------------------------------------------------------- Practice Mail, Week 5 inbox

def mail5_inbox(targets=()):
    marks = _marks(targets)
    n, p = _get(marks, 'row', 'r')
    row = (f'<div class="m-row{_t(n)}"><span class="m-from">{_lab("Maple Valley Health Plan", n)}</span>'
           f'<span class="m-subj">ACT NOW: your coverage stops today</span>{_bd(n, p)}</div>')
    label = ('Drawing: Practice Mail in Microsoft Edge. At the left is a Compose button above the folders Inbox, Drafts and Sent. '
             'The Inbox lists one message, from Maple Valley Health Plan, with the subject ACT NOW: your coverage stops today.'
             + _said([('the message from Maple Valley Health Plan', k) for _, (k, _) in marks.items()]))
    inner = _bar() + f'<div class="m-cols">{_side({})}<div class="m-list">{row}</div></div>'
    return _root('mail5-inbox', label, _edge('Practice Mail', MAIL5_URL, f'<div class="m-gm">{inner}</div>'))


def mail5_message(targets=(), status=False, reported=False, warn=False):
    """The suspicious message open. targets: act (ACT NOW in the subject), today (stops today), hour (within 1 hour),
    from, link, phone, report. status: Edge's address strip at the bottom left, as when the pointer is on the link."""
    marks = _marks(targets)

    def piece(key, text, pos='tr'):
        n, p = _get(marks, key, pos)
        return f'<span class="w5-p{_t(n)}">{_lab(text, n)}{_bd(n, p)}</span>'
    fn, fp = _get(marks, 'from', 'r')
    frm = (f'<span class="m-ml"><b>From</b><span class="w5-f{_t(fn)}">{_lab("Maple Valley Health Plan", fn)}<span class="w5-addr">&lt;mvhp-memberhelp@example.com&gt;</span>{_bd(fn, fp)}</span></span>')
    subj = f'<span class="m-ml"><b>Subject</b>{piece("act", "ACT NOW")}: your coverage {piece("today", "stops today")}</span>'
    ln, lp = _get(marks, 'link', 'r')
    link = f'<span class="w5-link{_t(ln)}">{_lab("maplevalleyhealth.org/confirm", ln)}{_bd(ln, lp)}</span>'
    body = (f'<span class="w5-l">Your coverage {piece("today2", "stops today")} unless you {piece("act2", "act now")}.</span>'
            f'<span class="w5-l">Confirm your account {piece("hour", "within 1 hour")}: {link}</span>'
            f'<span class="w5-l">Or call us now at {piece("phone", "304-555-0199")} to keep your coverage.</span>')
    rn, rp = _get(marks, 'report', 'r')
    rep = f'<span class="w5-rep{_t(rn)}{" w5-done" if reported else ""}">{_lab("Reported" if reported else "Report this message", rn)}{_bd(rn, rp)}</span>'
    warn_html = ('<span class="w5-warn">Practice warning: the link did not open.</span>' if warn else '')
    stat = f'<span class="w5-status">{LINK_DEST}</span>' if status else ''
    page = (f'<div class="m-gm"><div class="w5-msg">{frm}{subj}'
            f'<div class="w5-body">{body}</div>{rep}{warn_html}</div></div>{stat}')
    names = {'act': 'ACT NOW in the subject', 'today': 'stops today in the subject', 'today2': 'stops today in the message', 'act2': 'act now in the message',
             'hour': 'within 1 hour', 'from': 'the From line', 'link': 'the blue link', 'phone': 'the phone number in the message', 'report': 'the Report button'}
    label = ('Drawing: Practice Mail with one message open. From: Maple Valley Health Plan, mvhp-memberhelp@example.com. Subject: ACT NOW: your coverage stops today. '
             'The message says: Your coverage stops today unless you act now. Confirm your account within 1 hour: maplevalleyhealth.org/confirm. '
             'Or call us now at 304-555-0199 to keep your coverage. A Report this message button is at the bottom.'
             + (f' At the bottom left, Edge shows the real address of the link: {LINK_DEST}.' if status else '')
             + (' The button now says Reported.' if reported else '') + (' A note says the practice link did not open.' if warn else '')
             + _said([(names[k], n) for k, (n, _) in marks.items()]))
    return _root('mail5-message', label, _edge('Practice Mail', MAIL5_URL, page))


# ---------------------------------------------------------------- the two phone numbers side by side

def phone_compare(targets=()):
    marks = _marks(targets)
    a, ap = _get(marks, 'message', 'tr')
    b, bp = _get(marks, 'letter', 'tr')
    left = ('<div class="w5-card"><span class="w5-ch">In the message</span><span class="w5-cl">Or call us now at</span>'
            f'<span class="w5-num">304-555-<span class="w5-d{_t(a)}">{_lab("0199", a)}{_bd(a, ap)}</span></span></div>')
    right = ('<div class="w5-card w5-letter"><span class="w5-ch">On your letter</span><span class="w5-cl">Member Services:</span>'
             f'<span class="w5-num">304-555-<span class="w5-d{_t(b)}">{_lab("0188", b)}{_bd(b, bp)}</span></span></div>')
    label = ('Drawing: two cards side by side. The message card says to call 304-555-0199. The letter card, from Maple Valley Health Plan, says to call Member Services at 304-555-0188. '
             'The last four digits are different.' + _said([({'message': 'the end of the message number', 'letter': 'the end of the letter number'}[k], n) for k, (n, _) in marks.items()]))
    return _root('phone-compare', label, f'<div class="w5-pair">{left}<span class="w5-ne" aria-hidden="true">is not</span>{right}</div>')
