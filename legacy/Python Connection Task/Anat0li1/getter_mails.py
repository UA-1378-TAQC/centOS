import imaplib
import email
from email.header import decode_header
from dotenv import load_dotenv
import os

load_dotenv()

IMAP_SERVER = os.getenv("SERVER_IP")
IMAP_PORT = os.getenv("GET_PORT")
EMAIL_USER = os.getenv("USER_LOGIN")
EMAIL_PASS = os.getenv("USER_PASS")

def decode_str(s):
    decoded, enc = decode_header(s)[0]
    return decoded.decode(enc or 'utf-8') if isinstance(decoded, bytes) else decoded

def get_user_emails(server, port, user, password):
    with imaplib.IMAP4_SSL(server, port) as mail:
        mail.login(user, password)
        mail.select("inbox")

        status, messages = mail.search(None, "ALL")
        for num in messages[0].split():
            status, data = mail.fetch(num, "(RFC822)")
            msg = email.message_from_bytes(data[0][1])

            subject = decode_str(msg["Subject"])
            sender = decode_str(msg["From"])

            print(f"Від: {sender}")
            print(f"Тема: {subject}")

            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        print("Текст листа:")
                        print(part.get_payload(decode=True).decode())
                        break
            else:
                print("Текст листа:")
                print(msg.get_payload(decode=True).decode())

            print("=" * 100)

if __name__ == "__main__":
    get_user_emails(IMAP_SERVER, IMAP_PORT, EMAIL_USER, EMAIL_PASS)