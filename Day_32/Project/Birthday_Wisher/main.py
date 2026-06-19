import random
import pandas as pd
import datetime as dt
import smtplib

data = pd.read_csv(filepath_or_buffer="birthdays.csv").to_dict(orient="records")
today = dt.datetime.now()
current_day = today.day
current_month = today.month


def create_a_letter():
    letters_database = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
    select_letter = random.choice(letters_database)
    with open(select_letter) as birthday_letter:
        letter = birthday_letter.read().replace("[NAME]", current_info["name"])
    return letter


def send_letter(letter):
    my_email = "sample_mail@gmail.com"
    with open("D:/python_google.txt") as pass_file:
        password = pass_file.read()

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=current_info["email"],
            msg=f"Subject: Happy Birthday!!\n\n{letter}"
        )


for current_info in data:
    if current_info["day"] == current_day and current_info["month"] == current_month:
        our_letter = create_a_letter()
        send_letter(our_letter)
