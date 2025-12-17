from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="GhostQuant-AI-Pro Bot")

# Dummy storage for orders and positions
positions = []
strategies = [
    {"name": "MeanReversion", "description": "Buys low, sells high"},
    {"name": "Momentum", "description": "Follows trends"},
    {"name": "Scalping", "description": "Quick trades to capture small price movements"}
]

# Pydantic models
class Order(BaseModel):
    strategy: str
    symbol: str
    side: str
    quantity: float
    price: Optional[float] = None

class Position(BaseModel):
    strategy: str
    symbol: str
    side: str
    quantity: float
    price: Optional[float] = None

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "ok", "message": "Backend is running!"}

# Get available strategies
@app.get("/strategies")
async def get_strategies():
    return {"strategies": strategies}

# Place a new order
@app.post("/order")
async def place_order(order: Order):
    positions.append(order.dict())
    return {"status": "success", "order": order.dict()}

# Get current positions
@app.get("/positions")
async def get_positions():
    return {"positions": positions}
