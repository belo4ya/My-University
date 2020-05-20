from math import pi, atan
from decimal import Decimal
from check import get_x, get_eps, get_n


def arctg_(x, n=10, eps=None):  # рекуррентная магия
    x = Decimal(x)
    a = Decimal('1.0')
    b = x
    c = Decimal('-1.0')
    res = c / (a * b)
    if eps:
        tmp = 0
        i = 1
        while abs(res - tmp) > eps:
            tmp = res
            a += 2
            b = b * x ** 2
            c = -c
            res += c / (a * b)
            i += 1
        try:
            r = len(str(eps).split('.')[1])
        except IndexError:
            r = int(str(eps).split('-')[1])
        return round(Decimal(pi / 2) + res, r)
    for i in range(1, n):
        a += 2
        b = b * x ** 2
        c = -c
        res += c / (a * b)
    return Decimal(pi / 2) + res


if __name__ == '__main__':
    x = get_x()
    eps = get_eps()
    result = arctg_(x, eps=eps)  # мой результат
    true_res = atan(x)  # настоящий результат
    print(f'arctg({x}) = {result}, с точностью {eps}')
    print(f'arctg({x}) = {true_res}, вычисления, полученные с помощью math')
