# Заполнить вводом с клавиатуры численный массив за исключением последнего элемента,
# вывести его на экран. Запросить еще одно значение и его позицию в в массиве. Вставить
# указанное число в заданную позицию, подвинув элементы после него.

import numpy as np


def input_filter(kind: str):
    while True:
        try:
            n = int(input(f'Введите число {kind}: '))
        except ValueError:
            print('Введите число')
        else:
            return n


def foo(subj, j, n):
    res = subj[:]
    for i in range(len(subj)-1, j, -1):
        res[i] = res[i-1]
    c[j] = n
    return res


if __name__ == '__main__':
    c = np.zeros(8, dtype=int)
    print(c)
    for i in range(len(c) - 1):
        c[i] = input_filter('целое')
    print(c)
    n = input_filter('целое')
    while True:
        i = input_filter('индекс')
        if abs(i) <= len(c) - 1:
            break
        else:
            print(f'Размер массива {len(c)}')
    print(foo(c, i, n))
