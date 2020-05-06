from tools import *
import random


class SmartRandom:
    speech = ['Виу', 'Пиу', 'Пииии', 'Вжик', 'Уи-уи', 'Уиу-иии']

    def __init__(self, color, board):
        self.color = color
        self.board = board

    @staticmethod
    def step():
        print('\nХодит компьютер')
        load(random.choice(SmartRandom.speech))

    def placement(self):
        if self.color == 3:
            for i in range(len(self.board.board)):
                for j in range(len(self.board.board)):
                    if self.board.board[i][j].name in NAMES[4:8] and self.board.board[i][j].checker == 4:
                        pass
        else:
            pass

    def move(self):
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
