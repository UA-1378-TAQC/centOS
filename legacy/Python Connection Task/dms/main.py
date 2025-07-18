from smtplib import SMTP, SMTPException
from email.message import EmailMessage
import paramiko

def send():
    msg = EmailMessage()
    msg.set_content("Just lose it")
    msg["Subject"] = "Test message"
    msg["From"] = "user3@example.com"
    msg["To"] = "user2@example.com"

    try:
        with SMTP("192.168.229.132", 25) as smtp: #25 587 465
            smtp.starttls()
            smtp.login("dms", "root")
            smtp.send_message(msg)
        print("Message sent successfully!")
    except SMTPException as e:
        print(f"Error occurred: {e}")

def get_message(username):
    remote_ip = "192.168.229.132"
    maildir_path = f"/home/{username}/Maildir/new"
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(remote_ip, username=username, password="root")

    sftp = ssh.open_sftp()

    try:
        files = sftp.listdir(maildir_path)
        print(f"\n--- Maildir for {username} ---")
        for fname in files:
            print(fname)
    except FileNotFoundError:
        print(f"Maildir not found for {username}")
    finally:
        sftp.close()
        ssh.close()

if __name__ == "__main__":
    get_message("user1")

