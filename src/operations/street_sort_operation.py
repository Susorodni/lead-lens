import re

import pandas as pd

from .base_operation import BaseOperation


class StreetSortOperation(BaseOperation):

    def __init__(self) -> None:
        pass

    @property
    def name(self):
        return "Sort"

    def address_split(self, address: str) -> tuple[str, int]:
        """Converts:
        '123 SAMPLE ST' into: ('SAMPLE ST', 123)

        Args:
            address (str): full service street address

        Returns:
            tuple[str, int]: [street name, street number]
        """
        match = re.match(r"^\s*(\d+)\s+(.*)$", address)

        if not match:
            return (address.upper(), 0)

        street_number = int(match.group(1))
        street_name = match.group(2).upper()

        return (street_name, street_number)

    def execute(self, df: pd.DataFrame) -> pd.DataFrame:
        return df.sort_values(
            by="Service Address",
            key=lambda s: s.map(self.address_split)
        )
