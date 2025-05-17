import paramiko
from contextlib import contextmanager

@contextmanager
def ssh_connection(hostname, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, username=username, password=password)
    try:
        yield ssh
    finally:
        ssh.close()
