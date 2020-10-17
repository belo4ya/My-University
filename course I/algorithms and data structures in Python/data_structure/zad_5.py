# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как
# равны между собой (оба являться минимальными), так и различаться.

import array as ar
from random import randint

import numpy as np

from additions.tester import time_test, memory_test


@time_test
def foo(subj):
    return sorted(subj)[0], sorted(subj)[1]


if __name__ == '__main__':
    a = [randint(-2000, 2000) for _ in range(1000)]
    b = ar.array('i', a)
    c = np.array(a)
    for i in [a, b, c]:
        memory_test(i)
        result = foo(i)
        print()
    print('result =', result)
