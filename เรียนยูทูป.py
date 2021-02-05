# โปรแกรม คำนวณค่า BMI
weight = int(input("กรุณากรอกน้ำหนัก : "))
height = float(input("กรุณากรอกส่วนสูง : "))
#คำนวณ เอาส่วนสูงกำลังสองหารน้ำหนัก
height/=100
BMI = weight/height**2
print("ค่า BMI ของคุณเท่ากับ "+str(BMI))