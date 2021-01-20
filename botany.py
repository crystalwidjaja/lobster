import requests

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

