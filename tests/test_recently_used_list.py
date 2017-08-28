import pytest

from work_classes.recently_used_list import RecentlyUsedList


def test_returns_valid_length():
    ru = RecentlyUsedList(3)

    ru.insert("A")
    assert len(ru) == 1

    ru.insert("B")
    assert len(ru) == 2

    ru.insert("C")
    assert len(ru) == 3

    ru.insert("D")
    assert len(ru) == 3

    ru.insert("E")
    assert len(ru) == 3


def test_initialy_empty():
    ru = RecentlyUsedList(3)
    assert len(ru) == 0


def test_last_added_item_is_first():
    ru = RecentlyUsedList(3)

    ru.insert("A")
    assert len(ru) == 1

    assert ru[0] == "A"


def test_no_duplicates_allowed():
    ru = RecentlyUsedList(3)

    ru.insert("A")
    assert len(ru) == 1

    ru.insert("B")
    assert len(ru) == 2

    ru.insert("A")
    assert len(ru) == 2


def test_most_used_item_is_first():
    ru = RecentlyUsedList(3)

    ru.insert("A")
    assert len(ru) == 1

    ru.insert("B")
    assert len(ru) == 2

    ru.insert("A")
    assert len(ru) == 2

    assert ru[0] == "A"
    assert ru[1] == "B"


def test_raises_exception_when_adding_none():
    ru = RecentlyUsedList(3)

    ru.insert("A")
    assert len(ru) == 1

    with pytest.raises(Exception):
        ru.insert(None)

    assert len(ru) == 1


def test_raises_exception_when_adding_empty_string():
    ru = RecentlyUsedList(3)

    ru.insert("A")
    assert len(ru) == 1

    with pytest.raises(Exception):
        ru.insert("")

    assert len(ru) == 1


def test_raises_exception_on_negative_index():
    ru = RecentlyUsedList(3)

    ru.insert("A")
    assert len(ru) == 1

    with pytest.raises(IndexError):
        ru[-1]

    assert len(ru) == 1


def test_non_sizeable_lists_supported():
    ru = RecentlyUsedList(None)

    needful_size = 100
    for i in range(needful_size):
        ru.insert(str(i))
        assert len(ru) == (i + 1)

    assert len(ru) == needful_size
