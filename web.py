from flask import Flask, render_template, request, redirect, url_for
import pymysql as sql

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("home1.html")


@app.route('/home')
def index1():
    return render_template("home1.html")


@app.route('/aboutUs')
def index2():
    return render_template("aboutUs.html")


@app.route('/contact')
def index3():
    return render_template("contact.html")


@app.route('/register')
def index4():
    return render_template("register.html")

@app.route('/update')
def index5():
    return render_template("update.html")

@app.route('/update1')
def index6():
    name = request.args.get('qname')
    enrol = request.args.get('qenrol')
    password = request.args.get('qpass')
    email = request.args.get('qemail')
    number = request.args.get('qphone')
    tech = request.args.get('qtech')
    start = request.args.get('qstart')
    batch = request.args.get('qbatch')
    conn = sql.connect(host='localhost', port=3306, user='root', passwd='mayank', db='kvch_database')
    cusr = conn.cursor()
    cusr.execute(
        "update student_registration set enrollment='%s',email='%s',number='%s',technology='%s',start_date='%s',batchid='%s' where name ='%s'and password = '%s';" % (
            enrol, email, number, tech, start, batch,name,password))
    conn.commit()
    conn.close()
    return render_template("user.html")


@app.route('/register1')
def index7():
    name = request.args.get('qname')
    enrol = request.args.get('qenrol')
    password = request.args.get('qpass')
    email = request.args.get('qemail')
    number = request.args.get('qphone')
    tech = request.args.get('qtech')
    start = request.args.get('qstart')
    batch = request.args.get('qbatch')
    conn = sql.connect(host='localhost', port=3306, user='root', passwd='mayank', db='kvch_database')
    cusr = conn.cursor()
    cusr.execute("insert into student_registration values('%s','%s','%s','%s','%s','%s','%s','%s');" % (
        name, enrol, password, email, number, tech, start, batch))
    conn.commit()
    conn.close()
    return render_template("login1.html")


@app.route('/login')
def index8():
    name = str(request.args.get('name'))
    password = str(request.args.get('password'))
    conn = sql.connect(host='localhost', port=3306, user='root', passwd='mayank', db='kvch_database')
    cusr = conn.cursor()
    # cusr.execute("Insert into Hello(name,password) values('%s','%s')" % (name, password))
    cusr.execute("SELECT * FROM student_registration where Name =%s and Password = %s", (name, password))
    result = cusr.fetchall()
    if len(result) > 0:
        return render_template("user.html")
    else:
        return render_template("login1.html")


@app.route('/logout')
def index9():
    return render_template("Logout.html")

@app.route('/trainer')
def index10():
    name = str(request.args.get('name'))
    password = str(request.args.get('password'))
    conn = sql.connect(host='localhost', port=3306, user='root', passwd='mayank', db='kvch_database')
    cusr = conn.cursor()
    # cusr.execute("Insert into Hello(name,password) values('%s','%s')" % (name, password))
    cusr.execute("SELECT * FROM course_table where trainername =%s and login_password = %s", (name, password))
    result = cusr.fetchall()
    if len(result) > 0:
        return render_template("user.html")
    else:
        return render_template("trainer.html")

@app.route('/admin')
def index11():
        name = str(request.args.get('name'))
        password = str(request.args.get('password'))
        conn = sql.connect(host='localhost', port=3306, user='root', passwd='mayank', db='kvch_database')
        cusr = conn.cursor()
        # cusr.execute("Insert into Hello(name,password) values('%s','%s')" % (name, password))
        cusr.execute("SELECT * FROM admin where Name =%s and Password = %s", (name, password))
        result = cusr.fetchall()
        if len(result) > 0:
            return render_template("user.html")
        else:
            return render_template("admin.html")


app.run(debug=True)
