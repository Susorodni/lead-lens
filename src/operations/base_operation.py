from abc import ABC, abstractmethod

import pandas as pd


class BaseOperation(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def execute(self, df: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError
