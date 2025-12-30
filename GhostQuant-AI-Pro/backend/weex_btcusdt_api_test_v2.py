import os
from dotenv import load_dotenv
import requests
import time

# FORCE LOAD .env BY ABSOLUTE PATH
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_PATH = os.path.join(BASE_DIR, ".env")

print("Loading .env from:", ENV_PATH)
load_dotenv(dotenv_path=ENV_PATH, override=True)

API_KEY = os.getenv("WEEX_API_KEY")
SECRET_KEY = os.getenv("WEEX_SECRET_KEY")
PASSPHRASE = os.getenv("WEEX_PASSPHRASE")

print("\nENV CHECK:")
print("API KEY FOUND:", bool(API_KEY))
print("SECRET FOUND:", bool(SECRET_KEY))
print("PASSPHRASE FOUND:", bool(PASSPHRASE))
print("----------------------------------------")

# HARD FAIL ONLY IF ANY ARE MISSING
if not all([API_KEY, SECRET_KEY, PASSPHRASE]):
    print("RAW VALUES DEBUG:")
    print("API_KEY =", repr(API_KEY))
    print("SECRET_KEY =", repr(SECRET_KEY))
    print("PASSPHRASE =", repr(PASSPHRASE))
    raise Exception("WEEX API credentials not loaded. .env parsing issue.")

# ---- WEEX API TEST (ORDER ATTEMPT) ----
BASE_URL = "https://api.weex.com"

def test_btcusdt_order():
    print("\nAttempting BTCUSDT order via WEEX API...")
    
    endpoint = "/api/v1/order/place"
    url = BASE_URL + endpoint

    payload = {
        "symbol": "BTCUSDT",
        "side": "BUY",
        "type": "MARKET",
        "quantity": "0.0002"  # ≈ 10 USDT notional
    }

    headers = {
        "X-API-KEY": API_KEY,
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        print("STATUS CODE:", response.status_code)
        print("RESPONSE:", response.text)
    except Exception as e:
        print("NETWORK / CONNECTION ERROR:")
        print(str(e))

if __name__ == "__main__":
    test_btcusdt_order()
