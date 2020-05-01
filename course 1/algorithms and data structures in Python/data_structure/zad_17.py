# Сдвинуть элементы массива в указанном направлении (влево или вправо) и на указанное число
# шагов. Освободившиеся ячейки заполнить нулями. Выводить массив после каждого шага.

import array as ar
from random import randint

from additions.tester import time_test


@time_test
def foo(subj, p):
    res = subj[:]
    if p == '<':
        for i in range(len(subj)-1):
            res[i] = res[i+1]
        res[-1] = 0
    else:
        for i in range(len(subj)-1, 0, -1):
            res[i] = res[i-1]
        res[0] = 0
    return res


if __name__ == '__main__':
    P = '<'  # Направление сдвига
    N = 4  # Кол-во шагов
    b = ar.array('i', [randint(-10, 10) for _ in range(10)])
    print(b)
    for i in range(N):
        b = foo(b, P)
        print(b)
