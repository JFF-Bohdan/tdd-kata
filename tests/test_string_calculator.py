import pytest

from work_classes.string_calculator import StringCalculator


def test_empty_string(mocker):
    mc = mocky_ret(mocker, [])

    assert StringCalculator.Add("") == 0

    mc.assert_called_once_with("")


def test_one_value_sum(mocker):
    mc = mocky_ret(mocker, [1])
    assert StringCalculator.Add("1") == 1

    mc.assert_called_once_with("1")


def test_simple_input(mocker):
    mc = mocky_ret(mocker, [1, 2])
    assert StringCalculator.Add("1,2") == 3

    mc.assert_called_once_with("1,2")


def test_unknown_amount_of_numbers(mocker):
    mc = mocky_ret(mocker, [1, 2, 3, 4])
    assert StringCalculator.Add("1,2, 3, 4   ") == 10

    mc.assert_called_once_with("1,2, 3, 4   ")


def test_exceptions_for_negative_number(mocker):
    mc = mocky_ret(mocker, [1, 2, -3])

    with pytest.raises(Exception) as context:
        StringCalculator.Add("//;\n1;2;-3")

        msg = str(context.exception)
        wrong_values = context.exception.wrong_data

        assert "negatives not allowed" in msg
        assert -3 in wrong_values

        mc.parse_input.assert_called_once_with("//;\n1;2;-3")


def test_exception_for_negative_numbers_list(mocker):
    mc = mocky_ret(mocker, [1, 2, -3, -4, -5])

    wrong_command = "//;\n1;2;-3;-4;-5"

    with pytest.raises(Exception) as context:
        StringCalculator.Add(wrong_command)

        msg = str(context.exception)
        wrong_values = context.exception.wrong_data

        assert "negatives not allowed" in msg
        wrong_numbers = [-3, -4, -5]
        for value in wrong_numbers:
            assert value in wrong_values

        mc.assert_called_once_with(wrong_command)


def test_big_numbers_ignore(mocker):
    mc = mocky_ret(mocker, [1, 2, 3, 4, 1500, 2000, 1001])

    v = StringCalculator.Add("1,2, 3, 4, 1500, 2000, 1001   ")
    assert v == 10

    mc.assert_called_once_with("1,2, 3, 4, 1500, 2000, 1001   ")


def mocky_ret(mocker, mocked_return_value):
    res =  mocker.patch("work_classes.string_calculator.StringCalculatorInputParser.parse_input")
    res.return_value = mocked_return_value
    return res
