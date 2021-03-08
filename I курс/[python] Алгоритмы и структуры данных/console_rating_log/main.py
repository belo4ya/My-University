from menu import *

if __name__ == '__main__':
    print('\nЭта программа, что-то типа Электронного журнала')
    print('Студенты могут смотреть, преподаватели заполнять, изменять...\n')
    print('-----ВАЖНО-----')
    print('Если вы запускаете данный скрипт из командной строки,')
    print('разверните её, пожалуйста, на полный экран.')
    print('-----ВАЖНО-----')
    while True:
        statement = choice_period()
        if statement:
            while True:
                user = authorization(statement)
                if user:
                    if user[1] == 'S':
                        student = user[0]
                        while True:
                            action = str(student_menu(student))
                            if action.lower() == 'exit':
                                break
                    else:
                        teacher = user[0]
                        while True:
                            action = teacher_menu(teacher)
                            if action.lower() == 'exit':
                                break
                            elif action == 'edit':
                                while True:
                                    action = editing_menu(statement, teacher)
                                    if action.lower() == 'exit':
                                        break
                else:
                    break
        else:
            break
