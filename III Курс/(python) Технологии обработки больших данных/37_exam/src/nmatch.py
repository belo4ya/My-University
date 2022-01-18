import re


def nmatch(s: str, pattern: re.Pattern) -> int:
    return len(pattern.findall(s))
