import paramiko
import os
from dotenv import load_dotenv

load_dotenv()

hostname = os.getenv("HOSTNAME")
username = os.getenv("USERNAME1")
password = os.getenv("PASSWORD")
mail_file = os.getenv("MAIL_FILE")


def clear_mailbox():
    try:
        with paramiko.SSHClient() as ssh:
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname, username=username, password=password)

            ssh.exec_command(f"> {mail_file}")
            ssh.exec_command("sync")

            stdin, stdout, stderr = ssh.exec_command(f"cat {mail_file} | wc -l")
            line_count = stdout.read().decode().strip()

            if line_count == '0':
                print("Mailbox cleared successfully")
            else:
                print(f"Warning: Mailbox might not be empty (found {line_count} lines)")

    except paramiko.AuthenticationException:
        raise (f"Authentication failed - please check username/password")
    except paramiko.SSHException as e:
        raise (f"SSH connection failed: {str(e)}")
    except Exception as e:
        raise (f"Unexpected error: {str(e)}")


if __name__ == "__main__":
    clear_mailbox()
