import logging
import os
from datetime import datetime

from config.config import LOG_DIR, LOG_FILE_FORMAT, LOG_LEVEL

def setup_logger(test_name="default_test"):
    """
    Sets up a logger that writes log messages to a file with timestamp and test name.
    """
    logger = logging.getLogger(test_name)
    logger.setLevel(getattr(logging, LOG_LEVEL.upper()))

    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    timestamp = datetime.now().strftime(LOG_FILE_FORMAT)
    safe_test_name = test_name.replace(" ", "_").replace("/", "_").replace("\\", "_")

    log_file_name = "{}_{}.log".format(timestamp, safe_test_name)
    log_file = os.path.join(LOG_DIR, log_file_name)

    handler = logging.FileHandler(log_file)
    handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

    if not logger.handlers:
        logger.addHandler(handler)

    logger.propagate = False
    return logger
