listshop=[0,0,0,0,0]
cost=[5,10,15,20,25]
def menu():
	global choice
	print('        ขนมแสนอร่อยของคุณ        \n 1. แสดงรายการสินค้า\n 2. หยิบสินค้าใส่ตะกร้า\n 3.แสดงรายการจำนวนและราคาสินค้าที่หยิบ\n 4.หยิบสิค้าออกจากตะกร้า\n 5.ปิดโปรแกรม ')
	choice = input('กรุณาเลือกทำรายการ : ')

def costmenu():
	print('\n1. นิชชิน เวเฟอร์  ราคา 5 บาท \n 2. โอรีโอ เวเฟอร์โรล  ราคา 10 บาท\n 3. เวเฟอร์ อิมพีเรียล  ราคา 15 บาท\n 4. กัสเซ็น เวเฟอร์  ราคา 20 บาท\n 5. คิทแคท มัลติแพ็ค  ราคา 25 บาท\n ')

def pickmenu():
	global pick
	print('\nรายากรสินค้า\n 1.นิชชิน เวเฟอร์ \n 2.โอรีโอ เวเฟอร์โรล\n 3.เวเฟอร์ อิมพีเรียล\n 4. กัสเซ็น เวเฟอร์\n 5. คิทแคท มัลติแพ็ค')
	pick = int(input('เลือกหยิบสินค้าหมายเลข : '))
	if pick == 1:
		listshop[0] += 1
	elif pick == 2:
		listshop[1] += 1
	elif pick == 3:
		listshop[2] += 1
	elif pick == 4:
		listshop[3] += 1
	elif pick == 5:
		listshop[4] += 1

def allpick():
	list_cookie = ["นิชชิน เวเฟอร์" ,"โอรีโอ เวเฟอร์โรล" ,"เวเฟอร์ อิมพีเรียล" ,"กัสเซ็น เวเฟอร์" ,"คิทแคท มัลติแพ็ค"]
	list_cost = [5,10,15,20,25]
	print("{0:-<10}{2:-<10}{3}".format("นิชชิน เวเฟอร์" ,"โอรีโอ เวเฟอร์โรล" ,"เวเฟอร์ อิมพีเรียล" ,"กัสเซ็น เวเฟอร์" ,"คิทแคท มัลติแพ็ค"))
	for i in range(0,5):
		print("{0:-<10}{2:-<10}{3}".format(list_cookie[i],list_cost[i],listshop[i],listshop[i]*list_cost[i]))

def outpick():
	print('รายการสินค้า\n 1.นิชชิน เวเฟอร์\n 2.โอรีโอ เวเฟอร์โรล\n 3.เวเฟอร์ อิมพีเรียล\n 4.กัสเซ็น เวเฟอร์\n 5.คิทแคท มัลติแพ็ค')
	outpick = int(input("เลือกลำดับสินค้าที่จะหยิบออก หรือพิมพ์ -1 เพื่อออก"))
	if outpick == 1:
		listshop[0] -=1
	elif outpick == 2:
		listshop[1] -=1
	elif outpick == 3:
		listshop[2] -=1
	elif outpick == 4:
		listshop[3] -=1
	elif outpick == 5:
		listshop[4] -=1

while True:
	menu()
	if choice == '1':
		costmenu()
	elif choice == '2':
		pickmenu()
	elif choice == '3':
		allpick()
	elif choice == '4':
		outpick()
	elif choice == '5':
		ch = input("ต้องการใช้งานโปรแกรมต่อหรือไม่ y/n: ")
		if ch == 'y':
		   break
		elif ch == 'n':
		   continue
