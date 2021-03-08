# Дан список/массив целых чисел. Упорядочьте по возрастанию только:
# а) положительные числа;

from random import randint

from additions.tester import time_test

# a = [9, 2, -3, 3, -7, 5, 1, -8, 4] - исходные данные
# a = [1, 2, -3, 3, -7, 4, 5, -8, 9] - результат
a = [randint(-10_000, 10_000) for _ in range(10_000)]


@time_test
def foo(a):
    b = list(filter(lambda x: x > 0, a))
    b.sort(reverse=True)
    a = list(map(lambda x: b.pop() if x > 0 else x, a))
    return a


@time_test
def bar(a):
    b = [i for i in a if i > 0]
    b.sort(reverse=True)
    a = [(lambda x: b.pop() if x > 0 else x)(x) for x in a]
    return a


@time_test
def bas(a):
    b = []
    for i in a:
        if i > 0:
            b.append(i)
    b.sort(reverse=True)
    for i in range(len(a)):
        if a[i] > 0:
            a[i] = b.pop()
    return a


if __name__ == '__main__':
    # Интересное наблюдение:
    # - Самый большой и некрасивый код выполняется гораздо быстрее, чем красивый;
    # - Генераторы списков самые медленные.
    foo(a)  # Среднее время выполнения
    bar(a)  # Большое время выполнения
    bas(a)  # Маленькое время выполнения - самый некрасивый код
