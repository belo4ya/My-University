# Сгенерировать 2000 случайных целых чисел в диапазоне от -5 до 4, записать их в ячейки
# массива. Посчитать сколько среди них положительных, отрицательных и нулевых значений.
# Вывести на экран элементы массива и посчитанные количества. Рассмотрите возможность
# использования numpy.set_printoptions для полноценного вывода занчений массива на экран.

from random import randint

import numpy as np

np.set_printoptions(threshold=2000)

if __name__ == '__main__':
    a = np.array([randint(-5, 4) for _ in range(2000)], dtype=int)
    print(a)
    print('Положительных', sum(i > 0 for i in a))
    print('Отрицательных', sum(i < 0 for i in a))
    print('Нулевых', sum(i == 0 for i in a))
