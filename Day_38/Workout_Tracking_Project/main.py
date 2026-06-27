import requests
from datetime import datetime


with open(r"D:\Computer_Science_Learning_Material\api_keys\api_nutrition.txt") as nutrition_api_keys_file:
    n_api_keys = nutrition_api_keys_file.readlines()

APP_ID: str = n_api_keys[0].removesuffix("\n")
API_KEY: str = n_api_keys[1].removesuffix("\n")


header: dict = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY
}

nutrition_api_endpoint_post: str = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"


user_input: str = input("What exercise did you perform today ? -->\n")

nutri_parameters: dict = {
    "query" : user_input,
    "weight" : 64,
    "height" : 171,
    "age" : 25,
    "gender" : "male"
}


response = requests.post(url=nutrition_api_endpoint_post, json=nutri_parameters, headers=header)
response.raise_for_status()
result: dict = response.json()["exercises"][0]
print(result)


# Sheety
with open(r"D:\Computer_Science_Learning_Material\api_keys\sheety_api_info.txt") as sheety_info:
    sheety_info_text = sheety_info.readlines()


sheety_token: str = sheety_info_text[0].removesuffix("\n")
header: dict = {
    "Authorization" : f"Bearer (@sd3f%3fag]53"
}
# Adding to sheet
today = datetime.now()
sheet_parameters = {
    "sheet1" : {
        "date" : today.strftime("%d-%m-%Y"),
        "time" : today.strftime("%H:%M"),
        "exercise" : result["name"].title(),
        "duration"  : result["duration_min"],
        "calories" : result["nf_calories"]
    }
}

sheety_endpoint: str = sheety_info_text[1].removesuffix("\n")
response1 = requests.post(url=sheety_endpoint, json=sheet_parameters, headers=header)
