p = {"White":{100},
    "Blank": {100},
    "Gray": {100},
    "Red": {100},
    "Blue": {100},
    "Blue": {100},
    "Yellow": {100},
    "Pink": {100},
    "Purple": {100}
    }
def catalog():
   print("{:20} {}".format("Products(Color)"," Price"))
   for k,v in p.items():
       print("{:20}".format(k),end="")
       print(v)
   print("-"*50)
   print("Promotion")
   print("buy 15,000 - 100,000 baht Discount 10%")
   print("-" * 50)
catalog()

def buy():
   total = 0
   while True:
       a = input("select product : ").capitalize()
       b = input("select brand: ").upper()
       if a != "x".upper():
           n = p[a][b]
           total += int(n)
       else:
           break
   print("Total = {}".format(total))
   if total in range(15000,100001):
       d = (10/100)*total
       e = total - d
       print("Discount = {}".format(d))
       print("Total = {}".format(e))
   else:
       print()
buy()

def login():
    try:
        verusername = input('Enter Username : ')
        vuser = [verusername,]
        verpassword = input('Enter password : ')
        vpassword = [verpassword,]
        c.execute('SELECT * FROM login WHERE username = ?',vuser)
        c.execute('SELECT * FROM login WHERE password = ?',vpassword)
        result = c.fetchone()
        if verusername == result[0] and verpassword == result[1]:
            print('successful!')
        else:
            print('username or password are incorrect please try again!')

    except:
        print('ไม่มีชื่อผู้ใช้นี้ในระบบ กรุณาลองใหม่')
    conn.commit()