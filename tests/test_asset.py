from src.models.asset import Asset


def test_getattr_existing_key() -> None:
    asset = Asset(
        {
            "address": "123 Main St",
            "status": "Active",
        }
    )

    assert asset.address == "123 Main St"


def test_getattr_missing_key() -> None:
    asset = Asset({})

    assert asset.missing_property is None
