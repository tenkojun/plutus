# -*- coding: utf-8 -*-
"""English catalog — assembled from parts so batches stay reviewable.

One flat file would be 2,000+ entries and every edit would rewrite all of
it. Each part mirrors a source module group instead, and this module just
merges them. A key defined twice is a bug — `tests/test_report_i18n.py`
fails on it rather than letting the later part win silently.
"""
from ._glossary import CATALOG as _GLOSSARY
from ._panel import CATALOG as _PANEL
from ._report import CATALOG as _REPORT
from ._sections import CATALOG as _SECTIONS
from ._verdict import CATALOG as _VERDICT
from ._metrics import CATALOG as _METRICS
from ._risk import CATALOG as _RISK
from ._trade import CATALOG as _TRADE
from ._macro import CATALOG as _MACRO
from ._factors import CATALOG as _FACTORS
from ._portfolio import CATALOG as _PORTFOLIO
from ._dynamic1 import CATALOG as _DYNAMIC1
from ._dynamic2 import CATALOG as _DYNAMIC2
from ._dynamic3 import CATALOG as _DYNAMIC3
from ._equity import CATALOG as _EQUITY
from ._simple import CATALOG as _SIMPLE
from ._book import CATALOG as _BOOK
from ._panel2 import CATALOG as _PANEL2
from ._config import CATALOG as _CONFIG
from ._misc import CATALOG as _MISC
from ._final import CATALOG as _FINAL
from ._markdown import CATALOG as _MARKDOWN

PARTS = {
    "glossary": _GLOSSARY,
    "panel": _PANEL,
    "report": _REPORT,
    "sections": _SECTIONS,
    "verdict": _VERDICT,
    "metrics": _METRICS,
    "risk": _RISK,
    "trade": _TRADE,
    "macro": _MACRO,
    "factors": _FACTORS,
    "portfolio": _PORTFOLIO,
    "dynamic1": _DYNAMIC1,
    "dynamic2": _DYNAMIC2,
    "dynamic3": _DYNAMIC3,
    "equity": _EQUITY,
    "simple": _SIMPLE,
    "book": _BOOK,
    "panel2": _PANEL2,
    "config": _CONFIG,
    "misc": _MISC,
    "final": _FINAL,
    "markdown": _MARKDOWN,
}

CATALOG: dict[str, str] = {}
for _name, _part in PARTS.items():
    CATALOG.update(_part)

__all__ = ["CATALOG", "PARTS"]
