print("โปรแกรมรับค่าระยะทาง เพื่อคิดค่าบริการ\n")
print("เลือกเมนูเพื่อทำรายการ\n#####################")
print(" กด 1 เลือกเหมาจ่าย\n กด 2 เลือกจ่ายเพิ่ม")
a = int(input("  "))
s = int(input(" กรุณากรอกระยะทาง : "))
if a == 1 :
    if s <= 25 :
        print(" ค่าใช้จ่ายทั้งหมด 25 บาท ")
    else :
        print(" ค่าใช้จ่ายทั้งหมด 55 บาท ")  
if a == 2 :
    if s <= 25 :
        print(" ค่าใช้จ่ายทั้งหมด 25 บาท ")
    else :
        print(" ค่าใช้จ่ายทั้งหมด 80 บาท ")

