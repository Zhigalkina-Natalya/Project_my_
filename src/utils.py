import json
import os
from typing import Any, Dict, List


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Функция, принимающая на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """

    if not os.path.exists(file_path):
        return []

    if os.path.getsize(file_path) == 0:
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            return []  # Возвращаем пустой список, если это не список

        return data  # Если это список, возвращаем его

    except (OSError, json.JSONDecodeError):
        return []


# if __name__ == "__main__":
# Автоматически определяем путь до operations.json в папке data
#    current_dir = os.path.dirname(os.path.abspath(__file__))
#    json_path = os.path.join(current_dir, "..", "data", "operations.json")
#    json_path = os.path.normpath(json_path)  # приведение пути к нормальному виду

#    transactions = load_transactions(json_path)
#    print(transactions)
