import math


def foo_1(x):
    return math.atan(x) / (x**2 + 1)


def foo_2(x):
    return ((x**2 + 1) * math.log((2 - x) / (2 + x))) / math.sqrt(x**2 + 4)


def trapezoid(foo, a, b, n=1000):
    result = 0
    h = (b - a) / n
    for i in range(n):
        result += h * 0.5 * (foo(a + i * h) + foo(a + (i+1) * h))
    return result


def simpson(foo, a, b, n=1000):
    result = (b - a) / 6 * (foo(a) + 4 * foo((a + b) / 2) + foo(b))
    return result


def kotes_simpson(foo, a, b, n=1000):
    h = (b - a) / n
    x = [a + i * h for i in range(n)]
    y = [foo(i) for i in x]
    result = h / 3 * (min(y) + max(y) + 4 * sum([y[i] for i in range(len(y)) if i % 2])
                      + 2 * sum([y[i] for i in range(len(y)) if i % 2 == 0]))
    return result


if __name__ == '__main__':
    print('11.1 ∫ arctg(x)/(x^2+1) dx, x=0 to 1')
    print('11.2 ∫ (x^2+1)/sqrt(x^2+4) * ln((2-x)/(2+x)) dx, x=0 to 1')

    print('\nМетодом трапеций')
    print('1.', trapezoid(foo_1, 0, 1))
    print('2.', trapezoid(foo_2, 0, 1))

    print('\nФормулой Симпсона')
    print('1.', simpson(foo_1, 0, 1))
    print('2.', simpson(foo_2, 0, 1))

    print('\nСоставной формулой (формулой Котеса)')
    print('1.', kotes_simpson(foo_1, 0, 1))
    print('2.', kotes_simpson(foo_2, 0, 1))
