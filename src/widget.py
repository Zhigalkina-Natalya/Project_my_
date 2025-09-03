from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_number: str) -> str:
    """
    Возвращает информацию о картах или счете с замаскированными номерами
    """
    if not type_number or str(type_number).lower() == "nan":
        return ""

    # Приводим к строке
    type_number = str(type_number)

    digits_type = "".join(filter(str.isdigit, type_number))
    if "счет" in type_number.lower():
        if len(digits_type) != 20:
            raise ValueError("Неверный номер счета")
        else:
            number_account = digits_type[-20:]
            return f"Счет {get_mask_account(number_account)}"
    else:
        if len(digits_type) != 16:
            raise ValueError("Неверный номер карты")
        else:
            number_card = digits_type[-16:]
            return f"{type_number[:-16]}{get_mask_card_number(number_card)}"


def get_date(date: str) -> str:
    """
    Функция возвращает дату в формате 'ДД.ММ.ГГГГ, из "2024-03-11T02:26:18.671407"
    """
    if not date:
        return ""

        # Разделяем строку по "T" и берем только часть с датой (до "T")
    if "T" in date:
        date_part = date.split("T")[0]
        # Разделяем дату на год, месяц, день
        year_month_day = date_part.split("-")
        return f"{year_month_day[2]}.{year_month_day[1]}.{year_month_day[0]}"
    else:
        raise IndexError("Неправильный формат даты")
