# -*- coding: utf-8 -*-
"""简体中文目录 — 只负责把各部分合并。结构与 en 相同。

键是韩文原文片段。剩余项不要手工统计::

    python tools/i18n_todo.py zh-CN
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
