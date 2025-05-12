from flask import Flask, render_template, request
import pymysql
app = Flask(__name__)

db_config={
    "host":"localhost",
    "user":"root",
    "password":"nimmi*03@28",
    "database": "atm"
}

@app.route("/")
def landing():
    return render_template("home.html")

@app.route("/withdraw1")
def withdraw1():
    return render_template("withdraw1.html")

@app.route("/withdraw2", methods=['POST'])
def withdraw2():
    accno = request.form['account_number']
    pin = request.form['pin']

    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()
    query = "SELECT * FROM ACCOUNTS WHERE USER_ACCNO = %s"
    cursor.execute(query,(accno))
    data = cursor.fetchone()
    conn.close()
    print(data)
    if data is None:
        return render_template("withdraw1.html",msg="noaccount")
    elif data[-2] is None:
        return render_template("withdraw1.html",msg="nopin")
    elif data[-2] != int(pin):
        return render_template("withdraw1.html", msg='wrongpin')
    else:
         return render_template("withdraw2.html", user_name=data[1], accno=accno)

@app.route("/withdraw3", methods=["POST"])
def withdraw3():
    accno = request.form["accnno"]
    amount = int(request.form["amount"])

    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()
    query = "SELECT USER_BALANCE,USER_NAME FROM ACCOUNTS WHERE USER_ACCNO = %s"
    cursor.execute(query,(accno))
    data = cursor.fetchone()
    conn.close()
    print(data)

    if int(amount) <= int(data[0]):
        balance = int(data[0]) - int(amount)
        conn = pymysql.connect(**db_config)
        cursor = conn.cursor()
        query = "UPDATE ACCOUNTS SET USER_BALANCE = %s WHERE USER_ACCNO = %s"
        cursor.execute(query,(balance,accno))
        conn.commit()
        conn.close()
        return render_template("withdraw2.html", msg="balance", accno=accno, user_name=data[1])
    else:
        return render_template("withdraw2.html", msg="nobalance", accno=accno,user_name=data[1])

@app.route("/deposit")
def deposit():
    return render_template("deposit.html")

@app.route("/deposit2", methods=["POST"])
def deposit2():
    accno = request.form["account_number"]
    amount = int(request.form["amount"])

    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()
    query = "SELECT * FROM ACCOUNTS WHERE USER_ACCNO = %s"
    cursor.execute(query,(accno))
    data = cursor.fetchone()
    conn.close()
    print(data)
    if data is None:
        return render_template("deposit.html", msg="noaccount")
    else:
        conn = pymysql.connect(**db_config)
        cursor = conn.cursor()
        query = "UPDATE ACCOUNTS SET USER_BALANCE = USER_BALANCE + %s WHERE USER_ACCNO = %s"
        cursor.execute(query,(amount,accno))
        conn.commit()
        conn.close()
        return render_template("deposit.html", msg="success")
    
@app.route("/mini-statement", methods=["GET"])
def mini_statement():
    return render_template("mini_statement1.html")

@app.route("/mini-statement2", methods=["POST"])
def mini_statement_process():
    accno = request.form["account_number"]
    pin = request.form["pin"]

    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()
    query = "SELECT * FROM ACCOUNTS WHERE USER_ACCNO = %s"
    cursor.execute(query,(accno))
    data = cursor.fetchone()
    conn.close()
    print(data)
    if data is None:
        return render_template("ministatement.html", msg = "noaccount")
    elif data [-2] is None:
        return render_template("ministatement.html", msg = "nopin")
    elif int(pin) != int(data[-2]):
        return render_template("mini_statement1.html", msg="Incorrect PIN")
    else:
        accno = data[0]
        name = data[1]
        email=data[2]
        balance = data[-1]
        return render_template("mini_statement2.html", name=name, accno=accno, email=email, balance=balance)
    
@app.route("/pin_generation1")
def pin_generation1():
    return render_template("pin_generation1.html")

@app.route("/pin_generation2", methods=["POST"])
def pin_generation2():
    accno = request.form.get("accno")

    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()
    query = "SELECT * FROM ACCOUNTS WHERE USER_ACCNO = %s"
    cursor.execute(query,(accno))
    data = cursor.fetchone()
    conn.close()
    print(data)
    if data is None:
        return render_template("pin_generation1.html", msg="noaccount")
    elif data[-2] is not None:
        return render_template("pin_generation1.html", msg="account")
    else:
        return render_template("pin_generation2.html", accno=accno)

@app.route("/pin_generation3", methods=["POST"])
def pin_generation3():
    accno = request.form.get("accno")
    pin = request.form.get("pin")
    cpin = request.form.get("cpin")

    if pin != cpin:
        return render_template("pin_generation2.html", accno=accno, msg="wrongpin")
    else:
        conn = pymysql.connect(**db_config)
        cursor = conn.cursor()
        query = "UPDATE ACCOUNTS SET USER_PIN = %s WHERE USER_ACCNO = %s"
        cursor.execute(query,(pin,accno))
        conn.commit()
        conn.close()
        return render_template("pin_generation2.html", accno=accno, msg="ok")

app.run(port = 5015)
