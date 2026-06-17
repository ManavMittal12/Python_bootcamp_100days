from tkinter import *   # * imports all the classes and constants but doesn't import submodules.
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list.extend([choice(symbols) for _ in range(randint(2, 4))])
    password_list.extend([choice(numbers) for _ in range(randint(2, 4))])

    shuffle(password_list)

    password = "".join([char for char in password_list])

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_user_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops!", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \n Password: {password} \nIs it okay to save?" )
        if is_ok:
            with open("data.txt", "a") as user_data:
                user_data.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                email_user_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry()
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2,  sticky="EW")


email_user_label = Label(text="Email/Username:")
email_user_label.grid(column=0, row=2)
email_user_entry = Entry()
email_user_entry.insert(0, "iambatman@batcave.com")
email_user_entry.grid(column=1, row=2, columnspan=2,  sticky="EW")


password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="EW")

generate_pass_button = Button(text="Generate Password", command=password_generator)
generate_pass_button.grid(column=2, row=3,  sticky="EW")

add_button = Button(text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2,  sticky="EW")

window.mainloop()
