import requests

url = "https://community-rijksmuseum.p.rapidapi.com/null/collection"

querystring = {"key":"undefined","q":"Van Gogh"}

headers = {
    'x-rapidapi-key': "f355c1253fmshc0d833c7ebaacadp14ddc3jsn0a7f675fda7c",
    'x-rapidapi-host': "community-rijksmuseum.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)