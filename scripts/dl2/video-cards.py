"""Topic dividers and pause cards laid over a week's chapters (Britt, 2026-10-08).

A week opts in with video/digital-literacy-2/week-NN/cards.json:
  {"chapters": {"beat-02": {"divider": {"app": "Word", "mission": "3A", "title": "..."}},
                "beat-03": {"pause": {"try": ["...", "...", "..."], "where": "Mission 3A, tasks 2 to 4"}}}}
normalize-pace.py gives a divider chapter a silent lead-in and a pause chapter a silent hold;
build-media.py calls clips() to place one card composition over each of those silent stretches.
Cards are full-frame, sit above the chapter scene (z-index), and never show a countdown.
"""
import html
import json
from pathlib import Path

E = lambda s: html.escape(str(s), quote=True)
DIVIDER_SECONDS = 3.0
PAUSE_DELAY = 0.3
CSS = ("@font-face{font-family:VUB;src:url('assets/source-sans-3-latin-400-normal.woff2')}"
       "@font-face{font-family:VUB;src:url('assets/source-sans-3-latin-700-normal.woff2');font-weight:700}"
       "#ID{position:relative;width:100%;height:100%;overflow:hidden;background:#102c4b;color:#F5F7FA;font-family:VUB,'Segoe UI',sans-serif}"
       "#ID .card{position:absolute;inset:0}"
       "#ID .rule{position:absolute;left:96px;width:1088px;height:4px;background:#E6C65C}"
       "#ID .label{position:absolute;left:96px;margin:0;font-size:32px;font-weight:700;letter-spacing:.12em;color:#E6C65C}"
       "#ID .brand{position:absolute;left:96px;bottom:40px;font-size:26px;color:#e5edf2;display:flex;align-items:center;gap:12px}"
       "#ID .brand img{width:40px;height:40px}")


def load(week_dir: Path) -> dict:
    path = week_dir / 'cards.json'
    return json.loads(path.read_text())['chapters'] if path.exists() else {}


def composition(cid: str, duration: float, body: str) -> str:
    css = CSS.replace('#ID', '#' + cid)
    return (f'<template><div id="{cid}" data-composition-id="{cid}" data-start="0" data-duration="{duration:.3f}" '
            f'data-width="1280" data-height="720"><style>{css}</style><div class="card">{body}</div>'
            '<div class="brand"><img src="assets/vub-seal.png" alt="">VUB Learning</div>'
            f'<script>const tl=gsap.timeline({{paused:true}});tl.fromTo("#{cid} .card",{{opacity:0}},{{opacity:1,duration:.3}},0);'
            f'window.__timelines["{cid}"]=tl;</script></div></template>')


def divider(cid: str, card: dict) -> str:
    mission = f'<p style="position:absolute;left:96px;top:470px;margin:0;font-size:36px;color:#E6C65C">Mission {E(card["mission"])}</p>' if card.get('mission') else ''
    body = ('<p class="label" style="top:190px">NEXT TOPIC</p><div class="rule" style="top:244px"></div>'
            f'<h1 style="position:absolute;left:96px;top:280px;margin:0;font-size:72px;line-height:1.1">{E(card["app"])}</h1>'
            f'<p style="position:absolute;left:96px;top:385px;margin:0;font-size:44px;max-width:1088px">{E(card["title"])}</p>{mission}')
    return composition(cid, DIVIDER_SECONDS, body)


def pause(cid: str, card: dict, duration: float) -> str:
    steps = ''.join(f'<li style="margin:0 0 18px;padding-left:12px">{E(step)}</li>' for step in card['try'])
    body = ('<svg style="position:absolute;left:96px;top:70px" width="96" height="96" viewBox="0 0 64 64" fill="none" stroke="#E6C65C" '
            'stroke-width="5" stroke-linecap="round"><circle cx="32" cy="32" r="27"/><path d="M25 20v24M39 20v24"/></svg>'
            '<h1 style="position:absolute;left:216px;top:78px;margin:0;font-size:64px;line-height:1.2">Pause the video</h1>'
            '<p class="label" style="top:206px">TRY THIS NOW</p>'
            f'<ol style="position:absolute;left:96px;top:256px;margin:0;padding-left:44px;width:1080px;font-size:38px;line-height:1.25">{steps}</ol>'
            '<div style="position:absolute;left:96px;right:96px;top:540px;height:72px;border-radius:10px;background:#E6C65C;color:#102c4b;'
            f'font-size:34px;font-weight:700;display:flex;align-items:center;padding:0 28px">Worksheet · {E(card["where"])}</div>')
    return composition(cid, duration, body)


def clips(week_dir: Path, n: int, beats: list, starts: list) -> list:
    """Write card compositions for one week and return their host clips for index.html."""
    cards = load(week_dir)
    out = []
    for i, (beat, start) in enumerate(zip(beats, starts)):
        card = cards.get(beat['id'], {})
        if 'divider' in card:
            cid = f'w{n}-divider-{i + 1}'
            (week_dir / f'compositions/frames/{cid}.html').write_text(divider(cid, card['divider']))
            out.append((cid, start, DIVIDER_SECONDS))
        if 'pause' in card:
            cid = f'w{n}-pause-{i + 1}'
            at = start + beat['leadIn'] + beat['audioDuration'] + PAUSE_DELAY
            duration = round(start + beat['window'] - at, 3)
            (week_dir / f'compositions/frames/{cid}.html').write_text(pause(cid, card['pause'], duration))
            out.append((cid, at, duration))
    return [f'<div class="clip" id="host-{cid}" data-composition-id="{cid}" data-composition-src="compositions/frames/{cid}.html" '
            f'data-start="{at:.3f}" data-duration="{duration:.3f}" data-track-index="2" style="position:absolute;inset:0;z-index:5"></div>'
            for cid, at, duration in out]
