import mysql.connector as mysql
import os
from tabulate import tabulate
from datetime import datetime

class ConnectSql:
    def __init__(self):
        self.__localhost     = "localhost"
        self.__username      = "root"
        self.__password      = ""
        self.__database_name = "library_management_system"
        self.createConnection
    
    @property
    def createConnection(self):
        db = mysql.connect(
          host     = self.__localhost,
          user     = self.__username,
          passwd   = self.__password,
          database = self.__database_name
        )
        return db
        
class showItems(ConnectSql):
    def __init__(self,idLbr,item_id,library_id,category,title,author,publisher,production_year,copies):
        self.__idLbr            = idLbr
        self.__item_id          = item_id 
        self.__library_id       = library_id
        self.__category         = category
        self.__title            = title
        self.__author           = author
        self.__publisher        = publisher
        self.__production_year  = production_year
        self.__copies           = copies
        super().__init__()
        super().createConnection
        self.__db = self.createConnection

    def Library(self):
        mycursor = self.__db.cursor()
        mycursor.execute("SELECT * FROM library")
        myresult = mycursor.fetchall()
        print(tabulate(myresult, headers=["library_id","library_name"], tablefmt="grid"))

    def ItemsById(self):
        mycursor = self.__db.cursor()
        sql = "SELECT * FROM items WHERE library_id=%s"
        val = [self.__idLbr]
        mycursor.execute(sql,val)
        myresult = mycursor.fetchall()
        print(tabulate(myresult, headers=["item_id","library_id","category","title","author","publisher","production_year","copies"], tablefmt="grid"))

    def ReadItems(self):
        mycursor = self.__db.cursor()
        mycursor.execute("SELECT * FROM items")
        myresult = mycursor.fetchall()
        print(tabulate(myresult, headers=["item_id","library_id","category","title","author","publisher","production_year","copies"], tablefmt="grid"))

    def CreateItems(self):
        mycursor = self.__db.cursor()
        val = (self.__item_id, self.__library_id, self.__category, self.__title, self.__author, self.__publisher, self.__production_year, self.__copies)
        mycursor.execute("INSERT INTO items (item_id, library_id, category, title, author, publisher, production_year, copies) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", val)
        self.__db.commit()

        print(mycursor.rowcount, "record inserted.")

    def UpdateItems(self):
        mycursor = self.__db.cursor()
        val = (self.__library_id,self.__category,self.__title,self.__author,self.__publisher,self.__production_year,self.__copies,self.__item_id)
        mycursor.execute ("UPDATE items SET library_id=%s, category=%s, title=%s, author=%s, publisher=%s, production_year=%s, copies=%s WHERE item_id=%s ", val)
        self.__db.commit()

        print(mycursor.rowcount, "record update.")

    def DeleteItems(self):
        mycursor = self.__db.cursor()
        mycursor.execute ("DELETE FROM items WHERE item_id = %s", (self.__item_id,))
        self.__db.commit()

        print(mycursor.rowcount, "record deleted.")

def ItemsMenu():
    while(True):
        print("\nItems Menu")
        print('1. Show data')
        print('2. Insert data')
        print('3. Update data')
        print('4. Delete data')
        print('5. Quit')
        pilih = input("Choose Menu : ")

        if pilih == "1":
            item = showItems(0,0,0,0,0,0,0,0,0)
            item.Library()
            idLbr = int(input("Library ID : "))
            item = showItems(idLbr,0,0,0,0,0,0,0,0)
            item.ItemsById()

        elif pilih == "2":
            item = showItems(0,0,0,0,0,0,0,0,0)
            item.ReadItems()
            print("Insert data items")
            item_id = input("Item ID : ")
            library_id = input("Library ID : ")
            category = input("Category : ")
            title = input("Title : ")
            author = input("Author : ")
            publisher = input("Publisher : ")
            production_year = input("Production_year : ")
            copies = input("Copies : ")
            itemC = showItems(0,item_id,library_id,category,title,author,publisher,production_year,copies)
            itemC.CreateItems()
            
        elif pilih == "3":
            item = showItems(0,0,0,0,0,0,0,0,0)
            item.ReadItems()
            print("Update data items")
            item_id = input("Search by Item ID : ")
            print("Edit")
            library_id = input("Library ID : ")
            category = input("Category : ")
            title = input("Title : ")
            author = input("Author : ")
            publisher = input("Publisher : ")
            production_year = input("Production_year : ")
            copies = input("Copies : ")
            itemU = showItems(0,item_id,library_id,category,title,author,publisher,production_year,copies)
            itemU.UpdateItems()

        elif pilih == "4":
            item = showItems(0,0,0,0,0,0,0,0,0)
            item.ReadItems()
            print("Delete data items")
            item_id = input('Search by item id to delete :')
            itemD = showItems(0,item_id,0,0,0,0,0,0,0)
            itemD.DeleteItems()

        elif pilih == "5":
            os.system("cls")
            break
        else :
            print("You inputed the wrong menu, please try again")

class SubsCRUD(ConnectSql):
    def __init__(self,id_subs,tipe,name,address,phone,email):
        self.__id_subs      = id_subs
        self.__tipe         = tipe
        self.__name         = name
        self.__address      = address
        self.__phone        = phone
        self.__email        = email        
        super().__init__()
        super().createConnection
        self.__db = self.createConnection

    def create(self):
        cursor = self.__db.cursor()
        val = (self.__id_subs, self.__tipe, self.__name, self.__address, self.__phone, self.__email)
        cursor.execute("INSERT INTO subscribers (subscriber_id, type, name, address, phone, email) VALUES (%s,%s,%s,%s,%s,%s)", val)
        self.__db.commit()

        print(cursor.rowcount, "record inserted.")

    def read(self):
        cursor = self.__db.cursor()
        cursor.execute("SELECT * FROM subscribers")
        myresult = cursor.fetchall()

        print(tabulate(myresult, headers=["subscriber_id","type","name","address","phone","email"], tablefmt="grid"))

    def update(self):
        cursor = self.__db.cursor()
        val = (self.__tipe, self.__name, self.__address, self.__phone, self.__email, self.__id_subs)
        cursor.execute ("UPDATE subscribers SET type=%s, name=%s, address=%s, phone=%s, email=%s WHERE subscriber_id=%s ", val)
        self.__db.commit()

        print(cursor.rowcount, "record update.")

    def delete(self):
        cursor = self.__db.cursor()
        cursor.execute ("DELETE FROM subscribers WHERE subscriber_id = %s", (self.__id_subs,))
        self.__db.commit()

        print(cursor.rowcount, "record deleted.")

def SubsMenu():
    while(True):
        print("\nSubscribers Menu")
        print('1. Show data')
        print('2. Insert data')
        print('3. Update data')
        print('4. Delete data')
        print('5. Quit')
        pilih = input("Choose Menu : ")
        if pilih == "1":
            subs = SubsCRUD(0,0,0,0,0,0)
            subs.read()
        elif pilih == "2":
            subs = SubsCRUD(0,0,0,0,0,0)
            subs.read()
            print("Insert data subscriber")
            id_subs = input("Subscriber ID : ")
            print("\ngolden : golden subscribers can borrow for three months")
            print("regular : regular subscribers can borrow for three weeks")
            
            while(True):
                tipe = input("Type (regular/golden): ")
                if (tipe == "regular") or (tipe == "golden"):
                    break
                else:
                    print("You inputed the wrong type, please try again")
            name = input("Name : ")
            address = input("Address : ")
            phone = input("Phone : ")
            email = input("Email : ")
            subs = SubsCRUD(id_subs,tipe,name,address,phone,email)
            subs.create()
            
        elif pilih == "3":
            subs = SubsCRUD(0,0,0,0,0,0)
            subs.read()
            print("Update data subscriber")
            id_subs = input("Search by id subscriber : ")
            print("Edit")
            tipe = input("Type : ")
            name = input("Name : ")
            address = input("Address : ")
            phone = input("Phone : ")
            email = input("Email : ")
            subs = SubsCRUD(id_subs,tipe,name,address,phone,email)
            subs.update()
        elif pilih == "4":
            subs = SubsCRUD(0,0,0,0,0,0)
            subs.read()
            print("Delete data subscriber")
            id_subs = input('Search by subscriber id to delete :')
            subs = SubsCRUD(id_subs,0,0,0,0,0)
            subs.delete()
        elif pilih == "5":
            os.system("cls")
            break
        else :
            print("You inputed the wrong menu, please try again")

def SubsMenuAdmin():
    while(True):
        print("\nSubscribers Menu")
        print('1. Show data')
        print('2. Delete data')
        print('3. Quit')
        pilih = input("Choose Menu : ")
        if pilih == "1":
            subs = SubsCRUD(0,0,0,0,0,0)
            subs.read()
        elif pilih == "2":
            subs = SubsCRUD(0,0,0,0,0,0)
            subs.read()
            print("Delete data subscriber")
            id_subs = input('Search by subscriber id to delete :')
            subs = SubsCRUD(id_subs,0,0,0,0,0)
            subs.delete()
        elif pilih == "3":
            os.system("cls")
            break
        else :
            print("You inputed the wrong menu, please try again")

class Borrow(ConnectSql):
    def __init__(self,id_borrow,id_subs,borrow_date,item_id,return_date,fee):
        self.__id_borrow    = id_borrow
        self.__id_subs      = id_subs
        self.__borrow_date  = borrow_date
        self.__item_id      = item_id      
        self.__return_date  = return_date 
        self.__fee          = fee      
        super().__init__()
        super().createConnection
        self.__db = self.createConnection

    def Denda(self,data_type):
        mycursor = self.__db.cursor()
        val = [self.__id_borrow]
        if data_type == "regular":
            sql = "SELECT DATEDIFF(return_date, borrow_date + INTERVAL '21' DAY) FROM borrowing WHERE borrowing_id = (%s)"
        elif data_type == "golden":
            sql = "SELECT DATEDIFF(return_date, borrow_date + INTERVAL '90' DAY) FROM borrowing WHERE borrowing_id = (%s)"
        
        mycursor.execute(sql,val)
        myresult3 = mycursor.fetchone()
        for i in myresult3:
            tenggat = i
            
        if tenggat > 0 :
            self.__fee = tenggat*2000
            print("Returning Success, but you've got fee for late ",tenggat,"days, about",self.__fee)
            valFee = (self.__fee, self.__id_borrow)
            sqlFee = "UPDATE borrowing SET fee = (%s) WHERE borrowing_id = (%s)"
            mycursor.execute(sqlFee,valFee)
            self.__db.commit()
        else :
            print("Returning Success")
            self.__fee = 0
            valFee = (self.__fee, self.__id_borrow)
            sqlFee = "UPDATE borrowing SET fee = (%s) WHERE borrowing_id = (%s)"
            mycursor.execute(sqlFee,valFee)
            self.__db.commit()

        val1 = [self.__id_borrow]
        sql1 = "SELECT * FROM borrowing WHERE borrowing_id = (%s)"
        mycursor.execute(sql1, val1)
        myresult = mycursor.fetchall()
        print(tabulate(myresult, headers=["borrowing_id","subscriber_id","borrow_date","item_id","return_date","fee"], tablefmt="grid"))

    def Borrowing(self):
        mycursor = self.__db.cursor()
        val = (self.__id_borrow, self.__id_subs, self.__borrow_date, self.__item_id)
        sql = "INSERT INTO borrowing (borrowing_id, subscriber_id, borrow_date, item_id) VALUES (%s, %s, %s, %s)"
        mycursor.execute(sql,val)
        self.__db.commit()
        print("{} data saved".format(mycursor.rowcount))

        #copies -1
        valIdb = [self.__item_id]
        sqlCop = "UPDATE items SET copies = copies - 1 WHERE item_id = (%s)"
        mycursor.execute(sqlCop,valIdb)
        self.__db.commit()

        val1 = [self.__id_borrow]
        sql1 = "SELECT * FROM borrowing WHERE borrowing_id = (%s)"
        mycursor.execute(sql1, val1)
        myresult = mycursor.fetchall()
        print(tabulate(myresult, headers=["borrowing_id","subscriber_id","borrow_date","item_id","return_date","fee"], tablefmt="grid"))

    def ReturnDate(self):
        mycursor = self.__db.cursor()
        val = (self.__return_date, self.__id_borrow)
        sql = "UPDATE borrowing SET return_date = (%s) WHERE borrowing_id = (%s)"
        mycursor.execute(sql,val)
        self.__db.commit()
        print("{} data saved".format(mycursor.rowcount))

        #ngambil item_id
        valIdt = [self.__id_borrow]
        sqlIdt = "SELECT item_id FROM borrowing WHERE borrowing_id = %s"
        mycursor.execute(sqlIdt,valIdt)
        resultId = mycursor.fetchone()
        for i in resultId:
            item_id = i

        #copies +1
        valIdb = [self.__item_id]
        sqlCop = "UPDATE items SET copies = copies + 1 WHERE item_id = (%s)"
        mycursor.execute(sqlCop,valIdb)
        self.__db.commit()
        
        #ngambil type
        valsub = [self.__id_subs]
        sqlsub = "SELECT type FROM subscribers WHERE subscriber_id = %s"
        mycursor.execute(sqlsub,valsub)
        myresultsub = mycursor.fetchone()
        data_type = []
        for i in myresultsub:
            data_type.append(i)
        data_type = ''.join(data_type)

        self.Denda(data_type)

    def ReadBorrow(self):
        mycursor = self.__db.cursor()
        mycursor.execute("SELECT * FROM borrowing")
        myresult = mycursor.fetchall()
        print(tabulate(myresult, headers=["borrowing_id","subscriber_id","borrow_date","item_id","return_date","fee"], tablefmt="grid"))

    def CreateBorrow(self):
        mycursor = self.__db.cursor()
        val = (self.__id_borrow, self.__id_subs, self.__borrow_date, self.__item_id, self.__return_date, self.__fee)
        mycursor.execute("INSERT INTO borrowing (borrowing_id,subscriber_id,borrow_date,item_id,return_date,fee) VALUES (%s,%s,%s,%s,%s,%s)", val)
        self.__db.commit()
        print(mycursor.rowcount, "record inserted.")

    def UpdateBorrow(self):
        mycursor = self.__db.cursor()
        val = (self.__id_subs, self.__borrow_date, self.__item_id, self.__return_date, self.__fee, self.__id_borrow)
        mycursor.execute ("UPDATE borrowing SET subscriber_id=%s, borrow_date=%s, item_id=%s, return_date=%s, fee=%s WHERE borrowing_id=%s ", val)
        self.__db.commit()
        print(mycursor.rowcount, "record update.")

    def DeleteBorrow(self):
        mycursor = self.__db.cursor()
        mycursor.execute ("DELETE FROM borrowing WHERE borrowing_id = %s", (self.__id_borrow,))
        self.__db.commit()
        print(mycursor.rowcount, "record deleted.")

    def OverDue(self):
        mycursor = self.__db.cursor()
        mycursor.execute("SELECT * FROM borrowing WHERE fee > 0")
        myresult = mycursor.fetchall()
        print(tabulate(myresult, headers=["borrowing_id","subscriber_id","borrow_date","item_id","return_date","fee"], tablefmt="grid"))

def BorrowMenu():
    while(True):
        print("\nBorrowing Menu")
        print('1. Show data')
        print('2. Insert data')
        print('3. Update data')
        print('4. Delete data')
        print('2. Quit')
        pilih = input("Choose Menu : ")
        if pilih == "1":
            borrow = Borrow(0,0,0,0,0,0)
            borrow.ReadBorrow()
        elif pilih == "2":
            borrow = Borrow(0,0,0,0,0,0)
            borrow.ReadBorrow()
            print("Insert data Borrowing")
            id_borrow = int(input("Borrowing ID : "))
            id_subs = int(input("Subscriber ID : "))
            borrow_date = input("Borrowing date : ")
            item_id = input("Item id : ")
            return_date = input("Returning date : ")
            fee = int(input("Fee : "))
            borrow = Borrow(id_borrow,id_subs,borrow_date,item_id,return_date,fee)
            borrow.CreateBorrow()
            
        elif pilih == "3":
            borrow = Borrow(0,0,0,0,0,0)
            borrow.ReadBorrow()
            print("Update data borrowing")
            id_borrow = input("Search by borrowing ID : ")
            print("Edit")
            id_subs = int(input("Subscriber ID : "))
            borrow_date = input("Borrowing date : ")
            item_id = input("Item id : ")
            return_date = input("Returning date : ")
            fee = int(input("Fee : "))
            borrow = Borrow(id_borrow,id_subs,borrow_date,item_id,return_date,fee)
            borrow.UpdateBorrow()
        elif pilih == "4":
            borrow = Borrow(0,0,0,0,0,0)
            borrow.ReadBorrow()
            print("Delete data borrowing")
            id_borrow = input('Search by borrowing id to delete :')
            borrow = Borrow(id_borrow,0,0,0,0,0)
            borrow.DeleteBorrow()
        elif pilih == "2":
            os.system("cls")
            break
        else :
            print("You inputed the wrong menu, please try again")

def BorrowMenuAdmin():
    while(True):
        print("\nBorrowing Menu")
        print('1. Show data')
        print('2. Delete data')
        print('3. Quit')
        pilih = input("Choose Menu : ")
        if pilih == "1":
            borrow = Borrow(0,0,0,0,0,0)
            borrow.ReadBorrow()
        elif pilih == "2":
            borrow = Borrow(0,0,0,0,0,0)
            borrow.ReadBorrow()
            print("Delete data borrowing")
            id_borrow = input('Search by borrowing id to delete :')
            borrow = Borrow(id_borrow,0,0,0,0,0)
            borrow.DeleteBorrow()
        elif pilih == "3":
            os.system("cls")
            break
        else :
            print("You inputed the wrong menu, please try again")
                                                                  
def MenuSubs():
    print("\n=== Library Menu ===")
    print("1. List of Library")
    print("2. Subscribers")
    print("3. Borrowing")
    print("4. Returning")
    print("5. Quit")
    pilih_menu = input("Choose Menu : ")
    os.system("cls")
    if pilih_menu == "1":
        item = showItems(0,0,0,0,0,0,0,0,0)
        item.Library()
        idLbr = int(input("Library ID : "))
        item = showItems(idLbr,0,0,0,0,0,0,0,0)
        item.ItemsById()
    elif pilih_menu == "2":
        SubsMenu()       
    elif pilih_menu == "3":
        borrow = Borrow(0,0,0,0,0,0)
        borrow.ReadBorrow()
        print("\nInsert data borrowing")
        id_borrow = int(input("Borrowing ID : "))
        id_subs = int(input("Subscriber ID : "))
        borrow_date = input("Borrowing date : ")
        item_id = input("Item id : ")
        borrow = Borrow(id_borrow,id_subs,borrow_date,item_id,0,0)
        borrow.Borrowing()
    elif pilih_menu == "4":
        borrow = Borrow(0,0,0,0,0,0)
        borrow.ReadBorrow()
        id_subs = int(input("Subscriber ID : ")) 
        id_borrow = int(input("Borrowing ID : "))
        return_date = input("Returning date : ")
        returning = Borrow(id_borrow,id_subs,0,0,return_date,0)
        returning.ReturnDate()
    elif pilih_menu == "5":
        login()
    else:
        print("You inputed the wrong menu, please try again")

def MenuAdmin():
    print("\n=== Library Menu ===")
    print("1. Items")
    print("2. Subscriber")
    print("3. Borrowing")
    print("4. Report Overdue")
    print("5. Quit")
    pilih_menu = input("Choose Menu : ")
    os.system("cls")
    if pilih_menu == "1":
        ItemsMenu()       
    elif pilih_menu == "2":
        SubsMenuAdmin()     
    elif pilih_menu == "3":
        BorrowMenuAdmin()
    elif pilih_menu == "4":
        report = Borrow(0,0,0,0,0,0)
        report.OverDue()
    elif pilih_menu == "5":
        login()
    else:
        print("You inputed the wrong menu, please try again")

def login():
    print('\n=== WELCOME TO LIBRARY MANAGEMENT SYSTEM ===')
    print("Masuk Sebagai : ")
    print("1. Admin")
    print("2. Subscriber")
    print("3. Quit")
    pilih = input("Pilihan(1/2/3) : ")
    os.system("cls")
    if pilih == '1':
        while(True):
            usser = input("Usser : ")
            password = input("Password : ")
            if usser == "admin":
                if password == "admin123":
                    while (True):
                        MenuAdmin()
                else:
                    print("password incorrect, please try again")
            else:
                print("user incorrect, please try again")  
        
    elif pilih == '2':
        while(True):
            MenuSubs()
    elif pilih == '3':
        print("Thankyou")
        exit()
    else:
        print("You inputed the wrong menu, please try again")
        login()

while(True):
    login()