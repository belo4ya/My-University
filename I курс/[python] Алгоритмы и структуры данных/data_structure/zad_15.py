# Дан список студентов.Элемент списка содержит фамилию, имя,
# отчество, год рождения, курс, номер группы, оценки по пяти предметам.
# Упорядочите студентов по курсу, причем студенты одного курса
# располагались в алфавитном порядке. Найдите средний балл каждой
# группы по каждому предмету. Определите самого старшего студента
# и самого младшего студентов. Для каждой группы найдите лучшего
# с точки зрения успеваемости студента. Выберете структуру данных
# для программной реализации.

from datetime import datetime

STUDENTS = [
    [
        'Иванов Иван Иванович',
        datetime(2000, 11, 11),
        2,
        'ЙО18-1',
        {
            'Математика': [5, 4, 4, 5, 3, 5, 5],
            'Python': [5, 5, 5, 5, 4],
            'C#': [5, 5],
            'Алгоритмы': [4, 4, 3, 5, 4, 5],
            'Физика': [4, 4, 4, 5]
        }
    ],
    [
        'Петров Петр Петрович',
        datetime(1999, 12, 29),
        2,
        'ЙО18-1',
        {
            'Математика': [4, 4, 3, 5, 3, 5, 4],
            'Python': [4, 4, 4, 5, 4],
            'C#': [5, 4],
            'Алгоритмы': [4, 4, 3, 3, 4, 5],
            'Физика': [4, 3, 4, 5]
        }
    ],
    [
        'Иванов Степан Иванович',
        datetime(2001, 2, 14),
        1,
        'ЙО19-1',
        {
            'Математика': [4, 4, 4, 3, 3, 4, 4],
            'Python': [5, 5, 4, 3, 4],
            'C#': [5, 4],
            'Алгоритмы': [4, 3, 3, 3, 4, 5],
            'Физика': [5, 5, 4, 5]
        }
    ],
    [
        'Соколов Игорь Владимирович',
        datetime(2001, 7, 22),
        1,
        'ЙО19-2',
        {
            'Математика': [5, 4, 4, 5, 3, 5, 5],
            'Python': [5, 5, 5, 5, 4],
            'C#': [5, 5],
            'Алгоритмы': [4, 4, 3, 5, 4, 5],
            'Физика': [4, 4, 4, 5]
        }
    ],
    [
        'Ковалев Алексей Игоревич',
        datetime(2001, 9, 14),
        1,
        'ЙО19-2',
        {
            'Математика': [3, 2, 3, 3, 3, 5, 4],
            'Python': [3, 4, 3, 4, 5],
            'C#': [5, 4],
            'Алгоритмы': [3, 4, 3, 3, 4, 3],
            'Физика': [2, 2, 3, 5]
        }
    ],
    [
        'Соболев Александр Витальевич',
        datetime(2000, 1, 10),
        2,
        'ЁЁ-1',
        {
            'Математика': [5, 4, 4, 5, 4, 5, 5],
            'Python': [5, 5, 5, 5, 4],
            'C#': [5, 5],
            'Алгоритмы': [4, 4, 5, 5, 4, 5],
            'Физика': [5, 5, 4, 5]
        }
    ],
    [
        'Железов Василий Васильевич',
        datetime(2002, 6, 21),
        1,
        'ЙО-2',
        {
            'Математика': [5, 4, 4, 5, 3, 5, 5],
            'Python': [4, 4, 3, 5, 4],
            'C#': [5, 4],
            'Алгоритмы': [4, 5, 4, 5, 4, 5],
            'Физика': [4, 4, 4, 5]
        }
    ],
]


def sort_():
    res = STUDENTS[:]
    res.sort(key=lambda x: x[0])
    res.sort(key=lambda x: x[2], reverse=True)
    for i in res:
        print(i)
    print()
    return res


def average_score():
    res = {}

    def mean(subj):
        return sum(subj) / len(subj)

    mean_ = {}
    tmp = STUDENTS[0][3]
    uniq = len(set([STUDENTS[i][3] for i in range(len(STUDENTS))]))
    i = -1
    while i <= uniq:
        i += 1
        if STUDENTS[i][3] == tmp:
            for k, v in STUDENTS[i][4].items():
                try:
                    mean_[k] = mean([mean(v), mean_[k]])
                except KeyError:
                    mean_[k] = mean(v)
        else:
            res[tmp] = mean_
            tmp = STUDENTS[i][3]
            i -= 1
            mean_ = {}
        if i == uniq:
            res[tmp] = mean_

    for k, v in res.items():
        print(f'Группа {k}')
        for k_, v_ in v.items():
            print(f'{k_}: {v_}')
        print()

    return res


def youngest_oldest():
    res = STUDENTS[:]
    res.sort(key=lambda x: x[1])
    print(f'Самый маленький: {res[len(res)-1][0]} - {res[len(res)-1][1]}')
    print(f'Самый старенький: {res[0][0]} - {res[0][1]}\n')
    return res[len(res)-1], res[0]


def bests():
    res = {}

    def mean(subj):
        return sum(subj) / len(subj)

    mean_ = 0
    for i in range(len(STUDENTS)):
        for v in STUDENTS[i][4].values():
            if mean_:
                mean_ = mean([mean(v), mean_])
            else:
                mean_ = mean(v)
        if STUDENTS[i][3] in res.keys():
            if mean_ > res[STUDENTS[i][3]][1]:
                res[STUDENTS[i][3]] = [STUDENTS[i][0], mean_]
        else:
            res[STUDENTS[i][3]] = [STUDENTS[i][0], mean_]

    for k, v in res.items():
        print(f'Группа {k}')
        print(f'Лучший: {v[0]}, ср. балл: {round(v[1], 2)}')
        print()

    return res


if __name__ == '__main__':
    sort_()
    average_score()
    youngest_oldest()
    bests()
