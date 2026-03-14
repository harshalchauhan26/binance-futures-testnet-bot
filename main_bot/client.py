from binance.client import Client
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
API_KEY=os.getenv("API_KEY") or st.secrets.get["API_KEY"]
API_SECRET=os.getenv("API_SECRET") or st.secrets.get["API_SECRET"]

#MAIN LOGIC
def get_client():
    client=Client(API_KEY,API_SECRET)
    client.FUTURES_URL= "https://testnet.binancefuture.com"
    return client
