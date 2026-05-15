import requests
# from unittest.mock import patch
from src.external_api import conversion_amount
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
EXCHANGE_API_URL = "https://api.apilayer.com/exchangerates_data/convert"

def get_conversion(amount):
    url = "https://api.apilayer.com/exchangerates_data/convert"
    params: dict = {"from": "EUR", "to": "RUB", "amount": amount}
    payload: dict = {}
    headers = {"apikey": API_KEY}
    response = requests.get(url, headers=headers, data=payload, params=params)
    data = response.json()
    return round(float(data["result"]), 2)


# @patch("requests.get")
def test_conversion():
    transaction_eur = {"operationAmount": {"amount": "10", "currency": {"code": "EUR"}}}

    assert get_conversion(10) == conversion_amount(float(
        transaction_eur["operationAmount"]["amount"]),
        transaction_eur["operationAmount"]["currency"]["code"].upper())