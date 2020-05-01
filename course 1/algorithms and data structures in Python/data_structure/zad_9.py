# Дан список/массив целых чисел. Упорядочьте по возрастанию только:
# а) положительные числа;
# б) элементы с четными порядковыми номерами в списке.

import array as ar
from random import randint

import numpy as np

from additions.tester import time_test, memory_test


@time_test
def foo(subj):
    array_positive = [i for i in subj if i > 0]
    array_positive.sort(reverse=True)
    return [(lambda x: array_positive.pop() if x > 0 else x)(x) for x in subj]


@time_test
def bar(subj):
    array_positive = [i for i in range(len(subj)) if i % 2]
    array_positive.sort(reverse=True)
    return [(lambda x: array_positive.pop() if x % 2 == 0 else subj[x])(x) for x in range(len(subj))]


if __name__ == '__main__':
    a = [randint(-2000, 2000) for _ in range(1000)]
    b = ar.array('i', a)
    c = np.array(a)
    # Задание a)
    print('\nЗадание a)')
    for i in [a, b, c]:
        memory_test(i)
        result = foo(i)
        print()
    print('result =', np.array(result))
    # Задание b)
    print('\nЗадание b)')
    for i in [a, b, c]:
        memory_test(i)
        result = bar(i)
        print()
    print('result =', np.array(result))
