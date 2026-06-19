import random
import smtplib
import datetime as dt


with open("quotes.txt") as quotes:
    quotes_list = quotes.readlines()


quote_selected = random.choice(quotes_list)
message = f"""Subject: Friday fun day quote\n\n
Hey,
Greetings!\n
Here's your quote of the day to cheer you up.\n
{quote_selected}\n
I hope you are cheered up!
Thanks & Regards
Manav Mittal
"""



today = dt.datetime.now().isoweekday()
if today == 5:
    my_email = "manavmittal1211@gmail.com"
    with open("D:/python_google.txt") as pass_file:
        password = pass_file.read()
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=message
        )
