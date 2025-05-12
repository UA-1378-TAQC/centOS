import paramiko
from pathlib import Path
import os
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

hostname = os.getenv("HOSTNAME")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

base_dir = Path(__file__).resolve().parents[2]
remote_path = "/root/test.log"

local_path = base_dir / "downloaded" / "test.log"

local_path.parent.mkdir(parents=True, exist_ok=True)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username=username, password=password)

sftp = ssh.open_sftp()
sftp.get(remote_path, str(local_path))
sftp.close()
ssh.close()

print("✅ File downloaded from CentOS via SFTP!")
