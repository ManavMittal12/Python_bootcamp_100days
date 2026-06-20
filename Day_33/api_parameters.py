# API Parameters

# We saw, API Endpoints,
# apis also have parameters
# allows us to give input when making api request so that
# we can give different peices of input the same way
# we give different inputs to a function to get different outputs


# in the banker analogy, we can ask question to the banker to get
# specific peice of information.

# not all api have parameters but some have.

# Sunrise and Sunset API
# API documentation, it tells us how we can structure our parameters.
# there can be required and optional parameters.

import requests
from datetime import datetime

MY_LAT = 27.1767
MY_LONG = 78.0081

parameters = {
    "lat" : MY_LAT,
    "lng" : MY_LONG,
    "formatted" : 0,
    "tzid" : "Asia/Kolkata"
}

response = requests.get(url=f"https://api.sunrise-sunset.org/json?lat={MY_LAT}&lng={MY_LONG}", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)
