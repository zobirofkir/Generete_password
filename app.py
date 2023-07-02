import random
import smtplib
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def send_email(sender, recipient, subject, message):
    smtp_server = 'your_smtp_server'
    smtp_port = 587
    smtp_username = 'zobir'
    smtp_password = 'ofkir'

    email_message = f"Subject: {subject}\n\n{message}"

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender, recipient, email_message)

password = generate_password(12)
print("Generated Password:", password)

sender = 'zobirofkir19@gmail.com'
recipient = 'zobirofkir19@gmail.com'
subject = 'Generated Password'
message = f"Your password is: {password}"

send_email(sender, recipient, subject, message)
