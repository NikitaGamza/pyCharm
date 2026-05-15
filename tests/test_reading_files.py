import os
from unittest.mock import patch
from src.reading_files import read_csv_file

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
PATH_TO_FILE = os.path.join(ROOT_DIR, "data", "fake_xlsx.xlsx")
PATH_TO_FILE_CSV = os.path.join(ROOT_DIR, "data", "fake_csv.csv")
PATH_TO_NO_FILE = os.path.join(ROOT_DIR, "data", "no_file.csv")


@patch('pandas.read_excel')
def test_valid_read_excel(mock_read_excel):
    result = read_csv_file(PATH_TO_FILE_CSV)
    result_no_file = read_csv_file(PATH_TO_NO_FILE)
    result_no_file_xlsx = read_csv_file(PATH_TO_NO_FILE)
    expected_result = [{
        "id": "650703",
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": "16210",
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации"
    }]
    assert "File not found" == result_no_file_xlsx
    assert "File not found" == result_no_file
    assert result == expected_result