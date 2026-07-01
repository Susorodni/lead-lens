from abc import ABC, abstractmethod

from typing import List
from models.asset import Asset


class BaseOperation(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @abstractmethod
    def execute(self, assets: List[Asset]) -> List[Asset]:
        ...
