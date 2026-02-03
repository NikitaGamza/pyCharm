def mask_account_card(acc_info: str) -> str:
    if acc_info[0:7] == "Maestro":
        slice_type = "Maestro"
        slice_1 = acc_info[8:12]
        slice_2 = acc_info[12:14]
        slice_2 = slice_2 + '**'
        slice_3 = '****'
        slice_4 = acc_info[20:24]
        return f"{slice_type} {slice_1} {slice_2} {slice_3} {slice_4}"
    elif acc_info[0:10] == "MasterCard":
        slice_type = "MasterCard"
        slice_1 = acc_info[11:15]
        slice_2 = acc_info[15:17]
        slice_2 = slice_2 + '**'
        slice_3 = '****'
        slice_4 = acc_info[23:]
        return f"{slice_type} {slice_1} {slice_2} {slice_3} {slice_4}"
    elif acc_info[0:12] == "Visa Classic":
        return acc_info[13:]
    elif acc_info[0:13] == "Visa Platinum":
        return acc_info[14:]
    elif acc_info[0:9] == "Visa Gold":
        return acc_info[10:]
    else:
        return f"Счет **{acc_info[-4:]}"

def get_date(date_old: str) -> str:
    slice_year = date_old[0:4]
    slice_month = date_old[5:7]
    slice_day = date_old[8:10]
    return f"{slice_day}.{slice_month}.{slice_year}"