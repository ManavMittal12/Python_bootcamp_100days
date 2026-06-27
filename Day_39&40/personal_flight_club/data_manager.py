import requests
import requests_cache
from dotenv import load_dotenv
import os

requests_cache.install_cache("sheet_data")
load_dotenv(".env")

class DataManager:
    """
    This class is responsible for talking to the Google Sheet.
    """

    def __init__(self):
        self._user = os.getenv("usrname")
        self._proj_name = os.getenv("PROJECT_NAME")
        self._sheet_name = os.getenv("SHEET_NAME")
        self._sheety_api_endpoint = f"https://api.sheety.co/{self._user}/{self._proj_name}/{self._sheet_name}"
        self._header = {"Authorization" : os.getenv("Authorization")}


    def get_data(self) -> list:
        """
        Request for data from Google Sheet
        :return a list of places on bucketlist:
        """
        response = requests.get(url=self._sheety_api_endpoint, headers=self._header)
        return response.json()
