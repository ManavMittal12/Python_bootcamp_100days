# How to send mails using SMTP
# SMTP - Simple mail transfer protocol
# how mail is sent is
# we create a mail and send it from our email
# it goes to gmail server, from gmail server it goes to for example
# yahoo server, and from there, to the recipient
# SMTP is like postman in this process

# there's a library called SMTPLIB in python
import smtplib



my_email = "manavmittal1211@gmail.com"
with open("D:/python_google.txt") as pass_file:
    password = pass_file.read()


# connection = smtplib.SMTP("smtp.gmail.com", port=587)
# connection.starttls()   # TLS - Transport layer security, it's a way of securing our connection to our email server.
# # it will encrypt the message in transit.
#
# connection.login(user=my_email, password=password)
# connection.sendmail(
#     from_addr=my_email,
#     to_addrs=my_email,
#     msg="Subject: This is my first mail using smtplib\n\nThis is the body of my email, Pretty messed up right ?"
# )
# connection.close()  # we can avoid closing this manually by using the trick in the file handling

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=my_email,
        msg="Subject: This is my first mail using smtplib\n\nThis is the body of my email, Pretty messed up right ?"
    )
