# 1. Дано натуральное число n. Выведите все числа от 1 до n.


def foo(n, i=1):
    if i <= n:
        print(i, end=' ')
        foo(n, i+1)


n = int(input('n = '))
foo(n)
