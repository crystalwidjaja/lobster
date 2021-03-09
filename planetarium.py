import requests

url = "https://api.le-systeme-solaire.net/rest/bodies/"
response=requests.get(url)

responseJsonObj = response.json()
dataList = responseJsonObj.get('bodies')

#def planetdata
recordedList1 = []
for data in dataList:
    name = data['name']
    englishName = data['englishName']
    isPlanet = data['isPlanet']
    density = data['density']
    gravity = data['gravity']
    polarRadius = data['polarRadius']
    dimension = data['dimension']
    axialTilt = data['axialTilt']
    recordedList1.append(
        dict({"name": name, 'englishName': englishName, 'isPlanet': isPlanet, 'density': density,
              'gravity': gravity, 'polarRadius': polarRadius, 'dimension': dimension, 'axialTilt': axialTilt}))

print(recordedList1)