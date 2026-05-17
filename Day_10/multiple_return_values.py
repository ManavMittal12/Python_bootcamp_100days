# Multiple return values or multiple return keywords in same function

'''d
ef format_name(f_name, l_name):
    f_name = f_name.capitalize()
    l_name = l_name.capitalize()
    return f"{f_name} {l_name}"
    print("This got printed")   # This will not get executed, because return tells the interpreter that it's the
    # end of the function, and you should exit the function. You can have multiple return keyword with function, and
    # also we can have an empty return keyword without anything after-wards.
'''

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":    # By passing the rest of the code if the user enters empty first name or last name. We can use empty return
        return  # It will terminate the function early and return None, but it's recommended to return anything like a msg etc.
    f_name = f_name.capitalize()
    l_name = l_name.capitalize()
    return f"{f_name} {l_name}"




# formatted_string = format_name("micHeeeeheeeeal", "jackOUUUUuson")
# print(formatted_string)

print(format_name(input("What is your first name :"), input("What is your last name : ")))
