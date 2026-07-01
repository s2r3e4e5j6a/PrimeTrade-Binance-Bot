from bot.client import BinanceClient
from bot.logger import logger
from bot.exceptions import OrderPlacementError


class OrderManager:

    def __init__(self):
        self.client = BinanceClient()

    def place_order(
        self,
        symbol,
        side,
        order_type,
        quantity,
        price=None
    ):

        try:

            params = {
                "symbol": symbol.upper(),
                "side": side.upper(),
                "type": order_type.upper(),
                "quantity": quantity,
            }

            if order_type.upper() == "LIMIT":
                params["price"] = price
                params["timeInForce"] = "GTC"

            logger.info(f"Sending Order: {params}")

            response = self.client.signed_request(
                method="POST",
                endpoint="/fapi/v1/order",
                params=params
            )

            logger.info(f"Response: {response}")

            return {
                "orderId": response.get("orderId"),
                "status": response.get("status"),
                "executedQty": response.get("executedQty"),
                "avgPrice": response.get("avgPrice"),
                "symbol": response.get("symbol"),
                "side": response.get("side"),
                "type": response.get("type"),
            }

        except Exception as e:
            logger.exception("Order placement failed")
            raise OrderPlacementError(str(e))