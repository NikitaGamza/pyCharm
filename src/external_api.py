import os
from typing import Optional

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
EXCHANGE_API_URL = "https://api.apilayer.com/exchangerates_data/convert"


def conversion_amount(amount: float, base_currency: str, target_currency: str = "RUB") -> Optional[float]:
    """
    Функция, которая принимает на вход транзакцию
    и возвращает сумму транзакции (amount) в рублях, тип данных — float.
    """

    url = "https://api.apilayer.com/exchangerates_data/convert"
    params: dict = {"from": base_currency, "to": target_currency, "amount": amount}
    payload: dict = {}
    headers = {"apikey": API_KEY}

    try:
        response = requests.request("GET", url, headers=headers, data=payload, params=params)
        if response.status_code == 200:
            data = response.json()
            return round(float(data["result"]), 2)
    except requests.RequestException:
        return None
    except KeyError:
        return None
    except ValueError:
        return None
    return None


transaction_eur = {"operationAmount": {"amount": "10", "currency": {"code": "EUR"}}}


# print(conversion_amount(float(
#     transaction_eur["operationAmount"]["amount"]),
#     transaction_eur["operationAmount"]["currency"]["code"].upper()))
