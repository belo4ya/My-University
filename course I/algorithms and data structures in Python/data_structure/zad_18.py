# Заполнить массив случайными положительными и отрицательными целыми числами. Вывести его
# на экран. Удалить из массива все отрицательные элементы и снова вывести.

import array as ar
from random import randint

from additions.tester import time_test


@time_test
def foo(subj):
    return ar.array('i', [i for i in subj if i >= 0])


@time_test
def bar(subj):
    return ar.array('i', list(filter(lambda x: x >= 0, subj)))


@time_test
def bas(subj):
    res = subj[:]
    for i in subj:
        if i < 0:
            res.remove(i)  # O(n)
    return res


if __name__ == '__main__':
    b = ar.array('i', [randint(-10, 10) for _ in range(25)])
    print(b)
    x = foo(b)  # На массивах почему-то генератор
    y = bar(b)  # быстрее, чем filter()
    z = bas(b)  # Самый неэффективный
    print(x)
    print(y)
    print(z)
