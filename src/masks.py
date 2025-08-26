import logging

# Настройка логера для модуля masks
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
# FileHandler — перезаписываем файл при каждом запуске
file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
# Формат логов: время, модуль, уровень, сообщение
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
# добавляем Handler к логгеру
logger.addHandler(file_handler)


def get_mask_card_number(number_card: str) -> str:
    """
    Возвращает маску номера карты, в формате где видны только
    первые 6 и последние 4 цифры, остальные символы отображаются звездочками,
    номер разбит по блокам 4 цифры, разделенным пробелами.
    """
    if not isinstance(number_card, str):
        logger.error("Передан неверный тип данных для карты: %s", type(number_card))
        raise TypeError("Ошибка типа данных")

    digits_card = "".join(filter(str.isdigit, number_card))

    if len(digits_card) == 16:
        masked = f"{digits_card[0:4]} {digits_card[4:6]}** **** {digits_card[-4:]}"
        logger.info("Успешно замаскирован номер карты")
        return masked

    elif 0 < len(digits_card) < 16 or len(digits_card) > 16:
        logger.error("Неверный номер карты: %s", number_card)
        raise ValueError("Ошибка: Неверный номер карты")

    logger.debug("Передана пустая строка для маскировки карты")
    return ""


def get_mask_account(number_account: str) -> str:
    """Возвращает замаскированный номер счета, где видны только последние
    4 цифры, а перед ними две звездочки
    """
    if not isinstance(number_account, str):
        logger.error("Передан неверный тип данных для счета: %s", type(number_account))
        raise TypeError("Ошибка типа данных")

    digits_account = "".join(filter(str.isdigit, number_account))

    if 0 < len(digits_account) < 20 or len(digits_account) > 20:
        logger.error("Неверный номер счета: %s", number_account)
        raise ValueError("Неверный номер счета")

    if len(digits_account) == 20:
        logger.info("Успешно замаскирован номер счета")
        return f"**{digits_account[-4:]}"
    logger.debug("Передана пустая строка для маскировки счета")
    return ""

# if __name__ == '__main__':
#     get_mask_card_number("1111-2222-3333-4444")
#     get_mask_card_number("")
#
#     get_mask_account("")
#     get_mask_account("1111 2222 3333 4444 5555")
#     get_mask_account("c1111-2222333344445555")
#     get_mask_account("1111222233334444")
