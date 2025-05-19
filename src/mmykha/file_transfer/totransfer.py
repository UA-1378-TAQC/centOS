import os
import paramiko
from scp import SCPClient
from file_config import PORT_SSH, USERNAME_2, IP, PASSWORD

def connect_to_VM(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client


if __name__ == "__main__":
    local_dir = input("Input the path to local directory with files to be transfer:").strip()
    remote_dir = input("Input the path to remote directory where the files should transfer").strip()
    try:
        ssh = connect_to_VM(IP, PORT_SSH, USERNAME_2, PASSWORD)
        with SCPClient(ssh.get_transport()) as scp:
            scp.put(local_dir, recursive=True, remote_path=remote_dir)

        print("The transfer of files is successful.")
    except Exception as e:
        print(f"Exception: {e}")
    finally:
        if ssh:
            ssh.close()
            print("SSH connection is closed")
