from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

app = FastAPI(title="GhostQuant AI Pro")

# --------------------
# GLOBAL STATE (SIMULATION)
# --------------------
STARTING_BALANCE = 1.0  # 1 ETH
balance = STARTING_BALANCE
positions = []
trade_log = []

# --------------------
# MODELS
# --------------------
class TradeRequest(BaseModel):
    strategy: str
    symbol: str = "ETH"
    side: str  # buy or sell
    price: float
    quantity: float

class TradeResult(BaseModel):
    strategy: str
    symbol: str
    side: str
    price: float
    quantity: float
    pnl: float
    timestamp: str

# --------------------
# STRATEGIES
# --------------------
def mean_reversion(price):
    return price < 2400

def momentum(price):
    return price > 2450

def scalping(price):
    return 2420 <= price <= 2440

# --------------------
# CORE LOGIC
# --------------------
def execute_trade(strategy, side, price, quantity):
    global balance

    cost = price * quantity
    pnl = 0.0

    if side == "buy" and balance >= cost:
        balance -= cost
        positions.append({
            "strategy": strategy,
            "price": price,
            "quantity": quantity
        })

    elif side == "sell" and positions:
        entry = positions.pop(0)
        pnl = (price - entry["price"]) * quantity
        balance += cost + pnl

    trade = {
        "strategy": strategy,
        "symbol": "ETH",
        "side": side,
        "price": price,
        "quantity": quantity,
        "pnl": round(pnl, 6),
        "timestamp": datetime.utcnow().isoformat()
    }

    trade_log.append(trade)
    return trade

# --------------------
# API ENDPOINTS
# --------------------
@app.get("/health")
def health():
    return {"status": "running"}

@app.get("/balance")
def get_balance():
    return {"balance_eth": round(balance, 6)}

@app.get("/trades")
def get_trades():
    return trade_log

@app.post("/trade")
def place_trade(req: TradeRequest):
    trade = execute_trade(
        strategy=req.strategy,
        side=req.side,
        price=req.price,
        quantity=req.quantity
    )
    return trade
