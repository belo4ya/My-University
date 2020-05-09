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
            print('\nВы играете за БЕЛЫХ!\n')
            k = 1  # Определяет очередность хода
        else:
            print('\nВы играете за ЧЕРНЫХ!\n')
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
        winner, log_ = self.game(k)
        if winner == 'w4' and self.player_1.color == 4 or winner == 'w3' and self.player_1.color == 3:
            print('\n  |' + 47*'*' + '|')
            print('  |------------------- ПОБЕДА! -------------------|')
            print('  |' + 47 * '*' + '|')
        else:
            print('\n  |----- Вы проиграли. Повезет в другой раз! -----|\n')
        try:
            self.log(log_)
        except IndexError:
            self.note.write('Случилась партия без ходов')
        self.end()

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
                print('Робот:', place)
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
        status = self.board.peek(color)
        cmd = ''
        command = ''
        while status != 'w3' or status != 'w4':
            cmd += command + ' '
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
                    return status, cmd[1:-1]
            else:  # робот
                color = self.player_2.color
                status = self.board.peek(color)
                if status != 'w3' and status != 'w4':
                    self.player_2.step()
                    command = self.player_2.move()
                    print('Робот:', command)
                    self.board.check(color, command)
                    self.board.render()
                else:
                    return status, cmd[1:-1]
            status = self.board.peek(color)
            k += 1
        return status, cmd[1:-1] + ' ' + command

    def end(self):
        while True:
            print('\n!log - показать журнал игры\n!export - сохранить журнал игры'
                  '\n!exit - вернуться в главное меню\n')
            command = input_()
            if command == '!log':
                print('\nЖУРНАЛ ИГРЫ\n')
                print(self.note.log)
            elif command == '!export':
                self.note.export()
                print('\nЖурнал сохранен в текущей директории с именем game_log.txt')
            elif command == '!exit':
                load('Выход')
                return
            else:
                incorrect_()

    def log(self, s: str):
        """Преобразование команд в необходимый формат и запись в журнал игры"""
        c = ''

        def reformat(c):
            tmp = c.split('->')
            if abs(int(tmp[0][-1]) - int(tmp[1][-1])) == 2:
                return ':'.join(tmp)
            return '-'.join(tmp)

        if len(s) == 6:
            self.note.write(reformat(s) + 'X')
            return

        s = s.split(' ')
        for i in range(len(s) - 1):
            if i % 2 == 0:
                c += reformat(s[i]) + ' ' + reformat(s[i + 1]) + ' '
        if len(s) % 2:
            c += reformat(s[-1]) + ' '
        c = c[:-1] + 'X'
        c = c.split(' ')
        for i in range(len(c) - 1):
            if i % 2 == 0:
                self.note.write(c[i] + ' ' + c[i+1])
        if len(c) % 2:
            self.note.write(c[-1])
