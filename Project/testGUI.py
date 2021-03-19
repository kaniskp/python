import sqlite3
conn = sqlite3.connect (r"D:\kanis_python\Project\testGUI.db")
c = conn.cursor()
from os import close, name, system
from sqlite3.dbapi2 import connect
#c.execute('''CREATE TABLE byintendent (No integer PRIMARY KEY AUTOINCREMENT,
    #colorTshit varchar(100) NOT NULL,
    #priceamount varchar(100) NOT NULL,
    #amount varchar(100) NOT NULL)''')
#conn.commit()
#conn.close()

def choice():
    global choice_no
    choice_no = input('\tกรุณาใส่หมายเลขสินค้าที่ต้องการแก้ไข : ')
def choice1():
    global number
    number = input('\tกรุณาใส่หมายเลขสินค้าที่ต้องลบ : ')
def clear():
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear')
def menu():
    global room
    print('-'*20,'\n','\tเพิ่มข้อมูลสินค้า  [a]\n','\tแสดงข้อมูลสินค้า [s]\n','\tแก้ไขข้อมูลสินค้า [e]\n','\tลบข้อมูลสินค้า   [d]\n','\tออกจากโปรแกรม  [x]\n','-'*20,'')
    room = str(input(' กรุราใส่รายการที่ต้องการ :'))
def addstd():
    global colortshit,price,amount,data1
    print('\n\t\t*** เพิ่มข้อมูลสินค้า ***\n')
    data2 = []
    data1 = input('input colortshit,price,amount : ')
    data2 = data1.split(",")
    colortshit = data2[0]
    price = data2[1]
    amount = data2[2]
    
def addstd1():
    global colortshit,price,amount,data1
    print('\n\t*** เพิ่มข้อมูลสินค้าที่ต้องการแก้ไข   ***\n')
    data2 = []
    data1 = input('input colortshit,price,amount : ')
    data2 = data1.split(",")
    colortshit = data2[0]
    price = data2[1]
    amount = data2[2]
    
def insert (colortshit,price,amount) :
    try :
        conn = sqlite3.connect (r"D:\kanis_python\Project\testGUI.db")
        c = conn.cursor()

        sql = '''INSERT INTO byintendent(colortshit,price,amount) VALUES (?,?,?,?,?)'''
        data = (colortshit,price,amount)
        c.execute(sql,data)
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print('Failed to insert : ',e)
    finally :

        if conn :
            conn.close ()
def show():
    print('\n\t\t\t*** แสดงข้อมูลสินค้า ***\n')
    print('{0:<8}{1:<15}{2:<15}{3:<27}\n'.format('No','colortshit','price','amount'))
    with sqlite3.connect(r"D:\kanis_python\Project\testGUI.db") as con:
        con.row_factory = sqlite3.Row
        show1="SELECT * FROM intendent "
        for row in con.execute(show1):
            print('{0:<8}{1:<15}{2:<15}{3:<27}'.format(row["no"],row["colortshit"],row["price"],row["amount"]))
def edit() :
    choice()
    addstd1()
    conn = sqlite3.connect (r"D:\kanis_python\Project\testGUI.db")
    c = conn.cursor()
    update_data = (colortshit,price,amount,choice_no)
    c.execute ('''UPDATE byintendent SET colortshit = ?,price = ?,amount = ? WHERE NO = ?''',update_data)
    conn.commit()
    conn.close()
def delete():
    choice1()
    conn = sqlite3.connect(r"D:\kanis_python\Project\testGUI.db")
    c = conn.cursor()
    c.execute('''DELETE FROM byintendent WHERE No = ?''',number)
    conn.commit()
    conn.close()
while True:
    menu()
    if room == 'a':
        addstd()
        insert(colortshit,price,amount)
        print('\n\tทำรายการเสร็จสิ้น\n')
    elif room == 's':
        show()
        print('\n\tทำรายการเสร็จสิ้น\n')
    elif room == 'e':
        edit()
        print('\n\tทำรายการเสร็จสิ้น\n')
    elif room == 'd':
        delete()
        print('\n\tทำรายการเสร็จสิ้น\n')
    elif room == 'x':
        print('\tออกจากดปรแกรม')
        e=str(input('\tต้องการออกจาระบบหรือไม่ yes/no : '))
        if e == 'yes':
            clear()
            break
    else:
        print('\n\tกรุณาใส่รายการให้ถูกต้อง\n')




