import os
from pathlib import Path

from src.dima123493.utils.env_loader import load_env_vars
from src.dima123493.utils.ssh_utils import ssh_connection

load_env_vars()

def download_log_from_centos_sftp():
    hostname = os.getenv("HOSTNAME")
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    base_dir = Path(__file__).resolve().parents[2]
    remote_path = "/root/test.log"
    local_path = base_dir / "downloaded" / "test.log"

    local_path.parent.mkdir(parents=True, exist_ok=True)

    with ssh_connection(hostname, username, password) as ssh:
        with ssh.open_sftp() as sftp:
            sftp.get(remote_path, str(local_path))

    print("File downloaded from CentOS via SFTP!")

if __name__ == "__main__":
    download_log_from_centos_sftp()
