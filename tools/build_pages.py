# -*- coding: utf-8 -*-
"""
GitHub Pages 사이트 조립
========================
README 를 **단일 소스로 둔다.** 사이트용으로 같은 내용을 한 벌 더 두면
반드시 한쪽만 고쳐지고, 어느 쪽이 최신인지 아무도 모르게 된다.

그래서 저장소에는 템플릿(`site/`)만 커밋하고, 페이지 본문은 빌드할 때
README 에서 조립한다. 생성물은 커밋하지 않는다(.gitignore).

    README.md            → /            (한국어 · 기본)
    docs/README.en.md    → /en/
    docs/README.ja.md    → /ja/
    docs/README.zh-CN.md → /zh-cn/

조립하면서 고치는 것
--------------------
- 이미지 경로. README 는 저장소 기준(`webapp/static/…`), 사이트는
  루트 기준(`/assets/…`)이다.
- 저장소 안 파일로 가는 링크(`CHANGELOG.md`, `engine/paths.py` …).
  사이트에는 그 파일이 없으므로 GitHub 로 보낸다.
- 문서 맨 위의 언어 전환줄. 사이트는 레이아웃이 스위처를 그리므로 뺀다.

사용::

    python tools/build_pages.py
"""
from __future__ import annotations

import argparse
import io
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
REPO = "https://github.com/tenkojun/plutus"
BLOB = REPO + "/blob/main/"

# 언어별: 소스 · 출력 · <html lang> · 제목 · 설명(검색결과에 그대로 뜬다)
PAGES = [
    {
        "src": "README.md",
        "out": "index.md",
        "lang": "ko",
        "code": "ko",
        "permalink": "/",
        "title": "Plutus — 기관급 퀀트 분석 터미널",
        "desc": "종목 하나로 데이터 무결성부터 유동성·변동성·레짐·팩터·"
                "리스크까지 훑고, 전문가 패널 14인의 심의를 거쳐 외부 리소스 "
                "0개의 자기완결 HTML 보고서를 만드는 오픈소스 퀀트 분석 "
                "터미널. Python · MIT.",
    },
    {
        "src": "docs/README.en.md",
        "out": "en/index.md",
        "lang": "en",
        "code": "en",
        "permalink": "/en/",
        "title": "Plutus — Institutional-Grade Quant Research Terminal",
        "desc": "Open-source quant research terminal. One ticker in; data "
                "integrity, liquidity, volatility, regime, factors and risk "
                "out — reviewed by a 14-member expert panel and written to a "
                "self-contained HTML report with zero external resources. "
                "Python, MIT.",
    },
    {
        "src": "docs/README.ja.md",
        "out": "ja/index.md",
        "lang": "ja",
        "code": "ja",
        "permalink": "/ja/",
        "title": "Plutus — 機関級クオンツ分析ターミナル",
        "desc": "オープンソースのクオンツ分析ターミナル。銘柄を一つ入れると"
                "データ健全性から流動性・ボラティリティ・レジーム・ファクター"
                "・リスクまでを通し、14 名の専門家パネルの審議を経て外部"
                "リソース 0 個の自己完結 HTML レポートを生成する。Python・MIT。",
    },
    {
        "src": "docs/README.zh-CN.md",
        "out": "zh-cn/index.md",
        "lang": "zh-CN",
        "code": "zh-cn",
        "permalink": "/zh-cn/",
        "title": "Plutus — 机构级量化分析终端",
        "desc": "开源量化分析终端。输入一个标的，从数据完整性一路走过流动性、"
                "波动率、状态识别、因子与风险，经 14 位专家小组审议，产出一份"
                "零外部资源的自包含 HTML 报告。Python，MIT 许可。",
    },
]

# 사이트로 복사할 이미지. README 가 참조하는 것들이다.
ASSETS = [
    "webapp/static/plutus_mark.png",
    "webapp/static/plutus_mark_light.png",
]

# 저장소 안 파일로 가는 링크 — 사이트에는 없으니 GitHub 로 보낸다.
_REPO_LINK = re.compile(
    r"\]\((?!https?://|#|/)"          # 외부·앵커·절대경로는 그대로 둔다
    r"((?:\.\./)*[A-Za-z0-9_./-]+"
    r"\.(?:md|py|iss|toml|txt|yml|yaml|bat|ps1))\)")


def _strip_lang_bar(md: str) -> str:
    """맨 위 언어 전환줄을 뺀다 — 레이아웃이 스위처를 그린다."""
    return "\n".join(
        l for l in md.split("\n")
        if not ("한국어" in l and "简体中文" in l and "日本語" in l))


def _fix_assets(md: str) -> str:
    md = md.replace("../webapp/static/", "/assets/")
    return md.replace("webapp/static/", "/assets/")


def _fix_repo_links(md: str) -> str:
    def repl(m):
        target = m.group(1)
        while target.startswith("../"):
            target = target[3:]
        return "](%s%s)" % (BLOB, target.lstrip("./"))
    return _REPO_LINK.sub(repl, md)


def _front_matter(page: dict) -> str:
    def q(s):
        return '"' + s.replace('"', '\\"') + '"'
    return "\n".join([
        "---",
        "layout: page",
        "title: " + q(page["title"]),
        "description: " + q(page["desc"]),
        "lang: " + page["lang"],
        "code: " + page["code"],
        "permalink: " + page["permalink"],
        "---",
        "",
    ])


def build() -> list[tuple[str, int]]:
    made = []
    for page in PAGES:
        md = io.open(ROOT / page["src"], encoding="utf-8").read()
        md = _fix_repo_links(_fix_assets(_strip_lang_bar(md)))
        dst = SITE / page["out"]
        dst.parent.mkdir(parents=True, exist_ok=True)
        io.open(dst, "w", encoding="utf-8").write(_front_matter(page) + md)
        made.append((page["out"], len(md)))

    assets = SITE / "assets"
    assets.mkdir(parents=True, exist_ok=True)
    for rel in ASSETS:
        shutil.copy2(ROOT / rel, assets / Path(rel).name)
    return made


def main() -> int:
    argparse.ArgumentParser().parse_args()
    if not (SITE / "_config.yml").exists():
        print("site/_config.yml 이 없다 — 템플릿이 있어야 조립할 수 있다.")
        return 1

    made = build()
    for name, size in made:
        print("%-16s %6d자" % (name, size))
    print("assets  %d개" % len(ASSETS))

    # 상대경로가 남아 있으면 사이트에서 404 가 된다. 조용히 깨지는 종류라
    # 빌드에서 막는다.
    bad = []
    for name, _ in made:
        text = io.open(SITE / name, encoding="utf-8").read()
        bad += [(name, m.group(1)) for m in _REPO_LINK.finditer(text)]
    if bad:
        print("\n남은 저장소 상대링크:")
        for n, t in bad[:10]:
            print("  %s → %s" % (n, t))
        return 1
    print("남은 저장소 상대링크 없음")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
