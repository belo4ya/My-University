import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import math
from scipy import integrate
fig, ax = plt.subplots(4, 1, figsize=(11.6, 30))


def settings():
    """
    Форматирование отображения графиков
    :return: None
    """
    for i in range(0, 4):
        ax[i].set_xlabel('x')
        ax[i].set_ylabel('y')
        ax[i].xaxis.set_major_locator(ticker.MultipleLocator(2))
        ax[i].minorticks_on()
        ax[i].grid(color='gray', linestyle=':')
        ax[i].legend(ncol=4, loc=3, bbox_to_anchor=(0, 1))
    plt.subplots_adjust(wspace=0, hspace=0.46)
    plt.savefig('graph.png', format='png', dpi=100)
    plt.show()
    plt.clf()


def get_data():
    """
    :return: Наборы значений x и y
    """
    x = np.arange(-8, 12.2, 0.2)
    y1, y2, y3 = [], [], []
    x1, x2, x3 = [], [], []
    for i in x:
        if -8 <= i <= -3:
            y1.append(math.sin(i+3))
            x1.append(i)
        elif -3 < i <= 6:
            y2.append(abs(i + 3) ** (1/2))
            x2.append(i)
        else:
            y3.append(i / 2)
            x3.append(i)
    y = np.array(y1 + y2 + y3)
    y1, y2, y3 = np.array(y1), np.array(y2), np.array(y3)
    x1, x2, x3 = np.array(x1), np.array(x2), np.array(x3)
    return x, y, y1, y2, y3, x1, x2, x3


def linear(x, y):
    """
    Нахождение Y(расчетного) для линейной линии тренда
    :return: Y(расчетное), мат. ожидание, ср-кв. отклонение, R^2
    """
    n = len(x)
    x_sum = sum(x)
    x_2_sum = sum([i**2 for i in x])
    x_y_sum = sum([x[i]*y[i] for i in range(101)])
    y_sum = sum(y)
    d = n*x_2_sum - x_sum**2
    d1 = y_sum*x_2_sum - x_sum*x_y_sum
    d2 = n*x_y_sum - x_sum*y_sum
    a = d1 / d
    b = d2 / d
    y_calc = []
    new_x = np.arange(-8, 16.02, 0.2)
    for i in new_x:
        y_calc.append(b*i + a)
    y_calc = np.array(y_calc)  # Y(расчетный)
    m = integrate.quad(lambda x: x*b, -8, 12)  # Математическое ожидание
    avr = sum(y_calc[:101]) / n
    qu = math.sqrt(sum([(i - avr)**2 for i in y_calc[:101]]) / n)  # Среднеквадратическое отклонение
    y_y = [i - sum(y_calc[:101]) / n for i in y_calc[:101]]
    x_x = [i - sum(x) / n for i in x]
    x_x_y_y = [y_y[i]*x_x[i] for i in range(n)]
    x_x_2 = [i**2 for i in x_x]
    y_y_2 = [i ** 2 for i in y_y]
    correl = (sum(x_x_y_y) / math.sqrt(sum(x_x_2)*sum(y_y_2)))**2  # Коэффициент детерминации
    return y_calc, m[0], qu, correl


def parabola(x, y):
    """
    Нахождение Y(расчетного) для параболы 2-ого порядка
    :return: Y(расчетное), мат. ожидание, ср-кв. отклонение, R^2
    """
    x_2 = [i**2 for i in x]
    n = len(x)
    x_sum = x.sum()
    y_sum = y.sum()
    x_2_sum = sum(x_2)
    x_3_sum = sum([i**3 for i in x])
    x_4_sum = sum([i**4 for i in x])
    x_y_sum = sum([x[i] * y[i] for i in range(n)])
    x_2_y_sum = sum([x_2[i] * y[i] for i in range(n)])
    d = n*x_2_sum*x_4_sum + x_sum*x_3_sum*x_2_sum + x_2_sum*x_sum*x_3_sum -\
        x_2_sum**3 - n * x_3_sum**2 - x_4_sum * x_sum**2
    d1 = y_sum*x_2_sum*x_4_sum + x_sum*x_3_sum*x_2_y_sum + x_2_sum*x_y_sum*x_3_sum -\
        x_2_y_sum * x_2_sum**2 - y_sum * x_3_sum**2 - x_4_sum*x_y_sum*x_sum
    d2 = n*x_y_sum*x_4_sum + y_sum*x_3_sum*x_2_sum + x_2_sum*x_sum*x_2_y_sum -\
        x_y_sum * x_2_sum**2 - n*x_3_sum*x_2_y_sum - x_4_sum*x_sum*y_sum
    d3 = n*x_2_sum*x_2_y_sum + x_sum*x_y_sum*x_2_sum + y_sum*x_sum*x_3_sum -\
        y_sum * x_2_sum**2 - n*x_y_sum*x_3_sum - x_2_y_sum * x_sum**2
    a = d1 / d
    b = d2 / d
    c = d3 / d
    y_calc = []
    new_x = np.arange(-8, 16.02, 0.2)
    for i in new_x:
        y_calc.append(a + b*i + c*i**2)
    y_calc = np.array(y_calc)  # y(расчетный)
    m = integrate.quad(lambda x: x*(b + 2*c*x), -8, 12)  # Математическое ожидание
    avr = sum(y_calc[:101]) / n
    qu = math.sqrt(sum([(i - avr)**2 for i in y_calc[:101]]) / n)  # Среднеквадратическое отклонение
    y_y = [i - sum(y_calc[:101]) / n for i in y_calc[:101]]
    x_x = [i - sum(x) / n for i in x]
    x_x_y_y = [y_y[i]*x_x[i] for i in range(n)]
    x_x_2 = [i**2 for i in x_x]
    y_y_2 = [i ** 2 for i in y_y]
    correl = (sum(x_x_y_y) / math.sqrt(sum(x_x_2)*sum(y_y_2)))**2  # Коэффициент детерминации
    return y_calc, m[0], qu, correl


def power(x, y):
    """
    Степенная линия тренда - не используется
    """
    # Степенная линия тренда
    # Формула: y_calc_p = a * x**b
    # Преобразования: ln(y_calc_p) = ln(a * x**b);    ln(y_calc_p) = ln(a) + b*ln(x)
    # Замена: ln(y_calc_p) = Y;    ln(a) = A;    ln(x) = X
    # Уравнение: Y = A + b*X
    X = np.log(x[40:])
    Y = np.log(y[40:])
    XY = [X[i]*Y[i] for i in range(61)]
    XX = [i**2 for i in X]
    XX = np.array(XX)
    XY = np.array(XY)
    X_sum = X.sum()
    XX_sum = XX.sum()
    XY_sum = XY.sum()
    Y_sum = Y.sum()
    # Формулы
    A = (Y_sum*XX_sum - X_sum*XY_sum) / (len(X)*XX_sum - X_sum**2)
    B = (len(X)*XY_sum - X_sum*Y_sum) / (len(X)*XX_sum - X_sum**2)
    A = np.e**A
    # y_calc_p = a * x**b
    y_calc = []
    for i in x[40:]:
        y_calc.append(A * i**B)
    y_calc = np.array(y_calc)
    return y_calc


def graph_1(x1, y1, x2, y2, x3, y3, n):
    ax[0].scatter(x1, y1, s=2.5, color='red', label='y=sin(x+3)')
    ax[0].scatter(x2, y2, s=2.5, color='green', label='y=|x+3|^(1/2)')
    ax[0].scatter(x3, y3, s=2.5, color='blue',
                  label='y=x/2' + 30*' ' + f'Кол-во узловых точек: N = {n}')


def graph_2(x, y):
    ax[1].plot(x, y, color='red',
               label='График кусочно-непрерывной F на интервале [-8; 12]')


def graph_3(x, y, y_calc_li, y_calc_p, y_calc_p2):
    ax[2].plot(x, y, color='red', linewidth=2.5, label='Исходная F')
    ax[2].plot(x, y_calc_li[0][:101], color='green',
               label=f'Линия тренда(ЛИНЕЙНАЯ)\nМатематическое ожидание: М = {round(y_calc_li[1], 2)}\n' +
               f'Среднеквадратичное отклонение: Q = {round(y_calc_li[2], 2)}\n' +
               f'Коэффициент детерминации: R^2 = {round(y_calc_li[3], 2)}')
    # ax[2].plot(x[40:], y_calc_p, color='blue', label='Линия тренда\n(СТЕПЕННАЯ[0;12])')
    ax[2].plot(x, y_calc_p2[0][:101], color='blue',
               label=f'Линия тренда(ПАРАБОЛА)\nМатематическое ожидание: М = {round(y_calc_p2[1], 2)}\n' +
               f'Среднеквадратичное отклонение: Q = {round(y_calc_p2[2], 2)}\n' +
               f'Коэффициент детерминации: R^2 = {round(y_calc_p2[3], 2)}')


def graph_4(x, y, y_calc_li, y_calc_p2):
    new_x = np.arange(-8, 16.02, 0.2)
    ax[3].plot(x, y, color='red', linewidth=2.5, label='Исходная F')
    ax[3].plot(new_x, y_calc_li[0], color='green', label='Линия тренда(ЛИНЕЙНАЯ)')
    ax[3].plot(new_x, y_calc_p2[0], color='blue', label=f'Линия тренда(ПАРАБОЛА)')
    ax[3].vlines(-8, -1, 9)
    ax[3].vlines(12, -1, 9)
    ax[3].vlines(16, -1, 9)


def table(x, y):
    x = [str(i.round(4)) for i in x]
    y = [str(i.round(4)) for i in y]
    s = ''
    for i in range(len(x)):
        s += '|' + x[i].rjust(5) + ' |' + y[i].rjust(7) +\
             '|\n|' + '-'*6 + '+' + '-'*7 + '|\n'
    c = '|' + 'x'.rjust(5) + ' |' + 'y'.rjust(7) +\
        '|\n|' + '-'*6 + '+' + '-'*7 + '|\n'
    return c + s


if __name__ == '__main__':
    x, y, y_1, y_2, y_3, x_1, x_2, x_3 = get_data()
    line = linear(x, y)
    prbl = parabola(x, y)
    pwr = power(x, y)  # Степенная
    graph_1(x_1, y_1, x_2, y_2, x_3, y_3, n=len(x))
    graph_2(x, y)
    graph_3(x, y, line, pwr, prbl)
    graph_4(x, y, line, prbl)
    settings()
    print(table(x, y))
