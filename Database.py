#!usr/bin/python3

import mysql.connector as mysql 

#connect database
conn=mysql.Connect(user='root',password='root',database='kishor',host='localhost')


if conn.is_connected():
	print("database is connected successfully")
else :
	print("something is wrong")

# preparing the cursor object using cursor() method

cursor=conn.cursor()

#query  

query="insert into user(name,passwrd,email) values('karan','1234','karan@gmail.com')"
try:
	cursor.execute(query)
	conn.commit()
	#out=cursor.fetchall()
	#print(out)
except Exception as e:
	print(e)
	conn.rollback()








