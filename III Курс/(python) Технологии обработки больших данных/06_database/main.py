import sqlite3

con = sqlite3.connect('data/Chinook_Sqlite.sqlite')
cur = con.cursor()

cur.execute('SELECT name FROM sqlite_master WHERE type="table"')
print(cur.fetchall())

con.commit()
con.close()
