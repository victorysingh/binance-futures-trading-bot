# Binance Futures Testnet Trading Bot

Production-ready CLI application for USDT-M Futures trading with MARKET and LIMIT orders, comprehensive validation, structured logging, and optional mock mode for demonstration.

---

## Features

- MARKET & LIMIT orders (BUY/SELL)
- CLI interface using argparse with full input validation
- Structured logging (file + console)
- Direct Binance Futures REST API integration (`/fapi/v1/order`)
- HMAC-SHA256 request signing
- Layered architecture (client / orders / validators)
- Optional `--mock` mode for demonstration

---

## Quick Start

### Install Dependencies

```bash
pip install -r requirements.txt
