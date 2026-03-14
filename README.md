# Binance Futures Testnet Trading Bot

## 🌐 Overview

This project implements a simplified trading bot that can place **MARKET** and **LIMIT** orders on the **Binance Futures Testnet (USDT-M)**.
The application is built with a modular Python architecture and provides both a **Command Line Interface (CLI)** and a **Streamlit-based web UI**.

The project demonstrates:

* Integration with the Binance Futures Testnet API
* Structured and reusable Python code
* Input validation and error handling
* Logging of API requests and responses
* CLI interaction for order execution
* Lightweight Streamlit UI for easier interaction

---

## 1. Features

* Place **MARKET orders**
* Place **LIMIT orders**
* Support for **BUY** and **SELL**
* Binance Futures Testnet integration
* Input validation for order parameters
* Logging system for API requests and responses
* CLI interface for direct terminal usage
* Streamlit UI for a simple web-based trading interface

---

## 2. Project Structure

```text
Trading_bot
│
├── main_bot
│   ├── __init__.py
│   ├── client.py          # Binance API client configuration
│   ├── orders.py          # Order placement logic
│   ├── validators.py      # Input validation
│   └── logs.py            # Logging configuration
│
├── main.py                # CLI entry point
├── optional_ui.py         # Streamlit UI
├── requirements.txt       # Python dependencies
├── README.md
├── .gitignore
└── .env.example           # API key template
```

---

## 3. Installation

### 3.1 Clone the Repository

```bash
git clone https://github.com/harshalchauhan26/binance-futures-testnet-bot.git
cd binance-futures-testnet-bot
```

---

### 3.2 Create Virtual Environment

```bash
python -m venv venv
```

Activate it.

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

---

### 3.3 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Binance Testnet API Setup

Create a `.env` file in the root directory.

Example:

```text
API_KEY=your_testnet_api_key
API_SECRET=your_testnet_secret_key
```

Create a Binance Futures Testnet account here:

https://testnet.binancefuture.com

---

## 5. Running the Application

### 5.1 CLI Mode

Run the trading bot through the terminal.

```bash
python main.py
```

You will be prompted to enter:

1. Symbol
2. Side (BUY or SELL)
3. Order Type (MARKET or LIMIT)
4. Quantity
5. Price (only required for LIMIT orders)

---

### 5.2 Streamlit UI

Run the web interface:

```bash
streamlit run optional_ui.py
```

Open the application in your browser (usually):

```text
http://localhost:8501
```

---

## 6. Logging

All order requests, responses, and errors are recorded in:

```text
bot.log
```

Example log entry:

```text
2026-03-14 21:29:26 -- INFO -- Order executed | Symbol: BTCUSDT | Side: BUY | Type: MARKET | Qty: 0.001
```

Logging helps monitor bot activity and debug issues.

---

## 7. Validation and Error Handling

The application validates:

* Order type (`MARKET`, `LIMIT`)
* Trade side (`BUY`, `SELL`)
* Quantity must be greater than zero
* LIMIT orders require a price

Invalid inputs are caught before sending API requests.

---

## 8. Dependencies

Main Python libraries used:

* python-binance
* python-dotenv
* streamlit

Install them with:

```bash
pip install -r requirements.txt
```

---

## 9. Author

Harshal Chauhan

GitHub:
https://github.com/harshalchauhan26
