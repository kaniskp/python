from tkinter import *
import tkinter as tk
import sqlite3 as db
import sqlite3
conn = sqlite3.connect(r'D:\kanis_python\Project\My store.db')
c = conn.cursor()


root = tk.Tk()
root.option_add('*Font' , 'RSU 20')
root.title ('My Store Yuedpao')
root.minsize (width=1200 , height=720)


    
    
def main_menu() :
    Frame(root, bg="#CCCCCC",bd=5).place(relx=0.15,rely=0.3,relwidth=0.7,relheight=0.6)
    frame = Frame(root, bg="#FFFFFF",bd=8)
    Label(frame,text="T-Shit Yuedpao").place(relwidth=1,relheight=1)
    frame.place(relx=0.4, rely=0.27, relwidth=0.2, relheight=0.1)
    Button(root ,text ="👕เข้าสู่ระบบ",command=showshop).place(relx=0.4, rely=0.44,relwidth=0.2,relheight=0.1)
    Button(root ,text ="🔑เข้าสู่ระบบโดยผู้ดูแล",command=intendant).place(relx=0.4, rely=0.59,relwidth=0.2,relheight=0.1)
    Button(root ,text ="⛔ออกจากระบบ",command = Exit).place(relx=0.2, rely=0.79,relwidth=0.2,relheight=0.1)
def Exit():
    Frame(root, bg="#CCCCCC",bd=5).place(relx=0.15,rely=0.3,relwidth=0.7,relheight=0.6)
    frame = Frame(root, bg="#FFFFFF",bd=8)
    Label(frame,text="ต้องการออกจากระบบหรือไม่").place(relwidth=1,relheight=1)
    frame.place(relx=0.4, rely=0.27, relwidth=0.2, relheight=0.1)
    Button(root, text="ยืนยัน", command=root.destroy).place(relx=0.2, rely=0.5,relwidth=0.2,relheight=0.1)
    Button(root, text="ยกเลิก", command=main_menu).place(relx=0.6, rely=0.5,relwidth=0.2,relheight=0.1)
    
def todata():
    global name
    name = p.get()
    c.execute('INSERT INTO Order (NO) values=?',name)
    
def showshop():
    global p
    Frame(root, bg="#CCCCCC",bd=5).place(relx=0.15,rely=0.3,relwidth=0.7,relheight=0.6)
    frame = Frame(root, bg="#FFFFFF",bd=8)
    frame.place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.1)
    Label(frame,text="ผู้ใช้งาน").place(relwidth=1,relheight=1)
    frame.place(relx=0.4, rely=0.27, relwidth=0.2, relheight=0.1)
    Button(root, text="เลือกสินค้า", command = todata).place(relx=0.18, rely=0.4,relwidth=0.16,relheight=0.07)
    p = Entry(master = root).place(relx=0.21, rely=0.5,relwidth=0.1,relheight=0.05)
    Button(root, text="แก้ไขการเลือกสินค้า",command=modify).place(relx=0.18, rely=0.6,relwidth=0.16,relheight=0.07)
    Button(root, text="ยืนยันคำสั่งการซื้อ",command=confirm).place(relx=0.18, rely=0.7,relwidth=0.16,relheight=0.07)
    Button(root, text="หน้าหลัก",command=main_menu).place(relx=0.18, rely=0.8,relwidth=0.16,relheight=0.07)
    photo= PhotoImage(file=r"D:\kanis_python\Project\PJ fc\iloveimg-resized\ขาว1.png" )
    Label(root, image=photo,).place(relx=0.45, rely=0.4)
    photo1= PhotoImage(file=r"D:\kanis_python\Project\PJ fc\iloveimg-resized\ดำ1.png" )
    Label(root, image=photo1).place(relx=0.6 ,rely=0.4)
    photo2= PhotoImage(file=r"D:\kanis_python\Project\PJ fc\iloveimg-resized\เทาเข้ม1.png" )
    Label(root, image=photo2).place(relx=0.74 ,rely=0.4)
    photo3= PhotoImage(file=r"D:\kanis_python\Project\PJ fc\iloveimg-resized\เขียว1.png" )
    Label(root, image=photo3).place(relx=0.45, rely=0.57)
    photo4= PhotoImage(file=r"D:\kanis_python\Project\PJ fc\iloveimg-resized\น้ำเงิน1.png" )
    Label(root, image=photo4).place(relx=0.6 ,rely=0.57)
    photo5= PhotoImage(file=r"D:\kanis_python\Project\PJ fc\iloveimg-resized\เลือดหมู1.png" )
    Label(root, image=photo5).place(relx=0.74 ,rely=0.57)
    photo6= PhotoImage(file=r"D:\kanis_python\Project\PJ fc\iloveimg-resized\เหลือง1.png" )
    Label(root, image=photo6).place(relx=0.45 ,rely=0.75)
    photo7= PhotoImage(file=r"D:\kanis_python\Project\PJ fc\iloveimg-resized\พีข1.png" )
    Label(root, image=photo7).place(relx=0.6 ,rely=0.75)
    photo8= PhotoImage(file=r"D:\kanis_python\Project\PJ fc\iloveimg-resized\ลาเวนเดอร์1.png" )
    Label(root, image=photo8).place(relx=0.74 ,rely=0.75)
    root.mainloop()

def modify():
    Frame(root, bg="#CCCCCC",bd=5).place(relx=0.15,rely=0.3,relwidth=0.7,relheight=0.6)
    frame = Frame(root, bg="#FFFFFF",bd=8)
    frame.place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.1)
    Label(frame,text="แก้ไขรายการสินค้า").place(relwidth=1,relheight=1)
    frame.place(relx=0.4, rely=0.27, relwidth=0.2, relheight=0.1)
    Button(root, text="หน้าหลัก",command=main_menu).place(relx=0.18, rely=0.69,relwidth=0.16,relheight=0.09)
    Button(root,text="ยืนยันการเพิ่มสินค้า").place(relx=0.18, rely=0.4,relwidth=0.16,relheight=0.09)
    Button(root,text="ยืนยันการลบสินค้า").place(relx=0.18, rely=0.55,relwidth=0.16,relheight=0.09)

def confirm():
    Frame(root, bg="#CCCCCC",bd=5).place(relx=0.15,rely=0.3,relwidth=0.7,relheight=0.6)
    frame = Frame(root, bg="#FFFFFF",bd=8)
    frame.place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.1)
    Label(frame,text="ยืนยันการซื้อสินค้า").place(relwidth=1,relheight=1)
    frame.place(relx=0.4, rely=0.27, relwidth=0.2, relheight=0.1)
    Button(root, text="หน้าหลัก",command=main_menu).place(relx=0.18, rely=0.7,relwidth=0.16,relheight=0.09)
    Button(root, text="ยืนยันรายการ").place(relx=0.18, rely=0.48,relwidth=0.16,relheight=0.09)
    Button(root, text="ยกเลิกรายการ").place(relx=0.18, rely=0.59,relwidth=0.16,relheight=0.09)

def intendant():
    Frame(root, bg="#CCCCCC",bd=5).place(relx=0.15,rely=0.3,relwidth=0.7,relheight=0.6)
    frame = Frame(root, bg="#FFFFFF",bd=8)
    frame.place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.1)

    Label(frame,text="ผู้ดูแลระบบ").place(relwidth=1,relheight=1)
    frame.place(relx=0.4, rely=0.27, relwidth=0.2, relheight=0.1)

    Button(root, text="หน้าหลัก",command=main_menu).place(relx=0.425, rely=0.7,relwidth=0.16,relheight=0.09)
    Label(root,text="กรุณาใส่รหัส").place(relx=0.47, rely=0.4)
    Entry(root,tex="",width=6,show="*").place(relx=0.32, rely=0.5,relwidth=0.35,relheight=0.05)
    
    def clickpw():
        password == str(blockpw.get())
        if password=="tshit100" :
            def intendant2():
                Frame(root, bg="#CCCCCC",bd=5).place(relx=0.15,rely=0.3,relwidth=0.7,relheight=0.6)
                frame = Frame(root, bg="#FFFFFF",bd=8)
                frame.place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.1)
                Label(frame,text="ผู้ดูแลระบบ").place(relwidth=1,relheight=1)
                frame.place(relx=0.4, rely=0.27, relwidth=0.2, relheight=0.1)
        

        
def index():
    photo = PhotoImage(file = 'D:\\kanis_python\\Project\\photoo.png')
    Label(root, image= photo).pack()  
    main_menu()
    root.mainloop()


index()
conn.commit()
conn.close()

