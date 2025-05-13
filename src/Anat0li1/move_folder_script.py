import paramiko
import os

local_dir = r'C:\Users\Admin\Desktop\MyDocs\SSA Internship\python\moveFromDirectory'
remote_dir = '/home/admin/moveToDirectory'  

hostname = '127.0.0.1' 
port = 2222
username = 'admin'
password = 'rootPass123!'


transport = paramiko.Transport((hostname, port))
transport.connect(username=username, password=password)

sftp = paramiko.SFTPClient.from_transport(transport)

for filename in os.listdir(local_dir):
    local_path = os.path.join(local_dir, filename) 
    remote_path = f"{remote_dir}/{filename}"      
    if os.path.isfile(local_path):                
        sftp.put(local_path, remote_path)          

sftp.close()
transport.close()
