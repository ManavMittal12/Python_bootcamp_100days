# Tkinter: buttons, entry and setting component option
import tkinter
from tkinter import Entry

display = tkinter.Tk()
display.title("FirstGUI")
display.minsize(width=600, height=600)


# Label
my_label = tkinter.Label(text="I am a Label", font=("Ariel", 24, "bold"))
my_label.pack()

# ways to change the value of a labels
my_label["text"] = "New Text"
my_label.config(text="Newer Text")


# In addition to labels, we can also create buttons.
# Button

def button_click():
    new_val = input.get()
    my_label.config(text=new_val)
    print("I got clicked")



button = tkinter.Button(text = "Click Me", command=button_click)
button.pack()

# Entry component
input = tkinter.Entry(width=10) # for an entry box.
input.pack()
# to get hold of the entry
# new_val = input.get()


display.mainloop()
# first screen created is put on the screen first.
