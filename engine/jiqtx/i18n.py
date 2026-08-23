# -*- coding: utf-8 -*-
"""
보고서 언어 — 렌더 경계에서 한 번 번역한다
===========================================
화면(webapp/static/i18n.js)과 같은 원칙이지만 방식이 다르다. 보고서는
f-string 으로 HTML 을 조립하기 때문에, 완성된 문장을 키로 쓸 수 없다::

    f'<div class="cs2">확률 {v.direction_prob:.1%} · CI [{lo}, {hi}]</div>'

출력은 ``확률 47.9% · CI [41%, 55%]`` 가 되고, 이런 문자열은 종목마다
전부 다르다. 사전에 넣을 수가 없다.

그래서 **f-string 의 리터럴 조각**(``'확률 '``, ``' · CI ['``)을 키로 쓴다.
이 조각들은 값이 무엇이든 출력에 그대로 실리므로 항상 매칭된다.
키 목록은 ``tools/i18n_extract.py`` 가 AST 로 뽑는다 — 사람이 손으로
모으면 반드시 빠뜨린다.

치환 규칙
---------
- **긴 조각 우선.** ``'판정'`` 과 ``'최종 판정 — 3축 분리'`` 가 모두 있으면
  긴 쪽이 이겨야 한다. 짧은 쪽이 먼저 먹으면 문장이 조각난다.
- **태그 밖 텍스트만.** 속성값·태그명·클래스명을 건드리면 CSS 가 죽는다.
  예외로 툴팁 속성 몇 개는 번역한다(화면에 보이므로).
- ``<style>`` · ``<script>`` 안은 통째로 건너뛴다.
- 사전에 없으면 한국어로 남는다. 틀린 번역보다 원문이 낫다.

보고서는 **생성 시점에 언어가 굳는다.** 자기완결 HTML 이라 나중에 바꿀
방법이 없다 — 테마와 같은 성질이다. 다른 언어로 보려면 다시 생성한다.
"""
from __future__ import annotations

import re
from typing import Dict, List

__all__ = ["LANGS", "catalog", "translate_html", "t", "html_lang"]

# 지원 언어. 'ko' 는 원본이라 사전이 없다(치환 자체를 안 한다).
LANGS: Dict[str, str] = {
    "ko": "ko",
    "en": "en",
    "ja": "ja",
    "zh-CN": "zh-CN",
}

# 화면에 보이는 속성. 툴팁은 태그 밖 텍스트가 아니라 속성에 들어 있다.
_ATTRS = ("data-tip", "data-t", "title", "aria-label", "alt")

_CATALOGS: Dict[str, Dict[str, str]] = {}
_PATTERNS: Dict[str, "re.Pattern[str] | None"] = {}


def catalog(lang: str) -> Dict[str, str]:
    """언어별 사전. 없는 언어는 빈 사전(=원문 유지)."""
    if lang in _CATALOGS:
        return _CATALOGS[lang]
    table: Dict[str, str] = {}
    if lang != "ko":
        mod = lang.replace("-", "_").lower()
        try:
            pkg = __import__(
                "engine.jiqtx.locale.%s" % mod, fromlist=["CATALOG"])
            table = dict(getattr(pkg, "CATALOG", {}))
        except Exception:
            # 사전이 아직 없어도 보고서 생성은 막지 않는다.
            table = {}
    _CATALOGS[lang] = table
    return table


def _pattern(lang: str):
    """사전 키를 긴 것부터 늘어놓은 하나의 정규식.

    파이썬 정규식의 교대(|)는 **먼저 쓴 것**이 이긴다. 그래서 길이
    내림차순으로 붙여야 긴 조각이 우선한다.
    """
    if lang in _PATTERNS:
        return _PATTERNS[lang]
    table = catalog(lang)
    pat = None
    if table:
        keys: List[str] = sorted(table, key=len, reverse=True)
        # 앞뒤가 한글이면 매칭하지 않는다 — 한국어판 단어 경계다.
        #
        # 이게 없으면 조각 치환이 문장을 갈아 버린다. 사전에 '생존편향'
        # 이 있고 출력에 "생존편향된 데이터 소스" 가 있으면, 경계가
        # 없을 때 "survivorship bias된 데이터 소스" 가 된다. '일'(day)
        # 은 '일간'·'일봉'·'내일' 안에서 전부 터진다.
        #
        # 대가: f-string 두 조각이 한글끼리 맞붙어 나오면(드물다)
        # 번역이 안 된다. 그쪽은 한국어로 남을 뿐 망가지지는 않는다 —
        # 틀린 번역보다 원문이 낫다.
        pat = re.compile(
            "(?<![가-힣])(?:%s)(?![가-힣])"
            % "|".join(re.escape(k) for k in keys))
    _PATTERNS[lang] = pat
    return pat


def t(s: str, lang: str = "ko") -> str:
    """문자열 하나를 번역한다 (HTML 아닌 곳에서 쓴다)."""
    if not s or lang == "ko":
        return s
    pat = _pattern(lang)
    if pat is None:
        return s
    table = catalog(lang)
    return pat.sub(lambda m: table[m.group(0)], s)


def html_lang(lang: str) -> str:
    return LANGS.get(lang, "ko")


# <style>/<script> 블록과 태그를 통째로 잡는다. 나머지가 텍스트다.
_CHUNK = re.compile(
    r"(<style\b[^>]*>.*?</style>"
    r"|<script\b[^>]*>.*?</script>"
    r"|<[^>]*>)",
    re.S | re.I,
)
_ATTR_RE = re.compile(
    r"""(\b(?:%s)\s*=\s*)(["'])(.*?)\2"""
    % "|".join(a.replace("-", r"\-") for a in _ATTRS),
    re.S | re.I,
)


def translate_html(html: str, lang: str = "ko") -> str:
    """렌더된 보고서 HTML 을 번역한다.

    태그 밖 텍스트와 툴팁 속성만 건드린다. 사전에 없는 조각(종목명,
    숫자, 사용자 입력)은 그대로 지나간다.
    """
    if not html or lang == "ko":
        return html
    pat = _pattern(lang)
    if pat is None:
        return html
    table = catalog(lang)
    sub = lambda s: pat.sub(lambda m: table[m.group(0)], s)  # noqa: E731

    out: List[str] = []
    for part in _CHUNK.split(html):
        if not part:
            continue
        low = part[:7].lower()
        if low.startswith("<style") or low.startswith("<script"):
            out.append(part)                    # 코드는 손대지 않는다
        elif part.startswith("<"):
            # 태그 자체 — 보이는 속성만 번역한다.
            out.append(_ATTR_RE.sub(
                lambda m: m.group(1) + m.group(2) + sub(m.group(3))
                + m.group(2), part))
        else:
            out.append(sub(part))
    return "".join(out)
