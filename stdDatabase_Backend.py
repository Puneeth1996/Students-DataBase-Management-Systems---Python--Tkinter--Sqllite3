import sqlite3
#backend


def studentData():
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY,stdID text,FIRSTNAME text,SURNAME text,DOB text,AGE text,GENDER text,MOBILE text)")
    con.commit()
    con.close()

def addStdRec(stdID,FIRSTNAME,SURNAME,DOB,AGE,GENDER,MOBILE):
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("INSERT INTO student VALUES (NULL,?,?,?,?,?,?,?)",(stdID,FIRSTNAME,SURNAME,DOB,AGE,GENDER,MOBILE))
    con.commit()
    con.close()

def viewData():
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM student")
    rows=cur.fetchall()
    con.close()
    return rows

def deleteRec(id):
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("DELETE FROM student WHERE id=?",(id,))
    con.commit()
    con.close()
    
def searchData(stdID="",FIRSTNAME="",SURNAME="",DOB="",AGE="",GENDER="",MOBILE=""):
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM student WHERE stdID=? OR FIRSTNAME=? OR SURNAME=? OR DOB=? OR AGE=? OR GENDER=? OR MOBILE=?",(stdID,FIRSTNAME,SURNAME,DOB,AGE,GENDER,MOBILE))
    rows=cur.fetchall()
    con.close()
    return rows

def dataUpdate(id,stdID="",FIRSTNAME="",SURNAME="",DOB="",AGE="",GENDER="",MOBILE=""):
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("UPDATE student SET stdID=?,FIRSTNAME=?,SURNAME=?,DOB=?,AGE=?,GENDER=?,MOBILE=?,WHERE id=?",(stdID,FIRSTNAME,SURNAME,DOB,AGE,GENDER,MOBILE,id))
    con.commit()
    con.close()
    


studentData()




