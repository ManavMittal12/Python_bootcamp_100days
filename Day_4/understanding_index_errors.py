states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# the above list has 50 items which means the last item has the index
# 49

# What if we try to get index 50
# print(states_of_america[50])
# We get the error
# IndexError: list index out of range
# Also called off by one error, which is very frequent.

# very frequently we'll have this

num_of_states = len(states_of_america)
# print(states_of_america[num_of_states]) # This is off by one error, we just
# need to do -1

print(states_of_america[num_of_states - 1])
