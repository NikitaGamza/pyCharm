from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card

get_mask_card_number(2222222222222222)
get_mask_account(22222222222222221234)
print(mask_account_card("Maestro 7158300734726758"))
print(get_date("2024-03-11T02:26:18.671407"))
