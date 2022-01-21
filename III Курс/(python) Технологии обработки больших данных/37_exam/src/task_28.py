import pandas as pd
from collections import defaultdict
import numpy as np


def smart_count(s: str) -> bool:
    cnt = defaultdict(int)
    for ch in s:
        if cnt[ch] >= 8:
            return True
        cnt[ch] += 1
    return False


def solve(ints_sample) -> list[tuple[int, float]]:
    sin_s = pd.Series(np.sin(ints_sample), index=ints_sample)
    mask = sin_s.apply(lambda s: smart_count(str(s)))
    return list(sin_s[mask].items())
