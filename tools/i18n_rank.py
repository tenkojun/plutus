# -*- coding: utf-8 -*-
"""
번역 우선순위 — 실제 보고서에서 글자수를 가장 많이 줄이는 키부터
================================================================
추출된 키 2,150개를 아무 순서로 옮기면, 절반을 끝내도 화면은 여전히
한국어처럼 보일 수 있다. 짧은 라벨 1,000개보다 자주 쓰이는 긴 문장
100개가 훨씬 크게 줄인다.

그래서 실제 생성된 보고서에서 **키가 몇 번 등장하는가 × 길이**로 줄을
세운다. 이 순서대로 옮기면 커버리지가 가장 빨리 오른다.

사용::

    python tools/i18n_rank.py <보고서폴더> --lang en --limit 200
    python tools/i18n_rank.py <보고서폴더> --lang en --module dynamic_report
    python tools/i18n_rank.py <보고서폴더> --lang en --stub --limit 200
"""
from __future__ import annotations

import argparse
import io
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from engine.jiqtx import i18n                       # noqa: E402
from tools.i18n_extract import extract              # noqa: E402
from tools.i18n_coverage import visible_text        # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("reports", help="보고서 .html 폴더")
    ap.add_argument("--lang", default="en")
    ap.add_argument("--limit", type=int, default=150)
    ap.add_argument("--module", help="이 모듈의 키만")
    ap.add_argument("--stub", action="store_true", help="붙여 넣을 초안")
    a = ap.parse_args()

    per = extract()
    if a.module:
        per = {k: v for k, v in per.items() if a.module in k}
        if not per:
            print("그런 모듈이 없다:", a.module)
            return 1
    keys: list[str] = []
    for ks in per.values():
        for k in ks:
            if k not in keys:
                keys.append(k)

    d = Path(a.reports)
    paths = sorted(d.glob("*.html")) if d.is_dir() else [d]
    blob = "\n".join(visible_text(io.open(p, encoding="utf-8").read())
                     for p in paths)

    cat = i18n.catalog(a.lang)
    rows = []
    for k in keys:
        if k in cat:
            continue
        n = blob.count(k)
        if n == 0:
            continue
        rows.append((n * len(k.strip()), n, k))
    rows.sort(reverse=True)

    if a.stub:
        for _, _, k in rows[:a.limit]:
            print("    %r: %r," % (k, ""))
        return 0

    unused = sum(1 for k in keys if k not in cat and blob.count(k) == 0)
    print("# 미번역 %d개 중 이 보고서에 실제로 등장 %d개 (미등장 %d)"
          % (len(keys) - len(cat), len(rows), unused))
    print("# 상위 %d개가 덮는 글자수 %d자\n"
          % (min(a.limit, len(rows)), sum(r[0] for r in rows[:a.limit])))
    for impact, n, k in rows[:a.limit]:
        print("%7d  x%-3d  %r" % (impact, n, k[:78]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
