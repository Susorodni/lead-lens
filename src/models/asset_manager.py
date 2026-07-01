"""asset_manager.py"""

from typing import List

from operations.base_operation import BaseOperation

from .asset import Asset


class AssetManager:

    def __init__(self):
        self.assets: List[Asset] = []

    def load_assets(self, assets: List[Asset]):
        self.assets = assets

    def apply_operation(self, operation: BaseOperation):
        self.assets = operation.execute(self.assets)

    def get_assets(self):
        return self.assets
