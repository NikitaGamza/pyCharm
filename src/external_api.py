import requests
import os
from dotenv import load_dotenv

load_dotenv()

APY_KEY = os.getenv("APY_KEY")


def conversion_amount(transaction_data: dict) -> float:
    """фунция конфертации валюты"""
    url = "https://api.apilayer.com/exchangerates_data/convert"
    payload = {}
    headers = {"apikey": f"{APY_KEY}"}

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code != 200:
        raise ValueError(f"Не удалось получить курс валюты")
    result = response.json()["result"]
    return result