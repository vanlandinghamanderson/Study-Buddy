from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), unique=True)
    last_name = db.Column(db.String(64), unique=True)
    major = db.Column(db.String(64), unique=True)
    def __init__(self, first_name, last_name, major):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major

    def __repr__(self):
        return self.first_name + ' ' + self.last_name + ', ' + self.major

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/', methods=['GET', 'POST'])
def welcome():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        major = request.form['major']
        user = User(first_name=first_name, last_name=last_name, major=major)
        db.session.add(user)
        db.session.commit()
    return render_template('welcome.html', first_name=first_name)

@app.route('/find_a_buddy')
def find_a_buddy():
    return render_template('find_a_buddy.html')

@app.route('/find_a_group')
def find_a_group():
    return render_template('find_a_group.html')

@app.route('/my_buddies')
def my_buddies():
    return render_template('my_buddies.html')

if __name__ == '__main__':
    app.debug = True
    ip = '127.0.0.1'
    app.run(host=ip)
