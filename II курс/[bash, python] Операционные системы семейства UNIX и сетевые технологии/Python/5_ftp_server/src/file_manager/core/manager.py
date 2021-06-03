import os
import re
from pathlib import Path
from typing import List

from src.file_manager.core.api import FileSystemApi
from src.file_manager.utils import get_abspath


class Manager:

    def __init__(self, root: str):
        self._root = get_abspath(root)
        os.chdir(self._root)

        self._file_system = FileSystemApi

    @property
    def cwd(self):
        return self._file_system.getcwd()

    def root(self) -> "Answer":
        try:
            self._file_system.change_dir(self._root)
        except OSError as e:
            return Answer(returncode=1, error=e)

        return Answer(returncode=0)

    def listdir(self, path: str, mask: str) -> "Answer":
        path = get_abspath(path)

        if not self._in_scope_root(path):
            error = RootScopeError(self._root, path)
            return Answer(returncode=1, error=error)

        try:
            data = self._file_system.listdir(path, mask)
            return Answer(returncode=0, payload=data)
        except OSError as e:
            return Answer(returncode=1, error=e)

    def change_dir(self, path: str) -> "Answer":
        if re.fullmatch(r"\.{2,}", path):
            n_steps = len(path) - 2
            if n_steps >= len(self.cwd.parents):
                error = RootScopeError(self._root, path)
                return Answer(returncode=1, error=error)

            path = self.cwd.parents[n_steps]
        else:
            path = get_abspath(path)

        if not self._in_scope_root(path):
            error = RootScopeError(self._root, path)
            return Answer(returncode=1, error=error)

        try:
            self._file_system.change_dir(path)
        except OSError as e:
            return Answer(returncode=1, error=e)

        return Answer(returncode=0)

    def create_dir(self, path: str, args: List[str]) -> "Answer":
        path = get_abspath(path)
        parents = "-p" in args
        exist_ok = "-q" in args

        if not self._in_scope_root(path):
            error = RootScopeError(self._root, path)
            return Answer(returncode=1, error=error)

        if not self._is_valid_params(["-p", "-q"], args):
            error = OptionError()
            return Answer(returncode=1, error=error)

        try:
            self._file_system.create_dir(path, parents=parents, exist_ok=exist_ok)
        except OSError as e:
            return Answer(returncode=1, error=e)

        return Answer(returncode=0)

    def remove_dir(self, path: str, args: List[str]) -> "Answer":
        path = get_abspath(path)
        recursive = "-r" in args

        if not self._in_scope_root(path):
            error = RootScopeError(self._root, path)
            return Answer(returncode=1, error=error)

        if not self._is_valid_params(["-r"], args):
            error = OptionError()
            return Answer(returncode=1, error=error)

        try:
            self._file_system.remove_dir(path, recursive=recursive)
        except OSError as e:
            return Answer(returncode=1, error=e)

        return Answer(returncode=0)

    def create_file(self, path: str, args: List[str]) -> "Answer":
        path = get_abspath(path)
        exist_ok = "-q" in args

        if not self._in_scope_root(path):
            error = RootScopeError(self._root, path)
            return Answer(returncode=1, error=error)

        if not self._is_valid_params(["-q"], args):
            error = OptionError()
            return Answer(returncode=1, error=error)

        try:
            self._file_system.create_file(path, exist_ok=exist_ok)
        except OSError as e:
            return Answer(returncode=1, error=e)

        return Answer(returncode=0)

    def remove_file(self, path: str, args: List[str]) -> "Answer":
        path = get_abspath(path)
        missing_ok = "-q" in args

        if not self._in_scope_root(path):
            error = RootScopeError(self._root, path)
            return Answer(returncode=1, error=error)

        if not self._is_valid_params(["-q"], args):
            error = OptionError()
            return Answer(returncode=1, error=error)

        try:
            self._file_system.remove_file(path, missing_ok=missing_ok)
        except OSError as e:
            return Answer(returncode=1, error=e)

        return Answer(returncode=0)

    def write_file(self, path: str, data: str) -> "Answer":
        path = get_abspath(path)

        if not self._in_scope_root(path):
            error = RootScopeError(self._root, path)
            return Answer(returncode=1, error=error)

        try:
            self._file_system.write_file(path, data)
        except OSError as e:
            return Answer(returncode=1, error=e)

        return Answer(returncode=0)

    def show_file(self, path: str) -> "Answer":
        path = get_abspath(path)

        if not self._in_scope_root(path):
            error = RootScopeError(self._root, path)
            return Answer(returncode=1, error=error)

        try:
            data = self._file_system.show_file(path)
            return Answer(returncode=0, payload=data)
        except OSError as e:
            return Answer(returncode=1, error=e)

    def copy(self, src: str, dst: str, args: List[str]) -> "Answer":
        src, dst = get_abspath(src), get_abspath(dst)
        recursive = "-r" in args

        for path in [src, dst]:
            if not self._in_scope_root(path):
                error = RootScopeError(self._root, path)
                return Answer(returncode=1, error=error)

        if not self._is_valid_params(["-r"], args):
            error = OptionError()
            return Answer(returncode=1, error=error)

        try:
            self._file_system.copy(src, dst, recursive)
        except OSError as e:
            return Answer(returncode=1, error=e)

        return Answer(returncode=0)

    def move(self, src: str, dst: str) -> "Answer":
        src, dst = get_abspath(src), get_abspath(dst)

        for path in [src, dst]:
            if not self._in_scope_root(path):
                error = RootScopeError(self._root, path)
                return Answer(returncode=1, error=error)

        try:
            self._file_system.move(src, dst)
        except OSError as e:
            return Answer(returncode=1, error=e)

        return Answer(returncode=0)

    def rename(self, src: str, dst: str) -> "Answer":
        src, dst = get_abspath(src), get_abspath(dst)

        for path in [src, dst]:
            if not self._in_scope_root(path):
                error = RootScopeError(self._root, path)
                return Answer(returncode=1, error=error)

        try:
            self._file_system.rename(src, dst)
        except OSError as e:
            return Answer(returncode=1, error=e)

        return Answer(returncode=0)

    def _in_scope_root(self, path: Path) -> bool:
        return path == self._root or self._root in path.parents

    @staticmethod
    def _is_valid_params(params: List[str], args: List[str]):
        for arg in args:
            if arg not in params:
                return False

        return True


class Answer:

    def __init__(self, returncode, msg="", payload=None, error=None):
        self.returncode = returncode
        self.msg = msg
        self.payload = payload
        self.error = error

    def __repr__(self):
        output = ['returncode={!r}'.format(self.returncode)]
        if self.msg is not None:
            output.append('msg={!r}'.format(self.msg))
        if self.error is not None:
            output.append('error={!r}'.format(self.error))
        if self.payload is not None:
            output.append('payload={!r}'.format(self.payload))
        return "{}({})".format(type(self).__name__, ', '.join(output))

    __str__ = __repr__


class RootScopeError(OSError):

    def __init__(self, filename=None, filename2=None):
        self.filename = str(filename)
        self.filename2 = str(filename2)
        self.strerror = f"Попытка выхода за пределы корневого каталога"


class OptionError(OSError):

    def __init__(self, option=None):
        self.option = option
        self.strerror = f"Недопустимый параметр: '{self.option}'"
