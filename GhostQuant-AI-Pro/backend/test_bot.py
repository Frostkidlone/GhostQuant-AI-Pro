import requests

BASE_URL = "http://127.0.0.1:8000"

print("Starting backend test for GhostQuant-AI-Pro bot...\n")

# Health Check
try:
    r = requests.get(f"{BASE_URL}/health")
    print("Health Check:", r.status_code, r.json())
except Exception as e:
    print("Health Check Error:", e)

# Available Strategies
try:
    r = requests.get(f"{BASE_URL}/strategies")
    print("Available Strategies:", r.status_code, r.json())
except Exception as e:
    print("Available Strategies Error:", e)

# Place Order
order_data = {
    "strategy": "Scalping",
    "symbol": "BTCUSDT",
    "side": "buy",
    "quantity": 0.001,
    "price": None
}

try:
    r = requests.post(f"{BASE_URL}/order", json=order_data)
    print("Place Order:", r.status_code, r.json())
except Exception as e:
    print("Place Order Error:", e)

# Current Positions
try:
    r = requests.get(f"{BASE_URL}/positions")
    print("Current Positions:", r.status_code, r.json())
except Exception as e:
    print("Current Positions Error:", e)

print("\nAll tests completed.")
