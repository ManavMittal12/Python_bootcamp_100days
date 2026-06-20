from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:

    # we have imported the QuizBrain above and doing type annotation
    # to tell python that the quiz_brain object is of QuizBrain type.
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label()
        self.score_label.config(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125, font=FONT, fill=THEME_COLOR, width=280)



        self.tick = PhotoImage(file="images/true.png")
        self.cross = PhotoImage(file="images/false.png")
        self.tick_button = Button(image=self.tick, highlightthickness=0, command=self.pressed_true)
        self.tick_button.grid(column=0, row=2)
        self.cross_button = Button(image=self.cross, highlightthickness=0, command=self.pressed_false)
        self.cross_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        # when we use this, python doesn't know the data type of the
        # object. So, to help python, we can use type annotation.
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.tick_button.config(state="disabled")
            self.cross_button.config(state="disabled")


    def pressed_true(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def pressed_false(self):
        self.give_feedback(self.quiz.check_answer("False"))


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000 ,self.get_next_question)
