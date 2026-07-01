from typing import List

from models.asset import Asset

from .base_operation import BaseOperation


class FilterOperation(BaseOperation):

    def __init__(self, field: str, value: object):
        self.field: str = field
        self.value: object = value

    @property
    def name(self):
        return "Filter"

    def execute(self, assets: List[Asset]):
        return [asset for asset in assets if asset.get(self.field) == self.value]
