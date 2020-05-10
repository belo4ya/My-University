from matplotlib import pyplot as plt
import numpy as np
import math


if __name__ == '__main__':
    # 2y'+ y = 55
    # 2 * dy(x)/dx + y(x) = 55
    # --------------------------
    # dy(x)/dx + 1/2 * y(x) = 0 | * dx, / y(x)
    # dy(x)/dy + 1/2 * dx = 0
    # ∫dy(x)/y(x) = -∫1/2dx
    # ln|y| = -x/2
    # y = e^(-x/2) * C
    # --------------------------
    # y = C * e^(-x/2) + 55
    C = 11
    e = math.e
    x = np.linspace(-10, 10, 200)
    y = C * (e**(-x / 2)) + 55
    plt.plot(x, y)
    plt.savefig('differential_equation.png', format='png')
    plt.show()
