import pytest

@pytest.fixture
def mask_account():
    return "**1234"

@pytest.fixture
def mask_card():
    return "1234 56** **** 3456"

@pytest.fixture
def date():
    return "11.03.2024"

@pytest.fixture
def mask_account_card_1():
    return "Счет **1234"

@pytest.fixture
def mask_account_card_2():
    return "Maestro 1234 56** **** 3456"

@pytest.fixture
def mask_account_card_3():
    return "MasterCard 1234 56** **** 3456"

@pytest.fixture
def is_none() -> None:
    return None

@pytest.fixture
def empty_arr():
    return []

@pytest.fixture
def state_executed():
    return [{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}]

@pytest.fixture
def state_cancelled():
    return [{"id": 414288290, "state": "CANCELLED", "date": "2019-07-03T18:35:29.512364"}]

@pytest.fixture
def date_reversed():
    return [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ]

@pytest.fixture
def date_straight():
    return [{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ]

@pytest.fixture
def filtered_currency():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                  "name": "USD",
                  "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }
    ]