# Даны два списка/массива. Определите, совпадают ли множества их элементов.

import array as ar
from random import randint

import numpy as np

from additions.tester import time_test, memory_test


@time_test
def foo(subj_1, subj_2):
    if set(subj_1) == set(subj_2):
        return True
    return False


if __name__ == '__main__':
    a_1 = [randint(-10, 20) for _ in range(200)]
    b_1 = ar.array('i', a_1)
    c_1 = np.array(a_1)
    a_2 = [randint(-10, 20) for _ in range(200)]
    b_2 = ar.array('i', a_2)
    c_2 = np.array(a_2)
    for i, j in [(a_1, a_2), (b_1, b_2), (c_1, c_2)]:
        memory_test(i)
        memory_test(j)
        result = foo(i, j)
        print()
    print('result =', result)