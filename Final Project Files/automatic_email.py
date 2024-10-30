import smtplib
import getpass

def send_welcome_email():
    sender_email = "asameri@kenafricind.com"
    sender_password = getpass.getpass("Password ")
    user_name = input("Please enter your name: ")
    user_email = input("Please enter your email: ")

    message = f"Welcome {user_name} to our platform."

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, user_email, message)

    print(f"Your email was sent to {user_email}")
send_welcome_email()