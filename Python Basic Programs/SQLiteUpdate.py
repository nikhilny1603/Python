import sqlite3

conn = sqlite3.connect("sqlite.db")

conn.execute('''
             update Student set name = 'Nikhil Yadav' where id = 101
             ''')