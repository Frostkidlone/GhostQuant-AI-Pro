import os
import time
import hmac
import hashlib
import base64
import json
import requests
from dotenv import load_dotenv

# Load environment variables
from pathlib import Path
load_dotenv(dotenv_path=Path(__file__).parent / ".env")
API_KEY = os.getenv("WEEX_API_KEY")
SECRET_KEY = os.getenv("WEEX_SECRET_KEY")
PASSPHRASE = os.getenv("WEEX_API_PASSPHRASE")

BASE_URL = "https://api.weex.com"

if not all([API_KEY, SECRET_KEY, PASSPHRASE]):
    raise Exception("Missing API credentials in .env file")

def get_timestamp():
    return str(int(time.time() * 1000))

def sign_message(timestamp, method, request_path, body=""):
    message = timestamp + method + request_path + body
    hmac_key = base64.b64decode(SECRET_KEY)
    signature = hmac.new(hmac_key, message.encode(), hashlib.sha256)
    return base64.b64encode(signature.digest()).decode()

def get_headers(method, request_path, body=""):
    timestamp = get_timestamp()
    signature = sign_message(timestamp, method, request_path, body)

    return {
        "Content-Type": "application/json",
        "WEEX-ACCESS-KEY": API_KEY,
        "WEEX-ACCESS-SIGN": signature,
        "WEEX-ACCESS-TIMESTAMP": timestamp,
        "WEEX-ACCESS-PASSPHRASE": PASSPHRASE,
    }

def test_account_info():
    endpoint = "/api/v1/account/balance"
    url = BASE_URL + endpoint
    headers = get_headers("GET", endpoint)

    response = requests.get(url, headers=headers)
    print("STATUS:", response.status_code)
    print("RESPONSE:", response.text)

if __name__ == "__main__":
    print("Starting WEEX API test...")
    test_account_info()
