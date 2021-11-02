
from collections import Counter


def char_counts(path) -> Counter:
    with open(path, encoding='cp1251') as f:
        return Counter(f.read().casefold())

