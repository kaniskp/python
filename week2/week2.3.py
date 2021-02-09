i=1
n=1
print('+'*50)
print('\t\tโปรแกรมหยิบสินค้าใส่ตะกร้า')
print('+'*50)
productset = {'ไก่ทอด','หมูทอด','ส้มตำ','คอหมูย่าง','ลาบ'}
for x in productset :
    print('\t\tหยิบสินค้าชิ้นที่ '+str(i)+'\t'+x)
    i+=1
print('\t\tสินค้าหยิบใส่ตะกน้ามีดังนี้')
for x in productset :
    print('\t\t'+str(n)+'.'+x)
    n+=1


