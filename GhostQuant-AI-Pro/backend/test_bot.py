import requests
import time

BASE_URL = "http://127.0.0.1:8000"

demo_prices = [2380, 2410, 2435, 2460, 2440]

for price in demo_prices:
    if price < 2400:
        strategy = "MeanReversion"
        side = "buy"
    elif price > 2450:
        strategy = "Momentum"
        side = "sell"
    else:
        strategy = "Scalping"
        side = "buy"

    payload = {
        "strategy": strategy,
        "side": side,
        "price": price,
        "quantity": 0.01
    }

    r = requests.post(f"{BASE_URL}/trade", json=payload)
    print(r.json())

    time.sleep(1)
