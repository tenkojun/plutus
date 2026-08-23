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

PARTS: dict[str, dict[str, str]] = {
    "glossary": _GLOSSARY,
    "panel": _PANEL,
    "report": _REPORT,
    "sections": _SECTIONS,
    "verdict": _VERDICT,
    "metrics": _METRICS,
}

CATALOG: dict[str, str] = {}
for _name, _part in PARTS.items():
    CATALOG.update(_part)

__all__ = ["CATALOG", "PARTS"]
