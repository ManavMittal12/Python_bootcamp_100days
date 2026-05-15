# First method of Encryption

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] * 2

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.
# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

def encrypt(original_text, shift_amount):
    original_text_list = []
    for ch in original_text.casefold():
        original_text_list += ch

    for ind in range(len(original_text_list)):
        if original_text_list[ind].isalpha():
            original_text_list[ind] = alphabet[alphabet.index(original_text_list[ind]) + shift_amount ]

    encoded_message = "".join(original_text_list)
    print(f"Here is the encoded results: {encoded_message}")


# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

if direction.casefold() == "encode":
    encrypt(original_text=text, shift_amount=shift)
elif direction.casefold() == "decode":
    pass
else:
    print("Please select from 'encode' or 'decode'.")


