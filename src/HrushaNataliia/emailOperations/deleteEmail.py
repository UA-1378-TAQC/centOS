import paramiko
import os
from dotenv import load_dotenv

load_dotenv()

hostname = os.getenv("HOSTNAME")
username = os.getenv("USERNAME1")
password = os.getenv("PASSWORD")
mail_file = os.getenv("MAIL_FILE")

def clear_mailbox():

    with paramiko.SSHClient() as ssh:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, username=username, password=password)
        ssh.exec_command(f"> {mail_file}")
        ssh.exec_command("sync")

if __name__ == "__main__":
        clear_mailbox()
