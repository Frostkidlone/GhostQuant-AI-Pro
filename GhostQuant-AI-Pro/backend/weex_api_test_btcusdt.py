import os
import time
import hmac
import hashlib
import base64
import json
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEEX_API_KEY")
SECRET_KEY = os.getenv("WEEX_SECRET_KEY")
PASSPHRASE = os.getenv("WEEX_PASSPHRASE")

if not all([API_KEY, SECRET_KEY, PASSPHRASE]):
    raise Exception("Missing WEEX API credentials in .env")

BASE_URL = "https://api.weex.com"

def sign(timestamp, method, path, body=""):
    message = f"{timestamp}{method}{path}{body}"
    mac = hmac.new(
        SECRET_KEY.encode(),
        message.encode(),
        hashlib.sha256
    )
    return base64.b64encode(mac.digest()).decode()

def headers(method, path, body=""):
    ts = str(int(time.time() * 1000))
    return {
        "Content-Type": "application/json",
        "ACCESS-KEY": API_KEY,
        "ACCESS-SIGN": sign(ts, method, path, body),
        "ACCESS-TIMESTAMP": ts,
        "ACCESS-PASSPHRASE": PASSPHRASE
    }

def get_btc_price():
    path = "/api/v1/market/ticker?symbol=BTCUSDT"
    url = BASE_URL + path
    r = requests.get(url)
    r.raise_for_status()
    data = r.json()
    return float(data["data"]["last"])

def place_order():
    price = get_btc_price()
    qty = round(10 / price, 6)  # 10 USDT notional

    path = "/api/v1/order/place"
    body = {
        "symbol": "BTCUSDT",
        "side": "buy",
        "type": "market",
        "quantity": qty,
        "leverage": 1
    }

    body_json = json.dumps(body)
    url = BASE_URL + path

    r = requests.post(
        url,
        headers=headers("POST", path, body_json),
        data=body_json
    )

    print("ORDER RESPONSE:")
    print(r.status_code)
    print(r.text)

if __name__ == "__main__":
    print("Starting WEEX BTCUSDT API test...")
    try:
        place_order()
    except Exception as e:
        print("API TEST ERROR:")
        print(str(e))
