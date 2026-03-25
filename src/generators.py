from typing import Any, Dict, Generator, List


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Generator:
    """Генератор фильтрации по заданной валюте"""
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Generator:
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Any:
    if start > end:
        return "Некорректные данные"
    else:
        for i in range(start, end):
            yield str(i)
