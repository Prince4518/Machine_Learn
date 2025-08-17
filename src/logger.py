import logging
import os
from datetime import datetime

# 1. Create logs folder if not exists
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# 2. Log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_H%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# 3. Logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


