import requests

url = "http://api.aucklandmuseum.com/search/_search"

payload = {"_type": 'ecrm:E22_Man-Made_Object'}

response = requests.get(url, params=payload)

responseJsonObj = response.json()
dataList = responseJsonObj.get('data')

recordedList2 = []
for data in dataList:
    place = data['place']
    year = data['year']
    info = data['info']
    recordedList2.append(
        dict({"place": place, 'year': year, 'info': info}))

print(recordedList2)


