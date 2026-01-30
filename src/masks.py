from black.comments import Union


def get_mask_card_number(cart_number: int) -> Union[str, None]:
    """Функция маскировки карты"""
    if len(str(cart_number)) < 16 or len(str(cart_number)) > 16:
        print("Некорректный ввод")
        return None
    else:
        cart_str = str(cart_number)
        sliced_1 = cart_str[0:4]
        sliced_2 = cart_str[4:6]
        sliced_2 = sliced_2 + "**"
        sliced_3 = "****"
        sliced_4 = cart_str[8:12]
        return f"{sliced_1} {sliced_2} {sliced_3} {sliced_4}"


def get_mask_account(acc_number: int) -> Union[str, None]:
    """Функция маскировки аккаунта"""
    if len(str(acc_number)) < 20 or len(str(acc_number)) > 20:
        print("Некорректный ввод")
        return None
    else:
        acc_str = str(acc_number)
        sliced = acc_str[-4:]
        return f"**{sliced}"
