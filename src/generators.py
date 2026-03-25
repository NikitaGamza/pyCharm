from typing import Any, Dict, Generator, List


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Generator:
    """Генератор фильтрации по заданной валюте"""
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Generator:
    """Генератор вывода описания транзакции"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Any:
    """Генератор номеров карт"""
    if start > end:
        return "Некорректные данные"
    while start <= end:
        generate = str(start).zfill(16)
        slice1 = generate[:4]
        slice2 = generate[4:8]
        slice3 = generate[8:12]
        slice4 = generate[12:]
        yield f"{slice1} {slice2} {slice3} {slice4}"
        start += 1
    return None