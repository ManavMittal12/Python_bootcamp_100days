# Other Tkinter Widgets: Radiobuttons, Scales, Check-buttons and more
import tkinter as tk

display = tk.Tk()
display.minsize(width=600, height=600)
display.title("Widgets Examples")

label = tk.Label(text="My Widgets")
label.pack()

def change_title():
    var = text_entry.get()
    label.config(text=var)


button = tk.Button(text="Click", command=change_title)
button.pack()

text_entry = tk.Entry()
text_entry.pack()


## Text Entry Box - Allows multiple lines of text
## Spin box - Counter
## Scale - A slider
## checkbox
## radiobuttons
## list box of choices
## Refer to Other_Tkinter_Widgets.py for example##






display.mainloop()
