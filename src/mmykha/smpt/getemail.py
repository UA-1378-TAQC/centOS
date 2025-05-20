import imaplib
import email
import re
from mail_config import USERNAME, SERVER, IMAP_PORT, PASSWORD, MAILBOX


def fetch_emails(username, server, imap_port, mailbox, password):
    print("Connecting to IMAPS server...")
    mail = imaplib.IMAP4_SSL(server, imap_port)
    mail.login(username, password)
    mail.select(mailbox)
    result, data = mail.search(None, "ALL")

    if result != "OK":
        print("No messages found!")
        return
    
    for num in data[0].split():
        result, data = mail.fetch(num, "(RFC822)")
        raw_email = data[0][1]
        msg = email.message_from_bytes(raw_email)

        print(f"\nFrom: {msg['From']}")
        print(f"To: {msg['To']}")
        print(f"Subject: {msg['Subject']}")
        pattern = r'(;)\s((\w*\W*)*)'
        match = re.search(pattern, msg["Received"])

        if match:
            print("Date:", match.group(2))

        body = msg.get_payload(decode=True)
        print("Body:", body.decode(errors="replace"))

        print("-" * 60)
    print("Total number of emails: ",data[0][0][0:1].decode('utf-8'))
    mail.logout()

if __name__ == "__main__":
    try:
        fetch_emails(USERNAME,SERVER,IMAP_PORT,MAILBOX,PASSWORD)
    except Exception as e:
        print(e)
