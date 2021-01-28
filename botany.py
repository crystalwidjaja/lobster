import json
import os
import requests
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from main import Botany

''' Get db object adding entires to ArtInfo table '''
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "userprofiles.db"))
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)

url = "https://trefle.io/api/v1/plants?token=5-M6tX9TBt0XVNIgKY7d1V26zFEPH8Vm-WoGmZQfaMI"

payload = {}

response = requests.get(url, params=payload)

responseJsonObj = response.json()
dataList = responseJsonObj.get('data')

recordedList1 = []
for data in dataList:
    common_name = data['common_name']
    scientific_name = data['scientific_name']
    year = data['year']
    family_common_name = data['family_common_name']
    image_url = data['image_url']
    recordedList1.append(
        dict({"common_name": common_name, 'scientific_name': scientific_name, 'year': year, 'family_common_name': family_common_name, 'image_url': image_url}))

print(recordedList1)

''' Add Botany information into Records into the DB '''


for botanyInfo in recordedList1:
    commonName = botanyInfo['common_name']
    scientificName = botanyInfo['scientific_name']
    year = botanyInfo['year']
    familyCommonName = botanyInfo['family_common_name']
    imageURL = botanyInfo['image_url']

    botanyInfo = Botany(commonName=botanyInfo['common_name'], scientificName=botanyInfo['scientific_name'], year=int(botanyInfo['year']), familyCommonName=botanyInfo['family_common_name'], imageURL=botanyInfo['image_url'])
    db.session.add(botanyInfo)
    db.session.commit()

botanyInfos = Botany.query.all()
print(botanyInfos)
