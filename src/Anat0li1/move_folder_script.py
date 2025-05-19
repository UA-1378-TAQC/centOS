import paramiko
from dotenv import load_dotenv
import os

load_dotenv()
local_dir = os.path.join(os.path.dirname(__file__), "moveFromDirectory")
remote_dir = os.getenv('REMOTE_DIR', '/home/admin/remote_dir')

hostname = os.getenv('HOSTNAME') 
port = os.getenv('PORT', 22)
username = os.getenv('USERNAME', 'admin')
password = os.getenv('PASSWORD', 'admin')

def move_from_local_to_remote(local_dir, remote_dir, hostname=hostname, port=port, username=username, password=password):
    if not os.path.exists(local_dir):
        raise FileNotFoundError(f"Local directory {local_dir} does not exist.")

    if not os.path.exists(remote_dir):
        raise FileNotFoundError(f"Remote directory {remote_dir} does not exist.")

    if not os.path.isdir(local_dir):
        raise NotADirectoryError(f"{local_dir} is not a directory.")

    if not os.path.isdir(remote_dir):
        raise NotADirectoryError(f"{remote_dir} is not a directory.")
    
    with paramiko.Transport((hostname, port)) as transport:
        transport.connect(username=username, password=password)
        with paramiko.SFTPClient.from_transport(transport) as sftp:
            for filename in os.listdir(local_dir):
                local_path = os.path.join(local_dir, filename)
                remote_path = f"{remote_dir}/{filename}"
                if os.path.isfile(local_path):
                    sftp.put(local_path, remote_path)

    print(f"Files moved from {local_dir} to {remote_dir} successfully.")


if __name__ == "__main__":
    move_from_local_to_remote(local_dir, remote_dir)
