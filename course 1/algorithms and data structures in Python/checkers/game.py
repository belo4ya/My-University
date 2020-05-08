from gameplay import GamePlay
from tools import *


class Game:

    def __init__(self):
        self.game = GamePlay()

    def start(self):
        print('|--- ШАШКИ 20_20 (6x6) ---|\n')
        while True:
            print('!start - Начать игру\n!manual - Правила игры\n!config - Настройки\n!exit - Выход\n')
            command = input_()
            if command == '!start':
                self.game.start()
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
        pass

    def config(self):
        print('0 - Выбор доски\n1 - Выбор режима\n')

    def restart(self):
        self.game = GamePlay
        self.start()


if __name__ == '__main__':
    new_game = Game()
    new_game.start()
