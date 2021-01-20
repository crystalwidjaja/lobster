import requests

url = "http://{defaultHost}/api/v1/species"

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
        dict({"common_name": common_name, 'scientific_name': scientific_name, 'year': year, 'family_common_name': family_common_name, 'image_url': image_url)))

print(recordedList1)

#should create the table using the sqlalchemy library instead of sqlite3 library
class Botany(db.Model):
    common_name = db.Column(db.String, nullable=False)
    scientific_name = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, primary_key=True)
    family_common_name = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String, nullable=False)