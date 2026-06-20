# What is API Authentication and Why do we need to Authenticate Ourselves?
# we know about api endpoints and api parameters

# APIs that require authentication.
# till now, we saw free apis

# there are other apis with valuable data.
# the way companies prevent misuse the api is through API key
# it can authorize and prevent access through API key.

import requests
api_key = "a987e824217a4658f4e2d6c981f5d974"
lat = 27.1767
lon = 78.0081
parameters = {
    "lat": lat,
    "lon": lon,
    "appid": api_key
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
print(response.status_code)
print(response.json())
