from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card
from src.generators import card_number_generator

# get_mask_card_number(2222222222222222)
# get_mask_account(22222222222222221234)
# print(mask_account_card("Maestro 7158300734726758"))
# print(get_date("2024-03-11T02:26:18.671407"))
# print(
#     filter_by_state(
#         [
#             {"id": 414288290, "state": "CANCELLED", "date": "2019-07-03T18:35:29.512364"},
#             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#         ],
#         state="CANCELLED",
#     )
# )
# print(
#     sort_by_date(
#         [
#             {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         ],
#         reverse=True,
#     )
# )


new_card = card_number_generator(10003, 10001)
print(next(new_card))
print(next(new_card))
print(next(new_card))