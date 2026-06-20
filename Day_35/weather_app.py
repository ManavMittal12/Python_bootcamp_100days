import requests
import smtplib
import os

api_key = "a987e824217a4658f4e2d6c981f5d974"
lat = 27.1767
lon = 78.0081
# lat = 36.10380
# lon = 140.26968
parameters = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
will_rain = False
for hour in weather_data["list"]:
    condition_code = hour["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True


if will_rain:
    my_email = "manavmittal1211@gmail.com"
    with open("D:/python_google.txt") as pass_file:
        password = pass_file.read()

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg="Subject: It's raining\n\nBring Umbrella"
        )
