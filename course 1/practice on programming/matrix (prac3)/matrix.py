import numpy as np


class Matrix:

    def __init__(self, size_n, size_m):
        self.n = size_n
        self.m = size_m
        self.matrix = np.zeros((self.n, self.m), dtype=int)

    def random_fill(self):
        self.matrix = np.random.randint(1, 11, (self.n, self.m), dtype=int)
        return self.matrix

    def user_fill(self):
        for i in range(self.n):
            for j in range(self.m):
                while True:
                    try:
                        s = int(input(f'Элемент Matrix[{i+1}:{j+1}]: '))
                    except ValueError:
                        print('Введите целое число!')
                    else:
                        self.matrix[i][j] = s
                        break
        return self.matrix

    # Ни одного чекера!
    def data_fill(self, ar):
        for i in range(len(ar)):
            self.matrix[i] = ar[i]
        return self.matrix

    def display(self):
        print(self.matrix)


class MatrixCalculator:

    def __init__(self):
        pass

    @staticmethod
    def add(a, b):
        return np.add(a, b)

    @staticmethod
    def sub(a, b):
        b = MatrixCalculator.dot(-1, b)
        return np.add(a, b)

    @staticmethod
    def dot(a, b):
        return np.dot(a, b)

    @staticmethod
    def det(a):
        return np.linalg.det(a)

    @staticmethod
    def tran(a):
        return np.transpose(a)

    @staticmethod
    def inv(a):
        return np.linalg.inv(a)
