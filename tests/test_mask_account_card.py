from src.widget import mask_account_card

def test_mask_account_card():
    assert mask_account_card("Счет 22222222222222221234") == "Счет **1234"
    assert mask_account_card("Maestro 1234567890123456") == "Maestro 1234 56** **** 3456"
    assert mask_account_card("MasterCard 1234567890123456") == "MasterCard 1234 56** **** 3456"
    assert mask_account_card("MasterCard 123467890123456") is None
    assert mask_account_card("Счет 2222222222222221234") is None