"""
Custom Exceptions for Trading Bot
"""


class TradingBotError(Exception):
    """Base exception for all trading bot errors."""
    pass


class ValidationError(TradingBotError):
    """Raised when user input is invalid."""
    pass


class BinanceConnectionError(TradingBotError):
    """Raised when connection to Binance fails."""
    pass


class OrderPlacementError(TradingBotError):
    """Raised when an order cannot be placed."""
    pass 