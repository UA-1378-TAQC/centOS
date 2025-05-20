import os
import smtplib
from email.mime.text import MIMEText

from src.dima123493.utils.env_loader import load_env_vars

load_env_vars()

def send_test_email():
    smtp_server = os.getenv("HOSTNAME")
    port = int(os.getenv("PORT"))
    sender = os.getenv("SENDER")
    recipient = os.getenv("RECIPIENT")

    msg = MIMEText("This is a test letter")
    msg["Subject"] = "Test Email"
    msg["From"] = sender
    msg["To"] = recipient

    with smtplib.SMTP(smtp_server, port) as server:
        server.send_message(msg)

    print("✅ Letter is sent to SMTP server of CentOS!")

if __name__ == "__main__":
    send_test_email()
