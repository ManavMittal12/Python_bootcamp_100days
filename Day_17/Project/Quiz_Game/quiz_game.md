from Day_17.Project.Quiz_Game.question_model import Questionfrom Day_17.Project.Quiz_Game.question_model import Question

# QUIZ GAME

----

### Task 1
The first task that we have is to create a model for a question in our quiz
If we had a question object, what attribute should is have ?

```
Attributes
text
answer
```

Now these two attributes should be initialized with a value when a new_q
object is created from this class. When initialize goes through, the constructor should add them 
and analyze is. 

```
new_q = Question("2+3=5", "True")
```

Create a question class with an ```__init()__``` methods with two attributes: text and answer attributes

----

### Task 2
In this task, We will create a question bank of Question objects.
We can create a question object by giving it the name of the class 
and then give it some inputs for the question and the answers. 
Now, if we create a whole bunch of those and put it in a list, 
we can create a question bank of question to use in our quiz.

```python
question_bank = [
    Question(q1, a1),
    Question(q2, a2),
    Question(q3, a3),
    ...
]
```
Write a for loop to iterate over the ```question_data```.
Create a Question object from each entry in ```question_data```.
Append each Question object to the ```question_bank```.

----

### Task 3 
Task three is to bring up those questions and ask the user to answer the questions 
we are going to put to question functionality and checking function in quiz_brain.py

```python
# TODO1 : Asking the question
# TODO2 : Checking if the answer was correct 
# TODO3 : Checking if we are at the end of the quiz.
```

we are going to create a QuizBrain class
it will have these attributes, ```question_number = 0 ``` with a default value
and ```question_list``` 
and we're going to have method which is going to pop a new question from the list 
```next_question()```

1. Create a class called ```QuizBrain```.
2. Write an __init()__ method.
3. Initialise the question_number to 0.
4. Initialise the question_list to an input
5. Retrieve the item at the current question_number from the question_list
6. Use the input() function to show the user the question text and ask for the user's answer.

----

#### Task 4
we have to create another method ```still_has_question()```
it will return True or False, and while loop in it.
it should keep running until it runs out of questions 

1. Create method called still_has_questions()
2. Return a boolean depending on the value of question_number.
3. Use the while loop to show the next question until the end.

----

#### Task 5

1. Add an attribute ```score``` 
2. Create a new method ```check_answer()```, It's going to check if the input of the user is same as the answer.
3. tell right or wrong, and tell the answer to the user.
4. Add attribute score and increment it when user gets it right 
5. print out the score/current question
