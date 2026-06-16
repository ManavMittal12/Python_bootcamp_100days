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
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    checkmarks.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_min = WORK_MIN * 60
    short_break_min = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_min)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_min)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_min)
        timer_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
# we can use time module
'''
# great in principle but we are working with gui
import time

count = 5
while True:
    time.sleep(1)
    count -= 1
    
# GUI keeps listening for events and refresh, and when something happens 
it needs to react
# it needs to be event driven

# there's a loop called main loop that we are using, if we 
use another loop, it won't reach the mainloop to check the changed
and when the countdown is completed, only then will the timer will be updated 
and not be shown on the gui.

so we have to rethink it
there's a tkinter method 
'''
def count_down(count):
    global timer
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    # in canvas, the way we change element is different then changing the label
    # if label was there,we would have used
    # title.config(text="new text")

    # for canvas, we have to tap into the canvas, then we use the method .itemconfig() and give the element we want to change
    # then we mention the thing about it we want to change.
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)   # time in milliseconds to wait
    else:
        start_timer()
        mark = ""
        work_session = reps // 2
        for _ in range(work_session):
            mark = "✔"
            checkmarks.config(text=mark)

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
timer_text = canvas.create_text(125, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
checkmarks = Label(font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)
checkmarks.grid(row=3, column=1)
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)


window.mainloop()
