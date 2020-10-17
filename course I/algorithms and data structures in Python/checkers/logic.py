from tools import NAMES


class Cell:

    def __init__(self, name, x, y, color):
        """
        :param name: Имя ячейки на настоящей доске
        :param x: Столбец в массиве
        :param y: Строка в массиве
        :param color: Цвет ячейки (black/white)
        """
        self.name = name
        self.x = x
        self.y = y
        self.color = color
        self.checker = 2


class Board:

    def __init__(self):
        c = Cell
        self.board = [
            [c('a1', 0, 0, 1), c('b1', 1, 0, 0), c('c1', 2, 0, 1), c('d1', 3, 0, 0), c('e1', 4, 0, 1), c('f1', 5, 0, 0), c('g1', 6, 0, 1), c('h1', 7, 0, 0)],
            [c('a2', 0, 1, 0), c('b2', 1, 1, 1), c('c2', 2, 1, 0), c('d2', 3, 1, 1), c('e2', 4, 1, 0), c('f2', 5, 1, 1), c('g2', 6, 1, 0), c('h2', 7, 1, 1)],
            [c('a3', 0, 2, 1), c('b3', 1, 2, 0), c('c3', 2, 2, 1), c('d3', 3, 2, 0), c('e3', 4, 2, 1), c('f3', 5, 2, 0), c('g3', 6, 2, 1), c('h3', 7, 2, 0)],
            [c('a4', 0, 3, 0), c('b4', 1, 3, 1), c('c4', 2, 3, 0), c('d4', 3, 3, 1), c('e4', 4, 3, 0), c('f4', 5, 3, 1), c('g4', 6, 3, 0), c('h4', 7, 3, 1)],
            [c('a5', 0, 4, 1), c('b5', 1, 4, 0), c('c5', 2, 4, 1), c('d5', 3, 4, 0), c('e5', 4, 4, 1), c('f5', 5, 4, 0), c('g5', 6, 4, 1), c('h5', 7, 4, 0)],
            [c('a6', 0, 5, 0), c('b6', 1, 5, 1), c('c6', 2, 5, 0), c('d6', 3, 5, 1), c('e6', 4, 5, 0), c('f6', 5, 5, 1), c('g6', 6, 5, 0), c('h6', 7, 5, 1)],
            [c('a7', 0, 6, 1), c('b7', 1, 6, 0), c('c7', 2, 6, 1), c('d7', 3, 6, 0), c('e7', 4, 6, 1), c('f7', 5, 6, 0), c('g7', 6, 6, 1), c('h7', 7, 6, 0)],
            [c('a8', 0, 7, 0), c('b8', 1, 7, 1), c('c8', 2, 7, 0), c('d8', 3, 7, 1), c('e8', 4, 7, 0), c('f8', 5, 7, 1), c('g8', 6, 7, 0), c('h8', 7, 7, 1)]
        ]

    def fill(self, color, place):
        """
        Заполнение доски шашками (игра 6х6)
        :param color: Цвет игрока
        :param place: Имя ячейки
        :return: True - фигура установлена, False - установка невозможна
        """
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if (self.board[i][j].name == place and
                        self.board[i][j].color == 0 and
                        self.board[i][j].checker == 2):
                    self.board[i][j].checker = color
                    return True
        return False

    def peek(self, color):
        """
        Проверяет всю доску на наличие возможных ходов
        :param color: Цвет игока
        :return: w3 - победа черных, w4 - победа белых, b - нужно бить,
        xx->xx - возможный бой, c - продолжение игры
        """
        a2_b1 = [self.board[1][0], self.board[0][1]]
        a4_d1 = [self.board[3][0], self.board[2][1], self.board[1][2], self.board[0][3]]
        a6_f1 = [
            self.board[5][0], self.board[4][1], self.board[3][2], self.board[2][3],
            self.board[1][4], self.board[0][5]
        ]
        a8_h1 = [
            self.board[7][0], self.board[6][1], self.board[5][2], self.board[4][3],
            self.board[3][4], self.board[2][5], self.board[1][6], self.board[0][7]
        ]
        c8_h3 = [
            self.board[7][2], self.board[6][3], self.board[5][4], self.board[4][5],
            self.board[3][6], self.board[2][7]
        ]
        e8_h5 = [self.board[7][4], self.board[6][5], self.board[5][6], self.board[4][7]]
        g8_h7 = [self.board[7][6], self.board[6][7]]

        h3_f1 = [self.board[2][7], self.board[1][6], self.board[0][5]]
        h5_d1 = [
            self.board[4][7], self.board[3][6], self.board[2][5],
            self.board[1][4], self.board[0][3]
        ]
        h7_b1 = [
            self.board[6][7], self.board[5][6], self.board[4][5], self.board[3][4],
            self.board[2][3], self.board[1][2], self.board[0][1]
        ]
        g8_a2 = [
            self.board[7][6], self.board[6][5], self.board[5][4], self.board[4][3],
            self.board[3][2], self.board[2][1], self.board[1][0]
        ]
        e8_a4 = [
            self.board[7][4], self.board[6][3], self.board[5][2],
            self.board[4][1], self.board[3][0]
        ]
        c8_a6 = [self.board[7][2], self.board[6][1], self.board[5][0]]

        diagonals = [a2_b1, a4_d1, a6_f1, a8_h1, c8_h3, e8_h5, g8_h7, h3_f1, h5_d1, h7_b1, g8_a2, e8_a4, c8_a6]

        checkers = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                checkers.append(self.board[i][j].checker)
                if self.board[i][j].name in NAMES[:4] and self.board[i][j].checker == 3:
                    return 'w3'
                elif self.board[i][j].name in NAMES[28:] and self.board[i][j].checker == 4:
                    return 'w4'
        if len(set(checkers)) == 2:
            if 3 in set(checkers):
                return 'w3'
            else:
                return 'w4'

        nullifier = Cell('', '', '', '')

        for i in diagonals:
            pos_0 = nullifier
            pos_1 = nullifier
            for j in i:
                if pos_0.checker == 3 and pos_1.checker == 4 and j.checker == 2 and color == 3:
                    return 'b', ('->'.join([pos_0.name, j.name]))
                if pos_0.checker == 4 and pos_1.checker == 3 and j.checker == 2 and color == 4:
                    return 'b', ('->'.join([pos_0.name, j.name]))
                pos_0 = pos_1
                pos_1 = j

        for i in diagonals:
            pos_0 = nullifier
            pos_1 = nullifier
            for j in list(reversed(i)):
                if pos_0.checker == 3 and pos_1.checker == 4 and j.checker == 2 and color == 3:
                    return 'b', ('->'.join([pos_0.name, j.name]))
                elif pos_0.checker == 4 and pos_1.checker == 3 and j.checker == 2 and color == 4:
                    return 'b', ('->'.join([pos_0.name, j.name]))
                pos_0 = pos_1
                pos_1 = j

        for i in diagonals:
            pos_0 = nullifier
            for j in i:
                if pos_0.checker == 3 and j.checker == 2 and color == 3:
                    return 'c', color
                pos_0 = j

        for i in diagonals:
            pos_0 = nullifier
            for j in reversed(i):
                if pos_0.checker == 4 and j.checker == 2 and color == 4:
                    return 'c'
                pos_0 = j

        if color == 3:
            return 'w4'
        return 'w3'

    def move(self, color, pos_0, pos_1):
        """
        Ход-Перемещение
        :param color: Цвет игрока
        :param pos_0: Начальная позиция фигуры
        :param pos_1: Конечная позиция фигуры
        :return: None
        """
        pos_1.checker = color
        pos_0.checker = 2

    def battle(self, color, pos_0, pos_1, pos_m):
        """
        Ход-Бой
        :param color: Цвет игрока
        :param pos_0: Начальная позиция фигуры
        :param pos_1: Конечная позиция фигуры
        :param pos_m: Позиция фигуры, которую сняли
        :return: None
        """
        pos_1.checker = color
        pos_0.checker = 2
        self.board[pos_m.y][pos_m.x].checker = 2

    def check(self, color, command):
        """
        Отвечает за ходы по доске
        :param color: Цвет игрока
        :param command: Команда-Ход
        :return: 1 - совершен ход, 0 - неверная команда, (battle_flag, step) - Надо бить, подсказка
        """
        try:
            pos_0, pos_1 = self.parse(color, command)
        except TypeError:
            return 0
        try:
            battle_flag, step = self.peek(color)
        except (TypeError, ValueError):
            battle_flag = 0
            step = ''
        if battle_flag == 'b':
            pos_m = self.battle_check(color, pos_0, pos_1)
            if pos_m:
                self.battle(color, pos_0, pos_1, pos_m)
                return 1
            else:
                return battle_flag, step
        else:
            if self.move_check(color, pos_0, pos_1):
                self.move(color, pos_0, pos_1)
                return 1
            else:
                return 0

    def parse(self, color, command):
        """
        Переводит команды игрока
        :param color: Цвет игрока
        :param command: Команда-Ход
        :return: False - неверный формат команды, (pos_0, pos_1) - (клетка начала, клетка конца хода)
        """
        pos_0 = ''
        pos_1 = ''
        command = [i for i in command.split('->') if i]
        if len(command) == 2:
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.board[i][j].checker == color and self.board[i][j].name == command[0]:
                        pos_0 = self.board[i][j]
                    elif self.board[i][j].checker == 2 and self.board[i][j].name == command[1]:
                        pos_1 = self.board[i][j]
            if pos_0 and pos_1:
                return pos_0, pos_1
        return False

    def move_check(self, color, pos_0, pos_1):
        """
        Проверка на возможность перемещения фигуры в указанном направлении
        :param color: Цвет игрока
        :param pos_0: Начальная позиция фигуры
        :param pos_1: Конечная позиция фигуры
        :return: True - ход возможен, False - ход невозможен
        """
        if color == 4 and abs(pos_0.x - pos_1.x) == 1 and pos_0.y + 1 == pos_1.y and pos_1.checker == 2:
            return True
        elif color == 3 and abs(pos_0.x - pos_1.x) == 1 and pos_0.y - 1 == pos_1.y and pos_1.checker == 2:
            return True
        return False

    def battle_check(self, color, pos_0, pos_1):
        """
        Проверка на возможность боя в указанном направлении
        :param color: Цвет игрока
        :param pos_0: Начальная позиция фигуры
        :param pos_1: Конечная позиция фигуры
        :return: False - бой невозможен, pos_m - позиция шашки, которую бьют
        """
        pos_m = Cell('', '', '', '')
        if pos_1.y > pos_0.y:
            pos_m.y = pos_0.y + 1
            if pos_1.x > pos_0.x:
                pos_m.x = pos_0.x + 1
            else:
                pos_m.x = pos_0.x - 1
        else:
            pos_m.y = pos_0.y - 1
            if pos_1.x > pos_0.x:
                pos_m.x = pos_0.x + 1
            else:
                pos_m.x = pos_0.x - 1
        pos_m = self.board[pos_m.y][pos_m.x]
        if pos_m.checker != 2 and color != pos_m.checker and abs(pos_0.x - pos_1.x) == 2\
                and abs(pos_0.y - pos_1.y) == 2 and pos_1.checker == 2:
            return pos_m
        return False

    def render(self):
        """
        Вывод доски в привычном для игры виде
        :return: None
        """
        separator_1 = '  |-----------------------------------------------|\n'
        separator_2 = '  |-----+-----+-----+-----+-----+-----+-----+-----|\n'
        header = '  |  a  |  b  |  c  |  d  |  e  |  f  |  g  |  h  |\n'
        line = '{i} |  {a}  |  {b}  |  {c}  |  {d}  |  {e}  |  {f}  |  {g}  |  {h}  | {i}\n'
        template = header + separator_1
        visual = {
            0: 'х',
            1: ' ',
            2: 'х',
            3: 'Ч',
            4: 'Б'
        }
        table = ''
        tmp = {}
        k = 97
        for i in range(len(self.board)):
            for j in self.board[i]:
                if j.color:
                    tmp[chr(k)] = visual[j.color]
                else:
                    tmp[chr(k)] = visual[j.checker]
                k += 1
            tmp['i'] = i + 1
            table += line.format(**tmp) + separator_2
            k = 97
        template += table[:-52] + separator_1 + header
        print(template)
