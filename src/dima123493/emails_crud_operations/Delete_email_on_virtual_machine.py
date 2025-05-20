import os
from src.dima123493.utils.env_loader import load_env_vars
from src.dima123493.utils.ssh_utils import ssh_connection

load_env_vars()

def clear_centos_mails():
    hostname = os.getenv("HOSTNAME")
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    mail_file = os.getenv("MAIL_FILE")

    with ssh_connection(hostname, username, password) as ssh:
        ssh.exec_command(f"> {mail_file}")
        ssh.exec_command("sync")
        print("🗑️ CentOS mails are cleared!")

if __name__ == "__main__":
    clear_centos_mails()
