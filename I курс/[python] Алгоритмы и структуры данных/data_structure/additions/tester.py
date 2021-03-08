import timeit
from collections.abc import Mapping, Container
from sys import getsizeof


def time_test(function):
    def wrapper(*args):
        time = 0
        for i in range(100):
            start = timeit.default_timer()
            function(*args)
            stop = timeit.default_timer()
            time += stop - start
        res = function(*args)
        print(f"Время исполнения {function.__name__}:", f'{time / 100:.10f}', 's')
        return res
    return wrapper


def memory_test(subj):
    print(f'Объект {subj.__class__} - {deep_getsizeof(subj, set())} bytes')


# Элементы созданные повторно, т. е. копии (ссылки на них) не учитываются
def deep_getsizeof(subj, ids):
    if id(subj) in ids:
        return 0
    r = getsizeof(subj)
    ids.add(id(subj))
    if isinstance(subj, str):
        return r
    elif isinstance(subj, Mapping):
        return r + sum(deep_getsizeof(k, ids) + deep_getsizeof(v, ids) for k, v in subj.iteritems())
    elif isinstance(subj, Container):
        return r + sum(deep_getsizeof(x, ids) for x in subj)
    return r
