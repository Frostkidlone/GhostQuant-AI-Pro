
import random

class StrategyEngine:
    def decide_market_action(self):
        strategies = [
            "Trend Continuation",
            "Liquidity Sweep Reversal",
            "Mean Reversion",
            "Volatility Breakout"
        ]
        return {
            "market_regime": "simulated",
            "strategy": random.choice(strategies),
            "confidence": round(random.uniform(0.6, 0.9), 2),
            "action": random.choice(["BUY", "SELL", "NO_TRADE"])
        }
