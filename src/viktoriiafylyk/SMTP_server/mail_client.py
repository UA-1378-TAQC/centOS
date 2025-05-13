import os
import smtplib
import imaplib
import email
from email.message import EmailMessage
from dotenv import load_dotenv
from typing import Dict


def load_config() -> Dict[str, str]:
    load_dotenv()
    return {
        'SMTP_SERVER': os.getenv('SMTP_SERVER'),
        'SMTP_PORT': int(os.getenv('SMTP_PORT')),
        'IMAP_SERVER': os.getenv('IMAP_SERVER'),
        'IMAP_PORT': int(os.getenv('IMAP_PORT')),
        'EMAIL_ADDRESS': os.getenv('EMAIL_ADDRESS'),
        'EMAIL_PASSWORD': os.getenv('EMAIL_PASSWORD')
    }

def send_email(config: Dict[str, str], subject: str, body: str):
    msg = EmailMessage()
    msg['From'] = config['EMAIL_ADDRESS']
    msg['To'] = config['EMAIL_ADDRESS']
    msg['Subject'] = subject
    msg.set_content(body)

    with smtplib.SMTP(config['SMTP_SERVER'], config['SMTP_PORT']) as server:
        server.send_message(msg)
    print("Mail is sent.")

def read_emails(config: Dict[str, str]):
    with imaplib.IMAP4_SSL(config['IMAP_SERVER'], config['IMAP_PORT']) as mail:
        mail.login(config['EMAIL_ADDRESS'], config['EMAIL_PASSWORD'])
        mail.select('INBOX')

        status, messages = mail.search(None, f'FROM "{config["EMAIL_ADDRESS"]}"')
        email_ids = messages[0].split()

        for eid in email_ids:
            status, msg_data = mail.fetch(eid, '(RFC822)')
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    subject = msg['subject']
                    from_ = msg['from']
                    print(f'From: {from_}\nSubject: {subject}\n')

if __name__ == "__main__":
    config = load_config()
    send_email(config, "Test mail", "This is test mail, sent from Python.")
    read_emails(config)
