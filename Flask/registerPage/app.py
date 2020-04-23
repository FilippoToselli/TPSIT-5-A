from flask import Flask, render_template, redirect, url_for, request
import sqlite3

app = Flask(__name__)

def validate(username, password):
    completion = False
    with sqlite3.connect("C:\\Users\\filip\\Desktop\\tpsit\\5quinta\\Python\\Flask\\BotRegistrazioneSito\\registerPage\\static\\db.db") as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Users")
            rows = cur.fetchall()
            for row in rows:
                dbUser = row[0]
                dbPass = row[1]
                if dbUser==username:
                    completion=check_password(dbPass, password)
    return completion

def add(username, password):
    with sqlite3.connect("C:\\Users\\filip\\Desktop\\tpsit\\5quinta\\Python\\Flask\\BotRegistrazioneSito\\registerPage\\static\\db.db") as con:
        cur = con.cursor()
        cur.execute(f'INSERT INTO Users (USERNAME, PASSWORD) VALUES("{username}", "{password}");')

def check_password(hashed_password, user_password):
    return hashed_password == user_password

@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        add(username, password)
        return redirect(url_for('secret'))
    return render_template('Registra.html')

@app.route('/secret')
def secret():
    return "This is a secret page!"

if __name__== "__main__":
    app.run()