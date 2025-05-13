import paramiko
from scp import SCPClient
import os
from dotenv import load_dotenv

load_dotenv()

hostname = os.getenv("HOSTNAME")
username = os.getenv("USERNAME1")  
password = os.getenv("PASSWORD")
port = os.getenv("PORT2")
remote_dir = os.getenv("REMOTE_DIR")
local_file = os.getenv("LOCAL_FILE")
remote_file = os.path.join(remote_dir, "picture.png") if remote_dir else "picture.png"

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, port=port, username=username, password=password, timeout=10)
    
    with SCPClient(ssh.get_transport()) as scp:
        scp.put(local_file, remote_file)
    
    print(f"File copied to CentOS: {remote_file}")

except paramiko.AuthenticationException:
    print("Authentication failed: check username/password")
except paramiko.SSHException as e:
    print(f"SSH error: {str(e)}")
except Exception as e:
    print(f"Error: {str(e)}")
finally:
    if 'ssh' in locals():
        ssh.close()
