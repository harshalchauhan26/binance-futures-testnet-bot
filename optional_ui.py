import streamlit as st
from main_bot.orders import place_market_order, place_limit_order
from main_bot.validators import validate_order
from main_bot.logs import logger ,last_log
st.title("Binance Futures Testnet Trading Bot")

symbol = st.text_input("Symbol", "BTCUSDT")
side = st.selectbox("Side", ["BUY", "SELL"])
order_type = st.selectbox("Order Type", ["MARKET", "LIMIT"])
quantity = st.number_input("Quantity", min_value=0.0)

price = None
if order_type == "LIMIT":
    price = st.number_input("Price", min_value=0.0)

if st.button("Place Order"):
    try:
        validate_order(symbol, side, order_type, quantity, price)

        if order_type == "MARKET":
            response = place_market_order(symbol, side, quantity)
        else:
            response = place_limit_order(symbol, side, quantity, price)

        logger.info(
    f"Order executed | Symbol: {symbol} | Side: {side} | Type: {order_type} | Qty: {quantity} "
)
        last_log=last_log()

        st.success("Order placed successfully!")
        st.write(last_log)

    except Exception as e:
        logger.error(str(e))
        st.error(str(e))