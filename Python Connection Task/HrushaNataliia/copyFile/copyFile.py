import paramiko
from scp import SCPClient
import os
from dotenv import load_dotenv

load_dotenv()

hostname = os.getenv("HOSTNAME")
username = os.getenv("USERNAME1")
password = os.getenv("PASSWORD")
port = int(os.getenv("PORT2"))
remote_dir = os.getenv("REMOTE_DIR")
local_file = os.getenv("LOCAL_FILE")
remote_file = os.path.join(remote_dir, "picture.png") if remote_dir else "picture.png"

def transfer_file_to_remote():
    try:
        with paramiko.SSHClient() as ssh:
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(
                hostname=hostname,
                port=port,
                username=username,
                password=password,
                timeout=10
            )

            with SCPClient(ssh.get_transport()) as scp:
                scp.put(local_file, remote_file)
                print("File copied successfully!")

    except paramiko.AuthenticationException:
        raise Exception("Authentication failed: check username/password")
    except paramiko.SSHException as e:
        raise Exception(f"SSH error: {str(e)}")
    except Exception as e:
        raise Exception(f"Error: {str(e)}")

if __name__ == "__main__":
    transfer_file_to_remote()
