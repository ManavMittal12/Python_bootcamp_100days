# Reading CSV data in python

# CSV is a common way of representing the tabular data
# The data that fits into tables, like spreadsheet
# CSV - Comma Separated Values


# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data) # it would be a pain to work with str data and would need a lot of
        # cleaning of each row
        # what could we do instead ?


# There's an inbuilt library in python
import csv
# it helps with csv, python is used for data processing and data analysis
# so there are great tools


with open("weather_data.csv", "r") as data_file:
    data = csv.reader(data_file)        # takes the file in questions, that is opened and read it
    # and output the data
    print(data) # creates a csv data object with can be looped through.
    temperature = []
    for row in data:
        print(row)  # Separated each item in single value.
        if row[1] != "temp":
            temperature.append(int(row[1]))

    # challenge, create a list which contains all the temp, and in integer format
    print(temperature)
