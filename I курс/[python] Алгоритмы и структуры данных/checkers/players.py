from tools import *
from logic import Cell
import random


class SmartRandom:
    speech = ['Виу', 'Пиу', 'Пииии', 'Вжик', 'Уи-уи', 'Уиу-иии', 'И-у-ии-уу-и']

    def __init__(self, color, board):
        self.color = color
        self.board = board.board
        self.diagonals = self.get_diagonals()
        self.rows = self.get_rows()
        self.names = self.get_names()

    def step(self):
        """
        Создаёт ощущение размышлений
        :return: None
        """
        print('\nХодит робот')
        load(random.choice(SmartRandom.speech))

    def placement(self):
        """
        Наполнение доски фигурами:
        - сначала защищаются "позиции полей-дамок", если им что-то угрожает;
        - иначе, старается поставить свои фигуры ближе к "позициям полей-дамок"
        противника, при этом не подставляясь под бой.

        Выборка происходит с небольшим рассеиванием

        :return: Имя ячейки: str, в которую ставить фигуру
        """
        commands = self.defence()
        if commands:
            return random.choice(commands)
        else:
            commands = self.attack()
            return random.choice(commands)

    def move(self):
        """
        Движение фигур:
        - бьет в дамки;
        - иначе, старается бить вперед;
        - иначе, бьет назад;
        - иначе, ходит:
            - в дамку;
            - иначе, ходит ближе к дамке:
                - сначал, не подставляясь под бой;
                - иначе, не подставляясь под бой вперед;

        Выборка происходит с небольшим рассеиванием

        :return: Команда хода: str
        """
        commands = self.strike()
        if commands:
            return random.choice(commands)
        else:
            commands = self.win()
            if commands:
                return random.choice(commands)
            else:
                commands = self.shift()
                if commands:
                    return random.choice(commands)

    def get_diagonals(self):
        """
        Получение информации о диагоналях доски
        :return: Список диагоналей: list
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

        if self.color == 4:
            return diagonals
        return [list(reversed(i)) for i in diagonals]

    def get_rows(self):
        """
        Получение информации о линиях доски
        :return: Список линий: list
        """
        row1 = [i for i in self.board[0] if i.name in NAMES]
        row2 = [i for i in self.board[1] if i.name in NAMES]
        row3 = [i for i in self.board[2] if i.name in NAMES]
        row4 = [i for i in self.board[3] if i.name in NAMES]
        row5 = [i for i in self.board[4] if i.name in NAMES]
        row6 = [i for i in self.board[5] if i.name in NAMES]
        row7 = [i for i in self.board[6] if i.name in NAMES]
        row8 = [i for i in self.board[7] if i.name in NAMES]

        rows = [row1, row2, row3, row4, row5, row6, row7, row8]
        if self.color == 4:
            return rows
        return list(reversed(rows))

    def get_names(self):
        """
        Список доступных для хода имен
        :return: Список имен: list
        """
        if self.color == 4:
            return NAMES
        return list(reversed(NAMES))

    def defence(self):
        """
        Генерация возможных ходов, для защиты "полей-дамок"
        :return: список возможных ходов: list
        """
        steps = []
        for i in self.rows[1]:
            if abs(i.checker - self.color) == 1 and i.checker != 2:
                for j in self.rows[0]:
                    if abs(j.x - i.x) == 1 and j.checker == 2:
                        steps.append(j.name)
        return steps

    def attack(self):
        """
        Генерация ближайших к "полям-дамкам" противника ходов,
        учитывая возможность боя с помощью оценки
        :return: список возможных ходов: list
        """
        steps = {}
        for i in range(6, 0, -1):
            for j in self.rows[i]:
                if j.checker == 2:
                    score = i * 100
                    steps[j] = score
                    check_next = self.check_battle_next(j)
                    if check_next:
                        steps[j] += check_next
                    else:
                        check_prev = self.check_battle_prev(j)
                        if check_prev:
                            steps[j] += check_prev
        steps = sorted(steps, key=lambda x: steps.get(x), reverse=True)
        steps = [i.name for i in steps]
        return steps[:3] + steps[:4] + steps[:4] + steps[:5] + steps[:7] + steps[:9]

    def check_battle_next(self, step):
        """
        Возможный бой противником вперед; оценка
        :param step: потенциальный ход
        :return: -210 - оценка, False - невозможность боя для противника
        """
        nullifier = Cell('', '', '', '')
        for i in self.diagonals:
            pos_0 = nullifier
            pos_1 = nullifier
            for j in i:
                if pos_1 == step and pos_0.checker != self.color and pos_0.checker != 2 and j.checker == 2:
                    return -210
                pos_0 = pos_1
                pos_1 = j
        return False

    def check_battle_prev(self, step):
        """
        Возможный бой противником назад; оценка
        :param step: потенциальный ход
        :return: -100 - оценка, False - невозможность боя для противника
        """
        nullifier = Cell('', '', '', '')
        for i in self.diagonals:
            pos_0 = nullifier
            pos_1 = nullifier
            for j in list(reversed(i)):
                if pos_1 == step and pos_0.checker != self.color and pos_0.checker != 2 and j.checker == 2:
                    return -100
                pos_0 = pos_1
                pos_1 = j
        return False

    def strike(self):
        """
        Обязательный бой
        Оценка хода: бой в дамки, бой вперед, бой назад
        :return: список возможных ходов: list
        """
        steps = []
        nullifier = Cell('', '', '', '')
        for i in self.diagonals:
            pos_0 = nullifier
            pos_1 = nullifier
            for j in list(reversed(i)):
                if pos_0.checker == self.color and pos_1.checker != 2 and pos_1.checker != self.color\
                        and j.checker == 2 and (j.name[-1] == '8' or j.name[-1] == '1'):
                    steps.append(pos_0.name + '->' + j.name)
                pos_0 = pos_1
                pos_1 = j
        if steps:
            return steps
        for i in self.diagonals:
            pos_0 = nullifier
            pos_1 = nullifier
            for j in list(reversed(i)):
                if pos_0.checker == self.color and pos_1.checker != 2\
                        and pos_1.checker != self.color and j.checker == 2:
                    steps.append(pos_0.name + '->' + j.name)
                pos_0 = pos_1
                pos_1 = j
        steps = steps * 4
        for i in self.diagonals:
            pos_0 = nullifier
            pos_1 = nullifier
            for j in i:
                if pos_0.checker == self.color and pos_1.checker != 2 \
                        and pos_1.checker != self.color and j.checker == 2:
                    steps.append(pos_0.name + '->' + j.name)
                pos_0 = pos_1
                pos_1 = j
        return steps

    def win(self):
        """
        Ход в дамки
        :return: список возможных ходов: list
        """
        steps = []
        nullifier = Cell('', '', '', '')
        for i in self.diagonals:
            pos_0 = nullifier
            for j in list(reversed(i)):
                if pos_0.checker == self.color and j.checker == 2 \
                        and (j.name[-1] == '8' or j.name[-1] == '1'):
                    steps.append(pos_0.name + '->' + j.name)
                pos_0 = j
        return steps

    def shift(self):
        """
        Простой ход
        Оценка хода: ход ближе к дамке без потенциального боя, с боем противником назад, с боем вперед
        :return: список возможных ходов: list
        """
        steps = {}
        nullifier = Cell('', '', '', '')
        for i in self.diagonals:
            pos_0 = nullifier
            for j in list(reversed(i)):
                if pos_0.checker == self.color and j.checker == 2:
                    if self.color == 4:
                        steps[pos_0.name + '->' + j.name] = [int(j.name[-1]) * 200, pos_0, j]
                    else:
                        steps[pos_0.name + '->' + j.name] = [9 - int(j.name[-1]) * 200, pos_0, j]
                pos_0 = j
        for i in steps.values():
            tmp = i[1].checker
            i[1].checker = 2
            score = self.check_battle_next(i[2])
            if score:
                i[0] += score
            else:
                score = self.check_battle_prev(i[2])
                if score:
                    i[0] += score
            i[1].checker = tmp
        steps = sorted(steps, key=lambda x: list(steps.get(x))[0], reverse=True)
        return steps[:1] + steps[:1] + steps[:1] + steps[:2] + steps[:2] + steps[:3]


class Player:

    def __init__(self):
        self.color = self.choice_color()

    def choice_color(self):
        print('\nВыберите цвет шашек:\n0 - черные\n1 - белые\n')
        while True:
            color = input_()
            if color == '0' or color == '1':
                return int(color) + 3
            incorrect_()

    def step(self):
        print('\nВаш ход:\n')

    def placement(self):
        """
        Получение хода-заполнения от пользователя с фильтрацией
        :return: Ход: str
        """
        while True:
            place = input_()
            if self.color == 4 and place in NAMES[:-4]:
                return place
            elif self.color == 3 and place in NAMES[4:]:
                return place
            incorrect_()

    def move(self):
        """
        Получение хода от пользователя с фильтрацией
        :return: Ход: str
        """
        while True:
            command = input_()
            try:
                example = command.split('->')
            except (ValueError, TypeError):
                example = ''
            if len(example) == 2 and example[0] in NAMES and example[1] in NAMES:
                return command
            else:
                incorrect_()
