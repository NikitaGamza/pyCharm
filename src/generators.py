from typing import Any, Dict, List, Generator


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Generator:
    """Генератор фильтрации по заданной валюте"""
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Generator:
    for transaction in transactions:
        yield transaction["description"]