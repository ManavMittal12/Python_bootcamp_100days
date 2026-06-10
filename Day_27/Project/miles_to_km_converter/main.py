from tkinter import *


def convert_to_km():
    miles: float = float(miles_input.get())
    km: float = round((miles * 1.609344), 2)
    kilometer_result_label.config(text=f"{km}")



display = Tk()
display.title("Mile to Km Converter")
display.config(padx=20, pady=20)


miles_input = Entry(width=7)
miles_input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(row=1, column=0)


kilometer_result_label = Label(text="Km")
kilometer_result_label.grid(row=1, column=2)

calculate_button = Button(text="Calculate", command=convert_to_km)
calculate_button.grid(row=2, column=1)


display.mainloop()
