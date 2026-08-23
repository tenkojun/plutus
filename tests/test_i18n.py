# -*- coding: utf-8 -*-
"""
화면 언어(i18n.js) 검사
=======================
번역은 한국어 원문을 키로 쓰는 런타임 치환이다. 그래서 조용히 깨지는
방식이 둘 있다.

1. **키 오타** — 사전에 있는데 화면 문자열과 한 글자라도 다르면 아무 일도
   일어나지 않는다. 예외도 안 나고 그냥 한국어로 남는다.
2. **언어별 누락** — 영어만 넣고 일본어를 빠뜨리면 일본어 사용자에게만
   그 줄이 한국어로 보인다. 직접 그 언어로 켜 보지 않으면 모른다.

여기서는 사전 자체의 정합성(세 언어가 같은 키를 갖는가, 중복·빈 값은
없는가)과 배선(index.html 이 i18n.js 를 싣는가)을 본다.
"""
from __future__ import annotations

import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "webapp" / "static" / "i18n.js"
INDEX = ROOT / "webapp" / "static" / "index.html"

LANGS = ("en", "ja", "zh-CN")

# 의도적으로 빈 문자열로 옮기는 키 — 다른 언어에 대응어가 없다.
ALLOW_EMPTY = {"님"}


def _dicts() -> dict[str, dict[str, str]]:
    """i18n.js 의 DICT 를 소스에서 읽어 온다 (node 없이)."""
    src = I18N.read_text(encoding="utf-8")
    start = src.index("var DICT = {")
    end = src.index("// ── 상태 ──")
    body = src[start:end]

    out: dict[str, dict[str, str]] = {}
    cur: str | None = None
    # "    en: {" / "    'zh-CN': {" 로 언어 블록이 열린다.
    head = re.compile(r"^    '?([a-zA-Z-]+)'?: \{\s*$")
    # "      '키': '값'," — 값이 다음 줄로 넘어가는 경우도 있다.
    pair = re.compile(r"^      '(.+?)':\s*(.*)$")

    pending_key: str | None = None
    for line in body.splitlines():
        m = head.match(line)
        if m:
            cur = m.group(1)
            out[cur] = {}
            pending_key = None
            continue
        if cur is None:
            continue
        if pending_key is not None:
            out[cur][pending_key] = line.strip().rstrip(",").strip("'")
            pending_key = None
            continue
        m = pair.match(line)
        if not m:
            continue
        key, rest = m.group(1), m.group(2).strip()
        if not rest:                      # 값이 다음 줄에 있다
            pending_key = key
        else:
            out[cur][key] = rest.rstrip(",").strip("'")
    return out


@pytest.fixture(scope="module")
def dicts():
    d = _dicts()
    # 파서가 헛돌면 뒤의 검사가 전부 공허하게 통과한다.
    for lang in LANGS:
        assert lang in d, f"{lang} 블록을 못 찾았다 — 파서가 깨졌다"
        assert len(d[lang]) > 200, f"{lang} 항목이 {len(d[lang])}개뿐 — 파서 의심"
    return d


def test_langs_share_the_same_keys(dicts):
    """세 언어가 같은 키를 갖는다.

    한쪽에만 넣으면 그 언어에서만 한국어가 새는데, 그 언어로 직접
    켜 보기 전에는 아무도 모른다.
    """
    base = set(dicts["en"])
    for lang in ("ja", "zh-CN"):
        missing = sorted(base - set(dicts[lang]))
        extra = sorted(set(dicts[lang]) - base)
        assert not missing, f"{lang} 에 빠진 키 {len(missing)}개: {missing[:5]}"
        assert not extra, f"{lang} 에만 있는 키 {len(extra)}개: {extra[:5]}"


def test_no_value_is_left_in_korean(dicts):
    """번역값에 한글이 남아 있으면 그 줄은 번역이 안 된 것이다."""
    hangul = re.compile(r"[가-힣]")
    for lang in LANGS:
        for k, v in dicts[lang].items():
            if lang == "ja" and k == "님":
                continue          # さん — 한글 아님, 통과
            assert not hangul.search(v), f"{lang}: '{k}' → '{v}' 에 한글이 남았다"


def test_no_empty_translations(dicts):
    for lang in LANGS:
        for k, v in dicts[lang].items():
            if k in ALLOW_EMPTY:
                continue
            assert v.strip(), f"{lang}: '{k}' 의 값이 비었다"


def test_keys_are_unique_within_a_language():
    """중복 키는 나중 것이 앞의 것을 조용히 덮는다."""
    src = I18N.read_text(encoding="utf-8")
    body = src[src.index("var DICT = {"):src.index("// ── 상태 ──")]
    cur = None
    seen: dict[str, set[str]] = {}
    for line in body.splitlines():
        m = re.match(r"^    '?([a-zA-Z-]+)'?: \{\s*$", line)
        if m:
            cur = m.group(1)
            seen[cur] = set()
            continue
        m = re.match(r"^      '(.+?)':", line)
        if m and cur:
            key = m.group(1)
            assert key not in seen[cur], f"{cur} 에 중복 키: '{key}'"
            seen[cur].add(key)


def test_index_html_loads_i18n():
    html = INDEX.read_text(encoding="utf-8")
    assert '<script src="/static/i18n.js"></script>' in html, \
        "index.html 이 i18n.js 를 싣지 않는다 — 언어 설정이 통째로 죽는다"
    assert 'id="lang-picker"' in html, "설정 화면에 언어 선택 자리가 없다"


def test_dates_follow_the_ui_language():
    """날짜·시각 포매팅이 'ko-KR' 로 박혀 있으면 안 된다.

    언어를 영어로 바꿨는데 시계만 "12시 43분 8초" 로 남으면 설정이
    안 먹은 것처럼 보인다. _LOC() 가 화면 언어를 따라간다.
    """
    html = INDEX.read_text(encoding="utf-8")
    # _LOC() 정의 안의 폴백 하나만 허용한다.
    hits = re.findall(r"'ko-KR'", html)
    assert len(hits) <= 2, (
        f"'ko-KR' 하드코딩이 {len(hits)}곳 남았다 — _LOC() 를 쓸 것")
    assert "function _LOC()" in html


def test_i18n_does_not_translate_arbitrary_text():
    """사전에 없는 문자열은 건드리지 않는다는 계약.

    종목명·뉴스 제목·사용자 입력이 번역기를 타면 안 된다. t() 는
    사전 적중일 때만 값을 바꾼다.
    """
    src = I18N.read_text(encoding="utf-8")
    assert "var v = table[s];" in src
    assert "return (typeof v === 'string') ? v : s;" in src
