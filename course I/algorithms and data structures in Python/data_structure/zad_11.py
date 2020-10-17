# Дан список/массив. После каждого элемента добавьте предшествующую ему часть списка.

import array as ar
from random import randint

from additions.tester import time_test, memory_test


@time_test
def foo(subj, res):
    res = res[:]
    for i in range(1, len(subj)):
        for j in subj[:i]:
            res.append(j)
    return res


if __name__ == '__main__':
    a = [randint(-1000, 1000) for _ in range(20)]
    b = ar.array('i', a)
    memory_test(b)
    result = foo(b, ar.array('i'))
    memory_test(result)
    print('result =', result)
    print()
    memory_test(a)
    result = foo(a, [])
    memory_test(result)
    print('result =', result)
