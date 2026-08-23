# -*- coding: utf-8 -*-
"""日本語カタログ — パートを束ねるだけ。構造は en と同じ。

キーは韓国語の原文断片。残りは手で数えない::

    python tools/i18n_todo.py ja
"""

from ._glossary import CATALOG as _GLOSSARY
from ._panel import CATALOG as _PANEL

PARTS: dict[str, dict[str, str]] = {
    "glossary": _GLOSSARY,
    "panel": _PANEL,
}

CATALOG: dict[str, str] = {}
for _name, _part in PARTS.items():
    CATALOG.update(_part)

__all__ = ["CATALOG", "PARTS"]
