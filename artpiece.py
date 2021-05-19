import json
import os

import requests
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from database import ArtInfo


class ArtPiece:
    recordedList = []
    filteredRecordList = []
    filteredTitles = []

    def __init__(self, culture):
        if culture == 'OnLoad':
            self.buildRecordedList()
            self.saveToDB()
        self.buildFilterListByCulture(culture)

    def buildRecordedList(self):

        url = "https://openaccess-api.clevelandart.org/api/artworks/"

        payload = {"skip": "2", "limit": "20"}
        response = requests.get(url, params=payload)

        responseJsonObj = response.json()
        dataList = responseJsonObj.get('data')

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
            self.recordedList.append(
                dict({'title': title, 'creationDate': creationDate, 'culture': culture, 'creators': authorList}))

        # fl = list(filter(lambda x: (any(elem.find("America") != -1)) for elem in x['culture']), recordedList)
        print(self.recordedList)

    ''' Add ArtInfo Records into DB '''

    def saveToDB(self):
        ''' Get db object adding entires to ArtInfo table '''
        project_dir = os.path.dirname(os.path.abspath(__file__))
        database_file = "sqlite:///{}".format(os.path.join(project_dir, "userprofiles.db"))
        app = Flask(__name__)
        app.config["SQLALCHEMY_DATABASE_URI"] = database_file
        db = SQLAlchemy(app)
        for record in self.recordedList:
            artInfo = ArtInfo(title=record['title'], creationDate=record['creationDate'],
                              culture=json.dumps(record['culture']), authorInfo=json.dumps(record['creators']))
            db.session.add(artInfo)
            db.session.commit()

        artInfos = ArtInfo.query.all()
        print(artInfos)

    def buildFilterListByCulture(self, cultureName):
        self.filteredTitles = []
        for record in self.recordedList:
            tempCultureList = record['culture']
            if any(cultureName in str for str in tempCultureList):
                self.filteredTitles.append(record['title'])
                self.filteredRecordList.append(record)

    @property
    def get_filtered_titles(self):
        return self.filteredTitles
    @property
    def get_filtered_record_list(self):
        return self.filteredRecordList
