from isort.core import process

from src.widget import get_date


def filter_by_state(list_of_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция возвращает новый список словарей, содержащий словари, у которых ключ state
    соответствует указанному значению
    """
    new_list = []
    for i in list_of_dict:
        if i.get("state") == state:
            new_list.append(i)
        else:
            continue
    return new_list


def sort_by_date(list_of_dict: list[dict], sorting: bool = True) -> list[dict]:
    """
    Функция возвращает новый список словарей, отсортированный по дате
    """
    if not isinstance(list_of_dict, list):
        raise TypeError("Ожидается список словарей")

    # Проверяем наличие ключа date
    processed = []
    for idx, transaction in enumerate(list_of_dict):
        if "date" not in transaction:
            raise KeyError(f"Словарь №{idx} не содержит ключа 'date'")

        try:
            dt = get_date(transaction['date'])
            processed.append((dt, transaction))
        except ValueError as e:
            raise ValueError(f"Ошибка в словаре №{idx}: {str(e)}")

    processed.sort(key=lambda x: x[0], reverse=sorting)
    list_interval = [i[1] for i in processed]
    list_sorted = sorted(list_interval, key=lambda x: x["date"], reverse=sorting)
    return list_sorted
