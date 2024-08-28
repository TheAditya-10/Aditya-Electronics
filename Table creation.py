import mysql.connector as sql

conn = sql.connect(host='localhost', user='root', passwd='123456', database='Aditya_Electronics')

if conn.is_connected():
    print('successfully connected')
c1 = conn.cursor()

c1.execute(
    "CREATE TABLE employee(Emp_code int(4)primary key ,Emp_name varchar(25) ,"
    "Password int(8)not null,Purchased bigint)")
print("EMPLOYEE table created")

c1.execute(
    "create table Users(user_code int(4)primary key,user_name varchar(25),password varchar(25)not null,"
    "city varchar(25),ph_no bigint)")
print("Users table created")
