import json
import logging
import os
from typing import Any, Dict, List

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
# создаём FileHandler (перезаписываем лог при каждом запуске)
file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
# создаём Formatter
file_formatter = logging.Formatter("%(asctime)s: %(name)s: %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
# добавляем Handler к логгеру
logger.addHandler(file_handler)


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Функция, принимающая на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Функция возвращает пустой список, если:
     - файл не найден,
     - файл пуст,
     - файл содержит не список,
     - при чтении файла произошла ошибка.
    """

    if not os.path.exists(file_path):
        logger.warning("Файл не существует")
        return []

    if os.path.getsize(file_path) == 0:
        logger.info("Файл пуст")
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:

            data = json.load(file)

        if not isinstance(data, list):
            logger.info("В файле нет списка")
            return []  # Возвращаем пустой список, если это не список

        logger.info("Список транзакций успешно получен")
        return data  # Если это список, возвращаем его

    except OSError as err:
        logger.error(f"Ошибка при работе с файлом {err}")
        return []

    except json.JSONDecodeError as err:
        logger.error(f"Ошибка при чтении JSON: {err}")
        return []


# if __name__ == "__main__":
# # Автоматически определяем путь до operations.json в папке data
#    current_dir = os.path.dirname(os.path.abspath(__file__))
#    json_path = os.path.join(current_dir, "..", "data", "operations.json")
#    json_path = os.path.normpath(json_path)  # приведение пути к нормальному виду
#
#    transactions = load_transactions(json_path)
#    print(transactions)
