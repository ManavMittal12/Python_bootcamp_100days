from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
# putting images on the window
# we will use "canvas widget" - is like real canvas, it allows us to layer things
# one on the other
# in our case, allows us to place and image and some text on top of it
timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)
canvas = Canvas(width=250, height=230, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")        # reads through a file and get holds of the image in the file location
canvas.create_image(125, 112, image=tomato_img)
canvas.grid(row=1, column=1)
canvas.create_text(125, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
timer_label = Label(text="✔", font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=3, column=1)
start_button = Button(text="Start", highlightthickness=0)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(row=2, column=2)


window.mainloop()
