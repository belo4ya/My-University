from math import cosh
from check import get_x, get_eps, get_n


def ch_(x, n=10, eps=None):  # рекуррентная магия
    a = 1.0
    b = 1.0
    res = a / b
    if eps:
        tmp = 0
        i = 1
        while abs(res - tmp) > eps:
            tmp = res
            a = a * x ** 2
            b = b * (2 * i * (2 * i - 1))
            res += a / b
            i += 1
        try:
            r = len(str(eps).split('.')[1])
        except IndexError:
            r = int(str(eps).split('-')[1])
        return round(res, r)
    for i in range(1, n):
        a = a * x**2
        b = b * (2 * i * (2 * i - 1))
        res += a / b
    return res


if __name__ == '__main__':
    x = get_x()
    n = get_n()
    result = ch_(x, n=n)  # мой результат
    true_res = cosh(x)  # настоящий результат
    print(f'ch({x}) = {result}, для n = {n}')
    print(f'ch({x}) = {true_res}, вычисления, полученные с помощью math')
