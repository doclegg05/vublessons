"""Building blocks shared by the Mission Control week modules (week2.py, week3.py and later weeks).

A week module returns plain dicts; build.py renders them into the deck, worksheet, answer key and plans.
"""
from html import escape as e


def mission(title: str, app: str, start: str, finish: str, tell: list, show: list, do: list, question: str,
            choices: list, answer: int, why: str, lab: list, practice: int | None, rounds: tuple = (),
            links: tuple = ()) -> dict:
    """links are (label, url) pairs to real pages learners open, such as the Week 6 app versions."""
    return dict(title=title, app=app, start=start, finish=finish, tell=tell, show=show, do=do, question=question,
                choices=choices, answer=answer, why=why, lab=lab, practice=practice, rounds=list(rounds), links=list(links))


def rnd(title: str, app: str, steps: list, early: str, notes: str, paper: str = '', tasks: tuple = (), key: tuple = (),
        practice: int | None = None, links: tuple = ()) -> dict:
    """One extra hands-on round: a Do slide, matching worksheet tasks and answer-key lines.

    practice names a practice-library exercise that gets its own page for this round (practice_pages weeks only).
    links are (label, url) pairs to real pages the round uses.
    """
    assert not paper or app.startswith('Worksheet'), f'{title}: its material is printed on the worksheet, so the label must start with Worksheet'
    return dict(title=title, app=app, steps=list(steps), early=early, notes=notes, paper=paper, tasks=list(tasks), key=list(key),
                practice=practice, links=list(links))


def table(head: list, rows: list) -> str:
    """Small printable table for worksheet material. Cells are escaped."""
    th = ''.join(f'<th scope="col">{e(h)}</th>' for h in head)
    body = ''.join('<tr>' + ''.join(f'<td>{e(c)}</td>' for c in row) + '</tr>' for row in rows)
    return f'<div class="table-scroll" tabindex="0" role="region" aria-label="Practice material"><table><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>'


def quote(heading: str, text: str) -> str:
    """A printed sample (fictional page, draft or message) shown on the worksheet."""
    return f'<h3>{e(heading)}</h3><blockquote>{e(text)}</blockquote>'
