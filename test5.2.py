num = 0 
products_ =[]
rates_ = []
class shop :
    def __init__(self,products,rates):
        self.products = products
        self.rates = rates
    def showshop(self):
        print(i+1,'.',self.products,self.rates,' บาท')
    def show():
        print('-'*20,'ร้านนายดอม','-'*20)
        print('\tแสดงรายการสินค้า [a]\n\tเพิ่มรายการสินค้า[s]\n\tออกจากระบบ[x]')

while True :
    shop.show() 
    menu = input('กรุณาเลือกคำสั่ง :   ')
    if menu == 'a':
        for i in range(num):
            x = shop(products_[i],rates_[i])
            x.showshop()
    if menu == 's' :
        while True :
            print('เพิ่มรายการสินค้า หากต้องการยกเลิกให้กรอก exit')
            g = input('เพิ่มชื่อสินค้า :\t')
            if  g == 'exit' :
                break
            else:
                products_.append(g) 
                r = input('ใส่ราคาของ'+g+': ')
                rates_.append(r)
                print('-'*5+'[บันทึกข้อมูลสินค้าแล้ว]'+'-'*5)
                num +=1
                yn = input('ต้องการเพิ่มสินค้าอีกหรือไม่(y/n): ')
                if yn == 'n' :
                    break
    if menu == 'x' :
        yn = input('ต้องการออกจากระบบหรือไม่(y/n): ')
        if yn == 'y' :
            break
    
