import pandas as pd

from .base_operation import BaseOperation


class FilterOperation(BaseOperation):

    def __init__(self, field: str, value: object):
        self.field: str = field
        self.value: object = value

    @property
    def name(self):
        return "Filter"

    def execute(self, df: pd.DataFrame):
        return df[df[self.field] == self.value]
