import pytest
from src.processing import filter_by_state, sort_by_date


def test_filter_state_default(list_of_dict):
    assert filter_by_state(list_of_dict) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}
    ]


@pytest.mark.parametrize("state, expected",
                         [("CANCELED", [{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                                        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}])
                          ])
def test_filter_state(list_of_dict, state, expected):
    assert filter_by_state(list_of_dict, state) == expected


def test_filter_state_not_exist(list_of_dict):
    assert filter_by_state(list_of_dict, "COMPLETED") == []


def test_filter_state_empty_list():
    assert filter_by_state([], "COMPLETED") == []


def test_sort_by_date_descending(list_of_dict):
    assert sort_by_date(list_of_dict) == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


@pytest.mark.parametrize("sorting, expected", [(
        False, [
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        ]
)])
def test_sort_by_date_ascending(list_of_dict, sorting, expected):
    assert sort_by_date(list_of_dict, sorting) == expected


def test_sort_by_date_empty_list():
    assert sort_by_date([]) == []


@pytest.mark.parametrize("date_not_format, sorting, expected", [([
                                                                     {"id": 11111111, "state": "EXECUTED",
                                                                      "date": "2019-07-03T18:35:29.512364"},
                                                                     {"id": 594226727, "state": "CANCELED",
                                                                      "date": "2018-09-12T21:27:25.241689"}],
                                                                 False, [
                                                                     {'id': 594226727, 'state': 'CANCELED',
                                                                      'date': '2018-09-12T21:27:25.241689'},
                                                                     {"id": 11111111, "state": "EXECUTED",
                                                                      "date": "2019-07-03T18:35:29.512364"}]
)])
def test_sort_by_date_no_date(date_not_format, sorting, expected):
    assert sort_by_date(date_not_format, sorting) == expected


def test_sort_by_date_wrong_type():
    with pytest.raises(TypeError):
        sort_by_date("")


def test_sort_by_date_invalid():
    with pytest.raises(KeyError):
        sort_by_date([{"id": 594226727, "state": "CANCELED"}])
