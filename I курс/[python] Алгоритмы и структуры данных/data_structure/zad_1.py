# В массиве, содержащем положительные и отрицательные целые числа, вычислить
# сумму четных положительных элементов.

import array as ar
from random import randint

import numpy as np

from additions.tester import time_test, memory_test


@time_test  # 100 раз выполняет функцию и выводит среднее время выполнения (реализация в tester.py)
def foo(subj):
    s = 0
    for i in subj:
        if i % 2 == 0 and i > 0:
            s += i
    return s


if __name__ == '__main__':
    a = [randint(-2000, 2000) for _ in range(1000)]
    b = ar.array('i', a)
    c = np.array(a)
    for i in [a, b, c]:
        memory_test(i)  # Рассчитывает объем памяти, занимаемый объектом и его содержимым (реализация в tester.py)
        result = foo(i)
        print()
    print('result =', result)
