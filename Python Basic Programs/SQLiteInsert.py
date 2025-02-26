import sqlite3

conn = sqlite3.connect("sqlite.db")

Insert = '''
     Insert into Student Values (102,'Prakash','FY Btech','prak@gmail.com')
     Insert into Fee Values (1,1000)
     Insert into Fee Values (2,1000)
     Insert into Fee Values (3,3000)
     Insert into Fee Values (4,3000)

     
'''

conn.executemany(Insert)
conn.commit()
conn.close()
