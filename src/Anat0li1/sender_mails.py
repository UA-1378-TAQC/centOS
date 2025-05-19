import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER = os.getenv("SERVER_IP")
SMTP_PORT = os.getenv("SEND_PORT")
EMAIL_FROM = os.getenv("SENDER_MAIL")
EMAIL_TO = os.getenv("TARGET_MAIL")


subject = "Test from Windows"
body = f"This is a test email sent from Windows via Postfix on CentOS. (to {EMAIL_TO})"

def send_email(server, port, sender, recipient, subject, body):
    message = f"""\
        Subject: {subject}
        To: {EMAIL_TO}
        From: {EMAIL_FROM}

        {body}
        """
    with smtplib.SMTP(server, port) as smtp:
        smtp.sendmail(sender, recipient, message)
        print("✅ На цей раз повезло")


if __name__ == "__main__":
    send_email(SMTP_SERVER, SMTP_PORT, EMAIL_FROM, EMAIL_TO, subject, body)