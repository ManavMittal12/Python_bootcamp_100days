# Caesar Cipher part 1
  
You are going to build an encryption and decryption program using the Caesar cipher.
  
Demo
https://appbrewery.github.io/python-day8-demo/
  
  
#### TODO-1:    
Create a function called encrypt() that takes original_text and shift_amount as 2 inputs.
  
#### TODO-2: 
Inside the 'encrypt' function, shift each letter of the original_text forwards in the alphabet by the 
shift_amount and print the encrypted text.
  
You can use the built-in Python index() function to find out the position of an item in a list. e.g.  
  
```python
fruits = ["Apple", "Pear", "Orange"]
fruits.index("Pear") #1
```  
e.g. If we have following values:
  
```python  
plain_text = "hello"
shift_amount = 1
```  

The final encrypted output should be:
```python
Here is the encoded result: ifmmp
```

Where each of the letters of 'hello' is shifted up by 1.
  
**Hint 1**   
Let's breakdown the problem:  

1. You need a for loop to loop through each of the letters in the plain_text.
2. Find the position of each letter in the alphabet List
3. Add the user desired shift_amount to the position to get the position of the encoded letter.
4. Find the corresponding letter for that position.
5. Add each encoded letter to a new string and print it out after the loop ends.

#### TODO-3:  
Call the encrypt() function and pass in the user inputs. You should be able to test the code and encrypt a message.

#### TODO-4:  
What happens if you try to shift the letter 'z' forwards by 9? Can you fix the code?

**Hint 2**   
There are many approaches to do this. 1. You can add more than 1 set of the alphabet into the List of alphabet letters. 2. You can shift the shift_amount so that it is always within 0 - 25 and fits in the List. 3. You can use the modulo to get the remainder.



# Caesar Cipher part 2

#### TODO-1:  
Create a function called decrypt() that takes original_text and shift_amount as 2 inputs.

#### TODO-2:  
Inside the decrypt() function, shift each letter of the original_text forwards in the alphabet backwards by the shift_amount and print the decrypted text.
  
**Hint 1**   
You can multiply any number by -1 to make it a negative number.

#### TODO-3:  
Combine the encrypt() and decrypt() functions into a single function called caesar().
Use the value of the user chosen direction variable to determine which functionality to use.
call the caesar function instead of encrypt/decrypt and pass in all three variables direction/text/shift.

**Hint 2**   
Remember that when you multiply a number by -1 it will reverse its sign. e.g. 3 + ( 5 * -1) is the same as 3 - 5.  

**Hint 3**  
It should say:

```python
Here is the encoded result: XXX
```

or

```python
Here is the decoded result: XXX
```

# Caesar Cipher part 3

#### TODO-1:  
Import and print the logo from art.py when the program starts.

#### TODO-2:  
What happens if the user enters a number/symbol/space that's not in the List alphabet?
  
Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?

e.g.

```python
original_text = "meet me at 3!"
cipher_text = "XXXX XX XX 3!"
```

**Hint 1** 
If it's not a letter in the List alphabet, maybe you can just add it to the end of cipher_text as the unmodified character?

#### TODO-3:  
Can you figure out a way to restart the cipher program?

e.g.

```
Type 'yes' if you want to go again. Otherwise, type 'no'.
```

If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again.


**Hint 2**   
Try creating a while loop that continues to execute the program if the user types 'yes'.
