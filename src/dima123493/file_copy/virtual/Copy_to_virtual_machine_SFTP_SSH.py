import paramiko
from pathlib import Path
import os
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

hostname = os.getenv("HOSTNAME")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

this_file_dir = Path(__file__).resolve().parent
project_root = this_file_dir.parents[1]
print(project_root)
local_path = project_root / "resources" / "test.log"

remote_path = "/root/test.log"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username=username, password=password)

sftp = ssh.open_sftp()
sftp.put(str(local_path), remote_path)

sftp.close()
ssh.close()

print("✅ File is copied file_copy CentOS via SFTP!")
