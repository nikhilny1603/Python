import sqlite3

conn = sqlite3.connect("sqlite.db")

data = conn.execute("Select * from Student where name like '%P%' ")

for n in data:
    print(n)