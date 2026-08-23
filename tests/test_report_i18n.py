# -*- coding: utf-8 -*-
"""
보고서 번역 검사
================
조각 치환은 조용히 틀리는 방식이 여럿이다. 여기서 보는 것은 그 방식들이다.

1. **사전이 저장소에 없다.** 실제로 겪었다 — `.gitignore` 의 `_*.py` 가
   사전 파트를 전부 먹어서, 작업 트리는 깨끗한데 저장소에는 사전이 하나도
   없었다. `catalog()` 는 예외를 삼키고 빈 사전을 돌려주므로 보고서가
   그냥 한국어로 나올 뿐 아무도 모른다.
2. **문장 파괴.** 경계 규칙이 빠지면 '생존편향' 이 "생존편향된" 안에서
   터진다.
3. **한국어 무동작 깨짐.** lang='ko' 는 바이트 하나도 바꾸면 안 된다.
4. **중복 키.** 파트가 여럿이라 나중 것이 앞의 것을 조용히 덮는다.
5. **오타 키.** 소스에 없는 키는 영원히 안 쓰인다.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from engine.jiqtx import i18n                      # noqa: E402
from tools.i18n_extract import all_keys            # noqa: E402

LANGS = ("en", "ja", "zh-CN")


def _tracked(rel: str) -> bool:
    """git 이 이 경로를 추적하는가."""
    r = subprocess.run(["git", "ls-files", "--error-unmatch", rel],
                       cwd=ROOT, capture_output=True, text=True)
    return r.returncode == 0


def test_catalog_files_are_committed():
    """사전 파일이 저장소에 실제로 들어 있는가.

    .gitignore 의 `_*.py` 규칙이 사전 파트를 통째로 먹은 적이 있다.
    디스크에는 있고 저장소에는 없으면, 클론한 쪽에서는 번역이 통째로
    사라지는데 예외조차 나지 않는다.
    """
    locale = ROOT / "engine" / "jiqtx" / "locale"
    missing = []
    for p in sorted(locale.rglob("*.py")):
        if "__pycache__" in p.parts:
            continue
        rel = p.relative_to(ROOT).as_posix()
        if not _tracked(rel):
            missing.append(rel)
    assert not missing, (
        "사전 파일이 git 에 없다 (.gitignore 확인): %s" % missing)


def test_korean_is_byte_identical():
    """lang='ko' 는 완전한 무동작이어야 한다."""
    html = ('<style>.a{}</style><p class="x">판정 근거</p>'
            '<b data-tip="생존편향">확률 47%</b>')
    assert i18n.translate_html(html, "ko") == html
    assert i18n.t("아무 문장", "ko") == "아무 문장"


def test_boundary_rule_does_not_shred_sentences():
    """앞뒤가 한글이면 치환하지 않는다."""
    i18n._CATALOGS["xx"] = {"생존편향": "survivorship bias", "일": "day"}
    i18n._PATTERNS.pop("xx", None)
    try:
        # 뒤에 한글이 붙으면 건드리지 않는다
        assert i18n.t("생존편향된 데이터", "xx") == "생존편향된 데이터"
        assert i18n.t("일간 변동성", "xx") == "일간 변동성"
        # 경계가 맞으면 번역한다
        assert i18n.t("생존편향 문제", "xx") == "survivorship bias 문제"
    finally:
        i18n._CATALOGS.pop("xx", None)
        i18n._PATTERNS.pop("xx", None)


def test_tags_and_code_are_untouched():
    """class/id/CSS/JS 를 건드리면 보고서가 깨진다."""
    i18n._CATALOGS["xx"] = {"판정": "verdict"}
    i18n._PATTERNS.pop("xx", None)
    try:
        out = i18n.translate_html(
            '<style>/* 판정 */</style>'
            '<div class="판정-x" id="판정">판정</div>'
            '<script>var s="판정";</script>', "xx")
        assert "<style>/* 판정 */</style>" in out
        assert 'class="판정-x" id="판정"' in out      # 속성은 그대로
        assert ">verdict<" in out                      # 텍스트만 번역
        assert 'var s="판정"' in out
    finally:
        i18n._CATALOGS.pop("xx", None)
        i18n._PATTERNS.pop("xx", None)


@pytest.mark.parametrize("lang", LANGS)
def test_no_duplicate_keys_between_parts(lang):
    """파트가 여럿이라 나중 것이 앞의 것을 조용히 덮는다."""
    try:
        pkg = __import__("engine.jiqtx.locale.%s" % lang.replace("-", "_"),
                         fromlist=["PARTS"])
    except ImportError:
        pytest.skip("%s 사전 없음" % lang)
    seen: dict[str, str] = {}
    dupes = []
    for pname, part in pkg.PARTS.items():
        for k in part:
            if k in seen:
                dupes.append((k, seen[k], pname))
            seen[k] = pname
    assert not dupes, "중복 키: %s" % dupes[:5]


@pytest.mark.parametrize("lang", LANGS)
def test_every_key_exists_in_the_source(lang):
    """소스에 없는 키는 오타다 — 영원히 안 쓰인다."""
    cat = i18n.catalog(lang)
    if not cat:
        pytest.skip("%s 사전 없음" % lang)
    src = set(all_keys())
    stray = sorted(k for k in cat if k not in src)
    assert not stray, "소스에 없는 키 %d개: %s" % (len(stray), stray[:5])


@pytest.mark.parametrize("lang", LANGS)
def test_no_hangul_left_in_translations(lang):
    """번역값에 한글이 남아 있으면 그 항목은 번역이 안 된 것이다."""
    import re
    cat = i18n.catalog(lang)
    if not cat:
        pytest.skip("%s 사전 없음" % lang)
    hangul = re.compile(r"[가-힣]")
    bad = [(k, v) for k, v in cat.items() if hangul.search(v)]
    assert not bad, "한글이 남은 항목 %d개: %s" % (len(bad), bad[:3])


def test_render_html_accepts_lang():
    """진입점에 lang 이 실제로 달려 있는가."""
    import inspect
    from engine.jiqtx import dynamic_report, simple_report, portfolio_report
    from engine.jiqtx import report as md_report
    for fn in (dynamic_report.render_html, dynamic_report.save_html,
               simple_report.render_simple, simple_report.save_simple,
               portfolio_report.render_portfolio,
               portfolio_report.save_portfolio,
               md_report.render, md_report.save):
        sig = inspect.signature(fn)
        assert "lang" in sig.parameters, "%s 에 lang 이 없다" % fn.__name__
        assert sig.parameters["lang"].default == "ko", (
            "%s 의 lang 기본값이 'ko' 가 아니다 — 기존 호출이 바뀐다"
            % fn.__name__)
