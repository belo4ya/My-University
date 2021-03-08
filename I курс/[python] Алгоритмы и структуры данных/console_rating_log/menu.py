from datetime import datetime
from time import sleep
import config
import best_api

INPUT = '\n>>> '
EXIT = 'exit - выход/назад\n'
ERROR = '\nНекорректный ввод\n'


def choice_period():
    print('\n1 - Первая половиная семестра')
    print('2 - Вторая половина семестра')
    print(EXIT)
    while True:
        date = str(input(INPUT))
        if date == '1':
            return best_api.Statement(config.FILE_1)
        elif date == '2':
            return best_api.Statement(config.FILE_2)
        elif date.lower() == 'exit':
            return False
        else:
            print(ERROR)


def authorization(statement):
    print('\nДля авторизации в системе введите своё имя')
    print('\nСписок достуных имен:')
    print('- Все студенты ПИ19-3 (ФИ)')
    for i, j in config.teachers.items():
        print('-', i, '-', 'преподаватель', j)
    print(EXIT)
    while True:
        name = str(input(INPUT))
        if name.title() in config.teachers.keys():
            return best_api.Teacher(statement, name.title()), 'T'
        elif statement.get_line_by_name(statement.wb[config.SHT_NAME_1], name.title()):
            return best_api.Student(statement, name.title()), 'S'
        elif name.lower() == 'exit':
            return False
        else:
            print(ERROR)


def student_menu(user):
    while True:
        print('\n1 - Успеваемость по всем предметам')
        print('2 - Успеваемость по выбранному предмету')
        print(EXIT)
        choice = str(input(INPUT))
        if choice == '1':
            user.peek()
            return
        elif choice == '2':
            while True:
                print('\nВведите название предмета (Python, Algorithms, ComputerScience, Mathematics)')
                print(EXIT)
                discipline = str(input(INPUT))
                if discipline.title() in [config.SHT_NAME_1, config.SHT_NAME_2,
                                          config.SHT_NAME_3, config.SHT_NAME_4]:
                    user.peek(discipline)
                elif discipline.lower() == 'exit':
                    break
                else:
                    print(ERROR)
        elif choice.lower() == 'exit':
            return choice
        else:
            print(ERROR)


def teacher_menu(user):
    while True:
        print('\n1 - Посмотреть успеваемость группы')
        print('2 - Перейти в среду редактирования')
        print(EXIT)
        choice = str(input(INPUT))
        if choice == '1':
            user.peek()
        elif choice == '2':
            return 'edit'
        elif choice.lower() == 'exit':
            return 'exit'
        else:
            print(ERROR)


def input_filtering(val):
    val_data = [i.title() for i in val.split(':')]
    if val_data[0] == 'Контрольная работа'.title():
        print('\nВведите 0 <= целое число <= 5')
        print(EXIT)
        while True:
            new_val = str(input(INPUT))
            if new_val.lower() in ['', '~', 'exit']:
                return new_val
            else:
                try:
                    new_val = int(new_val)
                except ValueError:
                    print(ERROR)
                else:
                    if 0 <= new_val <= 5:
                        return new_val
                    else:
                        print(ERROR)
    elif val_data[0] == 'Экзамен':
        print('\nВведите 0 <= целое число <= 60')
        print(EXIT)
        while True:
            new_val = str(input(INPUT))
            if new_val.lower() in ['', '~', 'exit']:
                return new_val
            else:
                try:
                    new_val = int(new_val)
                except ValueError:
                    print(ERROR)
                else:
                    if 0 <= new_val <= 60:
                        return str(new_val)
                    else:
                        print(ERROR)
    elif val_data[1] == 'Задания':
        print('\nВведите кол-во выполненных заданий')
        print('Формат ввода: "Все", "11|15", "4|4", ...')
        print(EXIT)
        while True:
            new_val = str(input(INPUT))
            if new_val.lower() in ['', '~', 'exit', 'все']:
                return new_val
            else:
                try:
                    new_val = [int(i) for i in new_val.split('|')]
                except ValueError:
                    print(ERROR)
                else:
                    if new_val[0] <= new_val[1]:
                        new_val = [str(i) for i in new_val]
                        return '|'.join(new_val)
                    else:
                        print(ERROR)
    elif val_data[1] in ['Выполнено', 'Защищено']:
        print('\nВведите дату в удобном для вас формате: 14.09.2001, 14/09/2001, 14-09-2001')
        print(EXIT)
        while True:
            new_val = str(input(INPUT))
            if new_val.lower() in ['', '~', 'exit']:
                return new_val
            elif '.' in new_val:
                try:
                    new_val = str(datetime.strptime(new_val, '%d.%m.%Y'))
                except ValueError:
                    print(ERROR)
                else:
                    return new_val[:10]
            elif '/' in new_val:
                try:
                    new_val = str(datetime.strptime(new_val, '%d/%m/%Y'))
                except ValueError:
                    print(ERROR)
                else:
                    return new_val[:10]
            elif '-' in new_val:
                try:
                    new_val = str(datetime.strptime(new_val, '%d-%m-%Y'))
                except ValueError:
                    print(ERROR)
                else:
                    return new_val[:10]
            else:
                print(ERROR)
    elif val_data[1] == 'Баллы':
        print('\nВведите 0 <= целое число <= 3')
        print(EXIT)
        while True:
            new_val = str(input(INPUT))
            if new_val.lower() in ['', '~', 'exit']:
                return new_val
            else:
                try:
                    new_val = int(new_val)
                except ValueError:
                    print(ERROR)
                else:
                    if 0 <= new_val <= 3:
                        return str(new_val)
                    else:
                        print(ERROR)
    elif val_data[1] in ['1', '2', '3']:
        print('\nВведите 0 <= целое число <= 2')
        print(EXIT)
        while True:
            new_val = str(input(INPUT))
            if new_val.lower() in ['', '~', 'exit']:
                return new_val
            else:
                try:
                    new_val = int(new_val)
                except ValueError:
                    print(ERROR)
                else:
                    if 0 <= new_val <= 2:
                        return str(new_val)
                    else:
                        print(ERROR)
    else:
        return False


def auto_save(user):
    print('Автоматическое сохранение', end='')
    user.save()
    for _ in range(3):
        print('.', end='')
        sleep(0.35)
    print()


def editing_menu(statement, user):
    print('\n----СРЕДА РЕДАКТИРОВАНИЯ----')
    while True:
        print('\nВыберите режим\n')
        print('1 - Заполнение')
        print('2 - Редактирование')
        print('3 - Справка о режимах редактирования')
        print(EXIT)
        choice = str(input(INPUT))
        if choice == '1':
            while True:
                print('\nВведите ФИ студента, которого хотите редактировать (ну вы поняли)')
                print(EXIT)
                name = str(input(INPUT))
                if name.lower() == 'exit':
                    break
                elif statement.get_line_by_name(statement.wb[config.SHT_NAME_1], name.title()):
                    if statement.file_name == config.FILE_1:
                        headers = [i for i in config.headers if i != 'Экзамен']
                    else:
                        headers = [i for i in config.headers if i != 'Контрольная работа']
                    for i in headers:
                        print('\n' + i)
                        new_val = str(input_filtering(i))
                        if new_val.lower() == 'exit':
                            auto_save(user)
                            break
                        elif new_val == '' or new_val:
                            user.edit(name.title(), i, new_val)
                            if i == 'Контрольная работа' or i == 'Экзамен':
                                auto_save(user)
                        else:
                            print(ERROR)
                else:
                    print(ERROR)
        elif choice == '2':
            while True:
                print('\nВведите ФИ студента, которого хотите редактировать (ну вы поняли)')
                print('exit - Сохранить и вернуться назад!')
                name = str(input(INPUT))
                if name.lower() == 'exit':
                    auto_save(user)
                    break
                elif statement.get_line_by_name(statement.wb[config.SHT_NAME_1], name.title()):
                    print('\nВведите название столбца. Например, "Контрольная работа" или "Практика_1:Баллы"')
                    print('\nПолный список доступных имен: Практика_1:Задания, Практика_1:Выполнено,')
                    print('Практика_1:Защищено, Практика_1:Баллы, Практика_2:Задания, Практика_2:Выполнено,')
                    print('Практика_2:Защищено, Практика_2:Баллы, Практика_3:Задания, Практика_3:Выполнено,')
                    print('Практика_3:Защищено, Практика_3:Баллы, Тесты:1, Тесты:2, Тесты:3,')
                    print('Контрольная работа, Экзамен\n')
                    while True:
                        print('\nВведите название столбца. Например, "Контрольная работа" или "Практика_1:Баллы"')
                        print(EXIT)
                        val = str(input(INPUT))
                        if val.lower() == 'exit':
                            break
                        else:
                            try:
                                user.edit(name.title(), val)
                            except best_api.StatementError:  # Моё исключение
                                print(ERROR)                 # Возникает при отстствии запрашиваемых значений в ячейках
                            else:
                                new_val = str(input_filtering(val))
                                if new_val.lower() == 'exit':
                                    pass
                                elif new_val == '' or new_val:
                                    user.edit(name.title(), val, new_val)
                                else:
                                    print(ERROR)
                else:
                    print(ERROR)
        elif choice == '3':
            print('\n----СПРАВКА----\n')
            print('- Заполнение: в этом режиме вы будете последовательно')
            print('продвигаться по ячейкам без возможности выбора конкретной ячейки.')
            print('- Редактирование: в этом режиме вы можете обратиться к любой ячейке.')
        elif choice.lower() == 'exit':
            return choice
        else:
            print(ERROR)
