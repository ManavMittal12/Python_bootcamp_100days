import pandas
from pandas import DataFrame

# Create a csv, which contains fur_color, their count, and build a new data frame and create final csv "new_data"

detailed_squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_color = detailed_squirrel_data["Primary Fur Color"].to_list()



squirrel_color_list = list(set(squirrel_color))
squirrel_color_count_list = []
for color_variants in squirrel_color_list:
    squirrel_color_count_list.append(squirrel_color.count(color_variants))

squirrel_count = {
    "Fur Color": squirrel_color_list,
    "Count": squirrel_color_count_list,
}


new_dataset = DataFrame(squirrel_count)
new_dataset.to_csv("squirrel_count.csv")
