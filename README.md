GhostQuant AI Pro 🤖📈

GhostQuant AI Pro is an AI-assisted, algorithmic crypto trading engine designed for the WEEX AI Wars: Alpha Awakens Hackathon.
It focuses on disciplined execution, modular strategies, and controlled risk, behaving as naturally and reliably as a centralized exchange-native trading bot.

🚀 Vision

Manual trading is slow, emotional, and inconsistent.
GhostQuant AI Pro automates trading decisions using structured quantitative strategies and AI-assisted signal filtering, enabling consistent execution, reduced human bias, and scalable risk management on WEEX.

🧠 Core Features

Multi-Strategy Trading Engine

Mean Reversion

Momentum

Scalping

AI-Assisted Signal Filtering

Strategy validation

Trade condition confirmation

Strict Risk Management

Position sizing control

Exchange-compliant leverage logic

Exchange-Native Behavior

Designed to mirror real WEEX trading workflows

Modular Architecture

Easy to extend with new strategies

FastAPI Backend

Clean REST API for strategy execution and monitoring

🏗️ Architecture Overview
GhostQuant-AI-Pro/
│
├── backend/
│   ├── main.py              # FastAPI application
│   ├── strategies/          # Strategy modules
│   ├── risk/                # Risk management logic
│   ├── test_bot.py          # Backend testing script
│   └── requirements.txt
│
├── docs/                    # Project documentation
└── README.md

🔌 API Endpoints (Backend)
Endpoint	Description
/health	Health check
/strategies	List available strategies
/order	Place a simulated trade
/positions	View open positions
🧪 Local Setup & Testing
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Run backend server
uvicorn main:app --reload


Server runs at:

http://127.0.0.1:8000

3️⃣ Test trading logic
python test_bot.py


This script validates:

Backend availability

Strategy listing

Order placement

Position tracking

📊 Strategy Logic (Summary)
🔹 Mean Reversion

Identifies price deviations from historical averages and trades toward equilibrium.

🔹 Momentum

Follows strong directional price movement to capture trend continuation.

🔹 Scalping

Executes short-duration trades to capture small price inefficiencies.

Each strategy operates under risk-controlled execution rules.

⚠️ Risk Management

Controlled trade sizing

No high-risk gambling logic

Designed to comply with WEEX leverage limits

Prevents over-trading and runaway execution

🔮 AI Component

AI is used to:

Assist in filtering strategy signals

Reduce false positives

Improve execution discipline

The system is intentionally designed to prioritize stability and interpretability over black-box decision making.

🌐 WEEX Integration

Designed for WEEX OpenAPI integration

Modular API layer allows seamless transition from simulation to live trading

Prepared for IP allowlisting and API key authentication

🏆 Hackathon Alignment

This project directly aligns with:

AI Trading

Algorithmic Strategy Development

Risk Management

Web3 / Crypto Infrastructure

Built specifically for AI Wars: WEEX Alpha Awakens.

📌 Status

✅ Backend functional

✅ Strategy engine implemented

🔄 WEEX API integration pending approval

🔄 Live trading metrics to be added after API access

📜 Disclaimer

This project is for research and hackathon demonstration purposes only.
It does not constitute financial advice or a guarantee of profit.

🙌 Author

GhostQuant AI Pro
Built for WEEX AI Wars Hackathon
