import math


def foo(chunk, ints_sample):
    limit = 0.99999999
    result = set()
    for i in chunk:
        for j in ints_sample:
            sin_mul = math.sin(i * j)
            if sin_mul > limit:
                result.add((frozenset([i, j]), sin_mul))  # оставляем уникальную пару без порядка элементов

    return result
