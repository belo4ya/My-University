# В массиве найти максимальный элемент с четным индексом.
# Другая формулировка задачи: среди элементов массива с четными индексами, найти тот,
# который имеет максимальное значение.

import array as ar
import numpy as np
from additions.tester import time_test, memory_test
from random import randint


@time_test
def foo(subj):
    m = 0
    for i in range(len(subj)):
        if i % 2 == 0 and subj[i] > m:
            m = subj[i]
    return m


if __name__ == '__main__':
    a = [randint(-2000, 2000) for _ in range(1000)]
    b = ar.array('i', a)
    c = np.array(a)
    for i in [a, b, c]:
        memory_test(i)
        result = foo(i)
        print()
    print('result =', result)
