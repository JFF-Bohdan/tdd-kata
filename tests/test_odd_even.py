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


# "- Write a program that prints numbers within specified range lets say 1 to 100. If number is odd print 'Odd'
#   instead of the number. If number is even print 'Even' instead of number. Else print number [hint - if number is Prime]."

# "Lets divide into following steps:
# - Prints numbers from 1 to 100
# - Print "Even" instead of number, if the number is even, means divisible by 2
# - Print "Odd" instead of number, if the number is odd, means not divisible by 2 but not divisible by itself too [hint - it should not be Prime]
# - Print number, if it does not meet above two conditions, means if number is Prime
# - Make method to accept any number of range [currently  we have 1 to 100]
# - Create a new method to check Odd/Even/Prime of a single supplied method"