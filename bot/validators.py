from bot.exceptions import ValidationError

VALID_SIDES = {"BUY", "SELL"}
VALID_ORDER_TYPES = {"MARKET", "LIMIT"}


def validate_symbol(symbol: str):
    symbol = symbol.upper().strip()

    if not symbol:
        raise ValidationError("Symbol cannot be empty.")

    return symbol


def validate_side(side: str):
    side = side.upper().strip()

    if side not in VALID_SIDES:
        raise ValidationError("Side must be BUY or SELL.")

    return side


def validate_order_type(order_type: str):
    order_type = order_type.upper().strip()

    if order_type not in VALID_ORDER_TYPES:
        raise ValidationError("Order type must be MARKET or LIMIT.")

    return order_type


def validate_quantity(quantity):
    try:
        quantity = float(quantity)
    except ValueError:
        raise ValidationError("Quantity must be a number.")

    if quantity <= 0:
        raise ValidationError("Quantity must be greater than zero.")

    return quantity


def validate_price(price):
    try:
        price = float(price)
    except ValueError:
        raise ValidationError("Price must be a number.")

    if price <= 0:
        raise ValidationError("Price must be greater than zero.")

    return price