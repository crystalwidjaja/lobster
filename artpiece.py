import requests
from flask_sqlalchemy import SQLAlchemy
import sqlite3 as sl

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
        dict({"title": title, 'creationDate': creationDate, 'culture': culture, 'creators': authorList}))

print(recordedList)

#should create the table using the sqlalchemy library instead of sqlite3 library
#class ArtInfo(db.Model):
    #title = db.Column(db.String, nullable=False)
    #creation_date = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #culture = db.Column(db.String, nullable=False)
    #author = db.Column(db.String, nullable=False)
    #biography = db.Column(db.String, nullable=False)



# creating a connection to the Database created
#con = sl.connect('userprofiles.db')

# creating a table within the database
#with con:
#    con.execute("""
#        CREATE TABLE ARTINFO (
#            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#           title TEXT,
#            creation_date INTEGER,
#            culture TEXT,
#            author TEXT,
#            biography TEXT
#        );
#    """)
#sql = 'INSERT INTO ARTINFO (id, title, creation_date, culture, author, biography) values(?, ?, ?, ?, ?, ?)'

#with con:
#    data = con.execute("SELECT * FROM ARTINFO")
#    for row in data:
#        print(row)
