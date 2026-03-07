from src.masks import get_mask_account

def test_get_mask_account(mask_account, is_none):
    assert get_mask_account(2222222222222221234) == is_none
    assert get_mask_account(222222222222222221234) == is_none
    assert get_mask_account(22222222222222221234) == mask_account