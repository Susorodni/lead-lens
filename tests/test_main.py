from pytest import CaptureFixture

from src.main import main


def test_main(capsys: CaptureFixture[str]) -> None:
    main()

    captured = capsys.readouterr()

    assert captured.out == "running\n"
