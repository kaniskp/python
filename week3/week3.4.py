a=[]
while True :
    b = input("_____คุณดอมรีวิว_____\n เพิ่ม [a]\n แสดง [s]\n ออกจากระบบ [x]\n")
    if b=="a" :
        c = input("ป้อนรายการลูกค้า(สินค้า:ชื่อ:แบรนด์)")
        a.append(c)
        print("\n******ข้อมูลได้เข้าสู่ระบบแล้ว*******\n")
    elif b =="s" :
        print("{0: <6}{0: <10}{0: <10}".format(""))
        print("{0: <8}{1: <10}{2: <10}".format("สินค้า","ชื่อ","แบรนด์"))
        print("{0: <6}{0: <10}{0: <10}".format(""))
        for d in a :
            a_full = d.split (":")
            print("{}".format(a_full))
    elif b == "x" :
        break
    print("`ทำคำสั่งถัดไป")