import os
from unittest.mock import patch, Mock

import pandas as pd
from pandas import read_excel

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
PATH_TO_FILE = os.path.join(ROOT_DIR, "data", "fake_xlsx.xlsx")

@patch('pandas.read_excel')
def test_valid_read_excel(mock_read_excel):
    # Создаем фейковый DataFrame.
    mock_df = pd.DataFrame([{
        "id": "1",
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": "16210",
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации"
    }])

    # Настраиваем mock, чтобы он возвращал фейковый DataFrame.
    mock_read_excel.return_value = mock_df

    pd_file = pd.read_excel(PATH_TO_FILE)
    result = pd_file.fillna("").to_dict(orient="records")
    expected_result = [{
        "id": "1",
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": "16210",
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации"
    }]

    assert result == expected_result