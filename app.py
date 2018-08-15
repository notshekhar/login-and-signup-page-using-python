import mysql.connector
import base64, os, sys
from flask import Flask, jsonify, render_template, url_for, request, redirect, make_response


app = Flask(__name__)
@app.route("/")
def home():
    db = mysql.connector.connect(user='root', password='shekhar@mbasic', host='127.0.0.1', port='3306', database='flurr_note')
    cr = db.cursor()
    uid = request.cookies.get('uid')
    q = "select * from users where userId = '{}'".format(uid)
    cr.execute(q)
    u = cr.fetchall()
    print(len(u))
    cr.close()
    db.close()
    if(uid == None):
        return render_template('index.htm')
    elif(len(u)==0):
        return render_template('index.htm')
    else:
        return redirect(url_for('welcome'))

@app.route("/login", methods=["POST"])
def login():
    db = mysql.connector.connect(user='root', password='shekhar@mbasic', host='127.0.0.1', port='3306', database='flurr_note')
    cr = db.cursor()
    username = request.form.get("username")
    password = request.form.get("password")
    if(len(username)>0 and password != "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"):
        q = "select * from users where username = '{}' and passsword = '{}'".format(username, password)
        cr.execute(q)
        d = cr.fetchall()
        b = "select *from users where username = '{}'".format(username)
        cr.execute(b)
        a = cr.fetchall()
        if(len(d)>0):
            p = "select userId from users where username = '{}'".format(username)
            cr.execute(p)
            uid = cr.fetchall()[0][0]
        cr.close()
        db.close()
        if(len(a)>0):
            if (len(d) > 0):
                data = {'message': 'yes', 'uid': uid}
                return jsonify(data)
            else:
                return jsonify(message= 'Incorrect password')
        else:
            return jsonify(message= "Username doesn't exist")
    else:
        return jsonify(message= 'Fill all the fields')



@app.route("/signup", methods=['POST'])
def signup():
    db = mysql.connector.connect(user='root', password='shekhar@mbasic', host='127.0.0.1', port='3306', database='flurr_note')
    cr = db.cursor()
    cr.execute('select*from uid')
    uid = cr.fetchall()[0][0]
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')
    uq = "select*from users where username = '{}'".format(username)
    cr.execute(uq)
    uc = cr.fetchall()
    eq = "select*from users where email = '{}'".format(email)
    cr.execute(eq)
    ec = cr.fetchall()
    if(len(username)>0 and len(password)>0 and len(email)>0):
        if(len(uc)>0 and len(ec)>0):
            return jsonify(message = 'Username and Email are already exist')
        elif(len(ec)>0):
            return jsonify(message = 'Email is already exist')
        elif(len(uc)>0):
            return jsonify(message = 'Username already exist')
        else:
            p = "insert into users values('{}', {}, '{}', '{}')".format(username, uid, password, email)
            cr.execute(p)
            data = {'message': 'yes', 'uid': uid}
            # update uid
            uid+=1
            m = "update uid set uid = {}".format(uid)
            cr.execute(m)
            db.commit()
            cr.close()
            db.close()
            return jsonify(data)
    else:
        return jsonify(message = "You can't leave any of these field empty")

@app.route('/home')
def welcome():
    db = mysql.connector.connect(user='root', password='shekhar@mbasic', host='127.0.0.1', port='3306', database='flurr_note')
    cr = db.cursor()
    uid = request.cookies.get('uid')
    q = "select * from users where userId = '{}'".format(uid)
    cr.execute(q)
    u = cr.fetchall()
    cr.close()
    db.close()
    if(uid == None):
        return redirect(url_for('home'))
    elif(len(u)==0):
        return redirect(url_for('home'))
    else:
        return render_template('home.htm', un=u[0][0], email=u[0][3],)

if __name__ == '__main__':
    app.run(debug="development")
