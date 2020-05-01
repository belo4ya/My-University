# Создайте двусвязный список (или массив) групп факультета. Каждая группа представляет
# собой односвязный список (или массив) студентов.

from additions.tester import memory_test, time_test
from additions.dlinked_list import MDLinkedList
from random import shuffle, randint


def generator_groups():
    alphabet = 'АБВГД'
    digits = '123456789'
    groups = []
    group_name = ''
    for i in alphabet:
        group_name += i
        for k in alphabet:
            group_name += k + '-'
            for m in digits:
                group_name += m
                for n in digits:
                    group_name += n
                    groups.append(group_name)
                    group_name = group_name[:-1]
                group_name = group_name[:-1]
            group_name = group_name[:-2]
        group_name = group_name[1:]
    return groups


def generator_students():
    names = ['Иван', 'Егор', 'Степан', 'Петр', 'Александр', 'Артем']
    surnames = ['Иванов', 'Петров', 'Смирнов', 'Кузнецов', 'Попов', 'Соболев']
    students = [i + ' ' + j for i in surnames for j in names]
    return students


# [[group_name, list_students], [group_name, list_students], ..., [group_name, list_students]]
def create_list(groups, students):
    c = [list() for _ in range(len(groups))]
    for i in range(len(groups)):
        c[i].append(groups[i])
        shuffle(students)
        c[i].append(sorted(students[:randint(18, 24)]))
    return c


# [[group_name, link_list_students], [group_name, link_list_students], ..., [group_name, link_list_students]]
def create_deque_linked_list(groups, students):
    c = [list() for _ in range(len(groups))]
    for i in range(len(groups)):
        c[i].append(groups[i])
        shuffle(students)
        tmp = MDLinkedList(sorted(students[:randint(18, 24)]))
        c[i].append(tmp.link_list)
    return c


@time_test
def get_group(subj):
    for i in subj:
        if i[0] == GROUP:
            return i


@time_test
def get_student(subj):
    if STUDENT in subj[1]:
        return STUDENT


@time_test
def insert_student(subj):
    subj = subj[1].copy()
    subj.insert(10, 'Новенький')
    return subj


if __name__ == '__main__':
    GROUP = 'ВВ-55'
    STUDENT = 'Иванов Иван'
    groups = generator_groups()
    students = generator_students()
    a = create_list(groups, students)
    b = create_deque_linked_list(groups, students)
    print('\nПамять:')
    print('\nСписки в списке')
    memory_test(a)
    print('\nДвусвязные списки(очереди) в списке')
    memory_test(b)
    print('\nСкорость нахождения группы:')
    print('\nСписки в списке')
    g_a = get_group(a)
    print(g_a)
    print('\nДвусвязные списки(очереди) в списке')
    g_b = get_group(b)
    print(g_b)
    print('\nСкорость нахождения студента в группе:')
    print('\nВ списке')
    print(get_student(g_a))
    print('\nВ дусвязном списке')
    print(get_student(g_b))
    print('\nСкорость добавления студента')
    print('\nВ списке')
    g_a[1] = insert_student(g_a)
    print('\nВ дусвязном списке')
    g_b[1] = insert_student(g_b)
    print(g_a)
    print(g_b)
