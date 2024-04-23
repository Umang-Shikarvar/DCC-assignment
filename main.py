from flask import Flask, redirect, url_for, request, Response, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Uks@1602'
app.config['MYSQL_DB'] = 'EB'

mysql = MySQL(app)

@app.route('/', methods = ["POST", "GET"])
def main_page():
    return render_template("index.html")

@app.route('/a_1', methods = ["POST", "GET"])
def a_1():
    if request.method == "POST":
        print(request.method)
        print(request.form["box"])
        cursor = mysql.connection.cursor()
        cursor.execute("select * from eb_purchase where Bond_Number like %s", (request.form["box"],))

        data = cursor.fetchall()
        print(data)
        cursor.close()

    return render_template("index.html", a_1_data = data)
if __name__ == '__main__':
   app.run(host="0.0.0.0", port="80", debug = True) 