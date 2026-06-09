import pandas as pd

student_dict = {
    "student" : ["Angela", "James", "Lily"],
    "score" : [56, 76, 98],
}


# we know we can loop thru a dict using for loop
for (key, value) in student_dict.items():
    print(key, value)


# looping thru a data frame like looping thru a dictionary

student_table = pd.DataFrame(student_dict)
print(student_table)


# Loop through a data frame
for (key, value) in student_table.items():
    print(key)
    print(value)

# now this is not particularly useful, just looping thru names of columns

# pandas has its own loop
# it's called iter rows
# Loop through rows of a dataframe
# using for loop, then index and the rows, and then our data frame and calling "iterrows()"
for (index, row) in student_table.iterrows():
    # print(row)  # each row is python series object, so we can access these rows and
    # get hold of the value under a particular column by using the dot notation.
    print(row.student)
    # we can do something like this
    if row.student == "Angela":
        print(row.score)
