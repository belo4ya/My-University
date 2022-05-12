import multiprocessing
import random
import time

import filelock
import numpy as np

SIZE = 10
FILE = "matrix.txt"


def zeroes(n, m):
    return [[0 for _ in range(n)] for _ in range(m)]


def random_fill(n, m):
    return [[random.random() for _ in range(n)] for _ in range(m)]


def single_dot(a, b, pos, callback):
    n = len(a[0])
    i, j = pos
    res = sum([a[i][k] * b[k][j] for k in range(n)])

    callback(res, pos)
    return res, pos


def write_locking(res, pos, sep=" "):
    with filelock.FileLock("matrix.txt.lock"):
        with open(FILE, mode="a", encoding="utf-8") as f:
            f.write(sep.join([str(pos[0]), str(pos[1]), str(res)]) + "\n")


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__}:", time.time() - start)
        return result

    return wrapper


@time_it
def parallel_calc(a, b, callback):
    n = SIZE
    args = [(a, b, (i, j), callback) for i in range(n) for j in range(n)]
    with multiprocessing.Pool() as pool:
        res = pool.starmap(single_dot, args)

    pool.join()

    return res


@time_it
def consistently_calc(a, b, callback):
    n = SIZE
    res = zeroes(n, n)
    for i in range(n):
        for j in range(n):
            res[i][j] = single_dot(a, b, (i, j), callback)[1]

    return res


def clear_file():
    with open(FILE, mode="w+"):
        pass


def check_result(a, b):
    empty = zeroes(SIZE, SIZE)
    with open(FILE, mode="r", encoding="utf-8") as f:
        for line in f:
            if line:
                i, j, res = line.strip().split()
                empty[int(i)][int(j)] = float(res)

        print("Validated:", np.all(np.array(empty).round(4) == np.dot(np.array(a), np.array(b)).round(4)))


if __name__ == '__main__':
    for i in range(5):
        clear_file()
        m1 = random_fill(SIZE, SIZE)
        m2 = random_fill(SIZE, SIZE)
        parallel_calc(m1, m2, write_locking)

        # consistently_calc(m1, m2, write_locking)

        check_result(m1, m2)
