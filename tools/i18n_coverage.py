# -*- coding: utf-8 -*-
"""
보고서 번역 커버리지 실측
=========================
사전에 키가 몇 개 들었는지는 진척이 아니다. **실제로 생성된 보고서에
한글이 몇 자 남는가**가 진척이다. 쓰지도 않는 키를 1000개 넣어도 화면은
한국어 그대로일 수 있고, 반대로 키 하나가 수십 곳을 덮기도 한다.

그래서 진짜 보고서 HTML 을 번역기에 통과시킨 뒤, **눈에 보이는 자리에
남은 한글**을 센다. 태그 안(class/id/CSS/JS)은 세지 않는다 — 거긴
번역 대상이 아니다.

사용::

    python -m engine.jiqtx.cli --demo      # 보고서 먼저 생성
    python tools/i18n_coverage.py <보고서.html> en
    python tools/i18n_coverage.py <폴더> en --top 40
"""
from __future__ import annotations

import argparse
import io
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from engine.jiqtx import i18n            # noqa: E402

HANGUL = re.compile(r"[가-힣]")
# 남은 한글 덩어리 — 조사·공백까지 붙여 하나로 본다.
RUN = re.compile(r"[가-힣][가-힣0-9A-Za-z·%\s\-—/().,]*[가-힣]|[가-힣]")


def visible_text(html: str) -> str:
    """태그 밖 텍스트 + 보이는 속성만 이어 붙인다."""
    out = []
    for part in i18n._CHUNK.split(html):
        if not part:
            continue
        low = part[:7].lower()
        if low.startswith("<style") or low.startswith("<script"):
            continue
        if part.startswith("<"):
            for m in i18n._ATTR_RE.finditer(part):
                out.append(m.group(3))
            continue
        out.append(part)
    return "\n".join(out)


def analyse(paths: list[Path], lang: str, top: int):
    total_before = total_after = 0
    leftovers: Counter[str] = Counter()

    for p in paths:
        html = io.open(p, encoding="utf-8").read()
        before = visible_text(html)
        after = visible_text(i18n.translate_html(html, lang))
        total_before += len(HANGUL.findall(before))
        total_after += len(HANGUL.findall(after))
        for m in RUN.findall(after):
            s = m.strip()
            if s:
                leftovers[s] += 1

    done = total_before - total_after
    pct = (done / total_before * 100) if total_before else 100.0
    print("보고서 %d개 · 언어 %s" % (len(paths), lang))
    print("한글 글자 %d자 → %d자 남음   커버리지 %.1f%%"
          % (total_before, total_after, pct))
    if top and leftovers:
        print("\n남은 것 상위 %d (등장횟수 · 조각)" % top)
        for s, n in leftovers.most_common(top):
            print("%5d  %r" % (n, s[:88]))
    return pct


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("target", help="보고서 .html 또는 폴더")
    ap.add_argument("lang")
    ap.add_argument("--top", type=int, default=25)
    a = ap.parse_args()

    t = Path(a.target)
    paths = sorted(t.glob("*.html")) if t.is_dir() else [t]
    if not paths:
        print("보고서를 못 찾았다:", t)
        return 1
    analyse(paths, a.lang, a.top)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
