# Dictionary Comprehension
import random

# Just like list comprehension, dictionary comprehensions are also
# very useful

# new_dict = {new_key: new_value for item in list}

# created using {}
# mentioned are new key: new value and iterable.
# this is the simplest form

# just a way to create a dictionary using a shortened syntax


# we can also create a dictionary using an already existing dictionary
# new_dict = {new_key: new_value for (key, value) in dict.items()}
# getting all the keys and value using "dict.items()" and splitting them

# to go one step further, we can also add conditions in our dictionary comprehension
# just like list comprehension.
# new_dict = {new_key: new_value for item in list if test}


names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {
    name:random.randint(1, 100) for name in names
}
print(student_scores)


# taking it further
# looping through a dictionary

passed_students = {
    name: score for name, score in student_scores.items() if score >= 60
}
print(passed_students)
