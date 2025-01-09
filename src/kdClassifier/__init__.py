import os
import sys
import logging

logging_str = "[ %(asctime)s: %(levelname)s: %(module)s: %(message)s ]"

log_dirs = "Logs"
log_filepath = os.path.join(log_dirs, 'runningLogs.log')
os.makedirs(log_dirs, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger('kdClassifierlogger')