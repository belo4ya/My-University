# Заполнить один массив случайными числами, другой - введенными с клавиатуры числами, в
# ячейки третьего записать суммы соответствующих ячеек первых двух. Вывести содержимое
# массивов на экран.

from random import randint

import numpy as np


def input_filter(kind: str):
    while True:
        try:
            n = int(input(f'Введите число {kind}: '))
        except ValueError:
            print('Введите число')
        else:
            return n


def add_cells(a, b):
    return np.array(list(map(lambda x, y: x+y, a, b)), dtype=int)


if __name__ == '__main__':
    a = np.array([randint(-1000, 1000) for _ in range(8)], dtype=int)
    b = np.zeros(8, dtype=int)
    for i in range(len(b)):
        b[i] = input_filter('целое')
    print('Массив a', a)
    print('Массив b', b)
    print('Массив c', add_cells(a, b))
