import smtplib
from flask import *
from validate_email import validate_email

def email_validation(x):
    emailvalid = validate_email(x)
    return emailvalid

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)


def login_gmail(gamil_user, gmail_user_password):

    try:
        server.ehlo()
        server.login(gamil_user, gmail_user_password)
        return server
    except:
        return "Invalid credentials"



def send_email(to, body):
    if (email_validation(to) ==True):
        sent_from = "abramogol@gmail.com"
        login_gmail(sent_from, "Masterabram")
        server.sendmail(sent_from, to, body)
        return "Sent!"
    else:
        return "Invalid email"

send_email("abraham.ogol@andela.com", "Setup done succcesfully")




