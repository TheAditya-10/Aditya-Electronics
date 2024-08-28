import datetime

import mysql.connector as sql

conn = sql.connect(host='localhost', user='root', passwd='123456', database='Aditya_Electronics')
c1 = conn.cursor()
t_date = datetime.date.today()
t_time = datetime.datetime.now()
print("DATE:", t_date.day, "/", t_date.month, "/", t_date.year, "TIME:", t_time.hour, ":", t_time.minute)
print("Welcome To Aditya Electronics Shop")
print("1.Purchase Items")
print("2.Stock")
print("3.Exit")
choice = int(input("Enter the Choice - "))
if choice == 1:
    v_product_no = int(input("Enter the Product Number : "))
    if v_product_no == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8:
        c1.execute("select Product_name,Stock,Price_per from products where Product_no=" + str(v_product_no))
        data = c1.fetchall()
        for row in data:
            print("Available Stock Details ")
            print("        Product name:", row[0])
            print("               Stock:", row[1])
            print("Price per product Rs:", row[2])
            conn.commit()
            print("Do you want to buy this item:")
            print("1.Yes")
            print("2.No")
            ch = int(input("Enter the Choice - "))
            if ch == 1:
                q = int(input("enter how much do you need="))
                g = int(row[2]) * q
                print("The amount is Rs:", g)
                print("Do you want to continue:")
                print("1.Yes")
                print("2.No")
                cho = int(input("Enter the Choice - "))
                if cho == 1:
                    c1.execute("update products set Stock=Stock- " + str(q) + " where Product_no=" + str(v_product_no))
                    print("Items purchased successfully")
                    conn.commit()
                    print("Thank you")
                    print("Any kind of bulk or small orders of electronic items contact Aditya Electronics shop")
                    print("================================================================================")

                elif cho == 2:
                    print("Thank you")
                    print("Any kind of bulk or small orders of electronic items contact Aditya Electronics shop")
                    print("================================================================================")
                else:
                    print("ERROR 404:DTETCTED")
            elif ch == 2:
                print("Thank you")
                print("Any kind of bulk or small orders of electronic items contact Aditya Electronics shop")
                print("==============================================================================")
            else:
                print("Invalid choice")
                print("Any kind of bulk or small orders of electronic items contact Aditya Electronics shop")
                print("==============================================================================")
    else:
        print("Invalid choice of product number")
        print("Any kind of bulk or small orders of electronic items contact Aditya Electronics shop")
        print("==============================================================================")
elif choice == 2:
    print("1.Add stock")
    print("2.View stock")
    print("3.Update new stock")
    chi = int(input("Enter the Choice - "))
    if chi == 1:
        v = '123456'
        c = input("Enter the password:")
        if c == v:

            a = int(input("Enter the Product Number : "))
            b = int(input("Enter how much stock must be updated:"))
            c1.execute("update products set Stock = Stock + " + str(b) + " where Product_no = " + str(a))
            conn.commit()
            c1.execute("select Product_name,Product_no,Stock from products where Product_no=" + str(a))
            dat = c1.fetchall()
            for row in dat:
                print("Available Stock Details ")
                print("Product name:", row[0])
                print("Product number:", row[1])
                print("Stock:", row[2])
                print("Updated successfully")
        else:
            print("Password is wrong")
    elif chi == 2:

        z = int(input("Enter the Product Number : "))
        c1.execute("select Product_name,Product_no,Stock,Price_per from products where Product_no=" + str(z))
        dat = c1.fetchall()
        for row in dat:
            print("Available Stock Details ")
            print("Product name:", row[0])
            print("Product number:", row[1])
            print("Stock:", row[2])
            print("Price per product Rs:", row[3])

        else:
            print("Thank you")
            print("Any kind of bulk or small orders of electronic items contact Aditya Electronics shop")
            print("=======================================================================")
    elif chi == 3:
        de = '123456'
        da = input("Enter the password:")
        if de == da:
            print("Welcome to Aditya Electronics shop")
            fi = int(input("Enter the new product number:"))
            fe = input("Enter the new product name:")
            st = int(input("Enter the stock to be updated:"))
            price = int(input("Enter the price per product:"))
            c1.execute("Insert into products values('{}',{},'{}','{}')".format(fe, fi, st, price))
            print("Updated successfully")
            conn.commit()
        else:
            print("password is wrong")
    else:
        print("invalid choice")
elif choice == 3:
    print("Thank you")
    print("Any kind of bulk or small orders of electronic items contact Aditya Electronics shop")
    print("=============================================================================")
else:
    print("INVALID CHOICE OF OPTION")
    print("Any kind of bulk or small orders of electronic items contact Aditya Electronics shop")
    print("=============================================================================")
