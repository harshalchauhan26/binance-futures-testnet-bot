**Binance Futures Testnet Trading Bot
**
Live Demo: 

A lightweight Python trading bot that places MARKET and LIMIT orders on the Binance Futures Testnet.
The project includes a CLI interface, Streamlit UI, proper logging, and input validation.

Features**
**
Place MARKET orders

Place LIMIT orders

Supports BUY and SELL

Binance Futures Testnet integration

Input validation

Logging of requests, responses, and errors

Streamlit UI for easy interaction

Modular project structure

**Project Structure**
Trading_bot
│
├── main_bot
│   ├── client.py          # Binance API client setup
│   ├── orders.py          # Order execution logic
│   ├── validators.py      # Input validation
│   ├── logs.py            # Logging configuration
│
├── main.py                # CLI entry point
├── ui.py                  # Streamlit UI
├── requirements.txt       # Project dependencies
├── bot.log                # Log file generated during execution
├── .env                   # API keys (not committed)
└── README.md


**Setup Instructions**
1. Clone the repository
git clone <your_repo_url>
cd Trading_bot
2. Create Virtual Environment
python -m venv venv

Activate it:

Windows
venv\Scripts\activate

Mac/Linux
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Setup Binance Testnet API Keys

Create a .env file in the root directory:

API_KEY=your_binance_testnet_api_key
API_SECRET=your_binance_testnet_secret

Testnet registration:
https://testnet.binancefuture.com

**Running the Application
**
CLI Mode
Run the bot from terminal:
python main.py

Follow the prompts to place an order.


**Streamlit UI
**
Run the web interface:

streamlit run ui.py

Open the URL shown in the terminal (usually):

http://localhost:8501

Use the UI to place MARKET or LIMIT orders.

Logging

All requests, responses, and errors are logged in:

bot.log

Example log entry:

2026-03-14 21:29:26 -- INFO -- Order executed | Symbol: BTCUSDT | Side: BUY | Type: MARKET | Qty: 0.001
Bonus Features Implemented

Interactive Streamlit UI

Enhanced user interaction

Structured modular architecture

Logging of order requests and responses

Assumptions

Binance Futures Testnet account is used.

API keys have futures trading permission enabled.

Dependencies

python-binance

python-dotenv

streamlit

Author

Harshal Chauhan
