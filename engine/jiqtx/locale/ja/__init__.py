# -*- coding: utf-8 -*-
"""日本語カタログ — パートを束ねるだけ。構造は en と同じ。

キーは韓国語の原文断片。残りは手で数えない::

    python tools/i18n_todo.py ja
"""

from ._glossary import CATALOG as _GLOSSARY
from ._panel import CATALOG as _PANEL
from ._report import CATALOG as _REPORT
from ._sections import CATALOG as _SECTIONS
from ._verdict import CATALOG as _VERDICT
from ._metrics import CATALOG as _METRICS
from ._trade import CATALOG as _TRADE
from ._equity import CATALOG as _EQUITY
from ._simple import CATALOG as _SIMPLE
from ._dynamic1 import CATALOG as _DYNAMIC1
from ._dynamic2 import CATALOG as _DYNAMIC2
from ._dynamic3 import CATALOG as _DYNAMIC3
from ._panel2 import CATALOG as _PANEL2
from ._book import CATALOG as _BOOK
from ._config import CATALOG as _CONFIG
from ._final import CATALOG as _FINAL
from ._misc import CATALOG as _MISC

PARTS: dict[str, dict[str, str]] = {
    "glossary": _GLOSSARY,
    "panel": _PANEL,
    "report": _REPORT,
    "sections": _SECTIONS,
    "verdict": _VERDICT,
    "metrics": _METRICS,
    "trade": _TRADE,
    "equity": _EQUITY,
    "simple": _SIMPLE,
    "dynamic1": _DYNAMIC1,
    "dynamic2": _DYNAMIC2,
    "dynamic3": _DYNAMIC3,
    "panel2": _PANEL2,
    "book": _BOOK,
    "config": _CONFIG,
    "final": _FINAL,
    "misc": _MISC,
}

CATALOG: dict[str, str] = {}
for _name, _part in PARTS.items():
    CATALOG.update(_part)

__all__ = ["CATALOG", "PARTS"]
