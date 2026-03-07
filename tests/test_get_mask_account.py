from src.masks import get_mask_account

def test_get_mask_account():
    assert get_mask_account(2222222222222221234) is None
    assert get_mask_account(222222222222222221234) is None
    assert get_mask_account(22222222222222221234) == "**1234"