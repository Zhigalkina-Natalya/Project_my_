import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number",
    [
        ("111122223333"),
        ("1111222233334"),
        ("111122223333444"),
        ("11112222333344445"),
        ("11112222333344445555"),
    ],
)
def test_get_mask_card_number_invalid(card_number: str) -> None:
    """Тест на некорректные номера карт"""
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


def test_get_mask_card_number_wrong_type() -> None:
    """Тест на тип данных"""
    with pytest.raises(TypeError):
        get_mask_card_number([])


def test_get_mask_card_number(card_number: str) -> str:
    """Тест на корректные номера карт"""
    assert get_mask_card_number(card_number) == "1111 22** **** 4444"


def test_get_mask_card_number_symbol(card_number_symbol: str) -> str:
    """Тест на некорректные номера карт с разными символами и пробелами"""
    assert get_mask_card_number(card_number_symbol) == "1111 22** **** 4444"


@pytest.mark.parametrize("card_number, expected", [(" 1111 2222 33334444", "1111 22** **** 4444"), ("", "")])
def test_get_mask_card_empty_and_gap(card_number: str, expected: str) -> str:
    """Тест на пустую строку"""
    assert get_mask_card_number(card_number) == expected


def test_get_mask_account() -> str:
    """Тест на корректный номер счета"""
    assert "**5555"


@pytest.mark.parametrize("account_number, expected", [(" 11112222333344445555*", "**5555"), ("", "")])
def test_get_mask_account_(account_number: str, expected: str) -> str:
    """Тест на пустую строку и некорректные номера с пробелами и постаренними символами"""
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize(
    "account_number", [(" 11112222*3333/4444-"), ("111122223333444455556"), ("1111222233334444555567")]
)
def test_get_mask_account_invalid(account_number: str) -> None:
    """Тест на некорректные номера счета, количество символов"""
    with pytest.raises(ValueError):
        get_mask_account(account_number)


def test_get_mask_account_wrong_type() -> str:
    """Тест на тип данных"""
    with pytest.raises(TypeError):
        get_mask_account([1223456789])
