from tools import *
from logic import Board, Cell
import random


class SmartRandom:
    speech = ['Виу', 'Пиу', 'Пииии', 'Вжик', 'Уи-уи', 'Уиу-иии', 'И-у-ии-уу-и']

    def __init__(self, color, board):
        self.color = color
        self.board = board.board
        self.diagonals = self.get_diagonals()
        self.rows = self.get_rows()
        self.names = self.get_names()

    @staticmethod
    def step():
        print('\nХодит компьютер')
        load(random.choice(SmartRandom.speech))

    def placement(self):
        commands = self.defence()
        if commands:
            return random.choice(commands)  # щепотка рандома для интереса
        else:
            commands = self.attack()
            return random.choice(commands)  # щепотка рандома для интереса

    def move(self):
        pass
        # Проверить ходы в дамку
        # Проверить бои
        # Проверить ходы ближе к дамке

    # Здесь начинается УМ (чуть-чуть)
    def get_diagonals(self):
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
        if self.color == 4:
            return NAMES
        return list(reversed(NAMES))

    def defence(self):
        # защита своих позиций
        steps = []
        for i in self.rows[1]:
            if abs(i.checker - self.color) == 1 and i.checker != 2:
                for j in self.rows[0]:
                    if abs(j.x - i.x) == 1 and j.checker == 2:
                        steps.append(j.name)
        return steps

    def attack(self):
        steps = {}
        for i in range(6, 0, -1):
            for j in self.rows[i]:
                if j.checker == 2:
                    score = i * 100
                    steps[j] = score
                    check_next = self.check_battle_next(j)
                    check_prev = self.check_battle_prev(j)
                    if check_next:
                        steps[j] += check_next
                    elif check_prev:
                        steps[j] += check_prev
        steps = sorted(steps, key=lambda x: steps.get(x), reverse=True)
        steps = [i.name for i in steps]
        return steps[:7]

    def check_battle_next(self, step):
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
        pass

    def win(self):
        pass


class Player:

    def __init__(self):
        self.color = self.choice_color()

    @staticmethod
    def choice_color():
        print('Выберите цвет шашек:\n0 - черные\n1 - белые\n')
        while True:
            color = input_()
            if color == '0' or color == '1':
                return int(color) + 3
            incorrect_()

    @staticmethod
    def step():
        print('\nВаш ход:\n')

    def placement(self):
        while True:
            place = input_()
            if self.color == 4 and place in NAMES[:-4]:
                return place
            elif self.color == 3 and place in NAMES[4:]:
                return place
            incorrect_()

    def move(self):
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


if __name__ == '__main__':
    board = Board()
    color = 3
    AI = SmartRandom(color, board)
    board.fill(4, 'd7')
    board.fill(4, 'c4')
    board.render()
    board.fill(color, AI.placement())
    board.fill(color, AI.placement())
    board.fill(color, AI.placement())
    board.render()
