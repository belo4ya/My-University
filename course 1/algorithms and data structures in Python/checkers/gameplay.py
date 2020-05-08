from players import Player, SmartRandom
from logic import Board
from log_log import LogLog
from tools import *


class GamePlay:

    def __init__(self):
        self.player_1 = None
        self.player_2 = None
        self.board = Board()
        self.note = LogLog()

    def get_color(self):
        if self.player_1.color == 4:
            return 3
        return 4

    def start(self):
        self.player_1 = Player()
        self.player_2 = SmartRandom(self.get_color(), self.board)
        if self.player_1.color == 4:
            print('Вы играете за БЕЛЫХ!\n')
            k = 1  # Определяет очередность хода
        else:
            print('Вы играете за ЧЕРНЫХ!\n')
            k = 0  # Определяет очередность хода
        load('loading')
        print('x - Пустые черные клетки\nБ - белая шашка\nЧ - черная шашка\n'
              '\nh1 - поставить шашку в клетку h1'
              '\nb1->c2 - ход из клетки b1 в клетку c2\n'
              'd3->f5 - бой из клетки d3 через клетку e4 в клетку f5\n')
        print('Всё понятно?\n')
        input_()
        load('\nЗагружаю доску')
        self.board.render()
        print('  |----------- Давайте расставим шашки -----------|\n')
        self.fill(k)
        self.game(k)

    def fill(self, k):

        def queue(self, k):
            if k % 2:  # человек
                self.player_1.step()
                place = self.player_1.placement()
                while not self.board.fill(self.player_1.color, place):
                    incorrect_()
                    place = self.player_1.placement()
            else:  # робот
                self.player_2.step()
                place = self.player_2.placement()
                self.board.fill(self.player_2.color, place)
            k += 1
            self.board.render()
            return k

        if k == 1:
            while k != 13:
                k = queue(self, k)
        else:
            while k != 12:
                k = queue(self, k)

    def game(self, k):
        print('\n  |----------------- Начало игры -----------------|\n')
        color = 4
        cmd_black = ''
        cmd_white = ''
        status = self.board.peek(color)
        while status != 'w3' or status != 'w4':
            if k % 2:  # человек
                color = self.player_1.color
                status = self.board.peek(color)
                if status != 'w3' and status != 'w4':
                    self.player_1.step()
                    command = self.player_1.move()
                    step = self.board.check(color, command)
                    if step == 1:
                        self.board.render()
                    elif step == 0:
                        while step != 1:
                            incorrect_()
                            command = self.player_1.move()
                            step = self.board.check(color, command)
                        self.board.render()
                    elif isinstance(step, tuple):
                        while step != 1:
                            try:
                                print(f'Нужно бить! Подсказка: {step[1]}')
                            except TypeError:
                                incorrect_()
                            command = self.player_1.move()
                            step = self.board.check(color, command)
                        self.board.render()
                else:
                    print(status, 'Из белых')
                    return
            else:  # робот
                color = self.player_2.color
                status = self.board.peek(color)
                if status != 'w3' and status != 'w4':
                    self.player_2.step()
                    command = self.player_2.move()
                    self.board.check(color, command)
                    self.board.render()
                else:
                    print(status, 'Из черных')
                    return
            status = self.board.peek(color)
            k += 1
        print(status, 'Общий')
        return

    def record_format(self, s: str):
        if s:
            tmp = s.split('->')
            if abs(int(tmp[0][-1]) - int(tmp[1][-1])) == 2:
                return ':'.join(tmp)
            return '-'.join(tmp)
        return s

    def log(self, s: str):
        self.note.write(s)
        print(self.note.log)
