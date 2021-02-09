def addlist():
    global name,sex,grade,Department,county
    print("-"*20+"แนะนำตัว"+"-"*20)
    addlist = input('ชื่อ-สกุล:เพศ:ชั้นปีที่:สาขาวิชา:จังหวัด')
    addnew = addlist.split(':')
    name = addnew[0]
    sex = addnew[1]
    grade = addnew[2]
    Department = addnew[3]
    county = addnew[4]
class nisit :
    def __init__(self,name,sex,grade,Department,county):
        self.name = name
        self.sex = sex
        self.grade = grade
        self.Department = Department
        self.county = county
    def shownisit(self):
        print(' สวัสดีครับ ชื่อ-นามสกุล:'+self.name + 'เพศ:'+self.sex+ ' ชั้นปีที่:'+self.grade + ' สาขาวิชา:'+self.Department + ' จังหวัด:'+self.county)       
addlist()
x = nisit(name,sex,grade,Department,county)
x.shownisit()