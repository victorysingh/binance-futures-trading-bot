#!/usr/bin/env python3
import argparse
import os
from bot.client import BinanceFuturesClient
from bot.validators import *
from bot import logging_config
logger = logging_config.logger

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
    parser.add_argument('--symbol', required=True, help="e.g., BTCUSDT")
    parser.add_argument('--side', required=True, choices=['BUY', 'SELL'])
    parser.add_argument('--type', required=True, choices=['MARKET', 'LIMIT'])
    parser.add_argument('--quantity', required=True, type=float)
    parser.add_argument('--price', type=float, help="Required for LIMIT orders")
    parser.add_argument('--mock', action='store_true', help="Run in mock mode for demo")
    
    args = parser.parse_args()
    
    # Validate inputs
    if not validate_symbol(args.symbol):
        print("❌ Invalid symbol. Use e.g., BTCUSDT")
        return
    if not validate_side(args.side):
        print("❌ Invalid side. Use BUY or SELL")
        return
    if not validate_order_type(args.type):
        print("❌ Invalid type. Use MARKET or LIMIT")
        return
    if not validate_quantity(str(args.quantity)):
        print("❌ Invalid quantity. Must be >0")
        return
    if args.type == 'LIMIT' and (not args.price or not validate_price(str(args.price))):
        print("❌ Price required for LIMIT and must be >0")
        return
    
    print("\n📋 Order Summary:")
    print(f"Symbol: {args.symbol}")
    print(f"Side: {args.side}")
    print(f"Type: {args.type}")
    print(f"Quantity: {args.quantity}")
    if args.price:
        print(f"Price: {args.price}")
    print("-" * 40)
    
    if args.mock:
        logger.info("Running in MOCK mode for demonstration")
        response = {
            "orderId": 284957945,
            "status": "FILLED",
            "executedQty": str(args.quantity),
            "avgPrice": str(args.price or 58432.50),
            "symbol": args.symbol,
            "side": args.side
        }
        logger.info(f"MOCK order success: {response}")
    else:
        try:
            client = BinanceFuturesClient()
            response = client.place_order(args.symbol, args.side, args.type, args.quantity, args.price)
            
            if 'code' in response and response['code'] != 0:
                print(f"❌ API Error: {response.get('msg', 'Unknown error')}")
                return
        except Exception as e:
            print(f"❌ Failed: {e}")
            return
    
    print("\n✅ Order placed successfully!")
    print("Response details:")
    print(f"  Order ID: {response.get('orderId', 'N/A')}")
    print(f"  Status: {response.get('status', 'N/A')}")
    print(f"  Executed Qty: {response.get('executedQty', 'N/A')}")
    print(f"  Avg Price: {response.get('avgPrice', 'N/A')}")

if __name__ == "__main__":
    main()
