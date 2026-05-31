# Slicing in lists and tuples.

piano_keys = "abcdegf"
piano_keys_list = list(piano_keys)
print(piano_keys_list)


# using slicing to get elements from the piano keys
print(piano_keys_list[2: 5])   # we get a set of items
# from position 2 to position 5,

# imagine like 0 is before the first element.
'''
 a b c d e f g
0 1 2 3 4 5 6 7
'''
# you can say, it's upto but not including the last, stop element.

# or you can do is
# if you want to slice from 2 and to the end
# you can do this like this
print(piano_keys_list[2:])
# omit the stop and it will slice till the end

# it also works opposite
# if we want all the elements till position 5
print(piano_keys_list[:5])


# other than start and stop, we can add another number, step.
# step: sets the increment

print(piano_keys_list[2:5:2])
print(piano_keys_list[::2]) # skips every second one.

# you can also use negative increment and reverses the list for us
print(piano_keys_list[::-1])    # reverses the list and tuples


piano_keys_tuple = tuple(piano_keys_list)
print(piano_keys_tuple[::-1])
