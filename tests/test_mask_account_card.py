from src.widget import mask_account_card

def test_mask_account_card(mask_account_card_1, mask_account_card_2, mask_account_card_3, is_none):
    assert mask_account_card("Счет 22222222222222221234") == mask_account_card_1
    assert mask_account_card("Maestro 1234567890123456") == mask_account_card_2
    assert mask_account_card("MasterCard 1234567890123456") == mask_account_card_3
    assert mask_account_card("MasterCard 123467890123456") == is_none
    assert mask_account_card("Счет 2222222222222221234") == is_none