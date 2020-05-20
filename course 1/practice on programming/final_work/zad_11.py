from math import sin
from decimal import Decimal
from check import get_x, get_eps, get_n


def sin2_(x, n=10, eps=None):  # рекуррентная магия
    x = Decimal(x)
    a = Decimal('0.5')
    b = 1
    c = Decimal('-1.0')
    d = Decimal('1.0')
    res = 0
    if eps:
        tmp = 1
        i = 1
        while abs(res - tmp) > eps:
            tmp = res
            a = a * 4
            b = b * x ** 2
            c = -c
            d = d * (2 * i * (2 * i - 1))
            res += c * a * b / d
            i += 1
        try:
            r = len(str(eps).split('.')[1])
        except IndexError:
            r = int(str(eps).split('-')[1])
        return round(res, r)
    for i in range(1, n):
        a = a * 4
        b = b * x ** 2
        c = -c
        d = d * (2 * i * (2 * i - 1))
        res += c * a * b / d
    return res


if __name__ == '__main__':
    x = get_x()
    n = get_n()
    result = sin2_(x, n=n)  # мой результат
    true_res = sin(x) ** 2  # настоящий результат
    print(f'sin**2({x}) = {result}, для n = {n}')
    print(f'sin**2({x}) = {true_res}, вычисления, полученные с помощью math')
