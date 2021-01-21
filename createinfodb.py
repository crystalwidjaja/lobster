from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import create_engine
from sqlalchey.orm import Session

app = Flask(_name_)
db_url = 'sqlite:///informationDB'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URL'] = db_url
db = SQLALchemy(app)

engine = create_engine(db_url)
session = Session(bind=engine)
