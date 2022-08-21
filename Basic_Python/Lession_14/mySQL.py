import mysql.connector

myconn = mysql.connector.connect(host="localhost",

user="root",

passwd="root")

print('Connected to MySQL Database')

cur = myconn.cursor()

cur.execute("show databases")

for row in cur:

    print(row)

myconn.close()

#==========
myconn = mysql.connector.connect(host="localhost",

user="root",

passwd="root")

cur.execute("create database testdb")

cur.execute("show databases")

for row in cur:

    print(row)

myconn.close()