


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(directions, original_text, shift_amount):
    def encrypt():
        cipher_text = ""
        for letter in original_text:
            if letter.isalpha():
                shift_position = alphabet.index(letter) + shift_amount
                shift_position %= len(alphabet)
                cipher_text += alphabet[shift_position]
            else:
                cipher_text += " "
        print(f"Here is the encoded results: {cipher_text}")


    def decrypt():
        output_text = ""
        for letter in original_text:
            if letter.isalpha():
                restored_position = alphabet.index(letter) + shift_amount*(-1)
                restored_position %= len(alphabet)
                output_text += alphabet[restored_position]
            else:
                output_text += " "
        print(f"Here is the decoded result: {output_text}")

    if directions == "encode":
        encrypt()
    elif direction == "decode":
        decrypt()
		
caesar(direction, text, shift)
'''

# TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?
continue_flag = True
while continue_flag:
    def caesar(original_text, shift_amount, encode_or_decode):
        output_text = ""

        if encode_or_decode == "decode":
            shift_amount *= -1

        for letter in original_text:
            if letter.isalpha():
                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position %= len(alphabet)
                output_text += alphabet[shifted_position]
            else:
                output_text += letter

        print(f"Here is the {encode_or_decode}d result: {output_text}")


    # TODO-3: Can you figure out a way to restart the cipher program?


    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    user_flag = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").casefold()
    if user_flag == "no":
        continue_flag = False
