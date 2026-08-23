# -*- coding: utf-8 -*-
"""
남은 번역을 모듈별로 본다.

순위(등장횟수 × 길이) 방식은 초반에 커버리지를 빠르게 올리지만, 뒤로 갈수록
한 배치가 1%도 못 올린다. 그때부터는 **모듈을 하나씩 끝내는** 편이 낫다 —
100% 를 보장하고, 같은 맥락의 문장을 몰아서 옮기니 번역 품질도 붙는다.

사용::

    python tools/i18n_todo.py en                    # 모듈별 남은 개수
    python tools/i18n_todo.py en dynamic_report     # 그 모듈의 남은 키
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from engine.jiqtx import i18n              # noqa: E402
from tools.i18n_extract import extract     # noqa: E402


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    lang = sys.argv[1]
    want = sys.argv[2] if len(sys.argv) > 2 else None

    cat = i18n.catalog(lang)
    per = extract()

    if want:
        for mod, keys in per.items():
            if want not in mod:
                continue
            miss = [k for k in keys if k not in cat]
            print("# %s — 남은 %d개" % (mod, len(miss)))
            for k in miss:
                print("    %r: %r," % (k, ""))
        return 0

    rows = []
    for mod, keys in per.items():
        miss = sum(1 for k in keys if k not in cat)
        if miss:
            rows.append((miss, len(keys), mod))
    rows.sort(reverse=True)
    print("# %s — 남은 총 %d개" % (lang, sum(r[0] for r in rows)))
    for miss, total, mod in rows:
        print("%5d / %-5d  %s" % (miss, total, mod))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
