import re
import unittest
from unittest.mock import patch


class StringCalculatorInputParser(object):
    def __init__(self):
        pass

    @staticmethod
    def parse_delimiters(delims):
        """
        Parses delimiters list. Able to parse delimiters list for
        "[ABC][DEF][QPP]" -> ["ABC", "DEF", "QPP"]
        :param delims: string with delimiters
        :return: delimiters array
        """
        d = re.findall("\[(.*?)\]", delims)
        if len(d) == 0:
            return [delims]

        return d

    @staticmethod
    def get_tasks(commands):
        """
        Returns tasks and delimiters from input

        :param commands: string with delimiters and takss
        :return: tupple of delimiters, tasks
        """
        default_delimiters = ["\n", ","]

        index = commands.find("//")
        if index != 0:
            return default_delimiters, commands

        delimiters_query = None
        index = commands.find("\n")
        if index != -1:
            delimiters_query = commands[2:index]
            commands = commands[index + 1:]

        if delimiters_query is not None:
            delimiters_query = StringCalculatorInputParser.parse_delimiters(delimiters_query)

        if delimiters_query is None:
            delimiters_query = default_delimiters

        return delimiters_query, commands

    @staticmethod
    def parse_input(commands):
        """
        Parses input and yields values to process
        :param commands: string with delimiters and tasks
        :return: yields values for processing
        """
        possible_separators, data = StringCalculatorInputParser.get_tasks(commands)
        items = [data]

        for separator in possible_separators:
            iteration_items = []

            for item in items:
                iteration_items.extend([str(x).strip() for x in item.split(separator) if len(str(x)) > 0])

            items = iteration_items

        for item in items:
            yield item


class StringCalculator:
    def __init__(self):
        pass

    @staticmethod
    def Add(commands):
        """
        Calculates sum of tasks with delimiters according to rules
        :param commands: string with delimiters and tasks
        :return: result sum
        """
        res = 0

        wrong_numbers = []

        for v in StringCalculatorInputParser.parse_input(commands):
            v = str(v).strip()
            if not len(v):
                continue

            v = int(v)
            if v < 0:
                wrong_numbers.append(v)
                continue

            if v > 1000:
                continue

            res += int(v)

        if wrong_numbers:
            e = Exception("negatives not allowed")
            e.wrong_data = wrong_numbers
            raise e

        return res


class TestStringParser(unittest.TestCase):
    def _combine_yield_into_array(self, iterator):
        res = []
        for v in iterator:
            res.append(v)

        return res

    def test_simple_issues(self):
        values = self._combine_yield_into_array(StringCalculatorInputParser.parse_input("1,2"))
        self.assertEqual(["1", "2"], values)

    def test_crlf_in_command(self):
        values = self._combine_yield_into_array(StringCalculatorInputParser.parse_input("1\n2,3"))
        self.assertEqual(["1", "2", "3"], values)

    def test_crlf_and_non_std_separator(self):
        values = self._combine_yield_into_array(StringCalculatorInputParser.parse_input("//;\n1;2;4;6"))
        self.assertEqual(["1", "2", "4", "6"], values)

    def test_negative_values_parsing(self):
        values = self._combine_yield_into_array(StringCalculatorInputParser.parse_input("//;\n1;2;4;6;-10;-1005;1006;300"))
        self.assertEqual(["1", "2", "4", "6", "-10", "-1005", "1006", "300"], values)

    def test_long_separators(self):
        values = self._combine_yield_into_array(StringCalculatorInputParser.parse_input("//[***]\n1***2***3"))
        self.assertEqual(["1", "2", "3"], values)

    def test_multuple_separators_support(self):
        values = self._combine_yield_into_array(StringCalculatorInputParser.parse_input("//[*][%]\n1*2%3"))
        self.assertEqual(["1", "2", "3"], values)

    def test_multuple_long_separators_support(self):
        values = self._combine_yield_into_array(StringCalculatorInputParser.parse_input("//[&&*][%%@]\n1&&*2%%@3"))
        self.assertEqual(["1", "2", "3"], values)


class TestStringCalculator(unittest.TestCase):

    def _mocky_ret(self):
        return patch("__main__.StringCalculatorInputParser")

    def test_empty_string(self):
        with self._mocky_ret() as mc:
            mc.parse_input.return_value = []
            self.assertEqual(StringCalculator.Add(""), 0)

    def test_one_value_sum(self):
        with self._mocky_ret() as mc:
            mc.parse_input.return_value = [1]
            self.assertEqual(StringCalculator.Add("1"), 1)

    def test_simple_input(self):
        with self._mocky_ret() as mc:
            mc.parse_input.return_value = [1, 2]
            self.assertEqual(StringCalculator.Add("1,2"), 3)

    def test_unknown_amount_of_numbers(self):
        with self._mocky_ret() as mc:
            mc.parse_input.return_value = [1, 2, 3, 4]
            self.assertEqual(StringCalculator.Add("1,2, 3, 4   "), 10)

    def test_exceptions_for_negative_number(self):
        with self._mocky_ret() as mc:
            mc.parse_input.return_value = [1, 2, -3]

            self.assertRaises(Exception, StringCalculator.Add, "//;\n1;2;-3")

            with self.assertRaises(Exception) as context:
                StringCalculator.Add("//;\n1;2;-3")

            msg = str(context.exception)
            wrong_values = context.exception.wrong_data

            self.assertTrue("negatives not allowed" in msg)
            self.assertTrue(-3 in wrong_values)

    def test_exception_for_negative_numbers_list(self):
        with self._mocky_ret() as mc:
            mc.parse_input.return_value = [1, 2, -3, -4, -5]

            wrong_command = "//;\n1;2;-3;-4;-5"

            with self.assertRaises(Exception) as context:
                StringCalculator.Add(wrong_command)

            msg = str(context.exception)
            wrong_values = context.exception.wrong_data

            self.assertTrue("negatives not allowed" in msg)
            wrong_numbers = [-3, -4, -5]
            for value in wrong_numbers:
                self.assertTrue(value in wrong_values)

    def test_big_numbers_ignore(self):
        with self._mocky_ret() as mc:
            mc.parse_input.return_value = [1, 2, 3, 4, 1500, 2000, 1001]

            v = StringCalculator.Add("1,2, 3, 4, 1500, 2000, 1001   ")
            self.assertEqual(v, 10)


if __name__ == "__main__":
    unittest.main()
