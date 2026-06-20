import requests
import smtplib
from datetime import datetime
import time

MY_LAT = 27.1767
MY_LONG = 78.0081


EMAIL = "manavmittal1211@gmail.com"
with open("../../../../../python_google.txt") as data1:
    PASSWORD = data1.read()


def is_iss_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data=response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(iss_latitude, iss_longitude)
    if MY_LAT - 5 <= iss_longitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_latitude <=MY_LONG+5:
        print("ISS Above us")
        return True
    else:
        return False


def is_night():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data=response.json()
    parameters = {
        "lat" : MY_LAT,
        "lng" : MY_LONG,
        "formatted" : 0,
        "tzid" : "Asia/Kolkata"
    }
    response = requests.get(url=f"https://api.sunrise-sunset.org/json?lat={MY_LAT}&lng={MY_LONG}", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    if is_iss_close() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(EMAIL, PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL,
                msg="Subject: Look Up🌃\n\nThe ISS is above you in the sky."
            )
    time.sleep(60)
