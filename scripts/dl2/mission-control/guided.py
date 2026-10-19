"""Render a guided week (Weeks 3 and 4): deck, worksheet, answer guide, lesson plan, run sheet and notes.

Content lives in week3.py / week4.py. Drawings come from ui.py and ui_mail.py. Called from build.py for weeks whose dict
has guided=True; build.py still writes that week's practice library.
"""
import html
import inspect
import re

import ui
import ui_mail
from opening import media_url

BASE = '/courses/digital-literacy-2'


def e(t):
    return html.escape(str(t), quote=True)


def md(t):
    """Inline markup: [Label] on-screen name, {Key} keyboard key, «text» exact text."""
    t = e(t)
    t = re.sub(r'\[([^\]]+)\]', r'<b class="ui-name">\1</b>', t)
    t = re.sub(r'\{([^}]+)\}', r'<kbd>\1</kbd>', t)
    t = re.sub(r'«([^»]+)»', r'<span class="typed">\1</span>', t)
    return t


def plain(t):
    return re.sub(r'[\[\]{}«»]', '', t)


def end(text):
    """A sentence ending: add a period only when the text does not already end in . ? or !"""
    return text if text[-1:] in ('.', '?', '!') else text + '.'


def goal_ids(p):
    g = p.get('goals', p.get('goal'))
    return list(g) if isinstance(g, (list, tuple)) else [g]


def checks_of(p):
    c = p['check']
    return list(c) if isinstance(c, (list, tuple)) else [c]


def wrap_steps(wr):
    return wr['steps'] if 'steps' in wr else [wr['files']]


def mmss(seconds):
    s = int(round(seconds))
    return f'{s // 60}:{s % 60:02}'


def drawing(spec):
    if not spec:
        return ''
    name, kwargs = spec
    fn = getattr(ui, name, None) or getattr(ui_mail, name, None)
    if fn is None:
        return f'<div class="ui ui-missing" role="img" aria-label="Drawing not available">{e(name)}</div>'
    accepted = inspect.signature(fn).parameters
    return fn(**{k: v for k, v in kwargs.items() if k in accepted})


def app_tag(w, key, prefix='Working in:'):
    if not key:
        return '<span class="app">Mission Control</span>'
    return f'<span class="app app-{key}">{ui.app_badge(key, "sm")}<span>{e(prefix)} <b>{e(w["apps"][key])}</b></span></span>'


def build_week(n, w, target, letterhead):
    slides, notes_for, starts, schedule = [], [], [], []
    video_path = f'courses/digital-literacy-2/media/{w["video"]}'
    parts_n = len(w['parts'])
    goal_part = {g: k for k, p in enumerate(w['parts']) for g in goal_ids(p)}

    def add(title, body, phase, stage='', notes='', app=None, kind='', kicker='', prefix='Working in:'):
        i = len(slides) + 1
        kick = f'<span class="g-kicker">{e(kicker)}</span>' if kicker else ''
        slides.append(
            f'<section class="slide g-slide{" g-" + kind if kind else ""}" id="slide-{i}" data-phase="{phase}" data-stage="{stage}" data-scene="deck" aria-labelledby="s{i}">'
            f'<div class="panel full"><div class="hud"><img src="/assets/vub-seal-white.png" alt=""><span>Week {n}</span>{app_tag(w, app, prefix)}{kick}</div>'
            f'<h1 id="s{i}" tabindex="-1">{md(title)}</h1>{body}</div>'
            f'<aside class="notes"><h2>{e(plain(title))}</h2><p>{e(notes)}</p></aside></section>')
        return i

    def step_slide(s, part_app, kicker):
        acts = '<ol class="g-actions">' + ''.join(f'<li>{md(a)}</li>' for a in s['actions']) + '</ol>'
        see = f'<p class="g-see"><span>You should see:</span> {md(s["see"])}</p>'
        if s.get('card'):
            right = '<div class="g-card" data-visual role="group" aria-label="Lines to type"><p class="g-card-head">' + e(s.get("card_head") or "Type these lines:") + '</p>' + ''.join(f'<p>{e(line)}</p>' for line in s['card']) + '</div>'
        elif s.get('write'):
            right = f'<div class="g-write" data-visual><p class="g-card-head">{e(s.get("write_head") or "Your guess (worksheet, Part 3):")}</p><p>{md(s["write"])}</p><p class="g-blank" aria-hidden="true">______</p></div>'
        else:
            right = f'<div class="g-draw" data-visual>{drawing(s["draw"])}</div>'
        stuck = s.get('stuck')
        note = s.get('notes', '') + (f' If stuck: {plain(stuck[0])} {plain(stuck[1])}' if stuck else '')
        return add(s['title'], f'<div class="g-row"><div class="g-text">{acts}{see}</div>{right}</div>', 'practice', 'do', note.strip(), s.get('app') or part_app, 'step', kicker)

    def video(clip):
        src = f'{media_url(video_path + ".mp4")}#t={clip["start"]:.1f},{clip["end"]:.1f}'
        length = mmss(clip['end'] - clip['start'])
        return (f'<div class="g-watch"><video controls playsinline preload="metadata" tabindex="0" aria-label="Week {n} video clip: {e(clip["title"])}">'
                f'<source src="{src}" type="video/mp4"><track kind="captions" src="{media_url(video_path + ".vtt")}" srclang="en" label="English" default>'
                f'Your browser cannot play this video. The transcript has the same words.</video>'
                f'<div class="g-watch-text"><p><span class="g-label">Watch for:</span> {md(clip["look"])}</p><p>{length} long. It stops by itself.</p></div></div>')

    # Opening: welcome, warm-up, goals, plan.
    starts.append(0)
    first = add(w['title'], f'<div class="mission-hero"><div><p>Digital Literacy Level 2 · Week {n}</p><p>{e(w["hero"])}</p></div><figure><img src="{BASE}/assets/photos/{w["photo"]}.webp" alt="Illustrative West Virginia learning scenario"><figcaption>Fictional people and setting</figcaption></figure></div>',
                'warm-up', notes='Welcome learners by name. Tonight the class works together: you show each step on the projector and everyone does it at their own computer. F toggles fullscreen; N shows notes.')
    add('Start with what you know.', f'<p class="mission-prompt">{e(w["warm"])}</p><p>Share one example. Passing is welcome.</p>', 'warm-up',
        notes=w['warm_notes'])
    goals = '<ol class="g-goal-rows">' + ''.join(
        f'<li>{ui.app_badge(g["app"], "sm")}<span><b>Part {goal_part[k] + 1} · {e(w["apps"][g["app"]].replace("Microsoft ", ""))}:</b> {md(g["short"])}.</span></li>' for k, g in enumerate(w['goals'])) + '</ol>'
    add("Tonight's goals", f'<p class="g-lead">By the end of tonight, you can:</p>{goals}<p class="g-foot">{e(w["goals_foot"])}</p>', 'intro',
        notes=w['goals_notes'])
    add('How tonight works.', '<ol class="mission-principles"><li><span>1</span><div class="g-pt">Watch the step on the big screen.</div></li><li><span>2</span><div class="g-pt">Do the same step on your computer.</div></li>'
        '<li><span>3</span><div class="g-pt">Check <b>You should see</b>. Not the same? Raise your hand.</div></li></ol>'
        f'<p class="g-foot">The colored box at the top of every slide names the program you are in, like {app_tag(w, w["example_app"])}.</p>', 'intro',
        notes='Each part starts with a slide that names the program. Wait for every screen to match before you move on.')
    schedule.append((0, 8, 'Welcome, goals and plan', f'{first}–{len(slides)}'))

    # Before we start (Edge).
    r = w['ready']
    starts.append(len(slides))
    ready_first = len(slides) + 1
    for k, s in enumerate(r['steps']):
        step_slide(s, 'edge', f'Before we start · Step {k + 1} of {len(r["steps"])}')
    schedule.append((8, 13, 'Before we start: open the worksheet', f'{ready_first}–{len(slides)}'))

    minutes = w['minutes']
    elapsed = 13
    for k, p in enumerate(w['parts']):
        part_n = k + 1
        app = p['app']
        app_name = w['apps'][app]
        starts.append(len(slides))
        pfirst = len(slides) + 1
        lead = 'Still working in' if p.get('still') else 'Now working in'
        goal_lines = ''.join(f'<p class="g-goal"><span class="g-label">Goal {g + 1}:</span> {md(w["goals"][g]["short"])}</p>' for g in goal_ids(p))
        open_note = p.get('open_note') or ('We stay in Word for this part.' if p.get('still') else 'Everyone will open it in a moment.')
        add(f'{lead}: {app_name}',
            f'<div class="g-orient">{ui.app_badge(app, "lg")}<div><p class="g-what">{md(p["what"])}</p><p><span class="g-label">You will make:</span> {md(p["make"])}</p>'
            f'{goal_lines}</div></div>',
            'present', 'tell', f'Part {part_n} of {parts_n}. Say the program name out loud. {open_note}', app, 'orient', f'Part {part_n} of {parts_n}', 'Working in:')
        t = p['tell']
        add(t['title'], '<ol class="mission-principles">' + ''.join(f'<li><span>{i + 1}</span><div class="g-pt">{md(x)}</div></li>' for i, x in enumerate(t['points'])) + '</ol>', 'present', 'tell', t['notes'], app, 'tell', f'Part {part_n} · Why it matters')
        for clip in p['watch']:
            add(clip['title'], video(clip), 'present', 'show', clip['notes'] + ' Press Play; it never starts by itself. Captions are on.', app, 'watch', f'Part {part_n} · Watch')
        steps = [s for s in p['steps'] if s['kind'] == 'step']
        numbered = 0
        for s in p['steps']:
            if s['kind'] == 'map':
                items = '<ol class="g-map">' + ''.join(f'<li>{md(x)}</li>' for x in s['items']) + '</ol>'
                add(s['title'], f'<div class="g-row"><div class="g-text">{items}</div><div class="g-draw" data-visual>{drawing(s["draw"])}</div></div>', 'practice', 'do', s['notes'], app, 'map', f'Part {part_n} · Know your screen')
                continue
            numbered += 1
            step_slide(s, app, f'Part {part_n} · Step {numbered} of {len(steps)}')
        for c in checks_of(p):
            add(c['question'], f'<div class="mission-check" data-answer="{c["answer"]}" data-why="{e(c["why"])}">' + ''.join(
                f'<button type="button" data-choice="{j}"><b>{chr(65 + j)}</b> {e(ch)}</button>' for j, ch in enumerate(c['choices'])) +
                '<p class="mission-feedback" role="status">Choose an answer, then explain your reason.</p><button type="button" class="check-reset">Try again</button></div>',
                'evaluate', 'review', f'Ask everyone to choose before you select an answer. Correct answer: {end(c["choices"][c["answer"]])} {c["why"]}', app, 'check', f'Part {part_n} · Check')
        schedule.append((elapsed, elapsed + minutes[k], f'Part {part_n} · {app_name}: {p["title"]}', f'{pfirst}–{len(slides)}'))
        elapsed += minutes[k]

    # Wrap-up.
    wr = w['wrap']
    starts.append(len(slides))
    wfirst = len(slides) + 1
    def show_slide():
        add('Show your instructor.', '<ol class="g-map">' + ''.join(f'<li>{md(x)}</li>' for x in wr['show']) + '</ol>', 'evaluate', '', w['show_notes'], None, 'show', 'Wrap-up')

    if wr.get('show_first'):
        show_slide()
    for s in wrap_steps(wr):
        step_slide(s, s.get('app') or 'explorer', 'Wrap-up')
    if not wr.get('show_first'):
        show_slide()
    add('I can…', '<ul class="g-goals g-ican">' + ''.join(f'<li>{ui.app_badge(g["app"], "sm")}<span>{md(g["short"])}.</span></li>' for g in w['goals']) + '</ul><p class="g-foot">Check each box on your worksheet that you can do now.</p>', 'apply', '',
        'Celebrate one concrete result per learner. Anything unchecked is the first thing to practice next week.', None, 'ican', 'Wrap-up')
    add('Take it home.', f'<p class="mission-prompt">{md(wr["home"])}</p><div class="mission-actions"><a href="worksheet.html">Keep your worksheet</a><a href="video-transcript.html">Replay the video</a></div>', 'apply', '',
        w['home_notes'], None, 'home', 'Wrap-up')
    add('Mission complete.', f'<p>{e(w["done"])}</p><div class="mission-actions"><a href="{BASE}/index.html">Return to course home</a></div>', 'apply', '',
        'Collect evidence, not just confidence. Restore shared settings.', None, 'done')
    schedule.append((elapsed, 120, 'Wrap-up: check, I can, take it home', f'{wfirst}–{len(slides)}'))
    assert 120 - elapsed == 12, elapsed  # wrap-up: evidence check, I can, take it home

    # Deck page.
    jump_labels = w['jump_labels']
    nav = ('<nav class="mission-toolbar" aria-label="Presentation controls">' + f'<a href="{BASE}/index.html">Course home</a>'
           '<button type="button" data-deck-prev>Back</button><button type="button" data-deck-next>Next</button><button type="button" data-deck-notes aria-expanded="false">Notes (N)</button><button type="button" data-deck-full>Fullscreen (F)</button>'
           '<label>Jump to <select data-mission-jump>' + ''.join(f'<option value="{s}">{e(t)}</option>' for s, t in zip(starts, jump_labels)) + '</select></label></nav>')
    head = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Week {n} · {e(w["title"])} · VUB</title>'
            f'<link rel="stylesheet" href="{BASE}/os/fonts.css"><link rel="stylesheet" href="{BASE}/os/deck.css"><link rel="stylesheet" href="{BASE}/os/missions.css">'
            f'<link rel="stylesheet" href="{BASE}/os/ui-drawings.css"><link rel="stylesheet" href="{BASE}/os/guided.css">'
            + ''.join(f'<link rel="stylesheet" href="{BASE}/os/{c}">' for c in w.get('css', ())) + '</head>')
    (target / 'presentation.html').write_text(
        head + f'<body class="dl2-os mission-series guided-deck"><a class="mission-skip" href="#main">Skip to lesson</a>{nav}<main id="main" tabindex="-1" class="deck" aria-label="Week {n} presentation">'
        + ''.join(slides) + f'</main><script src="{BASE}/os/deck.js"></script><script src="{BASE}/os/missions.js"></script><script src="/shared/text-size.js"></script></body></html>')

    # Paper pages.
    def page(title, body, private=False):
        return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Week {n} · {e(title)} · VUB</title>'
                + ('<meta name="robots" content="noindex">' if private else '') +
                f'<link rel="stylesheet" href="{BASE}/os/fonts.css"><link rel="stylesheet" href="{BASE}/os/paper.css"><link rel="stylesheet" href="{BASE}/os/mission-paper.css"><link rel="stylesheet" href="{BASE}/os/guided.css"></head>'
                f'<body class="mission-paper guided-paper{" run-sheet" if title == "Instructor run sheet" else ""}"><nav class="paper-actions no-print" aria-label="Week resources"><button type="button" data-print>Print / Save as PDF</button>'
                f'<a href="presentation.html#1">Lesson</a><a href="worksheet.html">Worksheet</a><a href="{BASE}/index.html">Course home</a></nav>'
                f'<main class="paper-doc">{letterhead(n)}<h1>Week {n} · {e(title)}</h1>{body}</main><script src="{BASE}/os/mission-paper.js"></script><script src="/shared/text-size.js"></script></body></html>')

    def steps_list(items):
        out = '<ol class="mission-steps">'
        for k, s in enumerate(items, start=1):
            detail = ' '.join(md(a) for a in s['actions'])
            extra = ''
            if s.get('card'):
                extra = '<span class="g-type-card">' + '<br>'.join(e(x) for x in s['card']) + '</span>'
            if s.get('write'):
                fid = 'predict-' + re.sub(r'[^a-z0-9]+', '-', s['title'].lower()).strip('-')
                extra = f'<label class="g-write-label" for="{fid}">{md(s["write"])}</label><textarea class="worksheet-input" id="{fid}" rows="{s.get("write_rows") or 1}"></textarea><span class="print-answer"></span>'
            out += (f'<li><span class="n">{k}</span><div class="d"><b class="act">{md(s["title"])}.</b> {detail}{extra}<span class="see">{md(s["see"])}</span></div>'
                    f'<label class="box"><input type="checkbox"><span class="visually-hidden">Done: {e(plain(s["title"]))}</span></label></li>')
        return out + '</ol>'

    def stuck_box(pairs):
        return '<div class="stuck"><h4>IF YOU GET STUCK</h4>' + ''.join(f'<p><b>{md(a)}</b> {md(b)}</p>' for a, b in pairs) + '</div>'

    ws = ('<p class="g-intro">Follow along with the slides: each step there is a step here. Check the box when you see what <b>You should see</b> describes. '
          f'{e(w["ws_note"])}</p><div class="namerow"><span>Name</span><span>Workstation</span></div>')
    ws += '<section class="g-goal-box"><h2>Tonight’s goals</h2><p>Check each one at the end of class if you can do it.</p><ul class="g-ican-list">' + ''.join(
        f'<li><label><input type="checkbox"> <span>I can {md(g["short"][0].lower() + g["short"][1:])}. <small>({e(w["apps"][g["app"]])})</small></span></label></li>' for g in w['goals']) + '</ul></section>'
    if w.get('words'):
        ws += ('<section class="g-words"><h2>Words we use tonight</h2><dl>'
               + ''.join(f'<dt>{e(a)}</dt><dd>{md(b)}</dd>' for a, b in w['words']) + '</dl></section>')
    ws += (f'<section class="mission g-part" id="ready"><div class="mhead"><div><div class="k">BEFORE WE START · MICROSOFT EDGE</div><h2>{e(r["title"])}</h2></div></div>'
           f'<p>{md(r["what"])}</p>{steps_list(r["steps"])}{stuck_box([s["stuck"] for s in r["steps"] if s.get("stuck")])}</section>')
    answer = ('<p>Assess observable evidence. A spoken prompt is “With prompt”; using the worksheet alone counts as independent. '
              f'{e(w["answer_note"])}</p>')
    for k, p in enumerate(w['parts']):
        mid = f'{n}{chr(65 + k)}'
        app_name = w['apps'][p['app']]
        steps = [s for s in p['steps'] if s['kind'] == 'step']
        maps = [s for s in p['steps'] if s['kind'] == 'map']
        screen = ''
        if maps:
            screen = '<div class="g-screen"><b>Know your screen:</b> ' + ' · '.join(md(x) for x in maps[0]['items']) + '</div>'
        download = p.get('worksheet_extra', '')
        cs = checks_of(p)
        gids = goal_ids(p)
        ws += (f'<section class="mission g-part" id="m{mid}"><div class="mhead"><div><div class="k">PART {k + 1} OF {parts_n} · {e(app_name.upper())}</div><h2>{e(p["title"])}</h2></div>'
               f'<div class="badges"><span class="do">GOAL{"S" if len(gids) > 1 else ""} {", ".join(str(g + 1) for g in gids)}</span></div></div>'
               f'<div class="mission-ab"><div class="a"><small>POINT A · YOU START HERE</small>{md(p["start"])}</div><div class="arr" aria-hidden="true">→</div><div class="b"><small>POINT B · YOU’RE DONE WHEN</small>{md(p["finish"])}</div></div>'
               f'{download}{screen}{steps_list(steps)}<div class="two">{stuck_box(p["stuck"])}'
               f'<div class="check"><h4>CHECK YOURSELF</h4>' + ''.join(
                   f'<p>{e(c["question"])}</p><p>' + ' · '.join(f'{chr(65 + j)}. {e(ch)}' for j, ch in enumerate(c['choices'])) + '</p><p>My answer: <span class="ln"></span></p>' for c in cs) + '</div></div></section>')
        answer += (f'<section><h2>Part {k + 1} · {e(app_name)}: {e(p["title"])}</h2>' + ''.join(
                   f'<p><b>Goal {g + 1}</b> (post-test item {w["goals"][g]["item"]}): {md(w["goals"][g]["text"])}</p>' for g in gids) +
                   f'<p><b>Evidence:</b> {e(w["outcomes"][k])}</p>' + ''.join(f'<p><b>Check:</b> {e(c["question"])} <b>{e(end(c["choices"][c["answer"]]))}</b> {e(c["why"])}</p>' for c in cs) +
                   '<p><b>Common problems</b></p><ul>' + ''.join(f'<li><b>{md(a)}</b> {md(b)}</li>' for a, b in p['stuck']) + '</ul></section>')
    show = '<p><b>Show your instructor:</b></p><ul>' + ''.join(f'<li>{md(x)}</li>' for x in wr['show']) + '</ul>'
    ws += (f'<section class="mission g-part" id="wrap"><div class="mhead"><div><div class="k">WRAP-UP · {e(wr["label"])}</div><h2>Check your work</h2></div></div>'
           + (show + steps_list(wrap_steps(wr)) if wr.get('show_first') else steps_list(wrap_steps(wr)) + show)
           + f'<div class="home"><b>TAKE IT HOME</b>{md(wr["home"])}</div></section>')
    res = wr.get('result')
    if res:
        fields = ''.join(
            f'<label class="g-write-label" for="result-{i}">{md(lab)}</label><textarea class="worksheet-input" id="result-{i}" rows="{rows}"></textarea><span class="print-answer"></span>'
            for i, (lab, rows) in enumerate(res['fields'], start=1))
        ws += (f'<section class="mission g-part g-result" id="result"><div class="mhead"><div><div class="k">MY RESULT</div><h2>{e(res["title"])}</h2></div></div>'
               f'<p>{md(res["intro"])}</p>{fields}</section>')
    answer += ('<section><h2>End-of-class check</h2><ul>' + ''.join(f'<li>{md(x)}</li>' for x in wr['show']) + '</ul>'
               '<p>Record Independent, With prompt or Needs practice for each. Re-show only the missing step.</p></section>')
    if res:
        answer += '<section><h2>My result page</h2><ul>' + ''.join(f'<li>{md(lab)}</li>' for lab, _ in res['fields']) + '</ul><p>Collect the page, or read it on screen. Every box should hold the learner\'s own words.</p></section>'
    (target / 'worksheet.html').write_text(page('Worksheet', ws))
    (target / 'answer-key.html').write_text(page('Answer and observation guide', answer, True))

    table = '<table><thead><tr><th>Elapsed minutes</th><th>Slides</th><th>Segment</th></tr></thead><tbody>' + ''.join(
        f'<tr><td>{a}–{b} ({b - a} min)</td><td>{s}</td><td>{e(t)}</td></tr>' for a, b, t, s in schedule) + '</tbody></table>'
    clips = '<ul>' + ''.join(f'<li>Part {k + 1}: {e(c["title"].replace("Watch: ", ""))}, {mmss(c["start"])} to {mmss(c["end"])} of the Week {n} video.</li>' for k, p in enumerate(w['parts']) for c in p['watch']) + '</ul>'
    quick = '<h2>Quick card</h2><dl class="quick-card">' + ''.join(f'<dt>{e(a)}</dt><dd>{md(b)}</dd>' for a, b in w['quick']) + '</dl>'
    plan_html = ('<h2>Objectives</h2><ul>' + ''.join(f'<li>{md(g["text"])} ({e(w["apps"][g["app"]])}; post-test item {g["item"]})</li>' for g in w['goals']) + '</ul>'
                 '<h2>Observable outcomes</h2><ul>' + ''.join(f'<li>{e(o)}</li>' for o in w['outcomes']) + '</ul>'
                 '<h2>How this lesson runs</h2><p>You project the deck and the class does each step together, one or two clicks per slide. Every step slide names the program in its top corner, gives the clicks, and says what learners should see. The worksheet repeats every step with a check box, so anyone who falls behind can catch up, and adds an If you get stuck box for each part. Wait for every screen to match before moving on.</p>'
                 f'<p>{e(w["plan_scope"])}</p>'
                 f'<h2>120-minute plan</h2>{table}<h2>Video clips</h2><p>The full video is not played. Each Watch slide plays only its own clip, with captions, and stops by itself:</p>{clips}'
                 f'{quick}<h2>Week-specific preparation</h2><p>{e(w["prep"])}</p>'
                 f'<h2>Instructor support</h2><p><a href="{BASE}/weeks/week-{n:02}/answer-key.html">Answer and observation guide</a> · <a href="run-sheet.html">Run sheet</a> · <a href="instructor-notes.html">All slide notes</a></p>')
    (target / 'lesson-plan.html').write_text(page('Lesson plan', plan_html, True))
    (target / 'run-sheet.html').write_text(page('Instructor run sheet', table + '<p><b>Keys:</b> arrows / Page Up / Page Down · F fullscreen · N notes · B blackout · number + Enter jumps. Use Jump to for each part. Video clips play only when you press Play and stop by themselves.</p><p>Every step: show it, wait for every screen to match <b>You should see</b>, then move on.</p>', True))
    notes = ''.join(f'<section><h2>Slide {i + 1}</h2>' + re.search(r'<aside class="notes">(.*?)</aside>', s).group(1) + '</section>' for i, s in enumerate(slides))
    (target / 'instructor-notes.html').write_text(page('Instructor notes', notes, True))
    return len(slides)
