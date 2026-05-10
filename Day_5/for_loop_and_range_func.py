# Sometimes, we want to use a for loop in complete independence with
# the lists

# range() function creates a range of function to loop through.
'''
for number in range(a,b):
    print(number)
'''
# range function don't actually do anything by itself
print(range(1,10))

# the range below will be 1 to 10 and not including 10
# it does not print the last digit.
for number in range(1, 10):
    print(number)

# to get from 1 to 10, we have to use 11 in upto
for number in range(1, 11):
    print(number)

# By default, the range() function will step through all the numbers
# from the start to the end, and it will increase by one.

# If we wanna increase by any other number, than you have to add comma
# and specify how large you want the step to be


for number in range(1, 11, 3):
    print(number)


## Solving the gauss problem
sum = 0
for i in range(100,0,-1):
    sum += i
print(sum)
