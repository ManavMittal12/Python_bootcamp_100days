import pandas as pd

#TODO 1. Create a dictionary in this format:

nato_phonetic_dict = {
    row.letter: row.code for index,row in pd.read_csv("nato_phonetic_alphabet.csv").iterrows()
}

print(nato_phonetic_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = list(input("Enter the word: ").upper())

output_phonetic = [nato_phonetic_dict[letter] for letter in user_input if letter in nato_phonetic_dict.keys()]
print(output_phonetic)
