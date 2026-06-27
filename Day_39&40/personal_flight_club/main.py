
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
from datetime import datetime, timedelta



# Sheety Data
user_data = DataManager()
user_bucket_list = user_data.get_data()


# Getting dates
tomorrow = (datetime.now() + timedelta(1)).strftime("%Y-%m-%d")
six_months_later = (datetime.now() + timedelta(30 * 6)).strftime("%Y-%m-%d")


# Requesting Flight Data
flight_Data = FlightSearch()
flight_info = flight_Data.check_flights(from_time=tomorrow, to_time=six_months_later)
pprint(flight_info)
