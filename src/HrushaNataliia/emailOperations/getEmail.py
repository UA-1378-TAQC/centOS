import paramiko
import os
from dotenv import load_dotenv

load_dotenv()

hostname = os.getenv("HOSTNAME")
username = os.getenv("USERNAME1")
password = os.getenv("PASSWORD")
mail_file = os.getenv("MAIL_FILE")

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy (paramiko.AutoAddPolicy())
ssh.connect(hostname, username=username, password=password)

stdin, stdout, stderr = ssh.exec_command(f"cat {mail_file}")
mail_content = stdout.read().decode()

print("CentOS email box content:")
print(mail_content)

ssh.close()
