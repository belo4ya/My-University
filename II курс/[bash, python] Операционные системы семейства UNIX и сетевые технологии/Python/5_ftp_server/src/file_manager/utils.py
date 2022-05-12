from pathlib import Path


def get_abspath(path: str) -> Path:
    return Path(path).absolute()
