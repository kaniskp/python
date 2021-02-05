stu = int(input('จำนวนนักเรียนที่จะกรอกคะแนน :'))
tot = [0 , 0 , 0 , 0 , 0 , 0]
sco= ['90-100 : ','80-89 : ','70-79 : ','60-69 : ','50-59 : ','0-49 : ']
x = 1
while x<=stu:
    p = int(input("คะแนนนักเรียน :"))
    if p <= 100 and p >= 90 :
        tot[0] += 1
    elif p < 90 and p >= 80 :
        tot[1] += 1
    elif p < 80 and p >= 70 :
        tot[2] += 1
    elif p < 70 and p >= 60 :
        tot[3] += 1
    elif p < 60 and p >= 50 :
        tot[4] += 1
    elif p< 50 and p>= 0 :
        tot[5] += 1
    x = x+1
for x in range(0,6) :
    print(sco[x],"*"*tot[x])