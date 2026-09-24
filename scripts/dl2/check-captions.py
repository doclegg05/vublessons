"""Check caption quality for the DL2 videos: phrase-boundary cue breaks, line and
reading-rate limits, and (optionally) that the concatenated cue text still matches
the concatenated beat scripts.

Reads courses/digital-literacy-2/media/week-0*.vtt relative to the current working
directory. Exits 1 and prints every violation found; exits 0 when all files pass.

Usage:
  python3 scripts/dl2/check-captions.py
  python3 scripts/dl2/check-captions.py --script <video root>   # also diff vs SCRIPT.md
"""
from __future__ import annotations

import glob
import json
import pathlib
import re
import sys
from typing import TypedDict

FUNCTION_WORDS = {
    "a", "an", "the", "to", "of", "and", "or", "but", "for", "with", "in",
    "on", "at", "by", "from", "as", "that", "which", "who",
}
MAX_LINE_CHARS = 42
MAX_LINES = 2
MIN_DURATION = 0.7
MAX_DURATION = 7.0
MAX_CPS = 20.0
MAX_CPS_SHORT = 22.0
SHORT_CUE_SECONDS = 1.5
MIN_CLAUSE_END_SHARE = 0.60
MIN_WORDS_AFTER_TERMINATOR = 5

CUE_RE = re.compile(
    r"(\d{2}):(\d{2}):(\d{2})\.(\d{3}) --> (\d{2}):(\d{2}):(\d{2})\.(\d{3})[^\n]*\n"
    r"((?:(?!\n\n)[^\n]+\n?)+)"
)


class Cue(TypedDict):
    start: float
    end: float
    lines: list[str]
    text: str


def seconds(h: str, m: str, s: str, ms: str) -> float:
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000.0


def bare(word: str) -> str:
    return re.sub(r"^[^A-Za-z0-9]+|[^A-Za-z0-9]+$", "", word).lower()


def parse_vtt(text: str) -> list[Cue]:
    body = text.split("WEBVTT", 1)[-1]
    cues: list[Cue] = []
    for m in CUE_RE.finditer(body):
        h1, m1, s1, ms1, h2, m2, s2, ms2, raw_text = m.groups()
        start = seconds(h1, m1, s1, ms1)
        end = seconds(h2, m2, s2, ms2)
        lines = [ln for ln in raw_text.splitlines() if ln.strip()]
        cues.append(Cue(start=start, end=end, lines=lines, text=" ".join(lines)))
    return cues


def ends_on_function_word(text: str) -> bool:
    """A cue ending on a bare function word is a dangling mid-clause cut.
    A cue ending on one with its own sentence-final punctuation (an English
    phrasal verb or a sentence that trails off on a pronoun, e.g. "act on."
    or "responsible for.") is a complete sentence, not a dangling cut."""
    words = text.split()
    if not words:
        return False
    if words[-1][-1:] in ".!?":
        return False
    return bare(words[-1]) in FUNCTION_WORDS


def has_dangling_sentence_start(text: str) -> bool:
    """True when the cue holds a sentence terminator followed by fewer than
    MIN_WORDS_AFTER_TERMINATOR more words (a dangling start of the next
    sentence, e.g. '...to reverse. When')."""
    words = text.split()
    for i, w in enumerate(words[:-1]):
        if w[-1:] in ".!?":
            remaining = len(words) - (i + 1)
            if 0 < remaining < MIN_WORDS_AFTER_TERMINATOR:
                return True
    return False


def check_file(path: str) -> tuple[list[str], list[str], list[Cue]]:
    with open(path, encoding="utf-8") as f:
        text = f.read()
    violations: list[str] = []
    warnings: list[str] = []  # pace-bound limits the grouping cannot change
    if not text.startswith("WEBVTT"):
        violations.append(f"{path}: missing WEBVTT header")
    cues = parse_vtt(text)
    if not cues:
        violations.append(f"{path}: no cues found")
        return violations, cues

    clause_enders = 0
    for i, cue in enumerate(cues, start=1):
        tag = f"{path} cue {i} ({cue['start']:.3f}-{cue['end']:.3f})"
        if len(cue["lines"]) > MAX_LINES:
            violations.append(f"{tag}: {len(cue['lines'])} lines (max {MAX_LINES}): {cue['text']!r}")
        for line in cue["lines"]:
            if len(line) > MAX_LINE_CHARS:
                violations.append(f"{tag}: line over {MAX_LINE_CHARS} chars ({len(line)}): {line!r}")

        duration = cue["end"] - cue["start"]
        if duration < MIN_DURATION:
            warnings.append(f"{tag}: duration {duration:.3f}s below {MIN_DURATION}s")
        if duration > MAX_DURATION:
            warnings.append(f"{tag}: duration {duration:.3f}s above {MAX_DURATION}s")

        cps = len(cue["text"]) / duration if duration > 0 else float("inf")
        cps_limit = MAX_CPS_SHORT if duration < SHORT_CUE_SECONDS else MAX_CPS
        if cps > cps_limit:
            warnings.append(f"{tag}: reading rate {cps:.1f} cps above {cps_limit} cps: {cue['text']!r}")

        if ends_on_function_word(cue["text"]):
            violations.append(f"{tag}: ends on a function word/article: {cue['text']!r}")

        if has_dangling_sentence_start(cue["text"]):
            violations.append(f"{tag}: dangling start of next sentence: {cue['text']!r}")

        if cue["text"] and cue["text"][-1] in ".?!,;:":
            clause_enders += 1

    share = clause_enders / len(cues) if cues else 0.0
    print(f"{path}: {len(cues)} cues, {clause_enders} end mid-clause/sentence ({share:.1%})")
    if share < MIN_CLAUSE_END_SHARE:
        violations.append(
            f"{path}: only {share:.1%} of cues end on a clause boundary "
            f"(period, question mark, exclamation point, comma, semicolon, colon), "
            f"needs at least {MIN_CLAUSE_END_SHARE:.0%}"
        )
    return violations, warnings, cues


def check_against_script(path: str, cues: list[Cue], video_root: pathlib.Path) -> list[str]:
    beats_path = video_root / "narration" / "beats.json"
    if not beats_path.exists():
        return [f"{path}: no beats.json found at {beats_path} for --script check"]
    beats = json.loads(beats_path.read_text())
    expected = " ".join(" ".join(b["text"] for b in beats).split())
    actual = " ".join(" ".join(c["text"] for c in cues).split())
    if expected != actual:
        return [f"{path}: concatenated cue text differs from beats.json text"]
    return []


def main() -> int:
    args = sys.argv[1:]
    script_root: str | None = None
    if "--script" in args:
        idx = args.index("--script")
        script_root = args[idx + 1]
        args = args[:idx] + args[idx + 2:]

    paths = sorted(glob.glob("courses/digital-literacy-2/media/week-0*.vtt"))
    if not paths:
        print("No caption files found at courses/digital-literacy-2/media/week-0*.vtt")
        return 1

    strict = "--strict" in args
    all_violations: list[str] = []
    all_warnings: list[str] = []
    for path in paths:
        violations, warnings, cues = check_file(path)
        all_violations.extend(violations)
        all_warnings.extend(warnings)
        if script_root:
            week = re.search(r"week-(\d+)", path)
            assert week is not None
            video_root = pathlib.Path(script_root) / f"week-{week.group(1)}"
            all_violations.extend(check_against_script(path, cues, video_root))

    if all_warnings:
        print(f"\n{len(all_warnings)} pace warning(s) (narration speed; fatal only with --strict):")
        for w in all_warnings:
            print(f"  - {w}")
        if strict:
            all_violations.extend(all_warnings)
    if all_violations:
        print(f"\n{len(all_violations)} violation(s):")
        for v in all_violations:
            print(f"  - {v}")
        return 1

    print("\nAll caption files pass.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
