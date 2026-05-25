# Practice modifying object attributes and calling methods

from prettytable import PrettyTable

table = PrettyTable()   # creating an object



# Methods are functions associated with objects
table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

print(table)

'''
Output

+--------------+----------+
| Pokemon Name |   Type   |
+--------------+----------+
|   Pikachu    | Electric |
|   Squirtle   |  Water   |
|  Charmander  |   Fire   |
+--------------+----------+

'''

# Objects Attributes -->
# We can change objects attributes

# there are multiple attributes

# changing the alignment
table.align = "l"
print(table)
print(table.align)
