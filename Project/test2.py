import sqlite3
import datetime
from os import system,name
conn = sqlite3.connect(r'D:\kanis_python\Project\test2.db')
c = conn.cursor()
#c.execute('''CREATE TABLE showcar (NO integer PRIMARY KEY AUTOINCREMENT,
    #Carname varchar(100) NOT NULL,
    #Carbrand varchar(100) NOT NULL,
    #Cartype varchar(100) NOT NULL,
    #Carcolor varchar(100) NOT NULL,
    #condition varchar(100) NOT NULL,
    #Registration varchar(100) NOT NULL,
    #Mileage varchar(100) NOT NULL,
    #price varchar(100) NOT NULL)''')

#c.execute('''CREATE TABLE datapay (NO integer PRIMARY KEY AUTOINCREMENT,
    #Datetimes varchar(100) NOT NULL,
    #Carname varchar(100) NOT NULL,
    #Customer varchar(100) NOT NULL,
    #price varchar(100) NOT NULL,
    #status varchar(100) NOT NULL)''')

#conn.commit()
#conn.close()
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
def menu():
    global choice
    print('================== เบนซ์วงแสวงคาร์ ================ ')
    print('แสดงรายการรถทั้งหมดใรโชว์รูม [1]') 
    print('เพิ่มรายการรถยนต์           [2]')
    print('เพิ่มรายการรถยนต์ที่ขายออก    [3]')
    print('ลบรายการรถยนต์            [4]')
    print('ข้อมูลการขายรถ             [5]')
    print('แก้ไขข้อมูลรถ               [6]')
    print('ออกจากระบบ               [7]')
    choice = int(input('เลือกทำรายการซื้อรถ : '))
def names01():
    global Carname,Carbrand,Cartype,Carcolor,condition,Registration,Mileage,price
    Carname = input('ชื่อรถ\t')
    Carbrand = input('ยี่ห้อรถ\t')
    Cartype = input ('ประเภทรถ\t')
    Carcolor = input('สีรถ\t')
    condition = input('สภาพ\t')
    Registration = input('ทะเบียนรถยนต์\t')
    Mileage = input('เลขไมล์\t')
    price = input('ราคารถ\t')

def insert_showcar (Carname,Carbrand,Cartype,Carcolor,condition,Registration,Mileage,price) :
    try :
        conn = sqlite3.connect (r'D:\kanis_python\Project\test2.db')
        c = conn.cursor()
        sql = '''INSERT INTO showcar (Carname,Carbrand,Cartype,Carcolor,condition,Registration,Mileage,price) VALUES (?,?,?,?,?,?,?,?)'''
        data = (Carname,Carbrand,Cartype,Carcolor,condition,Registration,Mileage,price)
        c.execute(sql,data)
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print('Failed to insert : ',e)
    finally :
        if conn :
            conn.close ()
def names02():
    global datetime,Carname,Customer,price,status,Datetimes
    x = datetime.datetime.now()
    Datetimes = str(x)
    Carname = input('ชื่อรถ\t')
    Customer = input('ลูกค้า\t')
    price = input ('ราคา\t')
    status = input('สถานะ\t')
    
def insert_datapay (Datetimes,Carname,Customer,price,status) :
    try :
        conn = sqlite3.connect (r'D:\kanis_python\Project\test2.db')
        c = conn.cursor()
        sql = '''INSERT INTO datapay (Datetimes,Carname,Customer,price,status) VALUES (?,?,?,?,?)'''
        data = (Datetimes,Carname,Customer,price,status)
        c.execute(sql,data)
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print('Failed to insert : ',e)
    finally :
        if conn :
            conn.close ()

def showcar():
    print('{0:<10}{1:<30}{2:<25}{3:<25}{4:<18}{5:<16}{6:<23}{7:<20}{8}'.format('ลำดับ','ชื่อรถยนต์','ยี้ห้อรถยนต์','ประเภทรถยนต์','สีรถยนต์','สภาพรถยนต์','ทะเบียนรถยนต์','เลขไมล์','ราคา'))
    result = '''SELECT * from showcar '''
    for x in c.execute(result) :
        print('{0:<9}{1:<27}{2:<21}{3:<24}{4:<16}{5:<15}{6:<21}{7:<19}{8}'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]))

def delete():
    number = input('เลื่อกลำดับรายการที่จะลบ : ')
    conn = sqlite3.connect(r'D:\kanis_python\Project\test2.db')
    c = conn.cursor()
    c.execute('''DELETE FROM showcar WHERE No = ?''',number)
    conn.commit()
    conn.close()

def show_datapay():
    print('{0:<10}{1:<36}{2:<22}{3:<25}{4:<18}{5}'.format('ลำดับ','วัน-เวลาซื้อขาย','ชื่อรถ','ชื่อลูกค้า','ราคา','สถานะ'))
    show1 = '''SELECT * from datapay '''
    for x in c.execute(show1):
        print('{0:<9}{1:<33}{2:<20}{3:<21}{4:<18}{5}'.format(x[0],x[1],x[2],x[3],x[4],x[5]))

def Edit():
    minn = int(input('ใส่หมายเลขที่ต้องการแก้ไข : '))
    names01()
    conn = sqlite3.connect (r'D:\kanis_python\Project\test2.db')
    c = conn.cursor()
    update_data = (Carname,Carbrand,Cartype,Carcolor,condition,Registration,Mileage,price,minn)
    c.execute ('''UPDATE showcar SET Carname = ?,Carbrand = ?,Cartype =?,Carcolor = ?,condition = ?,Registration = ?,Mileage = ?,price =? WHERE NO = ?''',update_data)
    conn.commit()
    conn.close()
while True:
    try:
        menu()
        if choice == 1:
            showcar()
        elif choice == 2:
            names01()
            insert_showcar(Carname,Carbrand,Cartype,Carcolor,condition,Registration,Mileage,price)
        elif choice == 3:
            names02()
            insert_datapay (Datetimes,Carname,Customer,price,status)
        elif  choice == 4:
            delete()
        elif choice == 5:
            show_datapay()
        elif choice == 6:
            Edit()
        elif choice == 7:
            print('ออกจากโปรแกรม ')
            Exitt = str(input('ต้องการออกจากโปรแกรมหรือไม่ y/n :'))
            if Exitt == 'y' or Exitt == 'Y':
                clear()
                break
            else:
                print('ใส้ข้อมูลให้ถูกต้อง')
        else:
            print('กรุณาใส่หมายเลขให้ถูกต้อง')
    except:
        print('กรุณาใส่หมายเลขให้ถูกต้อง')
        


