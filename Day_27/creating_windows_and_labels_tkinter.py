import tkinter

# it will go away directly
window = tkinter.Tk()
window.title("My first GUI Program")

# changing the size of the window
window.minsize(width=600, height=600)

# creating components to put inside the window
# Label
my_label = tkinter.Label(text="I am a Label", font=("Ariel", 24, "bold")) # initializing the label class
# there are other properties as well


# when we are working with tkinter, we have to first create a component
# like label then we have to specify how that component is laid out on the screen

# to do that, get hold of the component and call the function pack()
my_label.pack() # it will center it on the screen.
# packer packs the component on the screen.



# there's a while loop inside tkinter which keeps running
# and listening for instructions
window.mainloop()   # always should be very end and rest of the thing between
# creating the window and this
