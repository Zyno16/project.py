import mysql.connector

all_err =""
myhost = "localhost"
myuser = "userpython"
mypass = "123456"
mydatabase ="mycompany1"


try:
    cn = mysql.connector.connect(
        host   = myhost,
        user   = myuser,
        passwd  = mypass
     
        )
    cu  =cn.cursor()
    cu.execute("""
            CREATE DATABASE IF NOT EXISTS mycompany1 DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci
            """)
except mysql.connector.Error as e:
    all_err += str(e) +", PLEASE CHECH THE SERVER AND USERNAME ,"




try:
    conn = mysql.connector.connect(
        host   = myhost,
        user   = myuser,
        passwd  =mypass ,
        database = mydatabase
        )
except mysql.connector.Error as e:
    all_err += str(e) +", "

def dbrun(sql):
    try:
        if 'conn' in globals():
            cur = conn.cursor()
            cur.execute( sql )
            conn.commit()
            return True
        else:
            return False

    except mysql.connector.Error as e:
        all_err += str(e) + ","
        return False
 
def dbget(sql):
    try:
        if "conn" in globals():
            cur =conn.cursor()
            cur.execute(sql)
            all_rows =cur.fetchall()
            return all_rows
        else:
            return []
    except mysql.connector.Error as e:
        all_err += str(e) +","
        return []
def dbautonum(table, column):
    try:
        if "conn" in globals():
            cur = conn.cursor()
            cur.execute("SELECT MAX(%s)+1 FROM %s" % (column ,table))
            row = cur.fetchone()
            if row[0] == None: return "1"
            else: return row[0]
        else:
            return ""
    
    except mysql.connector.Error as e:
        all_err += str(e) +","
        return ""              















    

    
