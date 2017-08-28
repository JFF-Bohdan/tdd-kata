import pytest

from work_classes.string_calculator import StringCalculator


def test_empty_string(mocker):
    mc = mocky_ret(mocker, [])

    task_string = ""
    assert StringCalculator.add(task_string) == 0

    mc.assert_called_once_with(task_string)


def test_one_value_sum(mocker):
    mc = mocky_ret(mocker, [1])

    task_string = "1"
    assert StringCalculator.add(task_string) == 1

    mc.assert_called_once_with(task_string)


def test_simple_input(mocker):
    mc = mocky_ret(mocker, [1, 2])

    task_string = "1,2"
    assert StringCalculator.add(task_string) == 3

    mc.assert_called_once_with(task_string)


def test_unknown_amount_of_numbers(mocker):
    mc = mocky_ret(mocker, [1, 2, 3, 4])

    task_string = "1,2, 3, 4   "
    assert StringCalculator.add(task_string) == 10

    mc.assert_called_once_with(task_string)


def test_exceptions_for_negative_number(mocker):
    mc = mocky_ret(mocker, [1, 2, -3])

    task_strins = "//;\n1;2;-3"
    with pytest.raises(Exception) as context:
        StringCalculator.add(task_strins)

        msg = str(context.exception)
        wrong_values = context.exception.wrong_data

        assert "negatives not allowed" in msg
        assert -3 in wrong_values

        mc.parse_input.assert_called_once_with(task_strins)


def test_exception_for_negative_numbers_list(mocker):
    mc = mocky_ret(mocker, [1, 2, -3, -4, -5])

    task_string = "//;\n1;2;-3;-4;-5"

    with pytest.raises(Exception) as context:
        StringCalculator.add(task_string)

        msg = str(context.exception)
        wrong_values = context.exception.wrong_data

        assert "negatives not allowed" in msg
        wrong_numbers = [-3, -4, -5]
        for value in wrong_numbers:
            assert value in wrong_values

        mc.assert_called_once_with(task_string)


def test_big_numbers_ignore(mocker):
    mc = mocky_ret(mocker, [1, 2, 3, 4, 1500, 2000, 1001])

    task_string = "1,2, 3, 4, 1500, 2000, 1001   "
    v = StringCalculator.add(task_string)
    assert v == 10

    mc.assert_called_once_with(task_string)


def mocky_ret(mocker, mocked_return_value):
    res = mocker.patch("work_classes.string_calculator.StringCalculatorInputParser.parse_input")
    res.return_value = mocked_return_value
    return res
