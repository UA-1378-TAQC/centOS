import smtplib
from email.message import EmailMessage
from mail_config import RECEIVER, SENDER, SMTP_PORT, SERVER

def sent_email(content, subject, sender, receiver):
    msg = EmailMessage()
    msg.set_content(content)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = receiver
    with smtplib.SMTP(SERVER, SMTP_PORT) as smtp:
        smtp.send_message(msg)

if __name__ == "__main__":
    email_body = "Lets be friends :)"
    email_subject = "how are you?"
    sent_email(email_body, email_subject,SENDER,RECEIVER)
