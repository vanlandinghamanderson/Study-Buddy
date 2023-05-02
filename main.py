import os
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# The db object instantiated from the class SQLAlchemy represents the database and
# provides access to all the functionality of Flask-SQLAlchemy.
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), unique=True)
    last_name = db.Column(db.String(64), unique=False)
    major = db.Column(db.String(64), unique=False)

    def __repr__(self):
        return '%r' % self.first_name + self.last_name

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        major = request.form['major']
        user = User(first_name=first_name, last_name=last_name, major=major)
        try:
            if not 'first_name' or not 'major' or not 'last_name':
                db.session.add(user)
                db.session.commit()
            return redirect(url_for('welcome', first_name=first_name))
        except:
            error = "Error"
            db.session.rollback()
            return error


@app.route('/welcome/<first_name>')
def welcome(first_name):
    return render_template('welcome.html', first_name=first_name)

@app.route('/find_your_buddy')
def find_your_buddy():
    return render_template('find_your_buddy.html')

@app.route('/find_your_grouo')
def find_your_group():
    return render_template('find_your_group.html')

@app.route('/my_buddies')
def my_buddies():
    return render_template('my_buddies.html')

if __name__ == '__main__':
    app.debug = True
    ip = '127.0.0.1'
    app.run(host=ip)