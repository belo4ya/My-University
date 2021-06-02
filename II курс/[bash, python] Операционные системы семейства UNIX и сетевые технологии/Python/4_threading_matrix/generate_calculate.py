import multiprocessing
import threading

import matrix_dot

queue = multiprocessing.Queue()
is_working = multiprocessing.Event()


def parallel_gen(size):
    while is_working.is_set():
        queue.put(matrix_dot.random_fill(size, size))


def parallel_calc():
    while is_working.is_set():
        if queue.qsize() > 1:
            m1 = queue.get()
            m2 = queue.get()
            matrix_dot.parallel_calc(m1, m2, matrix_dot.write_locking)


def console():
    while is_working.is_set():
        cmd = input(">>> ")
        if cmd.lower() == "exit":
            is_working.clear()


if __name__ == '__main__':
    is_working.set()
    threading.Thread(target=parallel_gen, args=(matrix_dot.SIZE,)).start()
    parallel_calc()
