NAMES = [
    'g1', 'e1', 'c1', 'a1',
    'h2', 'f2', 'd2', 'b2',
    'g3', 'e3', 'c3', 'a3',
    'h4', 'f4', 'd4', 'b4',
    'g5', 'e5', 'c5', 'a5',
    'h6', 'f6', 'd6', 'b6',
    'g7', 'e7', 'c7', 'a7',
    'h8', 'f8', 'd8', 'b8',
]


class Game:

    def __init__(self):
        pass

    def start(self):
        pass

    def game(self):
        pass

    def restart(self):
        pass

    def end(self, flag=None):
        pass

    def fill(self):
        pass

    def move(self):
        pass

    def log(self):
        pass


class Cell:

    def __init__(self, name, x, y, color):  # Да, я хочу знать всё и даже больше
        self.name = name  # a1 (0:0)
        self.x = x  # строка, буквы
        self.y = y  # столбец, цифры
        self.color = color  # 0 - black/1 - white
        self.checker = 0  # 2 - pass/3 - black/4 - white
        self.queen = 0  # 5 - black/6 - white queen?


class Board:

    def __init__(self):
        c = Cell  # Для удобства вмещения массива
        self.board = [
            [c('h1', 0, 0, 1), c('g1', 0, 1, 0), c('f1', 0, 2, 1), c('e1', 0, 3, 0), c('d1', 0, 4, 1), c('c1', 0, 5, 0), c('b1', 0, 6, 1), c('a1', 0, 7, 0)],
            [c('h2', 1, 0, 0), c('g2', 1, 1, 1), c('f2', 1, 2, 0), c('e2', 1, 3, 1), c('d2', 1, 4, 0), c('c2', 1, 5, 1), c('b2', 1, 6, 0), c('a2', 1, 7, 1)],
            [c('h3', 2, 0, 1), c('g3', 2, 1, 0), c('f3', 2, 2, 1), c('e3', 2, 3, 0), c('d3', 2, 4, 1), c('c3', 2, 5, 0), c('b3', 2, 6, 1), c('a3', 2, 7, 0)],
            [c('h4', 3, 0, 0), c('g4', 3, 1, 1), c('f4', 3, 2, 0), c('e4', 3, 3, 1), c('d4', 3, 4, 0), c('c4', 3, 5, 1), c('b4', 3, 6, 0), c('a4', 3, 7, 1)],
            [c('h5', 4, 0, 1), c('g5', 4, 1, 0), c('f5', 4, 2, 1), c('e5', 4, 3, 0), c('d5', 4, 4, 1), c('c5', 4, 5, 0), c('b5', 4, 6, 1), c('a5', 4, 7, 0)],
            [c('h6', 5, 0, 0), c('g6', 5, 1, 1), c('f6', 5, 2, 0), c('e6', 5, 3, 1), c('d6', 5, 4, 0), c('c6', 5, 5, 1), c('b6', 5, 6, 0), c('a6', 5, 7, 1)],
            [c('h7', 6, 0, 1), c('g7', 6, 1, 0), c('f7', 6, 2, 1), c('e7', 6, 3, 0), c('d7', 6, 4, 1), c('c7', 6, 5, 0), c('b7', 6, 6, 1), c('a7', 6, 7, 0)],
            [c('h8', 7, 0, 0), c('g8', 7, 1, 1), c('f8', 7, 2, 0), c('e8', 7, 3, 1), c('d8', 7, 4, 0), c('c8', 7, 5, 1), c('b8', 7, 6, 0), c('a8', 7, 7, 1)]
        ]

    def fill(self, color, place):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if (self.board[i][j].name == place and
                        self.board[i][j].color == 0 and
                        self.board[i][j].checker == 0):
                    self.board[i][j].name = place
                    self.board[i][j].checker = color

    def peek(self, color):  # САМЫЙ ВАЖНЫЙ КОМПОНЕНТ
        # обновление диагоналей TODO: диагонали на алгоритм; алгоритм на проверку хода
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

        # battle_flag = 1
        checkers = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                checkers.append(self.board[i][j].checker)
        if len(set(checkers)) == 2:
            if 3 in set(checkers):  # Выиграли черные?
                return 0
            else:  # Выиграли белые?
                return 1

        if color == 1:
            # ЧЕРНЫЕ БИТЬ ВПЕРЕД
            pos_0 = ''
            pos_1 = ''
            for i in diagonals:
                for j in i:
                    if pos_0 == 3 and pos_1 == 4 and j.checker == 2:
                        return 'Надо бить', color
                    pos_0 = pos_1
                    pos_1 = j

            # ЧЕРНЫЕ БИТЬ НАЗАД
            pos_0 = ''
            pos_1 = ''
            for i in diagonals:
                for j in reversed(i):
                    if pos_0 == 3 and pos_1 == 4 and j.checker == 2:
                        return 'Надо бить', color
                    pos_0 = pos_1
                    pos_1 = j

            # ЧЕРНЫЕ ходы
            pos_0 = ''
            for i in diagonals:
                for j in i:
                    if pos_0 == 3 and j == 2:
                        return 'Ходы есть! черные', color
                    pos_0 = j

        elif color == 2:
            # БЕЛЫЕ БИТЬ НАЗАД
            pos_0 = ''
            pos_1 = ''
            for i in diagonals:
                for j in i:
                    if pos_0 == 4 and pos_1 == 3 and j.checker == 2:
                        return 'Надо бить', color
                    pos_0 = pos_1
                    pos_1 = j

            # БЕЛЫЕ БИТЬ ВПЕРЕД
            pos_0 = ''
            pos_1 = ''
            for i in diagonals:
                for j in reversed(i):
                    if pos_0 == 4 and pos_1 == 3 and j.checker == 2:
                        return 'Надо бить', color
                    pos_0 = pos_1
                    pos_1 = j

            # БЕЛЫЕ ходы
            pos_0 = ''
            for i in diagonals:
                for j in reversed(i):
                    if pos_0 == 3 and j == 2:
                        return 'Ходы есть! белые', color
                    pos_0 = j

        return 'нет ходов', color

    def move(self, color, pos_0, pos_1):
        self.board[pos_1.x][pos_1.y].checker = color  # Заполнение
        self.board[pos_0.x][pos_0.y].checker = 2  # Очищение

    def battle(self, color, pos_0, pos_1, pos_m):
        self.board[pos_1.x][pos_1.y].checker = color  # Заполнение
        self.board[pos_0.x][pos_0.y].checker = 2  # Очищение
        self.board[pos_m.x][pos_m.y].checker = 2  # Снятие шашки

    def check(self, color, command):
        pos_0, pos_1 = self.parse(color, command)
        if Board().battle_flag:  # Проврка обязательного боя
            pos_m = self.battle_check(color, pos_0, pos_1)
            if pos_m:
                self.battle(color, pos_0, pos_1, pos_m)
            else:
                raise ValueError('Надо бить!')
        else:
            if self.move_check(color, pos_0, pos_1):
                self.move(color, pos_0, pos_1)
            else:
                raise ValueError('Так нельзя ходить!')

    def parse(self, color, command):
        pos_0 = ''  # Начальная клетка
        pos_1 = ''  # Конечная
        command = [i for i in command.split('->') if i]
        if len(command) == 2:  # безопасность 1
            # Получение позиций
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.board[i][j].color == color and self.board[i][j].name == command[0]:
                        pos_0 = self.board[i][j]
                    elif self.board[i][j].color == color and self.board[i][j].name == command[1]:
                        pos_1 = self.board[i][j]
            if pos_0 and pos_1:  # безопасность 2
                return pos_0, pos_1
            else:
                raise ValueError('Не найдена клетка начала или конца')
        raise ValueError('Неверная команда')

    @staticmethod
    def move_check(color, pos_0, pos_1):  # Сюда не дойдут команды, выходящие за поле
        # проверка хода белого
        if color and abs(pos_0.x - pos_1.x) == 1 and pos_0.y + 1 == pos_1.y and not pos_1.cheker:
            return True
        # проверка хода черного
        elif not color and abs(pos_0.x - pos_1.x) == 1 and pos_0.y - 1 == pos_1.y and not pos_1.checker:
            return True
        return False

    @staticmethod
    def battle_check(color, pos_0, pos_1):  # Сюда не дойдут команды, выходящие за поле
        pos_m = Cell('tmp', 'tmp', 'tmp', 'tmp')
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
        # проверка хода-боя белого
        if color and abs(pos_0.x - pos_1.x) == 2 and abs(pos_0.y - pos_1.y) == 2 and not pos_1.checker:
            return pos_m
        # проверка хода-боя черного
        if not color and abs(pos_0.x - pos_1.x) == 2 and abs(pos_0.y - pos_1.y) == 2 and not pos_1.checker:
            return pos_m
        return False

    def render(self):
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


class SR:  # Smart Random

    def __init__(self):
        pass


board = Board()
board.board[0][1].checker = 4
board.board[0][3].checker = 4
board.board[0][5].checker = 4
board.board[3][0].checker = 3
board.render()
