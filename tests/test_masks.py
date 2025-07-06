import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("card_number", [("111122223333"),
                                         ("1111222233334"),
                                         ("111122223333444"),
                                         ("11112222333344445"),
                                         ("11112222333344445555"), ])
def test_get_mask_card_number_invalid(card_number):
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


def test_get_mask_card_number_wrong_type():
    with pytest.raises(TypeError):
        get_mask_card_number([1111222233334444])


def test_get_mask_card_number(card_number):
    assert get_mask_card_number(card_number) == "1111 22** **** 4444"


def test_get_mask_card_number_symbol(card_number_symbol):
    assert get_mask_card_number(card_number_symbol) == "1111 22** **** 4444"


@pytest.mark.parametrize("card_number, expected", [(" 1111 2222 33334444", "1111 22** **** 4444"),
                                                   ("", "")])
def test_get_mask_card_empty_and_gap(card_number, expected):
    assert get_mask_card_number(card_number) == expected


def test_get_mask_account():
    assert "**5555"


@pytest.mark.parametrize("account_number, expected", [(" 11112222333344445555*", "**5555"),
                                                      ("", "")])
def test_get_mask_account_(account_number, expected):
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize("account_number", [(" 11112222*3333/4444-"),
                                            ("111122223333444455556"),
                                            ("111122223333444455556 ")])
def test_get_mask_account_invalid(account_number):
    with pytest.raises(ValueError):
        get_mask_account(account_number)


def test_get_mask_account_wrong_type():
    with pytest.raises(TypeError):
        get_mask_account([11112222333344445555])
