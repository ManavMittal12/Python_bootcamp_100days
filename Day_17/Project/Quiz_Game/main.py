from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for qdata in question_data:
    question_bank.append(Question(qdata["text"], qdata["answer"]))

# very often, when we are getting data from the internet, we can do it like this.
# we convert it in our objects.

quiz = QuizBrain(question_bank)

is_quiz_on = True
while is_quiz_on:
    are_questions_left = quiz.still_has_questions()
    if are_questions_left:
        quiz.next_question()
    else:
        is_quiz_on = False


print("You've completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
