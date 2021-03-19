from tkinter import *
import tkinter as tk
import sqlite3

window = tk.Tk()
window.option_add('*Font' , 'RSU 20')
window.title ('ED-TA-RO 16')
window.minsize (width=1280 , height=720)

def insertTousers (NAME,Tel,Round,Position) :
    try :
        conn = sqlite3.connect(r"D:\python\Project - Copy\data1.db")
        c = conn.cursor()

        sql = 'INSERT INTO edtaro (NAME,Tel,Round,Position) VALUES (?,?,?,?)'
        data = (NAME,Tel,Round,Position)
        c.execute (sql,data)
        conn.commit()
        c.close()

    except sqlite3.Error as e:
        print('เตือน : ไม่สามารถนำข้อมูลเข้า Database',e)

    finally :
        if conn :
            print('เตือน : ข้อมูลเข้า Database เสร็จสิ้น')
            conn.close ()

def home(): #เสร็จแล้ว
    w_screen = tk.Frame(window, bg= '#f0f0f0', bd=5)
    w_screen.place(relx=0.6, rely=0.35, relwidth=0.65, relheight=0.70, anchor='n')

    frame = tk.Frame(window, bg='#828282', bd=6)
    frame.place(relx=0.62, rely=0.35, relwidth=0.65, relheight=0.34, anchor='n')

    textblock = Label (frame, text="คำแนะนำการใช้โปรเเกรม\n---------------------\nเลือกเมนูที่ต้องการใช้งาน หากสิ้นสุดการทำงาน กดเลือกเมนู [กลับสู่หน้าหลัก] หรือ [ออกจากโปรแกรม]\n\nภาคเรียนที่ 2  ปีการศึกษา 2563\nสาขาวิชาคอมพิวเตอร์ศึกษา คณะศึกษาศาสตร์ มหาวิทยาลัยขอนแก่น",bg="#FFFFFF")
    textblock.place(relwidth=1, relheight=1)

    name = tk.Frame(window, bg='#1C1C1C', bd=6)
    name.place(relx=0.62, rely=0.71, relwidth=0.65, relheight=0.22, anchor='n')

    textblock = Label (name, text="จัดทำโดย\n1.นางสาวจิรดา บุญหนัก  รหัสนักศึกษา 633050128-3\n2.นายรัฐเกียรติ หริ่มเพ็ง  รหัสนักศึกษา 633050137-2",bg="#1C1C1C",fg="#FFFFFF",bd=1)
    textblock.place(relwidth=1, relheight=1)

def exit_app(): #เสร็จแล้ว
    w_screen = tk.Frame(window, bg= '#f0f0f0', bd=5)
    w_screen.place(relx=0.62, rely=0.35, relwidth=0.67, relheight=0.70, anchor='n')

    #Label (window, text="ออกจากโปรเเกรม",bg="#1C1C1C",fg="#FFFFFF").place(relx=0.62, rely=0.35, relwidth=0.65, relheight=0.08, anchor='n')
    
    frame = tk.Frame(window, bg='#f0f0f0', bd=6)
    frame.place(relx=0.62, rely=0.50, relwidth=0.6, relheight=0.07, anchor='n')
            
    nameblock = Label (frame, text="ยึนยันการปิดโปรแกรม")
    nameblock.place(relwidth=1, relheight=1)

    button = tk.Button(window,text='ตกลง', bg="#660000" , fg="#FFFFFF",command=window.destroy)
    button.place(relx=0.49,rely=0.60, relwidth=0.2, anchor='n')
    
    button = tk.Button(window,text='ยกเลิก', bg="#660000" , fg="#FFFFFF",command=home)
    button.place(relx=0.75,rely=0.60, relwidth=0.2, anchor='n')

def add_position(): #เสร็จแล้ว
    def adddata_position():
        #รับข้อมูลชื่อ
        frame = tk.Frame(window, bg='#828282', bd=6)
        frame.place(relx=0.62, rely=0.45, relwidth=0.6, relheight=0.07, anchor='n')
            
        nameblock = Label (frame, text="ชื่อผู้จอง")
        nameblock.place(relwidth=0.3, relheight=1)

        textblock1 = tk.Entry(frame)
        textblock1.place(relx=0.31,relwidth=0.69, relheight=1)

        #รับข้อมูลเบอร์โทรศัพท์
        frame = tk.Frame(window, bg='#828282', bd=6)
        frame.place(relx=0.62, rely=0.53, relwidth=0.6, relheight=0.07, anchor='n')
            
        nameblock = Label (frame, text="เบอร์โทรศัพท์")
        nameblock.place(relwidth=0.3, relheight=1)

        textblock2 = tk.Entry(frame)
        textblock2.place(relx=0.31,relwidth=0.69, relheight=1)

        #รับข้อมูลรอบการแสดง
        frame = tk.Frame(window, bg='#828282', bd=6)
        frame.place(relx=0.62, rely=0.61, relwidth=0.6, relheight=0.07, anchor='n')
            
        nameblock = Label (frame, text="รอบการแสดง")
        nameblock.place(relwidth=0.3, relheight=1)

        textblock3 = tk.Entry(frame)
        textblock3.place(relx=0.31,relwidth=0.69, relheight=1)

        #รับข้อมูลตำแหน่งที่นั่ง
        frame = tk.Frame(window, bg='#828282', bd=6)
        frame.place(relx=0.62, rely=0.69, relwidth=0.6, relheight=0.07, anchor='n')
            
        nameblock = Label (frame, text="ตำแหน่งที่นั่ง")
        nameblock.place(relwidth=0.3, relheight=1)

        textblock4 = tk.Entry(frame)
        textblock4.place(relx=0.31,relwidth=0.69, relheight=1)
    
        def savedata_position() :
            data11 = str(textblock1.get())
            data12 = str(textblock2.get())
            data13 = str(textblock3.get())
            data14 = str(textblock4.get())

            frame = tk.Frame(window, bg='#f0f0f0', bd=6)
            frame.place(relx=0.6, rely=0.77, relwidth=0.6, relheight=0.07, anchor='n')
            
            nameblock = Label (frame, text="บันทึกข้อมูลเข้าระบบเรียบร้อย ออกจากหน้านี้ กดเลือกเมนู [กลับสู่หน้าหลัก]")
            nameblock.place(relwidth=1, relheight=1)

            print('เก็บข้อมูลการจองเข้าตัวแปรแล้ว : '+data11+' '+data12+' '+data13+' '+data14)

            insertTousers(data11,data12,data13,data14)

        #ปุ่มบันทึกข้อมูล
        button = tk.Button(window,text='จองที่นั่ง และ บันทึกข้อมูล',bg="#660000" , fg="#FFFFFF",command=savedata_position)
        button.place(relx=0.62,rely=0.85, relwidth=0.5, anchor='n')

    #คำสั่งล้างหน้าจอสร้างพื้นที่ขาวทับ
    w_screen = tk.Frame(window, bg= '#f0f0f0', bd=5)
    w_screen.place(relx=0.6, rely=0.35, relwidth=0.7, relheight=0.58, anchor='n')
    
    Label (window, text="จองที่นั่ง",bg="#1C1C1C" , fg="#FFFFFF").place(relx=0.62, rely=0.35, relwidth=0.65, relheight=0.08, anchor='n')
    
    adddata_position()

def show():
    def show_position():
        #คำสั่งล้างหน้าจอสร้างพื้นที่ขาวทับ
        w_screen = tk.Frame(window, bg= '#f0f0f0', bd=5)
        w_screen.place(relx=0.62, rely=0.35, relwidth=0.7, relheight=0.58, anchor='n')
    
        Label (window, text="แสดงผังที่นั่ง",bg="#1C1C1C" , fg="#FFFFFF").place(relx=0.62, rely=0.35, relwidth=0.65, relheight=0.08, anchor='n')
    
    def stage():
        #รอบการแสดง
        frame = tk.Frame(window, bg='#828282', bd=6)
        frame.place(relx=0.62, rely=0.61, relwidth=0.6, relheight=0.07, anchor='n')
            
        nameblock = Label (frame, text="รอบการแสดง")
        nameblock.place(relwidth=0.3, relheight=1)

        textblock3 = tk.Entry(frame)
        textblock3.place(relx=0.31,relwidth=0.69, relheight=1)
        data13 = str(textblock3.get())

        #เวที
        stage = Label (window, text="เวที",bg="#CD853F" , fg="#FFFFFF")
        stage.place(relx=0.62, rely=0.42, relwidth=0.65, relheight=0.05, anchor='n')

    show_position()
    stage()

def seat() : #รับค่าเข้าตัวแปรได้แล้ว เหลือค้นหาเขตข้อมูลที่ตรงกันใน sql เเล้วดึงค่าตำแหน่งกลับมา
    def adddata_seat():
        #รับข้อมูลตำแหน่งชื่อ
        frame = tk.Frame(window, bg='#828282', bd=6)
        frame.place(relx=0.62, rely=0.45, relwidth=0.6, relheight=0.07, anchor='n')
            
        nameblock = Label (frame, text="ชื่อที่ใช้จอง")
        nameblock.place(relwidth=0.3, relheight=1)

        textblock1 = tk.Entry(frame)
        textblock1.place(relx=0.31,relwidth=0.69, relheight=1)

        #รับข้อมูลเบอร์โทรศัพท์
        frame = tk.Frame(window, bg='#828282', bd=6)
        frame.place(relx=0.62, rely=0.53, relwidth=0.6, relheight=0.07, anchor='n')
            
        nameblock = Label (frame, text="เบอร์โทรศัพท์")
        nameblock.place(relwidth=0.3, relheight=1)

        textblock2 = tk.Entry(frame)
        textblock2.place(relx=0.31,relwidth=0.69, relheight=1)

        #รับข้อมูลรอบการแสดง
        frame = tk.Frame(window, bg='#828282', bd=6)
        frame.place(relx=0.62, rely=0.61, relwidth=0.6, relheight=0.07, anchor='n')
            
        nameblock = Label (frame, text="รอบการแสดง")
        nameblock.place(relwidth=0.3, relheight=1)

        textblock3 = tk.Entry(frame)
        textblock3.place(relx=0.31,relwidth=0.69, relheight=1)

        def saveseat() :
            data21 = str(textblock1.get())
            data22 = str(textblock2.get())
            data23 = str(textblock3.get())

            frame = tk.Frame(window, bg='#f0f0f0', bd=6)
            frame.place(relx=0.6, rely=0.70, relwidth=0.6, relheight=0.15, anchor='n')
            
            nameblock = Label (frame, text="")
            nameblock.place(relwidth=1, relheight=1)

            nameblock = Label (frame, text="ตำแหน่งที่นั่งของคุณ : "+"text"+"\nออกจากหน้านี้ กดเลือกเมนู [กลับสู่หน้าหลัก]")
            nameblock.place(relwidth=1, relheight=1)

            print('รับค่าค้นหาชื่อเข้าตัวแปรแล้ว : '+data21+' '+data22+' '+data23)
        
        #ปุ่มค้นหาที่นั่ง
        button = tk.Button(window,text='ค้นหาที่นั่ง',bg="#660000" , fg="#FFFFFF",command=saveseat)
        button.place(relx=0.62,rely=0.85, relwidth=0.5, anchor='n')
        ### เหลือ output ผลการค้นหาที่นั่ง ###
    
    w_screen = tk.Frame(window, bg= '#f0f0f0', bd=5)
    w_screen.place(relx=0.6, rely=0.35, relwidth=0.7, relheight=0.58, anchor='n')
    
    Label (window, text="ค้นหาที่นั่ง",bg="#1C1C1C" , fg="#FFFFFF").place(relx=0.62, rely=0.35, relwidth=0.65, relheight=0.08, anchor='n')
    
    adddata_seat()

def head_app(): #เสร็จแล้ว
    Label (window, text="โปรเเกรมจองที่นั่งละครเวทีคณะศึกษาศาสตร์ ED-TA-RO 16 กุหลาบปากซัน The Musical 2564",
        width=200 , bg="#660000" , fg="#FFFFFF").pack()
    Label (window, text="Develop by Computer Education 17 | Khon Kean University",
        width=200 , bg="#660000" , fg="#FFFFFF").pack()
    Label (window, text="",width=200 , bg="#7e0f15").pack()

def admin():
    w_screen = tk.Frame(window, bg= '#f0f0f0', bd=5)
    w_screen.place(relx=0.62, rely=0.35, relwidth=0.67, relheight=0.70, anchor='n')

    def login():
        frame = tk.Frame(window, bg='#828282', bd=6)
        frame.place(relx=0.62, rely=0.61, relwidth=0.6, relheight=0.07, anchor='n')
            
        nameblock = Label (frame, text="กรุณาใส่รหัสผ่าน")
        nameblock.place(relwidth=0.3, relheight=1)

        textblock = tk.Entry(frame)
        textblock.place(relx=0.31,relwidth=0.69, relheight=1)

        def checkpass() :
            password = str(textblock.get())   

            if password=='comed17' :
                def adminmenu():
                    import os
                    w_screen = tk.Frame(window, bg= '#f0f0f0', bd=5)
                    w_screen.place(relx=0.6, rely=0.35, relwidth=0.7, relheight=0.58, anchor='n')
                    
                    Label (window, text="ผู้ดูแลระบบ",bg="#1C1C1C" , fg="#FFFFFF").place(relx=0.62, rely=0.35, relwidth=0.65, relheight=0.08, anchor='n')

                    def openSQLite():
                        filename = '"C:\\Program Files\\DB Browser for SQLite\\DB Browser for SQLite.exe"'
                        os.system(filename)
                    
                    button = tk.Button(window,text='เปิดโปรแกรม SQLite', bg="#000000" , fg="#FFFFFF",command=openSQLite)
                    button.place(relx=0.62,rely=0.5, relwidth=0.2, anchor='n')
                adminmenu()

                nameblock = Label (frame, text="บันทึกข้อมูลเข้าระบบเรียบร้อย ออกจากหน้านี้ กดเลือกเมนู [กลับสู่หน้าหลัก]")
                nameblock.place(relwidth=1, relheight=1)

            else :
                w_screen = tk.Frame(window, bg= '#f0f0f0', bd=5)
                w_screen.place(relx=0.6, rely=0.35, relwidth=0.7, relheight=0.58, anchor='n')

                frame = tk.Frame(window, bg='#f0f0f0', bd=6)
                frame.place(relx=0.6, rely=0.6, relwidth=0.6, relheight=0.07, anchor='n')
                
                nameblock = Label (frame, text="รหัสผ่านไม่ถูกต้อง")
                nameblock.place(relwidth=1, relheight=1)
        
        #ปุ่มบันทึกข้อมูล
        button = tk.Button(window,text='เข้าสู่ระบบ',bg="#660000" , fg="#FFFFFF",command=checkpass)
        button.place(relx=0.62,rely=0.70, relwidth=0.5, anchor='n')
    
    login()

def main_menu(): #เสร็จเเล้ว
    w_screen = tk.Frame(window, bg= '#1C1C1C', bd=5)
    w_screen.place(relx=0.1, rely=0.1, relwidth=0.3, relheight=1, anchor='n')

    Button (window, text='กลับสู่หน้าหลัก'  , bg="#8B0000" , fg="#ffffff", width=15, borderwidth=1, command=home) .place(relx=0.12, rely=0.35, relwidth=0.18, relheight=0.08, anchor='n')
    Button (window, text='แสดงผังที่นั่ง' , bg="#B22222" , fg="#FFFFFF", width=15, borderwidth=1, command=show).place(relx=0.12, rely=0.45, relwidth=0.18, relheight=0.08, anchor='n')
    Button (window, text='จองที่นั่ง'   , bg="#B22222" , fg="#FFFFFF", width=15, borderwidth=1, command=add_position) .place(relx=0.12, rely=0.55, relwidth=0.18, relheight=0.08, anchor='n')
    Button (window, text='ค้นหาที่นั่ง'  , bg="#B22222" , fg="#FFFFFF", width=15, borderwidth=1 , command=seat) .place(relx=0.12, rely=0.65, relwidth=0.18, relheight=0.08, anchor='n')
    Button (window, text='ออกจากโปรแกรม' , bg="#8B0000" , fg="#ffffff", width=15, borderwidth=1, command=exit_app)  .place(relx=0.12, rely=0.75, relwidth=0.18, relheight=0.08, anchor='n')
    Button (window, text='ผู้ดูแลระบบ' , bg="#4f080c" , fg="#ffffff" , width=15, borderwidth=1, command=admin)  .place(relx=0.12, rely=0.85, relwidth=0.18, relheight=0.08, anchor='n')

def final(): #เสร็จเเล้ว
    main_menu()
   
    Label (window , image=photo , borderwidth=0).pack()
    head_app()
    home()
    #window.attributes("-fullscreen",True)
    window.mainloop()

final()