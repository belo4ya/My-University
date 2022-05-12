# Дан текстовый файл. Создайте двусвязный список (или массив), каждый элемент которого
# содержит количество символов в соответствующей строке текста.

import array as ar
from additions.tester import time_test, memory_test
from additions.dlinked_list import MDLinkedList


def get_lines(path):
    list_lines = []
    with open(path, 'r', encoding='utf-8') as f:
        for i in f:
            list_lines.append(i)
    return list_lines


@time_test
def foo(subj, lines):
    try:
        res = subj[:]
    except TypeError:
        res = subj.copy()
    for i in lines:
        res.append(len(i))
    return res


if __name__ == '__main__':
    a = ar.array('i')
    path = 'files/for_13.txt'
    lines = get_lines(path)
    a = foo(a, lines)
    memory_test(a)
    print(a)
    print()
    b = MDLinkedList([])
    b = foo(b, lines)
    memory_test(b)
    print(b)
    print()
    c = foo([], lines)
    memory_test(c)
    print(c)
