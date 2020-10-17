# Вычислить сумму модулей элементов массива, расположенных после первого отрицательного
# элемента.

import array as ar
from random import randint

import numpy as np

from additions.tester import time_test, memory_test


@time_test
def foo(subj):
    res = 0
    for i in range(len(subj)):
        if subj[i] < 0:
            for j in range(i+1, len(subj)):
                res += abs(subj[j])
            return res


if __name__ == '__main__':
    a = [randint(-2000, 2000) for _ in range(1000)]
    b = ar.array('i', a)
    c = np.array(a)
    for i in [a, b, c]:
        memory_test(i)
        result = foo(i)
        print()
    print('result =', result)
