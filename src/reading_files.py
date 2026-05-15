import csv
import os
from typing import Any

import pandas as pd

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
PATH_TO_FILE = os.path.join(ROOT_DIR, "data", "transactions_excel.xlsx")
PATH_TO_FILE_CSV = os.path.join(ROOT_DIR, "data", "transactions.csv")


def read_excel_file(address: str) -> Any:
    """Чтение финансовых операций excel файла"""
    try:
        pd_file = pd.read_excel(address)
        result = pd_file.fillna("").to_dict(orient="records")
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return f"Error: {e}"
    return result


def read_csv_file(address: str) -> Any:
    """Чтение финансовых операций csv файла"""
    transactions = []
    try:
        with open(address, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                transactions.append(dict(row))
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return f"Error: {e}"
    return transactions