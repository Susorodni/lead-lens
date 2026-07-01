from typing import List

import pandas as pd

from models.asset import Asset


class ExportService:

    @staticmethod
    def export_excel(filepath: str, assets: List[Asset]) -> None:
        df: pd.DataFrame = pd.DataFrame([asset.data for asset in assets])

        df.to_excel(filepath, index=False)

    @staticmethod
    def export_csv(filepath: str, assets: List[Asset]) -> None:
        df: pd.DataFrame = pd.DataFrame([asset.data for asset in assets])

        df.to_csv(filepath, index=False)
