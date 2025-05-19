from dotenv import load_dotenv
import os

load_dotenv()

SERVER = os.getenv("CENTOS_IP") 
IMAP_PORT = os.getenv("CENTOS_IMAP_PORT") 
USERNAME = os.getenv("CENTOS_USER") 
PASSWORD = os.getenv("CENTOS_USER_PASSW") 
MAILBOX = os.getenv("MAILBOX") 
RECEIVER = os.getenv("RECEIVER") 
SENDER = os.getenv("SENDER") 
SMTP_PORT = os.getenv("CENTOS_SMTP_PORT") 