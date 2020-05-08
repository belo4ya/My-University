class LogLog:

    def __init__(self):
        self.log = ''
        self.row = 1

    def write(self, s):
        self.log += str(self.row) + '. ' + s + '\n'
        self.row += 1

    def export(self):
        pass
