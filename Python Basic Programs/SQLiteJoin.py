import sqlite3

conn = sqlite3.connect("sqlite.db")

data = conn.execute("Select * from Student as s inner join Fee as f where s.id = 101")
for i in data:
    print(i)