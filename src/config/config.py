import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# LOGGER SETUP

LOG_DIR = os.getenv("LOG_DIR", "logs")
LOG_FILE_FORMAT = "%d-%m-%Y"
LOG_BACKUP_COUNT = 0
LOG_LEVEL = "INFO"
