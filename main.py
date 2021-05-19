# https://flask.palletsprojects.com/en/1.1.x/api/

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, session, redirect, url_for, g
import os
from about import about
from artpiece import ArtPiece

# ''' database setup  '''
# project_dir = os.path.dirname(os.path.abspath(__file__))
# database_file = "sqlite:///{}".format(os.path.join(project_dir, "userprofiles.db"))
# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = database_file
# db = SQLAlchemy(app)
#
# '''app secret key'''
# app.secret_key = 'nighthawks'
#
# ''' table definitions '''
#
#
# class User(db.Model):
#     userid = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     username = db.Column(db.String(255), unique=True, nullable=False)
#     passwd = db.Column(db.String(255), unique=True, nullable=False)
#     firstname = db.Column(db.String(255), nullable=False)
#     lastname = db.Column(db.String(255), nullable=False)
#     email_address = db.Column(db.String(255), unique=True, nullable=True)
#     gender = db.Column(db.String(10), unique=False, nullable=True)
#     age = db.Column(db.Integer, unique=False, nullable=True)
#     dob = db.Column(db.DateTime, unique=False, nullable=True)
#     botany = db.Column(db.Integer, unique=False, nullable=True)
#     photography = db.Column(db.Integer, unique=False, nullable=True)
#     music = db.Column(db.Integer, unique=False, nullable=True)
#     space = db.Column(db.Integer, unique=False, nullable=True)
#
#     def __repr__(self):
#         return '<User %r>' % self.username
#
#
# class ArtInfo(db.Model):
#     artInfoId = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     title = db.Column(db.String, nullable=False)
#     creationDate = db.Column(db.String, nullable=False)
#     culture = db.Column(db.String, nullable=False)
#     authorInfo = db.Column(db.String, nullable=False)
#
#     def __repr__(self):
#         return '<ArtInfo %r>' % self.title
#
# class Botany(db.Model):
#     botanyId = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     commonName = db.Column(db.String, nullable=False)
#     scientificName = db.Column(db.String, nullable=False)
#     year = db.Column(db.Integer, nullable=False)
#     familyCommonName = db.Column(db.String, nullable=False)
#     imageURL = db.Column(db.String, nullable=False)
#
#     def __repr__(self):
#         return '<Botany %r>' % self.commonName
#
# class Search(db.Model):
#     searchid = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     exhibit = db.Column(db.String(255), unique=False, nullable=False)
#     link = db.Column(db.String(255), unique=False, nullable=False)
#
#     def __repr__(self):
#         return '<Search %r>' % self.searchid

# ''' table creation '''
# db.create_all()
#
# search = Search(exhibit="botany", link="/botany")
# search1 = Search(exhibit="my favorites", link="/favorites")
# search2 = Search(exhibit="all galleries", link="/all_galleries")
# search3 = Search(exhibit="music", link="/music")
# search4 = Search(exhibit="art", link="/photography")
# search5 = Search(exhibit="photography", link="/photography")
# search6 = Search(exhibit="about us", link="/about_us")
# db.session.add(search)
# db.session.add(search1)
# db.session.add(search2)
# db.session.add(search3)
# db.session.add(search4)
# db.session.add(search5)
# db.session.add(search6)
# db.session.commit()

# global session variable
from database import User, app, db, Search


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
            user = User(username=request.form.get("username"), passwd=request.form.get("passwd"),
                        firstname=request.form.get("firstName"), lastname=request.form.get("lastName"),
                        email_address=request.form.get("email_address"), gender=request.form.get("gender"),
                        age=request.form.get("age"), botany=request.form.get("botany"),
                        photography=request.form.get("photography"), music=request.form.get("music"),
                        space=request.form.get("space"))
            db.session.add(user)
            db.session.commit()
            session.pop('user', None)
            session['user'] = str(request.form['username'])
        except Exception as e:
            # print("failed to add user")
            # print(e)
            return ("Failed to add user. Please try again.")
        return redirect(url_for('home_route'))
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


@app.route('/music')
def music():
    # function use Flask import (Jinja) to render an HTML template
    if g.user:
        return render_template("music.html", user=session['user'])
    return redirect(url_for('landing_page'))


@app.route('/photography', methods=["GET", "POST"])
def photography():
    if request.form:
        return render_template("photography.html", artPiece123=ArtPiece(request.form['culture']))

    # function use Flask import (Jinja) to render an HTML template
    if g.user:
        return render_template("photography.html", user=session['user'], artPiece123=ArtPiece("OnLoad"))


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

@app.route('/easteregg')
def easteregg_route():
    # function use Flask import (Jinja) to render an HTML template
    if g.user:
        return render_template("easteregg.html", user=session['user'])
    return redirect(url_for('landing_page'))

@app.route('/search_results', methods=["GET", "POST"])
def search_results():
    # function use Flask import (Jinja) to render an HTML template
    searchkey = None
    selectedsearch = None
    if g.user:
        if request.form:
            searchkey = request.form.get("search")
            selectedsearch = Search.query.filter_by(exhibit=searchkey).first()
            return render_template("searchresults.html", user=session['user'], data=selectedsearch)
            #error=selectedsearch
        else:
            error = "Invalid Input. Please try again."
    #return redirect(url_for('landing_page'))
    return render_template("searchresults.html", error=error)

if __name__ == "__main__":
    app.run(debug=True, port='80', host='127.0.0.1')
