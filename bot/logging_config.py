import logging
import os
from datetime import datetime

log_dir = "bot/logs"
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, f"trading_bot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

print(f"Logging to: {log_file}")  # Tell user where logs are
