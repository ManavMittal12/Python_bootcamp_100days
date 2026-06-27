# HTTP Put
import requests
from datetime import datetime

USERNAME: str = "kakashiofthesharingan"
TOKEN: str  = "(sd234as14/!@41241"
GRAPH_ID: str  = "meditationgraph1"

header: dict[str, str] = {
    "X-USER-TOKEN" : TOKEN,
}

today: str = datetime.now().strftime("%Y%m%d")
update_pixel_endpoint: str = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{today}"

update_pixel_config: dict[str, str] = {
    "quantity": "60",
}

response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=header)
print(response.text)
