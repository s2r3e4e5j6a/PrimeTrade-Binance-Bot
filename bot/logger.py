import logging
import os

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

LOG_FILE = "logs/trading_bot.log"

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(filename)s:%(lineno)d | %(message)s",    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("TradingBot")