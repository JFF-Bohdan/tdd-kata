import pytest

from work_classes.prime_factor_game import PrimeFactorGame

PRIME_NUMBERS = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

COMPOSITE_NUMBERS = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36,
                     38, 39, 40, 42, 44, 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 60, 62, 63, 64, 65, 66,
                     68, 69, 70, 72, 74, 75, 76, 77, 78, 80, 81, 82, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95,
                     96, 98, 99, 100]


def test_raises_exception_when_zero_value_provided():
    with pytest.raises(Exception):
        PrimeFactorGame.play(0)


def test_raises_exception_when_less_than_zero_value_provided():
    with pytest.raises(Exception):
        PrimeFactorGame.play(-10)


def test_raises_exception_when_value_greater_than_100_provided():
    with pytest.raises(Exception):
        PrimeFactorGame.play(102)


def test_returns_string_prime_when_prime_number_provided():
    for v in PRIME_NUMBERS:
        assert PrimeFactorGame.play(v) == "prime"


def test_returns_string_composite_when_composite_number_provided():
    for v in COMPOSITE_NUMBERS:
        if v % 2 == 0:
            continue

        assert PrimeFactorGame.play(v) == "composite"


def test_returns_number_when_number_is_not_prime_and_composite():
    qty = 0
    for i in range(1, 101):
        if i in PRIME_NUMBERS:
            continue

        if (i % 2 != 0) and (i in COMPOSITE_NUMBERS):
            continue

        assert PrimeFactorGame.play(i) == str(i)
        qty += 1

    assert qty > 0


def test_full_game_support():
    res = PrimeFactorGame.game()
    for index, item in enumerate(res):
        assert PrimeFactorGame.play(index + 1) == item
