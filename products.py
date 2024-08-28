import mysql.connector as sql

conn = sql.connect(host='localhost', user='root', passwd='123456', database='Aditya_Electronics')
if conn.is_connected():
    print('successfully connected')
c1 = conn.cursor()

c1.execute(
    "create table products(Product_name varchar(55),Product_no bigint primary key,Stock varchar(10),"
    "Price_per varchar(1000))")
print("Products table created")

c1.execute("insert into products values ('Switch',1,'81','50')")
c1.execute("insert into products values ('mouse',2,'45','650')")
c1.execute("insert into products values ('Water motor',3,'20','15000')")
c1.execute("insert into products values ('Hammer',4,'198','250')")
c1.execute("insert into products values ('Screw',5,'4000','15')")
c1.execute("insert into products values ('Wire(in meters)',6,'100','200')")
c1.execute("insert into products values ('Switch board',7,'200','150')")
c1.execute("insert into products values ('Land motor',8,'25','10000')")
conn.commit()
print("updated  successfully")
