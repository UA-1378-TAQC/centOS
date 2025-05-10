from pathlib import Path

import paramiko
import os
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

hostname = os.getenv("HOSTNAME")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
mail_file = os.getenv("MAIL_FILE")

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username=username, password=password)

ssh.exec_command(f"> {mail_file}")
ssh.exec_command("sync")
print("🗑️ CentOS mails are cleared!")

ssh.close()
