from src.masks import get_mask_card_number

def test_get_mask_card_number(mask_card, is_none):
    assert get_mask_card_number(1234) == is_none
    assert get_mask_card_number(12345678901234565) == is_none
    assert get_mask_card_number(1234567890123456) == mask_card