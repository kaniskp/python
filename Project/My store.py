print('{0:<10}{1:<30}{2:<25}{3}'.format('ลำดับ', 'สีเสื้อ', 'ราคา 100 บาท' ,'จำนวน'))
    c.execute('SELECT NO,Color,Price,Quantity FROM dataadmin WHERE NO=1')
    result = c.fetchone()










