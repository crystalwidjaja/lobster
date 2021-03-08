import json
import os
from datetime import datetime

import requests
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlite3 as sl

from main import ArtInfo

''' Get db object adding entires to ArtInfo table '''
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "userprofiles.db"))
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)


url = "https://openaccess-api.clevelandart.org/api/artworks/"

payload = {"skip": "2", "limit": "20"}
response = requests.get(url, params=payload)

responseJsonObj = response.json()
dataList = responseJsonObj.get('data')

recordedList = []
for data in dataList:
    title = data['title']
    creationDate = data['creation_date']
    culture = data['culture']
    authorList = []
    creators = data['creators']
    for creator in creators:
        author = creator['description']
        biography = creator['biography']
        authorDict = dict({"author": author, "biography": biography})
        authorList.append(authorDict)
    recordedList.append(
        dict({'title': title, 'creationDate': creationDate, 'culture': culture, 'creators': authorList}))


print(recordedList)

''' Add ArtInfo Records into DB '''

for record in recordedList:
    title = record['title']
    creationDate = record['creation_date']
    culture = record['culture']
    authorInfo = json.dumps(record['creators'])

    artInfo = ArtInfo(title=record['title'], creationDate=record['creationDate'], culture=json.dumps(record['culture']), authorInfo=json.dumps(record['creators']))
    db.session.add(artInfo)
    db.session.commit()

artInfos = ArtInfo.query.all()
print(artInfos)


