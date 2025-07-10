import os

# LOGGER SETUP

LOG_DIR = os.getenv("LOG_DIR", "resources/logs")
LOG_FILE_FORMAT = "%d-%m-%Y"
LOG_BACKUP_COUNT = 0
LOG_LEVEL = "INFO"
