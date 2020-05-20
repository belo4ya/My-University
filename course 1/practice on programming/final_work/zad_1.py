from math import cos
from decimal import Decimal
from check import get_x, get_eps, get_n


def cos_(x, n=10, eps=None):  # рекуррентная магия
    x = Decimal(x)
    a = Decimal('1.0')
    b = Decimal('1.0')
    c = Decimal('1.0')
    res = c * a / b
    if eps:
        tmp = 0
        i = 1
        while abs(res - tmp) > eps:
            tmp = res
            a = a * x ** 2
            b = b * (2 * i * (2 * i - 1))
            c = -c
            res += c * a / b
            i += 1
        try:
            r = len(str(eps).split('.')[1])
        except IndexError:
            r = int(str(eps).split('-')[1])
        return round(res, r)
    for i in range(1, n):
        a = a * x ** 2
        b = b * (2 * i * (2 * i - 1))
        c = -c
        res += c * a / b
    return res


if __name__ == '__main__':
    x = get_x()
    eps = get_eps()
    result = cos_(x, eps=eps)  # мой результат
    true_res = cos(x)  # настоящий результат
    print(f'cos({x}) = {result}, с точностью {eps}')
    print(f'cos({x}) = {true_res}, вычисления, полученные с помощью math')
