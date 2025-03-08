import sqlite3

conn = sqlite3.connect("sqlite.db")

id = int(input("Enter the Student ID to Delete : "))
conn.execute("Delete From Student where id ="+str(id))
conn.commit()
conn.close()