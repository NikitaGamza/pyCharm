import logging

from black.comments import Union

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/masks.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(cart_number: int) -> Union[str, None]:
    """Функция маскировки карты"""
    logger.debug("Попытка маскировки карты")
    if len(str(cart_number)) < 16 or len(str(cart_number)) > 16:
        print("Некорректный ввод")
        logger.error("Некорректный ввод")
        return None
    else:
        cart_str = str(cart_number)
        sliced_1 = cart_str[0:4]
        sliced_2 = cart_str[4:6]
        sliced_2 = sliced_2 + "**"
        sliced_3 = "****"
        sliced_4 = cart_str[12:]
        logger.info(f"Замаскированная карта: {sliced_1} {sliced_2} {sliced_3} {sliced_4}")
        return f"{sliced_1} {sliced_2} {sliced_3} {sliced_4}"


def get_mask_account(acc_number: int) -> Union[str, None]:
    """Функция маскировки аккаунта"""
    logger.debug("Попытка маскировки аккаунта")
    if len(str(acc_number)) < 20 or len(str(acc_number)) > 20:
        print("Некорректный ввод")
        logger.error("Некорректный ввод")
        return None
    else:
        acc_str = str(acc_number)
        sliced = acc_str[-4:]
        logger.info(f"Замаскированный аккаунт: {sliced}")
        return f"**{sliced}"
