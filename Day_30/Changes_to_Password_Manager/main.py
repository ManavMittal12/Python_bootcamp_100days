import json
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
    new_data = {
        website: {
            "email" : email,
            "password" : password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops!", message="Please don't leave any fields empty!")
    else:

        # Exception Handling
        try:
            with open("data.json", "r") as user_data:
                # Writing data to JSON file.
                # json.dump(new_data, user_data, indent=4)
                # Reading the data
                # data = json.load(user_data)

                # Updating the old data
                    # Reading the old data
                data = json.load(user_data)
                # print(data)
                    # Updating the old data
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as user_data:
                json.dump(new_data, user_data, indent=4)
        else:
            with open("data.json", "w") as user_data:
                    # Saving the updated data
                json.dump(data, user_data, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def search():
    website = website_entry.get()
    try:
        with open("data.json") as user_data:
            current_dataset = json.load(user_data)
        messagebox.showinfo(title=f"{website}", message=f"Email: {current_dataset[website]["email"]}\n Password: {current_dataset[website]["password"]}")
    except KeyError:
        messagebox.showerror(title="Data Not Found!", message="Can't find this website in the database.")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Datafile found.")

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
website_entry.grid(column=1, row=1, sticky="EW")
search_button = Button(text="Search", command=search)
search_button.grid(column=2, row=1,  sticky="EW")

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
