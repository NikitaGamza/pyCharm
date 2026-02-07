from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(acc_info: str) -> str:
    if acc_info[0:4] == "Счет":
        slice_num = int(acc_info[5:])
        masked = get_mask_account(slice_num)
        return f"Счет {masked}"
    else:
        slice_num = int(acc_info[-16:])
        masked = get_mask_card_number(slice_num)
        return f"{acc_info[0:-16]}{masked}"


def get_date(date_old: str) -> str:
    slice_year = date_old[0:4]
    slice_month = date_old[5:7]
    slice_day = date_old[8:10]
    return f"{slice_day}.{slice_month}.{slice_year}"
