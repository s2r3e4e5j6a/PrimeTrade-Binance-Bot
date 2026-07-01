import time
import hmac
import hashlib
import requests
from urllib.parse import urlencode

from bot.config import API_KEY, API_SECRET, BASE_URL
from bot.logger import logger


class BinanceClient:
    def __init__(self):
        self.base_url = BASE_URL.rstrip("/")
        self.api_key = API_KEY
        self.api_secret = API_SECRET

    def _headers(self):
        return {
            "X-MBX-APIKEY": self.api_key
        }

    def _sign(self, params):
        query_string = urlencode(params)

        signature = hmac.new(
            self.api_secret.encode(),
            query_string.encode(),
            hashlib.sha256
        ).hexdigest()

        return signature

    def signed_request(self, method, endpoint, params=None):

        if params is None:
            params = {}

        params["timestamp"] = int(time.time() * 1000)

        params["signature"] = self._sign(params)

        url = f"{self.base_url}{endpoint}"

        logger.info(f"{method} {url}")

        response = requests.request(
            method=method,
            url=url,
            headers=self._headers(),
            params=params,
            timeout=20
        )

        logger.info(
            f"Status Code : {response.status_code}"
        )

        logger.info(response.text)

        response.raise_for_status()

        return response.json()

    def test_connection(self):

        return self.signed_request(
            "GET",
            "/fapi/v2/account"
        )