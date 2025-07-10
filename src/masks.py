def get_mask_card_number(number_card: str) -> str:
    """
    Возвращает маску номера карты, в формате где видны только
    первые 6 и последние 4 цифры, остальные символы отображаются звездочками,
    номер разбит по блокам 4 цифры, разделенным пробелами.
    """
    if not isinstance(number_card, str):
        raise TypeError("Ошибка типа данных")

    digits_card = "".join(filter(str.isdigit, number_card))

    if len(digits_card) == 16:
        return f"{digits_card[0:4]} {digits_card[4:6]}** **** {digits_card[-4:]}"
    elif 0 < len(digits_card) < 16 or len(digits_card) > 16:
        raise ValueError("Ошибка: Неверный номер карты")
    return ""


def get_mask_account(number_account: str) -> str:
    """Возвращает замаскированный номер счета, где видны только последние
    4 цифры, а перед ними две звездочки
    """
    if not isinstance(number_account, str):
        raise TypeError("Ошибка типа данных")

    digits_account = "".join(filter(str.isdigit, number_account))

    if 0 < len(digits_account) < 20 or len(digits_account) > 20:
        raise ValueError("Неправильный номер счета")

    if len(digits_account) == 20:
        return f"**{digits_account[-4:]}"
    return ""
