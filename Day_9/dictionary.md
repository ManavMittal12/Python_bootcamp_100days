# Dictionaries in Python
They work kind of similarly to the dictionaries in real-life

for example
We tryna find the word code in a dictionary, we'll get back the meaning of it

**for example**  
code : program instructions

Dictionaries are really useful because they allow us to group together 
and tag related pieces of information.

**You can think of dictionaries as a form of a table**   
There are two parts to it, left side is key, that is the 
equivalent of the word in the dictionary ,and then 
it also get an associated value. That would be the equivalent of the actual
definition of the word.

| KEY          | VALUE |
|--------------|-------------------------------------------------------------------------|
| Bug          |An error in a program that prevents the program<br/> from running as expected.|
| Function     |A piece of code that you can <br/>easily call over and over again|
| Loop         |The action of doing something over and over again.              |


### Syntax looks like : 
## {Key: Value}

Starts with curly braces, inside the curly braces goes the content of
the dictionary. Inside the curly braces, the **Key** goes first,
followed by a colon and then followed by a **Value**.


eg:  
```python
{  
"Bug" : "An error in a program that prevents the program from running as expected.",  
"Function": "A piece of code that you can easily call over and over again",  
"Loop" :"The action of doing something over and over again."  
}
```
what it we want to have more than one entry, we can separate each key value 
pairs with a comma, then we can continue adding key:value pairs until we get to the end of the dictionaries.

when you create a dictionary which has more than one key value pairs
we wanna format it properly.

There's a convention in python, starting the dictionary with a curly braces at top
every subsequent entry be indented by one indent.  and then end, there's a comma at the end,
and we hit enter and other values.
finally, the last curly brace should go at the very beginning in line with
the start of the dictionary.
also, cap off all the entries with a comma at the end, this means that if you
need to add more items into the dictionary, you can simply just hit enter.


What if we want to retrieve an item from the dictionary?
with list, we can use the name of the list, a set of square brackets and
give the index of the value we want to extract.
```list[2]```


for dictionaries, it's kind of the same, the only difference is that for dictionaries  have elements that are identified with their key

for our dictionary for example, we have a string key called Bug  
```pyhton
print(programming_dictionary["Bug"])
```

Be sure to spell the key correctly.
otherwise, we'll get the key error.

Like in list, when we use to type an index that was not there in the list
we use to get an index error,
similarly, here we get the KeyError, if we try to type in the wrong key that doesn't exist
we'll get an Error.

Remember, if you are putting a string literal as a key, you need to
have the surrounding quotes.
even while accessing the data.

----

**What if we want to add a piece of data to a dictionary?**  
```python
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)
```

When writing a code, it's helpful to start out with an empty dictionary
you can simply create it with a set of empty curly braces.
```python
empty_dictionary = {}
```

**What if you want to wipe an empty dictionary?**  
Wipe an existing dictionary

```python
programming_dictionary = {}  # We can also use the same method to wipe off the dictionary.
print(programming_dictionary)
```

Now, this method of tapping into a dictionary, using the key to fetch the 
relevant item from it, and then doing something with it goes beyond adding 

We can edit item in dictionary too  
```python
print("Bug")
programming_dictionary["Bug"] = "A moth in your computer"  # Editing the entry
```
if it finds the key, it will update the entry   
if it does not find it, it will end this entry to the very end of the 
dictionary.

```python
print(programming_dictionary["Bug"])
```

#### Looping through a dictionary  
```python
for thing in programming_dictionary:
    print(thing)
    print(programming_dictionary[thing])    # We can access the values as well using this.
```
The above program returns us with just the keys of the dictionary
