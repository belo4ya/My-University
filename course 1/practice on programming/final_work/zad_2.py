from math import sinh
from decimal import Decimal
from check import get_x, get_eps, get_n


def sh_(x, n=10, eps=None):  # рекуррентная магия
    x = Decimal(x)
    a = x
    b = 1
    res = a / b
    if eps:
        tmp = 0
        i = 1
        while abs(res - tmp) > eps:
            tmp = res
            a = a * x ** 2
            b = b * ((2 * i + 1) * 2 * i)
            res += a / b
            i += 1
        try:
            r = len(str(eps).split('.')[1])
        except IndexError:
            r = int(str(eps).split('-')[1])
        return round(res, r)
    for i in range(1, n):
        a = a * x ** 2
        b = b * ((2 * i + 1) * 2 * i)
        res += a / b
    return res


if __name__ == '__main__':
    x = get_x()
    eps = get_eps()
    result = sh_(x, eps=eps)  # мой результат
    true_res = sinh(x)  # настоящий результат
    print(f'sh({x}) = {result}, с точностью {eps}')
    print(f'sh({x}) = {true_res}, вычисления, полученные с помощью math')
