import timeit


def time_test(function):
    def wrapper(*args):
        time = 0
        for i in range(1000):
            start = timeit.default_timer()
            function(*args)
            stop = timeit.default_timer()
            time += stop - start
        res = function(*args)
        print(f"Время исполнения {function.__name__}:", f'{time / 1000:.10f}', 's')
        return res
    return wrapper
