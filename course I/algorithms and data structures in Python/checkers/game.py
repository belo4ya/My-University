from gameplay import GamePlay
from tools import *


class Game:

    def __init__(self):
        pass

    def start(self):
        print('|--- ШАШКИ 20_20 (6x6) ---|\n')
        while True:
            print('!start - Начать игру\n!manual - Правила игры\n!config - Настройки\n!exit - Выход\n')
            command = input_()
            if command == '!start':
                GamePlay().start()
            elif command == '!manual':
                self.manual()
            elif command == '!config':
                self.config()
            elif command == '!exit':
                load('Выход')
                break
            else:
                incorrect_()

    def manual(self):
        print('\n|--------------- ПРАВИЛА ИГРЫ ---------------|\n')
        print('\n1. Игроки выберают цвет фигур, за который будут играть')
        print('\n2. Игроки по очереди рассавляют фигуры с помощью команд вида:')
        print('h1, e4... Не допускается размещение фигур на первой линии противника')
        print('\n3. После того, как на поле присутствуют 12 фигур, 6 - белых и 6 черных,')
        print('начинается игра по правилам русских шашек*')
        print('\n* Нет возможности комбо-боя. Получение дамки означает победу')
        print('GL HF\n\n')

    def config(self):
        print('0 - Выбор доски\n1 - Выбор режима\n!exit - Назад\n')
        while True:
            command = input_()
            if command == '0':
                print('*Цветная доска в разработке*')
                break
            elif command == '1':
                print('*Полная версия игры возможно появится позже*')
                print('*Режим игры "на двоих" возможно появится позже*')
                break
            elif command == '!exit':
                load('Выход')
                break
            else:
                incorrect_()


if __name__ == '__main__':
    new_game = Game()
    new_game.start()
