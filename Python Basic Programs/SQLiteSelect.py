import sqlite3

conn = sqlite3.connect("sqlite.db")

data = conn.execute("Select * from Student ")
for i in data:
    print(i)
    
data = conn.execute("Select * from Student limit 0,1")
for i in data:
    print(i)