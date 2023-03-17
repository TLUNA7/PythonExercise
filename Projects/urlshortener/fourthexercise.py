from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import random
import string
import os

app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.before_first_request
def create_tables():
    db.create_all()

class urls(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    long = db.Column("long", db.String())
    short = db.Column("short", db.String(10))

    def __init__(self, long, short):
        self.long = long
        self.short = short

class users(db.Model):
    user = db.Column("id_", db.String())
    email = db.Column("email", db.String())
    password = db.Column("pass", db.String())

    def __init__(self, email, password, user):
        self.email = email
        self.password = password
        self.user = user


logged = False

def shorteningUrl():
    newLetters = string.ascii_lowercase + string.ascii_uppercase
    while True:
        randomLetters = random.choices(newLetters, k=3)
        randomLetters = "".join(randomLetters)
        short_url = urls.query.filter_by(short=randomLetters).first()
        if not short_url:
            return randomLetters

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        if request.method.get("shorten") == 'shorten':
            url_rec = request.form["nm"]
            found_url = urls.query.filter_by(long=url_rec).first()

            if found_url:
                return redirect(url_for("display_short_url", url=found_url.short))
            else:
                short_url = shorteningUrl()
                print(short_url)
                new_url = urls(url_rec, short_url)
                db.session.add(new_url)
                db.session.commit()
                pass
    return render_template("home.html")









# @app.route('/', methods=['POST', 'GET'])
# def home():
#     if request.method == 'POST':
#         if request.form.get('login') == 'login':
#             return redirect(url_for("login"))
#         elif request.form.get('register') == 'register':
#             return redirect(url_for('register')) 
#         elif request.form.get('shorten') == 'shorten':
#             pass
#     return render_template("home.html")

# @app.route('/login', methods=["POST","GET"])
# def login():
#     if request.method == "POST":
#         email_rec = request.form.get('email')
#         name_rec = request.form.get('name')
#         password_rec = request.form.get('password')

#         user_email = users.query.filter_by(email=email_rec).first()
#         user_password = users.query.filter_by(password=password_rec).first()
#         if user_email & user_password:
#             return redirect(url_for('home'))
#     return render_template('login.html')

# @app.route('/register', methods=["POST","GET"])
# def register():
#     if request.method == "POST":
#         if request.form.get('home') == 'home':
#             email_Rec = request.form.get('email')
#             name = request.form.get('name')
#             password = request.form.get('password')

#             user_email = users.query.filter_by(email=email_Rec).first()
#             if user_email:
#                 return flash('exists', category='error')
#             else:
#                 print(email_Rec, name,password)
#                 new_user = users(email_Rec,password,name)
#                 db.session.add(new_user)
#                 db.session.commit()
#                 logged = True
#                 return redirect(url_for('home'))
#     return render_template('register.html')




def checkoldies():
    pass

if __name__ == '__main__':
    checkoldies()
    app.run(port=5000, debug=True)