import pandas as pd


class ImportService:

    @staticmethod
    def import_file(filepath: str) -> pd.DataFrame:
        if filepath.endswith(".csv"):
            df: pd.DataFrame = pd.read_csv(filepath)
        else:
            df: pd.DataFrame = pd.read_excel(filepath)

        return df
