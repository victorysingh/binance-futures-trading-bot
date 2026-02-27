import requests
import hmac
import hashlib
import time
from urllib.parse import urlencode
import os
from dotenv import load_dotenv
import bot.logging_config as logging
logger = logging.logger

load_dotenv()

BASE_URL = "https://testnet.binancefuture.com"

class BinanceFuturesClient:
    def __init__(self):
        self.api_key = os.getenv('BINANCE_API_KEY')
        self.api_secret = os.getenv('BINANCE_SECRET_KEY')
        if not self.api_key or not self.api_secret:
            raise ValueError("Set BINANCE_API_KEY and BINANCE_SECRET_KEY in .env")
        logger.info("Binance Futures Testnet client initialized (REST)")

    def _sign(self, params):
        query = urlencode(sorted(params.items()))
        signature = hmac.new(
            self.api_secret.encode(), 
            query.encode(), 
            hashlib.sha256
        ).hexdigest()
        return signature
    
    def place_order(self, symbol: str, side: str, order_type: str, quantity: float, price: float = None):
        try:
            logger.info(f"Placing {order_type} {side} order: {symbol}, qty={quantity}, price={price}")
            
            timestamp = int(time.time() * 1000)
            params = {
                'symbol': symbol,
                'side': side.upper(),
                'type': order_type.upper(),
                'quantity': quantity,
                'timestamp': timestamp
            }
            
            if order_type.upper() == 'LIMIT' and price:
                params['price'] = price
                params['timeInForce'] = 'GTC'
            
            params['signature'] = self._sign(params)
            
            headers = {'X-MBX-APIKEY': self.api_key}
            
            response = requests.post(
                f"{BASE_URL}/fapi/v1/order",
                params=params,
                headers=headers
            )
            
            result = response.json()
            logger.info(f"Order response: {result}")
            return result
            
        except Exception as e:
            logger.error(f"Order failed: {e}")
            raise
