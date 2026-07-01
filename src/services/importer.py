import pandas as pd

from models.asset import Asset


class ImportService:

    @staticmethod
    def import_file(filepath: str):
        if filepath.endswith(".csv"):
            df: pd.DataFrame = pd.read_csv(filepath)
        else:
            df: pd.DataFrame = pd.read_excel(filepath)

        return [Asset(row.to_dict()) for _, row in df.iterrows()]
