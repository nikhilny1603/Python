import sqlite3

conn = sqlite3.connect("sqlite.db")

conn.execute('''
             Create Table Student (
                 id int Auto_Increment Primary Key,
                 name Varchar(50),
                 class Varchar(10),
                 email Varchar(30)
             )
             Create Table Fee (
                 fid int Auto_Increment Primary Key,
                 amount int
             )
             ''')

conn.close()