import paramiko
import os
from dotenv import load_dotenv

load_dotenv()

hostname = os.getenv("HOSTNAME")
username = os.getenv("USERNAME1")
password = os.getenv("PASSWORD")
mail_file = os.getenv("MAIL_FILE")

def get_mailbox_content():

    with paramiko.SSHClient() as ssh:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command(f"cat {mail_file}")
        return stdout.read().decode()

if __name__ == "__main__":
        content = get_mailbox_content()
