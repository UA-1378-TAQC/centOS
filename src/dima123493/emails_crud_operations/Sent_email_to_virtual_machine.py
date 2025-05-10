import smtplib
import os
from email.mime.text import MIMEText
from pathlib import Path

from dotenv import load_dotenv

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

smtp_server = os.getenv("HOSTNAME")
port = os.getenv("PORT")
sender = os.getenv("SENDER")
recipient = os.getenv("RECIPIENT")

msg = MIMEText("This is a test letter")
msg["Subject"] = "Test Email"
msg["From"] = sender
msg["To"] = recipient

with smtplib.SMTP(smtp_server, port) as server:
    server.send_message(msg)

print("✅ Letter is sent to SMTP server of CentOS!")
