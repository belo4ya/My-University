class LogLog:

    def __init__(self):
        self.log = ''
        self.row = 1

    def __repr__(self):
        print(self.log)

    def __str__(self):
        print(self.log)

    def write(self, s):
        self.log += str(self.row) + '.' + s + '\n'
        self.row += 1

    def export(self):
        pass
