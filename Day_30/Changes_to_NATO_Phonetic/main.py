# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("D:\\Computer_Science_Learning_Material\\Python_bootcamp_100days\\Day_30\\Changes_to_NATO_Phonetic\\nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

while True:
    try:
        word = input("Enter a word: ").upper()
        if not word.isalpha():
            raise ValueError
    except ValueError:
        print("Sorry, only letters in the alphabet please.")
    else:
        break

print(word)
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
