# import sqlite3
# db=sqlite3.connect('students')
# pointer=db.cursor()
# # pointer.execute("create table goldenbat (id int,name text,age int)")
# pointer.execute("insert into goldenbat values(1,'santosh',20),(2,'santosh',20)")
# pointer.execute("select*from goldenbat")
# data = pointer.fetchall()
# single_data = pointer.fetchall()
# print(single_data)