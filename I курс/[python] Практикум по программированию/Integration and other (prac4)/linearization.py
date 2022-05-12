from sympy import *
from matplotlib import pyplot as plt
import numpy as np


def foo(x):
    return 6 / (8 + 2 * x - x**2)


def linearization(foo, x, x0=1):
    dx = symbols('x')
    diff_ = str(diff(foo(dx), dx))
    diff_ = diff_.replace('x', str(x0))
    return foo(x0) + eval(diff_) * (x - x0)


if __name__ == '__main__':
    x = np.linspace(-10, 10, 200)
    y = np.array(foo(x))
    y_lin = np.array(linearization(foo, x))
    plt.plot(x, y)
    plt.plot(x, y_lin)
    plt.savefig('linearization.png', format='png')
    plt.show()
