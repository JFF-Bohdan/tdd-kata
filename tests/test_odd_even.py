import random

import pytest


from work_classes.odd_even import OddEvenGame


def test_raises_exception_when_zero_provided():
    with pytest.raises(Exception):
        OddEvenGame.play(0)


def test_raises_exception_when_less_than_zero_provided():
    with pytest.raises(Exception):
        OddEvenGame.play(-10)


def test_raises_exception_when_more_than_100_provided():
    with pytest.raises(Exception):
        OddEvenGame.play(101)


def test_returns_odd_when_odd_number_prodided():
    value = random.choice([1, 3, 5, 7])

    assert OddEvenGame.play(value) == "odd"


def test_returns_even_when_even_number_provided():
    value = random.choice([2, 4, 8, 12])

    assert OddEvenGame.play(value) == "even"


def test_full_game_results():
    res = OddEvenGame.game()
    assert len(res) == 100

    for index, item in enumerate(res):
        assert OddEvenGame.play(index + 1) == item
