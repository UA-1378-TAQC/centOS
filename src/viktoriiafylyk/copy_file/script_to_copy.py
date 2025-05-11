import paramiko
from dotenv import load_dotenv
import os

load_dotenv()

host = os.getenv('SSH_HOST')  
port = 22
username = os.getenv('SSH_USER')  
password = os.getenv('SSH_PASS')     
local_path = 'CentOS_Commands.txt'
remote_path = '/home/viktoriiafylyk/course_files/CentOS_Commands.txt'  

# Підключення та передача файлу
try:
    transport = paramiko.Transport((host, port))
    transport.connect(username=username, password=password)

    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put(local_path, remote_path)
    sftp.close()
    transport.close()
    print("Файл успішно передано.")
except Exception as e:
    print(f"Помилка при передачі файлу: {e}")
