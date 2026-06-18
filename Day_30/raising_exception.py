# raise - this allows us to do is raise our own exception

# eg
# try:
#     file = open("b_file.txt")
#     b_dictionary = {
#         "key" : "value"
#     }
#     print(b_dictionary["key"])
# except FileNotFoundError:
#     file = open("b_file", "w")
#     file.write("Learning about raising exceptions")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:    # for example, after our above code runs, we want to
#     # raise exception anyway
#     # tap into known exception classes
#     # raise TypeError
#     # we can specify a message with it
#     raise TypeError("This is a made up error ")


height = float(input("Height: "))   # what if we give some unrealistic height or weight which is not even possible
# and we might want to raise our own exception
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)
