# Step 1
  
Your goal is to build a Hangman game using everything you have learnt about Python programming.
  
Demo Final Project
https://appbrewery.github.io/python-day7-demo/
  
The project is split into 5 major steps. In each step, there will be multiple TODOs. Your goal is to go through each todo in order and complete them.
  
You can view all the todos easily in PyCharm by going to View -> Tool Windows -> TODOs
  
**TODO-1**  
Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
  
**TODO-2**  
Ask the user to guess a letter and assign their answer to a variable called guess. Make the String stored in guess lowercase.
  
**Hint 1**  
Search Google for the lower() function in Python.  

**TODO-3**  
Check if the letter the user guessed guess is one of the letters in the chosen_word. Loop through each of the letters in the chosen_word and print "Right" if the letter is a match, "Wrong" if it's not.
  
**Hint 2**  
You can loop through Strings the same way you can loop through Lists - by using the `for in` loop. Try Googling: "Loop through strings python"


# Step 2
**TODO-1**  
Create an empty String called placeholder.
For each letter in the chosen_word, add a `_` to placeholder.
So if the chosen_word was "apple", placeholder should be `_ _ _ _ _` with 5 `"_"` representing each letter to guess.
Print out hint.  

**Hint 1**  
Remember you can use the range() function inside a loop to carry out an 
action for a particular number of times.


**TODO-2**
- Create an empty string called "display".
- Loop through each letter in the chosen_word
- If the letter at that position matches guess then reveal that letter in the display at that position.
e.g. If the user guessed "p" and the chosen word was "apple", then display should be _ p p _ _.
- Print display and you should see the guessed letter in the correct position.
- But every letter that is not a match is represented with a `"_"`.  

**Hint 2**
Remember that the for loop will go through each letter in the chosen_word in 
order. You can use that fact to create a new string, 
appending the letter or an "_".

# Step 3 

**TODO-1**    
Use a while loop to let the user guess again.
The loop should only stop once the user has guessed all the letters in the chosen_word.
At that point display has no more blanks ("_"). Then you can tell the user they've won.

**Hint 1**     
You can use the in keyword to check if a String or List contains a particular item.
e.g. Google: check if a letter is present in a string python

**TODO-2**    
Update the for loop so that previous guesses are added to the display String.
At the moment, when the user makes a new guess, the previous guess gets replaced by a "_". We need to fix that by updating the for loop.

**Hint 2**  
Think about how you can store the matched letters and use an elif to check if a letter has been matched before.

# Step 4

**TODO-1:**  
Create a variable called lives to keep track of the number of lives left.
Set lives to equal 6.

**TODO-2:**  
If guess is not a letter in the chosen_word, Then reduce lives by 1.
If lives goes down to 0 then the game should end, and it should print "You lose."

**Hint:**  
The not in keywords will be your friend in this todo. You can check if something exists in the chosen_word completely separately from the rest of the code.

**TODO-3:**  
print the ASCII art from the list stages that corresponds to the current number of lives the user has remaining.

# Step 5
