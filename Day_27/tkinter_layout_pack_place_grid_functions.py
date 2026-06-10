# Tkinter layout managers: pack(), place() and grid()
import tkinter as tk


def change_title():
    var = text_entry.get()
    label.config(text=var)
    

display = tk.Tk()
display.minsize(width=600, height=600)
display.title("Widgets Examples")
display.config(padx=20, pady=20)

label = tk.Label(text="My Widgets")
# label.pack()
# label.place(x=100, y=0)
label.config(padx=20, pady=20)
label.grid(column=0, row=0)


button = tk.Button(text="Click", command=change_title)
# button.pack()
button.grid(column=1, row=1)


button2 = tk.Button(text="Click", command=change_title)
# button.pack()
button2.grid(column=0, row=3)


text_entry = tk.Entry()
# text_entry.pack()
text_entry.grid(column=3, row=2)



# Tkinter has a bunch of layout managers that define how to
# position each of the widgets in our GUI program
# there are three that we should know about
# 1) Pack
# 2) Place
# 3) Grid


# Place - Is about precise positioning
# when we use place, we provide x and y coordinate
# downside of place is, it's so specific and we have to work out coordinates
# if we have 50 or 100 widgets, it becomes a nightmare to find exact location for
# each widget
# label.place(x=100, y=0)


# important - if a widget is created but doesn't have any layout specified,
# pack place or grid, then it won't be shown.


# In-addition pack and place, we have grid.
# the grid is simple concept
# it imagines the whole program as grid
# rows and columns
# grid system is relative to other components
# easiest way is using the grid is starting the thing we want to be on the
# top-left and then for the next and subsequent widgets to just keep going through
# it and define its position on the grid

# warning, you can't mix up grid and pack in the same program.



# how to add the padding around the components
# by directly modifying the window
# e.g. display.config(padx=20, pady=20)

# modifying the widgets

display.mainloop()
