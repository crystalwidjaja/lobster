import json
import requests

url = "https://openaccess-api.clevelandart.org/api/artworks/"

payload={"skip": "2", "limit": "10"}
response = requests.get(url, params=payload)

responseJsonObj = response.json()
dataList = responseJsonObj.get('data')

recordedList = []
for data in dataList:
    title = data['title']
    creationDate = data['creation_date']
    authorList = []
    creators = data['creators']
    for creator in creators:
        author = creator['description']
        biography = creator['biography']
        authorDict = dict({"author": author, "biography": biography})
        authorList.append(authorDict)
    recordedList.append(dict({"title": title, 'creationDate': creationDate, 'creators': authorList}))

print(recordedList)


