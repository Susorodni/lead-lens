from src.models.asset_manager import AssetManager


def test_asset_manager_creation() -> None:
    manager = AssetManager()

    assert manager is not None
