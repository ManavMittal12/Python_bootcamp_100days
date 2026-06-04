#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: this method will help you: https://www.w3schools.com/python/ref_string_strip.asp


PLACEHOLDER = "[name]"

# with open("./Input/Letters/starting_letter.txt") as letter:
#     letter_contents = letter.readlines()


# with open("./Input/Names/invited_names.txt") as names_list:
#     names = names_list.readlines()
#
#
# for name in names:
#     file_name = f"./Output/ReadyToSend/your_letter_{name.strip("\n")}.txt"
#     with open(file_name, mode="w") as new_letter:
#         for lc in letter_contents:
#             if PLACEHOLDER in lc:
#                 new_letter.write(lc.replace(PLACEHOLDER, name.strip("\n")))
#             else:
#                 new_letter.write(lc)


with open("./Input/Names/invited_names.txt") as names_list:
    names = names_list.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    letter_contents = letter.read()

    for name in names:
        new_letter = letter_contents.replace(PLACEHOLDER,name.strip("\n"))
        with open(f"./Output/ReadyToSend/letter_for_{name.strip("\n")}.docx", mode="x") as make_letter:
            make_letter.write(new_letter)
