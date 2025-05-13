import paramiko
from dotenv import load_dotenv
import os

def load_ssh_config():
    load_dotenv()
    return {
        'host': os.getenv('SSH_HOST'),
        'port': int(os.getenv('SSH_PORT')),
        'username': os.getenv('SSH_USER'),
        'password': os.getenv('SSH_PASS')
    }

def transfer_file(ssh_config, local_path, remote_path):
    try:
        transport = paramiko.Transport((ssh_config['host'], ssh_config['port']))
        transport.connect(username=ssh_config['username'], password=ssh_config['password'])

        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.put(local_path, remote_path)
        sftp.close()
        transport.close()
        print("Файл успішно передано.")
    except Exception as e:
        print(f"Помилка при передачі файлу: {e}")

if __name__ == "__main__":
    ssh_config = load_ssh_config()
    local_file = 'CentOS_Commands.txt'
    remote_file = '/home/viktoriiafylyk/course_files/CentOS_Commands.txt'
    transfer_file(ssh_config, local_file, remote_file)
