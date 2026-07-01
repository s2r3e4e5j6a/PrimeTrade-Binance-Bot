import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Read API credentials
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")
BASE_URL = os.getenv("BINANCE_BASE_URL")

# Validate environment variables
if not API_KEY:
    raise ValueError("BINANCE_API_KEY is missing in the .env file.")

if not API_SECRET:
    raise ValueError("BINANCE_API_SECRET is missing in the .env file.")

if not BASE_URL:
    raise ValueError("BINANCE_BASE_URL is missing in the .env file.")