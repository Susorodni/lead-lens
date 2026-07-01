format:
    isort .
    black .

lint:
    flake8 .
    mypy .

test:
    pytest

coverage:
    pytest \
        --cov=src \
        --cov-report=term \
        --cov-report=html

quick:
    isort --check .
    black --check .
    flake8 .
    mypy .

enforced:
    isort --check .
    black --check .
    flake8 .
    mypy .
    pytest \
        --cov=src \
        --cov-fail-under=100

debug:
    pytest -vv -s

fix:
    isort .
    black .
