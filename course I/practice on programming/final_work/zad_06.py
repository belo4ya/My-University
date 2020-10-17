from math import pi
from check import get_x, get_eps, get_n


def arcctg_(x, n=10, eps=None):  # рекуррентная магия
    a = x
    b = 1.0
    c = -1.0
    res = c * a / b
    if eps:
        tmp = 0
        i = 1
        while abs(res - tmp) > eps:
            tmp = res
            a = a * x ** 2
            b += 2
            c = -c
            res += c * a / b
            i += 1
        try:
            r = len(str(eps).split('.')[1])
        except IndexError:
            r = int(str(eps).split('-')[1])
        return round(pi / 2 + res, r)
    for i in range(1, n):
        a = a * x ** 2
        b += 2
        c = -c
        res += c * a / b
    return pi / 2 + res


if __name__ == '__main__':
    while True:
        print('Введите |x| <= 1')
        x = get_x()
        if abs(x) <= 1:
            break
    eps = get_eps()
    result = arcctg_(x, eps=eps)  # мой результат
    print(f'arcctg({x}) = {result}, с точностью {eps}')
