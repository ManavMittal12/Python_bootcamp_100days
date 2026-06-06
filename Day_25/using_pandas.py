
# what if we get csv data with way more complex data.
# with way more columns and rows
# we are going to use the Pandas library
# It's a python data analysis library to perform analysis on tabular data

# we have to install it.
import pandas
# Documentation https://pandas.pydata.org/docs/
# when using a new library, it's a good idea to look at their getting started guide.


data = pandas.read_csv("weather_data.csv") # we don't have to open the file as data file
print(data)
# It formats the data into a table form.


# getting hold of the single column of data
print(data["temp"])
# pandas takes the first row as columns and knows how to find data when we
# specify the column's name.
