import pytest

from src.process_bank import process_bank_operations, process_bank_search


@pytest.fixture
def data_():
    return [
        {'description': 'Income'},
        {'description': 'Bill'},
        {'description': 'Income'},
        {'description': 'Credit'},
        {'description': 'Payment'},
        {'description': 'Transfer'},
        {'description': 'Payment'},
    ]

@pytest.mark.parametrize(
    "categories, categories_num",
    [
        (['Income', 'Bill', 'Credit'], {'Income': 2, 'Bill': 1, 'Credit': 1}),
        (['Groceries', 'Travel'], {}),
        ([], {}),
        ],
)

def test_process_bank_operations(data_, categories, categories_num):
    result = process_bank_operations(data_, categories)
    assert result == categories_num


def test_empty_transactions_list():
    data = []
    categories = ['Income', 'Bill']
    result = process_bank_operations(data, categories)
    assert result == {}

@pytest.mark.parametrize(
    "description_word, data_frm",
    [
       ("Payment", [{'description': 'Payment to Jane'},{'description': 'Payment to John'}]),
       ("payment", [{'description': 'Payment to Jane'},{'description': 'Payment to John'}]),
       ("Groceries", []),
       ([], []),
    ],
)
def test_process_bank_search(data_, description_word, data_frm):
    result = process_bank_search(data_, description_word)
    assert result == data_frm