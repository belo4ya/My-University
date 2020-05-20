def get_x():
    while True:
        try:
            return float(input('x = '))
        except ValueError:
            print('Неверный ввод!')


def get_eps():
    while True:
        try:
            value = float(input('eps = '))
            if value > 0:
                return value
        except ValueError:
            print('Неверный ввод!')
        print('Неверный ввод!')


def get_n():
    while True:
        try:
            value = int(input('n = '))
            if value > 0:
                return value
        except ValueError:
            print('Неверный ввод!')
        print('Неверный ввод!')
