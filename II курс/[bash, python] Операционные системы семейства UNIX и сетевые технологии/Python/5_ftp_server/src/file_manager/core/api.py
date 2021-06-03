import fnmatch
import os
import shutil
from pathlib import Path
from typing import List


class FileSystemApi:

    @staticmethod
    def getcwd() -> Path:
        return Path(os.getcwd())

    @staticmethod
    def listdir(path: Path, mask: str = "") -> List[Path]:
        if mask != "":
            return fnmatch.filter([p for p in path.iterdir()], mask)
        return list(path.iterdir())

    @staticmethod
    def change_dir(path: Path):
        os.chdir(path)

    @staticmethod
    def create_dir(path: Path, parents=False, exist_ok=False):
        path.mkdir(parents=parents, exist_ok=exist_ok)

    @staticmethod
    def remove_dir(path: Path, recursive=False):
        if recursive:
            shutil.rmtree(path)
        else:
            path.rmdir()

    @staticmethod
    def create_file(path: Path, exist_ok=True):
        path.touch(exist_ok=exist_ok)

    @staticmethod
    def remove_file(path: Path, missing_ok=False):
        path.unlink(missing_ok=missing_ok)

    @staticmethod
    def write_file(path: Path, data: str, encoding="utf-8"):
        path.write_text(data, encoding=encoding)

    @staticmethod
    def show_file(path: Path, encoding="utf-8") -> str:
        return path.read_text(encoding=encoding)

    @staticmethod
    def copy(src: Path, dst: Path, recursive=False):
        if recursive:
            shutil.copytree(src, dst)
        else:
            shutil.copy2(src, dst)

    @staticmethod
    def move(src: Path, dst: Path):
        shutil.move(src, dst)

    @staticmethod
    def rename(src: Path, dst: Path):
        src.rename(dst)
