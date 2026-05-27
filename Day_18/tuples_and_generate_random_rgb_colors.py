# with pencolor(you can use an rgb color )

# Tuple
# Tuple is a data type in python
# it has round brackets and each item is separated by a comma.
# it looks kind of similar to list

# eg
tuplee = (1 , 2 , 3)

# to get hold of an element, we do this
print(tuplee[0])


# what's the difference between list and tuples

# Tuple is carved in stone so you can't change the value list you
# can with the list

# tuplee[2] = 12  # we'll get a typeError, tuple doesn't support item assignment
# once you create a tuple, you can think of it as carved in stone.

# this is called immutable, and tuples are immutable.

# Why would you wanna use a tuple?
# for example, you are creating a color scheme for your website or are creating a
# some sort of list that you want to stay constant, and you don't want somebody to
# accidentally change it or accidentally mess it up, then you can think of creating a tuple.
# and if you find yourself creating a tuple and realizing that you need to change it
# then you can simply put your tuple inside a list like this,
list(tuplee)
# and then convert it into a list
