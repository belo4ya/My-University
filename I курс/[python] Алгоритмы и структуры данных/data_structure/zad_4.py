# Найти в массиве те элементы, значение которых меньше среднего арифметического, взятого от
# всех элементов массива.

import array as ar
from random import randint

import numpy as np

from additions.tester import time_test, memory_test


@time_test
def foo(subj):
    arithmetic = sum(subj) / len(subj)
    res = []
    for i in subj:
        if i < arithmetic:
            res.append(i)
    return np.array(res)


if __name__ == '__main__':
    a = [randint(-2000, 2000) for _ in range(1000)]
    b = ar.array('i', a)
    c = np.array(a)
    for i in [a, b, c]:
        memory_test(i)
        result = foo(i)
        print()
    print('result =', result)
