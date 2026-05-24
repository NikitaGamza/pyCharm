from src.reading_files import read_csv_file, read_excel_file
from src.utils import info_bank_operations
import os

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
PATH_TO_FILE_JSON = os.path.join(ROOT_DIR, "data", "operations.json")
PATH_TO_FILE_XLSX = os.path.join(ROOT_DIR, "data", "transactions_excel.xlsx")
PATH_TO_FILE_CSV = os.path.join(ROOT_DIR, "data", "transactions.csv")

def start():
    print("""Программа: Привет! Добро пожаловать в программу работы
            с банковскими транзакциями.
            Выберите необходимый пункт меню:
            1. Получить информацию о транзакциях из JSON-файла
            2. Получить информацию о транзакциях из CSV-файла
            3. Получить информацию о транзакциях из XLSX-файла""")
    file_choice = int(input())
    # if not isinstance(file_choice, int):
    #     print("Некорректный ввод")
    if file_choice == 1:
        result = info_bank_operations(PATH_TO_FILE_JSON)
        print(result)
        return result
    elif file_choice == 2:
        result = read_csv_file(PATH_TO_FILE_CSV)
        print(result)
        return result
    elif file_choice == 3:
        result = read_excel_file(PATH_TO_FILE_XLSX)
        print(result)
        return result
    else:
        print("Неверный ввод")
    return 'end'

start()