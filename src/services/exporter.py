import pandas as pd


class ExportService:

    @staticmethod
    def export_excel(filepath: str, df: pd.DataFrame) -> None:
        df.to_excel(filepath, index=False)

    @staticmethod
    def export_csv(filepath: str, df: pd.DataFrame) -> None:
        df.to_csv(filepath, index=False)
