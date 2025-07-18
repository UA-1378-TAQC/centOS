from dotenv import load_dotenv
import os

load_dotenv()

PORT_SSH = os.getenv("PORT_SSH") 
USERNAME_2 = os.getenv("CENTOS_USER_2") 
IP = os.getenv("CENTOS_IP")
PASSWORD = os.getenv("PASSWORD_2")
