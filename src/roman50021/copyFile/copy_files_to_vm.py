import os
from dotenv import load_dotenv
import paramiko
from scp import SCPClient
from pathlib import Path

env_path = Path(__file__).parent / "file.env"
load_dotenv(dotenv_path=env_path, override=True)

hostname = os.getenv("SSH_HOST")
port = int(os.getenv("SSH_PORT", 22))
username = os.getenv("SSH_USERNAME")
password = os.getenv("SSH_PASSWORD")
local_dir = os.getenv("LOCAL_DIR")
remote_dir = os.getenv("REMOTE_DIR")

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=hostname, port=port, username=username, password=password)

with SCPClient(ssh.get_transport()) as scp:
    for file_name in os.listdir(local_dir):
        full_path = os.path.join(local_dir, file_name)
        if os.path.isfile(full_path):
            print(f"Копіюю {file_name} → {remote_dir}")
            scp.put(full_path, remote_path=os.path.join(remote_dir, file_name))

print("Готово!")
ssh.close()
