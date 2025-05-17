import os
from pathlib import Path

from scp import SCPClient
from src.dima123493.utils.env_loader import load_env_vars
from src.dima123493.utils.ssh_utils import ssh_connection

def copy_log_from_centos_scp():
    load_env_vars()

    hostname = os.getenv("HOSTNAME")
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    base_dir = Path(__file__).resolve().parents[2]
    remote_path = "/root/test.log"
    local_path = base_dir / "downloaded" / "test.log"

    local_path.parent.mkdir(parents=True, exist_ok=True)

    with ssh_connection(hostname, username, password) as ssh:
        with SCPClient(ssh.get_transport()) as scp:
            scp.get(remote_path, str(local_path))

    print("✅ File is copied from CentOS to Windows machine via SCP!")

if __name__ == "__main__":
    copy_log_from_centos_scp()
