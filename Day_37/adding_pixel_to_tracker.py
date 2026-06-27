# Adding pixel to our data.
import requests


USERNAME: str = "kakashiofthesharingan"
TOKEN: str  = "(sd234as14/!@41241"
GRAPH_ID: str  = "meditationgraph1"


header: dict[str, str] = {
    "X-USER-TOKEN" : TOKEN,
}

pixel_endpoint: str = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"

pixel_config: dict[str, str] = {
    "date" : "20260627",
    "quantity": "10",
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=header)
print(response.text)
