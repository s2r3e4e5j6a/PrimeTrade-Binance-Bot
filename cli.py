from colorama import init, Fore, Style

from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

from bot.orders import OrderManager
from bot.exceptions import ValidationError, OrderPlacementError

init(autoreset=True)


def print_header():
    print("=" * 65)
    print("          PrimeTrade Binance Futures Trading Bot")
    print("=" * 65)


def print_summary(symbol, side, order_type, quantity, price):
    print("\nORDER REQUEST")
    print("-" * 65)
    print(f"Symbol      : {symbol}")
    print(f"Side        : {side}")
    print(f"Order Type  : {order_type}")
    print(f"Quantity    : {quantity}")

    if price:
        print(f"Price       : {price}")

    print("-" * 65)


def print_response(response):
    print("\nORDER RESPONSE")
    print("-" * 65)

    print(f"Order ID      : {response.get('orderId')}")
    print(f"Status        : {response.get('status')}")
    print(f"Executed Qty  : {response.get('executedQty')}")
    print(f"Average Price : {response.get('avgPrice')}")

    print("-" * 65)


print_header()

try:

    symbol = validate_symbol(input("Enter Symbol (e.g. BTCUSDT): "))
    side = validate_side(input("Enter Side (BUY/SELL): "))
    order_type = validate_order_type(input("Enter Order Type (MARKET/LIMIT): "))
    quantity = validate_quantity(input("Enter Quantity: "))

    price = None

    if order_type == "LIMIT":
        price = validate_price(input("Enter Price: "))

    print_summary(
        symbol,
        side,
        order_type,
        quantity,
        price
    )

    manager = OrderManager()

    response = manager.place_order(
        symbol=symbol,
        side=side,
        order_type=order_type,
        quantity=quantity,
        price=price
    )

    print()

    print(Fore.GREEN + Style.BRIGHT + "✓ ORDER PLACED SUCCESSFULLY")

    print_response(response)

except ValidationError as e:

    print(Fore.RED + f"\nValidation Error: {e}")

except OrderPlacementError as e:

    print(Fore.RED + f"\nOrder Placement Failed: {e}")

except Exception as e:

    print(Fore.RED + f"\nUnexpected Error: {e}")