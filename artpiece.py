import requests
from flask_sqlalchemy import SQLAlchemy
import sqlite3 as sl

# def laure_borreau():
#     name = "Mme L...Laure Borreau"
#     image = "https://images.fineartamerica.com/images/artworkimages/mediumlarge/2/mme-l-laure-borreau-1863-gustave-courbet.jpg"

# def twilight_in_the_wilderness():
#     name = "Twilight in the Wilderness"
#     image = "https://piction.clevelandart.org/cma/ump.di?e=3633D4677797EE7C5F85A52708022E07D793864033A90FB871EEA1462C4AE5BB&s=21&se=1727484391&v=&f=1965.233_o10.jpg"

# def the_race_track():
#     name = "The Race Track"
#     image = "https://piction.clevelandart.org/cma/ump.di?e=B06DDFF2916C41CB50013EF571266243BEADC7D08B5DBF15F3BBF8C5A29C2274&s=21&se=87832032&v=7&f=1928.8_o10.jpg"

# def view_of_schroon_mountain():
#     name = "View of Schroon Mountain"
#     image = "https://images.fineartamerica.com/images/artworkimages/mediumlarge/1/view-of-schroon-mountain-essex-county-new-york-after-a-storm-thomas-cole.jpg"

# def adeline_ravoux():
#     name = "Adeline Ravoux"
#     image = "https://www.vincentvangogh.org/images/paintings/portrait-of-adeline-ravoux.jpg"

# def large_plane_trees():
#     name = "The Large Plane Trees"
#     image = "https://images-na.ssl-images-amazon.com/images/I/61fsACmYkyL._AC_.jpg"

# def tiger_and_buffalo():
#     name = "Fight between a Tiger and a Buffalo"
#     image = "https://upload.wikimedia.org/wikipedia/commons/5/51/Henri_Rousseau_-_Fight_Between_a_Tiger_and_a_Buffalo.jpg"

# def red_kerchief():
#     name = "The Red Kerchief"
#     image = "https://upload.wikimedia.org/wikipedia/en/0/0f/Monet_Red_kerchief.jpg"

# def church_street_el():
#     name = "Church Street El"
#     image = "https://piction.clevelandart.org/cma/ump.di?e=B06DDFF2916C41CB127F7189B70767AFF2AEF96D4F0D61C4B7BDC29767D30B45&s=21&se=1727484391&v=5&f=1977.43_o10.jpg"

# def womans_work():
#     name = "A Woman's Work"
#     image = "https://piction.clevelandart.org/cma/ump.di?e=B06DDFF2916C41CB6F492A68A847F8FCB8CA92339AF74A910670ECEA07AFBD44&s=21&se=848699570&v=6&f=1964.160_o10.jpg"

#def art_pics():
#    return [laure_borreau(), twilight_in_the_wilderness(), the_race_track(), view_of_schroon_mountain(), adeline_ravoux(), large_plane_trees(), tiger_and_buffalo(), red_kerchief(), church_street_el(), womans_work()]

url = "https://openaccess-api.clevelandart.org/api/artworks/"

payload = {"skip": "2", "limit": "10"}
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
class ArtInfo(db.Model):
    title = db.Column(db.String, nullable=False)
    creation_date = db.Column(db.Integer, primary_key=True, autoincrement=True)
    culture = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    biography = db.Column(db.String, nullable=False)



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
