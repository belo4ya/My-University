from config import *


class SmartRandom:

    def __init__(self, color):
        self.color = color

    def placement(self):
        pass

    def step(self):
        pass


class Player:

    def __init__(self):
        self.color = self.choice_color()

    @staticmethod
    def choice_color():
        print('Выберите цвет шашек:\n0 - черные\n1 - белые')
        while True:
            color = input_()
            if color == '0':
                print('Вы играете за черных')
                return color
            elif color == '1':
                print('Вы играете за белых')
                return color
            incorrect_()

    def placement(self):
        pass

    def step(self):
        pass
