import requests
from unittest.mock import patch

EXCHANGE_API_URL = "https://api.apilayer.com/exchangerates_data/convert"

def get_conversion(amount):
    url = "https://api.apilayer.com/exchangerates_data/convert"
    params: dict = {"from": "EUR", "to": "RUB", "amount": amount}
    response = requests.get(url, params=params)
    return response.json()


@patch("requests.get")
def test_conversion(mock_get):
    mock_get.return_value.json.return_value = {"amount": 884.79}
    assert get_conversion(10) == {"amount": 884.79}
    mock_get.assert_called_once_with(EXCHANGE_API_URL, params={"from": "EUR", "to": "RUB", "amount": 10})