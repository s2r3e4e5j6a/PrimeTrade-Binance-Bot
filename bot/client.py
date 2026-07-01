from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException

from bot.config import API_KEY, API_SECRET, BASE_URL
from bot.logger import logger


class BinanceClient:
    def __init__(self):
        try:
            logger.info("Initializing Binance Client...")

            self.client = Client(API_KEY, API_SECRET)

            # Point the client to Binance Demo Futures
            self.client.FUTURES_URL = BASE_URL

            logger.info("Binance Client initialized successfully.")

        except Exception as e:
            logger.exception("Failed to initialize Binance Client.")
            raise e

    def test_connection(self):
        """
        Test whether the API credentials are valid.
        """
        try:
            logger.info("Testing Binance API connection...")

            account = self.client.futures_account()

            logger.info("Connection successful.")

            return {
                "success": True,
                "message": "Connected successfully!",
                "account_alias": account.get("accountAlias", "N/A")
            }

        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e}")
            return {
                "success": False,
                "message": str(e)
            }

        except BinanceRequestException as e:
            logger.error(f"Network Error: {e}")
            return {
                "success": False,
                "message": str(e)
            }

        except Exception as e:
            logger.exception("Unexpected Error")
            return {
                "success": False,
                "message": str(e)
            }