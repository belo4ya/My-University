# Выполнить программную реализацию калькулятора матриц.

import numpy as np

from additions.matrix import Matrix, MatrixCalculator

# Не использованы, но реализованы(см. matrix.py):
# Заполнение матрицы с клавиатуры (.user_fill())
# Заполнение матрицы с итерирумого объекта (.data_fill())
if __name__ == '__main__':
    np.set_printoptions(precision=3)  # Округление
    calc = MatrixCalculator()
    a = Matrix(3, 3).random_fill()
    b = Matrix(3, 3).random_fill()
    print('Матрица A')
    print(a)
    print('\nМатрица B')
    print(b)
    res = calc.add(a, b)
    print('\nA + B =')
    print(res)
    res = calc.sub(a, b)
    print('\nA - B =')
    print(res)
    res = calc.dot(a, b)
    print('\nA * B =')
    print(res)
    res = calc.det(a)
    print('\n|A| =')
    print(res)
    res = calc.tran(a)
    print('\nA^T =')
    print(res)
    res = calc.inv(a)
    print('\nA^-1')
    print(res)
