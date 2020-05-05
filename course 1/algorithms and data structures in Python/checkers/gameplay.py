from players import Player, SmartRandom
from logic import Board
from config import *


class GamePlay:

    def __init__(self):
        self.player_1 = Player()
        self.player_2 = SmartRandom(self.get_color())
        self.board = Board()

    def get_color(self):
        if self.player_1.color == '1':
            return '0'
        return '1'

    def start(self):
        pass

    def game(self):
        pass

    def restart(self):
        pass

    def end(self):
        pass

    def log(self):
        pass


a = GamePlay()
