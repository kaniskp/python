'''import sqlite3
def insertTousers (fname,lName,email) :
    try :
        conn = sqlite3.connect (r"D:\kanis_python\week6\week6.1.db")
        c = conn.cursor()

        data = ('A','A','A')
        c.executemany('INSERT INTO users (fname,lname,email) VALUES (?,?,?)',data)
        conn.commit ()
        c.close ()

    except sqlite3.Error as e :
        print('Failend to insert : ',e)
    finally :

        if conn :
            conn.close ()

insertTousers('kanyanat','kongpod','kanyanat@gmail.com')
insertTousers ('dom','aom','d@gmail.com')
'''

'''import sqlite3 
conn = sqlite3.connect (r'D:\kanis_python\week6\week6.1.db')
c = conn.cursor()
try :
    data = ('B','B','B'),('C','C','C'),('D','D','D')
    c.executemany('INSERT INTO users (fname,lname,email) VALUES (?,?,?)',data)
    conn.commit ()
    c.close ()
except sqlite3.Error as e :
    print(e)

finally :
    if conn :
        conn.close () '''

'''import sqlite3

conn = sqlite3.connect(r"D:\kanis_python\week6\week6.1.db")
c = conn.cursor()

try : 
    c.execute('SELECT * FROM users ORDER BY id  ')
    conn.commit ()
    result = c.fetchall()
    for x in result :
        print(x)
    c.close()

except sqlite3.Error as e :
    print(e)

finally :
    if conn :
        conn.close () 

import sqlite3
conn = sqlite3.connect (r'D:\kanis_python\week6\week6.1.db')
c = conn.cursor()

try :
    c.execute(' SELECT * FROM users LIMIT 5 OFFSET 2 ')
    result = c.fetchall()
    for x in result :
        print(x)
    c.close ()
    
except sqlite3.Error as e :
    print(e)
    
finally : 
    if conn :
        conn.cloes()
