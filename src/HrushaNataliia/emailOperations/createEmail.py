import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

smtp_server = os.getenv("HOSTNAME")
port = os.getenv("PORT")
sender = os.getenv("SENDER")
recipient = os.getenv("RECIPIENT")

def send_test_email():

    msg = MIMEText("This is a test letter")
    msg["Subject"] = "Test Email"
    msg["From"] = sender
    msg["To"] = recipient

    with smtplib.SMTP(smtp_server, port) as server:
        server.send_message(msg)

if __name__ == "__main__":
        send_test_email()
