import mysql.connector as sql

conn = sql.connect(host='localhost', user='root', passwd='123456')
c1 = conn.cursor()
c1.execute("create database Aditya_Electronics")
print("Data Base Created")
