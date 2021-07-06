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
time = datetime.datetime.now()

def ch2():
    global ch_num2
    ch_num2 = int(input('ใส่ลำดับที่ต้องการแก้ไข : '))
    '''จะทำงานตรงส่วนของแก้ไขจำนวนสินค้าของแอดมิน'''

def menu(): 
    '''จะโชว์หน้าเมนูในการเลือกทำรายการ'''
    global choice 
    print("*"*65)
    print('-'*20,'👕 T-shirt Yuedpao 👕','-'*20)
    print('{0:<10}{1:<30}{2:<15}{3}'.format('ลำดับ', 'สีเสื้อ', 'ราคา 100 บาท' ,'จำนวน'))
    result = '''SELECT * from shopshirt'''
    for x in c.execute(result) :
        print('{0:<7}{1:<30}{2:<16}{3}'.format(x[0],x[1],x[2],x[3]))
    print("-"*40)
    print(time.strftime("%c"))
    print("Promotion")
    print("Buy 100 shirt, get Discount 10%")
    print("-"*40)
    print('\n','\tแสดงข้อมูลสินค้าที่เลือก   [s]\n' , '\tเพิ่มสินค้าที่ต้องการ      [a]\n','\tลบข้อมูลสินค้า          [d]\n','\tเข้าสู่ระบบโดยผู้ดูแล     [p]\n','\tออกจากโปรแกรม       [x]\n','-'*40,'')

def menu2():
    '''จะโชว์หน้าเมนูในการเลือกทำรายการของแอดมิน'''
    global choice2
    while(True):
        print('\n',"*"*50)
        print("For admin")
        print('-'*40,'\n','\tแสดงข้อมูลสินค้า                  [s]\n' , '\tเพิ่มสินค้าที่ต้องการ                [a]\n','\tแก้ไขข้อมูลสินค้า                  [e]\n','\tลบข้อมูลสินค้า                    [d]\n','\tออกจากโปรแกรมแล้วกลับไปหน้าหลัก   [x]\n','-'*40,'')
        choice2 = str(input(' กรุณาใส่รายการที่ต้องการ : '))
        if choice2 == "s":
            sshirt2()
        elif choice2 == "a":
            addnameblock()
            insert_dataadmin(Color,Price,Quantity)
        elif choice2 == "e":
            modify()
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
        else :
            print('กรุณาทำรายการให้ถูกต้อง ')
    
def sshirt():
    '''จะโชว์สินค้าในตะกร้าของลูกค้า'''
    print('{0:<10}{1:<30}{2:<15}{3:<15}'.format('ลำดับ', 'สีเสื้อ' ,'จำนวน','เบอร์ที่ใช้ติดต่อ'))
    result = '''SELECT * from sorder '''
    for x in c.execute(result) :
        print('{0:<7}{1:<30}{2:<16}{3:<16}'.format(str(x[0]),str(x[1]),str(x[2]),str(x[3])))
        
    cf = str(input('ยืนยันสินค้าการดลือกสินค้าใช่หรือไม่ y/n : '))    
    cf = cf.lower()
    if cf =='y' :
        calculate1()        
    else :
        menu()       

def sshirt2():
    '''จะโชว์สินค้าในคลังของแอดมิน'''
    print('{0:<10}{1:<30}{2:<15}{3}'.format('ลำดับ', 'สีเสื้อ', 'ราคา 100 บาท' ,'จำนวน'))
    result = '''SELECT * from shopshirt '''
    for x in c.execute(result) :
        #print(x)
        print('{0:<7}{1:<30}{2:<15}{3:<5}'.format(x[0],x[1],x[2],x[3]))
    
def nameblock():
    global Color,Price,Quantity
    Price = ('100\t')
    '''กรอกสีเสื้อแล้วไปทำตามเด็ฟของสีต่างๆ'''
    while True:
        Color = str(input('สีเสื้อ :\t'))
        if Color == "Red" :
            red()
            break
        
        elif Color == "Green" :
            green()
            break
                
        elif Color == "Purple" :
            purple()
            break

        elif Color == "Pink" :
            pink()
            break
        
        elif Color == "White" :
            white()
            break
       
        elif Color == "Black":
            black()
            break

        elif Color == "Gray" :
            gray()
            break

        elif Color == "Yellow" :
            yellow()
            break

        elif Color == "Blue" :
            blue()
            break

        else :
            print("กรุณากรอกชื่อสีให้ถูกต้อง")

def editname():
    '''กรอกสีเสื้อแล้วก็จำนวนเสื้อแล้วไปแก้ไข หน้าแอดมิน'''
    global Color,Price,Quantity
    Color = input('สีเสื้อ :\t')
    Price = ('100')
    Quantity = input('จำนวน :')

def addnameblock():
    '''กรอกสีเสื้อแล้วก็จำนวนเสื้อแล้วไปเพิ่มในคลัง หน้าแอดมิน'''
    global Color,Price,Quantity
    Color = input('สีเสื้อ :\t')
    Price = ('100')
    Quantity = input('จำนวน :')
   
def login():
    '''เช็คยูสเซอร์'''
    try:
        verusername = input('Enter user : ')
        vuser = verusername
        verpassword = input('Enter password : ')
        vpassword = verpassword
        sql = "SELECT * FROM login WHERE user = '{0}' AND password = '{1}'".format(vuser,vpassword)
        '''print(sql)'''
        c.execute("SELECT * FROM login WHERE user = '{0}' AND password = '{1}'".format(vuser,vpassword))
        result = c.fetchone()
        if verusername == result[0] and verpassword == result[1]:
            print('ยืนยันการเข้าระบบสินค้า!')
            menu2()
        else:
            print('user or password are incorrect please try again!')
            login()
    except:
        print('ไม่มีชื่อผู้ใช้นี้ในระบบ กรุณาลองใหม่')
            
    conn.commit()

def insert_dataadmin (Color,Price,Quantity) :
    '''ต่อมาจากหน้าเพิ่มสินคค้าแอดมิน'''
    try :
        conn = sqlite3.connect (r'D:\kanis_python\Project2.db')
        c = conn.cursor()
        sql = '''INSERT INTO shopshirt (Color,Price,Quantity)VALUES (?,?,?)'''
        data = (Color,Price,Quantity)
        c.execute(sql,data)
        conn.commit()
        conn.close()
    except sqlite3.Error as e :
        print('Failed to insert : ',e)
    finally :
        if conn : 
            conn.close()

def calculate1():
    '''กรอกจำนวนเงินแล้วคิดเงิน'''
    showlist()
    conn = sqlite3.connect (r'D:\kanis_python\Project2.db')
    c=conn.cursor()
    c.execute('''SELECT sum(Quantity) FROM sorder''')
    result=c.fetchone()
    for i in result:
        print("จำนวนสินค้า",i)

    sum = int(i)*100
    sum2 = 0
    print('ราคารวมทั้งหมดเท่ากับ',str(sum),'บาท')
    if sum in range(10000,100001):
        d = (10/100)*sum
        sum2 = float(sum)- d
        print("ส่วนลด = {}".format(d))
        print("ราคาที่ต้องจ่าย = {} บาท\n".format(sum2))
    else :
        sum2 = sum

    while (True):
        try :
            total = int(input("กรุณาใส่จำนวนเงิน : "))
            if total < sum2 :
                print("กรุณาใส่จำนวนเงินให้ถูกต้อง")
            else:
                break
        except :
            print("กรุณากรอกแค่ตัวเลขเท่านั้น")
    conn = sqlite3.connect(r'D:\kanis_python\Project2.db')
    c = conn.cursor()
    conn.commit()
    try :
        c.execute('''DELETE FROM sorder ''')
        conn.commit()
        conn.close()
    except sqlite3.Error as e :
        print('Failed to data : ',e)
    finally :
        if conn :
            conn.close()
   
def telphone() :
    global telss 
    telss = input("กรุณากรอกหมายเลข :")
    
def showlist():
    print('{0:<10}{1:<30}{2:<15}'.format('ลำดับ', 'สีเสื้อ' ,'จำนวน'))
    result = '''SELECT * from sorder '''
    for x in c.execute(result) :
        print('{0:<7}{1:<30}{2:<16}'.format(x[0],x[1],x[2]))

def delete():
    conn = sqlite3.connect(r'D:\kanis_python\Project2.db')
    c = conn.cursor()
    print('{0:<10}{1:<30}{2}'.format('ลำดับ', 'สีเสื้อ','จำนวน'))
    result = '''SELECT * FROM sorder '''
    for x in c.execute(result) :
        print('{0:<7}{1:<30}{2}'.format(x[0],x[1],x[2]))
    number = input('เลือกรายการที่จะลบ : ')
    number = (number,)
    try :
        c.execute('''DELETE FROM sorder WHERE NO = ?''',number)
        conn.commit()
        conn.close()
    except sqlite3.Error as e :
        print('Failed to data : ',e)
    finally :
        if conn :
            conn.close()

def delete2():
    conn = sqlite3.connect(r'D:\kanis_python\Project2.db')
    c = conn.cursor()
    conn.commit()
    print('{0:<10}{1:<30}{2:<15}{3}'.format('ลำดับ', 'สีเสื้อ', 'ราคา 100 บาท' ,'จำนวน'))
    result = '''SELECT * FROM shopshirt '''
    for x in c.execute(result) :
        print('{0:<7}{1:<30}{2:<15}{3:<5}'.format(x[0],x[1],x[2],x[3]))
    number1 = int(input('เลือกรายการที่จะลบ : '))
    number1 = (number1,)
    try :
        c.execute('''DELETE FROM shopshirt WHERE NO = ?''',number1)
        conn.commit()
        conn.close()
    except sqlite3.Error as e :
        print('Failed to data : ',e)
    finally :
        if conn :
            conn.close()
    """c.execute('''DELETE FROM shopshirt WHERE No = ?''',number1)
    conn.close()"""
 
def modify():
    conn = sqlite3.connect (r'D:\kanis_python\Project2.db')
    c = conn.cursor()
    print('{0:<10}{1:<30}{2}'.format('ลำดับ', 'สีเสื้อ','จำนวน'))
    result = '''SELECT * from shopshirt '''
    for x in c.execute(result) :
        print('{0:<7}{1:<30}{2}'.format(x[0],x[1],x[3]))
    ch2()
    editname()
    update_data = (Color,Price,Quantity,ch_num2)
    c.execute('''UPDATE shopshirt SET Color = ? ,Price = ? ,Quantity = ? WHERE NO = ?''',update_data)
    conn.commit()
    conn.close()
    
def clear():
    if name =="nt":
        _ = system('cls')
    else:
        _ = system('clear')

def red():
    Quantity = input('จำนวน :\t')
    c.execute('''SELECT Quantity FROM shopshirt WHERE Color = ? ''',(Color,))
    result = c.fetchone()
    if int(Quantity) > int(result[0]):  
        print('จำนวนของในคลังไม่เพียงพอ')
    elif int(Quantity) <= int(result[0]): 
        newQuan = int(result[0])-int(Quantity)
        c.execute('''UPDATE shopshirt SET Quantity = ? WHERE Color = ?''',(newQuan,Color,))
        conn.commit()
        try:
            sql = "INSERT INTO sorder (Color,Quantity,Phone) VALUES ('{0}','{1}','{2}')".format(Color,Quantity,telss)
            c.execute(sql)
            conn.commit()
        except sqlite3.Error as e  :
            print('กรุณากรอกหมายเลขอีกครั้ง',e)
        try:
            sql = "INSERT INTO historyorder (Color,Quantity,Phone,date) VALUES ('{0}','{1}','{2}','{3}')".format(Color,Quantity,telss,time)
            c.execute(sql)
            conn.commit()
        except sqlite3.Error as e  :
            print('กรุณากรอกหมายเลขอีกครั้ง',e)
    do = str(input('ต้องการเลือกสินค้าอีกหรือไม่ y/n :')) 
    do = do.lower()
    if do == 'y' :
        nameblock()
    else :
        menu()

def green():
    Quantity = input('จำนวน :\t')
    c.execute('''SELECT Quantity FROM shopshirt WHERE Color = ? ''',(Color,))
    result = c.fetchone()
    if int(Quantity) > int(result[0]):  
        print('จำนวนของในคลังไม่เพียงพอ')
    elif int(Quantity) <= int(result[0]): 
        newQuan = int(result[0])-int(Quantity)
        c.execute('''UPDATE shopshirt SET Quantity = ? WHERE Color = ?''',(newQuan,Color,))
        conn.commit()
        try:
            sql = "INSERT INTO sorder (Color,Quantity,Phone) VALUES ('{0}','{1}','{2}')".format(Color,Quantity,telss)
            c.execute(sql)
            conn.commit()
        except sqlite3.Error as e  :
            print('กรุณากรอกหมายเลขอีกครั้ง',e)
        try:
            sql = "INSERT INTO historyorder (Color,Quantity,Phone,date) VALUES ('{0}','{1}','{2}','{3}')".format(Color,Quantity,telss,time)
            c.execute(sql)
            conn.commit()
        except sqlite3.Error as e  :
            print('กรุณากรอกหมายเลขอีกครั้ง',e)
    do = str(input('ต้องการเลือกสินค้าอีกหรือไม่ y/n :')) 
    do = do.lower()
    if do == 'y' :
        nameblock()
    else :
        menu()

def purple():
    Quantity = input('จำนวน :\t')
    c.execute('''SELECT Quantity FROM shopshirt WHERE Color = ? ''',(Color,))
    result = c.fetchone()
    if int(Quantity) > int(result[0]):  
        print('จำนวนของในคลังไม่เพียงพอ')
    elif int(Quantity) <= int(result[0]): 
        newQuan = int(result[0])-int(Quantity)
        c.execute('''UPDATE shopshirt SET Quantity = ? WHERE Color = ?''',(newQuan,Color,))
        conn.commit()
        try:
            sql = "INSERT INTO sorder (Color,Quantity,Phone) VALUES ('{0}','{1}','{2}')".format(Color,Quantity,telss)
            c.execute(sql)
            conn.commit()
        except sqlite3.Error as e  :
            print('กรุณากรอกหมายเลขอีกครั้ง',e)
        try:
            sql = "INSERT INTO historyorder (Color,Quantity,Phone,date) VALUES ('{0}','{1}','{2}','{3}')".format(Color,Quantity,telss,time)
            c.execute(sql)
            conn.commit()
        except sqlite3.Error as e  :
            print('กรุณากรอกหมายเลขอีกครั้ง',e)
    do = str(input('ต้องการเลือกสินค้าอีกหรือไม่ y/n :')) 
    do = do.lower()
    if do == 'y' :
        nameblock()
    else :
        menu()      

def pink():
    Quantity = input('จำนวน :\t')
    c.execute('''SELECT Quantity FROM shopshirt WHERE Color = ? ''',(Color,))
    result = c.fetchone()
    if int(Quantity) > int(result[0]):  
        print('จำนวนของในคลังไม่เพียงพอ')
    elif int(Quantity) <= int(result[0]): 
        newQuan = int(result[0])-int(Quantity)
        c.execute('''UPDATE shopshirt SET Quantity = ? WHERE Color = ?''',(newQuan,Color,))
        conn.commit()
        try:
            sql = "INSERT INTO sorder (Color,Quantity,Phone) VALUES ('{0}','{1}','{2}')".format(Color,Quantity,telss)
            c.execute(sql)
            conn.commit()
        except sqlite3.Error as e  :
            print('กรุณากรอกหมายเลขอีกครั้ง',e)
        try:
            sql = "INSERT INTO historyorder (Color,Quantity,Phone,date) VALUES ('{0}','{1}','{2}','{3}')".format(Color,Quantity,telss,time)
            c.execute(sql)
            conn.commit()
        except sqlite3.Error as e  :
            print('กรุณากรอกหมายเลขอีกครั้ง',e)
    do = str(input('ต้องการเลือกสินค้าอีกหรือไม่ y/n :')) 
    do = do.lower()
    if do == 'y' :
        nameblock()
    else :
        menu()

def white():
    Quantity = input('จำนวน :\t')
    c.execute('''SELECT Quantity FROM shopshirt WHERE Color = ? ''',(Color,))
    result = c.fetchone()
    if int(Quantity) > int(result[0]):  
        print('จำนวนของในคลังไม่เพียงพอ')
    elif int(Quantity) <= int(result[0]): 
        newQuan = int(result[0])-int(Quantity)
        c.execute('''UPDATE shopshirt SET Quantity = ? WHERE Color = ?''',(newQuan,Color,))
        conn.commit()
        try:
            sql = "INSERT INTO sorder (Color,Quantity,Phone) VALUES ('{0}','{1}','{2}')".format(Color,Quantity,telss)
            c.execute(sql)
            conn.commit()
        except sqlite3.Error as e  :
            print('กรุณากรอกหมายเลขอีกครั้ง',e)
        try:
            sql = "INSERT INTO historyorder (Color,Quantity,Phone,date) VALUES ('{0}','{1}','{2}','{3}')".format(Color,Quantity,telss,time)
            c.execute(sql)
            conn.commit()
        except sqlite3.Error as e  :
            print('กรุณากรอกหมายเลขอีกครั้ง',e)
    do = str(input('ต้องการเลือกสินค้าอีกหรือไม่ y/n :')) 
    do = do.lower()
    if do == 'y' :
        nameblock()
    else :
        menu()

def yellow():
    Quantity = input('จำนวน :\t')
    c.execute('''SELECT Quantity FROM shopshirt WHERE Color = ? ''',(Color,))
    result = c.fetchone()
    if int(Quantity) > int(result[0]):  
        print('จำนวนของในคลังไม่เพียงพอ')
    elif int(Quantity) <= int(result[0]): 
        newQuan = int(result[0])-int(Quantity)
        c.execute('''UPDATE shopshirt SET Quantity = ? WHERE Color = ?''',(newQuan,Color,))
        conn.commit()
        try:
            sql = "INSERT INTO sorder (Color,Quantity,Phone) VALUES ('{0}','{1}','{2}')".format(Color,Quantity,telss)
            c.execute(sql)
            conn.commit()
        except sqlite3.Error as e  :
            print('กรุณากรอกหมายเลขอีกครั้ง',e)
        try:
            sql = "INSERT INTO historyorder (Color,Quantity,Phone,date) VALUES ('{0}','{1}','{2}','{3}')".format(Color,Quantity,telss,time)
            c.execute(sql)
            conn.commit()
        except sqlite3.Error as e  :
            print('กรุณากรอกหมายเลขอีกครั้ง',e)
    do = str(input('ต้องการเลือกสินค้าอีกหรือไม่ y/n :')) 
    do = do.lower()
    if do == 'y' :
        nameblock()
    else :
        menu()

def black():
    Quantity = input('จำนวน :\t')
    c.execute('''SELECT Quantity FROM shopshirt WHERE Color = ? ''',(Color,))
    result = c.fetchone()
    if int(Quantity) > int(result[0]):  
        print('จำนวนของในคลังไม่เพียงพอ')
    elif int(Quantity) <= int(result[0]): 
        newQuan = int(result[0])-int(Quantity)
        c.execute('''UPDATE shopshirt SET Quantity = ? WHERE Color = ?''',(newQuan,Color,))
        conn.commit()
        try:
            sql = "INSERT INTO sorder (Color,Quantity,Phone) VALUES ('{0}','{1}','{2}')".format(Color,Quantity,telss)
            c.execute(sql)
            conn.commit()
        except sqlite3.Error as e  :
            print('กรุณากรอกหมายเลขอีกครั้ง',e)
        try:
            sql = "INSERT INTO historyorder (Color,Quantity,Phone,date) VALUES ('{0}','{1}','{2}','{3}')".format(Color,Quantity,telss,time)
            c.execute(sql)
            conn.commit()
        except sqlite3.Error as e  :
            print('กรุณากรอกหมายเลขอีกครั้ง',e)
    do = str(input('ต้องการเลือกสินค้าอีกหรือไม่ y/n :')) 
    do = do.lower()
    if do == 'y' :
        nameblock()
    else :
        menu()

def gray():
    Quantity = input('จำนวน :\t')
    c.execute('''SELECT Quantity FROM shopshirt WHERE Color = ? ''',(Color,))
    result = c.fetchone()
    if int(Quantity) > int(result[0]):  
        print('จำนวนของในคลังไม่เพียงพอ')
    elif int(Quantity) <= int(result[0]): 
        newQuan = int(result[0])-int(Quantity)
        c.execute('''UPDATE shopshirt SET Quantity = ? WHERE Color = ?''',(newQuan,Color,))
        conn.commit()
        try:
            sql = "INSERT INTO sorder (Color,Quantity,Phone) VALUES ('{0}','{1}','{2}')".format(Color,Quantity,telss)
            c.execute(sql)
            conn.commit()
        except sqlite3.Error as e  :
            print('กรุณากรอกหมายเลขอีกครั้ง',e)
        try:
            sql = "INSERT INTO historyorder (Color,Quantity,Phone,date) VALUES ('{0}','{1}','{2}','{3}')".format(Color,Quantity,telss,time)
            c.execute(sql)
            conn.commit()
        except sqlite3.Error as e  :
            print('กรุณากรอกหมายเลขอีกครั้ง',e)
    do = str(input('ต้องการเลือกสินค้าอีกหรือไม่ y/n :')) 
    do = do.lower()
    if do == 'y' :
        nameblock()
    else :
        menu()

def blue():
    Quantity = input('จำนวน :\t')
    c.execute('''SELECT Quantity FROM shopshirt WHERE Color = ? ''',(Color,))
    result = c.fetchone()
    if int(Quantity) > int(result[0]):  
        print('จำนวนของในคลังไม่เพียงพอ')
    elif int(Quantity) <= int(result[0]): 
        newQuan = int(result[0])-int(Quantity)
        c.execute('''UPDATE shopshirt SET Quantity = ? WHERE Color = ?''',(newQuan,Color,))
        conn.commit()
        try:
            sql = "INSERT INTO sorder (Color,Quantity,Phone) VALUES ('{0}','{1}','{2}')".format(Color,Quantity,telss)
            c.execute(sql)
            conn.commit()
        except sqlite3.Error as e  :
            print('กรุณากรอกหมายเลขอีกครั้ง',e)
        try:
            sql = "INSERT INTO historyorder (Color,Quantity,Phone,date) VALUES ('{0}','{1}','{2}','{3}')".format(Color,Quantity,telss,time)
            c.execute(sql)
            conn.commit()
        except sqlite3.Error as e  :
            print('กรุณากรอกหมายเลขอีกครั้ง',e)
    do = str(input('ต้องการเลือกสินค้าอีกหรือไม่ y/n :')) 
    do = do.lower()
    if do == 'y' :
        nameblock()
    else :
        menu()
   
while True:
    menu()
    choice = str(input(' กรุณาใส่รายการที่ต้องการ :'))
    if choice == "s":
        sshirt()
    elif choice == "a":
        telphone()
        nameblock()
        #insert_shopshirt (Datetimes,Color,Price,Quantity)
    elif choice == "d":
        delete()
    elif choice == "p":
        login()
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
        print('กรุณาใส่ให้ถูกต้อง')
conn.commit()
conn.close()