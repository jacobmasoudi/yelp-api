import requests
import config

url = "https://api.yelp.com/v3/businesses/search"

headers = {
    "Authorization": "Bearer " + config.api_key
}
params = {
    "term": " bar",
    "location": "chicago"
}
resoponse = requests.get(url, headers=headers, params=params)
businesses = resoponse.json()["businesses"]

names = [businesse["name"]
         for businesse in businesses]
print(names)
