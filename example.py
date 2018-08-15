import mysql.connector

db = mysql.connector.connect(user='root', password='shekhar@mbasic', host='127.0.0.1', port='3306', database='flurr_note')
cr = db.cursor()
cr.execute("select*from users")
q = cr.fetchall()
cr.execute("select*from uid")
w = cr.fetchall()
print(q)
print(w)
