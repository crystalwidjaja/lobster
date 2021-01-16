# https://flask.palletsprojects.com/en/1.1.x/api/

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, session, redirect, url_for, g
import os
from about import about

''' database setup  '''
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "userprofiles.db"))
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)

'''app secret key'''
app.secret_key = os.urandom(100)

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
    botany = db.Column(db.Integer, unique=False, nullable=True)
    history = db.Column(db.Integer, unique=False, nullable=True)
    photography = db.Column(db.Integer, unique=False, nullable=True)
    music = db.Column(db.Integer, unique=False, nullable=True)
    space = db.Column(db.Integer, unique=False, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username


''' table creation '''
db.create_all()

# global session variable
@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

# connects default URL of server to render home.html
@app.route('/')
@app.route('/landing_page', methods=["GET", "POST"])
def landing_page():
    users = None
    if request.form:
        try:
            """prepare data for primary table extracting from form"""
            user = User(username=request.form.get("username"), passwd=request.form.get("passwd"), firstname=request.form.get("firstName"), lastname=request.form.get("lastName"),
                        email_address=request.form.get("email_address"), gender=request.form.get("gender"), age=request.form.get("age"), botany=request.form.get("botany"), history=request.form.get("history"),
                        photography=request.form.get("photography"), music=request.form.get("music"), space=request.form.get("space"))
            db.session.add(user)
            db.session.commit()
            session.pop('user', None)
            session['user'] = str(request.form['username'])
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
            session.pop('user', None)
            session['user'] = POST_USERNAME
            return redirect(url_for('home_route'))
        else:
            error = "Invalid Credentials. Please try again."
    return render_template("login.html", error=error)


@app.route('/home')
def home_route():
    # function use Flask import (Jinja) to render an HTML template
    if g.user:
        return render_template("home.html", user=session['user'])
    return redirect(url_for('landing_page'))


@app.route('/all_galleries')
def all_galleries():
    # function use Flask import (Jinja) to render an HTML template
    if g.user:
        return render_template("all_galleries.html", user=session['user'])
    return redirect(url_for('landing_page'))


@app.route('/botany')
def botany():
    # function use Flask import (Jinja) to render an HTML template
    if g.user:
        return render_template("botany.html", user=session['user'])
    return redirect(url_for('landing_page'))


@app.route('/history')
def history():
    # function use Flask import (Jinja) to render an HTML template
    if g.user:
        return render_template("history.html", user=session['user'])
    return redirect(url_for('landing_page'))


@app.route('/japanese_culture')
def japanese_culture():
    # function use Flask import (Jinja) to render an HTML template
    if g.user:
        return render_template("japanese_culture.html", user=session['user'])
    return redirect(url_for('landing_page'))


@app.route('/music')
def music():
    # function use Flask import (Jinja) to render an HTML template
    if g.user:
        return render_template("music.html", user=session['user'])
    return redirect(url_for('landing_page'))


@app.route('/photography')
def photography():
    # function use Flask import (Jinja) to render an HTML template
    if g.user:
        return render_template("photography.html", user=session['user'])
    return redirect(url_for('landing_page'))


@app.route('/planetarium')
def planetarium():
    # function use Flask import (Jinja) to render an HTML template
    if g.user:
        return render_template("planetarium.html", user=session['user'])
    return redirect(url_for('landing_page'))


@app.route('/gift_shop')
def gift_shop():
    # function use Flask import (Jinja) to render an HTML template
    if g.user:
        return render_template("gift_shop.html", user=session['user'])
    return redirect(url_for('landing_page'))


@app.route('/about_us')
def about_us():
    # function use Flask import (Jinja) to render an HTML template
    if g.user:
        return render_template("about_us.html", aboutus=about(), user=session['user'])
    return redirect(url_for('landing_page'))


@app.route('/favorites')
def favorites():
    # function use Flask import (Jinja) to render an HTML template
    selected_user = None
    selected_fav = None
    if g.user:
        selected_user = session['user']
        selected_fav = User.query.filter_by(username=selected_user).first()
        return render_template("favorites.html", user=session['user'], selected_fav=selected_fav)
    return redirect(url_for('landing_page'))


if __name__ == "__main__":
    app.run(debug=True, port='80', host='127.0.0.1')
