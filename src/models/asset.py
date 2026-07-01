"""asset.py"""

from dataclasses import dataclass
from typing import Any, Hashable


@dataclass
class Asset:
    """Asset

    properties of one service address entry.
    """

    data: dict[Hashable, Any]

    def get(self, key: str, default=None):
        return self.data.get(key, default)
    
    def set(self, key: str, value: object):
        self.data[key] = value
