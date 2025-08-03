# utils/apps_logger.py

import logging
import os

LOG_DIR = "logs"
LOG_FILE = "apps.log"

# Create the log directory if it doesn't exist
os.makedirs(LOG_DIR, exist_ok=True)

# Full path to the log file
log_path = os.path.join(LOG_DIR, LOG_FILE)

# Configure the logging
logging.basicConfig(
    filename=log_path,
    filemode="a",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(module)s - %(message)s"
)

# Exported logger object
logger = logging.getLogger("KollywoodAppLogger")