import os
from src.dima123493.utils.env_loader import load_env_vars
from src.dima123493.utils.ssh_utils import ssh_connection

load_env_vars()

def read_centos_mails():
    hostname = os.getenv("HOSTNAME")
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    mail_file = os.getenv("MAIL_FILE")

    with ssh_connection(hostname, username, password) as ssh:
        stdin, stdout, stderr = ssh.exec_command(f"cat {mail_file}")
        mail_content = stdout.read().decode()

        print("📬 CentOS email box content:")
        print(mail_content)

if __name__ == "__main__":
    read_centos_mails()
