"""asset.py"""

from dataclasses import dataclass


@dataclass
class Asset:
    """Asset

    properties of one service address entry.
    """

    data: dict[str, object]

    def __getattr__(self, name: str) -> object:
        return self.data.get(name)
