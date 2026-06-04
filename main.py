import os
from typing import Any

from src.generators import filter_by_currency
from src.process_bank import process_bank_search
from src.processing import filter_by_state, sort_by_date
from src.reading_files import read_csv_file, read_excel_file
from src.utils import info_bank_operations
from src.widget import get_date, mask_account_card

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
PATH_TO_FILE_JSON = os.path.join(ROOT_DIR, "HomeWork9and1", "data", "operations.json")
PATH_TO_FILE_XLSX = os.path.join(ROOT_DIR, "HomeWork9and1", "data", "transactions_excel.xlsx")
PATH_TO_FILE_CSV = os.path.join(ROOT_DIR, "HomeWork9and1", "data", "transactions.csv")


def choice() -> Any:
    """Функция выбора файла для чтения"""
    print("""Программа: Привет! Добро пожаловать в программу работы
                с банковскими транзакциями.
                Выберите необходимый пункт меню:
                1. Получить информацию о транзакциях из JSON-файла
                2. Получить информацию о транзакциях из CSV-файла
                3. Получить информацию о транзакциях из XLSX-файла""")
    file_choice = 0
    while file_choice != 1 and file_choice != 2 and file_choice != 3:
        file_choice = int(input())
        if file_choice == 1:
            result = info_bank_operations(PATH_TO_FILE_JSON)
            print("Программа: Для обработки выбран JSON-файл.")
            return result
        elif file_choice == 2:
            result = read_csv_file(PATH_TO_FILE_CSV)
            print("Программа: Для обработки выбран CSV-файл.")
            return result
        elif file_choice == 3:
            result = read_excel_file(PATH_TO_FILE_XLSX)
            print("Программа: Для обработки выбран XLSX-файл.")
            return result
        else:
            print("Неверный ввод")
    return []


def start() -> Any:
    """Главная точка входа
    Выбирает файл с транзакциями.
    Фильтрует по статусу, валюте и слову в описании транзакции
    Сортирует по дате"""
    result = choice()
    print("""Введите статус, по которому необходимо выполнить фильтрацию.
            Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
    state_choice = ""
    while state_choice != "EXECUTED" and state_choice != "CANCELED" and state_choice != "PENDING":
        state_choice = input().upper()
        if state_choice != "EXECUTED" and state_choice != "CANCELED" and state_choice != "PENDING":
            print(f'Статус операции "{state_choice}" недоступен.')
            print("""Введите статус, по которому необходимо выполнить фильтрацию.
                Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
                """)
        else:
            result = filter_by_state(result, state_choice)

    print("Отсортировать операции по дате? Да/Нет")
    sort_choice = ""
    while sort_choice != "ДА" and sort_choice != "НЕТ":
        sort_choice = input().upper()
        if sort_choice != "ДА" and sort_choice != "НЕТ":
            print("Некорректный ввод")
    if sort_choice == "ДА":
        print("Отсортировать по возрастанию или по убыванию?")
        sort_seq = ""
        while sort_seq != "ПО ВОЗРАСТАНИЮ" and sort_seq != "ПО УБЫВАНИЮ":
            sort_seq = input().upper()
            if sort_seq != "ПО ВОЗРАСТАНИЮ" and sort_seq != "ПО УБЫВАНИЮ":
                print("Некорректный ввод")
        if sort_choice == "ДА" and sort_seq == "ПО УБЫВАНИЮ":
            result = sort_by_date(result, True)
        else:
            result = sort_by_date(result, False)

    print("Выводить только рублевые транзакции? Да/Нет")
    value_choice = ""
    while value_choice != "ДА" and value_choice != "НЕТ":
        value_choice = input().upper()
        if value_choice != "ДА" and value_choice != "НЕТ":
            print("Некорректный ввод")

    if value_choice == "ДА":
        result = list(filter_by_currency(result, "RUB"))
    else:
        pass

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    word_choice = ""
    while word_choice != "ДА" and word_choice != "НЕТ":
        word_choice = input().upper()
        if word_choice != "ДА" and word_choice != "НЕТ":
            print("Некорректный ввод")
    if word_choice == "ДА":
        print("Введите слово")
        word_pattern = input()
        result = process_bank_search(result, word_pattern)

    if len(result) > 0:
        print(f"Всего банковских операций в выборке: {len(result)}")
        # print(*result, sep="\n")
        for res in result:
            print(f"{get_date(res['date'])} {res['description']}")
            if "from" in res and "to" in res:
                print(f"{mask_account_card(res['from'])} -> {mask_account_card(res['to'])}")
            elif "from" in res:
                print(f"{mask_account_card(res['from'])}")
            elif "to" in res:
                print(f"{mask_account_card(res['to'])}")
            print(f"Сумма: {res['operationAmount']['amount']} {res['operationAmount']['currency']['name']} \n")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    return result


start()
