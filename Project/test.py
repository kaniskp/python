'''from tkinter import * 

male_cnt = 0
female_cnt = 0
total_cnt = 0

def on_click(e):
    global male_cnt, female_cnt
    global total_cnt
    gender = e.widget['text']
    if gender =="male":
        male_cnt +=1
        tv_male.set(male_cnt)
    else:
        female_cnt+=1
        tv_female.set(female_cnt)  

    total_cnt +=1
    tv_male.set(male_cnt)
    tv_total.set(f'total={total_cnt}')


root = Tk()
root.option_add('*Font', 'consolas 25')

tv_male=IntVar()
tv_female = IntVar()
tv_total = StringVar()
btn_male=Button(root, text="male", bg="#3399FF",width=8)
btn_male.grid(row=0, column=0)
btn_male.bind("<Button-1>",on_click)
btn_female=Button(root, text="female", bg="#FF69B4",width=8)
btn_female.grid(row=0, column=1)
btn_female.bind("<Button-1>",on_click)
Label(root, textvariable=tv_male, bg="#3399FF").grid(row=1,column=0,sticky="news")
Label(root, textvariable=tv_female, bg="#FF69B4").grid(row=1,column=1,sticky="news")
Label(root, textvariable=tv_total, bg="gold").grid(row=2,columnspan=2,sticky="news")
root.mainloop()'''

'''from tkinter import *
root = Tk()
root.option_add("*Font", "impact 20")
Label(root, text="weight (kg.)").grid(row=0 ,column=0, sticky=E)
Entry(root, width=8).grid(row=0, column=1)
Label(root, text="height(m.)").grid(row=1, column=0, sticky=E)
Label(root, text="BMI").grid(row=2, column=0)
Entry(root, width=8).grid(row=1, column=1)
Button(root, text="calculate").grid(row=3, columnspan=2)
root.mainloop()'''

'''from tkinter import *
from datetime import datetime
def record_transaction(menu_item):
    with open("sales.csv", mode="a", newline='', encoding='UTF-8') as f:
        price = menus[menu_item]
        dt = datetime.now().strftime("%d-%m-%dT%H:%M:%S")
        f.write(f'{menu_item},{price},{dt}\n')
def show(e):
    menu_item = e.widget.cget("text")
    tv_menu.set(f"{menu_item}/ {menus[menu_item]} Baht")
    record_transaction(menu_item)
root =Tk()
root.option_add("*Font","impact 20")
menus = {"mocha":30,"latte":40,"tea":25,"espresso":50 ,"green tea":25 ,"thai tea":25 }
item_per_row =2
tv_menu = StringVar()
for i,k in enumerate(menus.keys()):
    btn= Button(root, text=k,width=15)
    btn.grid(row = i // item_per_row, column = i % item_per_row)
    btn.bind("<Button-1>", show)
Label(root, text="menu", textvariable=tv_menu).grid(columnspan=item_per_row)
root.mainloop()'''
from tkinter import *
import tkinter as tk

window = tk.Tk()
window.option_add('*Font' , 'RSU 20')
window.title ('ED-TA-RO 16')
window.minsize (width=1280 , height=720)

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
def main_menu(): #เสร็จเเล้ว
    w_screen = tk.Frame(window, bg= '#1C1C1C', bd=5)
    w_screen.place(relx=0.1, rely=0.1, relwidth=0.3, relheight=1, anchor='n')

    Button (window, text='กลับสู่หน้าหลัก'  , bg="#8B0000" , fg="#ffffff", width=15, borderwidth=1, command=home).place(relx=0.12, rely=0.35, relwidth=0.18, relheight=0.08, anchor='n')
    Button (window, text='แสดงผังที่นั่ง' , bg="#B22222" , fg="#FFFFFF", width=15, borderwidth=1, command=show).place(relx=0.12, rely=0.45, relwidth=0.18, relheight=0.08, anchor='n')
    Button (window, text='จองที่นั่ง'   , bg="#B22222" , fg="#FFFFFF", width=15, borderwidth=1, command=add_position).place(relx=0.12, rely=0.55, relwidth=0.18, relheight=0.08, anchor='n')
    Button (window, text='ค้นหาที่นั่ง'  , bg="#B22222" , fg="#FFFFFF", width=15, borderwidth=1 , command=seat).place(relx=0.12, rely=0.65, relwidth=0.18, relheight=0.08, anchor='n')
    Button (window, text='ออกจากโปรแกรม' , bg="#8B0000" , fg="#ffffff", width=15, borderwidth=1, command=exit_app).place(relx=0.12, rely=0.75, relwidth=0.18, relheight=0.08, anchor='n')
    Button (window, text='ผู้ดูแลระบบ' , bg="#4f080c" , fg="#ffffff" , width=15, borderwidth=1, command=admin).place(relx=0.12, rely=0.85, relwidth=0.18, relheight=0.08, anchor='n')

def final(): #เสร็จเเล้ว
    main_menu()
    home()
    #window.attributes("-fullscreen",True)
    window.mainloop()

final()