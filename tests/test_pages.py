# -*- coding: utf-8 -*-
"""
GitHub Pages 조립 검사.

사이트 본문은 저장소에 없다 — `tools/build_pages.py` 가 README 4개를
빌드 시점에 조립한다. 그래서 깨져도 로컬에서는 티가 안 나고, Actions 가
초록불로 끝난 뒤 **사이트에서만** 404·깨진 이미지로 드러난다.
여기서 조립 결과를 직접 만들어 본다.
"""
from __future__ import annotations

import io
import re
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
if str(ROOT / "tools") not in sys.path:
    sys.path.insert(0, str(ROOT / "tools"))

import build_pages as bp  # noqa: E402

LANGS = ["ko", "en", "ja", "zh-cn"]


@pytest.fixture(scope="module")
def built():
    bp.build()
    return {p["code"]: io.open(SITE / p["out"], encoding="utf-8").read()
            for p in bp.PAGES}


def test_four_languages_are_built(built):
    assert sorted(built) == sorted(LANGS)
    for code, text in built.items():
        assert len(text) > 5000, code


def test_front_matter_has_permalink_and_lang(built):
    for page in bp.PAGES:
        head = built[page["code"]].split("---")[1]
        assert "permalink: " + page["permalink"] in head
        assert "lang: " + page["lang"] in head
        # 검색결과에 그대로 뜨는 문장이라 비어 있으면 안 된다
        assert len(page["desc"]) > 80


def test_korean_is_the_root_page():
    ko = [p for p in bp.PAGES if p["code"] == "ko"][0]
    assert ko["permalink"] == "/"
    assert ko["src"] == "README.md"


def test_no_repo_relative_links_survive(built):
    """상대링크가 남으면 사이트에서 404 다 — 조용히 깨지는 종류."""
    for code, text in built.items():
        assert not bp._REPO_LINK.findall(text), code


def test_images_point_at_site_assets(built):
    """baseurl 을 빼면 도메인 루트를 가리켜 404 다 — 로고가 사라진다."""
    for code, text in built.items():
        assert "webapp/static/" not in text, code
        assert "{{ site.baseurl }}/assets/" in text, code
        assert 'srcset="/assets/' not in text, code
        assert 'src="/assets/' not in text, code
    for rel in bp.ASSETS:
        assert (SITE / "assets" / Path(rel).name).exists()


def test_language_bar_is_stripped(built):
    """레이아웃이 스위처를 그린다. 본문에 또 있으면 두 줄이 된다."""
    for code, text in built.items():
        body = text.split("---", 2)[2]
        assert not [l for l in body.split("\n")
                    if "한국어" in l and "日本語" in l and "简体中文" in l], code


# ── 레이아웃 · 설정 ────────────────────────────────────────────

LAYOUT = io.open(SITE / "_layouts" / "page.html", encoding="utf-8").read()
CONFIG = io.open(SITE / "_config.yml", encoding="utf-8").read()


def test_layout_declares_every_hreflang():
    """
    hreflang 이 없으면 네 언어판이 중복으로 취급돼 하나만 색인된다.
    x-default 는 어느 언어도 안 맞을 때의 목적지 — 한국어다.
    """
    for code in ["ko", "en", "ja", "zh-Hans"]:
        assert code in LAYOUT
    assert 'hreflang="x-default"' in LAYOUT
    assert 'href="{{ site.url }}{{ site.baseurl }}/"' in LAYOUT


def test_layout_has_seo_and_sitemap_wiring():
    # title=false — 제목은 직접 쓴다(안 그러면 이름이 두 번 들어간다)
    assert "{% seo title=false %}" in LAYOUT
    assert "<title>{{ page.title" in LAYOUT
    assert "jekyll-seo-tag" in CONFIG
    assert "jekyll-sitemap" in CONFIG


def test_config_base_url_matches_the_repo():
    assert "baseurl: /plutus" in CONFIG
    assert "url: https://tenkojun.github.io" in CONFIG


def test_robots_points_at_the_sitemap():
    txt = io.open(SITE / "robots.txt", encoding="utf-8").read()
    assert "https://tenkojun.github.io/plutus/sitemap.xml" in txt


def test_generated_pages_are_not_committed():
    """
    README 가 단일 소스다. 조립 결과를 커밋하면 두 벌이 되고, 반드시
    한쪽만 고쳐진다. (locale/ 이 .gitignore 에 먹혀 빈 사전을 커밋했던
    사고와 같은 종류 — 이번엔 반대 방향으로 막는다.)
    """
    import subprocess
    out = subprocess.run(["git", "ls-files", "site"], cwd=str(ROOT),
                         capture_output=True, text=True).stdout.split()
    tracked = set(out)
    assert "site/_config.yml" in tracked
    assert "site/_layouts/page.html" in tracked
    for page in bp.PAGES:
        assert "site/" + page["out"] not in tracked


def test_workflow_builds_from_readme():
    wf = io.open(ROOT / ".github" / "workflows" / "pages.yml",
                 encoding="utf-8").read()
    assert "tools/build_pages.py" in wf
    assert "source: ./site" in wf
