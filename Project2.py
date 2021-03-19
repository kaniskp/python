import sqlite3
import datetime
from os import system,name
conn = sqlite3.connect(r'D:\kanis_python\Project2.db')
c = conn.cursor()
#c.execute('''CREATE TABLE shopshirt(NO integer PRIMARY KEY AUTOINCREMENT,
    #Datetimes varchar(100) NOT NULL,
    #Color varchar(100) NOT NULL,    
    #Price varchar(100) NOT NULL,
    #Quantity varchar(100) NOT NULL)''')

#c.execute('''CREATE TABLE dataadmin(NO integer PRIMARY KEY AUTOINCREMENT,
    #Color varchar(100) NOT NULL,
    #Price varchar(100) NOT NULL,
    #Quantity varchar(100) NOT NULL)''')

def ch():
    global ch_num
    ch_num = int(input('ใส่ลำดับที่ต้องการแก้ไข : '))

def ch2():
    global ch_num2
    ch_num2 = int(input('ใส่ลำดับที่ต้องการแก้ไข : '))

def menu(): 
    global choice 
    print("*"*65)
    print('-'*20,'👕 T-shirt Yuedpao 👕','-'*20)
    print('{0:<10}{1:<30}{2:<15}{3}'.format('ลำดับ', 'สีเสื้อ', 'ราคา 100 บาท' ,'จำนวน'))
    result = '''SELECT * from dataadmin '''
    for x in c.execute(result) :
        #print (x)
        print('{0:<7}{1:<30}{2:<15}{3}'.format(x[0],x[1],x[2],x[3]))
    print("-"*40)
    print("Promotion")
    print("Buy 100 shirt, get Discount 10%")
    print("-"*40)
    print('\n','\tแสดงข้อมูลสินค้าที่เลือก   [s]\n' , '\tเพิ่มสินค้าที่ต้องการ      [a]\n','\tแก้ไขข้อมูลสินค้า        [e]\n','\tยืนยันสินค้า            [c]\n','\tลบข้อมูลสินค้า          [d]\n','\tเข้าสู่ระบบโดยผู้ดูแล     [p]\n','\tออกจากโปรแกรม       [x]\n','-'*40,'')

def menu2(): 
    login()
    global choice2
    while(True):
        print('\n',"*"*50)
        print("For admin")
        print('-'*40,'\n','\tแสดงข้อมูลสินค้า                  [s]\n' , '\tเพิ่มสินค้าที่ต้องการ                [a]\n','\tแก้ไขข้อมูลสินค้า                  [e]\n','\tลบข้อมูลสินค้า                    [d]\n','\tออกจากโปรแกรมแล้วกลับไปหน้าหลัก   [x]\n','-'*40,'')
        choice2 = str(input(' กรุณาใส่รายการที่ต้องการ : '))
        if choice2 == "s":
            sshirt2()
        elif choice2 == "a":
            nameblock3()
            insert_dataadmin(Color,Price,Quantity)
        elif choice2 == "e":
            modify2()
        elif choice2 == "d":
            delete2()
        elif choice2 == "x":
            print('ออกจากโปรแกรมแล้วกลับไปหน้าหลัก ')
            Exitt1 = str(input('ต้องการออกจากโปรแกรมหรือไม่ y/n :'))
            Exitt1=Exitt1.lower()
            if Exitt1 == 'y' :
                break
            elif Exitt1== 'n':
                print('')
    
def sshirt():
    print('{0:<10}{1:<30}{2:<15}{3:<20}{4}'.format('ลำดับ','เวลา', 'สีเสื้อ', 'ราคา 100 บาท' ,'จำนวน'))
    result = '''SELECT * from shopshirt '''
    for x in c.execute(result) :
        print('{0:<7}{1:<30}{2:<15}{3:<20}{4}'.format(x[0],x[1],x[2],x[3],x[4]))

def sshirt2():
    print('{0:<10}{1:<30}{2:<15}{3}'.format('ลำดับ', 'สีเสื้อ', 'ราคา 100 บาท' ,'จำนวน'))
    result = '''SELECT * from dataadmin '''
    for x in c.execute(result) :
        print('{0:<7}{1:<30}{2:<10}{3:<5}'.format(x[0],x[1],x[2],x[3]))
    
def nameblock():
    global datetime,Color,Price,Quantity,Datetimes
    x = datetime.datetime.now()
    Datetimes = str(x)
    Color = input('สีเสื้อ :\t')
    Price = ('100\t')
    Quantity = input('จำนวน :\t')

def nameblock1():
    global Color,Price,Quantity
    Color = input('สีเสื้อ :\t')
    Price = ('100\t')
    Quantity = input('จำนวน :\t')

def nameblock2():
    global Color,Price,Quantity
    Color = input('สีเสื้อ :\t')
    Price = ('100')
    Quantity = input('จำนวน :\t')

def nameblock3():
    global Color,Price,Quantity
    Color = input('สีเสื้อ :\t')
    Price = ('100')
    Quantity = input('จำนวน :\t')
   
def login():
    try:
        verusername = input('Enter user : ')
        vuser = [verusername,]
        verpassword = input('Enter password : ')
        vpassword = [verpassword,]
        c.execute('SELECT * FROM login WHERE user = ?',vuser)
        c.execute('SELECT * FROM login WHERE password = ?',vpassword)
        result = c.fetchone()
        if verusername == result[0] and verpassword == result[1]:
            print('ยืนยันการเข้าระบบสินค้า!')
        else:
            print('user or password are incorrect please try again!')
    except:
        print('ไม่มีชื่อผู้ใช้นี้ในระบบ กรุณาลองใหม่')
            
    conn.commit()

def insert_shopshirt(Datetimes,Color,Price,Quantity) :
    try :
        conn = sqlite3.connect(r"D:\kanis_python\Project2.db")
        c =conn.cursor()
        sql = '''INSERT INTO shopshirt (Datetimes,Color,Price,Quantity) VALUES (?,?,?,?)'''
        data = (Datetimes,Color,Price,Quantity)
        c.execute(sql,data)
        conn.commit()
        conn.close()
    except sqlite3.Error as e :
        print('Failed to insert : ',e)
    finally :
        if conn :
            print('บันทึกข้อมูลแล้ว')
            conn.close()

def insert_dataadmin (Color,Price,Quantity) :
    try :
        conn = sqlite3.connect (r'D:\kanis_python\Project2.db')
        c = conn.cursor()
        sql = '''INSERT INTO dataadmin (Color,Price,Quantity)VALUES (?,?,?)'''
        data = (Color,Price,Quantity)
        c.execute(sql,data)
        conn.commit()
        conn.close()
    except sqlite3.Error as e :
        print('Failed to insert : ',e)
    finally :
        if conn : 
            conn.close ()

def calculate1():
    showlist()
    c=conn.cursor()
    c.execute('''SELECT sum(Quantity) FROM shopshirt''')
    result=c.fetchone()
    for i in result:
        print("จำนวนสินค้า",i)

    sum = int(i)*100
    print('ราคารวมทั้งหมดเท่ากับ',str(sum),'บาท')
    if sum in range(10000,100001):
       d = (10/100)*sum
       e = sum - d
       print("ส่วนลด = {}".format(d))
       print("ราคาที่ต้องจ่าย = {} บาท\n".format(e))
    else:
        print()
    
def showlist():
    print('{0:<10}{1}'.format('สีเสื้อ','จำนวน'))
    result = '''SELECT * FROM shopshirt '''
    for x in c.execute(result) :
        print('{0:<7}{1}'.format(x[2],x[4]))

def delete():
    number = input('เลือกรายการที่จะลบ : ')
    number = (number,)
    try :
        conn = sqlite3.connect(r'D:\kanis_python\Project2.db')
        c = conn.cursor()
        c.execute('''DELETE FROM shopshirt WHERE NO = ?''',number)
        conn.commit()
        conn.close()
    except sqlite3.Error as e :
        print('Failed to data : ',e)
    finally :
        if conn :
            conn.close()

def delete2():
    number1 = input('เลือกรายการที่จะลบ : ')
    number1 = (number1,)
    conn = sqlite3.connect(r'D:\kanis_python\Project2.db')
    c = conn.cursor()
    c.execute('''DELETE FROM dataadmin WHERE NO = ?''',number1)
    conn.commit()
    print('{0:<10}{1:<30}{2:<15}{3}'.format('ลำดับ', 'สีเสื้อ', 'ราคา 100 บาท' ,'จำนวน'))
    result = '''SELECT * from dataadmin '''
    for x in c.execute(result) :
        print('{0:<7}{1:<30}{2:<10}{3:<5}'.format(x[0],x[1],x[2],x[3]))
    conn.close()
    
def modify():
    ch()
    nameblock1()
    conn = sqlite3.connect (r'D:\kanis_python\Project2.db')
    c = conn.cursor()
    update_data = (Color,Price,Quantity,ch_num)
    c.execute('''UPDATE shopshirt SET Color = ? ,Price = ? ,Quantity = ? WHERE NO = ?''',update_data)
    conn.commit()
    conn.close()

def modify2():
    ch2()
    nameblock2()
    conn = sqlite3.connect (r'D:\kanis_python\Project2.db')
    c = conn.cursor()
    update_data = (Color,Price,Quantity,ch_num2)
    c.execute('''UPDATE dataadmin SET Color = ? ,Price = ? ,Quantity = ? WHERE NO = ?''',update_data)
    conn.commit()
    conn.close()
    
def clear():
    if name =="nt":
        _ = system('cls')
    else:
        _ = system('clear')

while True:
    try:
        menu()
        choice = str(input(' กรุณาใส่รายการที่ต้องการ :'))
        if choice == "s":
            sshirt()
        elif choice == "a":
            nameblock()
            insert_shopshirt (Datetimes,Color,Price,Quantity)
        elif choice == "e":
            modify()
        elif  choice == "c":
            calculate1()
        elif choice == "d":
            delete()
        elif choice == "p":
            menu2()
            continue
        elif choice == "x":
            print('ออกจากโปรแกรม ')
            Exitt = str(input('ต้องการออกจากโปรแกรมหรือไม่ y/n :'))
            Exitt=Exitt.lower()
            if Exitt == 'y' :
                clear()
                break
            elif Exitt== 'n':
                continue
        else:
            print('กรุณาใส่หมายเลขให้ถูกต้อง')
            
    
    except:
        print('กรุณาใส่หมายเลขให้ถูกต้อง')

conn.commit()
conn.close()