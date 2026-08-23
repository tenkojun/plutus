# -*- coding: utf-8 -*-
"""
사전 파트를 __init__ 에 등록하고 정합성을 확인한다.

배치를 하나 쓸 때마다 손으로 import 두 줄을 고치면 반드시 빠뜨린다.
등록 + 중복 검사 + 오타(소스에 없는 키) 검사 + 커버리지를 한 번에 돌린다.

사용::

    python tools/i18n_register.py en _macro macro
"""
from __future__ import annotations

import io
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))


def _dirname(lang: str) -> str:
    """언어 코드 → 디렉터리 이름. i18n.catalog() 와 같은 규칙이다."""
    return lang.replace("-", "_").lower()


def register(lang: str, module: str, name: str) -> None:
    init = (ROOT / "engine" / "jiqtx" / "locale"
            / _dirname(lang) / "__init__.py")
    s = io.open(init, encoding="utf-8").read()
    var = "_" + name.upper()
    if var in s:
        print("이미 등록됨:", name)
        return
    # 마지막 import 뒤에 붙인다. 첫 파트면 PARTS 선언 앞에 넣는다.
    lines = s.split("\n")
    idx = [i for i, l in enumerate(lines) if l.startswith("from .")]
    at = (max(idx) + 1 if idx
          else next(i for i, l in enumerate(lines) if l.startswith("PARTS")))
    lines.insert(at, "from .%s import CATALOG as %s" % (module, var))
    s = "\n".join(lines)
    s = s.replace("}\n\nCATALOG", '    "%s": %s,\n}\n\nCATALOG'
                  % (name, var), 1)
    io.open(init, "w", encoding="utf-8").write(s)
    print("등록:", name)


def verify(lang: str) -> int:
    from tools.i18n_extract import all_keys
    pkg = __import__("engine.jiqtx.locale.%s" % _dirname(lang),
                     fromlist=["CATALOG", "PARTS"])
    seen: dict[str, str] = {}
    dupes = 0
    for pname, part in pkg.PARTS.items():
        for k in part:
            if k in seen:
                dupes += 1
                print("  중복 %r  (%s ↔ %s)" % (k[:46], seen[k], pname))
            seen[k] = pname
    src = set(all_keys())
    stray = [k for k in pkg.CATALOG if k not in src]
    print("총 %d개 · 중복 %d · 소스에 없는 키 %d"
          % (len(pkg.CATALOG), dupes, len(stray)))
    for k in stray[:8]:
        print("  오타? %r" % (k[:60],))
    return dupes + len(stray)


def main() -> int:
    if len(sys.argv) == 2:
        return 1 if verify(sys.argv[1]) else 0
    if len(sys.argv) != 4:
        print(__doc__)
        return 2
    lang, module, name = sys.argv[1:4]
    register(lang, module, name)
    return 1 if verify(lang) else 0


if __name__ == "__main__":
    raise SystemExit(main())
