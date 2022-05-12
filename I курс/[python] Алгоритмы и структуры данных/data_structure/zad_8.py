# Пользователь вводит упорядоченный список/массив книг (заданной длины по алфавиту).
# Добавить новую книгу, сохранив упорядоченность списка по алфавиту

import numpy as np

from additions.tester import time_test, memory_test


@time_test
def foo(subj):
    new_book = 'Курс Алгебры'
    try:
        new_subj = subj[:]
        new_subj.append(new_book)
    except AttributeError:
        new_subj = np.ones((len(subj)+1), dtype=f'<U{max([len(i) for i in subj])}')
        new_subj[:len(subj)] = subj
        new_subj[-1] = new_book
    return sorted(new_subj)


if __name__ == '__main__':
    a = ['Богатый папа, бедный папа',
         'Грокаем алгоритмы',
         'Думай и богатей',
         'Кто заплачет, когда ты умрешь',
         'Мастер времени',
         'Мертвые души',
         'Укус Питона']
    c = np.array(a)
    for i in [a, c]:
        memory_test(i)
        result = foo(i)
        print()
    print('result =', result)
