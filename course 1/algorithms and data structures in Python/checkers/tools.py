import time

NAMES = [
    'b1', 'd1', 'f1', 'h1',
    'a2', 'c2', 'e2', 'g2',
    'b3', 'd3', 'f3', 'h3',
    'a4', 'c4', 'e4', 'g4',
    'b5', 'd5', 'f5', 'h5',
    'a6', 'c6', 'e6', 'g6',
    'b7', 'd7', 'f7', 'h7',
    'a8', 'c8', 'e8', 'g8',
]


def input_():
    return str(input('>>> '))


def incorrect_():
    print('Некорректный ввод. Попробуйте снова!\n')


def load(s):
    print(s, end='')
    for i in range(3):
        time.sleep(0.5)
        print('.', end='')
    print('\n')
    time.sleep(0.3)
