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
delete_pixel_endpoint: str = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{today}"
response = requests.delete(url=delete_pixel_endpoint, headers=header)
print(response.text)
