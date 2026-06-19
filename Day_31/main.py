import random
import tkinter
from tkinter import PhotoImage
import pandas



BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
SPANISH = "Spanish"
ENGLISH = "English"
current_word = None
to_learn_words = []

# Picking Word
try:
    word_dictionary = pandas.read_csv("data/words_to_learn.csv").to_dict(orient="records")
except FileNotFoundError:
    word_dictionary = pandas.read_csv("data/spanish_words.csv").to_dict(orient="records")
    print("Loading up spanish_words.csv......")
else:
    print("Loading up words_to_learn.csv......")

def next_card():
    global current_word, timer

    display.after_cancel(timer)
    current_word = random.choice(word_dictionary)
    canvas1.itemconfig(card_img, image=card_front_img)
    canvas1.itemconfig(language, text=SPANISH, fill="black")
    canvas1.itemconfig(language_word, text = current_word[SPANISH], fill="black")
    timer = display.after(3000, func=flip_card)



def flip_card():
    canvas1.itemconfig(card_img, image=card_back_img)
    canvas1.itemconfig(language, text=ENGLISH, fill="white")
    canvas1.itemconfig(language_word, text = current_word[ENGLISH], fill="white")


def word_known():
    global word_dictionary
    word_dictionary.remove(current_word)
    next_card()

def words_to_learn():
    global to_learn_words
    to_learn_words.append(current_word)
    to_learn_dict = pandas.DataFrame(to_learn_words)
    to_learn_dict.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# UI

display = tkinter.Tk()
display.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
display.title("Flash Cards")
timer = display.after(3000, func=flip_card)

canvas1 = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = tkinter.PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_img = canvas1.create_image(400, 263, image=card_front_img)
language= canvas1.create_text(400, 150, font=LANGUAGE_FONT)
language_word = canvas1.create_text(400, 263, font=WORD_FONT)
canvas1.grid(row=0, column=0, columnspan=2)


wrong_sign_img = tkinter.PhotoImage(file="images/wrong.png")
wrong_sign = tkinter.Button(image=wrong_sign_img, highlightcolor=BACKGROUND_COLOR, highlightthickness=0, command=words_to_learn)
wrong_sign.grid(row=1, column=0)


correct_sign_img = tkinter.PhotoImage(file="images/right.png")
correct_sign = tkinter.Button(image=correct_sign_img, highlightcolor=BACKGROUND_COLOR, highlightthickness=0, command=word_known)
correct_sign.grid(row=1, column=1)



next_card()

display.mainloop()
