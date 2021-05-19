''' database setup  '''
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "userprofiles.db"))
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)

'''app secret key'''
app.secret_key = 'nighthawks'

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
    photography = db.Column(db.Integer, unique=False, nullable=True)
    music = db.Column(db.Integer, unique=False, nullable=True)
    space = db.Column(db.Integer, unique=False, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username


class ArtInfo(db.Model):
    artInfoId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    creationDate = db.Column(db.String, nullable=False)
    culture = db.Column(db.String, nullable=False)
    authorInfo = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<ArtInfo %r>' % self.title

class Botany(db.Model):
    botanyId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    commonName = db.Column(db.String, nullable=False)
    scientificName = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    familyCommonName = db.Column(db.String, nullable=False)
    imageURL = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<Botany %r>' % self.commonName

class Search(db.Model):
    searchid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    exhibit = db.Column(db.String(255), unique=False, nullable=False)
    link = db.Column(db.String(255), unique=False, nullable=False)

    def __repr__(self):
        return '<Search %r>' % self.searchid

''' table creation '''
db.create_all()

search = Search(exhibit="botany", link="/botany")
search1 = Search(exhibit="my favorites", link="/favorites")
search2 = Search(exhibit="all galleries", link="/all_galleries")
search3 = Search(exhibit="music", link="/music")
search4 = Search(exhibit="art", link="/photography")
search5 = Search(exhibit="photography", link="/photography")
search6 = Search(exhibit="about us", link="/about_us")
db.session.add(search)
db.session.add(search1)
db.session.add(search2)
db.session.add(search3)
db.session.add(search4)
db.session.add(search5)
db.session.add(search6)
db.session.commit()