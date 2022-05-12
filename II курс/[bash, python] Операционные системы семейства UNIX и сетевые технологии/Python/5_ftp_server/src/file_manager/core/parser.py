import shlex
import sys
from typing import List, Tuple


class Parser:

    def __init__(self, platform: str = None):
        self.platform = platform or sys.platform
        self.posix = self.platform != "win32"

    def parse(self, s: str, ignore_case: bool = False) -> Tuple[List[str], List[str]]:
        if ignore_case:
            s = s.lower()

        paths = []
        args = []
        for el in shlex.split(s, posix=self.posix):
            if el.startswith("-"):
                args.append(el)
            else:
                paths.append(el)

        return paths, args
