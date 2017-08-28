import random

import pytest

from work_classes.fizz_buzz import FizzBuzzImplementation


def test_multipliers_for_3_supported():
    v = FizzBuzzImplementation.play(random.choice([3, 6, 9, 12]))

    assert str(v).lower() == "fizz"


def test_multipliers_for_5_supported():
    v = FizzBuzzImplementation.play(random.choice([5, 10, 20, 25]))

    assert str(v).lower() == "buzz"


def test_multipliers_for_3_and_5_supported():
    v = FizzBuzzImplementation.play(random.choice([15, 30]))

    assert str(v).lower() == "fizzbuzz"


def test_returns_ints_converted_to_strings_when_not_3_and_not_5_multipliers():
    int_value = random.choice([2, 4, 7, 8])
    result = FizzBuzzImplementation.play(int_value)

    assert result == str(int_value)


def test_raises_exception_when_got_negative_value():
    with pytest.raises(Exception):
        FizzBuzzImplementation.play(-10)


def test_raises_exception_when_got_value_more_than_100():
    with pytest.raises(Exception):
        FizzBuzzImplementation.play(101)


def test_all_game_is_valud():
    res = FizzBuzzImplementation.game()

    assert len(res) == 100

    for index, item in enumerate(res):
        assert FizzBuzzImplementation.play(index+1) == item
