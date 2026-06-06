from statistics import mean

import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])
print(type(data))

# we can do type checks on the objects
# what exactly is the data type of the data we getting from pandas


# two primary data structures in pandas
# series
# dataframe

# a data frame is equivalent to the whole table here
# so every single sheet inside Excel, or google sheet is data frame in pandas

# what about the single column?
print(type(data["temp"]))
# this is a pandas series object
# series is basically equivalent to a list, it's like a single column in your table.
# like in the data we are using as an example
# day column, temp and condition column are a series.

# every single column is a series, equivalent to a list


# API Reference
# we have the list of all the things we can do with pandas

data_dict = data.to_dict()
print(data_dict)

# converting a series in the list form
temp_list = data["temp"].to_list()
print(temp_list)


# avg temperature from our temperature column
print(round(mean(temp_list), 2))


# using the long way
avg_val = sum(temp_list)/len(temp_list)
print(round(avg_val, 2))

# using pandas
print(data["temp"].mean())


# get maximum value from temp using data series methods.
print(data["temp"].max())


# Get data in columns
# take the dataframe, use set of square brackets and specify the name
# of the column which it takes by default as the name of the column
print(data["condition"])    # have to be vigilant about the column names type sensitivity

# alternative way to using square bracket notation is
# pandas behind the scenes took all the headings and converted it
# into attributes
print(data.condition)   # when using this method, we are treating the column as attribute



# How to get data, which are in the rows of the dataframe
# get data in rows

# e.g. from our example, taking data from monday

# we start with mentioning the dataframe name, then in the square bracket, get the hold of the column
# and then telling if the row with value square to something eg "MONDAY"
print(data[data.day == "Monday"])
print(data[data["day"] == "Monday"])

# pull the data from the row of data where the temperature was maximum
print(data[data.temp == data.temp.max()])


# we extracted the row below
monday = data[data.day == "Monday"]

# we are printing data from the row for a particular column below
print(monday.condition)



# Challenge, Monday's temperature
print(((monday.temp) * 9/5) + 32)
print(((monday.temp[0]) * 9/5) + 32)



# creating a dataframe from scratch
data_dict = {
    "students" : ["Amy", "James", "Angela"],
    "scores" : [76, 56, 65]
}
# we will mention the library, then the dataframe class
# we initialize the data
data1 = pandas.DataFrame(data_dict)
print(data1)

# new csv file created with the data that we gave into the csv.

# Pandas is really powerful :)


# we can go even further than this
# we can convert it to the csv file using ".to_csv()"
data1.to_csv("new_data.csv")  # we mention the path inside the .to_csv()
# where we want our file to be extracted
