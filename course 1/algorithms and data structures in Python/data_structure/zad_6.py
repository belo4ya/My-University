# Сжать массив, удалив из него все элементы, величина которых находится в интервале [а, b].
# Освободившиеся в конце массива элементы заполнить нулями.

import array as ar
from random import randint

import numpy as np

from additions.tester import time_test, memory_test


def input_filter(kind: str):
    while True:
        try:
            n = int(input(f'Введите число {kind}: '))
        except ValueError:
            print('Введите число')
        else:
            return n


@time_test
def foo(a, b, subj):
    for i in range(len(subj)):
        if a <= subj[i] <= b:
            del subj[i]
            subj.append(0)
    return subj


if __name__ == '__main__':
    a = [randint(-2000, 2000) for _ in range(1000)]
    b = ar.array('i', a)
    A = input_filter('a')
    B = input_filter('b')
    for i in [b, a]:
        memory_test(i)
        result = foo(A, B, i)
        print()
    print('result =', np.array(result))
