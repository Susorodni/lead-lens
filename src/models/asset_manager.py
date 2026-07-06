"""asset_manager.py"""

from operations.base_operation import BaseOperation

import pandas as pd


class AssetManager:

    def __init__(self) -> None:
        self.df: pd.DataFrame = pd.DataFrame()

    def load_assets(self, df: pd.DataFrame) -> None:
        self.df = df

    def apply_operation(self, operation: BaseOperation) -> None:
        self.df = operation.execute(self.df)

    def get_assets(self) -> pd.DataFrame:
        return self.df
