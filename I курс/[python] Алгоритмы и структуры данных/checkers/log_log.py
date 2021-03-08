from datetime import datetime


class LogLog:

    def __init__(self):
        self.log = ''
        self.row = 1

    def write(self, s):
        self.log += str(self.row) + '. ' + s + '\n'
        self.row += 1

    def export(self):
        with open('game_log.txt', 'w') as f:
            f.write('ИГРА ' + str(datetime.strftime(datetime.now(), '%H:%M %d.%m.%Y')) + '\n\n')
            f.write(self.log)
