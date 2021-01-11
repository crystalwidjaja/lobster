# https://flask.palletsprojects.com/en/1.1.x/api/

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, redirect, url_for
import os
from about import about

''' database setup  '''
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "userprofiles.db"))
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)

''' table definitions '''
class User(db.Model):
    userid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    passwd = db.Column(db.String(255), unique=True, nullable=False)
    firstname = db.Column(db.String(255), nullable=False)
    lastname = db.Column(db.String(255), nullable=False)
    email_address = db.Column(db.String(255), unique=True, nullable=True)
    gender = db.Column(db.String(10), unique=False, nullable=True)
    age = db.Column(db.Integer, unique=False, nullable=True)
    dob = db.Column(db.DateTime, unique=False, nullable=True)


    def __repr__(self):
        return '<User %r>' % self.username


''' table creation '''
db.create_all()


# connects default URL of server to render home.html
@app.route('/')
@app.route('/landing_page', methods=["GET", "POST"])
def landing_page():
    users = None
    if request.form:
        try:
            """prepare data for primary table extracting from form"""
            user = User(username=request.form.get("username"), passwd=request.form.get("passwd"), firstname=request.form.get("firstName"), lastname=request.form.get("lastName"), email_address=request.form.get("email_address"), gender=request.form.get("gender"), age=request.form.get("age"))
            """add and commit data to user table"""
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            # print("failed to add user")
            # print(e)
            return ("Failed to add user. Please try again.")
    users = User.query.all()
    return render_template("landing_page.html", users=users)


@app.route('/signin', methods=["GET", "POST"])
def signin():
    error = None
    if request.form:
        POST_USERNAME = str(request.form['username'])
        POST_PASSWORD = str(request.form['password'])
        result1 = User.query.filter(User.username == POST_USERNAME).first()
        result2 = User.query.filter(User.passwd == POST_PASSWORD).first()
        if (result1 and result2):
            return redirect("/home")
        else:
            error = "Invalid Credentials. Please try again."
    return render_template("login.html", error=error)


@app.route('/home')
def home_route():
    # function use Flask import (Jinja) to render an HTML template
    return render_template("home.html")


@app.route('/all_galleries')
def all_galleries():
    # function use Flask import (Jinja) to render an HTML template
    return render_template("all_galleries.html")


@app.route('/botany')
def botany():
    # function use Flask import (Jinja) to render an HTML template
    return render_template("botany.html")


@app.route('/history')
def history():
    # function use Flask import (Jinja) to render an HTML template
    return render_template("history.html")


@app.route('/japanese_culture')
def japanese_culture():
    # function use Flask import (Jinja) to render an HTML template
    return render_template("japanese_culture.html")


@app.route('/music')
def music():
    # function use Flask import (Jinja) to render an HTML template
    return render_template("music.html")


@app.route('/photography')
def photography():
    # function use Flask import (Jinja) to render an HTML template
    return render_template("photography.html")


@app.route('/planetarium')
def planetarium():
    # function use Flask import (Jinja) to render an HTML template
    return render_template("planetarium.html")


@app.route('/gift_shop')
def gift_shop():
    # function use Flask import (Jinja) to render an HTML template
    return render_template("gift_shop.html")


@app.route('/about_us')
def about_us():
    # function use Flask import (Jinja) to render an HTML template
    return render_template("about_us.html", aboutus=about())


@app.route('/favorites')
def favorites():
    #function use Flask import (Jinja) to render an HTML template
    return render_template("favorites.html")

# Not sure if this will work but I'll just leave it here
#@app.route('/profile/<userid>')
#def profile(userid):
    # function use Flask import (Jinja) to render an HTML template
#    return "Welcome %s" % userid

if __name__ == "__main__":
    app.run(debug=True, port='80', host='127.0.0.1')
