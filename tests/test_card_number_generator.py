from src.generators import card_number_generator

def test_card_number_generator(card_list, empty_arr):
    result1 = list(card_number_generator(start=9999, end=10001))
    assert result1 == card_list
    result2 = list(card_number_generator(start=10002, end=10001))
    assert result2 == empty_arr