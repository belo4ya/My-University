import openpyxl as opx

# Используемые файлы
FILE_1 = 'statements/statement_1.xlsx'
FILE_2 = 'statements/statement_2.xlsx'

# Используемые листы
SHT_NAME_1 = 'Python'
SHT_NAME_2 = 'Algorithms'
SHT_NAME_3 = 'Computerscience'
SHT_NAME_4 = 'Mathematics'

# Используемые заголовки
headers = ['Практика_1:Задания', 'Практика_1:Выполнено', 'Практика_1:Защищено',
           'Практика_1:Баллы', 'Практика_2:Задания', 'Практика_2:Выполнено',
           'Практика_2:Защищено', 'Практика_2:Баллы', 'Практика_3:Задания',
           'Практика_3:Выполнено', 'Практика_3:Защищено', 'Практика_3:Баллы',
           'Тесты:1', 'Тесты:2', 'Тесты:3', 'Контрольная работа', 'Экзамен']

# Используемые учителя
teachers = {
    'Макрушин Сергей Вячеславович': SHT_NAME_1,
    'Петросов Давид Арегович': SHT_NAME_2,
    'Медведев Александр Валерьевич': SHT_NAME_3,
    'Щиголев Владимир Викторович': SHT_NAME_4
}

# Ширина колонок
wb = opx.load_workbook(FILE_1, read_only=True)
sht = wb['Mathematics']

COL_1 = max([len(str(i[0].value)) for i in sht['A3:A26']])   # №
COL_2 = max([len(str(i[0].value)) for i in sht['B1:B26']])   # Студент
COL_3 = max([len(str(i[0].value)) for i in sht['C2:C26']])   # Задания
COL_4 = max([len(str(i[0].value)) for i in sht['D2:D26']])   # Выполнено
COL_5 = max([len(str(i[0].value)) for i in sht['E2:E26']])   # Защищено
COL_6 = max([len(str(i[0].value)) for i in sht['F2:F26']])   # Баллы
COL_3_6 = COL_3 + COL_4 + COL_5 + COL_6                      # Практика_N
COL_15 = max([len(str(i[0].value)) for i in sht['O2:O26']])  # 1
COL_16 = max([len(str(i[0].value)) for i in sht['P2:P26']])  # 2
COL_17 = max([len(str(i[0].value)) for i in sht['Q2:Q26']])  # 3
COL_15_17 = COL_15 + COL_16 + COL_17                         # Тесты
COL_18 = max([len(str(i[0].value)) for i in sht['R1:R26']])  # Контрольная работа, Экзамен
COL_19 = max([len(str(i[0].value)) for i in sht['S1:S26']])  # Итог
