import datetime as dt

# getting the current datetime

now = dt.datetime.now()
year = now.year
month = now.month


date_of_birth = dt.datetime(year=2001, month=5, day=25, hour=15)
print(date_of_birth)
