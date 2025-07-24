import sqlite3

connection=sqlite3.connect("student.db")

#Create a cursor object to insert record,create table ,retrieve
cursor=connection.cursor()

table_info="""CREATE table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(10),SECTION CHAR(1),MARKS INT);"""

cursor.execute(table_info)
#Insert some records
cursor.execute('''INSERT Into STUDENT values('Krish','Data Science','A',90)''');
cursor.execute('''INSERT Into STUDENT values('Amal','English','B',50)''');
cursor.execute('''INSERT Into STUDENT values('Amala','Malayalam','C',40)''');
cursor.execute('''INSERT Into STUDENT values('Kabir','Electronics','A',30)''');
cursor.execute('''INSERT Into STUDENT values('Damu','Data Science','B',20)''');
#Display all records
print("The datas are:")

data=cursor.execute('''Select * From STUDENT''')

for row in data:
    print(row)

##Close the connection and run to see datas
connection.commit()
connection.close()

