# Nesting lists and dictionaries
from Day_4 import nested_list

# list as well as dictionaries
# if we imagine a list or a dictionary being something like a folder
# and a lot of thing inside them
# then nesting is putting one inside the another

# eg
# {key : value}

# or

# {key: value, key2: value2}

# or we can put
# { key : [list], key2 : {dict}, }

# it gives us a lot of flexibilities

# eg
# normal dict
capitals = {
    "France" : "Paris",
    "Germany" : "Berlin",
}

# complex dict
# travel_log = {
#     "France" : ["Paris", "Lille", "Dijon"],  # Key value pairs with list as a value
#     "Germany" : ["Stuttgart", "Berlin"]
# }

# Challenge : Print Lille
# print(travel_log["France"][1])

# we can list inside another list
# Challenge : Print the letter `D` inside the nested list
nested_list = ['A', 'B', ['C', 'D']]
print(nested_list[2][1])


# We can also nest a dict inside a dict as well
travel_log = {
    "France"  : {
        "num_times_visited" : 8,
        "cities_visited" : ["Paris", "Lille", "Dijon"]
    },
    "Germany": {
        "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"],
        "total_visit" : 5
    },
}

# Challenge : Print out "Stuttgart" from the travel_log dictionary
print(travel_log["Germany"]["cities_visited"][2])
