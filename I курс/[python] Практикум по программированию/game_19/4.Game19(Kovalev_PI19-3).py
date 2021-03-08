board = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9]
sh = 3 # Количество строк в игровом поле

# Отображение игрового поля
def draw_board(board, sh):
    print('__________________________\ny:x:   1|2|3|4|5|6|7|8|9||\n--------------------------')
    for i in range(sh):
        print(
                "%03d" % (1 + i), ' |', board[0 + i * 9], board[1 + i * 9], board[2 + i * 9],
                board[3 + i * 9], board[4 + i * 9], board[5 + i * 9],
                board[6 + i * 9], board[7 + i * 9], board[8 + i * 9], "|"
            )
    print('--------------------------\ny:x:   1|2|3|4|5|6|7|8|9||\n__________________________')

# Изменяет список board для последующего вывода через функцию draw_board
def change_board(board):
    global sh
    k = 0
    for i in board:
        if ' ' in board:
            board.remove(' ')
    for i in range(len(board)):
        if board[i] == 'X':
            pass
        else:
            board.append(board[i])
            k += 1
    reslen = len(board)
    if reslen % 9 != 0:
        sh = reslen // 9 + 1
    else:
        sh = reslen // 9
    for i in range(20):
            board.append(' ')
    return sh

# Проверяет "на победу"
# !Искусственную проверку может не пройти (если все элементы в board заменить на 'X'),
# но в реальной ситуации в списке всегда будут 2 элемента: ' ' и 'X'.
def check_win():
    if len(set(board)) == 2:
        return True
    else:
        return False

# Проверка интервала 'X' в строке
def check_x_row(col_start, col_end, row):
    ibegin = 0
    iend = 0
    if (col_start - col_end) < 0:
        ibegin = col_start
        iend = col_end
    else:
        ibegin = col_end
        iend = col_start
    ibegin += 1
    for i in  range(iend - ibegin):
        index = i + ibegin + 9 * row
        if board[index] != 'X':
            return False
    return True

# Проверка интервала 'X' в столбце
def check_x_col(row_start, row_end, col):
    ibegin = 0
    iend = 0
    if (row_start - row_end) < 0:
        ibegin = row_start
        iend = row_end
    else:
        ibegin = row_end
        iend = row_start
    ibegin += 1
    for i in range(iend - ibegin):
        index = 9 * (i + ibegin) + col
        if board[index] != 'X':
            return False
    return True

# Проверяет поле на наличие доступных ходов
def check_board():
    for i in range(len(board) - 1):
        row = int(i / 9)
        col = int(i % 9)
        if (board[i] != 'X' and board[i] != ' ') :
            if col != 8:
                if (board[i + 1] != 'X' and board[i + 1] != ' '):
                    if (board[i] == board[i + 1]) or (board[i] + board[i + 1]) == 10:
                        return True
                elif (board[i + 1] == 'X'):
                    for ii in range(1,9 - col):
                        if (board[i + ii] != 'X' and board[i + ii] != ' '):
                            if (board[i] == board[i + ii]) or (board[i] + board[i + ii]) == 10:
                                return True
                            else:
                                break
            if row != int(sh - 1):
                if (board[i + 9] != 'X' and board[i + 9] != ' '):
                    if board[i] == board[i + 9] or (board[i] + board[i + 9]) == 10:
                        return True
                elif (board[i + 9] == 'X'):
                    for ii in range(9, 9 * (int(sh - 1) - row), 9):
                        if (board[i + ii] != 'X' and board[i + ii] != ' '):
                            if (board[i] == board[i + ii]) or (board[i] + board[i + ii]) == 10:
                                return True
                            else:
                                break
    return False

# Пользовательский ввод и игра
def user_in_put():
    pos1 = ''
    pos2 = ''
    while True:
        xy1 = []
        xy2 = []
        for digit in input('Введите координаты в формате "x1;y1":\n>>>').split(';'):
            xy1.append(digit)
        print(xy1)
        for digit in input('Введите координаты в формате "x2;y2":\n>>>').split(';'):
            xy2.append(digit)
        print(xy2)
        try:
            xy1[0] = int(xy1[0])
            xy1[1] = int(xy1[1])
            xy2[0] = int(xy2[0])
            xy2[1] = int(xy2[1])
        except:
            print('Некорректный ввод. Попробуйте ещё раз.')
            continue
        xy1[0] -= 1
        xy1[1] -= 1
        xy2[0] -= 1
        xy2[1] -= 1
        if (
                xy1[0] <= 8 and xy2[0] <= 8 and xy1[0] * xy1[1] <= len(board) and
                xy2[0] * xy2[1] <= len(board) and (xy1[0] != xy2[0] or xy1[1] != xy2[1])
            ):
                pos1 = 9 * xy1[1] + xy1[0]
                pos2 = 9 * xy2[1] + xy2[0]
                if board[pos1] != 'X' and board[pos2] != 'X' and board[pos1] != ' ' and board[pos2] != ' ':
                    if (
                            (((xy1[1] == xy2[1] and abs(xy1[0] - xy2[0]) <= 1) or
                            (xy1[0] == xy2[0] and abs(xy1[1] - xy2[1]) <= 1)) or
                            (xy1[1] == xy2[1] and check_x_row(xy1[0], xy2[0], xy1[1]) or
                            (xy1[0] == xy2[0] and check_x_col(xy1[1], xy2[1], xy1[0]))))and
                            (board[pos1] == board[pos2] or (board[pos1] + board[pos2] == 10))
                        ):
                            board[pos1] = 'X'
                            board[pos2] = 'X'
                            break
                    else:
                        print('Неверный ход!')
                else:
                    print('Неверный ход!')
        else:
            print('Попробуйте ввести координаты, принадлежащие игровому полю')

# Программа
print('-----Цифры, числа, семечки или 19-----')
print('\nДобро пожаловать! Используйте команды, приведенные ниже:\n')
while True:
    k = 0
    win = False
    start = str(input('Команды:\n!start - начать игру;\n!rules - ознакомиться с правилами;\n!exit - выход.\n>>> '))
    if start == '!start':
        while not win:
            k += 1
            while  not check_win():
                draw_board(board, sh)
                user_in_put()
                if not check_board():
                    change_board(board)
            else:
                if k > 0:
                    win = check_win()
        else:
            score = 11200 - 137 * k
            print(f'\n-----Victory!-----\nYour score: {score}')
    elif start == '!rules':
        print('''
                Цифры, числа, семечки или 19. Правила.
-----------------------------------------------------------------------
На экране монитора появляются числа от 1 до 19(10 пропускается) так,
что в каждом ряду по 9 цифр. Цель игры - вычеркнуть все пары одинаковых
цифр или цифр, составляющих в сумме "10." Пары могут распологаться
по вертикали, горизонтали или через ряд уже зачеркнутых чисел.
Когда все возможные пары вычеркнуты, оставшиеся не зачеркнутые цифры
переписываются вниз, и процесс продолжается...
Подробнее: http://podelki-fox.ru/igry-dlya-detey-na-bumage-s-chislami/

!Цифры выбираются по их координатам в таблице. Ввод координат
осуществялется с клавиатуры: "x1;y1"[Enter], "x2;y2"[Enter].
-----------------------------------------------------------------------
        ''')
    elif start == '!exit':
        print('Bye!')
        break
    else:
        print('Введена неверная команда')