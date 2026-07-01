# PrimeTrade Binance Futures Trading Bot

## Overview

This project is a Python-based trading bot developed for the PrimeTrade.ai Python Developer Application Task.

The bot connects to the Binance Futures Demo Trading API and allows users to place BUY and SELL Market and Limit orders through a command-line interface (CLI). The application follows a modular architecture with input validation, logging, and exception handling.

---

## Features

- Place Market Orders
- Place Limit Orders
- BUY and SELL support
- Command Line Interface (CLI)
- Input Validation
- Exception Handling
- Logging of API requests and responses
- Environment variable support using `.env`
- Modular and reusable project structure

---

## Project Structure

```
PrimeTrade-Binance-Bot/
│
├── bot/
│   ├── client.py
│   ├── config.py
│   ├── exceptions.py
│   ├── logger.py
│   ├── orders.py
│   └── validators.py
│
├── logs/
├── screenshots/
├── cli.py
├── requirements.txt
├── README.md
└── .env
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/PrimeTrade-Binance-Bot.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file in the project root:

```env
BINANCE_API_KEY=YOUR_API_KEY
BINANCE_API_SECRET=YOUR_API_SECRET
BINANCE_BASE_URL=https://demo-fapi.binance.com
```

---

## Running the Bot

```bash
python cli.py
```

Example:

```
Enter Symbol: BTCUSDT
Enter Side: BUY
Enter Order Type: MARKET
Enter Quantity: 0.001
```

---

## Logging

All API requests, responses, and errors are stored in the `logs` directory.

---

## Assumptions

- Uses Binance Futures Demo Trading API.
- User has valid API credentials.
- Internet connection is available.

---

## Technologies Used

- Python 3.12
- Requests
- Colorama
- Python-dotenv

---

## Author

Sreeja Gurrala
