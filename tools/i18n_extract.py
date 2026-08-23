# -*- coding: utf-8 -*-
"""
보고서 엔진의 번역 대상 문자열 추출
===================================
`engine/jiqtx/` 를 AST 로 훑어 **화면에 나가는 한글 조각**을 모은다.

왜 AST 인가
-----------
보고서는 f-string 으로 HTML 을 조립한다::

    f'<div class="cs2">확률 {v.direction_prob:.1%} · '

여기서 실제로 출력에 그대로 실리는 한글은 ``'확률 '`` 하나다. 정규식으로
줄을 긁으면 포맷 자리(``{...}``)까지 키에 들어가 영원히 매칭되지 않는다.
AST 는 f-string 을 JoinedStr 로 주고 그 안의 Constant 만 꺼낼 수 있다 —
즉 **런타임 출력에 리터럴로 나타나는 조각과 정확히 일치**한다.

HTML 조각은 쪼갠다
------------------
리터럴이 통째로 HTML 인 경우가 많다::

    '<p class="muted">데이터 없음</p>'

이걸 그대로 키로 쓰면 **영원히 매칭되지 않는다.** 렌더된 문서에서
번역기가 보는 것은 태그가 아니라 태그 사이의 텍스트(``데이터 없음``)
뿐이기 때문이다. 그래서 태그를 걷어내고 안의 텍스트와 보이는 속성값만
키로 삼는다 — i18n.translate_html 이 실제로 훑는 것과 같은 단위다.

제외하는 것
-----------
- docstring : 화면에 안 나간다
- 주석      : AST 에 없다
- CSS/JS 덩어리 : 한글이 주석으로만 들어 있고 통째로 크다 (길이로 걸러냄)

사용::

    python tools/i18n_extract.py                # 요약
    python tools/i18n_extract.py --list         # 키 전부
    python tools/i18n_extract.py --missing en   # 아직 번역 안 된 키
    python tools/i18n_extract.py --stub ja      # 붙여 넣을 수 있는 초안
"""
from __future__ import annotations

import argparse
import ast
import io
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
ENGINE = ROOT / "engine" / "jiqtx"

HANGUL = re.compile(r"[가-힣]")

# 이보다 긴 리터럴은 CSS·JS·HTML 템플릿 덩어리다. 한글이 들어 있어도
# 그건 그 안의 주석이지 화면 문구가 아니다.
MAX_LEN = 400

# 번역하지 않는 모듈 — 화면에 안 나가거나(CLI·검증) 개발자용이다.
# i18n.py 자신은 제외한다 — docstring 예시로 든 한글이 잡힌다.
SKIP_MODULES = {"cli.py", "_validate.py", "_demo.py", "replay.py",
                "i18n.py"}


def _docstring_ids(tree: ast.AST) -> set[int]:
    out: set[int] = set()
    for node in ast.walk(tree):
        if not isinstance(node, (ast.Module, ast.FunctionDef,
                                 ast.AsyncFunctionDef, ast.ClassDef)):
            continue
        body = getattr(node, "body", None)
        if (body and isinstance(body[0], ast.Expr)
                and isinstance(body[0].value, ast.Constant)
                and isinstance(body[0].value.value, str)):
            out.add(id(body[0].value))
    return out


def _pieces(v: str) -> list[str]:
    """리터럴 하나에서 실제로 화면에 나가는 조각들을 뽑는다.

    HTML 이 아니면 그 자체가 조각 하나다. HTML 이면 태그를 빼고 텍스트와
    보이는 속성값만 남긴다.
    """
    if "<" not in v or ">" not in v:
        return [v]
    from engine.jiqtx import i18n
    out: list[str] = []
    for part in i18n._CHUNK.split(v):
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
    return [p for p in out if HANGUL.search(p)]


def extract() -> dict[str, list[str]]:
    """{모듈 경로: [한글 조각, ...]} — 등장 순서를 지킨다."""
    found: dict[str, list[str]] = {}
    for path in sorted(ENGINE.rglob("*.py")):
        if path.name in SKIP_MODULES:
            continue
        # 사전 자신은 훑지 않는다. locale/ 아래는 번역문이지 소스가 아니다 —
        # 넣으면 자기 키를 자기가 다시 발견하는 순환이 된다.
        if "locale" in path.parts:
            continue
        src = io.open(path, encoding="utf-8").read()
        try:
            tree = ast.parse(src)
        except SyntaxError:
            continue
        skip = _docstring_ids(tree)
        keys: list[str] = []
        for node in ast.walk(tree):
            if not isinstance(node, ast.Constant):
                continue
            if not isinstance(node.value, str) or id(node) in skip:
                continue
            v = node.value
            if not HANGUL.search(v) or len(v) > MAX_LEN:
                continue
            for piece in _pieces(v):
                if piece not in keys:
                    keys.append(piece)
        if keys:
            found[path.relative_to(ROOT).as_posix()] = keys
    return found


def all_keys() -> list[str]:
    seen: list[str] = []
    known: set[str] = set()
    for keys in extract().values():
        for k in keys:
            if k not in known:
                known.add(k)
                seen.append(k)
    return seen


def _catalog(lang: str) -> dict[str, str]:
    sys.path.insert(0, str(ROOT))
    from engine.jiqtx import i18n           # noqa: E402
    return i18n.catalog(lang)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true", help="키 전부 출력")
    ap.add_argument("--missing", metavar="LANG", help="번역 안 된 키")
    ap.add_argument("--stub", metavar="LANG", help="붙여 넣을 초안")
    ap.add_argument("--by-module", action="store_true")
    args = ap.parse_args()

    per = extract()
    keys = all_keys()

    if args.by_module:
        for mod, ks in sorted(per.items(), key=lambda x: -len(x[1])):
            print("%5d  %s" % (len(ks), mod))
        return 0

    if args.list:
        for k in keys:
            print(repr(k))
        return 0

    if args.missing or args.stub:
        lang = args.missing or args.stub
        cat = _catalog(lang)
        miss = [k for k in keys if k not in cat]
        if args.missing:
            print("# %s: 전체 %d · 번역 %d · 미번역 %d"
                  % (lang, len(keys), len(keys) - len(miss), len(miss)))
            for k in miss:
                print(repr(k))
            return 0
        for k in miss:
            print("    %r: %r," % (k, ""))
        return 0

    print("모듈 %d개 · 번역 대상 한글 조각 %d개 (고유)"
          % (len(per), len(keys)))
    print("총 %d자" % sum(len(k) for k in keys))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
