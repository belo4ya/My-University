# Выполните oбработку элементов прямоугольной матрицы A, имеющей N строк и M столбцов. Все
# элeменты имeют целый тип. Дано целое число H. Опрeделите, какие столбцы имeют хотя бы
# однo такое число, а какие не имeют.

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
def create_matrix(n, m):
    c = np.zeros((n, m), dtype=int)
    for i in range(n):
        for j in range(m):
            c[i][j] = randint(-20, 20)
    return c


@time_test
def check(matrix, h):
    res = []
    for i in matrix:
        for j in range(len(i)):
            if h == i[j]:
                a.append(j+1)
    return sorted(set(res))


if __name__ == '__main__':
    N, M = input_filter('Строк'), input_filter('Столбцов')
    c = create_matrix(N, M)
    memory_test(c)
    print(c)
    H = input_filter('H')
    a = check(c, H)
    if a:
        print('Столбцы:', *a, f'содержат {H}')
    else:
        print(f'Число {H} не найдено')
