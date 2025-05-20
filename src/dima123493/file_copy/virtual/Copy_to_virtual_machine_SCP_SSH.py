import os
from pathlib import Path
from scp import SCPClient
from src.dima123493.utils.env_loader import load_env_vars
from src.dima123493.utils.ssh_utils import ssh_connection

load_env_vars()

def copy_log_to_centos():
    hostname = os.getenv("HOSTNAME")
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    this_file_dir = Path(__file__).resolve().parent
    project_root = this_file_dir.parents[1]
    print(project_root)
    local_path = project_root / "resources" / "test.log"
    remote_path = "/root/test.log"

    with ssh_connection(hostname, username, password) as ssh:
        with SCPClient(ssh.get_transport()) as scp:
            scp.put(str(local_path), remote_path)

    print("✅ File is copied to CentOS via SCP!")

if __name__ == "__main__":
    copy_log_to_centos()
