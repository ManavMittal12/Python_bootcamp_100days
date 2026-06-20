import requests # this package is needed to call api


response = requests.get(url="http://api.open-notify.org/iss-now.json")  # we get back the response codes.
print(response)


'''
https://www.webfx.com/web-development/glossary/
# 1XX - hold on response code
# 2XX - Here you go
# 3XX - Go away (you don't have permission)
# 4XX - Doesn't exists or you screwed up
# 5XX - The server screwed up, Maybe the server is down or maybe there's some other issue
'''


# if response.status_code != 200:
#     raise Exception("Bad response from ISS API")    # that's very generic

# there are too many status codes
# use request module to raise the exceptions and show the user.

response.raise_for_status()

# getting hold of data
data = response.json()["iss_position"]
longitude = data["longitude"]
latitude = data["latitude"]

iss_position = (longitude, latitude)
print(iss_position)
