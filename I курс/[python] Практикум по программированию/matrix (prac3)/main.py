import numpy as np
from matrix import Matrix, MatrixCalculator


def task_1():
    print('\033[34mЗадание 1\033[0m')
    # 1. Задать две произвольные матрицы {3*3}
    print('\n\n\033[31m1. Задать две произвольные матрицы {3*3}\033[0m')
    a = Matrix(3, 3)
    a = a.random_fill()
    b = Matrix(3, 3)
    b = b.random_fill()
    print('\nМатрица А:')
    print(a)
    print('\nМатрица B:')
    print(b)
    # 2. Найти сумму и разность матриц
    print('\n\n\033[31m2. Найти сумму и разность матриц\033[0m')
    print('\nA + B =')
    print(calc.add(a, b))
    print('\nA - B =')
    print(calc.sub(a, b))
    # 3. Для матриц вычислить:
    print('\n\n\033[31m3. Для матриц вычислить:\033[0m')
    # 3.1 Определитель
    print('\n3.1 Определитель')
    print('\nОпределитель А (|A|)')
    print(round(calc.det(a), 3))
    print('\nОпределитель B (|B|)')
    print(round(calc.det(b), 3))
    # 3.2 Транспонированную матрицу
    print('\n3.2 Транспонированную матрицу')
    print('\nТранспонированная А (A^T)')
    print(calc.tran(a))
    print('\nТранспонированная B (B^T)')
    print(calc.tran(b))
    # 3.3 Обратную матрицу
    print('\n3.3 Обратную матрицу')
    print('\nОбратная A (A^-1)')
    inv_a = calc.inv(a)
    print(inv_a)
    print('Проверка: A * A^-1')
    res = calc.dot(a, inv_a)
    for i in range(len(res)):
        for j in range(i):
            res[i][j] = int(res[i][j])  # Очень грубое округление (для наглядности)
    print(res)
    print('\nОбратная B (B^-1)')
    inv_b = calc.inv(b)
    print(inv_b)
    print('Проверка: B * B^-1')
    res = calc.dot(a, inv_a)
    for i in range(len(res)):
        for j in range(i):
            res[i][j] = int(res[i][j])  # Очень грубое округление (для наглядности)
    print(res)
    # 4. Задать матрицы А(2*2), В(2*3), С(3*2), D(2*1) 1 генератором
    # случайных чисел из интервала [1;10]
    print('\n\n\033[31m4. Задать матрицы А(2*2), В(2*3), С(3*2), D(2*1) 1 генератором\n',
          '  случайных чисел из интервала [1;10]\033[0m')
    a = Matrix(2, 2).random_fill()
    b = Matrix(2, 3).random_fill()
    c = Matrix(3, 2).random_fill()
    d = Matrix(2, 1).random_fill()
    print('\nМатрица A:')
    print(a)
    print('\nМатрица B:')
    print(b)
    print('\nМатрица C:')
    print(c)
    print('\nМатрица D:')
    print(d)
    # 5. Найти произведения
    print('\n\n\033[31m5. Найти произведения\033[0m')
    # 5.1 A * B
    print('\nA * B =')
    print(calc.dot(a, b))
    # 5.2 C * D
    print('\nC * D =')
    print(calc.dot(c, d))
    # 5.3 B * C
    print('\nB * C =')
    print(calc.dot(b, c))
    # 5.4 C * B
    print('\nC * B =')
    print(calc.dot(c, b))


def task_2():
    print('\n\n\033[34mЗадание 2\033[0m')
    # 11-ый
    #  | -4a - 8c - 4d - 4 = 0
    # /   6a - 2b - 6c - 6d - 18 = 0
    # \  -4a + 2b - 8c - 8d + 2 = 0
    #  | -8b -6c - 8d - 30 = 0
    print(
        '\n | -4a - 8c - 4d - 4 = 0\n',
        '/  6a - 2b - 6c - 6d - 18 = 0\n',
        '\ -4a + 2b - 8c - 8d + 2 = 0\n',
        '| -8b -6c - 8d - 30 = 0'
    )
    coefficients = {
        '1': (-4, 0, -8, -4, 4),
        '2': (6, -2, -6, -6, 18),
        '3': (-4, 2, -8, -8, -2),
        '4': (0, -8, -6, -8, 30),
    }
    # 1. Решить систему лин. уравенений с помощью обратной матрицы
    print('\n\033[31m1. Решить систему лин. уравенений с помощью обратной матрицы\033[0m')
    main_matrix = permutation_of_columns(coefficients, 4)
    inv_matrix = calc.inv(main_matrix)
    data_matrix = permutation_of_columns(coefficients, 4, 4)
    res = calc.dot(inv_matrix, data_matrix)
    a, b, c, d = round(res[0][0], 1), round(res[1][0], 1), round(res[2][0], 1), round(res[3][0], 1)
    print(f'Ответ: a = {a}, b = {b}, c = {c}, d = {d}')
    # 2. Решить систему лин. уравенений методом Крамера
    print('\n\033[31m2. Решить систему лин. уравенений методом Крамера\033[0m')
    main_matrix = permutation_of_columns(coefficients, 4)
    matrix_a = permutation_of_columns(coefficients, 0)
    matrix_b = permutation_of_columns(coefficients, 1)
    matrix_c = permutation_of_columns(coefficients, 2)
    matrix_d = permutation_of_columns(coefficients, 3)
    det = calc.det(main_matrix)
    det_a = calc.det(matrix_a)
    det_b = calc.det(matrix_b)
    det_c = calc.det(matrix_c)
    det_d = calc.det(matrix_d)
    a = round(det_a / det, 1)
    b = round(det_b / det, 1)
    c = round(det_c / det, 1)
    d = round(det_d / det, 1)
    print(f'Ответ: a = {a}, b = {b}, c = {c}, d = {d}')


# Такой костыль
def permutation_of_columns(coeff, slip, row=None):
    matrix = []
    for i in coeff.values():
        copy_ = list(i)
        copy_[slip] = copy_[4]
        if row:
            matrix.append(copy_[row])
        else:
            matrix.append(copy_[:4])
    if row:
        matrix = Matrix(4, 1).data_fill(matrix)
    else:
        matrix = Matrix(4, 4).data_fill(matrix)
    return matrix


if __name__ == '__main__':
    np.set_printoptions(precision=3)
    calc = MatrixCalculator()
    task_1()
    task_2()
