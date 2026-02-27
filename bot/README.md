## Demo Mode


# Binance Futures Testnet Trading Bot

Production-ready CLI bot for USDT-M Futures orders with logging, validation, and mock mode.

## Features
- MARKET & LIMIT orders (BUY/SELL)
- Input validation & error handling  
- Structured logging to file
- Mock mode for testnet demo
- Real Binance Futures REST API ready

## Setup
```bash
pip install -r requirements.txt
# Add your testnet keys to .env
python cli.py --help
EXAMPLE
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001 --mock
limit Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000 --mock


