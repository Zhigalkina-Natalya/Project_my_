def filter_by_state(list_of_dict: list[dict], state: str="EXECUTED") -> list[dict]:
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
