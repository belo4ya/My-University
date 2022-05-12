import openpyxl as opx
import config


class StatementError(Exception):
    def __init__(self, text):
        self.txt = text


class Statement:

    def __init__(self, file_name):
        self.file_name = file_name
        self.wb = opx.load_workbook(file_name)

    @staticmethod
    def get_line_by_name(sht, name):
        for i in sht['B3:B26']:
            if str(i[0].value) == name:
                return i[0].coordinate[1:]

    @staticmethod
    def get_column_by_value(sht, val):
        val = val.split(':')
        for i in ['C1', 'G1', 'K1', 'O1', 'R1']:
            if sht[i].value.lower() == val[0].lower():
                if i == 'C1':
                    for j in ['C2', 'D2', 'E2', 'F2']:
                        if sht[j].value.lower() == val[1].lower():
                            return sht[j].coordinate[:1]
                elif i == 'G1':
                    for j in ['G2', 'H2', 'I2', 'J2']:
                        if sht[j].value.lower() == val[1].lower():
                            return sht[j].coordinate[:1]
                elif i == 'K1':
                    for j in ['K2', 'L2', 'M2', 'N2']:
                        if sht[j].value.lower() == val[1].lower():
                            return sht[j].coordinate[:1]
                elif i == 'O1':
                    for j in ['O2', 'P2', 'Q2']:
                        if str(sht[j].value) == val[1]:
                            return sht[j].coordinate[:1]
                else:
                    return sht[i].coordinate[:1]

    @staticmethod
    def get_cell(sht, name, val):
        a = Statement.get_column_by_value(sht, val)
        b = Statement.get_line_by_name(sht, name)
        if a and b:
            return a + b

    @staticmethod
    def alignment(data, width):
        """Расчитывает кол-во отступов для выравнивания контента в таблице по центру"""
        space = (width + 2) - len(data)
        if space % 2:
            return space // 2 + 1, space // 2
        return space // 2, space // 2

    @staticmethod
    def header(sht):
        """Создает шапку таблицы"""
        len_of_table = config.COL_1 + config.COL_2 + 3 * config.COL_3_6 +\
                       3 * config.COL_15_17 + config.COL_18 + config.COL_19
        hdr = '+' + '-' * (len_of_table + 16 * 2) + '+\n'
        separator = ''

        cells_1 = {'A1': config.COL_1,
                   'B1': config.COL_2,
                   'C1': config.COL_3_6,
                   'G1': config.COL_3_6,
                   'K1': config.COL_3_6,
                   'O1': config.COL_15_17,
                   'R1': config.COL_18,
                   'S1': config.COL_19}
        cells_2 = {'A1': config.COL_1,
                   'B1': config.COL_2,
                   'C2': config.COL_3,
                   'D2': config.COL_4,
                   'E2': config.COL_5,
                   'F2': config.COL_6,
                   'G2': config.COL_3,
                   'H2': config.COL_4,
                   'I2': config.COL_5,
                   'J2': config.COL_6,
                   'K2': config.COL_3,
                   'L2': config.COL_4,
                   'M2': config.COL_5,
                   'N2': config.COL_6,
                   'O2': config.COL_15,
                   'P2': config.COL_16,
                   'Q2': config.COL_17,
                   'R1': config.COL_18,
                   'S1': config.COL_19}

        # Контент 1
        for i, j in cells_1.items():
            data = str(sht[i].value)
            space = Statement.alignment(data, j)
            if i in ['C1', 'G1', 'K1']:
                hdr += '|' + ' ' * (space[0] + 4) + data + ' ' * (space[1] + 5)
                separator += '|' + '-' * (space[0] + 4) + '-' * len(data) + '-' * (space[1] + 5)
            elif i == 'O1':
                hdr += '|' + ' ' * (space[0] + 3) + data + ' ' * (space[1] + 3)
                separator += '|' + '-' * (space[0] + 3) + '-' * len(data) + '-' * (space[1] + 3)
            else:
                hdr += '|' + ' ' * space[0] + data + ' ' * space[1]
                separator += '|' + '-' * space[0] + '-' * len(data) + '-' * space[1]

        hdr += '|\n' + separator + '|\n'
        separator = ''

        # Контент 2
        for i, j in cells_2.items():
            if i in ['A1', 'B1', 'R1', 'S1']:
                data = ' ' * len(str(sht[i].value))
            else:
                data = str(sht[i].value)
            space = Statement.alignment(data, j)
            hdr += '|' + ' ' * space[0] + data + ' ' * space[1]
            separator += '|' + '-' * space[0] + '-' * len(data) + '-' * space[1]

        hdr += '|\n' + separator + '|\n'
        return hdr

    @staticmethod
    def table(sht, name):
        """Создает таблицу"""
        hdr = Statement.header(sht)
        tbl = ''
        separator = ''
        cells_data = {
            'A': config.COL_1,
            'B': config.COL_2,
            'C': config.COL_3,
            'D': config.COL_4,
            'E': config.COL_5,
            'F': config.COL_6,
            'G': config.COL_3,
            'H': config.COL_4,
            'I': config.COL_5,
            'J': config.COL_6,
            'K': config.COL_3,
            'L': config.COL_4,
            'M': config.COL_5,
            'N': config.COL_6,
            'O': config.COL_15,
            'P': config.COL_16,
            'Q': config.COL_17,
            'R': config.COL_18,
            'S': config.COL_19,
        }

        def table_generator(j):
            if j.value:
                data = str(j.value)
            else:
                data = ' '
            space = Statement.alignment(data, cells_data[j.coordinate[0]])
            tbl = '|' + ' ' * space[0] + data + ' ' * space[1]
            separator = '|' + '-' * space[0] + '-' * len(data) + '-' * space[1]
            return tbl, separator

        if name:
            for i in sht['B3:B26']:
                if str(i[0].value) == name:
                    for j in sht[f'A{i[0].coordinate[1:]}:S{i[0].coordinate[1:]}'][0]:
                        new_table, new_separator = table_generator(j)
                        tbl += new_table
                        separator += new_separator
                    break
            tbl += '|\n' + separator + '|\n'
        else:
            for i in range(3, 27):
                for j in sht[f'A{i}:S{i}'][0]:
                    new_table, new_separator = table_generator(j)
                    tbl += new_table
                    separator += new_separator
                tbl += '|\n' + separator + '|\n'
                separator = ''
        return hdr + tbl

    def display_data(self, sheet_name, name=None):
        sht = self.wb[sheet_name.title()]
        tbl = Statement.table(sht, name)
        return tbl

    def edit_data(self, sheet_name, name, val, new_val=''):
        sht = self.wb[sheet_name]
        cell_coordinate = Statement.get_cell(sht, name, val)
        if not cell_coordinate:
            raise StatementError('Такого студента или параметра нет')
        else:
            sht[cell_coordinate] = new_val
            # Пересчет итога
            result = 0
            line = Statement.get_line_by_name(sht, name)
            for i in [sht['F'+line].value, sht['J'+line].value,
                      sht['N'+line].value, sht['O'+line].value,
                      sht['P'+line].value, sht['Q'+line].value,
                      sht['R'+line].value]:
                if i:
                    result += int(i)
            result_coordinate = 'S' + line
            sht[result_coordinate] = result

    def save_data(self):
        self.wb.save(self.file_name)


class Student:

    def __init__(self, statement, name):
        self.statement = statement
        self.name = name

    def peek(self, discipline=None):
        if discipline:
            tbl = self.statement.display_data(discipline, self.name)
            print('+' + '-' * len(discipline) + '+\n|' + discipline + '|\n' + '+' + '-' * len(discipline) + '+')
            print(tbl)
        else:
            for i in [config.SHT_NAME_1, config.SHT_NAME_2, config.SHT_NAME_3, config.SHT_NAME_4]:
                tbl = self.statement.display_data(i, self.name)
                print('+' + '-'*len(i) + '+\n|' + i + '|\n' + '+' + '-'*len(i) + '+')
                print(tbl)


class Teacher:

    DISCIPLINES = config.teachers

    def __init__(self, statement, name):
        self.statement = statement
        self.name = name
        self.discipline = Teacher.DISCIPLINES[name.title()]

    def peek(self):
        print(self.statement.display_data(self.discipline))

    def edit(self, name, val, new_val=''):
        self.statement.edit_data(self.discipline, name, val, new_val)

    def save(self):
        self.statement.save_data()
