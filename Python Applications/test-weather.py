import json, requests

url = "https://api.weatherbit.io/v2.0/current?lat=35.7796&lon=-78.6382&key=ca8bbc0aa955422ba8a9f3fe3c82956a&include=minutely"

response = requests.request("GET", url)

line = json.loads(response.text)

sunset = line['data'][0]['sunset']

print(sunset)
