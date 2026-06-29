from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
from datetime import datetime, timedelta
import flight_data



# Sheety Data
user_data = DataManager()
user_bucket_list = user_data.get_data()



# Getting dates
tomorrow = (datetime.now() + timedelta(1)).strftime("%Y-%m-%d")
six_months_later = (datetime.now() + timedelta(30 * 6)).strftime("%Y-%m-%d")


# Requesting Flight Data
flight_Data = FlightSearch()
ORIGIN_CITY_IATA = "LHR"

for destination in user_bucket_list:
    pprint(f"Getting flights for {destination['city']}...")
    flights = flight_Data.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months_later
    )

cheapest_flight = flight_data.find_cheap_flight(data=flights, return_date=six_months_later)
pprint(f"{user_bucket_list[0]['city']}: GBP {cheapest_flight.price}")

if cheapest_flight.price != "N/A" and cheapest_flight.price < user_bucket_list[0]["lowestPrice"]:
    pprint(f"Lower price flight found to {user_bucket_list[0]['city']}!")
    user_data.update_lowest_price(user_bucket_list[0]["id"], cheapest_flight.price)
