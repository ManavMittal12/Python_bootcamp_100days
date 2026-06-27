import requests
import requests_cache
from dotenv import load_dotenv
import os

requests_cache.install_cache("Flight_data")
load_dotenv(".env")

FLIGHT_DATA_ENDPOINT = "https://app.100daysofpython.dev/v1/flights/search"

class FlightSearch:
    """
    This class is responsible for talking to the Flight Search API.
    """


    def __init__(self):
        self._api_key = os.getenv("API_KEY")


    def check_flights(self, origin_city_code="", destination_city_code="", from_time=None, to_time=None):
        param = {
            "engine": "google_flights",
            "departure_id": "LHR",
            "arrival_id": "CDG",
            "outbound_date": from_time,
            "return_date": to_time,
            "type": "1",
            "adults": "1",
            "currency": "GBP",
            "api_key": self._api_key,
        }

        response = requests.get(url=FLIGHT_DATA_ENDPOINT, params=param)

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            return None

        data = response.json()
        if "error" in data:
            print(f"API Error: {data["error"]}")
            return None
        return data
