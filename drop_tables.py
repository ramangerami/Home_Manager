import sqlite3

conn = sqlite3.connect('homes.sqlite')

c = conn.cursor()
c.execute('''
          DROP TABLE homes
          ''')

conn.commit()
conn.close()
