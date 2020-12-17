# https://flask.palletsprojects.com/en/1.1.x/api/

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, redirect, url_for
import os

''' database setup  '''
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "userprofiles.db"))
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)

''' table definitions '''
class User(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    passwd = db.Column(db.String(255), unique=True, nullable=False)
    firstname = db.Column(db.String(255), nullable=False)
    lastname = db.Column(db.String(255), nullable=False)
    email_address = db.Column(db.String(255), unique=True, nullable=True)
    gender = db.Column(db.String(10), unique=False, nullable=True)
    age = db.Column(db.Integer, unique=False, nullable=True)
    dob = db.Column(db.Date, unique=False, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username

''' table creation '''
db.create_all()

#connects default URL of server to render home.html

@app.route('/landing_page', methods=["GET", "POST"])
def landing_page():
    users = None
    if request.form:
        try:
            """prepare data for primary table extracting from form"""
            user = User(userid=request.form.get("userid"), username=request.form.get("username"), passwd=request.form.get("passwd"), firstname=request.form.get("firstName"),lastname=request.form.get("lastName"))
            """add and commit data to user table"""
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            print("failed to add user")
            print(e)
    users = User.query.all()
    return render_template("landing_page.html", users=users)

@app.route('/')
@app.route('/home')
def home_route():
    #function use Flask import (Jinja) to render an HTML template
    return render_template("home.html")

@app.route('/all_galleries')
def all_galleries():
    #function use Flask import (Jinja) to render an HTML template
    return render_template("all_galleries.html")

@app.route('/botany')
def botany():
    #function use Flask import (Jinja) to render an HTML template
    return render_template("botany.html")

@app.route('/history')
def history():
    #function use Flask import (Jinja) to render an HTML template
    return render_template("history.html")

@app.route('/japanese_culture')
def japanese_culture():
    #function use Flask import (Jinja) to render an HTML template
    return render_template("japanese_culture.html")

@app.route('/music')
def music():
    #function use Flask import (Jinja) to render an HTML template
    return render_template("music.html")

@app.route('/photography')
def photography():
    #function use Flask import (Jinja) to render an HTML template
    return render_template("photography.html")

@app.route('/planetarium')
def planetarium():
    #function use Flask import (Jinja) to render an HTML template
    return render_template("planetarium.html")

@app.route('/gift_shop')
def gift_shop():
    #function use Flask import (Jinja) to render an HTML template
    return render_template("gift_shop.html")

@app.route('/about_us')
def about_us():
    #function use Flask import (Jinja) to render an HTML template
    return render_template("about_us.html")

if __name__ == "__main__":
  app.run(port='80', host='127.0.0.1')
