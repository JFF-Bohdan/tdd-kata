from work_classes.string_calculator import StringCalculatorInputParser


def test_simple_issues():
    values = combine_yield_into_array(StringCalculatorInputParser.parse_input("1,2"))
    assert ["1", "2"] == values


def test_crlf_in_command():
    values = combine_yield_into_array(StringCalculatorInputParser.parse_input("1\n2,3"))
    assert ["1", "2", "3"] == values


def test_crlf_and_non_std_separator():
    values = combine_yield_into_array(StringCalculatorInputParser.parse_input("//;\n1;2;4;6"))
    assert ["1", "2", "4", "6"] == values


def test_negative_values_parsing():
    values = combine_yield_into_array(StringCalculatorInputParser.parse_input("//;\n1;2;4;6;-10;-1005;1006;300"))
    assert ["1", "2", "4", "6", "-10", "-1005", "1006", "300"] == values


def test_long_separators():
    values = combine_yield_into_array(StringCalculatorInputParser.parse_input("//[***]\n1***2***3"))
    assert ["1", "2", "3"] == values


def test_multuple_separators_support():
    values = combine_yield_into_array(StringCalculatorInputParser.parse_input("//[*][%]\n1*2%3"))
    assert ["1", "2", "3"] == values


def test_multuple_long_separators_support():
    values = combine_yield_into_array(StringCalculatorInputParser.parse_input("//[&&*][%%@]\n1&&*2%%@3"))
    assert ["1", "2", "3"] == values


def combine_yield_into_array(iterator):
    return [v for v in iterator]
