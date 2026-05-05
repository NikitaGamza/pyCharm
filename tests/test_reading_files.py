import os

import numpy as np
import pandas as pd
from unittest.mock import Mock, patch
import pytest

from src.reading_files import read_csv_file, read_excel_file

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
PATH_TO_FILE = os.path.join(ROOT_DIR, "data", "transactions_excel.xlsx")
PATH_TO_FILE_FAKE_CSV = os.path.join(ROOT_DIR, "data", "fake_csv.csv")

@patch("src.reading_files.pd.read_excel")
def test_read_excel_file(mock_read_excel: Mock) -> None:
    # Создаем пример данных, которые будет возвращать мок
    mock_df = pd.DataFrame(
        [
            {
                "Дата операции": "19.05.2019 14:51:40",
                "Дата платежа": "21.05.2019",
                "Номер карты": "*7197",
                "Статус": "OK",
                "Сумма операции": -34.0,
                "Валюта операции": "RUB",
                "Сумма платежа": -34.0,
                "Валюта платежа": "RUB",
                "Кэшбэк": None,
                "Категория": "Супермаркеты",
                "MCC": 5462.0,
                "Описание": "Rumyanyj Khleb Km",
                "Бонусы(включая кэшбэк)": 0,
                "Округление на инвесткопилку": 0,
                "Сумма операции с округлением": 34.0,
            },
            {
                "Дата операции": "19.05.201914: 50:13",
                "Дата платежа": "21.05.2019",
                "Номер карты": " * 7197",
                "Статус": "OK",
                "Сумма операции": -127.0,
                "Валюта операции": "RUB",
                "Сумма платежа": -127.0,
                "Валюта платежа": "RUB",
                "Кэшбэк": None,
                "Категория": "Супермаркеты",
                "MCC": 5499.0,
                "Описание": "Колхоз",
                "Бонусы(включая кэшбэк)": 2,
                "Округление на инвесткопилку": 0,
                "Сумма операции с округлением": 127.0,
            },
            {
                "Дата операции": "19.05.201914: 31:50",
                "Дата платежа": "20.05.2019",
                "Номер карты": " * 7197",
                "Статус": "OK",
                "Сумма операции": -90.0,
                "Валюта операции": "RUB",
                "Сумма платежа": -90.0,
                "Валюта платежа": "RUB",
                "Кэшбэк": None,
                "Категория": "Фастфуд",
                "MCC": 5814.0,
                "Описание": "IP Yakubovskaya M.V.",
                "Бонусы(включая кэшбэк)": 1,
                "Округление на инвесткопилку": 0,
                "Сумма операции с округлением": 90.0,
            },
        ]
    )
    mock_df = mock_df.where(pd.notnull(mock_df), None)
    mock_read_excel.return_value = mock_df

    # Вызываем функцию и проверяем результат
    expected_result = mock_df.to_dict(orient="records")

    # Проверяем каждую запись
    for record in expected_result:
        for key, value in record.items():
            if isinstance(value, float) and np.isnan(value):
                record[key] = None

    result = read_excel_file("fake_path.xlsx")

    # Проверяем каждую запись в результате
    for record in result:
        for key, value in record.items():
            if isinstance(value, float) and np.isnan(value):
                record[key] = None

    assert result == expected_result


@patch("src.reading_files.pd.read_excel")
def test_read_excel_file_raises_value_error(mock_read_excel: Mock) -> None:
    mock_read_excel.side_effect = FileNotFoundError("Ошибка при чтении файла Excel")
    with pytest.raises(FileNotFoundError, match="Ошибка при чтении файла Excel"):
        read_excel_file("non_existent_file.xlsx")


@patch('pandas.read_csv')
def test_read_csv_file(mock_read_csv: Mock) -> None:
    test_data: dict = {
       'id': [650703.0],
       'state': ['EXECUTED'],
       'date': ['2023-09-05T11:30:32Z'],
       'amount': [16210.0],
       'currency_name': ['Sol'],
       'currency_code': ['PEN'],
       'from': ['Счет 58803664561298323391'],
       'to': ['Счет 39745660563456619397'],
       'description': ['Перевод организации']
    }

    # Создаем DataFrame из test_data
    mock_read_csv.return_value = pd.DataFrame(test_data)

    # Ожидаемый результат
    expected_result = [
        {
            'id': 650703.0,
            'state': 'EXECUTED',
            'date': '2023-09-05T11:30:32Z',
            'amount': 16210.0,
            'currency_name': 'Sol',
            'currency_code': 'PEN',
            'from': 'Счет 58803664561298323391',
            'to': 'Счет 39745660563456619397',
            'description': 'Перевод организации'
        }
    ]

    # Вызываем функцию и проверяем результат
    result = read_csv_file('fake_path.csv')
    assert result == expected_result