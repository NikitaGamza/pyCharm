import requests
import os
from dotenv import load_dotenv
from typing import Dict, Optional

load_dotenv()

API_KEY = os.getenv("API_KEY")
EXCHANGE_API_URL = "https://api.apilayer.com/exchangerates_data/convert"


def conversion_amount(amount:float, base_currency: str, target_currency: str = "RUB") -> Optional[float]:
    """
    Функция, которая принимает на вход транзакцию
    и возвращает сумму транзакции (amount) в рублях, тип данных — float.
    """

    url = "https://api.apilayer.com/exchangerates_data/convert"
    params = {"from": base_currency, "to": target_currency, "amount": amount}
    payload = {}
    headers = {
        "apikey": API_KEY
    }

    try:
        response = requests.request("GET", url, headers=headers, data=payload, params=params)
        print(f"Ответ от API: {response.text}")
        if response.status_code == 200:
            data = response.json()
            return round(float(data["result"]),2)
    except requests.RequestException:
        return None
    except KeyError:
        return None
    except ValueError:
        return None
    return None

transaction_rub = {"operationAmount": {"amount": "1000", "currency": {"code": "RUB"}}}
transaction_usd = {"operationAmount": {"amount": "50", "currency": {"code": "USD"}}}
transaction_eur = {"operationAmount": {"amount": "30", "currency": {"code": "EUR"}}}

print(conversion_amount(float(transaction_rub["operationAmount"]["amount"]), transaction_rub["operationAmount"]["currency"]["code"].upper()), "RUB")  # 1000.0
print(conversion_amount(float(transaction_usd["operationAmount"]["amount"]), transaction_usd["operationAmount"]["currency"]["code"].upper()), "RUB")  # 1000.0
print(conversion_amount(float(transaction_eur["operationAmount"]["amount"]), transaction_eur["operationAmount"]["currency"]["code"].upper()), "RUB")


# url = "https://api.apilayer.com/exchangerates_data/convert"
# params = {"from": "EUR", "to": "RUB", "amount": 5}
# payload = {}
# headers= {
#   "apikey": API_KEY
# }
#
# response = requests.request("GET", url, headers=headers, data = payload, params=params)
# print(requests.request("GET", url, headers=headers, data = payload))
# status_code = response.status_code
# result = response.text
# print(result)