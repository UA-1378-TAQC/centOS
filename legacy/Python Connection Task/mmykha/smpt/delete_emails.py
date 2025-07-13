import imaplib
from mail_config import USERNAME, IMAP_PORT, SERVER, PASSWORD, MAILBOX

def delete_emails(username, server, imap_port, mailbox, password):
    print("Connecting to IMAPS server...")
    mail = imaplib.IMAP4_SSL(server, imap_port)
    mail.login(username, password)
    mail.select(mailbox)
    result, data = mail.search(None, "FROM","windows@localhost")
    if result == 'OK':
        for num in data[0].split():
            mail.store(num, '+FLAGS', '\\Deleted')
        mail.expunge()
        print(f"Deleted {len(data[0].split())} email(s) from {mailbox}.")
    else:
        print("No emails found or search failed.")

    mail.logout()

if __name__ == "__main__":
    try:
        delete_emails(USERNAME,SERVER,IMAP_PORT,MAILBOX,PASSWORD)
    except Exception as e:
        print(e)
        