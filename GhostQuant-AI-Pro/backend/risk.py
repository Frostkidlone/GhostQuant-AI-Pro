
class RiskManager:
    def approve(self, decision):
        if decision["confidence"] < 0.65:
            return False
        return decision["action"] != "NO_TRADE"
